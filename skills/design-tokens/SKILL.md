---
name: design-tokens
description: "Design token architecture workflow for defining semantic, scalable, and implementation-ready token systems. Use when UX, interaction, visual, or design-governance artifacts are the primary deliverable; do not use for backend data-model or deployment pipeline decisions."
---

# Design Tokens

## Trigger Boundary
- Use when visual values are hardcoded or inconsistent across UI surfaces.
- Do not use for component behavior design; use `interaction-design`.
- Do not use for final handoff packaging; use `figma-handoff`.

## Goal
Define a token system that is semantic, versionable, and implementation-safe.

## Shared Design Contract (Canonical)
- Use `../design-principles/references/design-governance-contract.md` as the single schema and gate source.
- Assign token IDs as `DSN-TOK-<CATEGORY>-*`.
- Run machine validation: `python3 ../design-principles/scripts/validate_design_contract.py --manifest <path/to/manifest.json>`.

## Inputs
- Brand and product visual requirements
- Existing style values and debt map
- Platform constraints and theming requirements

## Outputs
- Token taxonomy and naming rules
- Token set with `DSN-TOK-*` IDs
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

## Failure Handling
- Stop when token model depends on one-off component exceptions.
- Escalate when token changes break critical accessibility guarantees.
