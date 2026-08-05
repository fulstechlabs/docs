#!/usr/bin/env python3
"""Fail when a built Starlight page points at a missing local target."""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
import os
from pathlib import Path
from urllib.parse import unquote, urlsplit


class References(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.urls: list[str] = []

    def handle_starttag(self, _tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        for name in ("href", "src"):
            if values.get(name):
                self.urls.append(values[name] or "")


def candidates(target: Path, path: str) -> list[Path]:
    output = [target]
    if path.endswith("/"):
        output.append(target / "index.html")
    elif not target.suffix:
        output.extend((target.with_suffix(".html"), target / "index.html"))
    if target.is_dir():
        output.append(target / "index.html")
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dist", type=Path, default=Path("dist"))
    parser.add_argument("--base", default=os.environ.get("DOCS_BASE_PATH", "/"))
    args = parser.parse_args()

    root = args.dist.resolve()
    base = "/" + args.base.strip("/") if args.base.strip("/") else "/"
    missing: list[tuple[str, str]] = []
    outside_base: list[tuple[str, str]] = []
    checked = 0

    html_files = sorted(root.rglob("*.html"))
    for html_file in html_files:
        references = References()
        references.feed(html_file.read_text(encoding="utf-8", errors="replace"))
        for url in references.urls:
            parsed = urlsplit(url)
            if parsed.scheme or parsed.netloc or url.startswith(("#", "data:", "javascript:")):
                continue
            path = unquote(parsed.path)
            if not path:
                continue
            if path.startswith("/"):
                if base != "/" and path != base and not path.startswith(base + "/"):
                    outside_base.append((html_file.relative_to(root).as_posix(), url))
                    continue
                local_path = path[len(base) :] if base != "/" else path
                target = root / local_path.lstrip("/")
            else:
                target = html_file.parent / path
            checked += 1
            if not any(candidate.exists() for candidate in candidates(target, path)):
                missing.append((html_file.relative_to(root).as_posix(), url))

    for label, failures in (("outside configured base", outside_base), ("missing", missing)):
        for page, url in failures:
            print(f"{label}: {page} -> {url}")
    if outside_base or missing:
        raise SystemExit(1)
    print(f"Checked {checked} local href/src references across {len(html_files)} HTML files")


if __name__ == "__main__":
    main()
