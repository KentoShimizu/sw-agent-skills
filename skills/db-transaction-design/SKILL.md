---
name: db-transaction-design
description: Specialized workflow for transaction boundaries, isolation levels, and contention control. Trigger when multi-step write operations need explicit transaction semantics (boundary, isolation, retry/idempotency, lock contention behavior) to guarantee correctness under concurrency; do not use for API boundary design or infrastructure provisioning.
---

# Db Transaction Design

## Trigger Boundary
- Use when schema, indexing, transaction, migration, or durability behavior is in scope.
- Do not use for HTTP/API boundary design; use `api-*`.
- Do not use for cluster provisioning details; use `infrastructure-as-code` or `kubernetes-*`.

## Goal
Ensure data correctness, performance, and lifecycle reliability.

## Inputs
- Change scope and risk profile
- Domain evidence for transaction boundaries, isolation levels, and contention control
- Operational, compliance, and rollout constraints

## Outputs
- Transaction design specification by use case
- Decision log for transaction boundaries, isolation levels, and contention control
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for transaction boundaries, isolation levels, and contention control.
2. Produce options and select an approach for transaction boundaries, isolation levels, and contention control.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using concurrency test scenarios for deadlock and anomaly detection.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for transaction boundaries, isolation levels, and contention control are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when transaction boundaries allow data anomalies or deadlocks.
- Escalate when accepted risk exceeds team policy thresholds.
