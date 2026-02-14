---
name: db-conceptual-modeling
description: Specialized workflow for domain entities, relationships, and bounded context boundaries. Use when schema, indexing, query planning, transaction semantics, migration safety, or durability behavior is in scope; do not use for API boundary design or infrastructure provisioning.
---

# Db Conceptual Modeling

## Trigger Boundary
- Use when schema, indexing, transaction, migration, or durability behavior is in scope.
- Do not use for HTTP/API boundary design; use `api-*`.
- Do not use for cluster provisioning details; use `infrastructure-as-code` or `kubernetes-*`.

## Goal
Ensure data correctness, performance, and lifecycle reliability.

## Inputs
- Change scope and risk profile
- Domain evidence for domain entities, relationships, and bounded context boundaries
- Operational, compliance, and rollout constraints

## Outputs
- Conceptual domain model with entity relationship map
- Decision log for domain entities, relationships, and bounded context boundaries
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for domain entities, relationships, and bounded context boundaries.
2. Produce options and select an approach for domain entities, relationships, and bounded context boundaries.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using domain walkthrough with conflict and ambiguity checks.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for domain entities, relationships, and bounded context boundaries are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when core entities or relationships remain ambiguous.
- Escalate when accepted risk exceeds team policy thresholds.
