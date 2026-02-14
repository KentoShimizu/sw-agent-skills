#!/usr/bin/env python3
"""Generate draft release notes from commit history."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

BREAKING_PATTERN = re.compile(r"(^[a-z]+!\:)|breaking", re.IGNORECASE)


@dataclass(frozen=True)
class Commit:
    sha: str
    subject: str
    author: str


def run_git(args: list[str], cwd: Path) -> str:
    cmd = ["git", *args]
    proc = subprocess.run(
        cmd,
        cwd=str(cwd),
        check=False,
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"command failed: {' '.join(cmd)}\n{proc.stderr.strip()}")
    return proc.stdout


def load_commits(repo_dir: Path, from_ref: str, to_ref: str) -> list[Commit]:
    payload = run_git(
        ["log", "--pretty=format:%H\t%s\t%an", f"{from_ref}..{to_ref}"],
        repo_dir,
    )
    commits: list[Commit] = []
    for line in payload.splitlines():
        parts = line.split("\t", 2)
        if len(parts) != 3:
            raise RuntimeError("unexpected git log output format")
        commits.append(Commit(sha=parts[0], subject=parts[1], author=parts[2]))
    return commits


def classify(subject: str) -> str:
    s = subject.strip().lower()
    if BREAKING_PATTERN.search(s):
        return "breaking"
    if s.startswith("feat"):
        return "features"
    if s.startswith("fix"):
        return "fixes"
    if s.startswith("docs"):
        return "documentation"
    if s.startswith("test"):
        return "tests"
    return "maintenance"


def render_release_notes(version: str, from_ref: str, to_ref: str, commits: list[Commit]) -> str:
    groups: dict[str, list[Commit]] = {
        "breaking": [],
        "features": [],
        "fixes": [],
        "documentation": [],
        "tests": [],
        "maintenance": [],
    }

    for commit in commits:
        groups[classify(commit.subject)].append(commit)

    def section(title: str, key: str) -> list[str]:
        entries = groups[key]
        out = [f"## {title}"]
        if not entries:
            out.append("- None")
            return out
        for c in entries:
            out.append(f"- {c.subject} (`{c.sha[:7]}`, {c.author})")
        return out

    lines: list[str] = []
    lines.append(f"# Release {version}")
    lines.append("")
    lines.append(f"Range: `{from_ref}..{to_ref}`")
    lines.append(f"Total commits: {len(commits)}")
    lines.append("")
    lines.extend(section("Breaking Changes", "breaking"))
    lines.append("")
    lines.extend(section("Features", "features"))
    lines.append("")
    lines.extend(section("Fixes", "fixes"))
    lines.append("")
    lines.extend(section("Documentation", "documentation"))
    lines.append("")
    lines.extend(section("Tests", "tests"))
    lines.append("")
    lines.extend(section("Maintenance", "maintenance"))
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Draft release notes from git history")
    parser.add_argument("--repo", default=".", help="Path to repository")
    parser.add_argument("--version", required=True, help="Release version label")
    parser.add_argument("--from-ref", required=True, help="Start reference (exclusive)")
    parser.add_argument("--to-ref", default="HEAD", help="End reference (inclusive)")
    parser.add_argument("--out", help="Write output to file")
    args = parser.parse_args()

    repo_dir = Path(args.repo).resolve()
    try:
        commits = load_commits(repo_dir, args.from_ref, args.to_ref)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    if not commits:
        print("no commits found in range", file=sys.stderr)
        return 1

    notes = render_release_notes(args.version, args.from_ref, args.to_ref, commits)

    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(notes, encoding="utf-8")
        print(str(out_path))
    else:
        print(notes)

    return 0


if __name__ == "__main__":
    sys.exit(main())
