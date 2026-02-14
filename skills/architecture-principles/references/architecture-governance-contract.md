# Architecture Governance Contract

## Scope
Apply this contract to all `architecture-*` skills.
Do not redefine ID formats, lifecycle states, or compliance gate rules in individual skill files.

## ID Schema (Single Source of Truth)
- `ARC-DRV-<NNN>`: `^ARC-DRV-[0-9]{3,}$`
  - Meaning: architecture driver
  - Issuer: architecture owner
  - Uniqueness: repository-wide
- `ARC-PRN-<NNN>`: `^ARC-PRN-[0-9]{3,}$`
  - Meaning: architecture principle
  - Issuer: architecture owner
  - Uniqueness: repository-wide
- `ARC-OPT-<NNN>`: `^ARC-OPT-[0-9]{3,}$`
  - Meaning: architecture option
  - Issuer: architecture owner
  - Uniqueness: decision-scope-wide
- `ADR-<YYYYMMDD>-<NNN>`: `^ADR-[0-9]{8}-[0-9]{3,}$`
  - Meaning: architecture decision record
  - Issuer: architecture reviewer or owner
  - Uniqueness: repository-wide
- `ARC-RSK-<NNN>`: `^ARC-RSK-[0-9]{3,}$`
  - Meaning: architecture risk
  - Issuer: risk owner
  - Uniqueness: repository-wide
- `C4-CTX-<SYSTEM>-v<NN>`: `^C4-CTX-[A-Z0-9_]+-v[0-9]+$`
  - Meaning: C4 context diagram
  - Issuer: architecture owner
  - Uniqueness: system-wide
- `C4-CTR-<SYSTEM>-v<NN>`: `^C4-CTR-[A-Z0-9_]+-v[0-9]+$`
  - Meaning: C4 container diagram
  - Issuer: architecture owner
  - Uniqueness: system-wide
- `C4-CMP-<SYSTEM>-v<NN>`: `^C4-CMP-[A-Z0-9_]+-v[0-9]+$`
  - Meaning: C4 component diagram
  - Issuer: architecture owner
  - Uniqueness: system-wide
- `ARC-CMP-<YYYYMMDD>-<NNN>`: `^ARC-CMP-[0-9]{8}-[0-9]{3,}$`
  - Meaning: compliance evidence package
  - Issuer: compliance gate owner
  - Uniqueness: release-wide

## Issuance and Collision Rules
- Allocate IDs sequentially inside each prefix namespace.
- Never reuse retired IDs.
- Keep ID-to-artifact mapping append-only.
- Resolve collisions by issuing a new ID and marking collided ID as `invalid` with reason.

## Lifecycle Rules
- `ARC-DRV-*`, `ARC-PRN-*`, `ARC-OPT-*`: `proposed`, `accepted`, `rejected`, `deprecated`
- `ADR-*`: `proposed`, `accepted`, `rejected`, `superseded`
- `ARC-RSK-*`: `open`, `mitigating`, `accepted`, `closed`
- `ARC-CMP-*`: `draft`, `reviewed`, `approved`, `expired`

## Compliance Evidence Requirements (US, Japan, EU)
Each `ARC-CMP-*` package must include all required fields:
- `lawful_basis`
- `data_categories`
- `data_residency_map`
- `cross_border_transfer_control`
- `retention_and_deletion_policy`
- `encryption_and_key_management`
- `access_control_and_audit_log_location`
- `data_subject_rights_process`

## Approval Matrix
- Required for all architecture changes:
  - Architecture Owner
  - Security Reviewer
- Required when personal data is processed:
  - Legal or Privacy Reviewer
- Required when EU high-risk processing is involved:
  - DPO or formally delegated approver

### Canonical approver role names for machine validation
- `Architecture Owner`
- `Security Reviewer`
- `Legal Reviewer`
- `Privacy Reviewer`
- `DPO`
- `Delegated DPO Approver`

## Machine Validation
- Run `python3 skills/architecture-principles/scripts/validate_architecture_contract.py --manifest <path/to/manifest.json>`.
- For CI or batch validation, run `python3 scripts/run_contract_validators.py --architecture-manifest <path/to/manifest.json>`.
- Manifest must include: `artifact_id`, `approvers`, and `checks`.
- Include `checks.id_format_validated` as `true`.
- Include `checks.personal_data_processed` as `true` or `false`.
- Include `checks.eu_high_risk_processing` as `true` or `false`.
- Include `checks.system_type` as `greenfield` or `brownfield`.
- For `checks.system_type = greenfield`, include:
  - `checks.greenfield_no_fallback` as `true`
  - `checks.failure_exposure_criteria` (non-empty string)
  - `checks.redecision_trigger` (non-empty string)
- For `checks.system_type = brownfield`, include:
  - `checks.rollback_trigger_condition` (non-empty string)
  - `checks.rollback_runbook_link` (non-empty string)
- For `ARC-CMP-*` artifacts, include `compliance_evidence` with:
  - `lawful_basis`
  - `data_categories`
  - `data_residency_map`
  - `cross_border_transfer_control`
  - `retention_and_deletion_policy`
  - `encryption_and_key_management`
  - `access_control_and_audit_log_location`
  - `data_subject_rights_process`

### Valid Manifest Samples
- `skills/architecture-principles/references/samples/arc-prn-manifest.valid.json`
- `skills/architecture-principles/references/samples/arc-cmp-manifest.valid.json`
- Field-level guidance: `skills/architecture-principles/references/manifest-field-guide.md`

## Gate Policy
- Block release when mandatory fields in `ARC-CMP-*` are missing.
- Block release when required approvers are missing.
- Block release when ID format validation fails.
- For greenfield design:
  - Do not include fallback architecture paths.
  - Require explicit failure exposure criteria and re-decision trigger.
- For brownfield operated systems:
  - Allow rollback strategy only with explicit trigger condition and runbook link.
