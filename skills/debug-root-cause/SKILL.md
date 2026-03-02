---
name: debug-root-cause
description: "Systematic debugging workflow for isolating software root causes, implementing proportional fixes, and verifying recovery with reproducible evidence. Use when application/runtime failures, regressions, or flaky behavior are observed and the task requires both diagnosis and remediation. When specialized skills are available in the environment, defer GitHub Actions failure triage to `github-fix-ci`, commit-introduction isolation to `git-bisect-debugging`, profiler-led hotspot analysis to `performance-profiling`, active security incident command to `security-incident-response`, and postmortem-only reporting to `incident-postmortem`. Do not use for broad feature implementation or speculative hardening without evidence."
---

# Debug Root Cause

## Overview

Use this skill to move from symptom to confirmed root cause with minimal guesswork and auditable evidence.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.
- If available, prefer `github-fix-ci` when the primary symptom is a GitHub Actions check failure.
- If available, prefer `git-bisect-debugging` when the unresolved question is "which commit introduced the regression?"
- If available, prefer `performance-profiling` when profiler evidence and optimization prioritization are the main objective.
- If available, prefer `security-incident-response` for active compromise triage/containment/eradication.
- If available, prefer `incident-postmortem` when incident stabilization is complete and the task is retrospective analysis.

## Shared References
- Strategy matrix:
  - `references/debug-strategy-matrix.md`

## Templates And Assets
- Session log template:
  - `assets/debug-session-log-template.md`
- Fix verification checklist:
  - `assets/debug-fix-verification-checklist.md`

## Inputs To Gather
- Stable reproduction steps and failure evidence (logs, traces, failing tests, timestamps).
- Expected behavior and actual behavior with explicit mismatch.
- Suspected boundary (module/service/config/dependency) and recent changes.
- Runtime constraints (environment, dataset, flags, concurrency/load profile).
- Success condition that proves the issue is fixed.

## Deliverables
- Confirmed root cause statement with reproducible evidence.
- Implemented fix tied to the causal chain.
- Verification evidence that the failure no longer reproduces.
- Residual risks and follow-up items outside current scope.

## Workflow
1. Stabilize reproduction and capture a baseline using `assets/debug-session-log-template.md`.
2. Define the failure contract: expected vs actual behavior, first observable break, and affected boundary.
3. Build hypotheses and prioritize by likelihood, blast radius, and experiment cost.
4. Run controlled experiments by changing one variable at a time; record outcomes.
5. Confirm root cause by demonstrating both removal and reintroduction criteria where safe.
6. Select a remediation scope that matches project reality: required behavior, current architecture, operational constraints, and delivery risk.
7. Implement a minimal root-cause fix; avoid symptom-only guards, speculative hardening, hidden defaults, and unrelated refactors.
8. Verify using the checks in `assets/debug-fix-verification-checklist.md`.
9. Publish an investigation summary with evidence, implementation rationale, and follow-up actions.

## Remediation Fit Guardrails
- Prefer the smallest change that reliably resolves the observed failure mode.
- Match strictness and complexity to explicit requirements and real operational risk.
- Avoid adding framework-level abstractions or future-proofing not required by current constraints.
- Keep compatibility decisions explicit; do not retain legacy paths unless required by active consumers.
- When multiple fixes are possible, choose the option with the lowest long-term maintenance cost at acceptable risk.

## Quality Standard
- Reproduction is stable enough for repeated validation.
- Root cause is demonstrated by evidence, not inference only.
- Implemented fix scope is proportional and targets the causal path directly.
- Regression/edge checks are updated for the discovered failure mode.
- Logs/metrics/error surfaces remain actionable after the fix.

## Failure Conditions
- Stop when reproduction is nondeterministic and cannot be stabilized.
- Stop when required environment or data access is unavailable.
- Escalate when issue ownership crosses teams or requires architectural change.
