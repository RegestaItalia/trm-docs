#!/usr/bin/env python3
"""Copy the marked setup section into another repository's README."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


START_MARKER = "<!-- START OF SETUP.MD -->"
END_MARKER = "<!-- END OF SETUP.MD -->"
SOURCE_IMAGE_PREFIX = "../assets/"
README_IMAGE_PREFIX = (
    "https://raw.githubusercontent.com/RegestaItalia/trm-docs/main/docs/assets/"
)


def marked_block(document: str, document_name: str) -> str:
    start_count = document.count(START_MARKER)
    end_count = document.count(END_MARKER)
    if start_count != 1 or end_count != 1:
        raise ValueError(
            f"{document_name} must contain exactly one start marker and one end marker "
            f"(found {start_count} and {end_count})"
        )

    start = document.index(START_MARKER)
    end = document.index(END_MARKER, start) + len(END_MARKER)
    return document[start:end]


def convert_image_sources(block: str) -> str:
    """Make documentation-relative image sources valid in external READMEs."""

    return re.sub(
        r'(?P<prefix><img\s+[^>]*?src=["\'])'
        + re.escape(SOURCE_IMAGE_PREFIX),
        lambda match: match.group("prefix") + README_IMAGE_PREFIX,
        block,
        flags=re.IGNORECASE,
    )


def update_readme(source: str, readme: str, source_name: str, readme_name: str) -> str:
    source_block = convert_image_sources(marked_block(source, source_name))
    target_block = marked_block(readme, readme_name)
    return readme.replace(target_block, source_block, 1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path, help="Markdown file containing the source block")
    parser.add_argument("readmes", nargs="+", type=Path, help="README files to update")
    args = parser.parse_args()

    source = args.source.read_text(encoding="utf-8")
    for readme_path in args.readmes:
        current = readme_path.read_text(encoding="utf-8")
        updated = update_readme(source, current, str(args.source), str(readme_path))
        if updated != current:
            readme_path.write_text(updated, encoding="utf-8")
            print(f"Updated {readme_path}")
        else:
            print(f"Already current: {readme_path}")


if __name__ == "__main__":
    main()
