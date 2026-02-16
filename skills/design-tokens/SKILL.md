---
name: design-tokens
description: "Design token architecture workflow for defining semantic, scalable, and implementation-ready token systems. Trigger when multiple screens or products need consistent color/type/spacing/motion decisions and token definitions must be established before component implementation; do not use for backend data-model or deployment pipeline decisions."
---

# Design Tokens

## Trigger Boundary
- Use when visual values are hardcoded or inconsistent across UI surfaces.
- Do not use for component behavior design; use `interaction-design`.
- Do not use for final handoff packaging; use `figma-handoff`.

## Goal
Define a token system that is semantic, versionable, and implementation-safe.

## Project Rule Policy
- Follow existing repository or organization rules first for IDs, approvers, quality gates, locale scope, and privacy handling.
- If no existing rule is available, define a lightweight project default and mark it as provisional.
- Treat example IDs in this skill as non-binding guidance.
- Skip manifest validation for documentation-only deliverables unless the project explicitly requests governed validation.
- Use `references/engineering-judgment-defaults.md` for default decision scoring, risk gating, uncertainty handling, and output structure.

## Inputs
- Brand and product visual requirements
- Existing style values and debt map
- Platform constraints and theming requirements

## Outputs
- Token taxonomy and naming rules
- Token set with project-defined IDs (example: `DSN-TOK-*` when no existing policy is available)
- Token governance and migration guidance

## Workflow
1. Define semantic token categories and scopes.
2. Map raw values into semantic tokens.
3. Define alias and component token layering.
4. Establish versioning and deprecation rules.
5. Validate token coverage against key components.

## Quality Gates
- Token names are semantic and stable.
- Token hierarchy prevents duplication and drift.
- Accessibility-critical values meet contrast requirements.
- Token changes include migration impact notes.

## Engineering Judgment Application
1. Generate at least two plausible options before recommending one.
2. Evaluate options using project-defined criteria; if missing, use defaults in `references/engineering-judgment-defaults.md`.
3. Record assumptions, unknowns, confidence, and key trade-offs in the final output.

## Failure Handling
- Stop when token model depends on one-off component exceptions.
- Escalate when token changes break critical accessibility guarantees.
