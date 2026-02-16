#!/usr/bin/env python3
"""Validate API governance manifests against the canonical API contract."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

MIN_DEPRECATION_WINDOW_DAYS = 90

VALID_STATES_BY_PROFILE: dict[str, set[str]] = {
    "rest_api_design": {"draft", "reviewed", "approved", "deprecated"},
    "graphql_api_design": {"draft", "reviewed", "approved", "deprecated"},
    "error_handling_design": {"draft", "reviewed", "approved", "deprecated"},
    "versioning_strategy": {"draft", "reviewed", "approved", "deprecated"},
    "contract_testing_evidence": {"draft", "active", "blocked", "deprecated"},
    "compliance_evidence_package": {"draft", "reviewed", "approved", "expired"},
}

ALWAYS_REQUIRED_APPROVERS = {"API Owner", "Engineering Owner"}
SENSITIVE_DATA_APPROVER = "Security Reviewer"
PUBLIC_API_APPROVER = "API Governance Reviewer"
REGULATED_API_APPROVER = "Legal Reviewer"

VALID_API_AUDIENCE = {"internal", "external", "both"}
VALID_INTERACTION_MODE = {"sync", "async", "streaming", "bidirectional_realtime"}
VALID_PRIMARY_TRANSPORT = {"rest", "graphql", "grpc", "websocket", "sse", "queue"}

COMMON_REQUIRED_BOOL_KEYS = {
    "id_format_validated",
    "backward_compatibility_reviewed",
    "transport_selection_documented",
    "naming_convention_defined",
    "authz_modeled",
    "error_contract_defined",
    "observability_fields_defined",
    "runbook_updated",
    "timeout_budget_defined",
    "delivery_semantics_defined",
    "backpressure_strategy_defined",
    "connection_lifecycle_defined",
    "consumer_idempotency_defined",
    "no_fallback_logic",
    "rate_limit_policy_defined",
    "handles_sensitive_data",
    "external_public_api",
    "regulated_jurisdiction_impact",
}

COMMON_TRUE_KEYS = {
    "id_format_validated",
    "backward_compatibility_reviewed",
    "transport_selection_documented",
    "naming_convention_defined",
    "authz_modeled",
    "error_contract_defined",
    "observability_fields_defined",
    "runbook_updated",
    "timeout_budget_defined",
    "delivery_semantics_defined",
    "no_fallback_logic",
}

PROFILE_REQUIRED_BOOL_KEYS: dict[str, set[str]] = {
    "rest_api_design": {"http_semantics_validated", "idempotency_strategy_defined"},
    "graphql_api_design": {"query_cost_limits_defined", "n_plus_one_guard_defined"},
    "error_handling_design": {"status_mapping_complete", "error_code_registry_updated"},
    "versioning_strategy": {
        "compatibility_matrix_updated",
        "deprecation_policy_defined",
        "has_breaking_change",
    },
    "contract_testing_evidence": {"consumer_matrix_current", "ci_blocking_enabled"},
}

PROFILE_TRUE_KEYS: dict[str, set[str]] = {
    "rest_api_design": {"http_semantics_validated", "idempotency_strategy_defined"},
    "graphql_api_design": {"query_cost_limits_defined", "n_plus_one_guard_defined"},
    "error_handling_design": {"status_mapping_complete", "error_code_registry_updated"},
    "versioning_strategy": {"compatibility_matrix_updated", "deprecation_policy_defined"},
    "contract_testing_evidence": {"consumer_matrix_current", "ci_blocking_enabled"},
}

COMPATIBILITY_MATRIX_REQUIRED_PROFILES = {"versioning_strategy", "contract_testing_evidence"}

COMPLIANCE_EVIDENCE_KEYS = {
    "lawful_basis_or_contract",
    "data_categories",
    "retention_policy",
    "cross_border_transfer_control",
    "audit_log_location",
}

THRESHOLD_POLICY_KEYS = {
    "latency_target_derivation",
    "availability_target_derivation",
    "timeout_budget_derivation",
    "capacity_headroom_derivation",
    "payload_limit_derivation",
    "concurrency_limit_derivation",
    "retry_backoff_derivation",
    "delivery_semantics_derivation",
}


def load_manifest(path: Path) -> dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as fp:
            data = json.load(fp)
    except FileNotFoundError:
        raise SystemExit(f"manifest not found: {path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"invalid JSON in manifest: {exc}")

    if not isinstance(data, dict):
        raise SystemExit("manifest root must be an object")
    return data


def infer_profile(manifest: dict[str, Any], checks: dict[str, Any], errors: list[str]) -> str | None:
    if "compliance_evidence" in manifest:
        return "compliance_evidence_package"

    profile_signals: dict[str, bool] = {
        "rest_api_design": any(key in checks for key in {"http_semantics_validated", "idempotency_strategy_defined"}),
        "graphql_api_design": any(key in checks for key in {"query_cost_limits_defined", "n_plus_one_guard_defined"}),
        "error_handling_design": any(key in checks for key in {"status_mapping_complete", "error_code_registry_updated"}),
        "versioning_strategy": any(key in checks for key in {"compatibility_matrix_updated", "deprecation_policy_defined", "has_breaking_change"}),
        "contract_testing_evidence": any(key in checks for key in {"consumer_matrix_current", "ci_blocking_enabled"}),
    }

    matched_profiles = [name for name, matched in profile_signals.items() if matched]
    if len(matched_profiles) == 1:
        return matched_profiles[0]
    if len(matched_profiles) > 1:
        errors.append(
            "manifest includes overlapping profile-specific checks: "
            + ", ".join(sorted(matched_profiles))
        )
        return None

    context = manifest.get("decision_context")
    if isinstance(context, dict):
        primary_transport = context.get("primary_transport")
        if primary_transport == "graphql":
            return "graphql_api_design"
        if primary_transport == "rest":
            return "rest_api_design"

    errors.append(
        "unable to infer API profile; include profile-specific checks or decision_context.primary_transport"
    )
    return None


def require_bool(checks: dict[str, Any], key: str, errors: list[str]) -> bool | None:
    value = checks.get(key)
    if not isinstance(value, bool):
        errors.append(f"checks.{key} must be a boolean")
        return None
    return value


def require_bool_true(checks: dict[str, Any], key: str, errors: list[str]) -> None:
    value = checks.get(key)
    if not isinstance(value, bool):
        errors.append(f"checks.{key} must be a boolean")
    elif value is not True:
        errors.append(f"checks.{key} must be true")


def require_non_empty_string(obj: dict[str, Any], key: str, errors: list[str], prefix: str) -> None:
    value = obj.get(key)
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{prefix}.{key} must be a non-empty string")


def require_non_empty_string_list(obj: dict[str, Any], key: str, errors: list[str], prefix: str) -> None:
    raw_value = obj.get(key)
    if not isinstance(raw_value, list) or not raw_value or not all(isinstance(item, str) and item.strip() for item in raw_value):
        errors.append(f"{prefix}.{key} must be a non-empty array of strings")


def require_non_empty_string_map(obj: dict[str, Any], keys: set[str], errors: list[str], prefix: str) -> None:
    for key in sorted(keys):
        require_non_empty_string(obj, key, errors, prefix)


def validate_compatibility_matrix(matrix: Any, errors: list[str]) -> None:
    if not isinstance(matrix, dict):
        errors.append("compatibility_matrix must be an object")
        return

    require_non_empty_string_list(
        matrix,
        "supported_producer_versions",
        errors,
        "compatibility_matrix",
    )
    require_non_empty_string_list(
        matrix,
        "tested_consumers",
        errors,
        "compatibility_matrix",
    )


def validate_deprecation_plan(plan: Any, errors: list[str]) -> None:
    if not isinstance(plan, dict):
        errors.append("deprecation_plan must be an object when checks.has_breaking_change is true")
        return

    require_non_empty_string(plan, "target_version", errors, "deprecation_plan")
    require_non_empty_string(plan, "migration_guide_link", errors, "deprecation_plan")

    window_days = plan.get("deprecation_window_days")
    if not isinstance(window_days, int):
        errors.append("deprecation_plan.deprecation_window_days must be an integer")
    elif window_days < MIN_DEPRECATION_WINDOW_DAYS:
        errors.append(
            "deprecation_plan.deprecation_window_days must be "
            f">= {MIN_DEPRECATION_WINDOW_DAYS}"
        )


def validate_decision_context(context: Any, errors: list[str]) -> tuple[str | None, str | None]:
    if not isinstance(context, dict):
        errors.append("decision_context must be an object")
        return (None, None)

    api_audience = context.get("api_audience")
    interaction_mode = context.get("interaction_mode")
    primary_transport = context.get("primary_transport")

    if not isinstance(api_audience, str) or api_audience not in VALID_API_AUDIENCE:
        errors.append(f"decision_context.api_audience must be one of {sorted(VALID_API_AUDIENCE)}")

    if not isinstance(interaction_mode, str) or interaction_mode not in VALID_INTERACTION_MODE:
        errors.append(
            "decision_context.interaction_mode must be one of "
            f"{sorted(VALID_INTERACTION_MODE)}"
        )

    if not isinstance(primary_transport, str) or primary_transport not in VALID_PRIMARY_TRANSPORT:
        errors.append(
            "decision_context.primary_transport must be one of "
            f"{sorted(VALID_PRIMARY_TRANSPORT)}"
        )

    require_non_empty_string(context, "selection_rationale", errors, "decision_context")
    require_non_empty_string(context, "naming_convention_summary", errors, "decision_context")
    require_non_empty_string(context, "threshold_method_summary", errors, "decision_context")
    require_non_empty_string_list(context, "alternatives_considered", errors, "decision_context")

    normalized_mode = interaction_mode if isinstance(interaction_mode, str) else None
    normalized_transport = primary_transport if isinstance(primary_transport, str) else None
    return (normalized_mode, normalized_transport)


def validate_threshold_policy(policy: Any, errors: list[str]) -> None:
    if not isinstance(policy, dict):
        errors.append("threshold_policy must be an object")
        return

    require_non_empty_string_map(policy, THRESHOLD_POLICY_KEYS, errors, "threshold_policy")


def validate_manifest(manifest: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    artifact_id = manifest.get("artifact_id")
    if artifact_id is not None and (not isinstance(artifact_id, str) or not artifact_id.strip()):
        errors.append("artifact_id must be a non-empty string when present")

    state = manifest.get("state")
    approvers = manifest.get("approvers")
    checks = manifest.get("checks")
    decision_context = manifest.get("decision_context")
    threshold_policy = manifest.get("threshold_policy")
    compatibility_matrix = manifest.get("compatibility_matrix")
    deprecation_plan = manifest.get("deprecation_plan")
    compliance_evidence = manifest.get("compliance_evidence")

    if not isinstance(approvers, list) or not all(isinstance(item, str) for item in approvers):
        errors.append("approvers must be an array of strings")
        approver_set: set[str] = set()
    else:
        approver_set = set(approvers)
        missing_base = ALWAYS_REQUIRED_APPROVERS.difference(approver_set)
        for role in sorted(missing_base):
            errors.append(f"missing required approver: {role}")

    if not isinstance(checks, dict):
        errors.append("checks must be an object")
        return errors

    profile = infer_profile(manifest, checks, errors)
    if profile is None:
        return errors

    if not isinstance(state, str) or state not in VALID_STATES_BY_PROFILE[profile]:
        errors.append(f"state must be one of {sorted(VALID_STATES_BY_PROFILE[profile])}")

    for key in sorted(COMMON_REQUIRED_BOOL_KEYS):
        require_bool(checks, key, errors)

    for key in sorted(COMMON_TRUE_KEYS):
        require_bool_true(checks, key, errors)

    for key in sorted(PROFILE_REQUIRED_BOOL_KEYS.get(profile, set())):
        require_bool(checks, key, errors)

    for key in sorted(PROFILE_TRUE_KEYS.get(profile, set())):
        require_bool_true(checks, key, errors)

    interaction_mode, primary_transport = validate_decision_context(decision_context, errors)
    validate_threshold_policy(threshold_policy, errors)

    handles_sensitive_data = checks.get("handles_sensitive_data")
    external_public_api = checks.get("external_public_api")
    regulated_jurisdiction_impact = checks.get("regulated_jurisdiction_impact")

    if handles_sensitive_data is True and SENSITIVE_DATA_APPROVER not in approver_set:
        errors.append(f"missing required approver: {SENSITIVE_DATA_APPROVER}")

    if external_public_api is True:
        if PUBLIC_API_APPROVER not in approver_set:
            errors.append(f"missing required approver: {PUBLIC_API_APPROVER}")
        if checks.get("rate_limit_policy_defined") is not True:
            errors.append("checks.rate_limit_policy_defined must be true when checks.external_public_api is true")

    if regulated_jurisdiction_impact is True and REGULATED_API_APPROVER not in approver_set:
        errors.append(f"missing required approver: {REGULATED_API_APPROVER}")

    if interaction_mode in {"async", "streaming", "bidirectional_realtime"}:
        require_bool_true(checks, "backpressure_strategy_defined", errors)

    if primary_transport in {"websocket", "sse"}:
        require_bool_true(checks, "connection_lifecycle_defined", errors)

    if primary_transport == "queue":
        require_bool_true(checks, "consumer_idempotency_defined", errors)

    if profile == "rest_api_design" and primary_transport not in {None, "rest"}:
        errors.append("REST design manifests must use decision_context.primary_transport=rest")

    if profile == "graphql_api_design" and primary_transport not in {None, "graphql"}:
        errors.append("GraphQL design manifests must use decision_context.primary_transport=graphql")

    if profile in COMPATIBILITY_MATRIX_REQUIRED_PROFILES:
        validate_compatibility_matrix(compatibility_matrix, errors)

    if profile == "versioning_strategy":
        has_breaking_change = checks.get("has_breaking_change")
        if has_breaking_change is True:
            validate_deprecation_plan(deprecation_plan, errors)

    if profile == "compliance_evidence_package":
        if not isinstance(compliance_evidence, dict):
            errors.append("compliance_evidence must be an object for compliance evidence manifests")
        else:
            require_non_empty_string_map(
                compliance_evidence,
                COMPLIANCE_EVIDENCE_KEYS,
                errors,
                "compliance_evidence",
            )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate API governance manifest")
    parser.add_argument("--manifest", required=True, help="Path to manifest JSON")
    args = parser.parse_args()

    manifest = load_manifest(Path(args.manifest))
    errors = validate_manifest(manifest)

    if errors:
        print("validation=failed")
        for error in errors:
            print(f"- {error}")
        return 1

    print("validation=ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
