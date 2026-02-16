---
name: concurrency-patterns
description: Specialized workflow for shared-state safety, coordination primitives, and contention control. Trigger when code introduces parallel execution, shared mutable state, or async coordination and needs explicit safety/liveness decisions (race prevention, deadlock avoidance, and contention control); do not use for persistence schema design or deployment topology choices.
---

# Concurrency Patterns

## Trigger Boundary
- Use when parallel execution, coordination, or distributed failure semantics are central.
- Do not use for UX interaction design concerns; use design-related skills.
- Do not use for single-query database tuning only; use `db-query-optimization`.

## Goal
Ensure correctness and resilience under concurrency and partial failures.

## Inputs
- Change scope and risk profile
- Domain evidence for shared-state safety, coordination primitives, and contention control
- Operational, compliance, and rollout constraints

## Outputs
- Concurrency pattern selection record
- Decision log for shared-state safety, coordination primitives, and contention control
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for shared-state safety, coordination primitives, and contention control.
2. Produce options and select an approach for shared-state safety, coordination primitives, and contention control.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using race-condition and contention stress tests.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for shared-state safety, coordination primitives, and contention control are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when selected pattern allows race conditions or deadlocks.
- Escalate when accepted risk exceeds team policy thresholds.
