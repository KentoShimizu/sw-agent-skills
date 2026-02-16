#!/usr/bin/env python3
"""Run contract validators in one command."""

from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

ARCH_VALIDATOR = Path("skills/architecture-principles/scripts/validate_architecture_contract.py")
DESIGN_VALIDATOR = Path("skills/design-principles/scripts/validate_design_contract.py")
API_VALIDATOR = Path("skills/api-design-rest/scripts/validate_api_contract.py")
ARCH_SAMPLE_DIR = Path("skills/architecture-principles/references/samples")
API_SAMPLE_DIR = Path("skills/api-design-rest/assets")


@dataclass(frozen=True)
class ValidationTask:
    validator: Path
    manifest: Path


@dataclass(frozen=True)
class ValidationResult:
    task: ValidationTask
    return_code: int
    stdout: str
    stderr: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run all relevant governance contract validators")
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
        "--run-architecture-samples",
        action="store_true",
        help="Run architecture validator against reference sample manifests.",
    )
    parser.add_argument(
        "--run-api-samples",
        action="store_true",
        help="Run API validator against reference sample manifests.",
    )
    return parser.parse_args()


def build_tasks(args: argparse.Namespace) -> list[ValidationTask]:
    tasks: list[ValidationTask] = []

    for manifest in args.architecture_manifest:
        tasks.append(ValidationTask(validator=ARCH_VALIDATOR, manifest=Path(manifest)))

    for manifest in args.design_manifest:
        tasks.append(ValidationTask(validator=DESIGN_VALIDATOR, manifest=Path(manifest)))

    for manifest in args.api_manifest:
        tasks.append(ValidationTask(validator=API_VALIDATOR, manifest=Path(manifest)))

    if args.run_architecture_samples and ARCH_SAMPLE_DIR.exists():
        for sample in sorted(ARCH_SAMPLE_DIR.glob("*.json")):
            tasks.append(ValidationTask(validator=ARCH_VALIDATOR, manifest=sample))

    if args.run_api_samples and API_SAMPLE_DIR.exists():
        for sample in sorted(API_SAMPLE_DIR.glob("*.json")):
            tasks.append(ValidationTask(validator=API_VALIDATOR, manifest=sample))

    if not tasks:
        raise SystemExit(
            "no validation tasks provided; pass --architecture-manifest/--design-manifest/--api-manifest "
            "or use --run-architecture-samples/--run-api-samples"
        )

    return tasks


def run_task(task: ValidationTask) -> ValidationResult:
    cmd = [sys.executable, str(task.validator), "--manifest", str(task.manifest)]
    proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
    return ValidationResult(task=task, return_code=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)


def main() -> int:
    args = parse_args()
    tasks = build_tasks(args)

    results = [run_task(task) for task in tasks]
    failures = [result for result in results if result.return_code != 0]

    if failures:
        print("validation=failed")
        for result in failures:
            print(f"- task failed: validator={result.task.validator} manifest={result.task.manifest}")
            stdout_text = result.stdout.strip()
            stderr_text = result.stderr.strip()
            if stdout_text:
                for line in stdout_text.splitlines():
                    print(f"  stdout: {line}")
            if stderr_text:
                for line in stderr_text.splitlines():
                    print(f"  stderr: {line}")
        return 1

    print("validation=ok")
    print(f"validated_tasks={len(results)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
