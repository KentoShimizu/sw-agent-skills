---
name: architecture-ddd
description: "Model bounded contexts, aggregates, and context-map integrations with Domain-Driven Design. Use when domain language, ownership, or consistency boundaries are unclear; do not use for dependency-layer enforcement."
---

# Architecture DDD

## Overview
Use this skill to design domain boundaries that match business reality and team ownership. The output should reduce coupling, language drift, and integration ambiguity.

## Inputs To Gather
- Domain language from business and engineering.
- Process/event flows and invariants.
- Team ownership and release cadence.
- Existing integration pain points.

## Deliverables
- Bounded context map with ownership.
- Aggregate boundaries with invariants.
- Context integration strategy (shared kernel, ACL, published language, etc.).
- Ubiquitous language glossary for ambiguous terms.

## Quality Standard
- Context boundaries align with business capabilities and ownership.
- Aggregate boundaries protect transactional invariants.
- Cross-context integrations have explicit translation ownership.
- Context map choices include tradeoffs and risk notes.

## Workflow
1. Normalize domain language and resolve term conflicts.
2. Define bounded contexts from ownership and invariants.
3. Define aggregate boundaries and consistency rules.
4. Select integration pattern per context relationship.
5. Validate against change history and operational ownership.

## Failure Conditions
- Stop when boundaries are based only on technical layers.
- Stop when invariants are not tied to an aggregate.
- Escalate when ownership remains ambiguous across contexts.
