---
name: mlops-monitoring-drift
description: Specialized workflow for data drift, concept drift, and model quality degradation detection. Trigger when production ML systems need drift/quality monitoring design with actionable detection thresholds, diagnostics, and retraining escalation rules; do not use for model-architecture research decisions.
---

# Mlops Monitoring Drift

## Trigger Boundary
- Use when ML data, model, training, evaluation, or serving choices are being made.
- Do not use for generic API lifecycle governance; use `api-*`.
- Do not use for non-ML database administration concerns.

## Goal
Produce reliable ML lifecycle decisions from data to production monitoring.

## Inputs
- Change scope and risk profile
- Domain evidence for data drift, concept drift, and model quality degradation detection
- Operational, compliance, and rollout constraints

## Outputs
- Drift monitoring policy with alert thresholds
- Decision log for data drift, concept drift, and model quality degradation detection
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for data drift, concept drift, and model quality degradation detection.
2. Produce options and select an approach for data drift, concept drift, and model quality degradation detection.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using historical replay and alert precision checks.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for data drift, concept drift, and model quality degradation detection are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when drift detection lacks actionable thresholds or ownership.
- Escalate when accepted risk exceeds team policy thresholds.
