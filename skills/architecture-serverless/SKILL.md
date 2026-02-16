---
name: architecture-serverless
description: "Serverless architecture design for event-driven and bursty workloads using managed services and function execution. Trigger when architecture decisions must weigh serverless fit (event model, latency/cold-start tolerance, operational ownership, and cost variability) before implementation; do not use for single-module implementation refactors without architecture impact."
---

# Architecture Serverless

## Trigger Boundary
- Use when operational offloading and elastic scaling are primary goals.
- Do not use for long-lived stateful service topology; use `architecture-monolith` or `architecture-microservices`.
- Do not use for domain boundary modeling alone; use `architecture-ddd`.

## Goal
Design a production-safe serverless architecture with clear boundaries and constraints.

## Shared Architecture Contract (Canonical)
- Use `skills/architecture-principles/references/architecture-governance-contract.md` as the only schema source.
- Validate all IDs, lifecycle states, and gate rules against the canonical contract.
- Do not define local ID formats or alternate state machines.

## Compliance & Governance Baseline (US, Japan, EU)
- Enforce least privilege IAM for function and managed-service access.
- Define residency, encryption, and cross-border transfer constraints.
- Prepare an `ARC-CMP-*` evidence package for compliance sign-off.

## Inputs
- Workload profile and traffic variability
- Latency and execution-time constraints
- Cloud platform service constraints and quota limits

## Outputs
- Function and managed-service boundary map
- Cold-start, concurrency, and timeout budget strategy
- Security, observability, and cost-control guardrails

## Workflow
1. Partition workloads into event handlers with clear boundaries.
2. Externalize durable state and define consistency model.
3. Set concurrency, timeout, and retry policies by workload.
4. Define IAM boundaries and secret handling paths.
5. Add observability and cost controls for production operation.

## Quality Gates
- Function boundaries align with domain use cases.
- Timeouts and retries are explicit and workload-appropriate.
- `ARC-CMP-*` evidence package is complete and approved.
- Greenfield designs exclude fallback paths; brownfield rollback requires trigger and runbook.

## Failure Handling
- Stop when critical flows exceed platform execution constraints.
- Stop when canonical contract validation fails.
- Escalate when IAM and secret boundaries are not explicit.
