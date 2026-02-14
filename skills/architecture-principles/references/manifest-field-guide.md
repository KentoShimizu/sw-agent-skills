# Architecture Manifest Field Guide

## Purpose
Use this guide when authoring manifests validated by `skills/architecture-principles/scripts/validate_architecture_contract.py`.

## Top-level fields
- `artifact_id`: Architecture contract ID (for example `ARC-PRN-001`, `ARC-CMP-20260214-001`)
- `state`: Lifecycle state for the artifact prefix
- `approvers`: Array of reviewer role names
- `checks`: Gate checks object
- `compliance_evidence`: Required only for `ARC-CMP-*`

## `checks` fields

### Required for all manifests
- `id_format_validated` (`boolean`, must be `true`)
- `personal_data_processed` (`boolean`)
- `eu_high_risk_processing` (`boolean`)
- `system_type` (`"greenfield"` or `"brownfield"`)

### Required when `system_type = "greenfield"`
- `greenfield_no_fallback` (`boolean`, must be `true`)
- `failure_exposure_criteria` (`string`, non-empty)
- `redecision_trigger` (`string`, non-empty)

### Required when `system_type = "brownfield"`
- `rollback_trigger_condition` (`string`, non-empty)
- `rollback_runbook_link` (`string`, non-empty)

## `approvers` requirements

### Always required
- `Architecture Owner`
- `Security Reviewer`

### Conditional
- When `checks.personal_data_processed = true`: `Legal Reviewer` or `Privacy Reviewer`
- When `checks.eu_high_risk_processing = true`: `DPO` or `Delegated DPO Approver`

## `compliance_evidence` fields (`ARC-CMP-*` only)
- `lawful_basis`
- `data_categories`
- `data_residency_map`
- `cross_border_transfer_control`
- `retention_and_deletion_policy`
- `encryption_and_key_management`
- `access_control_and_audit_log_location`
- `data_subject_rights_process`

All `compliance_evidence` fields must be non-empty strings.

## Authoring workflow
1. Start from sample manifests under `skills/architecture-principles/references/samples/`.
2. Fill `checks` first, then validate required approvers.
3. For `ARC-CMP-*`, complete all `compliance_evidence` fields.
4. Run: `python3 skills/architecture-principles/scripts/validate_architecture_contract.py --manifest <path>`.
