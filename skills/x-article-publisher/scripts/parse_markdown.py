#!/usr/bin/env python3
"""
Parse Markdown for X Articles publishing.

Extracts:
- title
- cover image
- content images with block_index/editor_block_index
- dividers with block_index/editor_block_index
- rich-text HTML content
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
import urllib.parse
import urllib.request
from pathlib import Path


SEARCH_DIRS = [
    Path.home() / "Downloads",
    Path.home() / "Desktop",
    Path.home() / "Pictures",
]
FRONTMATTER_COVER_KEYS = ("cover_image", "coverImage", "cover", "image", "featureImage", "feature_image")
REMOTE_IMAGE_DIR = Path(tempfile.gettempdir()) / "x-article-publisher-images"

def parse_frontmatter(content: str) -> tuple[dict[str, str], str]:
    lines = content.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, content

    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            metadata: dict[str, str] = {}
            for raw_line in lines[1:idx]:
                line = raw_line.strip()
                if not line or line.startswith("#") or ":" not in raw_line:
                    continue
                key, value = raw_line.split(":", 1)
                key = key.strip()
                value = value.strip()
                if not key:
                    continue
                if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
                    value = value[1:-1]
                metadata[key] = value.strip()
            return metadata, "\n".join(lines[idx + 1 :]).lstrip()

    return {}, content


def pick_frontmatter_value(metadata: dict[str, str], keys: tuple[str, ...]) -> str | None:
    for key in keys:
        value = metadata.get(key)
        if value:
            return value
    return None


def extension_from_content_type(content_type: str | None) -> str:
    mapping = {
        "image/jpeg": ".jpg",
        "image/jpg": ".jpg",
        "image/png": ".png",
        "image/gif": ".gif",
        "image/webp": ".webp",
    }
    return mapping.get((content_type or "").lower(), ".png")


def get_remote_image_path(url: str) -> tuple[str, bool]:
    if not url.startswith("https://"):
        print(f"[parse_markdown] WARNING: skipping non-HTTPS image: '{url}'", file=sys.stderr)
        return url, False

    REMOTE_IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    parsed = urllib.parse.urlparse(url)
    suffix = Path(parsed.path).suffix.lower()
    if suffix not in {".png", ".jpg", ".jpeg", ".gif", ".webp"}:
        suffix = ""
    digest = hashlib.md5(url.encode("utf-8")).hexdigest()[:10]
    existing = sorted(REMOTE_IMAGE_DIR.glob(f"remote_{digest}.*"))
    if existing:
        return str(existing[0]), True

    try:
        request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(request, timeout=30) as response:
            if not suffix:
                suffix = extension_from_content_type(response.headers.get_content_type())
            output_path = REMOTE_IMAGE_DIR / f"remote_{digest}{suffix}"
            output_path.write_bytes(response.read())
        return str(output_path), True
    except Exception as exc:
        print(f"[parse_markdown] WARNING: failed to download '{url}': {exc}", file=sys.stderr)
        return url, False


def resolve_image_path(image_reference: str, base_path: Path) -> tuple[str, str, bool]:
    if image_reference.startswith(("https://", "http://")):
        path, exists = get_remote_image_path(image_reference)
        return path, image_reference, exists

    decoded_reference = urllib.parse.unquote(image_reference)
    resolved_path = str(base_path / decoded_reference) if not os.path.isabs(decoded_reference) else decoded_reference
    filename = os.path.basename(decoded_reference)
    full_path, exists = find_image_file(resolved_path, filename)
    return full_path, resolved_path, exists


def find_image_file(original_path: str, filename: str) -> tuple[str, bool]:
    if os.path.isfile(original_path):
        return original_path, True

    for search_dir in SEARCH_DIRS:
        candidate = search_dir / filename
        if candidate.is_file():
            print(
                f"[parse_markdown] Image not found at '{original_path}', using '{candidate}' instead",
                file=sys.stderr,
            )
            return str(candidate), True

    print(
        f"[parse_markdown] WARNING: Image not found: '{original_path}' "
        f"(also searched {[str(d) for d in SEARCH_DIRS]})",
        file=sys.stderr,
    )
    return original_path, False


def split_into_blocks(markdown: str) -> list[str]:
    blocks: list[str] = []
    current_block: list[str] = []
    in_code_block = False
    code_block_lines: list[str] = []

    for line in markdown.split("\n"):
        stripped = line.strip()

        if stripped.startswith("```"):
            if in_code_block:
                in_code_block = False
                if code_block_lines:
                    blocks.append("___CODE_BLOCK_START___" + "\n".join(code_block_lines) + "___CODE_BLOCK_END___")
                code_block_lines = []
            else:
                if current_block:
                    blocks.append("\n".join(current_block))
                    current_block = []
                in_code_block = True
            continue

        if in_code_block:
            code_block_lines.append(line)
            continue

        if not stripped:
            if current_block:
                blocks.append("\n".join(current_block))
                current_block = []
            continue

        if re.match(r"^---+$", stripped):
            if current_block:
                blocks.append("\n".join(current_block))
                current_block = []
            blocks.append("___DIVIDER___")
            continue

        if stripped.startswith(("#", ">")):
            if current_block:
                blocks.append("\n".join(current_block))
                current_block = []
            blocks.append(stripped)
            continue

        if re.match(r"^!\[.*\]\(.*\)$", stripped):
            if current_block:
                blocks.append("\n".join(current_block))
                current_block = []
            blocks.append(stripped)
            continue

        current_block.append(line)

    if current_block:
        blocks.append("\n".join(current_block))

    if code_block_lines:
        blocks.append("___CODE_BLOCK_START___" + "\n".join(code_block_lines) + "___CODE_BLOCK_END___")

    return blocks


def extract_images_and_dividers(markdown: str, base_path: Path) -> tuple[list[dict], list[dict], str, int]:
    blocks = split_into_blocks(markdown)
    images: list[dict] = []
    dividers: list[dict] = []
    clean_blocks: list[str] = []

    image_pattern = re.compile(r"^!\[([^\]]*)\]\(([^)]+)\)$")

    for block in blocks:
        stripped = block.strip()

        if stripped == "___DIVIDER___":
            editor_block_index = len(clean_blocks)
            block_index = editor_block_index + len(dividers)
            after_text = ""
            if clean_blocks:
                prev_block = clean_blocks[-1].strip()
                lines = [line for line in prev_block.split("\n") if line.strip()]
                after_text = lines[-1][:80] if lines else ""
            dividers.append(
                {
                    "block_index": block_index,
                    "editor_block_index": editor_block_index,
                    "after_text": after_text,
                }
            )
            continue

        match = image_pattern.match(stripped)
        if match:
            alt_text = match.group(1)
            image_path = match.group(2)
            full_path, original_path, exists = resolve_image_path(image_path, base_path)

            block_index = len(clean_blocks)
            editor_block_index = block_index
            after_text = ""
            if clean_blocks:
                prev_block = clean_blocks[-1].strip()
                lines = [line for line in prev_block.split("\n") if line.strip()]
                after_text = lines[-1][:80] if lines else ""

            images.append(
                {
                    "path": full_path,
                    "original_path": original_path,
                    "exists": exists,
                    "alt": alt_text,
                    "block_index": block_index,
                    "editor_block_index": editor_block_index,
                    "after_text": after_text,
                }
            )
        else:
            clean_blocks.append(block)

    return images, dividers, "\n\n".join(clean_blocks), len(clean_blocks)


def extract_title(markdown: str) -> tuple[str, str]:
    lines = markdown.strip().split("\n")
    title = "Untitled"
    title_line_idx: int | None = None

    for idx, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("# "):
            title = stripped[2:].strip()
            title_line_idx = idx
            break
        if stripped.startswith("## "):
            title = stripped[3:].strip()
            break
        if not stripped.startswith("!["):
            title = stripped[:100]
            break

    if title_line_idx is not None:
        lines.pop(title_line_idx)
        markdown = "\n".join(lines)

    return title, markdown


def markdown_to_html(markdown: str) -> str:
    html = markdown

    def convert_code_block(match: re.Match[str]) -> str:
        code_content = match.group(1)
        lines = code_content.strip().split("\n")
        formatted = "<br>".join(line for line in lines if line.strip())
        return f"<blockquote>{formatted}</blockquote>"

    html = re.sub(r"___CODE_BLOCK_START___(.*?)___CODE_BLOCK_END___", convert_code_block, html, flags=re.DOTALL)
    html = re.sub(r"^## (.+)$", r"<h2>\1</h2>", html, flags=re.MULTILINE)
    html = re.sub(r"^### (.+)$", r"<h3>\1</h3>", html, flags=re.MULTILINE)
    html = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", html)
    html = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", html)
    html = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', html)
    html = re.sub(r"^> (.+)$", r"<blockquote>\1</blockquote>", html, flags=re.MULTILINE)
    html = re.sub(r"^- (.+)$", r"<li>\1</li>", html, flags=re.MULTILINE)
    html = re.sub(r"^\d+\. (.+)$", r"<li>\1</li>", html, flags=re.MULTILINE)
    html = re.sub(r"((?:<li>.*?</li>\n?)+)", r"<ul>\1</ul>", html)

    parts = html.split("\n\n")
    processed: list[str] = []
    for part in parts:
        part = part.strip()
        if not part:
            continue
        if part.startswith(("<h2>", "<h3>", "<blockquote>", "<ul>", "<ol>")):
            processed.append(part)
        else:
            processed.append(f"<p>{part.replace(chr(10), '<br>')}</p>")

    return "".join(processed)


def parse_markdown_file(filepath: str, title_override: str | None = None, cover_override: str | None = None) -> dict:
    path = Path(filepath)
    base_path = path.parent
    metadata, content = parse_frontmatter(path.read_text(encoding="utf-8"))

    title, content = extract_title(content)
    if title_override:
        title = title_override
    elif frontmatter_title := metadata.get("title"):
        title = frontmatter_title
    images, dividers, clean_markdown, total_blocks = extract_images_and_dividers(content, base_path)
    html = markdown_to_html(clean_markdown)

    cover_image = None
    cover_exists = True
    content_images = images[1:] if len(images) > 1 else []

    cover_source = cover_override or pick_frontmatter_value(metadata, FRONTMATTER_COVER_KEYS)
    if cover_source:
        cover_image, _, cover_exists = resolve_image_path(cover_source, base_path)
        content_images = images
    elif images:
        cover_image = images[0]["path"]
        cover_exists = images[0]["exists"]

    missing = [img for img in images if not img["exists"]]
    if cover_image and not cover_exists:
        missing = [*missing, {"path": cover_image}]
    if missing:
        print(f"[parse_markdown] WARNING: {len(missing)} image(s) not found", file=sys.stderr)

    return {
        "title": title,
        "cover_image": cover_image,
        "cover_exists": cover_exists,
        "content_images": content_images,
        "dividers": dividers,
        "html": html,
        "total_blocks": total_blocks,
        "source_file": str(path.absolute()),
        "missing_images": len(missing),
        "cover_source": "frontmatter" if cover_source else ("first_content_image" if cover_image else "none"),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Parse Markdown for X Articles")
    parser.add_argument("file", help="Markdown file to parse")
    parser.add_argument("--output", choices=["json", "html"], default="json", help="Output format")
    parser.add_argument("--html-only", action="store_true", help="Output only HTML content")
    parser.add_argument("--title", help="Override title from markdown/frontmatter")
    parser.add_argument("--cover", help="Override cover image from frontmatter")
    parser.add_argument("--save-html", help="Save HTML output to a file")
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"Error: File not found: {args.file}", file=sys.stderr)
        return 1

    result = parse_markdown_file(args.file, title_override=args.title, cover_override=args.cover)
    if args.save_html:
        Path(args.save_html).write_text(result["html"], encoding="utf-8")
        print(f"[parse_markdown] HTML saved to: {args.save_html}", file=sys.stderr)
    if args.html_only or args.output == "html":
        print(result["html"])
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
