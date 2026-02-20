---
name: architecture-ddd
description: "Domain-driven design workflow for bounded context partitioning, aggregate design, and context mapping in complex domains. Use when domain complexity or organizational scaling requires explicit model boundaries; do not use for small CRUD domains without competing language models."
---

# Architecture DDD

## Overview
Use this skill to model complex domains so teams can evolve behavior without constant cross-team coupling.

## Scope Boundaries
- Domain language differs across teams or subsystems.
- Invariants are hard to maintain because boundaries are unclear.
- A single model is causing conflicting meanings and high coordination cost.

## Core Judgments
- Bounded context cuts: where language and invariants legitimately diverge.
- Aggregate boundaries: where consistency must be immediate versus eventual.
- Context integration style: ACL, conformist, published language, or shared kernel.
- Ownership model: which team can change which part without global coordination.

## Practitioner Heuristics
- Bound contexts by change patterns and invariants, not by database tables.
- Aggregates should protect invariants with minimal transactional scope.
- Cross-context communication should exchange explicit contracts, not internal models.
- In dynamic languages, model entities/value objects with explicit typed schemas instead of broad maps that require repetitive casting.

## Workflow
1. Build ubiquitous language per domain area and identify conflicting terms.
2. Partition bounded contexts by invariants, autonomy, and change cadence.
3. Design aggregates with clear consistency and lifecycle rules.
4. Define context map and integration contracts between contexts.
5. Identify anti-corruption needs and translation responsibilities.
6. Document residual ambiguity and model evolution triggers.

## Common Failure Modes
- "DDD" applied as folder naming without boundary behavior changes.
- Aggregates oversized, causing lock contention and slow writes.
- Shared database schema used as de facto integration API.

## Failure Conditions
- Stop when bounded contexts cannot be separated by language/invariant boundaries.
- Stop when aggregate consistency needs conflict with transaction feasibility.
- Escalate when cross-context contracts remain uncontrolled.
