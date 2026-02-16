---
name: architecture-tradeoff-analysis
description: "Compare viable architecture options using explicit criteria, evidence, and risk weighting. Use when multiple options are still on the table and a transparent decision is required; do not use after direction is fixed."
---

# Architecture Tradeoff Analysis

## Overview
Use this skill to produce a defensible architecture decision from competing options. The result should make decision logic auditable and reusable for future re-evaluation.

## Inputs To Gather
- Decision question and deadline.
- Option set at the same abstraction level.
- Hard constraints that cannot be violated.
- Quality targets and operational constraints.
- Known uncertainties and assumptions.

## Deliverables
- Option scorecard (criteria, weights, evidence, assumptions).
- Sensitivity analysis for uncertain assumptions.
- Recommendation with residual risk and owner.
- Re-decision triggers.

## Quality Standard
- Constraint filtering happens before scoring.
- Scoring criteria are defined before evaluating options.
- Every score links to evidence.
- Sensitivity analysis is present for high-uncertainty inputs.
- The recommendation includes operational consequences and reversibility.

## Workflow
1. Freeze scope, options, and non-negotiable constraints.
2. Define criteria and weights from quality priorities.
3. Score each option with explicit evidence and assumptions.
4. Run sensitivity checks and identify fragile outcomes.
5. Recommend one option and document residual risk.

## Failure Conditions
- Stop when criteria or weights are unstable.
- Stop when options are not comparable.
- Escalate when top options remain tied after sensitivity analysis.
