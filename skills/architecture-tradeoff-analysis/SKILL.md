---
name: architecture-tradeoff-analysis
description: "Structured architecture option evaluation with explicit criteria, weighting, and sensitivity checks. Trigger when multiple architecture options are still viable and the decision needs transparent scoring, risk weighting, and sensitivity analysis for stakeholder sign-off; do not use after the architecture direction is already fixed."
---

# Architecture Tradeoff Analysis

## Trigger Boundary
- Use when multiple architecture options exist and a defensible choice is required.
- Do not use to document final decision history; use `architecture-decision-records`.
- Do not use to produce communication diagrams only; use `architecture-c4-modeling`.

## Goal
Select architecture options through transparent, evidence-based evaluation.

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
- Include legal and privacy constraints as hard gates, not soft preferences.
- Reject options that require non-compliant data handling assumptions.
- Prepare an `ARC-CMP-*` evidence package for governance review.

## Inputs
- Decision question and candidate options
- Architecture drivers and quality attributes
- Constraints, risks, and cost assumptions

## Outputs
- Option scorecard with criteria and weights
- Sensitivity analysis on uncertain assumptions
- Recommended option with explicit risks and re-decision trigger
- Brownfield only: rollback strategy with trigger condition and runbook link

## Workflow
1. Define decision scope and non-negotiable constraints.
2. Enumerate at least two viable architecture options.
3. Score options against weighted criteria.
4. Perform sensitivity checks on uncertain inputs.
5. For greenfield, define failure exposure criteria and re-decision trigger.
6. For brownfield, add rollback trigger and runbook reference.

## Quality Gates
- Criteria and weights are defined before scoring.
- Options are comparable at equal abstraction level.
- `ARC-CMP-*` evidence package is complete and approved.
- Project-specific no-go checks and threshold choices are traceable to requirements, existing-system evidence, and stakeholder direction.
- Greenfield output does not contain fallback or rollback architecture paths.

## Failure Handling
- Stop when decision criteria are missing or unstable.
- Stop when canonical contract validation fails.
- Stop when no-go checks or threshold values are copied from generic defaults without project evidence.
- Escalate when top options are statistically indistinguishable under sensitivity checks.
