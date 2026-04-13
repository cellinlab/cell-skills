#!/usr/bin/env python3
"""
Preview and publish Markdown content to WeChat Official Account drafts.
"""

from __future__ import annotations

import argparse
import sys
import webbrowser
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from converter import ConvertResult, WeChatConverter, preview_html
from publisher import create_draft
from wechat_api import get_access_token, get_public_ip, upload_cover, upload_image


SKILL_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATHS = [
    Path.cwd() / "config.yaml",
    SKILL_ROOT / "config.yaml",
    Path(__file__).resolve().parent / "config.yaml",
    Path.home() / ".config" / "wechat-draft-publisher" / "config.yaml",
]


@dataclass
class PreflightIssue:
    level: str
    message: str


def load_config(config_path: str | None = None) -> dict[str, Any]:
    if config_path:
        path = Path(config_path)
        if not path.exists():
            raise FileNotFoundError(f"Config file not found: {config_path}")
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}

    for path in CONFIG_PATHS:
        if path.exists():
            return yaml.safe_load(path.read_text(encoding="utf-8")) or {}

    return {}


def cmd_preview(args: argparse.Namespace) -> int:
    config = load_config(args.config)
    converter = WeChatConverter()
    result = converter.convert_file(args.input)

    title = args.title or result.title or Path(args.input).stem
    output = _write_preview(result, args.input, args.output, title)

    print(f"Title: {title}")
    print(f"Digest: {args.digest or result.digest}")
    print(f"Images: {len(result.images)}")
    print(f"Output: {output}")

    auto_open = _coerce_bool(config.get("preview", {}).get("auto_open"), True)
    if not args.no_open and auto_open:
        webbrowser.open(f"file://{output}")
        print("Opened in browser.")

    return 0


def cmd_publish(args: argparse.Namespace) -> int:
    config = load_config(args.config)
    converter = WeChatConverter()
    result = converter.convert_file(args.input)

    title = args.title or result.title or Path(args.input).stem
    digest = args.digest or result.digest
    wechat_config = config.get("wechat", {}) if isinstance(config.get("wechat"), dict) else {}
    author = args.author or result.meta.author or wechat_config.get("author", "")
    cover_path = args.cover or result.meta.cover
    preferred_cover_media_type = str(wechat_config.get("cover_media_type", "thumb"))

    issues = run_preflight(result, args.input, title, digest, cover_path)
    blocking = [issue for issue in issues if issue.level == "error"]
    warnings = [issue for issue in issues if issue.level == "warning"]

    print(f"Title: {title}")
    print(f"Digest: {digest}")
    print(f"Images found: {len(result.images)}")
    for issue in warnings:
        print(f"Warning: {issue.message}")

    if blocking:
        reason = " | ".join(issue.message for issue in blocking)
        return _fallback_to_preview(result, args.input, args.output, title, reason, strict=args.strict_publish)

    appid = args.appid or wechat_config.get("appid")
    secret = args.secret or wechat_config.get("secret")
    if not appid or not secret:
        reason = "missing wechat.appid or wechat.secret"
        return _fallback_to_preview(result, args.input, args.output, title, reason, strict=args.strict_publish)

    html = result.html
    try:
        token = get_access_token(str(appid), str(secret))
        print("Access token obtained.")

        html = _replace_local_images(
            access_token=token,
            html=html,
            image_sources=result.images,
            markdown_path=args.input,
        )

        thumb_media_id = None
        if cover_path:
            print(f"Uploading cover: {cover_path}")
            cover_result = upload_cover(token, str(_resolve_path(cover_path, args.input)), preferred_cover_media_type)
            thumb_media_id = cover_result.media_id
            print(f"  -> media_id: {thumb_media_id} (type={cover_result.media_type})")

        draft = create_draft(
            access_token=token,
            title=title,
            html=html,
            digest=digest,
            thumb_media_id=thumb_media_id,
            author=author,
        )
    except Exception as exc:
        return _fallback_to_preview(result, args.input, args.output, title, str(exc), strict=args.strict_publish)

    print(f"Draft created! media_id: {draft.media_id}")
    print("请到公众号后台草稿箱检查并手动发布。")
    return 0


def cmd_show_ip(_: argparse.Namespace) -> int:
    print(get_public_ip())
    return 0


def run_preflight(result: ConvertResult, input_path: str, title: str, digest: str, cover_path: str | None) -> list[PreflightIssue]:
    issues: list[PreflightIssue] = []

    if not title.strip():
        issues.append(PreflightIssue("error", "title is empty"))
    elif len(title.encode("utf-8")) > 64:
        issues.append(PreflightIssue("warning", "title exceeds 64 UTF-8 bytes and may be rejected"))

    if digest and len(digest.encode("utf-8")) > 120:
        issues.append(PreflightIssue("error", "digest exceeds 120 UTF-8 bytes"))

    if len(result.images) > 20:
        issues.append(PreflightIssue("error", "article contains more than 20 images"))

    if len(result.html.encode("utf-8")) > 2 * 1024 * 1024:
        issues.append(PreflightIssue("error", "generated HTML exceeds 2MB"))

    missing_images: list[str] = []
    oversized_images: list[str] = []
    for image_source in result.images:
        if image_source.startswith(("http://", "https://")):
            continue
        resolved = _resolve_path(image_source, input_path, must_exist=False)
        if not resolved.exists():
            missing_images.append(image_source)
            continue
        if resolved.stat().st_size > 5 * 1024 * 1024:
            oversized_images.append(image_source)

    if missing_images:
        issues.append(PreflightIssue("error", f"missing local images: {', '.join(missing_images)}"))
    if oversized_images:
        issues.append(PreflightIssue("error", f"images exceed 5MB: {', '.join(oversized_images)}"))

    if cover_path:
        resolved_cover = _resolve_path(cover_path, input_path, must_exist=False)
        if not resolved_cover.exists():
            issues.append(PreflightIssue("error", f"cover not found: {cover_path}"))
        elif resolved_cover.stat().st_size > 5 * 1024 * 1024:
            issues.append(PreflightIssue("error", f"cover exceeds 5MB: {cover_path}"))
    else:
        issues.append(PreflightIssue("error", "cover image missing; current draft flow requires a valid cover"))

    if len(_plain_text(result.html)) < 200:
        issues.append(PreflightIssue("warning", "content is shorter than 200 characters"))

    return issues


def _replace_local_images(access_token: str, html: str, image_sources: list[str], markdown_path: str) -> str:
    updated_html = html
    for image_source in image_sources:
        if image_source.startswith(("http://", "https://")):
            print(f"Skipping remote image: {image_source}")
            continue

        resolved = _resolve_path(image_source, markdown_path)
        print(f"Uploading image: {image_source}")
        wechat_url = upload_image(access_token, str(resolved))
        updated_html = updated_html.replace(image_source, wechat_url)
        print(f"  -> {wechat_url}")

    return updated_html


def _fallback_to_preview(
    result: ConvertResult,
    input_path: str,
    output_path: str | None,
    title: str,
    reason: str,
    strict: bool,
) -> int:
    if strict:
        print(f"Publish failed: {reason}", file=sys.stderr)
        return 1

    preview_path = _write_preview(result, input_path, output_path, title)
    print(f"Publish skipped: {reason}")
    print(f"Preview generated: {preview_path}")
    return 0


def _write_preview(result: ConvertResult, input_path: str, output_path: str | None, title: str) -> Path:
    source_path = Path(input_path)
    output = Path(output_path) if output_path else source_path.with_suffix(".wechat-preview.html")
    output.write_text(preview_html(result.html, title=title), encoding="utf-8")
    return output.resolve()


def _resolve_path(path_str: str, markdown_path: str, must_exist: bool = True) -> Path:
    candidate = Path(path_str)
    if candidate.is_absolute():
        resolved = candidate
    else:
        resolved = candidate if candidate.exists() else Path(markdown_path).resolve().parent / candidate

    if must_exist and not resolved.exists():
        raise FileNotFoundError(f"path not found: {path_str}")
    return resolved


def _plain_text(html: str) -> str:
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text(separator=" ", strip=True)


def _coerce_bool(value: Any, default: bool) -> bool:
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() not in {"0", "false", "no", "off"}
    return bool(value)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Publish Markdown to WeChat Official Account drafts")
    sub = parser.add_subparsers(dest="command", required=True)

    preview = sub.add_parser("preview", help="Generate a local HTML preview")
    preview.add_argument("input", help="Markdown file path")
    preview.add_argument("-o", "--output", help="Output preview path")
    preview.add_argument("--config", help="Config YAML path")
    preview.add_argument("--title", help="Override title for preview")
    preview.add_argument("--digest", help="Unused in preview, kept for parity")
    preview.add_argument("--no-open", action="store_true", help="Do not open browser automatically")
    preview.set_defaults(func=cmd_preview)

    publish = sub.add_parser("publish", help="Publish to WeChat drafts or fall back to preview")
    publish.add_argument("input", help="Markdown file path")
    publish.add_argument("-o", "--output", help="Preview output path when publish falls back")
    publish.add_argument("--config", help="Config YAML path")
    publish.add_argument("--appid", help="WeChat AppID override")
    publish.add_argument("--secret", help="WeChat AppSecret override")
    publish.add_argument("--title", help="Override article title")
    publish.add_argument("--digest", help="Override article digest")
    publish.add_argument("--author", help="Override article author")
    publish.add_argument("--cover", help="Cover image path")
    publish.add_argument("--strict-publish", action="store_true", help="Fail instead of falling back to preview")
    publish.set_defaults(func=cmd_publish)

    show_ip = sub.add_parser("show-ip", help="Print current public IP for whitelist setup")
    show_ip.set_defaults(func=cmd_show_ip)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
