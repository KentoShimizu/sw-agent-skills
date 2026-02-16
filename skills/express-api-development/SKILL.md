---
name: express-api-development
description: "Express API development workflow. Trigger when Express-specific API code (routing, middleware chain, validation, error handling, auth integration, request lifecycle behavior) must be implemented or revised with framework-level decisions in scope; do not use for repository-wide architecture governance or release management policy."
---

# Express Api Development

## Trigger Boundary
- Use when building or modifying Express-based HTTP APIs.
- Do not use for framework-agnostic API policy only; use `api-design-rest`.
- Do not use for infrastructure deployment tasks.

## Goal
Build maintainable Express APIs with explicit middleware chain and reliable error semantics.

## Inputs
- Endpoint requirements and validation rules
- AuthN/AuthZ and rate-limit requirements
- Logging and observability expectations

## Outputs
- Route and middleware composition plan
- Request validation and error response strategy
- Operational checklist for logging and health endpoints

## Workflow
1. Define route modules by domain and resource responsibility.
2. Add validation middleware before business logic handlers.
3. Centralize error handling with consistent response shapes.
4. Wire auth, rate limiting, and request correlation IDs.
5. Validate critical paths with integration-level API tests.

## Quality Gates
- Middleware order is deterministic and documented.
- Validation failures return clear client-actionable responses.
- Error handling avoids unhandled promise or silent failures.
- Logs and metrics are sufficient for incident triage.

## Failure Handling
- Stop when middleware side effects are order-dependent and unclear.
- Escalate when error contracts diverge across endpoints.
