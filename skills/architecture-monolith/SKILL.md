---
name: architecture-monolith
description: "Modular monolith architecture design for systems that prioritize transactional consistency, operational simplicity, and fast team iteration in a single deployable unit. Trigger when architecture direction is undecided and teams must decide whether domain boundaries, dependency rules, and scaling constraints can be handled safely inside one deployable; do not use for single-module implementation refactors without architecture impact."
---

# Architecture Monolith

## Trigger Boundary
- Use when one deployable unit is acceptable and operational simplicity is prioritized.
- Do not use when independent scaling or deployment by domain is mandatory; use `architecture-microservices`.
- Do not use for async integration-first topology; use `architecture-event-driven`.

## Goal
Design a modular monolith with clear internal boundaries and low coupling.

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
- Isolate sensitive data handling modules and enforce least privilege.
- Centralize audit logging and retention controls for regulated data.
- Prepare an `ARC-CMP-*` evidence package for governance review.

## Inputs
- Domain boundaries and transactional requirements
- Team size and release cadence
- Performance, reliability, and compliance constraints

## Outputs
- Module boundary map and dependency rules
- Internal contract definitions and ownership map
- Evolution seams for future extraction if needed

## Workflow
1. Partition domains into high-cohesion modules.
2. Define strict dependency direction across modules.
3. Establish module-level API contracts and ownership.
4. Design transactional boundaries and failure behavior.
5. Identify extraction seams and record migration risks.

## Quality Gates
- Module boundaries align with domain responsibilities.
- Cross-module dependencies follow explicit rules.
- `ARC-CMP-*` evidence package is complete and approved.
- Project-specific no-go checks and threshold choices are traceable to requirements, existing-system evidence, and stakeholder direction.
- Greenfield designs exclude fallback paths; brownfield rollback requires trigger and runbook.

## Failure Handling
- Rework when cyclic dependencies appear between modules.
- Stop when canonical contract validation fails.
- Stop when no-go checks or threshold values are copied from generic defaults without project evidence.
- Escalate when module ownership cannot be assigned clearly.
