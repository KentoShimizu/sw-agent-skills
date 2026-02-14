---
name: db-replication-sharding
description: Specialized workflow for replication topology, shard strategy, and consistency trade-offs. Use when schema, indexing, query planning, transaction semantics, migration safety, or durability behavior is in scope; do not use for API boundary design or infrastructure provisioning.
---

# Db Replication Sharding

## Trigger Boundary
- Use when schema, indexing, transaction, migration, or durability behavior is in scope.
- Do not use for HTTP/API boundary design; use `api-*`.
- Do not use for cluster provisioning details; use `infrastructure-as-code` or `kubernetes-*`.

## Goal
Ensure data correctness, performance, and lifecycle reliability.

## Inputs
- Change scope and risk profile
- Domain evidence for replication topology, shard strategy, and consistency trade-offs
- Operational, compliance, and rollout constraints

## Outputs
- Replication and sharding topology decision
- Decision log for replication topology, shard strategy, and consistency trade-offs
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for replication topology, shard strategy, and consistency trade-offs.
2. Produce options and select an approach for replication topology, shard strategy, and consistency trade-offs.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using failover and rebalance simulations.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for replication topology, shard strategy, and consistency trade-offs are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when consistency guarantees or failover behavior are undefined.
- Escalate when accepted risk exceeds team policy thresholds.
