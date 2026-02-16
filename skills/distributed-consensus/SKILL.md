---
name: distributed-consensus
description: Specialized workflow for consensus protocol guarantees, quorum rules, and failure handling. Trigger when correctness depends on multi-node agreement under failures or partitions (leader election, quorum writes, commit guarantees) and consensus properties must be explicit; do not use for single-process application implementation details.
---

# Distributed Consensus

## Trigger Boundary
- Use when parallel execution, coordination, or distributed failure semantics are central.
- Do not use for UX interaction design concerns; use design-related skills.
- Do not use for single-query database tuning only; use `db-query-optimization`.

## Goal
Ensure correctness and resilience under concurrency and partial failures.

## Inputs
- Change scope and risk profile
- Domain evidence for consensus protocol guarantees, quorum rules, and failure handling
- Operational, compliance, and rollout constraints

## Outputs
- Consensus design and fault model document
- Decision log for consensus protocol guarantees, quorum rules, and failure handling
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for consensus protocol guarantees, quorum rules, and failure handling.
2. Produce options and select an approach for consensus protocol guarantees, quorum rules, and failure handling.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using partition and leader-failure simulation.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for consensus protocol guarantees, quorum rules, and failure handling are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when consensus safety or liveness guarantees are unverified.
- Escalate when accepted risk exceeds team policy thresholds.
