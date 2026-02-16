---
name: ml-model-selection
description: Specialized workflow for candidate model trade-offs across accuracy, latency, and cost. Trigger when selecting among multiple model candidates requires transparent tradeoff decisions against product KPIs and operational constraints; do not use for generic API-layer or infrastructure-only changes.
---

# Ml Model Selection

## Trigger Boundary
- Use when ML data, model, training, evaluation, or serving choices are being made.
- Do not use for generic API lifecycle governance; use `api-*`.
- Do not use for non-ML database administration concerns.

## Goal
Produce reliable ML lifecycle decisions from data to production monitoring.

## Inputs
- Change scope and risk profile
- Domain evidence for candidate model trade-offs across accuracy, latency, and cost
- Operational, compliance, and rollout constraints

## Outputs
- Model selection decision log
- Decision log for candidate model trade-offs across accuracy, latency, and cost
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for candidate model trade-offs across accuracy, latency, and cost.
2. Produce options and select an approach for candidate model trade-offs across accuracy, latency, and cost.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using head-to-head benchmark and robustness comparison.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for candidate model trade-offs across accuracy, latency, and cost are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when selected model lacks evidence against viable alternatives.
- Escalate when accepted risk exceeds team policy thresholds.
