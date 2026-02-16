---
name: architecture-c4-modeling
description: "C4 architecture modeling workflow for producing context, container, and component views that communicate system structure consistently. Trigger when teams need explicit boundary and dependency views to align architecture decisions before implementation, review, or handoff; do not use for single-module implementation refactors without architecture impact."
---

# Architecture C4 Modeling

## Trigger Boundary
- Use when architecture communication artifacts are missing or outdated.
- Do not use to decide architecture options; use `architecture-tradeoff-analysis`.
- Do not use as decision history storage; use `architecture-decision-records`.

## Goal
Produce accurate and traceable C4 views that align stakeholders on architecture.

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
- Mark sensitive data flows and regulated boundaries in relevant diagrams.
- Avoid exposing credentials or internal secrets in architecture artifacts.
- Prepare an `ARC-CMP-*` evidence package for governance review.

## Inputs
- Current architecture and dependency information
- Target audience and required abstraction level
- Related ADRs and risks

## Outputs
- Updated C4 context, container, and component views
- Relationship legend and assumptions list
- Traceability links to ADRs and key risks

## Workflow
1. Build context view with external actors and systems.
2. Build container view with runtime responsibilities.
3. Build component view for high-complexity containers.
4. Link diagrams to ADR and risk identifiers.
5. Validate naming and relationship consistency.

## Quality Gates
- Diagram scope matches intended audience.
- Names and relationships are consistent across views.
- `ARC-CMP-*` evidence package is complete and approved.
- Project-specific no-go checks and threshold choices are traceable to requirements, existing-system evidence, and stakeholder direction.
- Greenfield designs exclude fallback paths; brownfield rollback requires trigger and runbook.

## Failure Handling
- Stop when source architecture information is stale or conflicting.
- Stop when canonical contract validation fails.
- Stop when no-go checks or threshold values are copied from generic defaults without project evidence.
- Escalate when critical boundaries cannot be represented clearly.
