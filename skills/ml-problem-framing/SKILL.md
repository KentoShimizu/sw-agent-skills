---
name: ml-problem-framing
description: Specialized workflow for objective definition, target variable design, and success metrics. Trigger when a business problem is being translated into an ML task and objective/label/metric definitions are still ambiguous or contested; do not use for generic API-layer or infrastructure-only changes.
---

# Ml Problem Framing

## Trigger Boundary
- Use when ML data, model, training, evaluation, or serving choices are being made.
- Do not use for generic API lifecycle governance; use `api-*`.
- Do not use for non-ML database administration concerns.

## Goal
Produce reliable ML lifecycle decisions from data to production monitoring.

## Inputs
- Change scope and risk profile
- Domain evidence for objective definition, target variable design, and success metrics
- Operational, compliance, and rollout constraints

## Outputs
- Problem framing document with measurable objective
- Decision log for objective definition, target variable design, and success metrics
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for objective definition, target variable design, and success metrics.
2. Produce options and select an approach for objective definition, target variable design, and success metrics.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using objective-review against business and user constraints.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for objective definition, target variable design, and success metrics are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when problem statement is not measurable or decision-relevant.
- Escalate when accepted risk exceeds team policy thresholds.
