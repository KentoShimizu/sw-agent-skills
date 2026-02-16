---
name: observability-tracing
description: Specialized workflow for distributed trace coverage and critical path latency diagnosis. Trigger when cross-service request paths need trace instrumentation or analysis to localize latency/error bottlenecks and dependency failure propagation; do not use for business-feature implementation logic.
---

# Observability Tracing

## Trigger Boundary
- Use when production visibility, reliability targets, or incident response workflows are needed.
- Do not use for feature-level functional spec writing; use `requirements-*`.
- Do not use for pure code-style conformance checks.

## Goal
Maintain production reliability through measurable operational controls.

## Inputs
- Change scope and risk profile
- Domain evidence for distributed trace coverage and critical path latency diagnosis
- Operational, compliance, and rollout constraints

## Outputs
- Trace instrumentation map for critical flows
- Decision log for distributed trace coverage and critical path latency diagnosis
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for distributed trace coverage and critical path latency diagnosis.
2. Produce options and select an approach for distributed trace coverage and critical path latency diagnosis.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using trace completeness and span attribute validation.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for distributed trace coverage and critical path latency diagnosis are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when critical request paths are not traceable end-to-end.
- Escalate when accepted risk exceeds team policy thresholds.
