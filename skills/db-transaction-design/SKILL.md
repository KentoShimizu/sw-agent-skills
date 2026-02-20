---
name: db-transaction-design
description: "Transaction design workflow for boundary definition, isolation-level choice, and contention control under real workload behavior. Use when correctness depends on concurrent read/write semantics; do not use for schema-only tasks that do not affect transaction behavior."
---

# DB Transaction Design

## Overview
Use this skill to design transaction behavior that protects invariants while avoiding avoidable contention and deadlocks.

## Scope Boundaries
- Concurrent workflows must preserve business invariants.
- Anomalies (lost update, write skew, phantom) are possible.
- Lock contention or deadlocks are degrading reliability.

## Core Judgments
- Transaction boundary: what must be atomic versus eventually consistent.
- Isolation level per workflow and anomaly tolerance.
- Locking strategy: optimistic, pessimistic, or hybrid.
- Retry/idempotency behavior under deadlock/timeouts.

## Practitioner Heuristics
- Keep transactions as short as possible while preserving invariants.
- Choose isolation by anomaly risk, not blanket highest level.
- Model retries as business behavior with idempotent operations.
- External network calls inside DB transactions are a major anti-pattern.

## Workflow
1. Identify critical invariants and concurrent access patterns.
2. Define transaction boundaries per use case.
3. Map anomaly risks and select isolation/locking strategy.
4. Design timeout, retry, and deadlock-handling behavior.
5. Evaluate contention hotspots and redesign access ordering if needed.
6. Record assumptions and triggers for revisiting transaction policy.

## Common Failure Modes
- Broad transaction scopes serialize unrelated work.
- Retry logic replays side effects without idempotency guard.
- Isolation is changed to fix symptoms without invariant analysis.

## Failure Conditions
- Stop when invariants cannot be mapped to transaction boundaries.
- Stop when retry behavior can duplicate irreversible side effects.
- Escalate when contention cannot be controlled without workflow redesign.
