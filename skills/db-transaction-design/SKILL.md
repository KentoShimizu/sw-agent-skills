---
name: db-transaction-design
description: "Design transaction boundaries, isolation levels, and contention controls to preserve consistency under concurrent workloads. Use when correctness depends on atomic multi-step updates or race prevention; do not use for query-only micro-optimizations."
---

# DB Transaction Design

## Overview
Use this skill to define transaction behavior that protects business invariants while meeting throughput and latency needs.

## Inputs To Gather
- Business invariants and atomicity requirements.
- Read/write concurrency profile and conflict hotspots.
- Acceptable anomalies and consistency model constraints.
- Retry, timeout, and idempotency behavior at application boundaries.

## Deliverables
- Transaction boundary definition per critical workflow.
- Isolation-level decisions with anomaly rationale.
- Locking/contention strategy and deadlock handling policy.
- Verification scenarios for race and anomaly prevention.

## Quick Example
- Workflow: decrement inventory + create reservation.
- Requirement: no oversell under concurrent checkout.
- Design: single transaction with row-level lock or optimistic version check + bounded retry.

## Quality Standard
- Invariants are explicitly mapped to transaction boundaries.
- Isolation choice is justified by prevented anomalies.
- Retry/idempotency strategy is consistent with transaction semantics.
- Contention impact is measured and bounded.

## Workflow
1. Identify workflows requiring atomic guarantees.
2. Select isolation and locking model per workflow.
3. Define timeout/retry/idempotency behavior.
4. Validate with concurrent race and failure tests.
5. Publish operational signals for lock contention/deadlocks.

## Failure Conditions
- Stop when invariants rely on non-atomic multi-step updates.
- Stop when isolation choice permits unacceptable anomalies.
- Escalate when contention makes throughput targets unattainable.
