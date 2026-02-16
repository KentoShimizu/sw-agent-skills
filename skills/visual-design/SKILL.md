---
name: visual-design
description: "Visual design workflow for defining color, typography, spacing, and compositional language aligned with product and brand goals. Trigger when an experience needs concrete visual direction and teams must decide color/typography/layout language and brand expression before implementation; do not use for backend data-model or deployment pipeline decisions."
---

# Visual Design

## Trigger Boundary
- Use when visual hierarchy, consistency, or brand alignment is unclear.
- Do not use for interaction flow state logic; use `interaction-design`.
- Do not use for accessibility audit execution only; use `accessibility-design`.

## Goal
Deliver coherent visual language that improves clarity and trust.

## Project Rule Policy
- Follow existing repository or organization rules first for IDs, approvers, quality gates, locale scope, and privacy handling.
- If no existing rule is available, define a lightweight project default and mark it as provisional.
- Treat example IDs in this skill as non-binding guidance.
- Skip manifest validation for documentation-only deliverables unless the project explicitly requests governed validation.

## Inputs
- Brand direction and product context
- Existing UI artifacts and inconsistency reports
- Accessibility contrast and readability constraints

## Outputs
- Visual spec set with project-defined IDs (example: `VIS-SPEC-*` when no existing policy is available)
- Typography, color, spacing, and hierarchy rules
- Component-level visual usage guidance

## Workflow
1. Define visual hierarchy objectives by task criticality.
2. Build typography and spacing scales.
3. Define color role system and usage constraints.
4. Apply rules to representative screens.
5. Validate readability and contrast compliance.

6. Compare at least two feasible approaches and explain why one is preferred.
7. Record key assumptions, unknowns, confidence, and rollback considerations.

## Quality Gates
- Visual hierarchy supports task prioritization.
- Spec set is consistent and reusable.
- Contrast and legibility pass required thresholds.
- Visual decisions map to principle and token systems.

- Decision rationale and trade-offs are explicit.
- Assumptions, unknowns, and confidence are explicitly documented.

## Failure Handling
- Stop when visual rules rely on one-off overrides.
- Escalate when contrast or readability fails baseline gates.
