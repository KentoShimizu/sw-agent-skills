#!/usr/bin/env python3
"""Validate git workflow manifests against the git governance contract."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

INVALID_STATE = "invalid"

VALID_STATES = {
    "draft",
    "reviewed",
    "approved",
    "deprecated",
    "prepared",
    "released",
    "superseded",
    "expired",
    "executed",
    "rejected",
    INVALID_STATE,
}

ALWAYS_REQUIRED_APPROVERS = {"Repository Owner", "Engineering Owner"}
SECURITY_REVIEWER = "Security Reviewer"
PRIVACY_REVIEWER = "Privacy Reviewer"

REQUIRED_CHECK_KEYS = {
    "id_format_validated",
    "branch_protection_verified",
    "ci_required_checks_green",
    "secret_scan_passed",
    "history_rewrite_policy_compliant",
    "handles_personal_data",
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

    if artifact_id is not None and (not isinstance(artifact_id, str) or not artifact_id.strip()):
        errors.append("artifact_id must be a non-empty string when present")

    if not isinstance(state, str) or state not in VALID_STATES:
        errors.append(f"state must be one of {sorted(VALID_STATES)}")
    is_invalid_state = state == INVALID_STATE

    if not isinstance(approvers, list) or not all(isinstance(x, str) for x in approvers):
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

    for key in sorted(REQUIRED_CHECK_KEYS):
        value = checks.get(key)
        if not isinstance(value, bool):
            errors.append(f"checks.{key} must be a boolean")

    for key in sorted(OPTIONAL_TYPED_CHECK_KEYS):
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

    # Optional context-specific policy checks.
    pr_opened = checks.get("pr_opened")
    merge_sync_used = checks.get("merge_sync_used")
    rebase_used = checks.get("rebase_used")
    repository_merge_only_policy = checks.get("repository_merge_only_policy")
    signed_tag_verified = checks.get("signed_tag_verified")

    if not is_invalid_state and (
        pr_opened is True
        or merge_sync_used is not None
        or repository_merge_only_policy is not None
    ):
        if pr_opened is not True:
            errors.append("checks.pr_opened must be true for PR-sync style manifests")
        used_merge_sync = merge_sync_used is True
        used_rebase_sync = rebase_used is True
        if used_merge_sync and used_rebase_sync:
            errors.append(
                "checks.merge_sync_used and checks.rebase_used must not both be true for "
                "PR-sync style manifests"
            )
        if not used_merge_sync and not used_rebase_sync:
            errors.append(
                "one of checks.merge_sync_used or checks.rebase_used must be true for "
                "PR-sync style manifests"
            )
        if repository_merge_only_policy is True and used_rebase_sync:
            errors.append(
                "checks.rebase_used must be false when checks.repository_merge_only_policy is true"
            )

    if not is_invalid_state and pr_opened is False and rebase_used is not None:
        if rebase_used is not True:
            errors.append("checks.rebase_used must be true for rebase execution manifests")

    if signed_tag_verified is not None:
        if signed_tag_verified is not True:
            errors.append("checks.signed_tag_verified must be true when present")
        if SECURITY_REVIEWER not in approver_set:
            errors.append("missing required approver: Security Reviewer")

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
