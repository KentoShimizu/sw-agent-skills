---
name: code-review-performance
description: Specialized workflow for latency, throughput, and resource-efficiency risks in code changes. Use during code review when latency, throughput, or resource-efficiency risks must be assessed; do not use for broad non-performance review scopes.
---

# Code Review Performance

## Trigger Boundary
- Use when code changes need merge-readiness evaluation with explicit findings.
- Do not use for architecture option selection; use `architecture-tradeoff-analysis`.
- Do not use for writing implementation code directly; use relevant domain skills.

## Goal
Find high-risk defects early and unblock high-confidence merges.

## Inputs
- Change scope and risk profile
- Domain evidence for latency, throughput, and resource-efficiency risks in code changes
- Operational, compliance, and rollout constraints

## Outputs
- Performance review report with hotspot analysis
- Decision log for latency, throughput, and resource-efficiency risks in code changes
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for latency, throughput, and resource-efficiency risks in code changes.
2. Produce options and select an approach for latency, throughput, and resource-efficiency risks in code changes.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using complexity and benchmark evidence checks.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for latency, throughput, and resource-efficiency risks in code changes are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when performance regressions lack mitigation or verification.
- Escalate when accepted risk exceeds team policy thresholds.
