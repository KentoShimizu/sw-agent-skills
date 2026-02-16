---
name: architecture-event-driven
description: "Design event-driven architecture with explicit delivery, ordering, schema evolution, and failure-handling guarantees. Use when asynchronous workflows are core and correctness depends on messaging semantics."
---

# Architecture Event Driven

## Overview
Use this skill to design reliable asynchronous systems where events are first-class contracts. The output must be implementable and operable under failure.

## Inputs To Gather
- Event candidates and domain ownership.
- Throughput, latency, and ordering requirements.
- Consistency and compensation expectations.
- Recovery/compliance constraints.

## Deliverables
- Event catalog with schema and owner.
- Delivery semantics and ordering policy.
- Retry, DLQ, replay, and idempotency strategy.
- Schema evolution and compatibility policy.

## Quality Standard
- Event ownership and lifecycle are explicit.
- Delivery semantics are chosen intentionally per flow.
- Idempotency and dedupe strategy are testable.
- Retry and DLQ handling include operational ownership.
- Compatibility policy supports safe producer/consumer evolution.

## Workflow
1. Identify events and ownership boundaries.
2. Define schema contracts and evolution policy.
3. Define delivery, ordering, and idempotency guarantees.
4. Define retry, DLQ, and replay operations.
5. Validate consistency gaps and compensation design.

## Failure Conditions
- Stop when event ownership is undefined.
- Stop when consistency expectations are implicit.
- Escalate when compensation cannot bound business risk.
