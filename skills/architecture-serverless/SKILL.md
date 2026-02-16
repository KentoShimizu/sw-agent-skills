---
name: architecture-serverless
description: "Design serverless architectures with explicit workload fit, execution limits, security boundaries, and cost controls. Use when workloads are event-driven or bursty and managed-service leverage is a core goal."
---

# Architecture Serverless

## Overview
Use this skill to design serverless systems that are cost-aware, secure, and operable under platform constraints. The output must include concrete execution and observability policies.

## Inputs To Gather
- Workload profile (traffic, duration, concurrency).
- Latency SLO and cold-start tolerance.
- Platform quotas, regional constraints, runtime limits.
- Cost constraints and operational ownership model.

## Deliverables
- Serverless fit assessment by critical flow.
- Function/event/data boundary design.
- Execution policies (timeout, concurrency, retry, idempotency).
- Security, observability, and cost control guardrails.

## Quality Standard
- Fit rationale is explicit for each critical flow.
- Execution policies are defined per path and testable.
- IAM and secret/data boundaries follow least privilege.
- Quota and cost risk controls are operationally actionable.
- Cold-start strategy is explicit for latency-sensitive paths.

## Workflow
1. Evaluate serverless fit by workload and SLO.
2. Define function and managed-service boundaries.
3. Define execution policies and failure handling.
4. Define security and data protection boundaries.
5. Define observability and cost controls for production.

## Failure Conditions
- Stop when critical flows violate platform constraints.
- Stop when quota or cold-start risk is unbounded.
- Escalate when serverless is forced despite weak fit evidence.
