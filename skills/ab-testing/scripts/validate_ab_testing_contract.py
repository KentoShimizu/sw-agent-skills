#!/usr/bin/env python3
"""Validate AB testing manifests against the AB testing governance contract."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

VALID_STATES_BY_PROFILE: dict[str, set[str]] = {
    "experiment_plan": {"draft", "reviewed", "approved", "active", "stopped", "completed"},
    "decision_record": {"draft", "reviewed", "finalized"},
}

RISK_LEVELS = {"low", "medium", "high", "critical"}
ASSIGNMENT_UNITS = {"user", "session", "org", "device"}
VALID_ACTIONS = {"ship", "iterate", "rollback", "hold"}
ANALYSIS_METHODS = {"fixed_horizon", "sequential"}
GUARDRAIL_STATUSES = {"pass", "mixed", "fail"}

ALWAYS_REQUIRED_APPROVERS = {"Experiment Owner", "Data Science Reviewer"}
PRIVACY_APPROVERS = {"Legal Reviewer", "Privacy Reviewer"}

REQUIRED_CHECKS_TRUE = {
    "id_format_validated",
    "pre_registration_complete",
    "randomization_plan_defined",
    "assignment_unit_defined",
    "instrumentation_validated",
    "srm_monitor_defined",
    "guardrail_policy_defined",
    "one_primary_metric_defined",
    "no_posthoc_decision_rule_changes",
}

REQUIRED_CHECKS_BOOLEAN = {"external_user_impact"}

MIN_RUNTIME_DAYS = 7
MIN_BASELINE_WINDOW_DAYS = 7


def load_manifest(path: Path) -> dict[str, object]:
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except FileNotFoundError:
        raise SystemExit(f"manifest not found: {path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"invalid JSON in manifest: {exc}")

    if not isinstance(data, dict):
        raise SystemExit("manifest root must be an object")
    return data


def infer_profile(manifest: dict[str, object], errors: list[str]) -> str | None:
    has_result = "result" in manifest
    has_plan_fields = "evidence_plan" in manifest or "guardrails" in manifest

    if has_result and has_plan_fields:
        errors.append("manifest mixes decision_record and experiment_plan fields")
        return None
    if has_result:
        return "decision_record"
    if has_plan_fields:
        return "experiment_plan"

    errors.append(
        "unable to infer manifest profile; include result (decision_record) or "
        "evidence_plan/guardrails (experiment_plan)"
    )
    return None


def require_non_empty_string(
    obj: dict[str, object],
    key: str,
    errors: list[str],
    prefix: str,
) -> None:
    value = obj.get(key)
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{prefix}.{key} must be a non-empty string")


def require_numeric(
    obj: dict[str, object],
    key: str,
    errors: list[str],
    prefix: str,
) -> float | None:
    value = obj.get(key)
    if not isinstance(value, (int, float)):
        errors.append(f"{prefix}.{key} must be numeric")
        return None
    return float(value)


def require_integer_min(
    obj: dict[str, object],
    key: str,
    minimum: int,
    errors: list[str],
    prefix: str,
) -> int | None:
    value = obj.get(key)
    if not isinstance(value, int):
        errors.append(f"{prefix}.{key} must be an integer")
        return None
    if value < minimum:
        errors.append(f"{prefix}.{key} must be >= {minimum}")
    return value


def require_string_list(
    obj: dict[str, object],
    key: str,
    *,
    min_items: int,
    errors: list[str],
    prefix: str,
) -> list[str] | None:
    value = obj.get(key)
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        errors.append(f"{prefix}.{key} must be an array of strings")
        return None
    if len(value) < min_items:
        errors.append(f"{prefix}.{key} must have at least {min_items} item(s)")
        return None
    if any(not item.strip() for item in value):
        errors.append(f"{prefix}.{key} must not contain empty strings")
    return value


def validate_checks(checks: object, approver_set: set[str], errors: list[str]) -> None:
    if not isinstance(checks, dict):
        errors.append("checks must be an object")
        return

    check_map = checks
    for key in sorted(REQUIRED_CHECKS_TRUE):
        if check_map.get(key) is not True:
            errors.append(f"checks.{key} must be true")

    for key in sorted(REQUIRED_CHECKS_BOOLEAN):
        value = check_map.get(key)
        if not isinstance(value, bool):
            errors.append(f"checks.{key} must be a boolean")

    external_user_impact = check_map.get("external_user_impact")
    if external_user_impact is True and not PRIVACY_APPROVERS.intersection(approver_set):
        errors.append("Legal Reviewer or Privacy Reviewer is required when checks.external_user_impact is true")


def validate_decision_context(decision_context: object, errors: list[str]) -> None:
    if not isinstance(decision_context, dict):
        errors.append("decision_context must be an object")
        return

    context_map = decision_context
    for key in (
        "decision_question",
        "primary_decision_metric",
        "randomization_method",
        "contamination_risk_mitigation",
    ):
        require_non_empty_string(context_map, key, errors, "decision_context")

    false_positive_cost = context_map.get("false_positive_cost")
    if not isinstance(false_positive_cost, str) or false_positive_cost not in RISK_LEVELS:
        errors.append(f"decision_context.false_positive_cost must be one of {sorted(RISK_LEVELS)}")

    false_negative_cost = context_map.get("false_negative_cost")
    if not isinstance(false_negative_cost, str) or false_negative_cost not in RISK_LEVELS:
        errors.append(f"decision_context.false_negative_cost must be one of {sorted(RISK_LEVELS)}")

    assignment_unit = context_map.get("assignment_unit")
    if not isinstance(assignment_unit, str) or assignment_unit not in ASSIGNMENT_UNITS:
        errors.append(f"decision_context.assignment_unit must be one of {sorted(ASSIGNMENT_UNITS)}")

    actions = require_string_list(
        context_map,
        "allowed_actions",
        min_items=1,
        errors=errors,
        prefix="decision_context",
    )
    if actions is not None:
        invalid_actions = sorted(set(actions).difference(VALID_ACTIONS))
        if invalid_actions:
            errors.append(
                "decision_context.allowed_actions contains unsupported action(s): "
                + ", ".join(invalid_actions)
            )


def validate_evidence_plan(evidence_plan: object, errors: list[str]) -> None:
    if not isinstance(evidence_plan, dict):
        errors.append("evidence_plan must be an object for experiment_plan manifests")
        return

    evidence_map = evidence_plan

    min_detectable_effect = require_numeric(
        evidence_map,
        "min_detectable_effect_pct",
        errors,
        "evidence_plan",
    )
    if min_detectable_effect is not None and min_detectable_effect <= 0:
        errors.append("evidence_plan.min_detectable_effect_pct must be > 0")

    confidence_level = require_numeric(evidence_map, "confidence_level", errors, "evidence_plan")
    if confidence_level is not None and not (0 < confidence_level < 1):
        errors.append("evidence_plan.confidence_level must be between 0 and 1")

    power_target = require_numeric(evidence_map, "power_target", errors, "evidence_plan")
    if power_target is not None and not (0 < power_target < 1):
        errors.append("evidence_plan.power_target must be between 0 and 1")

    require_integer_min(
        evidence_map,
        "minimum_runtime_days",
        MIN_RUNTIME_DAYS,
        errors,
        "evidence_plan",
    )
    require_integer_min(
        evidence_map,
        "baseline_window_days",
        MIN_BASELINE_WINDOW_DAYS,
        errors,
        "evidence_plan",
    )

    analysis_method = evidence_map.get("analysis_method")
    if not isinstance(analysis_method, str) or analysis_method not in ANALYSIS_METHODS:
        errors.append(f"evidence_plan.analysis_method must be one of {sorted(ANALYSIS_METHODS)}")

    require_non_empty_string(evidence_map, "multiplicity_control", errors, "evidence_plan")


def validate_plan_fields(manifest: dict[str, object], errors: list[str]) -> None:
    validate_evidence_plan(manifest.get("evidence_plan"), errors)
    guardrails = manifest.get("guardrails")
    if not isinstance(guardrails, list) or not all(isinstance(item, str) for item in guardrails):
        errors.append("guardrails must be an array of strings for experiment_plan manifests")
        return
    if not guardrails:
        errors.append("guardrails must include at least one metric")
        return
    if any(not item.strip() for item in guardrails):
        errors.append("guardrails must not contain empty strings")


def validate_result(result: object, errors: list[str]) -> None:
    if not isinstance(result, dict):
        errors.append("result must be an object for decision_record manifests")
        return

    result_map = result
    decision_outcome = result_map.get("decision_outcome")
    if not isinstance(decision_outcome, str) or decision_outcome not in VALID_ACTIONS:
        errors.append(f"result.decision_outcome must be one of {sorted(VALID_ACTIONS)}")

    require_numeric(result_map, "primary_metric_effect_pct", errors, "result")
    require_non_empty_string(result_map, "uncertainty_interval", errors, "result")
    require_non_empty_string(result_map, "interpretation", errors, "result")

    guardrail_status = result_map.get("guardrail_status")
    if not isinstance(guardrail_status, str) or guardrail_status not in GUARDRAIL_STATUSES:
        errors.append(f"result.guardrail_status must be one of {sorted(GUARDRAIL_STATUSES)}")

    if result_map.get("complies_with_pre_registered_rules") is not True:
        errors.append("result.complies_with_pre_registered_rules must be true")

    require_string_list(
        result_map,
        "follow_up_actions",
        min_items=1,
        errors=errors,
        prefix="result",
    )

    if decision_outcome == "ship" and guardrail_status == "fail":
        errors.append("result.decision_outcome cannot be ship when result.guardrail_status is fail")


def validate_manifest(manifest: dict[str, object]) -> list[str]:
    errors: list[str] = []

    artifact_id = manifest.get("artifact_id")
    if artifact_id is not None and (not isinstance(artifact_id, str) or not artifact_id.strip()):
        errors.append("artifact_id must be a non-empty string when present")

    profile = infer_profile(manifest, errors)
    if profile is None:
        return errors

    state = manifest.get("state")
    if not isinstance(state, str) or state not in VALID_STATES_BY_PROFILE[profile]:
        errors.append(f"state must be one of {sorted(VALID_STATES_BY_PROFILE[profile])}")

    approvers = manifest.get("approvers")
    if not isinstance(approvers, list) or not all(isinstance(role, str) for role in approvers):
        errors.append("approvers must be an array of strings")
        approver_set: set[str] = set()
    else:
        approver_set = set(approvers)
        missing = ALWAYS_REQUIRED_APPROVERS.difference(approver_set)
        for role in sorted(missing):
            errors.append(f"missing required approver: {role}")

    validate_checks(manifest.get("checks"), approver_set, errors)
    validate_decision_context(manifest.get("decision_context"), errors)

    if profile == "experiment_plan":
        validate_plan_fields(manifest, errors)
    else:
        validate_result(manifest.get("result"), errors)

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate AB testing governance manifest")
    parser.add_argument("--manifest", required=True, help="Path to manifest JSON")
    args = parser.parse_args()

    manifest = load_manifest(Path(args.manifest))
    errors = validate_manifest(manifest)

    if errors:
        print("validation=failed")
        for err in errors:
            print(f"- {err}")
        return 1

    print("validation=ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
