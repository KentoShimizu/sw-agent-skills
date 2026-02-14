---
name: ml-experiment-tracking
description: Specialized workflow for experiment metadata integrity, reproducibility, and comparison traceability. Use when model, data, feature, or training decisions for ML systems are in scope; do not use for generic API-layer or infrastructure-only changes.
---

# Ml Experiment Tracking

## Trigger Boundary
- Use when ML data, model, training, evaluation, or serving choices are being made.
- Do not use for generic API lifecycle governance; use `api-*`.
- Do not use for non-ML database administration concerns.

## Goal
Produce reliable ML lifecycle decisions from data to production monitoring.

## Inputs
- Change scope and risk profile
- Domain evidence for experiment metadata integrity, reproducibility, and comparison traceability
- Operational, compliance, and rollout constraints

## Outputs
- Experiment tracking schema and logging plan
- Decision log for experiment metadata integrity, reproducibility, and comparison traceability
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for experiment metadata integrity, reproducibility, and comparison traceability.
2. Produce options and select an approach for experiment metadata integrity, reproducibility, and comparison traceability.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using re-run reproducibility checks from tracked metadata.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for experiment metadata integrity, reproducibility, and comparison traceability are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when experiment runs cannot be reproduced from recorded artifacts.
- Escalate when accepted risk exceeds team policy thresholds.
