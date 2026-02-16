#!/usr/bin/env python3
"""Run skill quality gates and contract validators in a single command."""

from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

ARCH_VALIDATOR = Path("skills/architecture-principles/scripts/validate_architecture_contract.py")
DESIGN_VALIDATOR = Path("skills/design-principles/scripts/validate_design_contract.py")
API_VALIDATOR = Path("skills/api-design-rest/scripts/validate_api_contract.py")
GIT_VALIDATOR = Path("skills/git-branch-strategy/scripts/validate_git_contract.py")
REQUIREMENTS_VALIDATOR = Path("skills/requirements-definition/scripts/validate_requirements_contract.py")

ARCH_SAMPLE_DIR = Path("skills/architecture-principles/references/samples")
API_SAMPLE_DIR = Path("skills/api-design-rest/assets")
REQUIREMENTS_SAMPLE_DIR = Path("skills/requirements-definition/references/samples")

TRIGGER_MATRIX_VALIDATOR = Path("scripts/validate_trigger_matrix_sync.py")
LINK_VALIDATOR = Path("scripts/validate_skill_links.py")
ABSOLUTE_PATH_VALIDATOR = Path("scripts/validate_no_absolute_paths.py")
SCRIPT_TEST_PATH = Path("scripts/tests")
SCRIPT_TEST_PATTERN = "test_*.py"


@dataclass(frozen=True)
class ValidationTask:
    name: str
    command: list[str]


@dataclass(frozen=True)
class ValidationResult:
    task: ValidationTask
    return_code: int
    stdout: str
    stderr: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run all skill quality gates")
    parser.add_argument(
        "--architecture-manifest",
        action="append",
        default=[],
        help="Architecture manifest path. Repeatable.",
    )
    parser.add_argument(
        "--design-manifest",
        action="append",
        default=[],
        help="Design manifest path. Repeatable.",
    )
    parser.add_argument(
        "--api-manifest",
        action="append",
        default=[],
        help="API manifest path. Repeatable.",
    )
    parser.add_argument(
        "--git-manifest",
        action="append",
        default=[],
        help="Git manifest path. Repeatable.",
    )
    parser.add_argument(
        "--requirements-manifest",
        action="append",
        default=[],
        help="Requirements manifest path. Repeatable.",
    )
    parser.add_argument(
        "--run-architecture-samples",
        action="store_true",
        help="Run architecture validator against reference sample manifests.",
    )
    parser.add_argument(
        "--run-api-samples",
        action="store_true",
        help="Run API validator against reference sample manifests.",
    )
    parser.add_argument(
        "--run-requirements-samples",
        action="store_true",
        help="Run requirements validator against reference sample manifests.",
    )
    parser.add_argument(
        "--skip-trigger-sync",
        action="store_true",
        help="Skip trigger matrix consistency validation.",
    )
    parser.add_argument(
        "--skip-links",
        action="store_true",
        help="Skip markdown link validation.",
    )
    parser.add_argument(
        "--skip-absolute-paths",
        action="store_true",
        help="Skip absolute-path leak validation.",
    )
    parser.add_argument(
        "--skip-script-tests",
        action="store_true",
        help="Skip script unit tests.",
    )
    return parser.parse_args()


def add_manifest_tasks(
    tasks: list[ValidationTask],
    *,
    validator: Path,
    manifests: list[str],
    prefix: str,
) -> None:
    for manifest in manifests:
        manifest_path = Path(manifest)
        tasks.append(
            ValidationTask(
                name=f"{prefix}:{manifest_path}",
                command=[sys.executable, str(validator), "--manifest", str(manifest_path)],
            )
        )


def add_sample_tasks(
    tasks: list[ValidationTask],
    *,
    enabled: bool,
    validator: Path,
    sample_dir: Path,
    prefix: str,
) -> None:
    if not enabled:
        return

    if not sample_dir.exists():
        tasks.append(
            ValidationTask(
                name=f"{prefix}:samples_missing",
                command=[
                    sys.executable,
                    "-c",
                    (
                        "import sys; "
                        "print('sample directory not found: ' + sys.argv[1]); "
                        "sys.exit(1)"
                    ),
                    str(sample_dir),
                ],
            )
        )
        return

    for sample in sorted(sample_dir.glob("*.json")):
        tasks.append(
            ValidationTask(
                name=f"{prefix}:{sample}",
                command=[sys.executable, str(validator), "--manifest", str(sample)],
            )
        )


def build_tasks(args: argparse.Namespace) -> list[ValidationTask]:
    tasks: list[ValidationTask] = []

    add_manifest_tasks(
        tasks,
        validator=ARCH_VALIDATOR,
        manifests=args.architecture_manifest,
        prefix="architecture_manifest",
    )
    add_manifest_tasks(
        tasks,
        validator=DESIGN_VALIDATOR,
        manifests=args.design_manifest,
        prefix="design_manifest",
    )
    add_manifest_tasks(
        tasks,
        validator=API_VALIDATOR,
        manifests=args.api_manifest,
        prefix="api_manifest",
    )
    add_manifest_tasks(
        tasks,
        validator=GIT_VALIDATOR,
        manifests=args.git_manifest,
        prefix="git_manifest",
    )
    add_manifest_tasks(
        tasks,
        validator=REQUIREMENTS_VALIDATOR,
        manifests=args.requirements_manifest,
        prefix="requirements_manifest",
    )

    add_sample_tasks(
        tasks,
        enabled=args.run_architecture_samples,
        validator=ARCH_VALIDATOR,
        sample_dir=ARCH_SAMPLE_DIR,
        prefix="architecture_sample",
    )
    add_sample_tasks(
        tasks,
        enabled=args.run_api_samples,
        validator=API_VALIDATOR,
        sample_dir=API_SAMPLE_DIR,
        prefix="api_sample",
    )
    add_sample_tasks(
        tasks,
        enabled=args.run_requirements_samples,
        validator=REQUIREMENTS_VALIDATOR,
        sample_dir=REQUIREMENTS_SAMPLE_DIR,
        prefix="requirements_sample",
    )

    if not args.skip_trigger_sync:
        tasks.append(
            ValidationTask(
                name="trigger_matrix_sync",
                command=[sys.executable, str(TRIGGER_MATRIX_VALIDATOR)],
            )
        )

    if not args.skip_links:
        tasks.append(
            ValidationTask(
                name="skill_markdown_links",
                command=[sys.executable, str(LINK_VALIDATOR), "--root", "."],
            )
        )

    if not args.skip_absolute_paths:
        tasks.append(
            ValidationTask(
                name="no_absolute_paths",
                command=[sys.executable, str(ABSOLUTE_PATH_VALIDATOR)],
            )
        )

    if not args.skip_script_tests:
        tasks.append(
            ValidationTask(
                name="script_unit_tests",
                command=[
                    sys.executable,
                    "-m",
                    "unittest",
                    "discover",
                    "-s",
                    str(SCRIPT_TEST_PATH),
                    "-p",
                    SCRIPT_TEST_PATTERN,
                ],
            )
        )

    return tasks


def run_task(task: ValidationTask) -> ValidationResult:
    proc = subprocess.run(task.command, capture_output=True, text=True, check=False)
    return ValidationResult(
        task=task,
        return_code=proc.returncode,
        stdout=proc.stdout,
        stderr=proc.stderr,
    )


def print_output(prefix: str, text: str) -> None:
    normalized = text.strip()
    if not normalized:
        return
    for line in normalized.splitlines():
        print(f"  {prefix}: {line}")


def main() -> int:
    args = parse_args()
    tasks = build_tasks(args)

    if not tasks:
        print(
            "no validation tasks configured; provide manifest/sample flags or keep default gate checks enabled"
        )
        return 2

    results = [run_task(task) for task in tasks]
    failures = [result for result in results if result.return_code != 0]

    for result in results:
        status = "ok" if result.return_code == 0 else "failed"
        print(f"[{status}] {result.task.name}")
        print_output("stdout", result.stdout)
        print_output("stderr", result.stderr)

    if failures:
        print("validation=failed")
        print(f"total_tasks={len(results)}")
        print(f"failed_tasks={len(failures)}")
        return 1

    print("validation=ok")
    print(f"total_tasks={len(results)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
