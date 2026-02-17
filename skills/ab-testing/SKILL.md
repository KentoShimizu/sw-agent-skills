---
name: ab-testing
description: "Controlled online experiment workflow for product changes with causal inference, randomization integrity checks, and pre-registered decision criteria. Trigger when ship/no-ship decisions require causal evidence under uncertainty and KPI trade-offs must be quantified. Do not use for feature-flag rollout policy without experiment design, deterministic functional verification, or observability-only analysis."
---

# Ab Testing

## Scope Boundaries
- Use when product, pricing, ranking, recommendation, or policy changes may impact user/business KPIs and causal validation is required.
- Use proactively when metric impact is uncertain, stakeholder opinions conflict, or ship/no-ship criteria are not explicit.
- Use when canary metrics alone are insufficient to support a decision.
- Do not use for deterministic functional verification; use `testing-*`.
- Do not use for long-term reliability telemetry design; use `observability-*`.

## Goal
Produce causally valid, operationally safe, and decision-ready experiment outcomes.

## Shared Experiment Contract (Canonical)
- Use `references/ab-testing-governance-contract.md` as the primary reference for recommended structure.
- Optional consistency checks (only if your repository enforces manifest validation):
  - `python3 scripts/validate_ab_testing_contract.py --manifest <path/to/manifest.json>`
- Start from valid templates in `assets/`:
  - `assets/ab-pln-manifest.valid.json`
  - `assets/ab-dec-manifest.valid.json`
- Use decision-rule details in:
  - `references/decision-threshold-playbook.md`
- Do not define local ID formats, lifecycle states, or gate rules in this file.

## Implementation Templates
- Experiment charter template:
  - `assets/ab-experiment-charter-template.md`
- Decision record template:
  - `assets/ab-decision-record-template.md`

## Inputs
- Proposed change and explicit decision to be made (`ship`, `iterate`, `rollback`, `hold`).
- Business objective and target KPI with current baseline/variance estimates.
- Traffic budget, experiment window constraints, and seasonality considerations.
- Risk posture for false positives/false negatives and required confidence level.
- Guardrail metrics (reliability, latency, abuse, revenue-risk, support load).
- Data contract and instrumentation readiness for all required events.

## Outputs
- Experiment charter: hypothesis, population, assignment unit, randomization method, and contamination controls.
- Analysis plan: primary metric, secondary metrics, guardrails, `MIN_DETECTABLE_EFFECT`, confidence/precision targets, and decision gates.
- Runbook for monitoring, stop/escalation criteria, and incident response during experiment.
- Decision record with effect sizes, uncertainty bounds, segmentation caveats, and rollout recommendation.

## Decision Framework
- Define explicit costs for wrong decisions:
  - `FALSE_POSITIVE_COST`: shipping harmful change.
  - `FALSE_NEGATIVE_COST`: rejecting beneficial change.
- Set statistical strictness from decision risk, not preference:
  - Higher `FALSE_POSITIVE_COST` -> stricter false-positive control.
  - Higher `FALSE_NEGATIVE_COST` -> higher power and/or larger sample.
- Derive `MIN_DETECTABLE_EFFECT` from minimum business-material impact worth shipping.
- Use one primary decision metric; other metrics are supportive or guardrails.
- Pre-register ship criteria before exposure starts; do not redefine after peeking.

## Workflow
1. Frame the decision and hypothesis.
   - Specify target behavior change, affected population, and unacceptable harm scenarios.
   - Record decision owner and approvers for release risk.
2. Define metrics and decision rules before launch.
   - Choose exactly one primary metric for go/no-go.
   - Define guardrails and hard stop conditions (for example reliability or revenue damage).
   - Document attribution window, aggregation level, and missing-data handling.
3. Design assignment and contamination controls.
   - Select assignment unit (`user`, `session`, `org`, `device`) based on interference risk.
   - Define randomization strategy and stratification requirements.
   - Prevent spillover between treatment/control where feasible.
4. Plan evidence requirements.
   - Estimate sample size from baseline, variance, `MIN_DETECTABLE_EFFECT`, and confidence/power targets.
   - Define fixed-horizon or sequential analysis plan before runtime.
   - Ensure minimum runtime captures weekday/weekend and campaign effects.
5. Validate instrumentation and randomization integrity.
   - Run event schema and logging checks before exposure ramp.
   - Monitor sample ratio mismatch (SRM) and stop if assignment integrity is broken.
6. Execute with operational safeguards.
   - Ramp traffic gradually with explicit hold points.
   - Continuously evaluate guardrails and trigger rollback on hard breaches.
7. Analyze according to the pre-registered plan.
   - Report effect size and uncertainty interval for primary metric.
   - Treat unplanned segment findings as exploratory unless pre-registered.
   - Apply multiplicity control when multiple hypotheses can drive decisions.
8. Make and document the decision.
   - `ship`: primary metric meets target and all guardrails remain within limits.
   - `iterate`: inconclusive or mixed result without severe harm.
   - `rollback`: primary harm or guardrail breach beyond allowed limits.
9. Capture learning for reuse.
   - Record assumptions that were wrong (baseline, variance, ramp safety).
   - Update experiment playbook and metric definitions for future tests.

## Quality Gates
- Decision question, owner, and allowed actions are explicit and auditable.
- Assignment unit and contamination risk are documented with mitigation.
- Evidence plan includes `MIN_DETECTABLE_EFFECT`, confidence/power targets, and runtime rationale.
- SRM/instrumentation integrity checks pass before interpreting outcomes.
- Guardrail breach policy and rollback procedure are defined before launch.
- Analysis follows pre-registered rules; exploratory insights are clearly labeled.
- Privacy/compliance checks pass for user data collection and joins.

## Failure Handling
- Stop when primary metric, assignment unit, or decision criteria are undefined.
- Stop when SRM or telemetry integrity failures invalidate causal interpretation.
- Escalate when expected exposure risk exceeds approved guardrails.
- Escalate when required sample size/time budget cannot support a decision-quality experiment.
