---
name: testing-unit
description: Specialized workflow for small-scope deterministic unit behavior validation. Trigger when logic units need isolated, deterministic verification with fast feedback and controlled dependencies before broader integration testing; do not use for observability ownership or release scheduling policy.
---

# Testing Unit

## Trigger Boundary
- Use when verification strategy or release confidence evidence must be designed.
- Do not use for production observability ownership; use `observability-*`.
- Do not use for architecture topology selection.

## Goal
Build sufficient verification evidence to prevent regressions.

## Inputs
- Change scope and risk profile
- Domain evidence for small-scope deterministic unit behavior validation
- Operational, compliance, and rollout constraints

## Outputs
- Unit test suite with isolation strategy
- Decision log for small-scope deterministic unit behavior validation
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for small-scope deterministic unit behavior validation.
2. Produce options and select an approach for small-scope deterministic unit behavior validation.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using fast deterministic execution with dependency isolation.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for small-scope deterministic unit behavior validation are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when core units lack deterministic tests for edge and failure paths.
- Escalate when accepted risk exceeds team policy thresholds.
