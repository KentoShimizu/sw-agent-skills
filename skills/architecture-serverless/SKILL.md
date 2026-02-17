---
name: architecture-serverless
description: "Serverless architecture workflow for event-driven and bursty workloads using managed compute and platform services. Use when elasticity and reduced platform operations justify managed-service constraints; do not use when workload shape requires long-lived stateful control loops."
---

# Architecture Serverless

## Overview
Use this skill to design serverless systems that are cost-aware, failure-tolerant, and operationally predictable.

## Scope Boundaries
- Traffic is variable or bursty and elastic scaling is valuable.
- Team capacity for infrastructure operations is limited.
- Workloads are naturally event-driven or request/response with bounded execution.

## Core Judgments
- Compute model: function granularity, execution time bounds, and concurrency profile.
- State model: where session/process state lives outside function runtime.
- Integration model: event source guarantees, retry semantics, and idempotency.
- Cost model: invocation frequency, cold-start impact, data transfer/storage economics.

## Practitioner Heuristics
- Keep functions narrow by business action, not by tiny technical helpers.
- Externalize state deliberately (DB/cache/object store) and design for retries.
- Control concurrency at event source and downstream dependency limits.
- Treat timeouts as business behavior decisions, not only platform defaults.

## Workflow
1. Profile workload shape and latency/cost sensitivity.
2. Design event and request paths with explicit idempotency rules.
3. Choose managed services for state, orchestration, and messaging.
4. Define concurrency limits and backpressure behavior.
5. Model cost and failure behavior under peak and degraded conditions.
6. Record escape hatches for workloads that outgrow serverless constraints.

## Common Failure Modes
- Hidden coupling through shared environment variables and broad IAM policies.
- Unbounded retries causing duplicate side effects.
- Cost surprises from chatty event chains and storage/egress growth.

## Failure Conditions
- Stop when critical workflows cannot tolerate at-least-once delivery semantics.
- Stop when latency SLOs are incompatible with runtime startup behavior.
- Escalate when concurrency or cost risk cannot be bounded.
