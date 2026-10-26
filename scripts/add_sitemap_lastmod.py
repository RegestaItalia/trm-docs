#!/usr/bin/env python3
"""Add reliable per-page lastmod dates to the generated sitemap."""

from __future__ import annotations

import argparse
import html
import re
import subprocess
from pathlib import Path
from urllib.parse import urlparse


URL_PATTERN = re.compile(r"(?P<indent>\s*)<url>\s*<loc>(?P<loc>[^<]+)</loc>(?P<body>.*?)</url>", re.DOTALL)


def source_for_location(location: str, source_dir: Path) -> Path:
    path = urlparse(html.unescape(location)).path.strip("/")
    if not path:
        return source_dir / "index.md"
    page = source_dir / f"{path}.md"
    index = source_dir / path / "index.md"
    return index if index.is_file() else page


def git_last_modified(source: Path, repository: Path) -> str:
    try:
        relative = source.relative_to(repository)
    except ValueError as error:
        raise RuntimeError(f"{source} is outside {repository}") from error
    result = subprocess.run(
        ["git", "log", "-1", "--format=%cs", "--", relative.as_posix()],
        cwd=repository,
        check=True,
        capture_output=True,
        text=True,
    )
    date = result.stdout.strip()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
        raise RuntimeError(f"No committed modification date found for {relative}")
    return date


def enrich_sitemap(xml: str, source_dir: Path, repository: Path) -> str:
    seen = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal seen
        seen += 1
        location = match.group("loc")
        source = source_for_location(location, source_dir)
        if not source.is_file():
            raise RuntimeError(f"No documentation source maps to {html.unescape(location)}")
        date = git_last_modified(source, repository)
        body = re.sub(r"\s*<lastmod>[^<]*</lastmod>", "", match.group("body"))
        indent = match.group("indent")
        child_indent = f"{indent}  "
        return f"{indent}<url>\n{child_indent}<loc>{location}</loc>\n{child_indent}<lastmod>{date}</lastmod>{body}\n{indent}</url>"

    enriched = URL_PATTERN.sub(replace, xml)
    if seen == 0:
        raise RuntimeError("Sitemap contains no URL entries")
    return enriched


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sitemap", type=Path, default=Path("site/sitemap.xml"))
    parser.add_argument("--source-dir", type=Path, default=Path("docs"))
    parser.add_argument("--repository", type=Path, default=Path.cwd())
    args = parser.parse_args()
    xml = args.sitemap.read_text(encoding="utf-8")
    args.sitemap.write_text(enrich_sitemap(xml, args.source_dir.resolve(), args.repository.resolve()), encoding="utf-8")
    print(f"Added Git-derived lastmod dates to {args.sitemap}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
