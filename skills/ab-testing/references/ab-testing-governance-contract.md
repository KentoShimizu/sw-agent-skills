# AB Testing Governance Contract

## Scope
Apply this contract to all artifacts produced by `ab-testing`.
Do not redefine ID formats, lifecycle states, or gate rules in local notes.

## ID Schema (Single Source of Truth)
- `AB-PLN-<YYYYMMDD>-<NNN>`: `^AB-PLN-[0-9]{8}-[0-9]{3,}$`
  - Meaning: experiment plan and pre-registered analysis design
  - Issuer: experiment owner
  - Uniqueness: repository-wide
- `AB-DEC-<YYYYMMDD>-<NNN>`: `^AB-DEC-[0-9]{8}-[0-9]{3,}$`
  - Meaning: post-run decision record and rollout action
  - Issuer: experiment owner
  - Uniqueness: repository-wide

## Lifecycle Rules
- `AB-PLN-*`: `draft`, `reviewed`, `approved`, `active`, `stopped`, `completed`
- `AB-DEC-*`: `draft`, `reviewed`, `finalized`

## Approval Matrix
- Required for all experiment artifacts:
  - `Experiment Owner`
  - `Data Science Reviewer`
- Required when `checks.external_user_impact = true`:
  - `Legal Reviewer` or `Privacy Reviewer`

## Required Check Flags
Manifest field: `checks`

- Must be `true`:
  - `id_format_validated`
  - `pre_registration_complete`
  - `randomization_plan_defined`
  - `assignment_unit_defined`
  - `instrumentation_validated`
  - `srm_monitor_defined`
  - `guardrail_policy_defined`
  - `one_primary_metric_defined`
  - `no_posthoc_decision_rule_changes`
- Must be boolean:
  - `external_user_impact`

## Decision Context Requirements
Manifest field: `decision_context`

- Required non-empty strings:
  - `decision_question`
  - `primary_decision_metric`
  - `randomization_method`
  - `contamination_risk_mitigation`
- Required risk levels:
  - `false_positive_cost` in `low | medium | high | critical`
  - `false_negative_cost` in `low | medium | high | critical`
- Required assignment unit:
  - `assignment_unit` in `user | session | org | device`
- Required decision action list:
  - `allowed_actions` must be non-empty
  - Every action must be one of `ship | iterate | rollback | hold`

## Evidence Plan Requirements (`AB-PLN-*`)
Manifest field: `evidence_plan`

- Required numeric bounds:
  - `min_detectable_effect_pct` > 0
  - `confidence_level` in (0, 1)
  - `power_target` in (0, 1)
- Required runtime windows:
  - `minimum_runtime_days` >= 7
  - `baseline_window_days` >= 7
- Required analysis method:
  - `analysis_method` in `fixed_horizon | sequential`
  - `multiplicity_control` must be non-empty
- Required guardrails:
  - `guardrails` must be a non-empty array of non-empty strings

## Decision Result Requirements (`AB-DEC-*`)
Manifest field: `result`

- Required outcome:
  - `decision_outcome` in `ship | iterate | rollback | hold`
- Required quantitative summary:
  - `primary_metric_effect_pct` must be numeric
  - `uncertainty_interval` must be non-empty
- Required guardrail interpretation:
  - `guardrail_status` in `pass | mixed | fail`
- Required execution integrity:
  - `complies_with_pre_registered_rules` must be `true`
- Required documentation:
  - `interpretation` must be non-empty
  - `follow_up_actions` must be a non-empty array of non-empty strings

## Gate Policy
- Block when required approvers are missing.
- Block when ID format or lifecycle state is invalid.
- Block when checks are missing or set to false.
- Block when evidence plan is insufficient for decision-quality inference.
- Block when decision outcomes contradict guardrail status (`ship` with `fail` guardrails).

## Machine Validation
- Run:
  - `python3 skills/ab-testing/scripts/validate_ab_testing_contract.py --manifest <path/to/manifest.json>`
- For batch validation:
  - `python3 scripts/run_contract_validators.py --ab-manifest <path/to/manifest.json>`

## Valid Manifest Samples
- `skills/ab-testing/assets/ab-pln-manifest.valid.json`
- `skills/ab-testing/assets/ab-dec-manifest.valid.json`
