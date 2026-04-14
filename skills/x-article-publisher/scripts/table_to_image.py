#!/usr/bin/env python3
"""
Convert Markdown table to PNG image.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Error: Pillow not installed. Run: pip install pillow", file=sys.stderr)
    raise SystemExit(1)


def parse_markdown_table(content: str) -> tuple[list[str], list[list[str]], list[str]]:
    lines = [line.strip() for line in content.strip().split("\n") if line.strip()]
    if len(lines) < 2:
        raise ValueError("Table must have at least 2 rows")

    def parse_cells(line: str) -> list[str]:
        line = line.strip()
        if line.startswith("|"):
            line = line[1:]
        if line.endswith("|"):
            line = line[:-1]
        return [cell.strip() for cell in line.split("|")]

    separator_idx = -1
    for idx, line in enumerate(lines):
        if re.match(r"^\|?[\s]*:?-{2,}:?[\s]*(\|[\s]*:?-{2,}:?[\s]*)*\|?$", line):
            separator_idx = idx
            break

    if separator_idx > 0:
        headers = parse_cells(lines[separator_idx - 1])
        separator_cells = parse_cells(lines[separator_idx])
        alignments: list[str] = []
        for cell in separator_cells:
            cell = cell.strip()
            if cell.startswith(":") and cell.endswith(":"):
                alignments.append("center")
            elif cell.endswith(":"):
                alignments.append("right")
            else:
                alignments.append("left")
        rows = [parse_cells(line) for line in lines[separator_idx + 1 :]]
    else:
        headers = []
        rows = [parse_cells(line) for line in lines]
        alignments = ["left"] * (len(rows[0]) if rows else 0)

    return headers, rows, alignments


def get_font(size: int):
    font_paths = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/TTF/DejaVuSans.ttf",
        "C:/Windows/Fonts/msyh.ttc",
        "C:/Windows/Fonts/arial.ttf",
    ]

    for path in font_paths:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue

    return ImageFont.load_default()


def render_table_to_image(headers: list[str], rows: list[list[str]], alignments: list[str], scale: int = 2) -> Image.Image:
    font_size = 14 * scale
    padding_x = 16 * scale
    padding_y = 12 * scale
    margin = 20 * scale
    border_radius = 8 * scale

    background = (255, 255, 255)
    header_background = (249, 250, 251)
    text_color = (55, 65, 81)
    header_text = (17, 24, 39)
    border_color = (229, 231, 235)

    regular_font = get_font(font_size)
    bold_font = get_font(font_size)

    col_count = len(headers) if headers else (len(rows[0]) if rows else 0)
    col_widths = [0] * col_count

    temp = Image.new("RGB", (1, 1))
    temp_draw = ImageDraw.Draw(temp)

    for idx, header in enumerate(headers):
        bbox = temp_draw.textbbox((0, 0), header, font=bold_font)
        col_widths[idx] = max(col_widths[idx], bbox[2] - bbox[0])

    for row in rows:
        for idx, cell in enumerate(row):
            if idx < col_count:
                bbox = temp_draw.textbbox((0, 0), cell, font=regular_font)
                col_widths[idx] = max(col_widths[idx], bbox[2] - bbox[0])

    col_widths = [width + padding_x * 2 for width in col_widths]
    row_height = font_size + padding_y * 2
    header_height = row_height if headers else 0
    table_width = sum(col_widths)
    table_height = header_height + len(rows) * row_height

    image = Image.new("RGB", (table_width + margin * 2, table_height + margin * 2), background)
    draw = ImageDraw.Draw(image)

    x0, y0 = margin, margin
    x1, y1 = margin + table_width, margin + table_height
    draw.rounded_rectangle([x0, y0, x1, y1], radius=border_radius, outline=border_color, width=scale)

    y = margin
    if headers:
        draw.rounded_rectangle([x0, y0, x1, y0 + row_height], radius=border_radius, fill=header_background)
        draw.rectangle([x0, y0 + row_height - border_radius, x1, y0 + row_height], fill=header_background)
        draw.line([(x0, y + row_height), (x1, y + row_height)], fill=border_color, width=scale)

        x = margin
        for idx, header in enumerate(headers):
            bbox = draw.textbbox((0, 0), header, font=bold_font)
            text_width = bbox[2] - bbox[0]
            alignment = alignments[idx] if idx < len(alignments) else "left"
            if alignment == "center":
                text_x = x + (col_widths[idx] - text_width) // 2
            elif alignment == "right":
                text_x = x + col_widths[idx] - text_width - padding_x
            else:
                text_x = x + padding_x
            draw.text((text_x, y + padding_y), header, fill=header_text, font=bold_font)
            x += col_widths[idx]
        y += row_height

    for row_idx, row in enumerate(rows):
        if row_idx < len(rows) - 1:
            draw.line([(x0, y + row_height), (x1, y + row_height)], fill=border_color, width=scale)

        x = margin
        for idx, cell in enumerate(row):
            if idx >= col_count:
                break
            bbox = draw.textbbox((0, 0), cell, font=regular_font)
            text_width = bbox[2] - bbox[0]
            alignment = alignments[idx] if idx < len(alignments) else "left"
            if alignment == "center":
                text_x = x + (col_widths[idx] - text_width) // 2
            elif alignment == "right":
                text_x = x + col_widths[idx] - text_width - padding_x
            else:
                text_x = x + padding_x
            draw.text((text_x, y + padding_y), cell, fill=text_color, font=regular_font)
            x += col_widths[idx]
        y += row_height

    return image


def main() -> int:
    if len(sys.argv) < 3:
        print("Usage: python3 table_to_image.py <input.md> <output.png> [--scale N]", file=sys.stderr)
        return 1

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    scale = 2
    if "--scale" in sys.argv:
        idx = sys.argv.index("--scale")
        if idx + 1 < len(sys.argv):
            try:
                scale = int(sys.argv[idx + 1])
            except ValueError:
                pass

    content = Path(input_path).read_text(encoding="utf-8")
    headers, rows, alignments = parse_markdown_table(content)
    image = render_table_to_image(headers, rows, alignments, scale=scale)
    image.save(output_path)
    print(f"Table image saved to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
