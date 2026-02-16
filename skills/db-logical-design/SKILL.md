---
name: db-logical-design
description: Specialized workflow for table structure, keys, constraints, and relational consistency. Trigger when entities and relationships must be translated into relational tables with enforceable keys, constraints, and integrity rules before migration or implementation; do not use for API boundary design or infrastructure provisioning.
---

# Db Logical Design

## Trigger Boundary
- Use when schema, indexing, transaction, migration, or durability behavior is in scope.
- Do not use for HTTP/API boundary design; use `api-*`.
- Do not use for cluster provisioning details; use `infrastructure-as-code` or `kubernetes-*`.

## Goal
Ensure data correctness, performance, and lifecycle reliability.

## Inputs
- Change scope and risk profile
- Domain evidence for table structure, keys, constraints, and relational consistency
- Operational, compliance, and rollout constraints

## Outputs
- Logical schema specification with key and constraint definitions
- Decision log for table structure, keys, constraints, and relational consistency
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for table structure, keys, constraints, and relational consistency.
2. Produce options and select an approach for table structure, keys, constraints, and relational consistency.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using schema rule checks for integrity and referential consistency.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for table structure, keys, constraints, and relational consistency are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when key constraints or integrity rules are missing.
- Escalate when accepted risk exceeds team policy thresholds.
