---
name: testing-property-based
description: Specialized workflow for invariant validation using randomized and generative inputs. Trigger when correctness depends on invariants across broad input spaces and generated/randomized tests are needed beyond finite example-based cases; do not use for observability ownership or release scheduling policy.
---

# Testing Property Based

## Trigger Boundary
- Use when verification strategy or release confidence evidence must be designed.
- Do not use for production observability ownership; use `observability-*`.
- Do not use for architecture topology selection.

## Goal
Build sufficient verification evidence to prevent regressions.

## Inputs
- Change scope and risk profile
- Domain evidence for invariant validation using randomized and generative inputs
- Operational, compliance, and rollout constraints

## Outputs
- Property specification and generator definition
- Decision log for invariant validation using randomized and generative inputs
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for invariant validation using randomized and generative inputs.
2. Produce options and select an approach for invariant validation using randomized and generative inputs.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using property test runs with shrinking evidence.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for invariant validation using randomized and generative inputs are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when core invariants are not expressible or repeatedly violated.
- Escalate when accepted risk exceeds team policy thresholds.
