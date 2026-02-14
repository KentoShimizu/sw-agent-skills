---
name: architecture-event-driven
description: "Event-driven architecture design for asynchronous workflows, decoupled integration, and scalable domain event propagation. Use when system boundaries, module relationships, and architecture-level constraints are being defined; do not use for single-module implementation refactors without architecture impact."
---

# Architecture Event Driven

## Trigger Boundary
- Use when asynchronous integration and loose coupling are required.
- Do not use for request-response dominant topology design; use `architecture-microservices` or `architecture-monolith`.
- Do not use to document final decision history; use `architecture-decision-records`.

## Goal
Define event model, schema governance, and runtime guarantees for asynchronous systems.

## Shared Architecture Contract (Canonical)
- Use `skills/architecture-principles/references/architecture-governance-contract.md` as the only schema source.
- Validate all IDs, lifecycle states, and gate rules against the canonical contract.
- Do not define local ID formats or alternate state machines.

## Compliance & Governance Baseline (US, Japan, EU)
- Classify event payload sensitivity and minimize personal data fields.
- Enforce retention and replay policy under jurisdictional constraints.
- Prepare an `ARC-CMP-*` evidence package for governance review.

## Inputs
- Domain events and producer/consumer candidates
- Latency and durability requirements
- Ordering, duplication, and consistency constraints

## Outputs
- Event catalog with schema ownership and versioning rules
- Delivery semantics and retry/dead-letter policy
- Consistency and compensating-action strategy

## Workflow
1. Identify domain events and bounded payload contracts.
2. Define event schema lifecycle and compatibility policy.
3. Specify delivery guarantees and idempotency requirements.
4. Design dead-letter handling and replay procedures.
5. Record eventual consistency behavior and compensations.

## Quality Gates
- Every event has owner, schema, and versioning policy.
- Consumers can handle duplicates and out-of-order messages.
- `ARC-CMP-*` evidence package is complete and approved.
- Greenfield designs exclude fallback paths; brownfield rollback requires trigger and runbook.

## Failure Handling
- Stop when event ownership or schema governance is undefined.
- Stop when canonical contract validation fails.
- Escalate when consistency gaps cannot be compensated safely.
