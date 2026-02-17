---
name: docker-compose-patterns
description: "Design multi-service local orchestration with Docker Compose, including dependency wiring, startup order, health checks, and shared network/storage boundaries. Use when local integration environments need deterministic service composition; do not use for production orchestration policy design."
---

# Docker Compose Patterns

## Overview
Use this skill to define reliable multi-service local stacks for development, debugging, and integration testing.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- Dependency and startup patterns:
  - `references/compose-dependency-guidance.md`

## Templates And Assets
- Compose stack baseline:
  - `assets/compose-stack-template.yaml`
- Operations runbook:
  - `assets/compose-operations-runbook-template.md`

## Inputs To Gather
- Services and dependencies required for target workflows.
- Required startup order and readiness conditions.
- Shared volumes/networks and data persistence needs.
- Local resource constraints and isolation requirements.

## Deliverables
- Compose service topology with explicit dependency rules.
- Health-check strategy and startup stabilization policy.
- Environment and secret handling policy for local use.
- Developer runbook for common stack operations.

## Quick Example
- API depends on DB and cache with health-check gating.
- Use named network; avoid host network unless required.
- Use profiles to separate optional services (e.g., observability tools).

## Quality Standard
- Dependency behavior is deterministic and health-driven.
- Service contracts (ports, env, volumes) are explicit.
- Local stack startup/shutdown is repeatable.
- Secret handling avoids committing sensitive defaults.

## Workflow
1. Map required services and dependency graph.
2. Define compose services, networks, volumes, and env boundaries using `assets/compose-stack-template.yaml`.
3. Add health checks and readiness-aware dependency rules.
4. Validate full stack startup and critical workflows.
5. Document operational commands and troubleshooting notes in `assets/compose-operations-runbook-template.md`.

## Failure Conditions
- Stop when service dependencies are implicit or race-prone.
- Stop when local stack requires unsafe credential handling.
- Escalate when resource contention prevents reliable local execution.
