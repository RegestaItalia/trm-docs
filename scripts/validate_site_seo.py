#!/usr/bin/env python3
"""Validate canonical URLs and maintained redirects in the built documentation."""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse


class HeadMetadataParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.canonicals: list[str] = []
        self.refreshes: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "link" and values.get("rel", "").lower() == "canonical" and values.get("href"):
            self.canonicals.append(values["href"])
        if tag == "meta" and values.get("http-equiv", "").lower() == "refresh" and values.get("content"):
            self.refreshes.append(values["content"])


def page_url(path: Path, site_dir: Path, site_url: str) -> str:
    relative = path.relative_to(site_dir).as_posix()
    suffix = "" if relative == "index.html" else relative.removesuffix("index.html")
    return urljoin(site_url, suffix)


def output_for_url(url: str, site_dir: Path, site_url: str) -> Path | None:
    parsed = urlparse(urljoin(site_url, url))
    base = urlparse(site_url)
    if parsed.netloc != base.netloc or parsed.scheme != base.scheme:
        return None
    relative = parsed.path.removeprefix("/")
    return site_dir / relative / "index.html" if parsed.path.endswith("/") else site_dir / relative


def parse_metadata(path: Path) -> HeadMetadataParser:
    parser = HeadMetadataParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def validate(site_dir: Path, source_dir: Path, site_url: str) -> list[str]:
    errors: list[str] = []
    redirect_outputs = {
        site_dir / path.relative_to(source_dir)
        for path in source_dir.rglob("*.html")
    }

    for path in sorted(site_dir.rglob("index.html")):
        metadata = parse_metadata(path)
        label = path.relative_to(site_dir).as_posix()
        if len(metadata.canonicals) != 1:
            errors.append(f"{label}: expected exactly one canonical URL")
            continue

        canonical = metadata.canonicals[0]
        expected = page_url(path, site_dir, site_url)
        if path in redirect_outputs:
            if len(metadata.refreshes) != 1 or "url=" not in metadata.refreshes[0].lower():
                errors.append(f"{label}: maintained redirect needs exactly one meta refresh")
                continue
            target = metadata.refreshes[0].split("=", 1)[1].strip()
            resolved_target = urljoin(site_url, target)
            if canonical != resolved_target:
                errors.append(f"{label}: redirect canonical does not match its destination")
            output = output_for_url(resolved_target, site_dir, site_url)
            if output is None or not output.is_file():
                errors.append(f"{label}: redirect destination is not a built documentation page")
        elif canonical != expected:
            errors.append(f"{label}: canonical is {canonical!r}, expected {expected!r}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-dir", type=Path, default=Path("site"))
    parser.add_argument("--source-dir", type=Path, default=Path("docs"))
    parser.add_argument("--site-url", default="https://docs.trmregistry.com/")
    args = parser.parse_args()
    errors = validate(args.site_dir, args.source_dir, args.site_url)
    if errors:
        print("\n".join(errors))
        return 1
    print("Documentation canonicals and redirects are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
