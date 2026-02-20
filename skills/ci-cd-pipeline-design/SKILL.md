---
name: ci-cd-pipeline-design
description: "Design CI/CD pipelines with explicit stage order, quality gates, artifact traceability, and rollback safety. Use when build/test/release flow is being created or changed and teams need deterministic release controls before adoption; do not use for application-domain algorithm or schema design."
---

# CI CD Pipeline Design

## Overview
Use this skill to design delivery pipelines that are deterministic, auditable, and safe under both success and failure paths.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Inputs To Gather
- Repository topology (mono-repo/multi-repo), services affected, and deployment targets.
- Required checks (lint, test, security, compliance, performance) and risk tolerance.
- Artifact model (build outputs, provenance, signing, retention).
- Rollout model (blue/green, canary, phased, manual approvals).

## Deliverables
- Pipeline stage blueprint with gate criteria and ownership.
- Artifact traceability model (source -> build -> deployable -> environment).
- Failure-path policy (auto-stop, rollback, manual override policy).
- Verification checklist for rollout and rollback readiness.

## Quick Start Blueprint

### Baseline stage order
1. `validate` (format/lint/static checks)
2. `test` (unit/integration)
3. `package` (immutable artifact creation)
4. `security` (SCA, secrets, policy checks)
5. `pre-release` (staging deploy + smoke)
6. `release` (progressive production rollout)

### Example gate policy
- No deploy if unit tests, integration tests, or security checks fail.
- Deploy only immutable artifacts produced by current commit.
- Rollback trigger: SLO breach or error-rate threshold breach during rollout window.

## Quality Standard
- Stage order is deterministic and enforces risk reduction early.
- Each gate has binary pass/fail criteria and named owner.
- Artifacts are immutable and traceable to source commit.
- Rollback path is validated, not assumed.
- Manual approvals are explicit and auditable where required.

## Workflow
1. Define delivery risks and non-negotiable release constraints.
2. Design stage sequence from fastest/high-signal checks to rollout.
3. Define gate criteria and failure behavior per stage.
4. Define artifact lineage and environment promotion rules.
5. Validate success and failure paths with dry-runs.
6. Publish operating policy and handoff guidance.

## Failure Conditions
- Stop when release-critical gates are undefined or non-deterministic.
- Stop when rollback path cannot be executed within required recovery time.
- Escalate when policy/compliance gates are bypassed without approved exception.
