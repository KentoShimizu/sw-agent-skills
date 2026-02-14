#!/usr/bin/env python3
"""Lint CODEOWNERS file for common ownership and routing issues."""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Rule:
    line_no: int
    pattern: str
    owners: tuple[str, ...]


@dataclass(frozen=True)
class Finding:
    level: str
    message: str
    line_no: int | None = None


def parse_rules(path: Path) -> list[Rule]:
    rules: list[Rule] = []
    text = path.read_text(encoding="utf-8")
    for line_no, raw in enumerate(text.splitlines(), start=1):
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue

        fields = stripped.split()
        if len(fields) < 2:
            raise ValueError(f"line {line_no}: CODEOWNERS rule must contain pattern and owner")

        pattern = fields[0]
        owners = tuple(fields[1:])
        rules.append(Rule(line_no=line_no, pattern=pattern, owners=owners))
    return rules


def is_valid_owner(owner: str) -> bool:
    if owner.startswith("@"):
        return True
    if "@" in owner:
        return True
    return False


def lint_rules(
    rules: list[Rule], required_patterns: set[str], policy: str
) -> list[Finding]:
    findings: list[Finding] = []
    seen_patterns: dict[str, Rule] = {}

    for idx, rule in enumerate(rules):
        for owner in rule.owners:
            if not is_valid_owner(owner):
                findings.append(
                    Finding(
                        level="ERROR",
                        line_no=rule.line_no,
                        message=f"invalid owner format: {owner}",
                    )
                )

        previous = seen_patterns.get(rule.pattern)
        if previous is not None:
            findings.append(
                Finding(
                    level="WARNING",
                    line_no=rule.line_no,
                    message=(
                        f"duplicate pattern '{rule.pattern}' (previously defined on line {previous.line_no})"
                    ),
                )
            )
        else:
            seen_patterns[rule.pattern] = rule

        if rule.pattern == "*" and idx != len(rules) - 1:
            if policy == "team":
                findings.append(
                    Finding(
                        level="ERROR",
                        line_no=rule.line_no,
                        message="catch-all '*' must be the last CODEOWNERS rule (team policy)",
                    )
                )
            else:
                findings.append(
                    Finding(
                        level="WARNING",
                        line_no=rule.line_no,
                        message=(
                            "catch-all '*' is not last; valid in GitHub semantics but"
                            " discouraged by team policy"
                        ),
                    )
                )

    for pattern in sorted(required_patterns):
        if pattern not in seen_patterns:
            findings.append(
                Finding(
                    level="ERROR",
                    message=f"required pattern missing: {pattern}",
                )
            )

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint CODEOWNERS")
    parser.add_argument(
        "--path",
        default=".github/CODEOWNERS",
        help="Path to CODEOWNERS file",
    )
    parser.add_argument(
        "--require-pattern",
        action="append",
        default=[],
        help="Require specific pattern to exist (repeatable)",
    )
    parser.add_argument(
        "--policy",
        choices=["team", "github"],
        default="team",
        help="Validation policy: team (strict catch-all order) or github (spec semantics)",
    )
    args = parser.parse_args()

    path = Path(args.path)
    if not path.exists():
        print(f"ERROR: CODEOWNERS file not found: {path}")
        return 2

    try:
        rules = parse_rules(path)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    findings = lint_rules(rules, set(args.require_pattern), args.policy)
    has_error = False
    for finding in findings:
        prefix = f"{finding.level}"
        if finding.line_no is not None:
            prefix += f" line={finding.line_no}"
        print(f"{prefix}: {finding.message}")
        if finding.level == "ERROR":
            has_error = True

    if not findings:
        print("lint=ok")
    return 1 if has_error else 0


if __name__ == "__main__":
    sys.exit(main())
