#!/usr/bin/env python3
"""Validate requirements workflow manifests against the requirements governance contract."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

INVALID_STATE = "invalid"

ARTIFACT_ID_PATTERNS: dict[str, re.Pattern[str]] = {
    "RQM-ELC": re.compile(r"^RQM-ELC-[0-9]{8}-[0-9]{3,}$"),
    "RQM-DEF": re.compile(r"^RQM-DEF-[0-9]{8}-[0-9]{3,}$"),
    "RQM-PRI": re.compile(r"^RQM-PRI-[0-9]{8}-[0-9]{3,}$"),
    "RQM-NFR": re.compile(r"^RQM-NFR-[0-9]{8}-[0-9]{3,}$"),
    "RQM-ACD": re.compile(r"^RQM-ACD-[0-9]{8}-[0-9]{3,}$"),
    "RQM-RSK": re.compile(r"^RQM-RSK-[0-9]{8}-[0-9]{3,}$"),
    "RQM-UCM": re.compile(r"^RQM-UCM-[0-9]{8}-[0-9]{3,}$"),
    "RQM-STY": re.compile(r"^RQM-STY-[0-9]{8}-[0-9]{3,}$"),
    "RQM-INT": re.compile(r"^RQM-INT-[0-9]{8}-[0-9]{3,}$"),
    "RQM-URS": re.compile(r"^RQM-URS-[0-9]{8}-[0-9]{3,}$"),
    "RQM-CMP": re.compile(r"^RQM-CMP-[0-9]{8}-[0-9]{3,}$"),
}

BASE_VALID_STATES: dict[str, set[str]] = {
    "RQM-CMP": {"draft", "reviewed", "approved", "expired"},
}

DEFAULT_VALID_STATES = {"draft", "reviewed", "approved", "rejected"}

VALID_STATES: dict[str, set[str]] = {
    prefix: states | {INVALID_STATE}
    for prefix, states in {
        **{prefix: DEFAULT_VALID_STATES for prefix in ARTIFACT_ID_PATTERNS if prefix != "RQM-CMP"},
        **BASE_VALID_STATES,
    }.items()
}

WORK_ITEM_ID_PATTERNS: dict[str, re.Pattern[str]] = {
    "requirements": re.compile(r"^REQ-[A-Z0-9_]+-[0-9]{3,}$"),
    "nfr": re.compile(r"^NFR-REQ-[A-Z0-9_]+-[0-9]{3,}-[0-9]{2,}$"),
    "acceptance_criteria": re.compile(r"^AC-REQ-[A-Z0-9_]+-[0-9]{3,}-[0-9]{2,}$"),
    "risks": re.compile(r"^RSK-REQ-[A-Z0-9_]+-[0-9]{3,}-[0-9]{2,}$"),
    "interviews": re.compile(r"^INT-[0-9]{8}-[0-9]{2,}$"),
    "user_research": re.compile(r"^UR-[0-9]{8}-[0-9]{2,}$"),
    "evidence": re.compile(r"^EVD-[A-Z0-9_]+-[0-9]{3,}$"),
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

PREFIX_REQUIRED_CHECK_KEYS: dict[str, set[str]] = {
    "RQM-ELC": {"source_authority_recorded"},
    "RQM-INT": {"source_authority_recorded"},
    "RQM-URS": {"source_authority_recorded"},
    "RQM-PRI": {"prioritization_rule_frozen"},
    "RQM-NFR": {"metric_threshold_defined"},
    "RQM-ACD": {"acceptance_mapping_complete"},
    "RQM-RSK": {"mitigation_owner_assigned"},
    "RQM-UCM": {"exception_flows_documented"},
    "RQM-STY": {"story_size_validated"},
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

EVIDENCE_DRIVEN_PREFIXES = {"RQM-ELC", "RQM-INT", "RQM-URS"}
REQUIREMENT_BOUND_PREFIXES = {
    "RQM-DEF",
    "RQM-PRI",
    "RQM-NFR",
    "RQM-ACD",
    "RQM-RSK",
    "RQM-UCM",
    "RQM-STY",
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


def artifact_prefix(artifact_id: str) -> str | None:
    for prefix, pattern in ARTIFACT_ID_PATTERNS.items():
        if pattern.match(artifact_id):
            return prefix
    return None


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


def require_id_list(
    linked_ids: dict[str, object],
    key: str,
    pattern: re.Pattern[str],
    errors: list[str],
) -> list[str]:
    raw_value = linked_ids.get(key)
    if raw_value is None:
        return []

    if not isinstance(raw_value, list) or not all(isinstance(item, str) for item in raw_value):
        errors.append(f"linked_ids.{key} must be an array of strings when present")
        return []

    values = [item.strip() for item in raw_value]
    for value in values:
        if not pattern.match(value):
            errors.append(f"linked_ids.{key} contains invalid ID format: {value}")
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

    if not isinstance(artifact_id, str):
        errors.append("artifact_id must be a string")
        return errors

    prefix = artifact_prefix(artifact_id)
    if prefix is None:
        errors.append("artifact_id does not match any allowed ID schema")
        return errors

    if not isinstance(state, str) or state not in VALID_STATES[prefix]:
        errors.append(f"state must be one of {sorted(VALID_STATES[prefix])}")
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

    required_check_keys = COMMON_REQUIRED_CHECK_KEYS | PREFIX_REQUIRED_CHECK_KEYS.get(prefix, set())
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

    if prefix == "RQM-CMP":
        if not isinstance(compliance_evidence, dict):
            errors.append("compliance_evidence must be an object for RQM-CMP artifacts")
        else:
            require_non_empty_string_map(
                compliance_evidence,
                COMPLIANCE_EVIDENCE_KEYS,
                errors,
                "compliance_evidence",
            )

    if not isinstance(linked_ids, dict):
        errors.append("linked_ids must be an object")
        return errors

    unknown_linked_keys = set(linked_ids.keys()).difference(WORK_ITEM_ID_PATTERNS.keys())
    for key in sorted(unknown_linked_keys):
        errors.append(f"linked_ids.{key} is not defined in the canonical contract")

    validated_linked_ids: dict[str, list[str]] = {}
    for key, pattern in WORK_ITEM_ID_PATTERNS.items():
        validated_linked_ids[key] = require_id_list(linked_ids, key, pattern, errors)

    if is_invalid_state:
        return errors

    if prefix in EVIDENCE_DRIVEN_PREFIXES:
        source_count = (
            len(validated_linked_ids["interviews"])
            + len(validated_linked_ids["user_research"])
            + len(validated_linked_ids["evidence"])
        )
        if source_count == 0:
            errors.append(
                "at least one of linked_ids.interviews, linked_ids.user_research, or "
                "linked_ids.evidence must be present for evidence-driven artifacts"
            )

    if prefix in REQUIREMENT_BOUND_PREFIXES and len(validated_linked_ids["requirements"]) == 0:
        errors.append("linked_ids.requirements must be non-empty for requirement-bound artifacts")

    if prefix == "RQM-NFR" and len(validated_linked_ids["nfr"]) == 0:
        errors.append("linked_ids.nfr must be non-empty for RQM-NFR artifacts")

    if prefix == "RQM-ACD" and len(validated_linked_ids["acceptance_criteria"]) == 0:
        errors.append("linked_ids.acceptance_criteria must be non-empty for RQM-ACD artifacts")

    if prefix == "RQM-RSK" and len(validated_linked_ids["risks"]) == 0:
        errors.append("linked_ids.risks must be non-empty for RQM-RSK artifacts")

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
