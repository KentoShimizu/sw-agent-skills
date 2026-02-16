---
name: testing-tdd
description: Specialized workflow for red-green-refactor discipline and test-first design feedback. Trigger when implementation approach requires test-first iteration to shape design, lock behavior, and reduce regression risk from the first code change; do not use for observability ownership or release scheduling policy.
---

# Testing Tdd

## Trigger Boundary
- Use when verification strategy or release confidence evidence must be designed.
- Do not use for production observability ownership; use `observability-*`.
- Do not use for architecture topology selection.

## Goal
Build sufficient verification evidence to prevent regressions.

## Inputs
- Change scope and risk profile
- Domain evidence for red-green-refactor discipline and test-first design feedback
- Operational, compliance, and rollout constraints

## Outputs
- TDD cycle evidence with failing-then-passing tests
- Decision log for red-green-refactor discipline and test-first design feedback
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for red-green-refactor discipline and test-first design feedback.
2. Produce options and select an approach for red-green-refactor discipline and test-first design feedback.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using commit-level trace of test-first evolution.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for red-green-refactor discipline and test-first design feedback are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when implementation lands without preceding failing tests.
- Escalate when accepted risk exceeds team policy thresholds.
