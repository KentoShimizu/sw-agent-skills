---
name: figma-handoff
description: "Design-to-engineering handoff workflow for packaging implementation-ready Figma specifications, assets, and acceptance criteria. Trigger when approved Figma designs must be translated into engineering-ready handoff materials (specs, assets, states, acceptance criteria) before implementation starts; do not use for backend data-model or deployment pipeline decisions."
---

# Figma Handoff

## Trigger Boundary
- Use when design outputs must be converted into engineering-ready handoff artifacts.
- Do not use for defining new principles or token architecture; use `design-principles` or `design-tokens`.
- Do not use for exploratory research synthesis; use `ux-research-synthesis`.

## Goal
Deliver unambiguous handoff artifacts that reduce implementation drift.

## Project Rule Policy
- Follow existing repository or organization rules first for IDs, approvers, quality gates, locale scope, and privacy handling.
- If no existing rule is available, define a lightweight project default and mark it as provisional.
- Treat example IDs in this skill as non-binding guidance.
- Skip manifest validation for documentation-only deliverables unless the project explicitly requests governed validation.
- Use `references/engineering-judgment-defaults.md` for default decision scoring, risk gating, uncertainty handling, and output structure.

## Inputs
- Finalized Figma frames, components, and variants
- Token and interaction specifications
- Accessibility and localization constraints

## Outputs
- Handoff package with project-defined ID (example: `FIG-HND-*` when no existing policy is available)
- Asset inventory and spec mapping
- Acceptance checklist for engineering verification
- Privacy evidence package when policy requires it

## Workflow
1. Confirm design artifacts are final and versioned.
2. Export required assets with naming and usage rules.
3. Map tokens, states, and interactions to implementation notes.
4. Add accessibility and localization checkpoints.
5. Publish handoff package with owner, review status, and privacy evidence.

## Quality Gates
- Handoff includes all required assets and spec references.
- States and variants are fully documented.
- Accessibility and localization checks are explicit.
- Policy-required approvers and privacy controls are explicitly recorded.
- Engineering owner confirms implementability.

## Engineering Judgment Application
1. Generate at least two plausible options before recommending one.
2. Evaluate options using project-defined criteria; if missing, use defaults in `references/engineering-judgment-defaults.md`.
3. Record assumptions, unknowns, confidence, and key trade-offs in the final output.

## Failure Handling
- Stop when source designs are not version-locked.
- Stop when policy-required approvers are missing.
- Escalate when critical specs or assets are missing.
