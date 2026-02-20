# AB Testing Governance Contract

## Scope
Apply this contract to all artifacts produced by `ab-testing`.
Project teams must define and operate a repository-specific ID policy.
Treat this document as operational guidance, not a mandatory schema.
When repository-specific rules exist, follow those first; otherwise use this as a default operating method.

## Manifest Profile Model (Canonical)
Validation profiles are inferred from manifest structure, not from a fixed ID format.

Profiles:
- `experiment_plan`
  - Identified when `evidence_plan` or `guardrails` is present.
- `decision_record`
  - Identified when `result` is present.

## ID Format Policy (Project-Defined)
- `artifact_id` is optional and project-defined.
- If present, it must be non-empty and should follow your repository's ID policy.
- `checks.id_format_validated=true` means the manifest was validated against that project policy.

## Lifecycle Rules
- `experiment_plan`: `draft`, `reviewed`, `approved`, `active`, `stopped`, `completed`
- `decision_record`: `draft`, `reviewed`, `finalized`

## Approval Matrix
- Required for all experiment artifacts:
  - `Experiment Owner`
  - `Data Science Reviewer`
- Required when `checks.external_user_impact = true`:
  - `Legal Reviewer` or `Privacy Reviewer`

## Required Check Flags
Manifest field: `checks`

- Recommended `true` flags:
  - `id_format_validated`
  - `pre_registration_complete`
  - `randomization_plan_defined`
  - `assignment_unit_defined`
  - `instrumentation_validated`
  - `srm_monitor_defined`
  - `guardrail_policy_defined`
  - `one_primary_metric_defined`
  - `no_posthoc_decision_rule_changes`
- Recommended boolean flag:
  - `external_user_impact`

## Decision Context Guidance
Manifest field: `decision_context`

- Recommended non-empty strings:
  - `decision_question`
  - `primary_decision_metric`
  - `randomization_method`
  - `contamination_risk_mitigation`
- Recommended risk levels:
  - `false_positive_cost` in `low | medium | high | critical`
  - `false_negative_cost` in `low | medium | high | critical`
- Recommended assignment unit:
  - `assignment_unit` in `user | session | org | device`
- Recommended decision action list:
  - `allowed_actions` should be non-empty
  - Prefer one of `ship | iterate | rollback | hold`

## Evidence Plan Guidance (`experiment_plan` profile)
Manifest field: `evidence_plan`

- Recommended numeric bounds:
  - `min_detectable_effect_pct` > 0
  - `confidence_level` in (0, 1)
  - `power_target` in (0, 1)
- Recommended runtime windows:
  - `minimum_runtime_days` >= 7
  - `baseline_window_days` >= 7
- Recommended analysis method:
  - `analysis_method` in `fixed_horizon | sequential`
  - `multiplicity_control` must be non-empty
- Recommended guardrails:
  - `guardrails` should be a non-empty array of non-empty strings

## Decision Result Guidance (`decision_record` profile)
Manifest field: `result`

- Recommended outcome:
  - `decision_outcome` in `ship | iterate | rollback | hold`
- Recommended quantitative summary:
  - `primary_metric_effect_pct` should be numeric
  - `uncertainty_interval` should be non-empty
- Recommended guardrail interpretation:
  - `guardrail_status` in `pass | mixed | fail`
- Recommended execution integrity:
  - `complies_with_pre_registered_rules` should be `true`
- Recommended documentation:
  - `interpretation` should be non-empty
  - `follow_up_actions` should be a non-empty array of non-empty strings

## Operational Handling (Recommended)
- Escalate when approvers are missing.
- Escalate when inferred profile and lifecycle state do not match.
- Escalate when critical checks are missing or false.
- Escalate when evidence plan is insufficient for decision-quality inference.
- Escalate when decision outcomes contradict guardrail status (`ship` with `fail` guardrails).

## Optional Consistency Check
- Optional:
  - `python3 skills/ab-testing/scripts/validate_ab_testing_contract.py --manifest <path/to/manifest.json>`

## Valid Manifest Samples (Example IDs)
- `skills/ab-testing/assets/ab-pln-manifest.valid.json`
- `skills/ab-testing/assets/ab-dec-manifest.valid.json`
