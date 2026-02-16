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

## Shared Design Contract (Canonical)
- Use `../design-principles/references/design-governance-contract.md` as the single schema and gate source.
- Track handoff packages with `FIG-HND-*` IDs.
- Run machine validation: `python3 ../design-principles/scripts/validate_design_contract.py --manifest <path/to/manifest.json>`.

## Inputs
- Finalized Figma frames, components, and variants
- Token and interaction specifications
- Accessibility and localization constraints

## Outputs
- `FIG-HND-*` handoff package
- Asset inventory and spec mapping
- Acceptance checklist for engineering verification
- Privacy evidence package for handoff artifacts

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
- Privacy Reviewer approval is always present.
- Engineering owner confirms implementability.

## Failure Handling
- Stop when source designs are not version-locked.
- Stop when Privacy Reviewer approval is missing.
- Escalate when critical specs or assets are missing.
