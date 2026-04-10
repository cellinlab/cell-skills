#!/usr/bin/env python3
"""
Quick structural checks for a generated perspective skill SKILL.md.

Usage:
    python3 quality_check.py path/to/SKILL.md
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


def section_block(content: str, pattern: str) -> str:
    match = re.search(pattern, content, flags=re.IGNORECASE | re.DOTALL | re.MULTILINE)
    return match.group(1) if match else ""


def count_models(content: str) -> tuple[bool, str]:
    block = section_block(
        content, r"##\s+(?:Core Mental Models|核心心智模型)(.*?)(?=\n##\s|\Z)"
    )
    count = len(re.findall(r"^###\s+(?:Model|模型)\s*\d", block, flags=re.MULTILINE))
    passed = 3 <= count <= 7
    return passed, f"{count} models {'OK' if passed else '(need 3-7)'}"


def count_heuristics(content: str) -> tuple[bool, str]:
    block = section_block(
        content, r"##\s+(?:Decision Heuristics|决策启发式)(.*?)(?=\n##\s|\Z)"
    )
    count = len(re.findall(r"^\s*\d+\.", block, flags=re.MULTILINE))
    passed = 5 <= count <= 10
    return passed, f"{count} heuristics {'OK' if passed else '(need 5-10)'}"


def check_expression_dna(content: str) -> tuple[bool, str]:
    block = section_block(content, r"##\s+(?:Expression DNA|表达 DNA)(.*?)(?=\n##\s|\Z)")
    markers = len(
        re.findall(r"句式|词汇|节奏|幽默|确定性|禁忌|sentence|vocabulary|rhythm|humor", block, flags=re.IGNORECASE)
    )
    passed = bool(block.strip()) and markers >= 3
    return passed, f"expression markers={markers} {'OK' if passed else '(need >=3)'}"


def check_tensions(content: str) -> tuple[bool, str]:
    block = section_block(
        content,
        r"##\s+(?:Values, Anti-patterns, and Tensions|价值观.*张力)(.*?)(?=\n##\s|\Z)",
    )
    markers = len(re.findall(r"张力|矛盾|tension|paradox|既.*又|一方面.*另一方面", block, flags=re.IGNORECASE))
    passed = bool(block.strip()) and markers >= 1
    return passed, f"tension markers={markers} {'OK' if passed else '(need >=1)'}"


def check_boundary(content: str) -> tuple[bool, str]:
    block = section_block(content, r"##\s+(?:Honest Boundary|诚实边界)(.*?)(?=\n##\s|\Z)")
    items = len(re.findall(r"^\s*[-*]\s+", block, flags=re.MULTILINE))
    passed = items >= 3
    return passed, f"{items} boundary items {'OK' if passed else '(need >=3)'}"


def check_sources(content: str) -> tuple[bool, str]:
    block = section_block(content, r"##\s+(?:Sources|来源)(.*?)(?=\n##\s|\Z)")
    passed = bool(block.strip())
    return passed, "sources section OK" if passed else "sources section missing"


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python3 quality_check.py <SKILL.md>")
        return 1

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"File not found: {path}")
        return 1

    content = path.read_text(encoding="utf-8")
    checks = [
        ("Core models", count_models),
        ("Heuristics", count_heuristics),
        ("Expression DNA", check_expression_dna),
        ("Tensions", check_tensions),
        ("Honest boundary", check_boundary),
        ("Sources", check_sources),
    ]

    passed_count = 0
    for label, fn in checks:
        passed, detail = fn(content)
        print(f"{label:16} {'PASS' if passed else 'FAIL'}  {detail}")
        if passed:
            passed_count += 1

    total = len(checks)
    print(f"\nResult: {passed_count}/{total} passed")
    return 0 if passed_count == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
