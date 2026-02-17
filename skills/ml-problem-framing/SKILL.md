---
name: ml-problem-framing
description: "ML problem framing workflow for objective definition, target variable design, and success criteria. Use when translating business problems into ML tasks and objective/label/metric definitions are still ambiguous; do not use for generic API-layer or infrastructure-only changes."
---

# Ml Problem Framing

## Overview
Use this skill to define an ML problem that supports a real product decision with measurable outcomes.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- Objective and labeling rules:
  - `references/objective-and-labeling-rules.md`

## Templates And Assets
- Problem framing template:
  - `assets/problem-framing-template.md`

## Inputs To Gather
- Business decision to support and value target.
- Candidate prediction target and labeling source.
- Risk constraints (fairness, latency, compliance).
- Baseline process and non-ML alternatives.

## Deliverables
- Framed ML objective with explicit non-goals.
- Label definition and prediction unit.
- Success metrics and decision thresholds.
- Risks and assumptions log.

## Workflow
1. Define decision context with `assets/problem-framing-template.md`.
2. Validate objective/label choices using `references/objective-and-labeling-rules.md`.
3. Align metric choices to business and user outcomes.
4. Document assumptions, constraints, and alternatives.
5. Publish go/no-go framing decision.

## Quality Standard
- Objective is measurable and decision-relevant.
- Label definition is leakage-safe and reproducible.
- Metrics and thresholds are operationally actionable.

## Failure Conditions
- Stop when objective does not map to a concrete decision.
- Stop when label quality/timing cannot be validated.
- Escalate when framing risks exceed policy tolerance.
