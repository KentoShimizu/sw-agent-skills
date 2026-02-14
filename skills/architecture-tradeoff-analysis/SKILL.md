---
name: architecture-tradeoff-analysis
description: "Structured architecture option evaluation with explicit criteria, weighting, and sensitivity checks. Use when evaluating competing architecture options with explicit criteria and risk weighting; do not use after the architecture direction is already fixed."
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
- Greenfield output does not contain fallback or rollback architecture paths.

## Failure Handling
- Stop when decision criteria are missing or unstable.
- Stop when canonical contract validation fails.
- Escalate when top options are statistically indistinguishable under sensitivity checks.
