---
name: docker-basics
description: "Design and review container runtime basics for reproducible local/service execution using Docker. Use when container build/run behavior, networking, volumes, and runtime isolation need explicit decisions; do not use for API contract or requirement prioritization tasks."
---

# Docker Basics

## Overview
Use this skill to ensure containerized workloads are reproducible, debuggable, and operationally safe.

## Inputs To Gather
- Application runtime requirements and dependencies.
- Local/dev/prod run differences.
- Required network ports, volumes, and environment variables.
- Security constraints (user, capabilities, filesystem access).

## Deliverables
- Container run policy (entrypoint, env, ports, volumes, user).
- Local reproducibility checklist.
- Runtime risk list (permissions, secrets, mutable state).
- Verification steps for startup and health checks.

## Quick Example
- Run as non-root user.
- Mount only required volume paths.
- Fail fast if required env vars are missing.
- Expose health endpoint and readiness check.

## Quality Standard
- Runtime config is minimal and explicit.
- Container behavior is reproducible across environments.
- Security posture follows least-privilege defaults.
- Health and failure signals are observable.

## Workflow
1. Define container runtime contract.
2. Configure networking, storage, and environment boundaries.
3. Validate startup/health behavior.
4. Verify security constraints and secret handling.
5. Document reproducible run commands.

## Failure Conditions
- Stop when required runtime dependencies are implicit.
- Stop when container requires unnecessary privileged execution.
- Escalate when runtime differences make behavior non-reproducible.
