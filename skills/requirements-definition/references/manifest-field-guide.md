# Requirements Manifest Field Guide

This guide provides a recommended manifest shape.
Optional check command:
`python3 skills/requirements-definition/scripts/validate_requirements_contract.py --manifest <path/to/manifest.json>`

## Root Fields
- `artifact_id` (string, optional): project-defined artifact ID.
- `state` (string, recommended): lifecycle state from the governance contract.
- `approvers` (array[string], recommended): approval roles.
- `checks` (object, recommended): machine-check booleans.
- `linked_ids` (object, recommended): traced work item IDs.
- `privacy_evidence` (object, conditional): recommended when `checks.handles_personal_data=true`.
- `compliance_evidence` (object, conditional): recommended for compliance evidence manifests.

Profile routing does not use `artifact_kind`. The validator infers profile from `checks`, `linked_ids`, and optional `compliance_evidence`.

## `checks` Object
Common keys (recommended as `true`):
- `id_format_validated`
- `traceability_verified`
- `decision_owner_assigned`
- `unresolved_conflicts_absent`
- `compliance_constraints_captured`

Common policy toggles:
- `handles_personal_data`
- `regulated_jurisdiction_impact`

Profile-specific keys (recommended):
- Evidence-driven profile: `source_authority_recorded`
- Prioritization profile: `prioritization_rule_frozen`
- NFR profile: `metric_threshold_defined`
- Acceptance criteria profile: `acceptance_mapping_complete`
- Risk analysis profile: `mitigation_owner_assigned`
- Use-case profile: `exception_flows_documented`
- User story profile: `story_size_validated`

## `linked_ids` Object
Allowed keys are optional arrays of non-empty strings:
- `requirements`
- `nfr`
- `acceptance_criteria`
- `risks`
- `interviews`
- `user_research`
- `evidence`

ID naming inside `linked_ids` is project-defined and validated outside this contract.

Minimum presence by profile (recommended):
- Evidence-driven profile:
  at least one of interviews/user_research/evidence.
- Requirement-bound profiles (baseline, prioritization, nfr, acceptance criteria, risk analysis, use case, user story):
  `requirements` must be non-empty.
- Additional required sets:
  - NFR profile: `nfr`
  - Acceptance criteria profile: `acceptance_criteria`
  - Risk analysis profile: `risks`

## Privacy and Compliance Evidence
### `privacy_evidence` (recommended when personal data is handled)
- `lawful_basis_or_consent`
- `pii_data_inventory`
- `data_minimization_decision`
- `retention_and_deletion_policy`
- `cross_border_transfer_control`
- `data_subject_rights_process`
- `redaction_and_access_control`

### `compliance_evidence` (recommended for compliance evidence manifests)
- `jurisdiction_scope`
- `lawful_basis_summary`
- `retention_policy_reference`
- `cross_border_transfer_control`
- `data_subject_rights_path`
- `audit_log_location`
