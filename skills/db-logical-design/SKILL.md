---
name: db-logical-design
description: "Design logical schema (tables, keys, constraints, relationships) from approved conceptual models and access requirements. Use when relational consistency and integrity rules must be codified before implementation; do not use for engine-specific storage tuning or deployment topology design."
---

# DB Logical Design

## Overview
Use this skill to produce a schema that preserves business invariants while remaining queryable and maintainable.

## Inputs To Gather
- Approved conceptual model.
- Access patterns (read/write paths and join paths).
- Integrity requirements (uniqueness, referential constraints, domain rules).
- Change tolerance for future schema evolution.

## Deliverables
- Logical schema definition (tables, columns, PK/FK, constraints).
- Data integrity policy per entity relationship.
- Rationale for nullable vs non-nullable columns.
- Compatibility notes for future evolution.

## Quick Example
- `orders(order_id PK, customer_id FK, status, created_at)`.
- `payments(payment_id PK, order_id FK UNIQUE, state, amount)`.
- Constraint: one active payment record per order if business rule requires 1:1.

## Quality Standard
- Keys and constraints enforce domain invariants directly.
- Nullability decisions are intentional and justified.
- Relationship integrity is enforced with FK or equivalent policy.
- Naming is consistent and semantically clear.

## Workflow
1. Map conceptual entities to logical tables.
2. Define keys, relationships, and integrity constraints.
3. Validate schema against core query/update paths.
4. Review nullability/default semantics for correctness.
5. Publish schema with rationale and open risks.

## Failure Conditions
- Stop when critical invariants are not enforceable by schema rules.
- Stop when table responsibilities overlap ambiguously.
- Escalate when access paths require contradictory integrity choices.
