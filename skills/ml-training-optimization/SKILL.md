---
name: ml-training-optimization
description: Specialized workflow for training efficiency, convergence stability, and resource utilization. Trigger when training runs are too slow, unstable, or costly and optimization decisions (batching, scheduling, precision, checkpointing, hyperparameter strategy) are required; do not use for generic API-layer or infrastructure-only changes.
---

# Ml Training Optimization

## Trigger Boundary
- Use when ML data, model, training, evaluation, or serving choices are being made.
- Do not use for generic API lifecycle governance; use `api-*`.
- Do not use for non-ML database administration concerns.

## Goal
Produce reliable ML lifecycle decisions from data to production monitoring.

## Inputs
- Change scope and risk profile
- Domain evidence for training efficiency, convergence stability, and resource utilization
- Operational, compliance, and rollout constraints

## Outputs
- Training optimization plan with run budget
- Decision log for training efficiency, convergence stability, and resource utilization
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for training efficiency, convergence stability, and resource utilization.
2. Produce options and select an approach for training efficiency, convergence stability, and resource utilization.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using learning curve and resource usage profiling.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for training efficiency, convergence stability, and resource utilization are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when training cannot meet time or cost constraints.
- Escalate when accepted risk exceeds team policy thresholds.
