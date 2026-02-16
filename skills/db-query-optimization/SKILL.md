---
name: db-query-optimization
description: Specialized workflow for query rewrite, plan stability, and latency reduction on hot paths. Trigger when critical queries miss SLOs, execution plans are unstable, or resource usage is excessive and query-level remediation must be chosen before release; do not use for API boundary design or infrastructure provisioning.
---

# Db Query Optimization

## Trigger Boundary
- Use when schema, indexing, transaction, migration, or durability behavior is in scope.
- Do not use for HTTP/API boundary design; use `api-*`.
- Do not use for cluster provisioning details; use `infrastructure-as-code` or `kubernetes-*`.

## Goal
Ensure data correctness, performance, and lifecycle reliability.

## Inputs
- Change scope and risk profile
- Domain evidence for query rewrite, plan stability, and latency reduction on hot paths
- Operational, compliance, and rollout constraints

## Outputs
- Query optimization report with before/after benchmarks
- Decision log for query rewrite, plan stability, and latency reduction on hot paths
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for query rewrite, plan stability, and latency reduction on hot paths.
2. Produce options and select an approach for query rewrite, plan stability, and latency reduction on hot paths.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using query plan and latency benchmark comparison.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for query rewrite, plan stability, and latency reduction on hot paths are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when critical query latency remains above agreed thresholds.
- Escalate when accepted risk exceeds team policy thresholds.
