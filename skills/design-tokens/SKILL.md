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

6. Compare at least two feasible approaches and explain why one is preferred.
7. Record key assumptions, unknowns, confidence, and rollback considerations.

## Quality Gates
- Token names are semantic and stable.
- Token hierarchy prevents duplication and drift.
- Accessibility-critical values meet contrast requirements.
- Token changes include migration impact notes.

- Decision rationale and trade-offs are explicit.
- Assumptions, unknowns, and confidence are explicitly documented.

## Failure Handling
- Stop when token model depends on one-off component exceptions.
- Escalate when token changes break critical accessibility guarantees.
