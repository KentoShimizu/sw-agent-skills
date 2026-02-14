#!/usr/bin/env python3
"""Validate architecture governance manifest against the architecture contract."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ID_PATTERNS: dict[str, re.Pattern[str]] = {
    "ARC-DRV": re.compile(r"^ARC-DRV-[0-9]{3,}$"),
    "ARC-PRN": re.compile(r"^ARC-PRN-[0-9]{3,}$"),
    "ARC-OPT": re.compile(r"^ARC-OPT-[0-9]{3,}$"),
    "ADR": re.compile(r"^ADR-[0-9]{8}-[0-9]{3,}$"),
    "ARC-RSK": re.compile(r"^ARC-RSK-[0-9]{3,}$"),
    "C4-CTX": re.compile(r"^C4-CTX-[A-Z0-9_]+-v[0-9]+$"),
    "C4-CTR": re.compile(r"^C4-CTR-[A-Z0-9_]+-v[0-9]+$"),
    "C4-CMP": re.compile(r"^C4-CMP-[A-Z0-9_]+-v[0-9]+$"),
    "ARC-CMP": re.compile(r"^ARC-CMP-[0-9]{8}-[0-9]{3,}$"),
}

VALID_STATES: dict[str, set[str]] = {
    "ARC-DRV": {"proposed", "accepted", "rejected", "deprecated"},
    "ARC-PRN": {"proposed", "accepted", "rejected", "deprecated"},
    "ARC-OPT": {"proposed", "accepted", "rejected", "deprecated"},
    "ADR": {"proposed", "accepted", "rejected", "superseded"},
    "ARC-RSK": {"open", "mitigating", "accepted", "closed"},
    "ARC-CMP": {"draft", "reviewed", "approved", "expired"},
}

SYSTEM_TYPES = {"greenfield", "brownfield"}
ALWAYS_REQUIRED_APPROVERS = {"Architecture Owner", "Security Reviewer"}
PERSONAL_DATA_APPROVERS = {"Legal Reviewer", "Privacy Reviewer"}
EU_HIGH_RISK_APPROVERS = {"DPO", "Delegated DPO Approver"}

COMPLIANCE_EVIDENCE_KEYS = {
    "lawful_basis",
    "data_categories",
    "data_residency_map",
    "cross_border_transfer_control",
    "retention_and_deletion_policy",
    "encryption_and_key_management",
    "access_control_and_audit_log_location",
    "data_subject_rights_process",
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
    for prefix, pattern in ID_PATTERNS.items():
        if pattern.match(artifact_id):
            return prefix
    return None


def require_bool_true(checks: dict[str, object], key: str, errors: list[str]) -> None:
    if checks.get(key) is not True:
        errors.append(f"checks.{key} must be true")


def require_bool(checks: dict[str, object], key: str, errors: list[str]) -> bool | None:
    value = checks.get(key)
    if not isinstance(value, bool):
        errors.append(f"checks.{key} must be a boolean")
        return None
    return value


def require_non_empty_string(obj: dict[str, object], key: str, errors: list[str], prefix: str) -> None:
    value = obj.get(key)
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{prefix}.{key} must be a non-empty string")


def require_non_empty_string_map(
    obj: dict[str, object],
    keys: set[str],
    errors: list[str],
    prefix: str,
) -> None:
    for key in sorted(keys):
        require_non_empty_string(obj, key, errors, prefix)


def validate_manifest(manifest: dict[str, object]) -> list[str]:
    errors: list[str] = []

    artifact_id = manifest.get("artifact_id")
    state = manifest.get("state")
    approvers = manifest.get("approvers")
    checks = manifest.get("checks")
    compliance_evidence = manifest.get("compliance_evidence")

    if not isinstance(artifact_id, str):
        errors.append("artifact_id must be a string")
        return errors

    prefix = artifact_prefix(artifact_id)
    if prefix is None:
        errors.append("artifact_id does not match any allowed ID schema")
        return errors

    allowed_states = VALID_STATES.get(prefix)
    if allowed_states is not None:
        if not isinstance(state, str) or state not in allowed_states:
            errors.append(f"state must be one of {sorted(allowed_states)}")
    elif state is not None:
        errors.append("state is not defined for this artifact type in the canonical contract")

    if not isinstance(approvers, list) or not all(isinstance(x, str) for x in approvers):
        errors.append("approvers must be an array of strings")
        approver_set: set[str] = set()
    else:
        approver_set = set(approvers)
        missing_required = ALWAYS_REQUIRED_APPROVERS.difference(approver_set)
        for role in sorted(missing_required):
            errors.append(f"missing required approver: {role}")

    if not isinstance(checks, dict):
        errors.append("checks must be an object")
        return errors

    check_map = checks
    require_bool_true(check_map, "id_format_validated", errors)

    personal_data_processed = require_bool(check_map, "personal_data_processed", errors)
    eu_high_risk_processing = require_bool(check_map, "eu_high_risk_processing", errors)

    system_type = check_map.get("system_type")
    if not isinstance(system_type, str) or system_type not in SYSTEM_TYPES:
        errors.append(f"checks.system_type must be one of {sorted(SYSTEM_TYPES)}")
    elif system_type == "greenfield":
        require_bool_true(check_map, "greenfield_no_fallback", errors)
        require_non_empty_string(check_map, "failure_exposure_criteria", errors, "checks")
        require_non_empty_string(check_map, "redecision_trigger", errors, "checks")
    elif system_type == "brownfield":
        require_non_empty_string(check_map, "rollback_trigger_condition", errors, "checks")
        require_non_empty_string(check_map, "rollback_runbook_link", errors, "checks")

    if personal_data_processed is True and not PERSONAL_DATA_APPROVERS.intersection(approver_set):
        errors.append("Legal Reviewer or Privacy Reviewer is required when checks.personal_data_processed is true")

    if eu_high_risk_processing is True and not EU_HIGH_RISK_APPROVERS.intersection(approver_set):
        errors.append("DPO or Delegated DPO Approver is required when checks.eu_high_risk_processing is true")

    if prefix == "ARC-CMP":
        if not isinstance(compliance_evidence, dict):
            errors.append("compliance_evidence must be an object for ARC-CMP artifacts")
        else:
            require_non_empty_string_map(compliance_evidence, COMPLIANCE_EVIDENCE_KEYS, errors, "compliance_evidence")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate architecture governance manifest")
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
