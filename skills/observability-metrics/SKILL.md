---
name: observability-metrics
description: Specialized workflow for metric model design aligned to service health and business impact. Use when telemetry signal design, alertability, and operational detection policy are in scope; do not use for business-feature implementation logic.
---

# Observability Metrics

## Trigger Boundary
- Use when production visibility, reliability targets, or incident response workflows are needed.
- Do not use for feature-level functional spec writing; use `requirements-*`.
- Do not use for pure code-style conformance checks.

## Goal
Maintain production reliability through measurable operational controls.

## Inputs
- Change scope and risk profile
- Domain evidence for metric model design aligned to service health and business impact
- Operational, compliance, and rollout constraints

## Outputs
- Metrics taxonomy and dashboard contract
- Decision log for metric model design aligned to service health and business impact
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for metric model design aligned to service health and business impact.
2. Produce options and select an approach for metric model design aligned to service health and business impact.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using metric cardinality and SLI correlation review.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for metric model design aligned to service health and business impact are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when key health indicators are missing or misleading.
- Escalate when accepted risk exceeds team policy thresholds.
