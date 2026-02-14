#!/usr/bin/env python3
"""Detect host-specific absolute paths in skill documentation."""

from __future__ import annotations

import argparse
import re
import sys
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

SCAN_ROOT = Path(".")
DEFAULT_PATTERNS = (
    "references/**/*.md",
    "skills/**/*.md",
    "skills/**/*.py",
    "scripts/**/*.py",
)

# Detect host-specific paths that are non-portable across machines.
POSIX_HOST_PATH = re.compile(r"(?<![A-Za-z0-9_])/(Users|home|root|var/folders)/[^\s`\"'<>]+")
WINDOWS_HOST_PATH = re.compile(r"\b[A-Za-z]:\\(?:[^\\/:*?\"<>|\r\n]+\\)+[^\\/:*?\"<>|\r\n]+")


@dataclass(frozen=True)
class Finding:
    file: Path
    line: int
    path_text: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate that docs do not contain host-specific absolute paths")
    parser.add_argument(
        "--root",
        default=str(SCAN_ROOT),
        help=f"Root directory to scan. Default: {SCAN_ROOT}",
    )
    parser.add_argument(
        "--pattern",
        action="append",
        dest="patterns",
        help="Glob pattern under --root. Repeatable.",
    )
    return parser.parse_args()


def find_host_absolute_paths(root: Path, patterns: Iterable[str]) -> list[Finding]:
    findings: list[Finding] = []
    for pattern in patterns:
        for file_path in sorted(root.glob(pattern)):
            if not file_path.is_file():
                continue

            text = file_path.read_text(encoding="utf-8")
            for line_no, line in enumerate(text.splitlines(), start=1):
                for match in POSIX_HOST_PATH.finditer(line):
                    findings.append(Finding(file=file_path, line=line_no, path_text=match.group(0)))
                for match in WINDOWS_HOST_PATH.finditer(line):
                    findings.append(Finding(file=file_path, line=line_no, path_text=match.group(0)))
    return findings


def main() -> int:
    args = parse_args()
    root = Path(args.root)

    if not root.exists():
        print(f"scan root not found: {root}")
        return 2

    patterns = args.patterns if args.patterns else list(DEFAULT_PATTERNS)
    findings = find_host_absolute_paths(root=root, patterns=patterns)
    if findings:
        print("validation=failed")
        for finding in findings:
            print(f"- {finding.file}:{finding.line} contains non-portable absolute path: {finding.path_text}")
        return 1

    print("validation=ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
