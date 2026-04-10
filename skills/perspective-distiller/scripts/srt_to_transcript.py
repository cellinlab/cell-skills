#!/usr/bin/env python3
"""
Clean SRT or VTT subtitles into a readable transcript.

Usage:
    python3 srt_to_transcript.py input.srt [output.txt]
    python3 srt_to_transcript.py input.vtt [output.txt]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


def _clean_lines(content: str) -> list[str]:
    lines = content.strip().splitlines()
    texts: list[str] = []

    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        if re.fullmatch(r"\d+", line):
            continue
        if re.match(r"\d{2}:\d{2}:\d{2}", line):
            continue
        if line.startswith("WEBVTT"):
            continue
        if line.startswith("NOTE"):
            continue

        line = re.sub(r"<[^>]+>", "", line)
        line = re.sub(r"\s+(align|position|line|size):.*$", "", line).strip()
        if line:
            texts.append(line)

    deduped: list[str] = []
    for text in texts:
        if not deduped or deduped[-1] != text:
            deduped.append(text)
    return deduped


def to_transcript(content: str) -> str:
    chunks = _clean_lines(content)
    paragraphs: list[str] = []
    current: list[str] = []

    for chunk in chunks:
        current.append(chunk)
        joined = " ".join(current)
        if len(joined) >= 220 or re.search(r"[.!?。！？]$", chunk):
            paragraphs.append(joined)
            current = []

    if current:
        paragraphs.append(" ".join(current))

    return "\n\n".join(paragraphs).strip() + "\n"


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python3 srt_to_transcript.py <input.srt|input.vtt> [output.txt]")
        return 1

    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(f"Input file not found: {input_path}")
        return 1

    output_path = Path(sys.argv[2]) if len(sys.argv) >= 3 else input_path.with_name(
        f"{input_path.stem}_transcript.txt"
    )

    content = input_path.read_text(encoding="utf-8")
    transcript = to_transcript(content)
    output_path.write_text(transcript, encoding="utf-8")

    print(f"Wrote transcript: {output_path}")
    print(f"Characters: {len(transcript)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
