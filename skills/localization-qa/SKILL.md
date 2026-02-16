---
name: localization-qa
description: "Localization quality assurance workflow for validating language correctness, layout resilience, and locale-specific UX behavior. Trigger when localized UI/content must be verified across target locales for translation quality, truncation/layout issues, formatting rules, and locale behavior before release; do not use for backend data-model or deployment pipeline decisions."
---

# Localization Qa

## Trigger Boundary
- Use when localized UI must be validated before release.
- Do not use for translation creation workflows.
- Do not use for global navigation IA redesign; use `information-architecture`.

## Goal
Ensure localized experiences are accurate, usable, and visually stable.

## Shared Design Contract (Canonical)
- Use `../design-principles/references/design-governance-contract.md` as the primary reference for recommended structure.
- Track localization QA artifacts with `DREV-*` IDs.
- Optional consistency check (only if your repository enforces manifest validation): `python3 ../design-principles/scripts/validate_design_contract.py --manifest <path/to/manifest.json>`.

## Inputs
- Localized strings and glossary references
- Target locales including `en-US`, `ja-JP`, and at least two EU locales
- UI builds covering target locales

## Outputs
- `DREV-*` locale-by-locale QA report
- Truncation, overflow, and semantic mismatch findings
- Release recommendation with blocking issues

## Workflow
1. Validate locale coverage and explicit missing-locale failure behavior.
2. Check text correctness and terminology consistency.
3. Stress-test expansion, truncation, and wrapping behavior.
4. Validate date, time, number, and currency formatting.
5. Publish defects by severity and locale impact with contract validation evidence.

## Quality Gates
- Required locales are fully tested.
- No blocking truncation or semantic errors remain.
- Critical user flows pass in every required locale.
- Defect ownership and retest status are explicit.
- Contract validation passes for `DREV-*` artifact manifests.
- When `checks.user_facing_change` is `true`, Privacy Reviewer approval and privacy evidence are present.

## Failure Handling
- Stop release recommendation when required locale coverage is incomplete.
- Escalate when locale-specific blockers remain unresolved.
