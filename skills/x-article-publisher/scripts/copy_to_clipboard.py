#!/usr/bin/env python3
"""
Copy image or HTML to system clipboard for X Articles publishing.
"""

from __future__ import annotations

import argparse
import io
import os
import sys
from pathlib import Path


def compress_image(image_path: str, quality: int = 85, max_size: tuple[int, int] = (2000, 2000)) -> bytes:
    from PIL import Image

    image = Image.open(image_path)
    if image.mode in ("RGBA", "P"):
        image = image.convert("RGB")
    image.thumbnail(max_size, Image.Resampling.LANCZOS)

    buffer = io.BytesIO()
    image.save(buffer, format="JPEG", quality=quality, optimize=True)
    return buffer.getvalue()


def copy_image_to_clipboard_macos(image_path: str, quality: int | None = None) -> bool:
    try:
        from AppKit import NSPasteboard, NSPasteboardTypePNG, NSPasteboardTypeTIFF
        from Foundation import NSData
        from PIL import Image
    except ImportError as exc:
        print(f"Error: Missing dependency: {exc}", file=sys.stderr)
        print("Install with: pip install Pillow pyobjc-framework-Cocoa", file=sys.stderr)
        return False

    try:
        if quality:
            image_data = compress_image(image_path, quality)
        else:
            image_data = Path(image_path).read_bytes()

        pasteboard = NSPasteboard.generalPasteboard()
        pasteboard.clearContents()
        ext = Path(image_path).suffix.lower()

        if ext == ".png":
            ns_data = NSData.dataWithBytes_length_(image_data, len(image_data))
            pasteboard.setData_forType_(ns_data, NSPasteboardTypePNG)
        else:
            image = Image.open(io.BytesIO(image_data))
            tiff_buffer = io.BytesIO()
            image.save(tiff_buffer, format="TIFF")
            tiff_data = NSData.dataWithBytes_length_(tiff_buffer.getvalue(), len(tiff_buffer.getvalue()))
            pasteboard.setData_forType_(tiff_data, NSPasteboardTypeTIFF)
        return True
    except Exception as exc:
        print(f"Error copying image: {exc}", file=sys.stderr)
        return False


def copy_html_to_clipboard_macos(html: str) -> bool:
    try:
        from AppKit import NSPasteboard, NSPasteboardTypeHTML, NSPasteboardTypeString
        from Foundation import NSData
    except ImportError as exc:
        print(f"Error: Missing dependency: {exc}", file=sys.stderr)
        print("Install with: pip install pyobjc-framework-Cocoa", file=sys.stderr)
        return False

    try:
        pasteboard = NSPasteboard.generalPasteboard()
        pasteboard.clearContents()
        html_data = html.encode("utf-8")
        ns_data = NSData.dataWithBytes_length_(html_data, len(html_data))
        pasteboard.setData_forType_(ns_data, NSPasteboardTypeHTML)
        pasteboard.setString_forType_(html, NSPasteboardTypeString)
        return True
    except Exception as exc:
        print(f"Error copying HTML: {exc}", file=sys.stderr)
        return False


def copy_image_to_clipboard_windows(image_path: str, quality: int | None = None) -> bool:
    try:
        import win32clipboard
        from PIL import Image
    except ImportError as exc:
        print(f"Error: Missing dependency: {exc}", file=sys.stderr)
        print("Install with: pip install Pillow pywin32", file=sys.stderr)
        return False

    try:
        if quality:
            image_data = compress_image(image_path, quality)
            image = Image.open(io.BytesIO(image_data))
        else:
            image = Image.open(image_path)

        if image.mode in ("RGBA", "P", "LA"):
            image = image.convert("RGB")

        output = io.BytesIO()
        image.save(output, format="BMP")
        dib = output.getvalue()[14:]
        output.close()

        win32clipboard.OpenClipboard()
        try:
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(win32clipboard.CF_DIB, dib)
        finally:
            win32clipboard.CloseClipboard()
        return True
    except Exception as exc:
        print(f"Error copying image: {exc}", file=sys.stderr)
        return False


def copy_html_to_clipboard_windows(html: str) -> bool:
    try:
        from clipboard import Clipboard
    except ImportError as exc:
        print(f"Error: Missing dependency: {exc}", file=sys.stderr)
        print("Install with: pip install clip-util", file=sys.stderr)
        return False

    try:
        with Clipboard() as clipboard:
            clipboard["html"] = html
        return True
    except Exception as exc:
        print(f"Error copying HTML: {exc}", file=sys.stderr)
        return False


def copy_image_to_clipboard(image_path: str, quality: int | None = None) -> bool:
    if sys.platform == "darwin":
        return copy_image_to_clipboard_macos(image_path, quality)
    if sys.platform == "win32":
        return copy_image_to_clipboard_windows(image_path, quality)
    print(f"Error: Unsupported platform: {sys.platform}", file=sys.stderr)
    return False


def copy_html_to_clipboard(html: str) -> bool:
    if sys.platform == "darwin":
        return copy_html_to_clipboard_macos(html)
    if sys.platform == "win32":
        return copy_html_to_clipboard_windows(html)
    print(f"Error: Unsupported platform: {sys.platform}", file=sys.stderr)
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Copy image or HTML to clipboard")
    subparsers = parser.add_subparsers(dest="type", required=True)

    image_parser = subparsers.add_parser("image", help="Copy image to clipboard")
    image_parser.add_argument("path", help="Path to image file")
    image_parser.add_argument("--quality", type=int, default=None, help="JPEG quality (1-100)")

    html_parser = subparsers.add_parser("html", help="Copy HTML to clipboard")
    html_parser.add_argument("content", nargs="?", help="HTML content")
    html_parser.add_argument("--file", "-f", help="Read HTML from file")

    args = parser.parse_args()

    if args.type == "image":
        if not os.path.exists(args.path):
            print(f"Error: Image not found: {args.path}", file=sys.stderr)
            return 1
        ok = copy_image_to_clipboard(args.path, args.quality)
        if ok:
            print(f"Image copied to clipboard: {args.path}")
        return 0 if ok else 1

    if args.file:
        if not os.path.exists(args.file):
            print(f"Error: File not found: {args.file}", file=sys.stderr)
            return 1
        html = Path(args.file).read_text(encoding="utf-8")
    elif args.content:
        html = args.content
    else:
        html = sys.stdin.read()

    ok = copy_html_to_clipboard(html)
    if ok:
        print(f"HTML copied to clipboard ({len(html)} chars)")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
