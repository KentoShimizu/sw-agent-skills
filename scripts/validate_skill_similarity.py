#!/usr/bin/env python3
"""Detect near-duplicate SKILL.md documents by normalized text similarity."""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from dataclasses import dataclass
from pathlib import Path

DEFAULT_SIMILARITY_THRESHOLD = 0.96
SKILLS_ROOT = Path("skills")


@dataclass(frozen=True)
class SkillDocument:
    path: Path
    normalized_body: str


def normalize_markdown(text: str) -> str:
    body = text
    if body.startswith("---\n"):
        parts = body.split("\n---\n", 1)
        if len(parts) == 2:
            body = parts[1]

    lines = []
    for raw_line in body.splitlines():
        stripped = raw_line.strip()
        if stripped.startswith("# "):
            continue
        if not stripped:
            continue
        lines.append(stripped.lower())

    collapsed = " ".join(lines)
    collapsed = re.sub(r"\s+", " ", collapsed).strip()
    return collapsed


def load_skill_documents(root: Path) -> list[SkillDocument]:
    docs: list[SkillDocument] = []
    for skill_file in sorted(root.glob("*/SKILL.md")):
        text = skill_file.read_text(encoding="utf-8")
        docs.append(SkillDocument(path=skill_file, normalized_body=normalize_markdown(text)))
    return docs


def similarity_ratio(left: str, right: str) -> float:
    return difflib.SequenceMatcher(a=left, b=right).ratio()


def find_near_duplicates(docs: list[SkillDocument], threshold: float) -> list[tuple[float, Path, Path]]:
    findings: list[tuple[float, Path, Path]] = []
    for i, left in enumerate(docs):
        for right in docs[i + 1 :]:
            ratio = similarity_ratio(left.normalized_body, right.normalized_body)
            if ratio >= threshold:
                findings.append((ratio, left.path, right.path))
    findings.sort(key=lambda item: item[0], reverse=True)
    return findings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate SKILL.md similarity")
    parser.add_argument(
        "--threshold",
        type=float,
        default=DEFAULT_SIMILARITY_THRESHOLD,
        help=f"Similarity threshold in [0, 1]. Default: {DEFAULT_SIMILARITY_THRESHOLD}",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    threshold = args.threshold
    if threshold < 0.0 or threshold > 1.0:
        print("threshold must be between 0 and 1")
        return 2

    docs = load_skill_documents(SKILLS_ROOT)
    findings = find_near_duplicates(docs, threshold)

    if findings:
        print("validation=failed")
        for ratio, left, right in findings:
            print(f"- similarity={ratio:.4f} {left} <-> {right}")
        return 1

    print("validation=ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
