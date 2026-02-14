---
name: observability-alerting
description: Specialized workflow for alert signal quality, routing policy, and actionable thresholds. Use when telemetry signal design, alertability, and operational detection policy are in scope; do not use for business-feature implementation logic.
---

# Observability Alerting

## Trigger Boundary
- Use when production visibility, reliability targets, or incident response workflows are needed.
- Do not use for feature-level functional spec writing; use `requirements-*`.
- Do not use for pure code-style conformance checks.

## Goal
Maintain production reliability through measurable operational controls.

## Inputs
- Change scope and risk profile
- Domain evidence for alert signal quality, routing policy, and actionable thresholds
- Operational, compliance, and rollout constraints

## Outputs
- Alert rule catalog with severity routing
- Decision log for alert signal quality, routing policy, and actionable thresholds
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for alert signal quality, routing policy, and actionable thresholds.
2. Produce options and select an approach for alert signal quality, routing policy, and actionable thresholds.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using alert precision and noise ratio review.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for alert signal quality, routing policy, and actionable thresholds are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when alerts are noisy, non-actionable, or missing critical paths.
- Escalate when accepted risk exceeds team policy thresholds.
