---
name: mlops-model-serving
description: Specialized workflow for serving architecture, latency SLOs, and rollout safety. Trigger when ML models must be deployed to production serving paths and teams need explicit decisions on serving topology, latency/error budgets, and safe rollout controls; do not use for model-architecture research decisions.
---

# Mlops Model Serving

## Trigger Boundary
- Use when ML data, model, training, evaluation, or serving choices are being made.
- Do not use for generic API lifecycle governance; use `api-*`.
- Do not use for non-ML database administration concerns.

## Goal
Produce reliable ML lifecycle decisions from data to production monitoring.

## Inputs
- Change scope and risk profile
- Domain evidence for serving architecture, latency SLOs, and rollout safety
- Operational, compliance, and rollout constraints

## Outputs
- Model serving deployment specification
- Decision log for serving architecture, latency SLOs, and rollout safety
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for serving architecture, latency SLOs, and rollout safety.
2. Produce options and select an approach for serving architecture, latency SLOs, and rollout safety.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using load and canary behavior validation for serving endpoints.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for serving architecture, latency SLOs, and rollout safety are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when serving latency or reliability targets are not met.
- Escalate when accepted risk exceeds team policy thresholds.
