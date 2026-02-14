#!/usr/bin/env python3
"""Validate git workflow manifests against the git governance contract."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ID_PATTERNS: dict[str, re.Pattern[str]] = {
    "GIT-BRN": re.compile(r"^GIT-BRN-[0-9]{3,}$"),
    "GIT-CMT": re.compile(r"^GIT-CMT-[0-9]{8}-[0-9]{3,}$"),
    "GIT-RBS": re.compile(r"^GIT-RBS-[0-9]{8}-[0-9]{3,}$"),
    "GIT-MRG": re.compile(r"^GIT-MRG-[0-9]{8}-[0-9]{3,}$"),
    "GIT-CHP": re.compile(r"^GIT-CHP-[0-9]{8}-[0-9]{3,}$"),
    "GIT-HIS": re.compile(r"^GIT-HIS-[0-9]{8}-[0-9]{3,}$"),
    "GIT-BIS": re.compile(r"^GIT-BIS-[0-9]{8}-[0-9]{3,}$"),
    "GIT-RVT": re.compile(r"^GIT-RVT-[0-9]{8}-[0-9]{3,}$"),
    "GIT-REL": re.compile(r"^GIT-REL-[0-9]{8}-[0-9]{3,}$"),
    "GIT-PRS": re.compile(r"^GIT-PRS-[0-9]{8}-[0-9]{3,}$"),
    "GIT-CMP": re.compile(r"^GIT-CMP-[0-9]{8}-[0-9]{3,}$"),
}

INVALID_STATE = "invalid"

BASE_VALID_STATES: dict[str, set[str]] = {
    "GIT-BRN": {"draft", "reviewed", "approved", "deprecated"},
    "GIT-REL": {"prepared", "reviewed", "released", "superseded"},
    "GIT-CMP": {"draft", "reviewed", "approved", "expired"},
    "GIT-CMT": {"draft", "reviewed", "executed", "rejected"},
    "GIT-RBS": {"draft", "reviewed", "executed", "rejected"},
    "GIT-MRG": {"draft", "reviewed", "executed", "rejected"},
    "GIT-CHP": {"draft", "reviewed", "executed", "rejected"},
    "GIT-HIS": {"draft", "reviewed", "executed", "rejected"},
    "GIT-BIS": {"draft", "reviewed", "executed", "rejected"},
    "GIT-RVT": {"draft", "reviewed", "executed", "rejected"},
    "GIT-PRS": {"draft", "reviewed", "executed", "rejected"},
}

VALID_STATES: dict[str, set[str]] = {
    prefix: states | {INVALID_STATE} for prefix, states in BASE_VALID_STATES.items()
}

ALWAYS_REQUIRED_APPROVERS = {"Repository Owner", "Engineering Owner"}
SECURITY_REVIEWER = "Security Reviewer"
PRIVACY_REVIEWER = "Privacy Reviewer"
SECURITY_REQUIRED_PREFIXES = {"GIT-REL", "GIT-RVT", "GIT-CHP"}

REQUIRED_CHECK_KEYS = {
    "id_format_validated",
    "branch_protection_verified",
    "ci_required_checks_green",
    "secret_scan_passed",
    "history_rewrite_policy_compliant",
    "handles_personal_data",
}

PREFIX_REQUIRED_CHECK_KEYS: dict[str, set[str]] = {
    "GIT-PRS": {"pr_opened", "merge_sync_used", "rebase_used", "repository_merge_only_policy"},
    "GIT-RBS": {"pr_opened", "rebase_used"},
    "GIT-REL": {"signed_tag_verified"},
}

OPTIONAL_TYPED_CHECK_KEYS = {
    "pr_opened",
    "merge_sync_used",
    "rebase_used",
    "repository_merge_only_policy",
    "signed_tag_verified",
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


def artifact_prefix(artifact_id: str) -> str | None:
    for prefix, pattern in ID_PATTERNS.items():
        if pattern.match(artifact_id):
            return prefix
    return None


def require_bool(checks: dict[str, Any], key: str, errors: list[str]) -> None:
    value = checks.get(key)
    if not isinstance(value, bool):
        errors.append(f"checks.{key} must be a boolean")
    elif value is not True:
        errors.append(f"checks.{key} must be true")


def require_non_empty_string_map(
    obj: dict[str, Any], keys: set[str], errors: list[str], prefix: str
) -> None:
    for key in sorted(keys):
        value = obj.get(key)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{prefix}.{key} must be a non-empty string")


def validate_manifest(manifest: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    artifact_id = manifest.get("artifact_id")
    state = manifest.get("state")
    approvers = manifest.get("approvers")
    checks = manifest.get("checks")
    privacy_evidence = manifest.get("privacy_evidence")

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

    if not isinstance(approvers, list) or not all(isinstance(x, str) for x in approvers):
        errors.append("approvers must be an array of strings")
        approver_set: set[str] = set()
    else:
        approver_set = set(approvers)
        missing_base = ALWAYS_REQUIRED_APPROVERS.difference(approver_set)
        for role in sorted(missing_base):
            errors.append(f"missing required approver: {role}")

    if prefix in SECURITY_REQUIRED_PREFIXES and SECURITY_REVIEWER not in approver_set:
        errors.append("missing required approver: Security Reviewer")

    if not isinstance(checks, dict):
        errors.append("checks must be an object")
        return errors

    required_prefix_check_keys = set()
    if not is_invalid_state:
        required_prefix_check_keys = PREFIX_REQUIRED_CHECK_KEYS.get(prefix, set())

    required_check_keys = REQUIRED_CHECK_KEYS | required_prefix_check_keys
    for key in sorted(REQUIRED_CHECK_KEYS):
        value = checks.get(key)
        if not isinstance(value, bool):
            errors.append(f"checks.{key} must be a boolean")
    for key in sorted(required_prefix_check_keys):
        value = checks.get(key)
        if not isinstance(value, bool):
            errors.append(f"checks.{key} must be a boolean")
    for key in sorted(OPTIONAL_TYPED_CHECK_KEYS - required_check_keys):
        if key in checks and not isinstance(checks.get(key), bool):
            errors.append(f"checks.{key} must be a boolean when present")

    require_bool(checks, "id_format_validated", errors)
    require_bool(checks, "branch_protection_verified", errors)
    require_bool(checks, "ci_required_checks_green", errors)
    require_bool(checks, "secret_scan_passed", errors)
    require_bool(checks, "history_rewrite_policy_compliant", errors)

    handles_personal_data = checks.get("handles_personal_data")
    if handles_personal_data is True and PRIVACY_REVIEWER not in approver_set:
        errors.append("missing required approver: Privacy Reviewer")

    if handles_personal_data is True:
        if not isinstance(privacy_evidence, dict):
            errors.append("privacy_evidence must be an object when personal data is handled")
        else:
            require_non_empty_string_map(
                privacy_evidence, PRIVACY_EVIDENCE_KEYS, errors, "privacy_evidence"
            )

    # Prefix-specific policy checks.
    pr_opened = checks.get("pr_opened")
    merge_sync_used = checks.get("merge_sync_used")
    rebase_used = checks.get("rebase_used")
    repository_merge_only_policy = checks.get("repository_merge_only_policy")
    signed_tag_verified = checks.get("signed_tag_verified")

    if not is_invalid_state and prefix == "GIT-PRS":
        if pr_opened is not True:
            errors.append("checks.pr_opened must be true for GIT-PRS artifacts")
        used_merge_sync = merge_sync_used is True
        used_rebase_sync = rebase_used is True
        if used_merge_sync and used_rebase_sync:
            errors.append(
                "checks.merge_sync_used and checks.rebase_used must not both be true for "
                "GIT-PRS artifacts"
            )
        if not used_merge_sync and not used_rebase_sync:
            errors.append(
                "one of checks.merge_sync_used or checks.rebase_used must be true for "
                "GIT-PRS artifacts"
            )
        if repository_merge_only_policy is True and used_rebase_sync:
            errors.append(
                "checks.rebase_used must be false when "
                "checks.repository_merge_only_policy is true for GIT-PRS artifacts"
            )

    if not is_invalid_state and prefix == "GIT-RBS":
        if pr_opened is not False:
            errors.append("checks.pr_opened must be false for GIT-RBS artifacts")
        if rebase_used is not True:
            errors.append("checks.rebase_used must be true for GIT-RBS artifacts")

    if not is_invalid_state and prefix == "GIT-REL" and signed_tag_verified is not True:
        errors.append("checks.signed_tag_verified must be true for GIT-REL artifacts")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate git governance manifest")
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
