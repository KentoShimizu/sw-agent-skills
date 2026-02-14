---
name: observability-logging
description: Specialized workflow for structured logging schema and incident triage utility. Use when telemetry signal design, alertability, and operational detection policy are in scope; do not use for business-feature implementation logic.
---

# Observability Logging

## Trigger Boundary
- Use when production visibility, reliability targets, or incident response workflows are needed.
- Do not use for feature-level functional spec writing; use `requirements-*`.
- Do not use for pure code-style conformance checks.

## Goal
Maintain production reliability through measurable operational controls.

## Inputs
- Change scope and risk profile
- Domain evidence for structured logging schema and incident triage utility
- Operational, compliance, and rollout constraints

## Outputs
- Logging schema and retention policy
- Decision log for structured logging schema and incident triage utility
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for structured logging schema and incident triage utility.
2. Produce options and select an approach for structured logging schema and incident triage utility.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using searchability and correlation tests with incident scenarios.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for structured logging schema and incident triage utility are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when logs lack required context for troubleshooting.
- Escalate when accepted risk exceeds team policy thresholds.
