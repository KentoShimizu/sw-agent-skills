---
name: sqlalchemy-orm-patterns
description: "SQLAlchemy ORM design workflow. Trigger when SQLAlchemy model mappings, relationship loading strategy, query composition, or session/transaction behavior must be implemented or revised with ORM-specific decisions in scope; do not use for repository-wide architecture governance or release management policy."
---

# Sqlalchemy Orm Patterns

## Trigger Boundary
- Use when Python services rely on SQLAlchemy ORM/core patterns.
- Do not use for database-agnostic conceptual modeling only.
- Do not use for migration tooling policy without ORM context.

## Goal
Build clear ORM mappings and query patterns with controlled transaction and session behavior.

## Inputs
- Domain entities and relationship constraints
- Session lifecycle and transaction requirements
- Query performance and consistency expectations

## Outputs
- ORM model and relationship design
- Session and transaction boundary policy
- Query optimization and loading-strategy checklist

## Workflow
1. Define model mappings with explicit constraints and indexes.
2. Choose loading strategy (`joinedload`, `selectinload`, etc.) by access pattern.
3. Scope sessions per request/unit-of-work to avoid leaks.
4. Guard transaction boundaries with explicit rollback semantics.
5. Validate generated SQL and performance on hot queries.

## Quality Gates
- Session lifecycle is explicit and leak-free.
- Transactions are atomic for business-critical operations.
- Query strategy avoids avoidable N+1 and overfetching.
- Model constraints align with database integrity rules.

## Failure Handling
- Stop when session ownership is ambiguous across layers.
- Escalate when ORM abstractions hide critical SQL behavior.
