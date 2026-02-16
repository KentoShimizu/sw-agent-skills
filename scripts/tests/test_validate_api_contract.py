#!/usr/bin/env python3
"""Regression tests for API contract validation behavior."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

MODULE_PATH = (
    Path(__file__).resolve().parents[2]
    / "skills"
    / "api-design-rest"
    / "scripts"
    / "validate_api_contract.py"
)
MODULE_NAME = "validate_api_contract_module"


def load_validator_module():
    spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"failed to load module spec: {MODULE_PATH}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[MODULE_NAME] = module
    spec.loader.exec_module(module)
    return module


def common_checks() -> dict[str, bool]:
    return {
        "id_format_validated": True,
        "backward_compatibility_reviewed": True,
        "transport_selection_documented": True,
        "naming_convention_defined": True,
        "authz_modeled": True,
        "error_contract_defined": True,
        "observability_fields_defined": True,
        "runbook_updated": True,
        "timeout_budget_defined": True,
        "delivery_semantics_defined": True,
        "backpressure_strategy_defined": False,
        "connection_lifecycle_defined": False,
        "consumer_idempotency_defined": False,
        "no_fallback_logic": True,
        "rate_limit_policy_defined": False,
        "handles_sensitive_data": False,
        "external_public_api": False,
        "regulated_jurisdiction_impact": False,
    }


def base_decision_context() -> dict[str, object]:
    return {
        "api_audience": "internal",
        "interaction_mode": "sync",
        "primary_transport": "rest",
        "selection_rationale": "Synchronous internal read/write paths require predictable request-response behavior.",
        "alternatives_considered": ["graphql", "grpc"],
        "naming_convention_summary": "Path nouns and query naming are standardized.",
        "threshold_method_summary": "Thresholds are derived from SLO budget and dependency limits.",
    }


def base_threshold_policy() -> dict[str, str]:
    return {
        "latency_target_derivation": "Derived from user journey p95 SLO.",
        "availability_target_derivation": "Derived from criticality tier and error budget policy.",
        "timeout_budget_derivation": "Derived from client-edge-service call-chain split.",
        "capacity_headroom_derivation": "Derived from peak forecast and failover margin.",
        "payload_limit_derivation": "Derived from network and serialization cost budget.",
        "concurrency_limit_derivation": "Derived from worker saturation and dependency constraints.",
        "retry_backoff_derivation": "Derived from idempotency and dependency failure profile.",
        "delivery_semantics_derivation": "Derived from duplicate tolerance and ordering requirements.",
    }


class ValidateApiContractTest(unittest.TestCase):
    def test_api_version_valid_manifest_passes(self) -> None:
        module = load_validator_module()
        manifest = {
            "artifact_id": "API-VER-20260215-001",
            "state": "reviewed",
            "approvers": ["API Owner", "Engineering Owner"],
            "checks": {
                **common_checks(),
                "compatibility_matrix_updated": True,
                "deprecation_policy_defined": True,
                "has_breaking_change": False,
            },
            "decision_context": base_decision_context(),
            "threshold_policy": base_threshold_policy(),
            "compatibility_matrix": {
                "supported_producer_versions": ["v1", "v2"],
                "tested_consumers": ["web-app"],
            },
        }

        errors = module.validate_manifest(manifest)
        self.assertEqual([], errors)

    def test_api_version_breaking_change_requires_deprecation_plan(self) -> None:
        module = load_validator_module()
        manifest = {
            "artifact_id": "API-VER-20260215-001",
            "state": "reviewed",
            "approvers": ["API Owner", "Engineering Owner"],
            "checks": {
                **common_checks(),
                "compatibility_matrix_updated": True,
                "deprecation_policy_defined": True,
                "has_breaking_change": True,
            },
            "decision_context": base_decision_context(),
            "threshold_policy": base_threshold_policy(),
            "compatibility_matrix": {
                "supported_producer_versions": ["v1", "v2"],
                "tested_consumers": ["web-app"],
            },
        }

        errors = module.validate_manifest(manifest)
        self.assertIn(
            "deprecation_plan must be an object when checks.has_breaking_change is true",
            errors,
        )

    def test_api_version_rejects_short_deprecation_window(self) -> None:
        module = load_validator_module()
        manifest = {
            "artifact_id": "API-VER-20260215-001",
            "state": "reviewed",
            "approvers": ["API Owner", "Engineering Owner"],
            "checks": {
                **common_checks(),
                "compatibility_matrix_updated": True,
                "deprecation_policy_defined": True,
                "has_breaking_change": True,
            },
            "decision_context": base_decision_context(),
            "threshold_policy": base_threshold_policy(),
            "compatibility_matrix": {
                "supported_producer_versions": ["v1", "v2"],
                "tested_consumers": ["web-app"],
            },
            "deprecation_plan": {
                "target_version": "v2",
                "deprecation_window_days": 30,
                "migration_guide_link": "https://example.com/migration",
            },
        }

        errors = module.validate_manifest(manifest)
        self.assertIn("deprecation_plan.deprecation_window_days must be >= 90", errors)

    def test_external_public_api_requires_governance_approver(self) -> None:
        module = load_validator_module()
        manifest = {
            "artifact_id": "API-RES-20260215-001",
            "state": "draft",
            "approvers": ["API Owner", "Engineering Owner"],
            "checks": {
                **common_checks(),
                "external_public_api": True,
                "rate_limit_policy_defined": True,
                "http_semantics_validated": True,
                "idempotency_strategy_defined": True,
            },
            "decision_context": {
                **base_decision_context(),
                "api_audience": "external",
                "primary_transport": "rest",
            },
            "threshold_policy": base_threshold_policy(),
        }

        errors = module.validate_manifest(manifest)
        self.assertIn("missing required approver: API Governance Reviewer", errors)

    def test_async_transport_requires_backpressure_strategy(self) -> None:
        module = load_validator_module()
        manifest = {
            "artifact_id": "API-CDC-20260215-001",
            "state": "active",
            "approvers": ["API Owner", "Engineering Owner"],
            "checks": {
                **common_checks(),
                "consumer_matrix_current": True,
                "ci_blocking_enabled": True,
                "backpressure_strategy_defined": False,
            },
            "decision_context": {
                **base_decision_context(),
                "interaction_mode": "async",
                "primary_transport": "queue",
            },
            "threshold_policy": base_threshold_policy(),
            "compatibility_matrix": {
                "supported_producer_versions": ["v1"],
                "tested_consumers": ["worker-a"],
            },
        }

        errors = module.validate_manifest(manifest)
        self.assertIn("checks.backpressure_strategy_defined must be true", errors)


if __name__ == "__main__":
    unittest.main()
