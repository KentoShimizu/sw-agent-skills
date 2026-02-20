---
name: technical-roadmapping
description: "Technical roadmap workflow for sequencing initiatives, dependencies, and risk-aware milestones. Use when teams must decide what technical work to do first across multiple increments; do not use for low-level code implementation details."
---

# Technical Roadmapping

## Overview
Use this skill to produce realistic technical roadmaps that make sequencing, risk, and ownership explicit.

## Scope Boundaries
- Multiple initiatives compete for the same engineering capacity.
- Dependency ordering and milestone timing determine delivery feasibility.
- Teams need a defensible plan across quarters or release trains.

## Templates And Assets
- Milestone template:
  - `assets/roadmap-milestone-template.md`
- Dependency and risk register:
  - `assets/dependency-risk-register-template.md`

## Inputs To Gather
- Initiative goals, outcome metrics, and non-negotiable deadlines.
- Dependency graph (technical, organizational, vendor, compliance).
- Capacity assumptions, staffing constraints, and environment readiness.
- Risk tolerance and escalation policy.

## Deliverables
- Sequenced roadmap with milestones, owners, and decision checkpoints.
- Dependency map and critical-path analysis.
- Risk register with mitigation actions and trigger-based contingency plans.

## Workflow
1. Define desired outcomes and constraints for each initiative.
2. Map dependencies and identify the critical path.
3. Evaluate at least two sequencing options with trade-offs (risk, value timing, coordination cost).
4. Select a roadmap option and document rationale and rejected alternatives.
5. Assign milestone entry/exit criteria and measurable progress signals.
6. Add contingency actions for high-impact dependency or staffing failures.
7. Publish roadmap with review cadence and explicit replan triggers.

## Quality Standard
- Sequence is justified by dependencies, not only stakeholder preference.
- Milestones have objective entry/exit criteria.
- Risks are tied to owners, deadlines, and mitigation plans.
- The roadmap can be revised predictably when assumptions change.

## Failure Conditions
- Stop when critical dependencies are unknown or unowned.
- Stop when milestones lack measurable completion criteria.
- Escalate when required outcomes exceed feasible capacity under current constraints.
