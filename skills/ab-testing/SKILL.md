---
name: ab-testing
description: "Experiment design and analysis workflow for controlled A B tests on product changes. Use when controlled online experiments require hypothesis, randomization, and decision thresholds; do not use for feature-flag rollout policy without experiment design."
---

# Ab Testing

## Trigger Boundary
- Use when product-impacting changes require controlled experiment validation.
- Do not use for deterministic functional verification; use `testing-*`.
- Do not use for long-term reliability telemetry design; use `observability-*`.

## Goal
Produce statistically and operationally sound experiment decisions.

## Inputs
- Experiment hypothesis and expected user/business outcome
- Current baseline metrics and traffic constraints
- Risk thresholds, guardrails, and stop conditions

## Outputs
- Experiment plan with metric definitions and guardrails
- Analysis plan and decision thresholds
- Post-experiment decision record and follow-up actions

## Workflow
1. Define hypothesis, target population, and experiment guardrails.
2. Define primary and secondary metrics with decision thresholds.
3. Validate randomization and sample-size assumptions.
4. Run experiment with safety monitors and stop criteria.
5. Analyze outcomes and publish decision with confidence bounds.

## Quality Gates
- Metrics and stop conditions are explicit and auditable.
- Experiment population and randomization assumptions are documented.
- Decision criteria are defined before outcome analysis.
- Privacy and compliance checks pass for user data handling.

## Failure Handling
- Stop when metric definitions or stop conditions are missing.
- Escalate when experiment risk exceeds agreed guardrails.
