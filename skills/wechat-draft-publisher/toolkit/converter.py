"""
Minimal Markdown -> WeChat HTML converter for publish-only workflows.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import markdown
import yaml
from bs4 import BeautifulSoup


OUTER_CONTAINER_STYLE = (
    "max-width: 100%; color: #2c2c2c; font-size: 16px; "
    "line-height: 1.75; word-break: break-word;"
)


INLINE_STYLES: dict[str, str] = {
    "h1": "font-size: 24px; line-height: 1.35; margin: 0 0 24px; color: #111827; font-weight: 700;",
    "h2": "font-size: 20px; line-height: 1.45; margin: 32px 0 16px; color: #111827; font-weight: 700;",
    "h3": "font-size: 18px; line-height: 1.5; margin: 24px 0 12px; color: #111827; font-weight: 700;",
    "h4": "font-size: 17px; line-height: 1.5; margin: 20px 0 10px; color: #111827; font-weight: 700;",
    "h5": "font-size: 16px; line-height: 1.5; margin: 18px 0 8px; color: #111827; font-weight: 700;",
    "h6": "font-size: 15px; line-height: 1.5; margin: 18px 0 8px; color: #111827; font-weight: 700;",
    "p": "margin: 0 0 16px; color: #2c2c2c; line-height: 1.75; font-size: 16px;",
    "blockquote": "margin: 24px 0; padding: 14px 18px; border-left: 4px solid #cbd5e1; background: #f8fafc; color: #475569;",
    "pre": "margin: 24px 0; padding: 16px; white-space: pre-wrap; word-wrap: break-word; overflow-x: auto; background: #0f172a; color: #e2e8f0; border-radius: 10px;",
    "code": "font-family: Menlo, Consolas, Monaco, monospace; font-size: 14px;",
    "ul": "margin: 0 0 16px; padding-left: 24px;",
    "ol": "margin: 0 0 16px; padding-left: 24px;",
    "li": "margin: 0 0 8px; color: #2c2c2c; line-height: 1.75;",
    "table": "width: 100%; border-collapse: collapse; margin: 24px 0; font-size: 14px;",
    "th": "border: 1px solid #e2e8f0; padding: 10px 12px; background: #f8fafc; text-align: left;",
    "td": "border: 1px solid #e2e8f0; padding: 10px 12px; vertical-align: top;",
    "hr": "border: none; border-top: 1px solid #e2e8f0; margin: 32px 0;",
    "a": "color: #2563eb; text-decoration: underline;",
    "strong": "font-weight: 700; color: #111827;",
    "em": "font-style: italic;",
}


@dataclass
class DocumentMeta:
    title: str = ""
    digest: str = ""
    author: str = ""
    cover: str = ""


@dataclass
class ConvertResult:
    html: str
    title: str
    digest: str
    images: list[str] = field(default_factory=list)
    meta: DocumentMeta = field(default_factory=DocumentMeta)


class WeChatConverter:
    def convert_file(self, input_path: str) -> ConvertResult:
        path = Path(input_path)
        if not path.exists():
            raise FileNotFoundError(f"Input file not found: {input_path}")
        return self.convert(path.read_text(encoding="utf-8"))

    def convert(self, markdown_text: str) -> ConvertResult:
        meta, body = _extract_frontmatter(markdown_text)
        title = meta.title or _extract_title(body)
        body = _strip_h1(body)
        body = _fix_cjk_spacing(body)

        html = markdown.Markdown(
            extensions=[
                "markdown.extensions.fenced_code",
                "markdown.extensions.tables",
                "markdown.extensions.nl2br",
                "markdown.extensions.sane_lists",
            ]
        ).convert(body)

        soup = BeautifulSoup(html, "html.parser")
        images = _process_images(soup)
        _apply_inline_styles(soup)
        _apply_wechat_fixes(soup)

        body_html = "".join(str(node) for node in soup.contents)
        wrapped_html = f'<section data-wechat-draft-publisher="article" style="{OUTER_CONTAINER_STYLE}">{body_html}</section>'
        digest = meta.digest or _generate_digest(wrapped_html)

        return ConvertResult(
            html=wrapped_html,
            title=title,
            digest=digest,
            images=images,
            meta=meta,
        )


def preview_html(body_html: str, title: str = "WeChat Preview") -> str:
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <style>
    :root {{
      color-scheme: light;
    }}
    * {{
      box-sizing: border-box;
    }}
    body {{
      margin: 0;
      padding: 32px 16px;
      font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Hiragino Sans GB",
        "Microsoft YaHei", sans-serif;
      background:
        radial-gradient(circle at top, #dbeafe 0%, transparent 32%),
        linear-gradient(180deg, #f8fafc 0%, #eef2ff 100%);
      color: #111827;
    }}
    .frame {{
      max-width: 420px;
      margin: 0 auto;
      padding: 14px;
      border-radius: 28px;
      background: #111827;
      box-shadow: 0 32px 80px rgba(15, 23, 42, 0.18);
    }}
    .screen {{
      min-height: 720px;
      background: #ffffff;
      border-radius: 22px;
      padding: 28px 20px 36px;
      overflow: hidden;
    }}
    .meta {{
      max-width: 420px;
      margin: 0 auto 16px;
      text-align: center;
      color: #475569;
      font-size: 13px;
    }}
  </style>
</head>
<body>
  <div class="meta">本地预览，仅用于检查排版与图片替换效果</div>
  <div class="frame">
    <div class="screen">
      {body_html}
    </div>
  </div>
</body>
</html>"""


def _extract_frontmatter(markdown_text: str) -> tuple[DocumentMeta, str]:
    if not markdown_text.startswith("---\n"):
        return DocumentMeta(), markdown_text

    parts = markdown_text.split("\n---\n", 1)
    if len(parts) != 2:
        return DocumentMeta(), markdown_text

    raw_frontmatter = parts[0][4:]
    body = parts[1]
    try:
        data = yaml.safe_load(raw_frontmatter) or {}
    except Exception:
        return DocumentMeta(), markdown_text

    if not isinstance(data, dict):
        return DocumentMeta(), markdown_text

    return (
        DocumentMeta(
            title=str(data.get("title", "") or ""),
            digest=str(data.get("digest", "") or ""),
            author=str(data.get("author", "") or ""),
            cover=str(data.get("cover", "") or ""),
        ),
        body,
    )


def _extract_title(text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# ") and not stripped.startswith("## "):
            return stripped[2:].strip()
    return ""


def _strip_h1(text: str) -> str:
    return "\n".join(
        line
        for line in text.splitlines()
        if not (line.strip().startswith("# ") and not line.strip().startswith("## "))
    )


def _fix_cjk_spacing(text: str) -> str:
    cjk = r"[\u4e00-\u9fff\u3400-\u4dbf\u3000-\u303f\uff00-\uffef]"
    latin = r"[A-Za-z0-9]"

    lines: list[str] = []
    in_code_block = False

    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            lines.append(line)
            continue
        if in_code_block:
            lines.append(line)
            continue

        line = re.sub(f"({cjk})({latin})", r"\1 \2", line)
        line = re.sub(f"({latin})({cjk})", r"\1 \2", line)
        lines.append(line)

    return "\n".join(lines)


def _process_images(soup: BeautifulSoup) -> list[str]:
    images: list[str] = []
    for img in soup.find_all("img"):
        src = img.get("src", "")
        if src:
            images.append(src)
        existing = img.get("style", "")
        additions = "max-width: 100%; height: auto; display: block; margin: 24px auto;"
        img["style"] = f"{existing}; {additions}".strip("; ") if existing else additions
    return images


def _apply_inline_styles(soup: BeautifulSoup) -> None:
    for tag_name, style in INLINE_STYLES.items():
        for node in soup.find_all(tag_name):
            existing = node.get("style", "")
            node["style"] = f"{existing}; {style}".strip("; ") if existing else style


def _apply_wechat_fixes(soup: BeautifulSoup) -> None:
    for paragraph in soup.find_all("p"):
        style = paragraph.get("style", "")
        if "color" not in style:
            paragraph["style"] = f"{style}; color: #2c2c2c".strip("; ")

    for pre in soup.find_all("pre"):
        style = pre.get("style", "")
        if "white-space" not in style:
            pre["style"] = f"{style}; white-space: pre-wrap; word-wrap: break-word".strip("; ")


def _generate_digest(html: str, max_bytes: int = 120) -> str:
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(separator=" ", strip=True)
    text = re.sub(r"\s+", " ", text).strip()

    if not text:
        return ""

    ellipsis = "..."
    if len(text.encode("utf-8")) <= max_bytes:
        return text

    target_bytes = max_bytes - len(ellipsis.encode("utf-8"))
    truncated = text.encode("utf-8")[:target_bytes].decode("utf-8", errors="ignore").rstrip()
    return truncated + ellipsis
