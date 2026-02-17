# Architecture Manifest Field Guide

## Purpose
Use this guide for recommended manifest structure.
Optional check: `skills/architecture-principles/scripts/validate_architecture_contract.py`.

## Top-level fields
- `state`: lifecycle state for the manifest profile (or omitted for stateless views)
- `approvers`: array of reviewer role names
- `checks`: recommended checks object
- `compliance_evidence`: recommended when compliance evidence is provided
- `artifact_id`: optional project-defined identifier

## State rules
### Allowed states when provided
- `proposed`, `accepted`, `rejected`, `deprecated`, `superseded`
- `open`, `mitigating`, `closed`
- `draft`, `reviewed`, `approved`, `expired`

### Omitted state
- Allowed for stateless view records (for example C4 view snapshots)

## Compliance inference rule
- If `compliance_evidence` is present, treat the manifest as a compliance evidence package and prefer `state` in `draft`, `reviewed`, `approved`, `expired`.

## `checks` fields

### Recommended for all manifests
- `id_format_validated` (`boolean`, usually `true`)
- `personal_data_processed` (`boolean`)
- `eu_high_risk_processing` (`boolean`)
- `system_type` (`"greenfield"` or `"brownfield"`)

### Recommended when `system_type = "greenfield"`
- `greenfield_no_fallback` (`boolean`, usually `true`)
- `failure_exposure_criteria` (`string`, non-empty)
- `redecision_trigger` (`string`, non-empty)

### Recommended when `system_type = "brownfield"`
- `rollback_trigger_condition` (`string`, non-empty)
- `rollback_runbook_link` (`string`, non-empty)

## `approvers` requirements

### Usually required
- `Architecture Owner`
- `Security Reviewer`

### Conditional
- When `checks.personal_data_processed = true`: `Legal Reviewer` or `Privacy Reviewer`
- When `checks.eu_high_risk_processing = true`: `DPO` or `Delegated DPO Approver`

## `compliance_evidence` fields (when provided)
- `lawful_basis`
- `data_categories`
- `data_residency_map`
- `cross_border_transfer_control`
- `retention_and_deletion_policy`
- `encryption_and_key_management`
- `access_control_and_audit_log_location`
- `data_subject_rights_process`

Prefer non-empty strings for all `compliance_evidence` fields.

## Authoring workflow
1. Start from sample manifests under `skills/architecture-principles/assets/`.
2. Fill `checks`, then confirm approver coverage.
3. If compliance evidence is needed, add `compliance_evidence` and use compliance states.
4. Optional: run `python3 skills/architecture-principles/scripts/validate_architecture_contract.py --manifest <path>`.
