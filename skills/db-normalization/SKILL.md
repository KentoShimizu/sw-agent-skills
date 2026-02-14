---
name: db-normalization
description: Specialized workflow for normal form decisions and update anomaly prevention. Use when schema, indexing, query planning, transaction semantics, migration safety, or durability behavior is in scope; do not use for API boundary design or infrastructure provisioning.
---

# Db Normalization

## Trigger Boundary
- Use when schema, indexing, transaction, migration, or durability behavior is in scope.
- Do not use for HTTP/API boundary design; use `api-*`.
- Do not use for cluster provisioning details; use `infrastructure-as-code` or `kubernetes-*`.

## Goal
Ensure data correctness, performance, and lifecycle reliability.

## Inputs
- Change scope and risk profile
- Domain evidence for normal form decisions and update anomaly prevention
- Operational, compliance, and rollout constraints

## Outputs
- Normalization decision record with trade-off rationale
- Decision log for normal form decisions and update anomaly prevention
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for normal form decisions and update anomaly prevention.
2. Produce options and select an approach for normal form decisions and update anomaly prevention.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using anomaly analysis for insert, update, and delete operations.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for normal form decisions and update anomaly prevention are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when normalization gaps cause unresolved integrity anomalies.
- Escalate when accepted risk exceeds team policy thresholds.
