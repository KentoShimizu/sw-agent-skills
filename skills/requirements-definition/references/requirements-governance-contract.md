# Requirements Governance Contract

## Scope
Apply this contract to all requirement workflow skills:
- `requirement-elicitation`
- `requirements-definition`
- `requirement-prioritization`
- `non-functional-requirements`
- `acceptance-criteria-design`
- `risk-requirements-analysis`
- `use-case-modeling`
- `user-story-writing`
- `stakeholder-interview`
- `user-research`

Do not redefine ID formats, lifecycle states, approval gates, or compliance evidence rules in individual `SKILL.md` files.

## ID Schema (Single Source of Truth)
### Requirement Work Item IDs
- `REQ-<DOMAIN>-<NNN>`: `^REQ-[A-Z0-9_]+-[0-9]{3,}$`
  - Canonical requirement item
- `NFR-<REQ_ID>-<NN>`: `^NFR-REQ-[A-Z0-9_]+-[0-9]{3,}-[0-9]{2,}$`
  - Non-functional requirement tied to `REQ-*`
- `AC-<REQ_ID>-<NN>`: `^AC-REQ-[A-Z0-9_]+-[0-9]{3,}-[0-9]{2,}$`
  - Acceptance criteria tied to `REQ-*`
- `RSK-<REQ_ID>-<NN>`: `^RSK-REQ-[A-Z0-9_]+-[0-9]{3,}-[0-9]{2,}$`
  - Requirement risk entry tied to `REQ-*`
- `INT-<YYYYMMDD>-<NN>`: `^INT-[0-9]{8}-[0-9]{2,}$`
  - Stakeholder interview record
- `UR-<YYYYMMDD>-<NN>`: `^UR-[0-9]{8}-[0-9]{2,}$`
  - User research record
- `EVD-<SOURCE>-<NNN>`: `^EVD-[A-Z0-9_]+-[0-9]{3,}$`
  - Evidence record

### Validation Artifact IDs
- `RQM-ELC-<YYYYMMDD>-<NNN>`: elicitation output package
- `RQM-DEF-<YYYYMMDD>-<NNN>`: requirements baseline package
- `RQM-PRI-<YYYYMMDD>-<NNN>`: prioritization package
- `RQM-NFR-<YYYYMMDD>-<NNN>`: NFR package
- `RQM-ACD-<YYYYMMDD>-<NNN>`: acceptance criteria package
- `RQM-RSK-<YYYYMMDD>-<NNN>`: risk analysis package
- `RQM-UCM-<YYYYMMDD>-<NNN>`: use case package
- `RQM-STY-<YYYYMMDD>-<NNN>`: user story package
- `RQM-INT-<YYYYMMDD>-<NNN>`: stakeholder interview synthesis package
- `RQM-URS-<YYYYMMDD>-<NNN>`: user research synthesis package
- `RQM-CMP-<YYYYMMDD>-<NNN>`: compliance evidence package

Regex (single source):
- `^RQM-(ELC|DEF|PRI|NFR|ACD|RSK|UCM|STY|INT|URS|CMP)-[0-9]{8}-[0-9]{3,}$`

## Issuance Rules
- Allocate IDs sequentially per prefix namespace.
- Keep IDs immutable and append-only.
- Never reuse retired IDs.
- On collision, issue a new ID and mark the old ID as `invalid` with reason.

## Lifecycle States
- `RQM-CMP-*`: `draft`, `reviewed`, `approved`, `expired`
- Other `RQM-*`: `draft`, `reviewed`, `approved`, `rejected`
- `invalid` is allowed for all `RQM-*` prefixes only to retire collided or voided IDs.

## Compliance Baseline (US, Japan, EU)
- Record lawful basis before collecting or linking personal data.
- Minimize personal data and avoid direct identifiers in requirement artifacts.
- Ensure retention/deletion policy and data subject rights handling are documented.
- Capture cross-border transfer control before sharing regulated evidence.
- Preserve auditable approvals and change history for requirement decisions.

## Required Check Keys
Manifest `checks` must include all of the following common keys:
- `id_format_validated` (boolean)
- `traceability_verified` (boolean)
- `decision_owner_assigned` (boolean)
- `unresolved_conflicts_absent` (boolean)
- `compliance_constraints_captured` (boolean)
- `handles_personal_data` (boolean)
- `regulated_jurisdiction_impact` (boolean)

Prefix-specific required keys:
- `RQM-ELC-*`, `RQM-INT-*`, `RQM-URS-*`
  - `source_authority_recorded` (boolean)
- `RQM-PRI-*`
  - `prioritization_rule_frozen` (boolean)
- `RQM-NFR-*`
  - `metric_threshold_defined` (boolean)
- `RQM-ACD-*`
  - `acceptance_mapping_complete` (boolean)
- `RQM-RSK-*`
  - `mitigation_owner_assigned` (boolean)
- `RQM-UCM-*`
  - `exception_flows_documented` (boolean)
- `RQM-STY-*`
  - `story_size_validated` (boolean)
- `RQM-DEF-*`, `RQM-CMP-*`
  - No additional required check keys beyond the common set

## Linked IDs Schema
Manifest `linked_ids` is mandatory and must satisfy:
- `requirements`: array of `REQ-*`
- `nfr`: array of `NFR-*`
- `acceptance_criteria`: array of `AC-*`
- `risks`: array of `RSK-*`
- `interviews`: array of `INT-*`
- `user_research`: array of `UR-*`
- `evidence`: array of `EVD-*`

Presence rules:
- `RQM-ELC-*`, `RQM-INT-*`, `RQM-URS-*`: at least one of `interviews`, `user_research`, or `evidence` must be non-empty.
- `RQM-DEF-*`, `RQM-PRI-*`, `RQM-NFR-*`, `RQM-ACD-*`, `RQM-RSK-*`, `RQM-UCM-*`, `RQM-STY-*`: `requirements` must be non-empty.
- `RQM-NFR-*`: `nfr` must be non-empty.
- `RQM-ACD-*`: `acceptance_criteria` must be non-empty.
- `RQM-RSK-*`: `risks` must be non-empty.

## Privacy Evidence Requirements
When `checks.handles_personal_data` is `true`, `privacy_evidence` is mandatory and must include:
- `lawful_basis_or_consent`
- `pii_data_inventory`
- `data_minimization_decision`
- `retention_and_deletion_policy`
- `cross_border_transfer_control`
- `data_subject_rights_process`
- `redaction_and_access_control`

## Compliance Evidence Requirements
For `RQM-CMP-*`, `compliance_evidence` is mandatory and must include:
- `jurisdiction_scope`
- `lawful_basis_summary`
- `retention_policy_reference`
- `cross_border_transfer_control`
- `data_subject_rights_path`
- `audit_log_location`

## Approval Matrix
- Required for all requirement workflow artifacts:
  - Product Owner
  - Engineering Owner
- Required when `checks.handles_personal_data` is `true`:
  - Privacy Reviewer
- Required when `checks.regulated_jurisdiction_impact` is `true`:
  - Legal Reviewer

## Machine Validation
- Run `python3 skills/requirements-definition/scripts/validate_requirements_contract.py --manifest <path/to/manifest.json>` from repository root.
- Manifest must include `artifact_id`, `state`, `approvers`, `checks`, and `linked_ids`.

## Gate Policy
- Block approval when IDs are malformed.
- Block approval when lifecycle state is invalid for the artifact type.
- Block approval when required approvers are missing.
- Block approval when required checks are not all `true`.
- Block approval when required linked ID sets are missing.
- Block approval when privacy or compliance evidence is incomplete.
- When `state` is `invalid`, prefix-specific execution checks are not enforced.
