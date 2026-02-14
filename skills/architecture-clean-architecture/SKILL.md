---
name: architecture-clean-architecture
description: "Clean Architecture implementation design for enforcing dependency inversion and stable domain-centric layering. Use when system boundaries, module relationships, and architecture-level constraints are being defined; do not use for single-module implementation refactors without architecture impact."
---

# Architecture Clean Architecture

## Trigger Boundary
- Use when dependency direction and layering violations must be prevented.
- Do not use for service-level topology choice; use `architecture-monolith` or `architecture-microservices`.
- Do not use for domain boundary discovery; use `architecture-ddd`.

## Goal
Define enforceable layer boundaries and dependency rules around core domain logic.

## Shared Architecture Contract (Canonical)
- Use `skills/architecture-principles/references/architecture-governance-contract.md` as the only schema source.
- Validate all IDs, lifecycle states, and gate rules against the canonical contract.
- Do not define local ID formats or alternate state machines.

## Compliance & Governance Baseline (US, Japan, EU)
- Keep policy and compliance logic in domain/use-case layers, not frameworks.
- Ensure sensitive data access crosses explicit adapter boundaries.
- Prepare an `ARC-CMP-*` evidence package for governance review.

## Inputs
- Domain rules and application use cases
- Existing code structure and dependency graph
- Framework and infrastructure constraints

## Outputs
- Layer model and dependency rules
- Port and adapter definitions
- Refactoring plan for boundary violations

## Workflow
1. Define layers: domain, use case, interface, infrastructure.
2. Specify allowed dependency direction between layers.
3. Define ports for external systems and adapters for implementations.
4. Identify existing violations and prioritize refactoring steps.
5. Record enforcement checks for CI or review.

## Quality Gates
- Inner layers have no dependency on outer frameworks.
- Use cases orchestrate behavior without infrastructure leakage.
- `ARC-CMP-*` evidence package is complete and approved.
- Greenfield designs exclude fallback paths; brownfield rollback requires trigger and runbook.

## Failure Handling
- Stop when layer boundaries cannot be enforced technically.
- Stop when canonical contract validation fails.
- Escalate when critical business rules reside in outer layers.
