---
name: requirement-prioritization
description: "Requirement prioritization workflow for dependency-aware ranking and release cut-line decisions. Use when finalized requirement baselines need ordering under value, risk, and capacity constraints; do not use for requirement discovery."
---

# Requirement Prioritization

## Overview
Use this skill to produce reproducible priority decisions that are executable under real dependency and capacity constraints.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- Dependency-aware ranking rules:
  - `references/dependency-aware-ranking-rules.md`

## Templates And Assets
- Prioritization scorecard template:
  - `assets/prioritization-scorecard-template.csv`

## Inputs To Gather
- Approved requirement baseline.
- Effort/dependency estimates and capacity limits.
- Risk/compliance constraints.
- Release timeline assumptions.

## Deliverables
- Ranked requirement backlog with rationale.
- Release cut-line and deferred set.
- Dependency-feasible execution sequence.

## Workflow
1. Set ranking dimensions and weights.
2. Score requirements with `assets/prioritization-scorecard-template.csv`.
3. Apply dependency and mandatory-item rules via `references/dependency-aware-ranking-rules.md`.
4. Validate resulting sequence against capacity.
5. Publish ranking decision and deferral triggers.

## Quality Standard
- Ranking is reproducible from documented rules.
- Sequence is dependency-feasible.
- Mandatory constraints are never silently deprioritized.

## Failure Conditions
- Stop when ranking ignores required dependencies.
- Stop when mandatory compliance/security items are deferred without escalation.
- Escalate when capacity assumptions invalidate priority outcomes.
