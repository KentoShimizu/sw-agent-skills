---
name: architecture-event-driven
description: "Event-driven architecture workflow for asynchronous integration, decoupled workflows, and failure-tolerant event propagation. Use when temporal decoupling and independent evolution are required; do not use when strict synchronous consistency is mandatory across all steps."
---

# Architecture Event Driven

## Overview
Use this skill to design event-driven systems that remain correct under retries, delays, and partial failures.

## Scope Boundaries
- Workflows span multiple bounded contexts or services asynchronously.
- Temporal decoupling is needed to improve autonomy or resilience.
- Integration churn is high and direct RPC coupling causes fragility.

## Core Judgments
- Event semantics: fact versus command and ownership of meaning.
- Delivery guarantees: at-most-once, at-least-once, effectively-once patterns.
- Ordering strategy: global ordering, per-key ordering, or order independence.
- Recovery model: replay, dead-letter, compensating actions, and backfill.

## Practitioner Heuristics
- Publish events as immutable domain facts from the source of truth.
- Never rely on "exactly-once" assumptions; design idempotent consumers.
- Partition keys must align with business consistency boundaries.
- Version event contracts with additive evolution first; reserve breaking changes for controlled migrations.

## Workflow
1. Define domain events and ownership boundaries.
2. Specify producer guarantees and consumer idempotency requirements.
3. Choose ordering and partitioning strategies by business invariant.
4. Design failure-handling paths for retry storms, poison messages, and replay.
5. Align observability with event lifecycle (published, consumed, failed, compensated).
6. Document contract evolution and deprecation strategy.

## Common Failure Modes
- Events used as remote procedure calls in disguise.
- Shared event schema controlled by consumers instead of producers.
- Unbounded retry loops causing downstream saturation.

## Failure Conditions
- Stop when event ownership or semantics are ambiguous.
- Stop when consumer correctness depends on fragile global ordering.
- Escalate when replay/compensation behavior is undefined for critical flows.
