#!/usr/bin/env python3
"""
Export a horizontal-vertical research report from Markdown to PDF.

Usage:
  python md_to_pdf.py input.md output.pdf --title "Title" --author "Cell 细胞"
  python md_to_pdf.py input.md output.pdf --html-only

Dependencies:
  pip install markdown weasyprint --break-system-packages
"""

from __future__ import annotations

import argparse
import html
import os
import re
import sys
from pathlib import Path

import markdown


CSS = """
@page {
  size: A4;
  margin: 22mm 18mm 18mm 18mm;

  @top-center {
    content: string(report-title);
    font-family: "PingFang SC", "Noto Sans CJK SC", "Microsoft YaHei", sans-serif;
    font-size: 8pt;
    color: #64748b;
    border-bottom: 0.5pt solid #cbd5e1;
    padding-bottom: 2.5mm;
  }

  @bottom-center {
    content: counter(page);
    font-family: "PingFang SC", "Noto Sans CJK SC", "Microsoft YaHei", sans-serif;
    font-size: 8pt;
    color: #64748b;
    border-top: 0.5pt solid #cbd5e1;
    padding-top: 2.5mm;
  }
}

@page :first {
  @top-center { content: none; }
  @bottom-center { content: none; }
}

body {
  font-family: "PingFang SC", "Noto Sans CJK SC", "Microsoft YaHei", sans-serif;
  color: #0f172a;
  font-size: 10.5pt;
  line-height: 1.75;
  text-align: justify;
}

.cover {
  page-break-after: always;
  text-align: center;
  padding-top: 40%;
}

.cover h1 {
  border: none;
  color: #0f172a;
  font-size: 26pt;
  margin-bottom: 6mm;
  page-break-before: avoid;
}

.cover .subtitle {
  color: #166534;
  font-size: 13pt;
  margin-bottom: 4mm;
}

.cover .meta,
.cover .author {
  color: #64748b;
  font-size: 10.5pt;
}

.cover .rule {
  width: 58%;
  margin: 8mm auto;
  border: none;
  border-top: 1.5pt solid #166534;
}

h1 {
  string-set: report-title content();
  color: #0f172a;
  font-size: 19pt;
  margin-top: 14mm;
  margin-bottom: 5mm;
  padding-bottom: 2mm;
  border-bottom: 1.5pt solid #166534;
  page-break-before: always;
}

h2 {
  color: #166534;
  font-size: 13.5pt;
  margin-top: 8mm;
  margin-bottom: 3mm;
}

h3 {
  color: #0f766e;
  font-size: 11.5pt;
  margin-top: 5mm;
  margin-bottom: 2mm;
}

h4 {
  color: #334155;
  font-size: 10.5pt;
  margin-top: 4mm;
  margin-bottom: 1mm;
}

p {
  margin: 1.5mm 0;
  orphans: 3;
  widows: 3;
}

blockquote {
  margin: 4mm 0;
  padding: 3mm 4mm 3mm 8mm;
  background: #f8fafc;
  border-left: 3pt solid #166534;
  color: #334155;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin: 4mm 0;
  font-size: 9.5pt;
}

thead th {
  background: #166534;
  color: #ffffff;
  text-align: left;
  padding: 2.5mm;
}

tbody td {
  border-bottom: 0.5pt solid #cbd5e1;
  padding: 2.3mm 2.5mm;
}

tbody tr:nth-child(even) {
  background: #f8fafc;
}

code {
  font-family: "SFMono-Regular", "Menlo", monospace;
  font-size: 9pt;
  background: #eff6ff;
  color: #1d4ed8;
  padding: 0.4mm 1.2mm;
  border-radius: 2pt;
}

pre code {
  display: block;
  white-space: pre-wrap;
  padding: 3mm;
}

ul, ol {
  margin: 2mm 0;
  padding-left: 7mm;
}

li {
  margin-bottom: 1mm;
}

a {
  color: #0f766e;
  text-decoration: none;
}

hr {
  border: none;
  border-top: 0.5pt solid #cbd5e1;
  margin: 4mm 0;
}
"""


def extract_title(markdown_text: str, fallback: str) -> tuple[str, str]:
    match = re.search(r"^\s*#\s+(.+?)\s*$", markdown_text, flags=re.MULTILINE)
    if not match:
        return fallback, markdown_text

    title = match.group(1).strip()
    remaining = markdown_text[: match.start()] + markdown_text[match.end() :]
    return title, remaining.lstrip("\n")


def extract_meta_line(markdown_text: str) -> str:
    for line in markdown_text.splitlines():
        stripped = line.strip()
        if stripped.startswith(">"):
            candidate = stripped.lstrip(">").strip()
            if "研究时间" in candidate or "所属领域" in candidate or "研究对象类型" in candidate:
                return html.escape(candidate)
    return ""


def build_cover(title: str, meta_line: str, author: str) -> str:
    meta_html = f"<div class='meta'>{meta_line}</div>" if meta_line else ""
    return f"""
    <section class="cover">
      <h1>{html.escape(title)}</h1>
      <div class="subtitle">横纵分析研究报告</div>
      {meta_html}
      <hr class="rule">
      <div class="author">作者：{html.escape(author)}</div>
    </section>
    """


def build_html(markdown_text: str, title_arg: str | None, author: str) -> str:
    derived_title, body_md = extract_title(markdown_text, "横纵分析研究报告")
    title = title_arg or derived_title
    meta_line = extract_meta_line(markdown_text)
    body_html = markdown.markdown(
        body_md,
        extensions=["tables", "fenced_code", "nl2br"],
        output_format="html5",
    )

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <style>{CSS}</style>
</head>
<body>
  {build_cover(title, meta_line, author)}
  {body_html}
</body>
</html>
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Markdown to PDF for horizontal-vertical research reports")
    parser.add_argument("input", help="Input markdown path")
    parser.add_argument("output", help="Output PDF path")
    parser.add_argument("--title", default=None, help="Override the report title")
    parser.add_argument("--author", default="Cell 细胞", help="Author name shown on cover")
    parser.add_argument(
        "--html-only",
        action="store_true",
        help="Only render the intermediate HTML and skip PDF generation",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)
    markdown_text = input_path.read_text(encoding="utf-8")
    html_text = build_html(markdown_text, args.title, args.author)

    html_path = output_path.with_suffix(".html")
    html_path.write_text(html_text, encoding="utf-8")
    print(f"[ok] HTML written to {html_path}")

    if args.html_only:
        print("[ok] Skipped PDF generation because --html-only was set")
        return

    try:
        from weasyprint import HTML
    except Exception as exc:  # pragma: no cover - depends on local native libs
        print(
            "[error] Could not import WeasyPrint runtime dependencies. "
            "The HTML draft is ready, but PDF export is unavailable in this environment.",
            file=sys.stderr,
        )
        print(
            "[hint] On macOS, install the native libraries required by WeasyPrint "
            "(for example via Homebrew: glib pango cairo gdk-pixbuf) and retry.",
            file=sys.stderr,
        )
        print(f"[hint] HTML fallback is available at: {html_path}", file=sys.stderr)
        raise SystemExit(1) from exc

    try:
        HTML(string=html_text, base_url=os.getcwd()).write_pdf(str(output_path))
    except Exception as exc:  # pragma: no cover - depends on local native libs
        print(
            "[error] PDF generation failed after HTML export. "
            f"Inspect the HTML draft at {html_path} and verify native WeasyPrint dependencies.",
            file=sys.stderr,
        )
        raise SystemExit(1) from exc

    print(f"[ok] PDF written to {output_path}")


if __name__ == "__main__":
    main()
