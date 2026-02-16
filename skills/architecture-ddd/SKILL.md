---
name: architecture-ddd
description: "Domain-driven design workflow for modeling bounded contexts, aggregates, and context maps in complex domains. Trigger when complex domain behavior requires explicit context boundaries and model ownership to avoid cross-team leakage and integration ambiguity; do not use for single-module implementation refactors without architecture impact."
---

# Architecture Ddd

## Trigger Boundary
- Use when domain complexity or terminology conflicts drive design risk.
- Do not use for implementation-layer dependency rules; use `architecture-clean-architecture`.
- Do not use for diagram-only communication; use `architecture-c4-modeling`.

## Goal
Create domain-aligned architecture boundaries with explicit ubiquitous language and ownership.

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
- Model privacy-sensitive concepts explicitly in ubiquitous language.
- Isolate regulated data concerns within bounded contexts.
- Prepare an `ARC-CMP-*` evidence package for governance review.

## Inputs
- Domain events, processes, and terminology sources
- Stakeholder language conflicts and ownership boundaries
- Business invariants and critical consistency rules

## Outputs
- Bounded context map with integration relationships
- Aggregate and entity boundary definitions
- Ubiquitous language glossary and ownership model

## Workflow
1. Discover domain language and conflicting meanings.
2. Define bounded contexts and ownership boundaries.
3. Model aggregates around consistency invariants.
4. Create context map with integration and anti-corruption patterns.
5. Align team boundaries with context ownership.

## Quality Gates
- Bounded contexts have clear ownership and purpose.
- Aggregates enforce explicit invariants.
- `ARC-CMP-*` evidence package is complete and approved.
- Project-specific no-go checks and threshold choices are traceable to requirements, existing-system evidence, and stakeholder direction.
- Greenfield designs exclude fallback paths; brownfield rollback requires trigger and runbook.

## Failure Handling
- Stop when context boundaries are purely technical.
- Stop when canonical contract validation fails.
- Stop when no-go checks or threshold values are copied from generic defaults without project evidence.
- Escalate when invariant ownership is ambiguous across teams.
