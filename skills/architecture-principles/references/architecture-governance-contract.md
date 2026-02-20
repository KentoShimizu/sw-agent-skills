# Architecture Governance Contract

## Scope
Apply this contract to all `architecture-*` skills.
Use project-specific ID naming rules; example IDs in this document are illustrative only.
Treat this document as operational guidance, not a mandatory schema.
When repository-specific rules exist, follow those first; otherwise use this as a default operating method.

## Manifest Profile Model (Canonical)
Validation profile is inferred from state and field presence.

Profiles:
- `compliance_evidence_package`
  - Identified when `compliance_evidence` is present.
- `risk_like_record`
  - State in `open | mitigating | closed`.
- `stateful_architecture_record`
  - State in `proposed | accepted | rejected | deprecated | superseded`.
- `stateless_view_record`
  - State omitted (used for C4 view artifacts).

## ID Format Policy (Project-Defined)
- `artifact_id` is optional and project-defined.
- If present, it must be non-empty and follow your repository ID policy.
- `checks.id_format_validated=true` means validation against that policy has been completed.

## Issuance and Collision Rules
- Allocate IDs sequentially inside each project namespace.
- Never reuse retired IDs.
- Keep ID-to-artifact mapping append-only.
- Resolve collisions by issuing a new ID and marking collided ID as `invalid` with reason.

## Lifecycle Rules
- Stateful architecture records: `proposed`, `accepted`, `rejected`, `deprecated`, `superseded`
- Risk-like records: `open`, `mitigating`, `accepted`, `closed`
- Compliance evidence package: `draft`, `reviewed`, `approved`, `expired`
- Stateless view records: `state` is omitted

## Compliance Evidence Requirements (US, Japan, EU)
Each compliance evidence package must include all required fields:
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

## Optional Consistency Check
- Optional: run `python3 skills/architecture-principles/scripts/validate_architecture_contract.py --manifest <path/to/manifest.json>`.
- Recommended structured manifest fields:
  - `state`, `approvers`, and `checks`
  - Optional: `artifact_id`
- Recommended check flags:
  - `checks.id_format_validated` as `true`
  - `checks.personal_data_processed` as `true` or `false`
  - `checks.eu_high_risk_processing` as `true` or `false`
  - `checks.system_type` as `greenfield` or `brownfield`
- For `checks.system_type = greenfield`, recommend:
  - `checks.greenfield_no_fallback` as `true`
  - `checks.failure_exposure_criteria` (non-empty string)
  - `checks.redecision_trigger` (non-empty string)
- For `checks.system_type = brownfield`, recommend:
  - `checks.rollback_trigger_condition` (non-empty string)
  - `checks.rollback_runbook_link` (non-empty string)
- When `compliance_evidence` is present, recommend:
  - `lawful_basis`
  - `data_categories`
  - `data_residency_map`
  - `cross_border_transfer_control`
  - `retention_and_deletion_policy`
  - `encryption_and_key_management`
  - `access_control_and_audit_log_location`
  - `data_subject_rights_process`

### Valid Manifest Samples (Example IDs)
- `skills/architecture-principles/assets/arc-prn-manifest.valid.json`
- `skills/architecture-principles/assets/arc-cmp-manifest.valid.json`
- Field-level guidance: `skills/architecture-principles/references/manifest-field-guide.md`

## Operational Handling (Recommended)
- When compliance evidence fields are missing, escalate and resolve before final approval.
- When required approvers are missing, hold decision closure until ownership is explicit.
- When `checks.id_format_validated` is false, run ID policy review or document why ID checks are intentionally not used.
- For greenfield design:
  - Do not include fallback architecture paths.
  - Require explicit failure exposure criteria and re-decision trigger.
- For brownfield operated systems:
  - Allow rollback strategy only with explicit trigger condition and runbook link.
