#!/usr/bin/env python3
"""Regression tests for git contract validation behavior."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

MODULE_PATH = (
    Path(__file__).resolve().parents[2]
    / "skills"
    / "git-branch-strategy"
    / "scripts"
    / "validate_git_contract.py"
)
MODULE_NAME = "validate_git_contract_module"


def load_validator_module():
    spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"failed to load module spec: {MODULE_PATH}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[MODULE_NAME] = module
    spec.loader.exec_module(module)
    return module


def build_manifest(
    artifact_id: str,
    state: str,
    checks_extra: dict[str, bool] | None = None,
    approvers_extra: list[str] | None = None,
) -> dict[str, object]:
    checks: dict[str, bool] = {
        "id_format_validated": True,
        "branch_protection_verified": True,
        "ci_required_checks_green": True,
        "secret_scan_passed": True,
        "history_rewrite_policy_compliant": True,
        "handles_personal_data": False,
    }
    if checks_extra:
        checks.update(checks_extra)

    approvers = ["Repository Owner", "Engineering Owner"]
    if approvers_extra:
        approvers.extend(approvers_extra)

    return {
        "artifact_id": artifact_id,
        "state": state,
        "approvers": approvers,
        "checks": checks,
    }


class ValidateGitContractTest(unittest.TestCase):
    def test_invalid_state_does_not_require_prs_execution_keys(self) -> None:
        module = load_validator_module()
        manifest = build_manifest("GIT-PRS-20260215-001", "invalid")
        errors = module.validate_manifest(manifest)
        self.assertEqual([], errors)

    def test_invalid_state_does_not_require_rbs_execution_keys(self) -> None:
        module = load_validator_module()
        manifest = build_manifest("GIT-RBS-20260215-001", "invalid")
        errors = module.validate_manifest(manifest)
        self.assertEqual([], errors)

    def test_invalid_state_does_not_require_rel_execution_keys(self) -> None:
        module = load_validator_module()
        manifest = build_manifest(
            "GIT-REL-20260215-001",
            "invalid",
            approvers_extra=["Security Reviewer"],
        )
        errors = module.validate_manifest(manifest)
        self.assertEqual([], errors)

    def test_non_invalid_state_without_prs_signals_does_not_require_execution_keys(self) -> None:
        module = load_validator_module()
        manifest = build_manifest("GIT-PRS-20260215-001", "executed")
        errors = module.validate_manifest(manifest)
        self.assertEqual([], errors)

    def test_prs_signal_requires_execution_consistency(self) -> None:
        module = load_validator_module()
        manifest = build_manifest(
            "GIT-PRS-20260215-001",
            "executed",
            checks_extra={"pr_opened": True},
        )
        errors = module.validate_manifest(manifest)
        self.assertIn(
            "one of checks.merge_sync_used or checks.rebase_used must be true for "
            "PR-sync style manifests",
            errors,
        )


if __name__ == "__main__":
    unittest.main()
