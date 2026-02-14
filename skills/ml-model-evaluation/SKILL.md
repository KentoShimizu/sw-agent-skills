---
name: ml-model-evaluation
description: Specialized workflow for evaluation metrics, threshold selection, and failure segmentation. Use when model, data, feature, or training decisions for ML systems are in scope; do not use for generic API-layer or infrastructure-only changes.
---

# Ml Model Evaluation

## Trigger Boundary
- Use when ML data, model, training, evaluation, or serving choices are being made.
- Do not use for generic API lifecycle governance; use `api-*`.
- Do not use for non-ML database administration concerns.

## Goal
Produce reliable ML lifecycle decisions from data to production monitoring.

## Inputs
- Change scope and risk profile
- Domain evidence for evaluation metrics, threshold selection, and failure segmentation
- Operational, compliance, and rollout constraints

## Outputs
- Model evaluation report with acceptance thresholds
- Decision log for evaluation metrics, threshold selection, and failure segmentation
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for evaluation metrics, threshold selection, and failure segmentation.
2. Produce options and select an approach for evaluation metrics, threshold selection, and failure segmentation.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using slice-based metric review and calibration checks.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for evaluation metrics, threshold selection, and failure segmentation are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when evaluation ignores critical segments or risk-sensitive errors.
- Escalate when accepted risk exceeds team policy thresholds.
