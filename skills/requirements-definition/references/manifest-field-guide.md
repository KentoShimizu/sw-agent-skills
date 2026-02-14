# Requirements Manifest Field Guide

This guide defines the manifest shape validated by:
`python3 skills/requirements-definition/scripts/validate_requirements_contract.py --manifest <path/to/manifest.json>`

## Root Fields
- `artifact_id` (string, required): `RQM-*` artifact ID.
- `state` (string, required): lifecycle state from the governance contract.
- `approvers` (array[string], required): approval roles.
- `checks` (object, required): machine-check booleans.
- `linked_ids` (object, required): traced work item IDs.
- `privacy_evidence` (object, conditional): required when `checks.handles_personal_data=true`.
- `compliance_evidence` (object, conditional): required for `RQM-CMP-*`.

## `checks` Object
Common required keys (boolean, must be `true`):
- `id_format_validated`
- `traceability_verified`
- `decision_owner_assigned`
- `unresolved_conflicts_absent`
- `compliance_constraints_captured`

Common required keys (boolean, policy toggles):
- `handles_personal_data`
- `regulated_jurisdiction_impact`

Prefix-specific required keys:
- `RQM-ELC-*`, `RQM-INT-*`, `RQM-URS-*`: `source_authority_recorded`
- `RQM-PRI-*`: `prioritization_rule_frozen`
- `RQM-NFR-*`: `metric_threshold_defined`
- `RQM-ACD-*`: `acceptance_mapping_complete`
- `RQM-RSK-*`: `mitigation_owner_assigned`
- `RQM-UCM-*`: `exception_flows_documented`
- `RQM-STY-*`: `story_size_validated`

## `linked_ids` Object
All keys are optional arrays, but IDs must match schema when present:
- `requirements`: `REQ-*`
- `nfr`: `NFR-*`
- `acceptance_criteria`: `AC-*`
- `risks`: `RSK-*`
- `interviews`: `INT-*`
- `user_research`: `UR-*`
- `evidence`: `EVD-*`

Minimum presence by artifact type:
- Evidence-driven artifacts (`RQM-ELC-*`, `RQM-INT-*`, `RQM-URS-*`): at least one of interviews/user_research/evidence.
- Requirement-bound artifacts (`RQM-DEF-*`, `RQM-PRI-*`, `RQM-NFR-*`, `RQM-ACD-*`, `RQM-RSK-*`, `RQM-UCM-*`, `RQM-STY-*`): `requirements` must be non-empty.
- Additional required sets:
  - `RQM-NFR-*`: `nfr`
  - `RQM-ACD-*`: `acceptance_criteria`
  - `RQM-RSK-*`: `risks`

## Privacy and Compliance Evidence
### `privacy_evidence` (required when personal data is handled)
- `lawful_basis_or_consent`
- `pii_data_inventory`
- `data_minimization_decision`
- `retention_and_deletion_policy`
- `cross_border_transfer_control`
- `data_subject_rights_process`
- `redaction_and_access_control`

### `compliance_evidence` (required for `RQM-CMP-*`)
- `jurisdiction_scope`
- `lawful_basis_summary`
- `retention_policy_reference`
- `cross_border_transfer_control`
- `data_subject_rights_path`
- `audit_log_location`
