---
name: testing-integration
description: Specialized workflow for component and service interaction correctness at integration boundaries. Use when designing verification strategy and evidence at this test level; do not use for observability ownership or release scheduling policy.
---

# Testing Integration

## Trigger Boundary
- Use when verification strategy or release confidence evidence must be designed.
- Do not use for production observability ownership; use `observability-*`.
- Do not use for architecture topology selection.

## Goal
Build sufficient verification evidence to prevent regressions.

## Inputs
- Change scope and risk profile
- Domain evidence for component and service interaction correctness at integration boundaries
- Operational, compliance, and rollout constraints

## Outputs
- Integration boundary test matrix
- Decision log for component and service interaction correctness at integration boundaries
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for component and service interaction correctness at integration boundaries.
2. Produce options and select an approach for component and service interaction correctness at integration boundaries.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using dependency and interface integration test runs.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for component and service interaction correctness at integration boundaries are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when integration seams are unverified for failure and timeout paths.
- Escalate when accepted risk exceeds team policy thresholds.
