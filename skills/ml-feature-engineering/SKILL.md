---
name: ml-feature-engineering
description: Specialized workflow for feature generation, feature store consistency, and online-offline parity. Trigger when model performance depends on feature design and teams need explicit feature definitions, transformation logic, and offline/online parity controls; do not use for generic API-layer or infrastructure-only changes.
---

# Ml Feature Engineering

## Trigger Boundary
- Use when ML data, model, training, evaluation, or serving choices are being made.
- Do not use for generic API lifecycle governance; use `api-*`.
- Do not use for non-ML database administration concerns.

## Goal
Produce reliable ML lifecycle decisions from data to production monitoring.

## Inputs
- Change scope and risk profile
- Domain evidence for feature generation, feature store consistency, and online-offline parity
- Operational, compliance, and rollout constraints

## Outputs
- Feature specification catalog with lineage
- Decision log for feature generation, feature store consistency, and online-offline parity
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for feature generation, feature store consistency, and online-offline parity.
2. Produce options and select an approach for feature generation, feature store consistency, and online-offline parity.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using feature drift and leakage checks across training and serving.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for feature generation, feature store consistency, and online-offline parity are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when feature definitions are inconsistent between training and serving.
- Escalate when accepted risk exceeds team policy thresholds.
