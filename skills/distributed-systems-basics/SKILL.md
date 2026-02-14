---
name: distributed-systems-basics
description: Specialized workflow for distributed failure modes, consistency models, and reliability primitives. Use when multi-node consistency, partition tolerance, and fault-handling semantics are central; do not use for single-process application implementation details.
---

# Distributed Systems Basics

## Trigger Boundary
- Use when parallel execution, coordination, or distributed failure semantics are central.
- Do not use for UX interaction design concerns; use design-related skills.
- Do not use for single-query database tuning only; use `db-query-optimization`.

## Goal
Ensure correctness and resilience under concurrency and partial failures.

## Inputs
- Change scope and risk profile
- Domain evidence for distributed failure modes, consistency models, and reliability primitives
- Operational, compliance, and rollout constraints

## Outputs
- Distributed system baseline design notes
- Decision log for distributed failure modes, consistency models, and reliability primitives
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for distributed failure modes, consistency models, and reliability primitives.
2. Produce options and select an approach for distributed failure modes, consistency models, and reliability primitives.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using failure-mode walkthrough across network and node faults.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for distributed failure modes, consistency models, and reliability primitives are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when core distributed assumptions are undefined or contradictory.
- Escalate when accepted risk exceeds team policy thresholds.
