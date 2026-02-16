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

## Project Rule Policy
- Follow existing repository or organization rules first for IDs, approvers, quality gates, locale scope, and privacy handling.
- If no existing rule is available, define a lightweight project default and mark it as provisional.
- Treat example IDs in this skill as non-binding guidance.
- Skip manifest validation for documentation-only deliverables unless the project explicitly requests governed validation.
- Use `references/engineering-judgment-defaults.md` for default decision scoring, risk gating, uncertainty handling, and output structure.

## Inputs
- Content inventory and navigation pain points
- User mental models and task priorities
- Localization constraints and terminology rules

## Outputs
- Information hierarchy and sitemap with project-defined IDs (example: `IA-NAV-*` when no existing policy is available)
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

## Engineering Judgment Application
1. Generate at least two plausible options before recommending one.
2. Evaluate options using project-defined criteria; if missing, use defaults in `references/engineering-judgment-defaults.md`.
3. Record assumptions, unknowns, confidence, and key trade-offs in the final output.

## Failure Handling
- Stop when taxonomy terms conflict across core surfaces.
- Escalate when key tasks remain undiscoverable.
