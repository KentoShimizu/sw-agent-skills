---
name: ml-data-preprocessing
description: Specialized workflow for data cleaning, normalization, and leakage prevention rules. Use when model, data, feature, or training decisions for ML systems are in scope; do not use for generic API-layer or infrastructure-only changes.
---

# Ml Data Preprocessing

## Trigger Boundary
- Use when ML data, model, training, evaluation, or serving choices are being made.
- Do not use for generic API lifecycle governance; use `api-*`.
- Do not use for non-ML database administration concerns.

## Goal
Produce reliable ML lifecycle decisions from data to production monitoring.

## Inputs
- Change scope and risk profile
- Domain evidence for data cleaning, normalization, and leakage prevention rules
- Operational, compliance, and rollout constraints

## Outputs
- Data preprocessing pipeline specification
- Decision log for data cleaning, normalization, and leakage prevention rules
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for data cleaning, normalization, and leakage prevention rules.
2. Produce options and select an approach for data cleaning, normalization, and leakage prevention rules.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using dataset quality checks and leakage audit.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for data cleaning, normalization, and leakage prevention rules are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when preprocessing introduces label leakage or irreversible data loss.
- Escalate when accepted risk exceeds team policy thresholds.
