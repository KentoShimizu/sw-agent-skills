---
name: design-tokens
description: "Design token architecture workflow for semantic, scalable, implementation-ready token systems. Use when multiple screens or products need consistent color/type/spacing/motion decisions and token definitions before component implementation; do not use for backend data-model or deployment pipeline decisions."
---

# Design Tokens

## Overview
Use this skill to replace hardcoded visual values with a governed token model that scales across teams and platforms.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- Naming rules and anti-patterns:
  - `references/token-naming-rules.md`
- Versioning and deprecation decision rules:
  - `references/token-versioning-policy.md`
- Accessibility and localization checks:
  - `references/token-accessibility-and-localization-checks.md`

## Templates And Assets
- Token taxonomy starter:
  - `assets/token-taxonomy-template.json`
- Legacy-to-token mapping sheet:
  - `assets/token-mapping-template.csv`
- Component token example set:
  - `assets/component-token-example.json`
- Deprecation decision record:
  - `assets/token-deprecation-plan-template.md`
- Rollout execution checklist:
  - `assets/token-rollout-checklist.md`

## Inputs To Gather
- Brand rules and product-level visual requirements.
- Current hardcoded values and style drift hotspots.
- Platform targets, theming needs, and implementation constraints.
- Accessibility requirements and localization-sensitive typography rules.

## Deliverables
- Token taxonomy and naming conventions (core, semantic, component-level).
- Token mapping plan from raw values to semantic tokens.
- Versioning/deprecation policy with migration guidance.
- Adoption checklist for design and engineering teams.

## Quick Example
- Core token: `color.blue.600`.
- Semantic token: `color.action.primary.default`.
- Component token: `button.primary.background.default`.
- Rule: components consume semantic/component tokens only, never raw core values directly.

## Quality Standard
- Naming reflects intent, not specific component or hex value.
- Token layering prevents direct coupling between components and raw primitives.
- Accessibility-critical token sets pass contrast and state visibility requirements.
- Token changes include migration impact and rollout sequence.

## Workflow
1. Define token layers and scope boundaries using `assets/token-taxonomy-template.json`.
2. Map existing raw values to semantic tokens with `assets/token-mapping-template.csv`.
3. Add component-level aliases only where needed for stability, referencing `assets/component-token-example.json`.
4. Establish version/deprecation workflow using `references/token-versioning-policy.md` and `assets/token-deprecation-plan-template.md`.
5. Validate coverage with `references/token-accessibility-and-localization-checks.md` and complete `assets/token-rollout-checklist.md`.

## Failure Conditions
- Stop when token design allows uncontrolled one-off exceptions.
- Stop when naming ties tokens to unstable implementation details.
- Escalate when token changes break accessibility without mitigation.
