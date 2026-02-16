---
name: playwright
description: "Browser flow verification workflow using Playwright CLI. Trigger when web user journeys need executable browser-level verification evidence (pass/fail results, traces, screenshots) before merge or release; do not use for product requirement prioritization or architecture topology selection."
---

# Playwright

## Trigger Boundary
- Use when real browser interaction is required to validate behavior.
- Do not use for unit or API-only verification scopes.
- Do not use for desktop app capture where no browser is involved.

## Goal
Produce deterministic browser-run evidence for functional and UI flow validation.

## Inputs
- Target URLs and critical user journey definition
- Test credentials or fixtures (provided via environment variables or secret store)
- Required artifacts (`snapshot`, `screenshot`, `trace`)

## Outputs
- Reproducible command sequence for target flow
- Artifact bundle for key checkpoints and failures
- Findings list with exact reproduction references

## Workflow
1. Confirm Playwright CLI runtime availability and browser readiness.
2. Prepare test credentials from environment variables; avoid inline plaintext secrets.
3. Open target page and snapshot before interacting.
4. Execute flow step-by-step; refresh references after DOM-changing actions.
5. Capture artifacts at decision points and failure boundaries.
6. Report observed behavior with command-level traceability.

## Quality Gates
- Every action maps to a fresh, valid UI reference.
- Flow can be replayed from the documented command sequence.
- Artifacts cover both success path and failing branch when present.
- Conclusions are based on observed runs, not inferred behavior.
- Credentials are never hardcoded in commands, scripts, logs, or screenshots.

## Failure Handling
- Stop when automation prerequisites (runtime, auth, env) are unmet.
- Escalate when deterministic replay is impossible due to external instability.
- Stop when only plaintext credentials are available and secure injection is not possible.
