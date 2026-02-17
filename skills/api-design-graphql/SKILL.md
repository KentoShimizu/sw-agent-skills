---
name: api-design-graphql
description: GraphQL schema and resolver contract design for type boundaries, nullability, authz, and query-cost safety. Trigger when SDL, resolver behavior, field contracts, or query safety controls are added/changed, and their contract impact is not yet explicitly specified. Do not use for REST/OpenAPI endpoint design, API version lifecycle governance, or standalone error taxonomy design.
---

# API Design GraphQL

## Scope Boundaries
- Use when GraphQL schema boundaries, resolver contracts, and query safety must be defined.
- Use proactively when GraphQL SDL/resolver diffs appear in specs, manifests, or source.
- Use when clients need flexible field selection but query safety and authz boundaries are not yet explicit.
- Do not use for REST-first endpoint design; use `api-design-rest`.
- Do not use for storage internals; use `db-*`.

## Goal
Deliver GraphQL contracts that are safe to evolve and efficient at runtime.

## Shared API Contract (Canonical)
- Use `../api-design-rest/references/api-governance-contract.md` as the canonical contract.
- Optional consistency checks (only if your repository enforces manifest validation):
  - `python3 ../api-design-rest/scripts/validate_api_contract.py --manifest <path/to/manifest.json>`
- Use valid templates in `../api-design-rest/assets/`.
- Use transport decision reference:
  - `../api-design-rest/references/transport-selection-matrix.md`
- Use threshold derivation reference:
  - `../api-design-rest/references/threshold-derivation-framework.md`
- Do not redefine API artifact ID formats, states, or approval gates.

## Implementation Templates
- GraphQL SDL template:
  - `../api-design-rest/assets/graphql-schema-template.graphql`

## Inputs
- Required queries/mutations and consumer usage patterns
- Entity ownership and field-level authorization requirements
- Performance budgets for depth, complexity, and resolver latency

## Outputs
- Schema contract (types, inputs, mutations, deprecation tags)
- Resolver behavior contract (authz, caching, batching, nullability semantics)
- Query safety controls (complexity/depth limits and abuse controls)

## Workflow
1. Define schema boundaries aligned with domain ownership, not backend table layout.
2. Model inputs and payloads for forward-compatible evolution and explicit nullability.
3. Set resolver authorization rules and avoid N+1 with batching strategy.
4. Decide whether GraphQL is the primary transport or a gateway facade, and document alternatives.
5. Define query complexity/depth limits and abuse safeguards for public access paths.
6. Define error extension fields and trace correlation behavior.
7. Derive threshold methods for query latency, complexity limits, and resolver concurrency.
8. Validate compatibility, operational readiness, and canonical API contract compliance.

## Quality Gates
- Schema evolution rules are explicit, including deprecations and migration notes.
- Resolver behavior is deterministic, authorized, and free of unbounded fan-out paths.
- Query safety limits are defined and enforced.
- Observability and error semantics are consistent with API governance contract.

## Failure Handling
- Stop when schema changes break existing client contracts without approved version plan.
- Stop when resolver performance or query safety controls are undefined.
- Escalate when required security/governance approvers are missing.
