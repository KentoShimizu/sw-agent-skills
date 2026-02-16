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

## Project-Specific Decision Calibration (Mandatory)
- Use `skills/architecture-principles/references/project-calibration-framework.md` to derive decision criteria from project evidence.
- Derive no-go conditions from current requirements, existing implementation constraints, and user/stakeholder direction collected in this task.
- Do not hardcode universal no-go rules; represent them as falsifiable, project-scoped checks with evidence links.
- Define threshold types before values (for example latency budget, consistency tolerance, recovery objective, ownership capacity, and cost volatility).
- For each threshold, document rationale, measurement method, observation window, and re-decision trigger.
- If evidence is incomplete, record explicit assumptions and decision confidence.

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
- Project-specific no-go checks and threshold choices are traceable to requirements, existing-system evidence, and stakeholder direction.
- Greenfield designs exclude fallback paths; brownfield rollback requires trigger and runbook.

## Failure Handling
- Stop when critical flows exceed platform execution constraints.
- Stop when canonical contract validation fails.
- Stop when no-go checks or threshold values are copied from generic defaults without project evidence.
- Escalate when IAM and secret boundaries are not explicit.
