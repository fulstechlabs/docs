#!/usr/bin/env python3
"""Import the public Fulstech GitBook into the local MkDocs source tree."""

from __future__ import annotations

import concurrent.futures
import hashlib
import html
from html.parser import HTMLParser
import json
import mimetypes
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import time
from urllib.parse import parse_qs, unquote, urlparse
from urllib.request import Request, urlopen


SOURCE = "https://fulstech.gitbook.io/docs"
ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
ASSETS = DOCS / "assets"
USER_AGENT = "Fulstech GitBook migration/1.0"


def fetch(url: str, attempts: int = 4) -> tuple[bytes, str]:
    for attempt in range(attempts):
        try:
            request = Request(url, headers={"User-Agent": USER_AGENT})
            with urlopen(request, timeout=45) as response:
                return response.read(), response.headers.get_content_type()
        except Exception:
            if attempt == attempts - 1:
                raise
            time.sleep(0.5 * (attempt + 1))
    raise AssertionError("unreachable")


def fetch_text(url: str) -> str:
    payload, _ = fetch(url)
    return payload.decode("utf-8")


class MainImages(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_main = False
        self.sources: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "main":
            self.in_main = True
        elif self.in_main and tag == "img":
            values = dict(attrs)
            if values.get("src"):
                self.sources.append(html.unescape(values["src"] or ""))

    def handle_endtag(self, tag: str) -> None:
        if tag == "main":
            self.in_main = False


def page_path(url: str) -> PurePosixPath:
    relative = url.removeprefix(SOURCE + "/")
    if relative == "readme.md":
        return PurePosixPath("index.md")
    return PurePosixPath(relative)


def page_title(markdown: str) -> str:
    match = re.search(r"^#\s+(.+?)\s*$", markdown, re.MULTILINE)
    if not match:
        raise ValueError("page has no level-one heading")
    return re.sub(r"[*_`]", "", match.group(1)).strip()


def original_asset_url(proxy_url: str) -> str:
    parsed = urlparse(proxy_url)
    values = parse_qs(parsed.query).get("url")
    return values[0] if values else proxy_url


def external_asset_key(url: str) -> str:
    return "external-" + hashlib.sha256(url.encode()).hexdigest()[:16]


def visible_image_targets(markdown: str) -> list[str]:
    without_code = re.sub(r"```.*?```", "", markdown, flags=re.DOTALL)
    pattern = re.compile(
        r'!\[[^]]*\]\((?P<markdown>[^) ]+)[^)]*\)|<img[^>]+src="(?P<html>[^"]+)"',
        re.IGNORECASE,
    )
    return [match.group("markdown") or match.group("html") for match in pattern.finditer(without_code)]


def extension_for(url: str, content_type: str) -> str:
    suffix = Path(urlparse(url).path).suffix.lower()
    if suffix and len(suffix) <= 6:
        return suffix
    return mimetypes.guess_extension(content_type) or ".bin"


def internal_target(target: str) -> str | None:
    raw = target.replace("\\&", "&")
    if raw.startswith(SOURCE):
        raw = raw.removeprefix(SOURCE)
    elif raw.startswith("/docs"):
        raw = raw.removeprefix("/docs")
    else:
        return None
    raw = raw.split("?", 1)[0]
    fragment = ""
    if "#" in raw:
        raw, fragment = raw.split("#", 1)
        fragment = "#" + fragment
    raw = raw.strip("/")
    if not raw or raw == "readme.md":
        return "index.md" + fragment
    if not raw.endswith(".md"):
        raw += ".md"
    return raw + fragment


def transform_links(
    markdown: str,
    current: PurePosixPath,
    valid_paths: set[str],
) -> str:
    pattern = re.compile(r"(?P<prefix>!?\[[^]]*\]\()(?P<target>[^) ]+)(?P<suffix>[^)]*\))")

    def replace(match: re.Match[str]) -> str:
        target = match.group("target")
        normalized = internal_target(target)
        if normalized is None:
            return match.group(0)
        path, marker, fragment = normalized.partition("#")
        if fragment == "create-a-new-custom-field-of-type-text-field-multi-line":
            fragment = "create-a-new-custom-field"
        if path not in valid_paths:
            candidates = [candidate for candidate in valid_paths if candidate.endswith("/" + path)]
            if len(candidates) == 1:
                path = candidates[0]
        relative = os.path.relpath(path, start=str(current.parent))
        if marker:
            relative += "#" + fragment
        return match.group("prefix") + relative + match.group("suffix")

    return pattern.sub(replace, markdown)


def transform_gitbook(markdown: str) -> str:
    markdown = re.sub(
        r"^> For the complete documentation index,.*?\n\n",
        "",
        markdown,
        count=1,
        flags=re.DOTALL,
    )
    markdown = re.sub(
        r'<figure><img src="([^"]+)" alt="[^"]*"><figcaption><p>(.*?)</p></figcaption></figure>',
        r'![\2](\1)',
        markdown,
    )
    markdown = re.sub(
        r'<figure><img src="([^"]+)"[^>]*><figcaption>(?:<p>(.*?)</p>)?</figcaption></figure>',
        lambda match: f'![{match.group(2) or ""}]({match.group(1)})',
        markdown,
    )
    markdown = re.sub(
        r'<img src="([^"]+)" alt="([^"]*)"[^>]*>',
        r'![\2](\1)',
        markdown,
    )
    markdown = re.sub(r'{% hint style="([^"]+)" %}', r'> **\1**\n>', markdown)
    markdown = markdown.replace("{% endhint %}", "")
    markdown = re.sub(r'{% tab title="([^"]+)" %}', r'#### \1', markdown)
    markdown = re.sub(r"{% (?:end)?tabs? %}", "", markdown)
    markdown = re.sub(
        r'{% embed url="<?([^">]+)>?" %}',
        r'[Watch the video](\1)',
        markdown,
    )
    markdown = re.sub(r"{% endembed %}", "", markdown)
    markdown = re.sub(r"{% (?:end)?content-ref(?: [^%]*)? %}", "", markdown)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    return "\n".join(line.rstrip() for line in markdown.strip().splitlines()) + "\n"


def yaml_nav(pages: list[tuple[PurePosixPath, str]]) -> str:
    tree: dict[str, object] = {}
    for path, title in pages:
        parts = list(path.with_suffix("").parts)
        if parts == ["index"]:
            continue
        node = tree
        for part in parts:
            node = node.setdefault(part, {})  # type: ignore[assignment]
        node["__page__"] = (title, str(path))

    lines = ["nav:", '  - "Home": index.md']

    def emit(nodes: dict[str, object], indent: int) -> None:
        for key, value in nodes.items():
            if key == "__page__":
                continue
            child = value
            assert isinstance(child, dict)
            page = child.get("__page__")
            nested = [item for item in child if item != "__page__"]
            label = page[0] if page else key.replace("-", " ").title()
            prefix = " " * indent + "- " + json.dumps(label) + ":"
            if page and not nested:
                lines.append(prefix + " " + page[1])
            else:
                lines.append(prefix)
                if page:
                    lines.append(" " * (indent + 2) + '- "Overview": ' + page[1])
                emit(child, indent + 2)

    emit(tree, 2)
    return "\n".join(lines) + "\n"


def main() -> None:
    llms = fetch_text(SOURCE + "/llms.txt")
    urls = list(dict.fromkeys(re.findall(r"https://fulstech\.gitbook\.io/docs/[^)]+\.md", llms)))
    if not urls:
        raise RuntimeError("GitBook index did not contain Markdown pages")

    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool:
        markdown_values = list(pool.map(fetch_text, urls))

    page_data = list(zip(urls, markdown_values, strict=True))
    image_pages = [(url, text) for url, text in page_data if visible_image_targets(text)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
        html_values = list(pool.map(lambda item: fetch_text(item[0][:-3]), image_pages))

    asset_sources: dict[str, str] = {}
    remote_keys: dict[str, str] = {}
    for (url, markdown), rendered in zip(image_pages, html_values, strict=True):
        targets = visible_image_targets(markdown)
        file_ids = [target.removeprefix("/files/") for target in targets if target.startswith("/files/")]
        parser = MainImages()
        parser.feed(rendered)
        rendered_sources = [original_asset_url(source) for source in parser.sources]
        used: set[int] = set()

        for target in targets:
            if target.startswith("/files/"):
                continue
            normalized = original_asset_url(target.replace("\\&", "&"))
            matches = [index for index, source in enumerate(rendered_sources) if source == normalized]
            if len(matches) == 1:
                used.add(matches[0])
            if "gitbook.io" in target and "~gitbook/image" in target:
                key = "remote-" + hashlib.sha256(normalized.encode()).hexdigest()[:16]
                remote_keys[target] = key
                asset_sources[key] = normalized
            elif urlparse(normalized).scheme in {"http", "https"}:
                key = external_asset_key(normalized)
                remote_keys[target] = key
                asset_sources[key] = normalized

        unresolved_ids: list[str] = []
        for file_id in file_ids:
            matches = [
                index
                for index, source in enumerate(rendered_sources)
                if index not in used and file_id in unquote(urlparse(source).path)
            ]
            if len(matches) == 1:
                used.add(matches[0])
                asset_sources[file_id] = rendered_sources[matches[0]]
            else:
                unresolved_ids.append(file_id)

        unresolved_sources = [
            source for index, source in enumerate(rendered_sources) if index not in used
        ]
        if len(unresolved_ids) != len(unresolved_sources):
            raise RuntimeError(
                f"image mapping mismatch for {url}: "
                f"unresolved Markdown={len(unresolved_ids)}, rendered={len(unresolved_sources)}"
            )
        for file_id, resolved in zip(unresolved_ids, unresolved_sources, strict=True):
            existing = asset_sources.setdefault(file_id, resolved)
            if existing != resolved:
                raise RuntimeError(f"conflicting asset mapping for {file_id}")

    temp_docs = ROOT / ".imported-docs"
    if temp_docs.exists():
        shutil.rmtree(temp_docs)
    temp_assets = temp_docs / "assets"
    temp_assets.mkdir(parents=True)

    def download(item: tuple[str, str]) -> tuple[str, str]:
        file_id, url = item
        try:
            payload, content_type = fetch(url)
        except Exception as error:
            raise RuntimeError(f"failed to download {file_id} from {url}") from error
        extension = extension_for(url, content_type)
        (temp_assets / f"{file_id}{extension}").write_bytes(payload)
        return file_id, extension

    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool:
        downloaded = dict(pool.map(download, asset_sources.items()))

    nav_pages: list[tuple[PurePosixPath, str]] = []
    valid_paths = {str(page_path(url)) for url, _ in page_data}
    for url, source in page_data:
        destination = page_path(url)
        output = transform_gitbook(source)
        output = transform_links(output, destination, valid_paths)

        def replace_asset(match: re.Match[str]) -> str:
            file_id = match.group(1)
            asset = PurePosixPath("assets") / f"{file_id}{downloaded[file_id]}"
            return os.path.relpath(str(asset), start=str(destination.parent))

        output = re.sub(r"/files/([A-Za-z0-9_-]+)", replace_asset, output)
        for remote, key in remote_keys.items():
            if remote in output:
                asset = PurePosixPath("assets") / f"{key}{downloaded[key]}"
                output = output.replace(
                    remote,
                    os.path.relpath(str(asset), start=str(destination.parent)),
                )
        target = temp_docs / destination
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(output, encoding="utf-8")
        nav_pages.append((destination, page_title(output)))

    stylesheet = DOCS / "stylesheets" / "extra.css"
    (temp_docs / "stylesheets").mkdir()
    shutil.copy2(stylesheet, temp_docs / "stylesheets" / "extra.css")
    shutil.rmtree(DOCS)
    temp_docs.rename(DOCS)

    config = ROOT / "mkdocs.yml"
    base_config = re.sub(r"\nnav:\n.*\Z", "\n", config.read_text(encoding="utf-8"), flags=re.DOTALL)
    config.write_text(base_config.rstrip() + "\n\n" + yaml_nav(nav_pages), encoding="utf-8")
    print(f"Imported {len(page_data)} pages and {len(downloaded)} assets")


if __name__ == "__main__":
    main()
