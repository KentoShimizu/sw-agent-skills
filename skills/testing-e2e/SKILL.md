---
name: testing-e2e
description: "End-to-end test planning for critical user journeys across integrated systems. Use when release confidence depends on browser/API/dependency behavior as one flow; do not use for isolated unit behavior or pure contract checks."
---

# Testing E2E

## Overview
Use this skill to validate business-critical journeys under integrated runtime conditions.

## Scope Boundaries
- Use when failure risk is in end-to-end user or operator flows.
- Typical requests:
  - `Validate checkout flow across UI, API, and payment integration.`
  - `Define minimum critical E2E regression set before release.`
  - `Prove no fatal breakage in top user journeys.`
- Do not use when:
  - Only deterministic function logic must be tested (`testing-unit`).
  - Only interface compatibility is required (`testing-contract`).

## Inputs
- Critical journey map and release risk profile
- Test environment constraints and dependencies
- Existing automation assets and known flaky areas

## Outputs
- Critical journey E2E pack with environment assumptions
- Decision record for coverage depth and gating strategy
- Verification checklist and rollback signals

## Workflow
1. Identify journeys that gate release confidence.
2. Define minimum E2E set by risk and business impact using `assets/critical-journey-template.md`.
3. Compare execution strategies (full, smoke, tiered) and choose one.
4. Implement deterministic setup/teardown and evidence capture.
5. Publish pass/fail status, flake risk, and residual gaps.

## Quality Gates
- Critical journeys are explicitly covered.
- Test evidence is reproducible with fixed environment assumptions.
- Gating and rollback signals are defined.
- Flakiness and environment risks are documented.

## Failure Handling
- Stop when critical journeys remain untested.
- Escalate when environment instability prevents reliable evidence.

## Bundled Resources
- `references/trigger-and-examples.md`: trigger patterns, anti-patterns, and deliverable expectations.
- `assets/critical-journey-template.md`: concise template for critical-path E2E scenario definition and evidence capture.
