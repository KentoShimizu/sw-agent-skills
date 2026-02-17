---
name: localization-qa
description: "Localization QA workflow for language correctness, layout resilience, and locale-specific behavior validation before release. Use when localized UI/content must be verified across target locales; do not use for backend data-model or deployment pipeline decisions."
---

# Localization Qa

## Overview
Use this skill to verify that localized experiences remain correct, usable, and release-safe across required locales.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- Localization defect severity rules:
  - `references/localization-defect-severity-rules.md`

## Templates And Assets
- Locale QA report template:
  - `assets/localization-qa-report-template.csv`
- Localization regression checklist:
  - `assets/localization-regression-checklist.md`

## Inputs To Gather
- Required locale list and release scope.
- Localized strings, glossary, and style rules.
- UI builds/config for locale switching.
- Critical flows and compliance-sensitive copy.

## Deliverables
- Locale-by-locale defect report with severity and ownership.
- Regression verification evidence for critical flows.
- Release recommendation with blocker summary.
- Follow-up retest plan for unresolved issues.

## Workflow
1. Confirm locale coverage and build readiness.
2. Validate language and terminology correctness.
3. Stress-test layout expansion/truncation/wrapping behavior.
4. Validate locale formatting and directional behavior.
5. Record findings in `assets/localization-qa-report-template.csv` and close with `assets/localization-regression-checklist.md`.

## Quality Standard
- Required locales are fully covered.
- Critical flows pass with no blocker-level localization defects.
- Severity reflects user/business impact across locales.
- Defect ownership and retest status are explicit.

## Failure Conditions
- Stop release recommendation when required locale coverage is incomplete.
- Stop when blocker-level semantic or layout defects remain unresolved.
- Escalate when localization defects affect legal/compliance-critical content.
