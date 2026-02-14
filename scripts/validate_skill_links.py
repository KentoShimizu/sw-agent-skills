#!/usr/bin/env python3
"""Validate repository-relative links referenced from markdown documents."""

from __future__ import annotations

import argparse
import re
import shlex
import sys
from dataclasses import dataclass
from pathlib import Path

SCAN_ROOT = Path(".")
DEFAULT_PATTERNS = (
    "skills/*/SKILL.md",
    "skills/*/references/**/*.md",
    "references/**/*.md",
)

MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
CODE_SPAN_PATTERN = re.compile(r"`([^`\n]+)`")

IGNORE_PREFIXES = (
    "http://",
    "https://",
    "mailto:",
    "#",
)

PATH_PREFIXES = (
    "skills/",
    "scripts/",
    "references/",
    "./",
    "../",
    "/",
)

PATH_EXTENSIONS = (".md", ".py", ".json", ".yaml", ".yml", ".toml", ".txt")
LEADING_WRAPPERS = "([{"
TRAILING_PUNCTUATION = ".,;:)]}"


@dataclass(frozen=True)
class CandidatePath:
    file: Path
    line: int
    raw_value: str


@dataclass(frozen=True)
class MissingPath:
    file: Path
    line: int
    raw_value: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate links in skill documentation")
    parser.add_argument(
        "--root",
        default=str(SCAN_ROOT),
        help=f"Directory root to scan. Default: {SCAN_ROOT}",
    )
    parser.add_argument(
        "--pattern",
        action="append",
        dest="patterns",
        help="Glob pattern under --root. Repeatable.",
    )
    parser.add_argument(
        "--allow-external-local",
        action="store_true",
        help="Allow existing local filesystem references outside --root.",
    )
    parser.add_argument(
        "--scan-code-spans",
        action="store_true",
        help="Also scan inline code spans (disabled by default).",
    )
    return parser.parse_args()


def is_bare_filename_path(value: str) -> bool:
    return "/" not in value and "\\" not in value and Path(value).suffix.lower() in PATH_EXTENSIONS


def looks_like_relevant_path(value: str, *, allow_bare_filename: bool) -> bool:
    path_portion = strip_link_suffixes(value)

    if path_portion.startswith(("skills/", "scripts/", "references/", "./", "../")):
        return True
    if path_portion.startswith("/") and path_portion.endswith(PATH_EXTENSIONS):
        return True
    if allow_bare_filename and is_bare_filename_path(path_portion):
        return True
    return False


def trim_wrapped_token(token: str) -> str:
    value = token.strip()
    if not value:
        return ""

    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"', "`"}:
        value = value[1:-1].strip()

    while value and value[0] in LEADING_WRAPPERS:
        value = value[1:].lstrip()

    while value and value[-1] in TRAILING_PUNCTUATION:
        value = value[:-1].rstrip()

    return value


def strip_link_suffixes(value: str) -> str:
    without_fragment = value.split("#", 1)[0]
    without_query = without_fragment.split("?", 1)[0]
    return without_query


def candidate_from_token(token: str, *, allow_bare_filename: bool) -> str | None:
    value = trim_wrapped_token(token)
    if not value:
        return None

    if value.startswith(IGNORE_PREFIXES):
        return None

    if value.startswith("$"):
        return None

    if any(ch in value for ch in ("<", ">", "*", "?", "{", "}")):
        return None

    path_portion = strip_link_suffixes(value)
    if not path_portion:
        return None

    if "/" not in path_portion and "\\" not in path_portion:
        if not allow_bare_filename:
            return None
        if not is_bare_filename_path(path_portion):
            return None
        return value

    if not any(path_portion.startswith(prefix) for prefix in PATH_PREFIXES):
        return None

    if path_portion.startswith("/") and not path_portion.endswith(PATH_EXTENSIONS):
        return None

    return value


def extract_candidates(file_path: Path, text: str, scan_code_spans: bool) -> list[CandidatePath]:
    candidates: list[CandidatePath] = []

    for line_no, line in enumerate(text.splitlines(), start=1):
        for match in MARKDOWN_LINK_PATTERN.finditer(line):
            target = match.group(1).strip()
            candidate = candidate_from_token(target, allow_bare_filename=True)
            if candidate is not None and looks_like_relevant_path(
                candidate, allow_bare_filename=True
            ):
                candidates.append(CandidatePath(file=file_path, line=line_no, raw_value=candidate))

        if scan_code_spans:
            for match in CODE_SPAN_PATTERN.finditer(line):
                code = match.group(1).strip()
                if not code:
                    continue

                try:
                    parts = shlex.split(code)
                except ValueError:
                    parts = code.split()

                for part in parts:
                    candidate = candidate_from_token(part, allow_bare_filename=False)
                    if candidate is not None and looks_like_relevant_path(
                        candidate, allow_bare_filename=False
                    ):
                        candidates.append(CandidatePath(file=file_path, line=line_no, raw_value=candidate))

    return candidates


def is_within_root(candidate: Path, root_resolved: Path) -> bool:
    try:
        candidate.resolve(strict=False).relative_to(root_resolved)
        return True
    except ValueError:
        return False


def candidate_exists_and_allowed(candidate: Path, root_resolved: Path, allow_external_local: bool) -> bool:
    if not candidate.exists():
        return False
    if allow_external_local:
        return True
    return is_within_root(candidate=candidate, root_resolved=root_resolved)


def path_exists_for_candidate(
    root: Path,
    source_file: Path,
    raw_value: str,
    allow_external_local: bool,
) -> bool:
    root_resolved = root.resolve(strict=False)
    normalized_value = strip_link_suffixes(raw_value)
    if not normalized_value:
        return False

    candidates: list[Path] = [
        source_file.parent / normalized_value,
        root / normalized_value,
    ]

    source_parts = source_file.parts
    if "skills" in source_parts:
        skills_index = source_parts.index("skills")
        if len(source_parts) > skills_index + 1:
            skill_root = Path(*source_parts[: skills_index + 2])
            candidates.append(skill_root / normalized_value)

    if normalized_value.startswith("/"):
        no_slash = normalized_value.lstrip("/")
        candidates.append(root / no_slash)
        candidates.append(root / "skills" / no_slash)

    if allow_external_local:
        candidates.append(Path(normalized_value))

    for candidate in candidates:
        if candidate_exists_and_allowed(
            candidate=candidate,
            root_resolved=root_resolved,
            allow_external_local=allow_external_local,
        ):
            return True

    return False


def validate_links(
    root: Path,
    patterns: list[str],
    allow_external_local: bool,
    scan_code_spans: bool,
) -> list[MissingPath]:
    missing: list[MissingPath] = []

    for pattern in patterns:
        for file_path in sorted(root.glob(pattern)):
            if not file_path.is_file():
                continue

            text = file_path.read_text(encoding="utf-8")
            for candidate in extract_candidates(
                file_path=file_path,
                text=text,
                scan_code_spans=scan_code_spans,
            ):
                if not path_exists_for_candidate(
                    root=root,
                    source_file=file_path,
                    raw_value=candidate.raw_value,
                    allow_external_local=allow_external_local,
                ):
                    missing.append(
                        MissingPath(
                            file=candidate.file,
                            line=candidate.line,
                            raw_value=candidate.raw_value,
                        )
                    )

    return missing


def main() -> int:
    args = parse_args()
    root = Path(args.root)

    if not root.exists():
        print(f"scan root not found: {root}")
        return 2

    patterns = args.patterns if args.patterns else list(DEFAULT_PATTERNS)
    missing = validate_links(
        root=root,
        patterns=patterns,
        allow_external_local=args.allow_external_local,
        scan_code_spans=args.scan_code_spans,
    )

    if missing:
        print("validation=failed")
        for item in missing:
            print(f"- {item.file}:{item.line} references missing path: {item.raw_value}")
        return 1

    print("validation=ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
