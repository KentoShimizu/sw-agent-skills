---
name: testing-contract
description: Specialized workflow for provider-consumer contract compatibility across service boundaries. Use when designing verification strategy and evidence at this test level; do not use for observability ownership or release scheduling policy.
---

# Testing Contract

## Trigger Boundary
- Use when verification strategy or release confidence evidence must be designed.
- Do not use for production observability ownership; use `observability-*`.
- Do not use for architecture topology selection.

## Goal
Build sufficient verification evidence to prevent regressions.

## Inputs
- Change scope and risk profile
- Domain evidence for provider-consumer contract compatibility across service boundaries
- Operational, compliance, and rollout constraints

## Outputs
- Versioned consumer-provider contract set
- Decision log for provider-consumer contract compatibility across service boundaries
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for provider-consumer contract compatibility across service boundaries.
2. Produce options and select an approach for provider-consumer contract compatibility across service boundaries.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using contract verification in CI for both provider and consumer.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for provider-consumer contract compatibility across service boundaries are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when contract mismatches break backward expectations between services.
- Escalate when accepted risk exceeds team policy thresholds.
