#!/usr/bin/env python3
"""
Check that runtime skill docs do not contain design-source narration.

This script scans the implementation layer under skills/ and flags prose that
belongs in specs/ instead, such as "设计来源", "上游", "吸收了", or
"保留的部分 / 改造的部分".
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class Rule:
    name: str
    pattern: re.Pattern[str]
    message: str


RULES = [
    Rule(
        name="design-source",
        pattern=re.compile(r"设计来源"),
        message="设计来源应放在 specs/，不应出现在 skills/ 运行层。",
    ),
    Rule(
        name="upstream",
        pattern=re.compile(r"上游(?:仓库|repo|skill|实现|共识)?"),
        message="上游来源叙述应放在 specs/，不应出现在 skills/ 运行层。",
    ),
    Rule(
        name="learned-from",
        pattern=re.compile(r"((?:核心|主要|明显)?吸收(?:了)?|(?:核心|主要|明显)?参考了|借鉴了)"),
        message="来源/借鉴说明应放在 specs/，不应出现在 skills/ 运行层。",
    ),
    Rule(
        name="learned-from-alt",
        pattern=re.compile(r"(学习自|改自|源于)"),
        message="来源说明应放在 specs/，不应出现在 skills/ 运行层。",
    ),
    Rule(
        name="design-diff",
        pattern=re.compile(r"(保留的部分|改造的部分)"),
        message="设计对比应放在 specs/，不应出现在 skills/ 运行层。",
    ),
    Rule(
        name="pulled-from-upstream",
        pattern=re.compile(r"从.+抽出.+共同部分"),
        message="历史来源表述应放在 specs/，不应出现在 skills/ 运行层。",
    ),
    Rule(
        name="upstream-comparison",
        pattern=re.compile(r"(两个上游实现|和上游实现不同)"),
        message="实现层应写当前规则，不应写上游比较。",
    ),
]


def iter_skill_docs(root: Path) -> list[Path]:
    paths: list[Path] = []
    skills_dir = root / "skills"

    for skill_dir in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
        candidates = [skill_dir / "SKILL.md"]
        for subdir in ("references", "assets"):
            doc_dir = skill_dir / subdir
            if doc_dir.exists():
                candidates.extend(sorted(p for p in doc_dir.rglob("*") if p.is_file() and p.suffix == ".md"))
        openai_yaml = skill_dir / "agents" / "openai.yaml"
        if openai_yaml.exists():
            candidates.append(openai_yaml)

        for path in candidates:
            if path.exists():
                paths.append(path)

    return paths


def strip_frontmatter(text: str, suffix: str) -> str:
    if suffix != ".md":
        return text
    if not text.startswith("---\n"):
        return text
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return text
    return parts[1]


def strip_fenced_code_blocks(text: str, suffix: str) -> str:
    if suffix != ".md":
        return text

    lines = text.splitlines()
    cleaned: list[str] = []
    in_fence = False

    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            cleaned.append("")
            continue
        if in_fence:
            cleaned.append("")
            continue
        cleaned.append(line)

    return "\n".join(cleaned)


def normalize_text(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    text = strip_frontmatter(text, path.suffix)
    text = strip_fenced_code_blocks(text, path.suffix)
    return text.splitlines()


def main() -> int:
    findings: list[str] = []

    for path in iter_skill_docs(ROOT):
        rel = path.relative_to(ROOT)
        lines = normalize_text(path)
        for lineno, line in enumerate(lines, start=1):
            if not line.strip():
                continue
            for rule in RULES:
                if rule.pattern.search(line):
                    findings.append(
                        f"{rel}:{lineno}: {rule.name}: {rule.message}\n"
                        f"  {line.strip()}"
                    )

    if findings:
        print("Found implementation-layer boundary violations:\n")
        print("\n".join(findings))
        return 1

    print("No implementation-layer boundary violations found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
