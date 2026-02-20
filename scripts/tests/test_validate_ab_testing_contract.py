#!/usr/bin/env python3
"""Regression tests for AB testing contract validation behavior."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

MODULE_PATH = (
    Path(__file__).resolve().parents[2]
    / "skills"
    / "ab-testing"
    / "scripts"
    / "validate_ab_testing_contract.py"
)
MODULE_NAME = "validate_ab_testing_contract_module"


def load_validator_module():
    spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"failed to load module spec: {MODULE_PATH}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[MODULE_NAME] = module
    spec.loader.exec_module(module)
    return module


def base_checks() -> dict[str, object]:
    return {
        "id_format_validated": True,
        "pre_registration_complete": True,
        "randomization_plan_defined": True,
        "assignment_unit_defined": True,
        "instrumentation_validated": True,
        "srm_monitor_defined": True,
        "guardrail_policy_defined": True,
        "one_primary_metric_defined": True,
        "no_posthoc_decision_rule_changes": True,
        "external_user_impact": False,
    }


def base_decision_context() -> dict[str, object]:
    return {
        "decision_question": "Should the new recommendation ranker replace baseline ranking?",
        "primary_decision_metric": "weekly_retained_users",
        "false_positive_cost": "high",
        "false_negative_cost": "medium",
        "allowed_actions": ["ship", "iterate", "rollback", "hold"],
        "assignment_unit": "user",
        "randomization_method": "hash(user_id) modulo 100",
        "contamination_risk_mitigation": "Assignment is shared across app and web.",
    }


def base_evidence_plan() -> dict[str, object]:
    return {
        "min_detectable_effect_pct": 1.5,
        "confidence_level": 0.95,
        "power_target": 0.8,
        "minimum_runtime_days": 14,
        "baseline_window_days": 28,
        "analysis_method": "fixed_horizon",
        "multiplicity_control": "Holm-Bonferroni across two secondary metrics.",
    }


class ValidateAbTestingContractTest(unittest.TestCase):
    def test_plan_valid_manifest_passes(self) -> None:
        module = load_validator_module()
        manifest = {
            "artifact_id": "AB-PLN-20260216-001",
            "state": "approved",
            "approvers": ["Experiment Owner", "Data Science Reviewer"],
            "checks": base_checks(),
            "decision_context": base_decision_context(),
            "evidence_plan": base_evidence_plan(),
            "guardrails": ["p95_latency <= +30ms", "error_rate <= +0.20% absolute"],
        }

        errors = module.validate_manifest(manifest)
        self.assertEqual([], errors)

    def test_external_user_impact_requires_privacy_approver(self) -> None:
        module = load_validator_module()
        manifest = {
            "artifact_id": "AB-PLN-20260216-001",
            "state": "approved",
            "approvers": ["Experiment Owner", "Data Science Reviewer"],
            "checks": {**base_checks(), "external_user_impact": True},
            "decision_context": base_decision_context(),
            "evidence_plan": base_evidence_plan(),
            "guardrails": ["p95_latency <= +30ms", "error_rate <= +0.20% absolute"],
        }

        errors = module.validate_manifest(manifest)
        self.assertIn(
            "Legal Reviewer or Privacy Reviewer is required when checks.external_user_impact is true",
            errors,
        )

    def test_plan_rejects_short_runtime_window(self) -> None:
        module = load_validator_module()
        manifest = {
            "artifact_id": "AB-PLN-20260216-001",
            "state": "approved",
            "approvers": ["Experiment Owner", "Data Science Reviewer"],
            "checks": base_checks(),
            "decision_context": base_decision_context(),
            "evidence_plan": {
                **base_evidence_plan(),
                "minimum_runtime_days": 3,
            },
            "guardrails": ["p95_latency <= +30ms"],
        }

        errors = module.validate_manifest(manifest)
        self.assertIn("evidence_plan.minimum_runtime_days must be >= 7", errors)

    def test_decision_rejects_ship_on_failed_guardrail(self) -> None:
        module = load_validator_module()
        manifest = {
            "artifact_id": "AB-DEC-20260216-001",
            "state": "finalized",
            "approvers": ["Experiment Owner", "Data Science Reviewer"],
            "checks": base_checks(),
            "decision_context": base_decision_context(),
            "result": {
                "decision_outcome": "ship",
                "primary_metric_effect_pct": 2.1,
                "uncertainty_interval": "[+0.5%, +3.7%]",
                "guardrail_status": "fail",
                "interpretation": "Primary metric improved but guardrails regressed.",
                "complies_with_pre_registered_rules": True,
                "follow_up_actions": ["Rollback and run root-cause analysis."],
            },
        }

        errors = module.validate_manifest(manifest)
        self.assertIn(
            "result.decision_outcome cannot be ship when result.guardrail_status is fail",
            errors,
        )

    def test_decision_valid_manifest_passes(self) -> None:
        module = load_validator_module()
        manifest = {
            "artifact_id": "AB-DEC-20260216-001",
            "state": "finalized",
            "approvers": ["Experiment Owner", "Data Science Reviewer"],
            "checks": base_checks(),
            "decision_context": base_decision_context(),
            "result": {
                "decision_outcome": "iterate",
                "primary_metric_effect_pct": 0.4,
                "uncertainty_interval": "[-0.3%, +1.1%]",
                "guardrail_status": "pass",
                "interpretation": "Effect remains below pre-registered material threshold.",
                "complies_with_pre_registered_rules": True,
                "follow_up_actions": [
                    "Increase runtime by seven days.",
                    "Refine feature weights and rerun.",
                ],
            },
        }

        errors = module.validate_manifest(manifest)
        self.assertEqual([], errors)


if __name__ == "__main__":
    unittest.main()
