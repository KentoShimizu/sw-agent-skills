#!/usr/bin/env python3
"""Inspect failing GitHub PR checks and summarize actionable failures."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

FAIL_STATES = {
    "failure",
    "failed",
    "error",
    "cancelled",
    "timed_out",
    "action_required",
    "startup_failure",
}
RUN_ID_PATTERN = re.compile(r"/actions/runs/(\d+)")
ERROR_LINE_PATTERN = re.compile(r"error|failed|exception|traceback", re.IGNORECASE)


@dataclass(frozen=True)
class CheckRecord:
    name: str
    state: str
    link: str | None


@dataclass(frozen=True)
class FailureSummary:
    name: str
    state: str
    link: str | None
    run_id: str | None
    snippet: str | None
    snippet_error: str | None


def run_gh(args: list[str], cwd: Path) -> str:
    cmd = ["gh", *args]
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


def resolve_pr_number(repo_dir: Path, pr_value: str | None) -> int:
    if pr_value is not None:
        try:
            return int(pr_value)
        except ValueError as exc:
            raise RuntimeError("--pr must be a pull request number") from exc

    payload = run_gh(["pr", "view", "--json", "number"], repo_dir)
    data = json.loads(payload)
    if not isinstance(data, dict) or not isinstance(data.get("number"), int):
        raise RuntimeError("failed to resolve current branch PR number")
    return data["number"]


def load_checks(repo_dir: Path, pr_number: int) -> list[CheckRecord]:
    payload = run_gh(
        ["pr", "checks", str(pr_number), "--json", "name,state,link"],
        repo_dir,
    )
    data = json.loads(payload)
    if not isinstance(data, list):
        raise RuntimeError("unexpected response format from gh pr checks")

    checks: list[CheckRecord] = []
    for item in data:
        if not isinstance(item, dict):
            raise RuntimeError("invalid check entry from gh pr checks")

        name = item.get("name")
        state = item.get("state")
        link = item.get("link")

        if not isinstance(name, str) or not isinstance(state, str):
            raise RuntimeError("check entry missing required fields")
        if link is not None and not isinstance(link, str):
            raise RuntimeError("check entry contains invalid link type")

        checks.append(CheckRecord(name=name, state=state, link=link))

    return checks


def is_failure_state(state: str) -> bool:
    return state.strip().lower() in FAIL_STATES


def extract_run_id(link: str | None) -> str | None:
    if link is None:
        return None
    match = RUN_ID_PATTERN.search(link)
    if match is None:
        return None
    return match.group(1)


def summarize_error_message(message: str, max_len: int = 240) -> str:
    compact = " ".join(message.splitlines()).strip()
    if len(compact) <= max_len:
        return compact
    return compact[: max_len - 3] + "..."


def extract_failure_snippet(
    repo_dir: Path, run_id: str, max_lines: int
) -> tuple[str | None, str | None]:
    try:
        payload = run_gh(["run", "view", run_id, "--log"], repo_dir)
    except RuntimeError as exc:
        return None, summarize_error_message(str(exc))

    lines = payload.splitlines()
    if not lines:
        return None, None

    start = 0
    for index, line in enumerate(lines):
        if ERROR_LINE_PATTERN.search(line):
            start = max(0, index - 4)
            break

    end = min(len(lines), start + max_lines)
    snippet = "\n".join(lines[start:end]).strip() or None
    return snippet, None


def summarize_failures(repo_dir: Path, checks: list[CheckRecord], max_lines: int) -> list[FailureSummary]:
    failures: list[FailureSummary] = []
    for check in checks:
        if not is_failure_state(check.state):
            continue

        run_id = extract_run_id(check.link)
        snippet: str | None = None
        snippet_error: str | None = None
        if run_id is not None:
            snippet, snippet_error = extract_failure_snippet(repo_dir, run_id, max_lines)

        failures.append(
            FailureSummary(
                name=check.name,
                state=check.state,
                link=check.link,
                run_id=run_id,
                snippet=snippet,
                snippet_error=snippet_error,
            )
        )
    return failures


def render_text(pr_number: int, checks: list[CheckRecord], failures: list[FailureSummary]) -> str:
    lines: list[str] = []
    lines.append(f"pr={pr_number}")
    lines.append(f"checks_total={len(checks)}")
    lines.append(f"failures={len(failures)}")

    for idx, failure in enumerate(failures, start=1):
        lines.append(f"[{idx}] {failure.name} ({failure.state})")
        if failure.link is not None:
            lines.append(f"  link: {failure.link}")
        if failure.run_id is not None:
            lines.append(f"  run_id: {failure.run_id}")
        if failure.snippet:
            lines.append("  snippet:")
            for snippet_line in failure.snippet.splitlines():
                lines.append(f"    {snippet_line}")
        elif failure.snippet_error:
            lines.append(f"  snippet_error: {failure.snippet_error}")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect failing PR checks via gh")
    parser.add_argument("--repo", default=".", help="Path to repository")
    parser.add_argument("--pr", help="Pull request number")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    parser.add_argument(
        "--max-lines",
        type=int,
        default=60,
        help="Maximum log snippet lines per failure",
    )
    args = parser.parse_args()

    repo_dir = Path(args.repo).resolve()
    try:
        pr_number = resolve_pr_number(repo_dir, args.pr)
        checks = load_checks(repo_dir, pr_number)
        failures = summarize_failures(repo_dir, checks, args.max_lines)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    if args.json:
        payload = {
            "pr": pr_number,
            "checks_total": len(checks),
            "failures": [
                {
                    "name": f.name,
                    "state": f.state,
                    "link": f.link,
                    "run_id": f.run_id,
                    "snippet": f.snippet,
                    "snippet_error": f.snippet_error,
                }
                for f in failures
            ],
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(render_text(pr_number, checks, failures))

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
