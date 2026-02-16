---
name: fastapi-service-development
description: "FastAPI service development workflow. Trigger when FastAPI service behavior (path operations, dependency injection, request/response models, validation, async execution, OpenAPI exposure) must be implemented or revised; do not use for repository-wide architecture governance or release management policy."
---

# Fastapi Service Development

## Trigger Boundary
- Use when implementing or refactoring FastAPI applications.
- Do not use for pure model training pipelines without HTTP interfaces.
- Do not use for ORM tuning alone; use database-specific skills.

## Goal
Deliver FastAPI services with explicit schema contracts, dependency boundaries, and predictable runtime behavior.

## Inputs
- Endpoint definitions and request/response schema requirements
- Dependency injection graph and external service dependencies
- Authentication, validation, and observability requirements

## Outputs
- Endpoint map with typed request/response models
- Dependency and lifecycle management plan
- Test and verification checklist for API behavior

## Workflow
1. Define Pydantic models and endpoint contracts first.
2. Separate routers, service logic, and infrastructure adapters.
3. Use dependency injection for shared resources and auth context.
4. Implement exception handlers with consistent API error shapes.
5. Validate docs generation and behavior with endpoint tests.

## Quality Gates
- All endpoints use explicit typed schemas.
- Dependency lifecycle is deterministic and testable.
- Error responses are consistent and documented.
- OpenAPI docs reflect actual runtime behavior.

## Failure Handling
- Stop when schema contracts are ambiguous or loosely typed.
- Escalate when dependency lifecycle cannot be managed safely.
