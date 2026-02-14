---
name: sre-sli-slo
description: Specialized workflow for SLI definition, SLO target setting, and error budget policy. Use when telemetry signal design, alertability, and operational detection policy are in scope; do not use for business-feature implementation logic.
---

# Sre Sli Slo

## Trigger Boundary
- Use when production visibility, reliability targets, or incident response workflows are needed.
- Do not use for feature-level functional spec writing; use `requirements-*`.
- Do not use for pure code-style conformance checks.

## Goal
Maintain production reliability through measurable operational controls.

## Inputs
- Change scope and risk profile
- Domain evidence for SLI definition, SLO target setting, and error budget policy
- Operational, compliance, and rollout constraints

## Outputs
- SLI/SLO catalog with error-budget rules
- Decision log for SLI definition, SLO target setting, and error budget policy
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for SLI definition, SLO target setting, and error budget policy.
2. Produce options and select an approach for SLI definition, SLO target setting, and error budget policy.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using historical data fit and burn-rate simulation.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for SLI definition, SLO target setting, and error budget policy are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when SLO targets are not measurable from available telemetry.
- Escalate when accepted risk exceeds team policy thresholds.
