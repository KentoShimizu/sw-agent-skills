---
name: design-qa-implementation-parity
description: "Verify implementation parity against approved design specs with severity-based decisions and fix guidance. Use when implemented UI must be compared against approved specs before release or sign-off; do not use for backend data-model or deployment pipeline decisions."
---

# Design Qa Implementation Parity

## Overview
Use this skill to detect and triage design-to-implementation drift with evidence that engineers and designers can both act on.

## Inputs To Gather
- Approved design source and exact version/snapshot.
- Target implementation build, environment, and feature flags.
- Scope list of screens, states, breakpoints, and locales to validate.
- Existing acceptance criteria or release gates for UI parity.

## Deliverables
- Parity findings report with severity, scope, owner, and reproduction steps.
- State-level pass/fail checklist for critical flows.
- Prioritized remediation plan with release impact notes.
- Sign-off decision (approve/conditional/reject) with clear rationale.

## Quick Example
- Blocker: CTA button hidden on mobile breakpoint in checkout summary.
- Major: loading state typography differs from approved scale and causes truncation.
- Minor: icon spacing deviates by 2px without usability impact.
- Decision: reject until blocker fixed; allow major/minor with dated follow-up only if policy permits.

## Quality Standard
- Source versions are locked so comparisons are deterministic.
- Coverage includes critical states: loading, empty, error, success.
- Every mismatch includes reproducible evidence and ownership.
- Severity rules are consistent and tied to user/business impact.

## Workflow
1. Freeze source design and implementation versions for the review window.
2. Compare critical flows first, then secondary and edge states.
3. Classify mismatches by severity and release impact.
4. Assign owners and define remediation order.
5. Publish sign-off outcome with unresolved risk explicitly documented.

## Failure Conditions
- Stop sign-off when source versions are not locked.
- Stop when critical flows are missing parity coverage.
- Escalate when blocker-level mismatches remain unresolved near release.
