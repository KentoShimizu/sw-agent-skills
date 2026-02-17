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

Use project-specific ID naming rules. Example ID patterns in this contract are non-binding.
Treat this document as operational guidance, not a mandatory schema.
When repository-specific rules exist, follow those first; otherwise use this as a default operating method.

## Profile Inference Contract (Canonical)
Do not require `artifact_kind` in manifests.
Infer profile from manifest signals:
- Evidence-driven profile: `checks.source_authority_recorded` is present, or evidence links exist without requirement links.
- Prioritization profile: `checks.prioritization_rule_frozen` is present.
- NFR profile: `checks.metric_threshold_defined` is present.
- Acceptance criteria profile: `checks.acceptance_mapping_complete` is present.
- Risk analysis profile: `checks.mitigation_owner_assigned` is present.
- Use-case profile: `checks.exception_flows_documented` is present.
- User story profile: `checks.story_size_validated` is present.
- Compliance evidence profile: `compliance_evidence` is present.
- Baseline profile: none of the profile-specific signals above are present.

For repository operations, filename and location are valid project-level routing controls.

## ID Format Policy (Project-Defined)
- `artifact_id` is optional and project-defined.
- Keep one repository-level ID policy and enforce it consistently.
- `checks.id_format_validated=true` must represent validation against that policy.
- Example IDs (non-binding):
  - `RQM-ELC-20260214-001`
  - `RQM-DEF-20260214-001`
  - `RQM-PRI-20260214-001`
  - `RQM-NFR-20260214-001`
  - `RQM-ACD-20260214-001`
  - `RQM-RSK-20260214-001`
  - `RQM-UCM-20260214-001`
  - `RQM-STY-20260214-001`
  - `RQM-INT-20260214-001`
  - `RQM-URS-20260214-001`
  - `RQM-CMP-20260214-001`

## Issuance Rules
- Allocate IDs sequentially per project namespace.
- Keep IDs immutable and append-only.
- Never reuse retired IDs.
- On collision, issue a new ID and mark the old ID as `invalid` with reason.

## Lifecycle States
- Compliance evidence profile: `draft`, `reviewed`, `approved`, `expired`
- Other profiles: `draft`, `reviewed`, `approved`, `rejected`
- `invalid` is allowed for all profiles only to retire collided or voided IDs.

## Compliance Baseline (US, Japan, EU)
- Record lawful basis before collecting or linking personal data.
- Minimize personal data and avoid direct identifiers in requirement artifacts.
- Ensure retention/deletion policy and data subject rights handling are documented.
- Capture cross-border transfer control before sharing regulated evidence.
- Preserve auditable approvals and change history for requirement decisions.

## Recommended Check Keys
Recommended common keys in `checks`:
- `id_format_validated` (boolean)
- `traceability_verified` (boolean)
- `decision_owner_assigned` (boolean)
- `unresolved_conflicts_absent` (boolean)
- `compliance_constraints_captured` (boolean)
- `handles_personal_data` (boolean)
- `regulated_jurisdiction_impact` (boolean)

Profile-specific keys (recommended when applicable):
- Evidence-driven profile
  - `source_authority_recorded` (boolean)
- Prioritization profile
  - `prioritization_rule_frozen` (boolean)
- NFR profile
  - `metric_threshold_defined` (boolean)
- Acceptance criteria profile
  - `acceptance_mapping_complete` (boolean)
- Risk analysis profile
  - `mitigation_owner_assigned` (boolean)
- Use-case profile
  - `exception_flows_documented` (boolean)
- User story profile
  - `story_size_validated` (boolean)
- Baseline profile, compliance evidence profile
  - No additional required check keys beyond the common set

## Linked IDs Guidance
Use `linked_ids` with these keys when applicable:
- `requirements`
- `nfr`
- `acceptance_criteria`
- `risks`
- `interviews`
- `user_research`
- `evidence`

Linked ID naming format is project-defined and validated outside this contract.
Presence rules:
- Evidence-driven profile:
  at least one of `interviews`, `user_research`, or `evidence` must be non-empty.
- Requirement-bound profiles (baseline, prioritization, nfr, acceptance criteria, risk analysis, use case, user story):
  `requirements` must be non-empty.
- NFR profile: `nfr` must be non-empty.
- Acceptance criteria profile: `acceptance_criteria` must be non-empty.
- Risk analysis profile: `risks` must be non-empty.

## Privacy Evidence Guidance
When `checks.handles_personal_data` is `true`, include `privacy_evidence` with:
- `lawful_basis_or_consent`
- `pii_data_inventory`
- `data_minimization_decision`
- `retention_and_deletion_policy`
- `cross_border_transfer_control`
- `data_subject_rights_process`
- `redaction_and_access_control`

## Compliance Evidence Guidance
For the compliance evidence profile (`compliance_evidence` is present), include:
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

## Optional Consistency Check
- Optional: `python3 skills/requirements-definition/scripts/validate_requirements_contract.py --manifest <path/to/manifest.json>` from repository root.
- Recommended structured fields: `state`, `approvers`, `checks`, and `linked_ids`.
- `artifact_id` is optional. If present, keep it non-empty.

## Operational Handling (Recommended)
- Escalate when identifier policy checks fail (`checks.id_format_validated=false`).
- Escalate when lifecycle state is invalid.
- Escalate when required approvers are missing.
- Escalate when critical checks are not all `true`.
- Escalate when required linked ID sets are missing for the selected profile.
- Escalate when privacy or compliance evidence is incomplete.
- When `state` is `invalid`, context-specific execution checks are not enforced.
