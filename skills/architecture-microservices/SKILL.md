---
name: architecture-microservices
description: "Microservices architecture design for independent deployability, team autonomy, and domain-level scaling. Trigger when service boundaries, ownership, and inter-service integration risks must be resolved to decide whether a microservices direction is viable; do not use for single-module implementation refactors without architecture impact."
---

# Architecture Microservices

## Trigger Boundary
- Use when independent deployment and scaling by domain are explicit goals.
- Do not use for single-deploy modular systems; use `architecture-monolith`.
- Do not use solely to evaluate options; use `architecture-tradeoff-analysis` first when undecided.

## Goal
Define robust service boundaries, contracts, and operational controls for microservices.

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
- Define data ownership and residency per service boundary.
- Enforce service-to-service authentication, authorization, and audit trails.
- Prepare a project-defined compliance evidence package ID (for example `ARC-CMP-*`) for compliance sign-off.

## Inputs
- Domain decomposition and team ownership model
- Scalability and availability targets
- Integration patterns and compliance constraints

## Outputs
- Service boundary map with ownership and dependencies
- API and event contract strategy
- Resilience and observability requirements per service

## Workflow
1. Derive service boundaries from domain and team topology.
2. Assign ownership and lifecycle responsibility per service.
3. Define synchronous and asynchronous contracts explicitly.
4. Specify reliability patterns: retries, timeouts, and circuit breaking.
5. Record consistency model and data ownership per boundary.

## Quality Gates
- No ambiguous ownership between services.
- Inter-service contracts are versioned and reviewable.
- project-defined compliance evidence package ID (for example `ARC-CMP-*`) is complete and approved.
- Project-specific no-go checks and threshold choices are traceable to requirements, existing-system evidence, and stakeholder direction.
- Greenfield designs exclude fallback paths; brownfield rollback requires trigger and runbook.

## Failure Handling
- Stop when boundaries are split by technical layers instead of domains.
- Stop when canonical contract validation fails.
- Stop when no-go checks or threshold values are copied from generic defaults without project evidence.
- Escalate when critical services lack clear resilience strategy.
