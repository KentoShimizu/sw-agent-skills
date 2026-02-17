---
name: express-api-development
description: "Express API development workflow for production-ready Node.js services. Use when Express-specific API code (routing, middleware chain, validation, error handling, auth integration, request lifecycle behavior) must be implemented or revised; do not use for repository-wide architecture governance or release management policy."
---

# Express Api Development

## Overview
Use this skill to design and implement Express services with explicit middleware ordering, stable API errors, and operationally debuggable behavior.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- Middleware ordering guidance:
  - `references/express-middleware-ordering-guidance.md`
- Error handling guidance:
  - `references/express-error-handling-guidance.md`

## Templates And Assets
- Route module starter:
  - `assets/express-route-module-template.js`
- Error catalog template:
  - `assets/express-error-catalog-template.md`
- Verification checklist:
  - `assets/express-api-verification-checklist.md`

## Inputs To Gather
- Endpoint requirements and validation rules.
- AuthN/AuthZ and rate-limit requirements.
- Logging and observability expectations.
- Existing middleware stack and error contract conventions.
- Request/response shape contracts for boundary-safe handoff to service layer.

## Deliverables
- Route and middleware composition plan.
- Validation and error response contract.
- Security and observability integration plan.
- Verification checklist with critical-path coverage.

## Workflow
1. Define route modules by domain and resource responsibility.
2. Apply middleware ordering from `references/express-middleware-ordering-guidance.md`.
3. Implement route handlers using `assets/express-route-module-template.js`.
4. Parse and validate `req.params`/`req.query`/`req.body` once, then map to explicit domain input objects.
5. Centralize and normalize error handling using `references/express-error-handling-guidance.md` and `assets/express-error-catalog-template.md`.
6. Validate behavior with `assets/express-api-verification-checklist.md`.

## Quality Standard
- Middleware order is explicit, deterministic, and testable.
- Validation failures are client-actionable and consistent.
- Error responses use stable codes and correlation IDs.
- Operational signals are sufficient for incident triage.
- Route handlers do not pass raw request objects or untyped payload bags into core domain services.

## Failure Conditions
- Stop when middleware side effects are order-dependent and undocumented.
- Stop when endpoints bypass centralized error mapping.
- Escalate when error contracts diverge across routes without policy approval.
