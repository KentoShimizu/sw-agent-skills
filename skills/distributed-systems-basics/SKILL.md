---
name: distributed-systems-basics
description: "Analyze distributed-system design using failure modes, consistency models, and reliability primitives across networked components. Use when correctness depends on partitions, retries, timeouts, ordering, or partial failures; do not use for single-process implementation details only."
---

# Distributed Systems Basics

## Overview
Use this skill to reason about correctness and reliability when components communicate over unreliable networks.

## Inputs To Gather
- Component boundaries and communication patterns.
- Consistency and ordering requirements per workflow.
- Failure scenarios (partition, timeout, duplicate, out-of-order, stale read).
- Recovery and observability capabilities.

## Deliverables
- Failure-mode map and risk ranking.
- Consistency decision record per critical flow.
- Reliability mechanism selection (retry, idempotency, backoff, timeout).
- Validation plan (fault injection and invariant checks).

## Quick Example
- Workflow: payment status sync between services.
- Risks: duplicate messages + out-of-order delivery.
- Controls: idempotency key, monotonic version check, retry with backoff, DLQ.

## Quality Standard
- Critical flows have explicit consistency and ordering rules.
- Retry/timeout semantics are bounded and intentional.
- Idempotency strategy exists where at-least-once delivery is possible.
- Failure handling is observable and testable.

## Workflow
1. Enumerate critical distributed workflows.
2. Model failure and timing assumptions.
3. Choose consistency/reliability primitives per flow.
4. Define observability and recovery behavior.
5. Validate assumptions with targeted failure tests.

## Failure Conditions
- Stop when consistency assumptions are implicit or contradictory.
- Stop when retries/timeouts can amplify failure unboundedly.
- Escalate when critical failure modes have no mitigation path.
