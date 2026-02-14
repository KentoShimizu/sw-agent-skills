---
name: mlops-pipeline-design
description: Specialized workflow for orchestration of training, validation, packaging, and promotion stages. Use when ML deployment, monitoring, and pipeline operations are in scope; do not use for model-architecture research decisions.
---

# Mlops Pipeline Design

## Trigger Boundary
- Use when ML data, model, training, evaluation, or serving choices are being made.
- Do not use for generic API lifecycle governance; use `api-*`.
- Do not use for non-ML database administration concerns.

## Goal
Produce reliable ML lifecycle decisions from data to production monitoring.

## Inputs
- Change scope and risk profile
- Domain evidence for orchestration of training, validation, packaging, and promotion stages
- Operational, compliance, and rollout constraints

## Outputs
- MLOps pipeline architecture and stage contract
- Decision log for orchestration of training, validation, packaging, and promotion stages
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for orchestration of training, validation, packaging, and promotion stages.
2. Produce options and select an approach for orchestration of training, validation, packaging, and promotion stages.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using pipeline dry-run across success and failure branches.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for orchestration of training, validation, packaging, and promotion stages are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when pipeline stages are not reproducible or promotion gates are missing.
- Escalate when accepted risk exceeds team policy thresholds.
