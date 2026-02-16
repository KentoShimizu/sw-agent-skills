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

## Shared Design Contract (Canonical)
- Use `../design-principles/references/design-governance-contract.md` as the single schema and gate source.
- Track visual specs with `VIS-SPEC-*` IDs.
- Run machine validation: `python3 ../design-principles/scripts/validate_design_contract.py --manifest <path/to/manifest.json>`.

## Inputs
- Brand direction and product context
- Existing UI artifacts and inconsistency reports
- Accessibility contrast and readability constraints

## Outputs
- Visual spec set with `VIS-SPEC-*` IDs
- Typography, color, spacing, and hierarchy rules
- Component-level visual usage guidance

## Workflow
1. Define visual hierarchy objectives by task criticality.
2. Build typography and spacing scales.
3. Define color role system and usage constraints.
4. Apply rules to representative screens.
5. Validate readability and contrast compliance.

## Quality Gates
- Visual hierarchy supports task prioritization.
- Spec set is consistent and reusable.
- Contrast and legibility pass required thresholds.
- Visual decisions map to principle and token systems.

## Failure Handling
- Stop when visual rules rely on one-off overrides.
- Escalate when contrast or readability fails baseline gates.
