---
name: information-architecture
description: "Information architecture workflow for structuring navigation, content hierarchy, and labeling across product surfaces. Trigger when product content/navigation structure is unclear and teams need explicit hierarchy, taxonomy, and labeling decisions before screen-level design; do not use for backend data-model or deployment pipeline decisions."
---

# Information Architecture

## Trigger Boundary
- Use when users cannot find content or navigation structure is inconsistent.
- Do not use for flow-level state behavior; use `interaction-design`.
- Do not use for design system token decisions; use `design-tokens`.

## Goal
Create clear, scalable, and discoverable information structures.

## Shared Design Contract (Canonical)
- Use `../design-principles/references/design-governance-contract.md` as the single schema and gate source.
- Track structures with `IA-NAV-*` IDs.
- Run machine validation: `python3 ../design-principles/scripts/validate_design_contract.py --manifest <path/to/manifest.json>`.

## Inputs
- Content inventory and navigation pain points
- User mental models and task priorities
- Localization constraints and terminology rules

## Outputs
- Information hierarchy and sitemap with `IA-NAV-*` IDs
- Labeling and taxonomy recommendations
- Navigation risk and ambiguity log

## Workflow
1. Audit current hierarchy and duplicate pathways.
2. Group content by user intent and task relevance.
3. Define navigation levels and cross-links.
4. Validate labeling for clarity and localization fit.
5. Test discoverability against key user tasks.

## Quality Gates
- Hierarchy depth and breadth remain navigable.
- Labels are unambiguous across supported locales.
- Critical tasks are reachable in predictable steps.
- Structural decisions are traceable to user needs.

## Failure Handling
- Stop when taxonomy terms conflict across core surfaces.
- Escalate when key tasks remain undiscoverable.
