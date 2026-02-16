#!/usr/bin/env python3
"""Validate design governance manifests using project-declared policy rules."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


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


def require_non_empty_string(value: Any, field: str, errors: list[str]) -> None:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{field} must be a non-empty string")


def validate_string_list(value: Any, field: str, errors: list[str]) -> list[str]:
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        errors.append(f"{field} must be an array of strings")
        return []

    cleaned = [item.strip() for item in value]
    if any(not item for item in cleaned):
        errors.append(f"{field} must not contain empty strings")
    return cleaned


def validate_checks(checks: dict[str, Any], errors: list[str]) -> None:
    for key, value in checks.items():
        if key == "locales":
            validate_string_list(value, "checks.locales", errors)
            continue

        if not isinstance(value, bool):
            errors.append(f"checks.{key} must be a boolean")


def validate_policy(policy: dict[str, Any], errors: list[str]) -> None:
    if "required_approvers" in policy:
        validate_string_list(policy["required_approvers"], "policy.required_approvers", errors)

    if "required_checks" in policy:
        validate_string_list(policy["required_checks"], "policy.required_checks", errors)

    if "required_locales" in policy:
        validate_string_list(policy["required_locales"], "policy.required_locales", errors)

    if "allowed_states" in policy:
        validate_string_list(policy["allowed_states"], "policy.allowed_states", errors)

    if "require_artifact_id" in policy and not isinstance(policy["require_artifact_id"], bool):
        errors.append("policy.require_artifact_id must be a boolean")

    if "require_privacy_evidence" in policy and not isinstance(policy["require_privacy_evidence"], bool):
        errors.append("policy.require_privacy_evidence must be a boolean")

    if "required_privacy_fields" in policy:
        validate_string_list(policy["required_privacy_fields"], "policy.required_privacy_fields", errors)


def enforce_policy(
    manifest: dict[str, Any],
    policy: dict[str, Any],
    approvers: list[str],
    checks: dict[str, Any],
    errors: list[str],
) -> None:
    if policy.get("require_artifact_id") is True:
        require_non_empty_string(manifest.get("artifact_id"), "artifact_id", errors)

    if "allowed_states" in policy:
        allowed_states = set(validate_string_list(policy["allowed_states"], "policy.allowed_states", errors))
        state = manifest.get("state")
        require_non_empty_string(state, "state", errors)
        if isinstance(state, str) and allowed_states and state not in allowed_states:
            errors.append(f"state must be one of {sorted(allowed_states)}")

    required_approvers = policy.get("required_approvers", [])
    if isinstance(required_approvers, list):
        missing_approvers = set(required_approvers).difference(set(approvers))
        for role in sorted(missing_approvers):
            errors.append(f"missing required approver: {role}")

    required_checks = policy.get("required_checks", [])
    if isinstance(required_checks, list):
        for key in required_checks:
            value = checks.get(key)
            if value is not True:
                errors.append(f"checks.{key} must be true")

    required_locales = policy.get("required_locales", [])
    if isinstance(required_locales, list) and required_locales:
        locales = checks.get("locales")
        locale_list = locales if isinstance(locales, list) else []
        missing_locales = set(required_locales).difference(set(locale_list))
        for locale in sorted(missing_locales):
            errors.append(f"missing required locale: {locale}")

    require_privacy_evidence = policy.get("require_privacy_evidence") is True
    if require_privacy_evidence:
        privacy_evidence = manifest.get("privacy_evidence")
        if not isinstance(privacy_evidence, dict):
            errors.append("privacy_evidence must be an object when policy.require_privacy_evidence is true")
            return

        required_fields = policy.get("required_privacy_fields", [])
        if isinstance(required_fields, list):
            for key in required_fields:
                require_non_empty_string(privacy_evidence.get(key), f"privacy_evidence.{key}", errors)


def validate_manifest(manifest: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    artifact_id = manifest.get("artifact_id")
    if artifact_id is not None:
        require_non_empty_string(artifact_id, "artifact_id", errors)

    state = manifest.get("state")
    if state is not None:
        require_non_empty_string(state, "state", errors)

    approvers_raw = manifest.get("approvers")
    if approvers_raw is None:
        approvers: list[str] = []
    else:
        approvers = validate_string_list(approvers_raw, "approvers", errors)

    checks_raw = manifest.get("checks")
    if checks_raw is None:
        checks: dict[str, Any] = {}
    elif not isinstance(checks_raw, dict):
        errors.append("checks must be an object when present")
        checks = {}
    else:
        checks = checks_raw
        validate_checks(checks, errors)

    policy_raw = manifest.get("policy")
    if policy_raw is None:
        policy: dict[str, Any] = {}
    elif not isinstance(policy_raw, dict):
        errors.append("policy must be an object when present")
        policy = {}
    else:
        policy = policy_raw
        validate_policy(policy, errors)

    if policy:
        enforce_policy(manifest, policy, approvers, checks, errors)

    privacy_evidence = manifest.get("privacy_evidence")
    if privacy_evidence is not None and not isinstance(privacy_evidence, dict):
        errors.append("privacy_evidence must be an object when present")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate design governance manifest")
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
