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

## Project Rule Policy
- Follow existing repository or organization rules first for IDs, approvers, quality gates, locale scope, and privacy handling.
- If no existing rule is available, define a lightweight project default and mark it as provisional.
- Treat example IDs in this skill as non-binding guidance.
- Skip manifest validation for documentation-only deliverables unless the project explicitly requests governed validation.
- Use `references/engineering-judgment-defaults.md` for default decision scoring, risk gating, uncertainty handling, and output structure.

## Inputs
- Localized strings and glossary references
- Target locales required by product scope or project policy
- UI builds covering target locales

## Outputs
- Locale-by-locale QA report with project-defined IDs (example: `LQA-*` when no existing policy is available)
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
- Policy-required approvers and privacy controls are explicitly recorded.

## Engineering Judgment Application
1. Generate at least two plausible options before recommending one.
2. Evaluate options using project-defined criteria; if missing, use defaults in `references/engineering-judgment-defaults.md`.
3. Record assumptions, unknowns, confidence, and key trade-offs in the final output.

## Failure Handling
- Stop release recommendation when required locale coverage is incomplete.
- Escalate when locale-specific blockers remain unresolved.
