#!/usr/bin/env python3
"""Validate design governance manifest against the design governance contract."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ID_PATTERNS: dict[str, re.Pattern[str]] = {
    "DSN-PRN": re.compile(r"^DSN-PRN-[0-9]{3,}$"),
    "DSN-SYS": re.compile(r"^DSN-SYS-[0-9]{3,}$"),
    "DSN-TOK": re.compile(r"^DSN-TOK-[A-Z0-9_]+-[0-9]{3,}$"),
    "UX-FLW": re.compile(r"^UX-FLW-[0-9]{3,}$"),
    "IA-NAV": re.compile(r"^IA-NAV-[0-9]{3,}$"),
    "VIS-SPEC": re.compile(r"^VIS-SPEC-[0-9]{3,}$"),
    "A11Y-CHK": re.compile(r"^A11Y-CHK-[0-9]{3,}$"),
    "RESP-RUL": re.compile(r"^RESP-RUL-[0-9]{3,}$"),
    "UX-RSR": re.compile(r"^UX-RSR-[0-9]{8}-[0-9]{3,}$"),
    "FIG-HND": re.compile(r"^FIG-HND-[0-9]{8}-[0-9]{3,}$"),
    "DREV": re.compile(r"^DREV-[0-9]{8}-[0-9]{3,}$"),
}

VALID_STATES: dict[str, set[str]] = {
    "DSN-PRN": {"proposed", "accepted", "deprecated"},
    "DSN-SYS": {"proposed", "accepted", "deprecated"},
    "DSN-TOK": {"proposed", "accepted", "deprecated"},
    "UX-FLW": {"draft", "reviewed", "approved", "deprecated"},
    "IA-NAV": {"draft", "reviewed", "approved", "deprecated"},
    "VIS-SPEC": {"draft", "reviewed", "approved", "deprecated"},
    "A11Y-CHK": {"draft", "reviewed", "approved", "rejected"},
    "RESP-RUL": {"draft", "reviewed", "approved", "deprecated"},
    "UX-RSR": {"draft", "reviewed", "approved", "rejected"},
    "FIG-HND": {"prepared", "reviewed", "released", "superseded"},
    "DREV": {"draft", "reviewed", "approved", "rejected"},
}

EU_LOCALES = {
    "fr-FR",
    "de-DE",
    "es-ES",
    "it-IT",
    "nl-NL",
    "pt-PT",
    "pl-PL",
    "sv-SE",
    "da-DK",
    "fi-FI",
    "cs-CZ",
}

ALWAYS_REQUIRED_APPROVERS = {"Design Owner", "Engineering Owner"}
ACCESSIBILITY_REVIEWER = "Accessibility Reviewer"
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
    if checks.get(key) is not True:
        errors.append(f"checks.{key} must be true")


def require_non_empty_string_map(obj: dict[str, Any], keys: set[str], errors: list[str], prefix: str) -> None:
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

    require_bool(checks, "id_format_validated", errors)
    require_bool(checks, "wcag_aa", errors)
    require_bool(checks, "keyboard_navigation", errors)
    require_bool(checks, "visible_focus_states", errors)
    require_bool(checks, "color_contrast", errors)
    require_bool(checks, "semantic_structure", errors)
    require_bool(checks, "screen_reader_order", errors)
    require_bool(checks, "text_expansion", errors)
    require_bool(checks, "text_truncation", errors)

    user_facing_change = checks.get("user_facing_change")
    if not isinstance(user_facing_change, bool):
        errors.append("checks.user_facing_change must be a boolean")
    elif user_facing_change and ACCESSIBILITY_REVIEWER not in approver_set:
        errors.append("Accessibility Reviewer is required when checks.user_facing_change is true")

    locales = checks.get("locales")
    if not isinstance(locales, list) or not all(isinstance(x, str) for x in locales):
        errors.append("checks.locales must be an array of locale strings")
    else:
        required_locales = {"en-US", "ja-JP"}
        missing_required = required_locales.difference(set(locales))
        for loc in sorted(missing_required):
            errors.append(f"missing required locale: {loc}")

        eu_count = len(EU_LOCALES.intersection(set(locales)))
        if eu_count < 2:
            errors.append("at least two EU locales are required in checks.locales")

    privacy_required = prefix in {"UX-RSR", "FIG-HND"} or user_facing_change is True

    if prefix in {"UX-RSR", "FIG-HND"} and "Privacy Reviewer" not in approver_set:
        errors.append("Privacy Reviewer is required for UX-RSR and FIG-HND artifacts")

    if privacy_required:
        if not isinstance(privacy_evidence, dict):
            errors.append("privacy_evidence must be an object when privacy evidence is required")
        else:
            require_non_empty_string_map(privacy_evidence, PRIVACY_EVIDENCE_KEYS, errors, "privacy_evidence")

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
