#!/usr/bin/env python3
"""Validate requirements workflow manifests against the requirements governance contract."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

INVALID_STATE = "invalid"

VALID_STATES = {
    "draft",
    "reviewed",
    "approved",
    "rejected",
    "expired",
    INVALID_STATE,
}

ALWAYS_REQUIRED_APPROVERS = {"Product Owner", "Engineering Owner"}
PRIVACY_REVIEWER = "Privacy Reviewer"
LEGAL_REVIEWER = "Legal Reviewer"

COMMON_REQUIRED_CHECK_KEYS = {
    "id_format_validated",
    "traceability_verified",
    "decision_owner_assigned",
    "unresolved_conflicts_absent",
    "compliance_constraints_captured",
    "handles_personal_data",
    "regulated_jurisdiction_impact",
}

PROFILE_REQUIRED_CHECK_KEYS: dict[str, set[str]] = {
    "evidence_driven": {"source_authority_recorded"},
    "prioritization": {"prioritization_rule_frozen"},
    "nfr": {"metric_threshold_defined"},
    "acceptance_criteria": {"acceptance_mapping_complete"},
    "risk_analysis": {"mitigation_owner_assigned"},
    "use_case": {"exception_flows_documented"},
    "user_story": {"story_size_validated"},
}

OPTIONAL_TYPED_CHECK_KEYS = {
    "source_authority_recorded",
    "prioritization_rule_frozen",
    "metric_threshold_defined",
    "acceptance_mapping_complete",
    "mitigation_owner_assigned",
    "exception_flows_documented",
    "story_size_validated",
}

PRIVACY_EVIDENCE_KEYS = {
    "lawful_basis_or_consent",
    "pii_data_inventory",
    "data_minimization_decision",
    "retention_and_deletion_policy",
    "cross_border_transfer_control",
    "data_subject_rights_process",
    "redaction_and_access_control",
}

COMPLIANCE_EVIDENCE_KEYS = {
    "jurisdiction_scope",
    "lawful_basis_summary",
    "retention_policy_reference",
    "cross_border_transfer_control",
    "data_subject_rights_path",
    "audit_log_location",
}

LINKED_ID_KEYS = {
    "requirements",
    "nfr",
    "acceptance_criteria",
    "risks",
    "interviews",
    "user_research",
    "evidence",
}

REQUIREMENT_BOUND_PROFILES = {
    "baseline",
    "prioritization",
    "nfr",
    "acceptance_criteria",
    "risk_analysis",
    "use_case",
    "user_story",
}


def load_manifest(path: Path) -> dict[str, object]:
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


def infer_profile(manifest: dict[str, object], checks: dict[str, object], linked_ids: dict[str, object], errors: list[str]) -> str:
    if "compliance_evidence" in manifest:
        return "compliance"

    profile_signals: dict[str, bool] = {
        "evidence_driven": "source_authority_recorded" in checks,
        "prioritization": "prioritization_rule_frozen" in checks,
        "nfr": "metric_threshold_defined" in checks,
        "acceptance_criteria": "acceptance_mapping_complete" in checks,
        "risk_analysis": "mitigation_owner_assigned" in checks,
        "use_case": "exception_flows_documented" in checks,
        "user_story": "story_size_validated" in checks,
    }

    matched_profiles = [name for name, matched in profile_signals.items() if matched]
    if len(matched_profiles) > 1:
        errors.append(
            "manifest includes overlapping profile-specific checks: "
            + ", ".join(sorted(matched_profiles))
        )
        return "invalid"
    if len(matched_profiles) == 1:
        return matched_profiles[0]

    evidence_like = 0
    for key in ("interviews", "user_research", "evidence"):
        raw = linked_ids.get(key)
        if isinstance(raw, list) and any(isinstance(item, str) and item.strip() for item in raw):
            evidence_like += 1

    requirements = linked_ids.get("requirements")
    requirements_non_empty = isinstance(requirements, list) and any(
        isinstance(item, str) and item.strip() for item in requirements
    )

    if evidence_like > 0 and not requirements_non_empty:
        return "evidence_driven"

    return "baseline"


def require_bool_true(checks: dict[str, object], key: str, errors: list[str]) -> None:
    value = checks.get(key)
    if not isinstance(value, bool):
        errors.append(f"checks.{key} must be a boolean")
    elif value is not True:
        errors.append(f"checks.{key} must be true")


def require_non_empty_string_map(
    obj: dict[str, object],
    keys: set[str],
    errors: list[str],
    prefix: str,
) -> None:
    for key in sorted(keys):
        value = obj.get(key)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{prefix}.{key} must be a non-empty string")


def require_string_list(
    linked_ids: dict[str, object],
    key: str,
    errors: list[str],
) -> list[str]:
    raw_value = linked_ids.get(key)
    if raw_value is None:
        return []

    if not isinstance(raw_value, list) or not all(isinstance(item, str) for item in raw_value):
        errors.append(f"linked_ids.{key} must be an array of strings when present")
        return []

    values = [item.strip() for item in raw_value]
    if any(not value for value in values):
        errors.append(f"linked_ids.{key} must not contain empty strings")
    return values


def validate_manifest(manifest: dict[str, object]) -> list[str]:
    errors: list[str] = []

    artifact_id = manifest.get("artifact_id")
    state = manifest.get("state")
    approvers = manifest.get("approvers")
    checks = manifest.get("checks")
    linked_ids = manifest.get("linked_ids")
    privacy_evidence = manifest.get("privacy_evidence")
    compliance_evidence = manifest.get("compliance_evidence")

    if artifact_id is not None and (not isinstance(artifact_id, str) or not artifact_id.strip()):
        errors.append("artifact_id must be a non-empty string when present")

    if not isinstance(state, str) or state not in VALID_STATES:
        errors.append(f"state must be one of {sorted(VALID_STATES)}")
    is_invalid_state = state == INVALID_STATE

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

    if not isinstance(linked_ids, dict):
        errors.append("linked_ids must be an object")
        return errors

    profile = infer_profile(manifest, checks, linked_ids, errors)
    if profile == "invalid":
        return errors

    required_check_keys = set(COMMON_REQUIRED_CHECK_KEYS)
    required_check_keys.update(PROFILE_REQUIRED_CHECK_KEYS.get(profile, set()))

    for key in sorted(required_check_keys):
        value = checks.get(key)
        if not isinstance(value, bool):
            errors.append(f"checks.{key} must be a boolean")

    for key in sorted(OPTIONAL_TYPED_CHECK_KEYS - required_check_keys):
        if key in checks and not isinstance(checks.get(key), bool):
            errors.append(f"checks.{key} must be a boolean when present")

    for key in sorted({
        "id_format_validated",
        "traceability_verified",
        "decision_owner_assigned",
        "unresolved_conflicts_absent",
        "compliance_constraints_captured",
    }):
        require_bool_true(checks, key, errors)

    handles_personal_data = checks.get("handles_personal_data")
    regulated_jurisdiction_impact = checks.get("regulated_jurisdiction_impact")

    if handles_personal_data is True and PRIVACY_REVIEWER not in approver_set:
        errors.append("missing required approver: Privacy Reviewer")

    if regulated_jurisdiction_impact is True and LEGAL_REVIEWER not in approver_set:
        errors.append("missing required approver: Legal Reviewer")

    if handles_personal_data is True:
        if not isinstance(privacy_evidence, dict):
            errors.append("privacy_evidence must be an object when personal data is handled")
        else:
            require_non_empty_string_map(
                privacy_evidence,
                PRIVACY_EVIDENCE_KEYS,
                errors,
                "privacy_evidence",
            )

    if compliance_evidence is not None:
        if not isinstance(compliance_evidence, dict):
            errors.append("compliance_evidence must be an object when present")
        else:
            require_non_empty_string_map(
                compliance_evidence,
                COMPLIANCE_EVIDENCE_KEYS,
                errors,
                "compliance_evidence",
            )

    unknown_linked_keys = set(linked_ids.keys()).difference(LINKED_ID_KEYS)
    for key in sorted(unknown_linked_keys):
        errors.append(f"linked_ids.{key} is not defined in the canonical contract")

    validated_linked_ids: dict[str, list[str]] = {}
    for key in sorted(LINKED_ID_KEYS):
        validated_linked_ids[key] = require_string_list(linked_ids, key, errors)

    if is_invalid_state:
        return errors

    if profile == "evidence_driven":
        source_count = (
            len(validated_linked_ids["interviews"])
            + len(validated_linked_ids["user_research"])
            + len(validated_linked_ids["evidence"])
        )
        if source_count == 0:
            errors.append(
                "at least one of linked_ids.interviews, linked_ids.user_research, or "
                "linked_ids.evidence must be present for evidence-driven manifests"
            )

    if profile in REQUIREMENT_BOUND_PROFILES and len(validated_linked_ids["requirements"]) == 0:
        errors.append("linked_ids.requirements must be non-empty for requirement-bound manifests")

    if profile == "nfr" and len(validated_linked_ids["nfr"]) == 0:
        errors.append("linked_ids.nfr must be non-empty for NFR manifests")

    if profile == "acceptance_criteria" and len(validated_linked_ids["acceptance_criteria"]) == 0:
        errors.append("linked_ids.acceptance_criteria must be non-empty for acceptance-criteria manifests")

    if profile == "risk_analysis" and len(validated_linked_ids["risks"]) == 0:
        errors.append("linked_ids.risks must be non-empty for risk-analysis manifests")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate requirements governance manifest")
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
