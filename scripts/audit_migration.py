#!/usr/bin/env python3
"""Audit the committed Starlight source against the published GitBook space."""

from __future__ import annotations

import argparse
from collections import Counter
import concurrent.futures
import html
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path, PurePosixPath
import re
import sys
import xml.etree.ElementTree as ET
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin
from urllib.request import Request, urlopen

from import_gitbook import (
    DOCS,
    ROOT,
    SOURCE,
    external_asset_key,
    fetch_text,
    page_path,
    page_title,
    sidebar_data,
    starlight_page,
    original_asset_url,
    transform_gitbook,
    transform_links,
    visible_image_targets,
)


def duplicate_overview_groups(
    items: list[dict[str, object]], path: tuple[str, ...] = ()
) -> list[str]:
    duplicates: list[str] = []
    for item in items:
        label = str(item.get("label", ""))
        current_path = (*path, label)
        children = item.get("items")
        if not isinstance(children, list):
            continue
        overview_count = sum(
            isinstance(child, dict) and child.get("label") == "Overview" for child in children
        )
        if overview_count > 1:
            duplicates.append(" > ".join(current_path))
        duplicates.extend(duplicate_overview_groups(children, current_path))
    return duplicates


MARKDOWN_URL = re.compile(r"https://fulstech\.gitbook\.io/docs/[^)\s]+\.md")
NEXT_LLMS_PAGE = re.compile(r"\[Next Page\]\(([^)]+)\)")
ASSET_PATH = re.compile(r"(?:(?:\.\./)*)assets/([A-Za-z0-9_-]+)(?:\.[A-Za-z0-9]+)")
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
URL = re.compile(r"https?://[^\s)\]>\"]+")
REMOTE_MARKDOWN_IMAGE = re.compile(
    r"(?P<prefix>!\[[^]]*\]\()(?P<url>https?://[^)\s]+)(?P<suffix>[^)]*\))"
)
GITBOOK_BLOCK = re.compile(
    r"{%\s+(hint|endhint|tabs|endtabs|tab|endtab|embed|endembed|content-ref|endcontent-ref)\b"
)


def normalize_markdown(value: str) -> str:
    def replace_remote(match: re.Match[str]) -> str:
        target = match.group("url")
        normalized = original_asset_url(target.replace("\\&", "&"))
        if "gitbook.io" in target and "~gitbook/image" in target:
            key = "remote-" + hashlib.sha256(normalized.encode()).hexdigest()[:16]
        else:
            key = external_asset_key(normalized)
        return match.group("prefix") + f"/files/{key}" + match.group("suffix")

    value = REMOTE_MARKDOWN_IMAGE.sub(replace_remote, value)
    value = ASSET_PATH.sub(lambda match: f"/files/{match.group(1)}", value)
    value = "\n".join(line.rstrip() for line in value.splitlines()).strip() + "\n"
    return re.sub(r"\n{3,}", "\n\n", value)


def split_fenced_markdown(value: str) -> tuple[str, list[tuple[str, str]]]:
    prose: list[str] = []
    blocks: list[tuple[str, str]] = []
    marker: str | None = None
    language = ""
    body: list[str] = []
    for line in value.splitlines():
        stripped = line.strip()
        opening = re.match(r"^(`{3,}|~{3,})(.*)$", stripped)
        if marker is None and opening:
            marker = opening.group(1)
            language = opening.group(2).strip()
            body = []
        elif marker is not None and stripped == marker:
            blocks.append((language, "\n".join(body)))
            marker = None
            language = ""
            body = []
        elif marker is not None:
            body.append(line)
        else:
            prose.append(line)
    if marker is not None:
        blocks.append((language, "\n".join(body)))
    return "\n".join(prose), blocks


def markdown_headings(value: str) -> list[tuple[int, str]]:
    prose, _ = split_fenced_markdown(value)
    headings = [(len(level), title.strip()) for level, title in HEADING.findall(prose)]
    frontmatter = re.match(r'^---\n.*?\n---\n', prose, re.DOTALL)
    if frontmatter:
        headings.insert(0, (1, page_title(prose)))
    return headings


def rendered_heading_label(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    value = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", value)
    value = re.sub(r"\\([\\`*{}\[\]()#+.!_>~-])", r"\1", value)
    value = re.sub(r"[*_`~]", "", value)
    return " ".join(html.unescape(value).split()).translate(
        str.maketrans({"’": "'", "‘": "'", "“": '"', "”": '"'})
    )


def markdown_code_blocks(value: str) -> list[tuple[str, str]]:
    _, blocks = split_fenced_markdown(value)
    return [(language, normalize_markdown(body).rstrip()) for language, body in blocks]


def external_urls(value: str) -> list[str]:
    prose, _ = split_fenced_markdown(value)
    prose = re.sub(r"!\[[^]]*\]\([^)]+\)", "", prose)
    return sorted({url.rstrip(".,") for url in URL.findall(prose) if not url.startswith(SOURCE)})


def fetch_llms_full_pages() -> list[str]:
    """Fetch every page of GitBook's paginated full-space Markdown export."""
    url = SOURCE + "/llms-full.txt"
    pages: list[str] = []
    seen: set[str] = set()
    while url not in seen:
        seen.add(url)
        content = fetch_text(url)
        pages.append(content)
        match = NEXT_LLMS_PAGE.search(content)
        if not match:
            break
        url = urljoin(SOURCE + "/", match.group(1))
        if not url.startswith(SOURCE + "/llms-full.txt/"):
            raise ValueError(f"Unexpected llms-full continuation URL: {url}")
    return pages


def llms_full_titles(pages: list[str]) -> list[str]:
    titles: list[str] = []
    for page in pages:
        prose, _ = split_fenced_markdown(page)
        titles.extend(line[2:].strip() for line in prose.splitlines() if line.startswith("# "))
    return titles


def expected_page(url: str, source: str, valid_paths: set[str]) -> str:
    destination = page_path(url)
    transformed = transform_gitbook(source)
    return starlight_page(transform_links(transformed, destination, valid_paths))


def target_url(base: str, destination: PurePosixPath) -> str:
    if destination == PurePosixPath("index.md"):
        return base.rstrip("/") + "/"
    return urljoin(base.rstrip("/") + "/", str(destination.with_suffix("")) + "/")


def published_url(markdown_url: str) -> str:
    if markdown_url == SOURCE + "/readme.md":
        return SOURCE
    return markdown_url[:-3].rstrip("/")


class RenderedFacts(HTMLParser):
    def __init__(self, content_tag: str) -> None:
        super().__init__()
        self.content_tag = content_tag
        self.depth = 0
        self.heading_tag: str | None = None
        self.heading_parts: list[str] = []
        self.headings: list[tuple[int, str]] = []
        self.images = 0
        self.pre_blocks = 0

    @property
    def in_content(self) -> bool:
        return self.depth > 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == self.content_tag:
            self.depth += 1
            return
        if not self.in_content:
            return
        if tag == self.content_tag:
            self.depth += 1
        elif re.fullmatch(r"h[1-6]", tag):
            self.heading_tag = tag
            self.heading_parts = []
        elif tag == "img":
            self.images += 1
        elif tag == "pre":
            self.pre_blocks += 1

    def handle_endtag(self, tag: str) -> None:
        if self.in_content and tag == self.heading_tag:
            text = rendered_heading_label("".join(self.heading_parts).replace("¶", ""))
            self.headings.append((int(tag[1]), text))
            self.heading_tag = None
            self.heading_parts = []
        if tag == self.content_tag and self.depth:
            self.depth -= 1

    def handle_data(self, data: str) -> None:
        if self.in_content and self.heading_tag:
            self.heading_parts.append(data)


def fetch_html(url: str) -> str:
    request = Request(url, headers={"User-Agent": "Fulstech migration audit/1.0"})
    with urlopen(request, timeout=45) as response:
        return response.read().decode("utf-8", errors="replace")


def rendered_facts(url: str, content_tag: str) -> dict[str, object]:
    try:
        parser = RenderedFacts(content_tag)
        parser.feed(fetch_html(url))
        return {
            "url": url,
            "ok": True,
            "headings": parser.headings,
            "images": parser.images,
            "pre_blocks": parser.pre_blocks,
        }
    except (HTTPError, URLError, TimeoutError) as error:
        return {"url": url, "ok": False, "error": str(error)}


def audit(live_base: str | None) -> dict[str, object]:
    llms = fetch_text(SOURCE + "/llms.txt")
    urls = list(dict.fromkeys(MARKDOWN_URL.findall(llms)))
    full_export_pages = fetch_llms_full_pages()
    full_export_titles = llms_full_titles(full_export_pages)
    sitemap = ET.fromstring(fetch_text(SOURCE + "/sitemap-pages.xml"))
    sitemap_urls = {
        (element.text or "").rstrip("/")
        for element in sitemap.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
    }
    markdown_published_urls = {published_url(url) for url in urls}
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool:
        sources = list(pool.map(fetch_text, urls))

    page_data = list(zip(urls, sources, strict=True))
    expected_full_export_titles = [page_title(source) for source in sources]
    valid_paths = {str(page_path(url)) for url in urls}
    expected_paths = {Path(path) for path in valid_paths}
    actual_paths = {path.relative_to(DOCS) for path in DOCS.rglob("*.md")}

    missing_pages = sorted(str(path) for path in expected_paths - actual_paths)
    extra_pages = sorted(str(path) for path in actual_paths - expected_paths)
    content_mismatches: list[str] = []
    title_mismatches: list[str] = []
    heading_mismatches: list[str] = []
    code_mismatches: list[str] = []
    external_link_mismatches: list[str] = []
    external_image_references: dict[str, list[str]] = {}
    unresolved_blocks: dict[str, list[str]] = {}
    source_block_counts: Counter[str] = Counter()
    expected_assets: set[str] = set()
    nav_pages: list[tuple[PurePosixPath, str]] = []

    for url, source in page_data:
        destination = page_path(url)
        path = DOCS / destination
        source_block_counts.update(GITBOOK_BLOCK.findall(source))
        transformed_source = transform_gitbook(source)
        for target in visible_image_targets(transformed_source):
            if target.startswith("/files/"):
                expected_assets.add(target.removeprefix("/files/"))
            elif target.startswith(("http://", "https://")):
                normalized = original_asset_url(target.replace("\\&", "&"))
                if "gitbook.io" in target and "~gitbook/image" in target:
                    expected_assets.add(
                        "remote-" + hashlib.sha256(normalized.encode()).hexdigest()[:16]
                    )
                else:
                    expected_assets.add(external_asset_key(normalized))
        if not path.exists():
            continue
        expected = expected_page(url, source, valid_paths)
        actual = path.read_text(encoding="utf-8")
        label = str(destination)
        nav_pages.append((destination, page_title(expected)))
        if normalize_markdown(expected) != normalize_markdown(actual):
            content_mismatches.append(label)
        if page_title(expected) != page_title(actual):
            title_mismatches.append(label)
        if markdown_headings(expected) != markdown_headings(actual):
            heading_mismatches.append(label)
        if markdown_code_blocks(expected) != markdown_code_blocks(actual):
            code_mismatches.append(label)
        if external_urls(expected) != external_urls(actual):
            external_link_mismatches.append(label)
        external_images = sorted(
            target
            for target in visible_image_targets(actual)
            if target.startswith(("http://", "https://"))
        )
        if external_images:
            external_image_references[label] = external_images
        remaining = sorted(set(GITBOOK_BLOCK.findall(actual)))
        if remaining:
            unresolved_blocks[label] = remaining

    actual_asset_files = [path for path in (DOCS / "assets").glob("*") if path.is_file()]
    actual_asset_keys = {path.stem for path in actual_asset_files}
    missing_assets = sorted(expected_assets - actual_asset_keys)
    extra_assets = sorted(actual_asset_keys - expected_assets)
    broken_local_assets: list[str] = []
    for page in DOCS.rglob("*.md"):
        content = page.read_text(encoding="utf-8")
        for relative in re.findall(r"!?\[[^]]*\]\(([^) ]+)", content):
            if "assets/" not in relative:
                continue
            target = (page.parent / relative.split("#", 1)[0]).resolve()
            if not target.is_file():
                broken_local_assets.append(f"{page.relative_to(DOCS)} -> {relative}")

    actual_nav = json.loads((ROOT / "src" / "sidebar.json").read_text(encoding="utf-8"))
    expected_nav = sidebar_data(nav_pages)

    live: dict[str, object] | None = None
    if live_base:
        source_rendered_urls = [url[:-3] for url in urls]
        target_rendered_urls = [target_url(live_base, page_path(url)) for url in urls]
        with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool:
            source_facts = list(pool.map(lambda item: rendered_facts(item, "main"), source_rendered_urls))
            target_facts = list(pool.map(lambda item: rendered_facts(item, "main"), target_rendered_urls))
        unavailable = [
            {"source": source, "target": target}
            for source, target in zip(source_facts, target_facts, strict=True)
            if not source.get("ok") or not target.get("ok")
        ]
        rendered_mismatches = []
        known_rendered_differences = []
        for markdown_source, source, target in zip(sources, source_facts, target_facts, strict=True):
            if not source.get("ok") or not target.get("ok"):
                continue
            expected_markdown = transform_gitbook(markdown_source)
            expected_headings = [
                (level, rendered_heading_label(title))
                for level, title in markdown_headings(expected_markdown)
            ]
            expected_images = len(visible_image_targets(expected_markdown))
            expected_code_blocks = len(markdown_code_blocks(expected_markdown))
            source_headings = list(source["headings"])
            known: list[dict[str, object]] = []
            if source_headings and expected_headings:
                source_level, source_title = source_headings[0]
                expected_level, expected_title = expected_headings[0]
                if (
                    source_level == expected_level
                    and source_title != expected_title
                    and source_title.endswith(expected_title)
                ):
                    known.append(
                        {
                            "type": "gitbook_page_icon",
                            "gitbook": source_title,
                            "github_pages": expected_title,
                        }
                    )
                    source_headings[0] = expected_headings[0]
            for tab_title in re.findall(r'{% tab title="([^"]+)" %}', markdown_source):
                known.append({"type": "flattened_gitbook_tab", "title": tab_title})
            differences: dict[str, object] = {}
            if expected_headings != target["headings"]:
                differences["headings"] = {
                    "expected_from_gitbook_markdown": expected_headings,
                    "github_pages": target["headings"],
                }
            if expected_images != target["images"]:
                differences["images"] = {
                    "expected_from_gitbook_markdown": expected_images,
                    "github_pages": target["images"],
                }
            if expected_code_blocks != target["pre_blocks"]:
                differences["code_blocks"] = {
                    "expected_from_gitbook_markdown": expected_code_blocks,
                    "github_pages": target["pre_blocks"],
                }
            if differences:
                rendered_mismatches.append(
                    {"source": source["url"], "target": target["url"], "differences": differences}
                )
            if known:
                known_rendered_differences.append(
                    {"source": source["url"], "target": target["url"], "differences": known}
                )
        live = {
            "checked_pages": len(urls),
            "unavailable": unavailable,
            "rendered_mismatches": rendered_mismatches,
            "known_rendered_differences": known_rendered_differences,
        }

    failures = {
        "missing_pages": missing_pages,
        "extra_pages": extra_pages,
        "content_mismatches": content_mismatches,
        "title_mismatches": title_mismatches,
        "heading_mismatches": heading_mismatches,
        "code_mismatches": code_mismatches,
        "external_link_mismatches": external_link_mismatches,
        "external_image_references": external_image_references,
        "unresolved_gitbook_blocks": unresolved_blocks,
        "missing_assets": missing_assets,
        "extra_assets": extra_assets,
        "broken_local_assets": broken_local_assets,
        "navigation_mismatch": actual_nav != expected_nav,
        "duplicate_overview_groups": duplicate_overview_groups(actual_nav),
        "sitemap_only_urls": sorted(sitemap_urls - markdown_published_urls),
        "markdown_only_urls": sorted(markdown_published_urls - sitemap_urls),
        "llms_full_title_order_mismatch": (
            {
                "expected_from_llms": expected_full_export_titles,
                "actual_from_llms_full": full_export_titles,
            }
            if full_export_titles != expected_full_export_titles
            else {}
        ),
    }
    if live:
        failures["live_unavailable"] = live["unavailable"]
        failures["unexpected_rendered_mismatches"] = live["rendered_mismatches"]

    return {
        "source": SOURCE,
        "pages": {
            "gitbook_markdown": len(urls),
            "gitbook_sitemap": len(sitemap_urls),
            "gitbook_llms_full": len(full_export_titles),
            "gitbook_llms_full_chunks": len(full_export_pages),
            "github": len(actual_paths),
        },
        "assets": {"gitbook_references": len(expected_assets), "github": len(actual_asset_files)},
        "gitbook_block_counts": dict(sorted(source_block_counts.items())),
        "failures": failures,
        "live": live,
        "passed": not any(failures.values()),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--live-base", help="Also compare rendered GitBook and Pages URLs")
    parser.add_argument("--output", type=Path, help="Write the full JSON report")
    args = parser.parse_args()
    report = audit(args.live_base)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    if not report["passed"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
