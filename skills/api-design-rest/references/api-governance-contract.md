# API Governance Contract

## Scope
Apply this contract to all API skills:
- `api-design-rest`
- `api-design-graphql`
- `api-error-handling`
- `api-versioning`
- `api-contract-testing`

Do not redefine ID formats, lifecycle states, compatibility rules, or approval gates in individual skill files.

## ID Schema (Single Source of Truth)
- `API-RES-<YYYYMMDD>-<NNN>`: `^API-RES-[0-9]{8}-[0-9]{3,}$`
  - REST design artifact
- `API-GQL-<YYYYMMDD>-<NNN>`: `^API-GQL-[0-9]{8}-[0-9]{3,}$`
  - GraphQL design artifact
- `API-ERR-<YYYYMMDD>-<NNN>`: `^API-ERR-[0-9]{8}-[0-9]{3,}$`
  - API error-handling artifact
- `API-VER-<YYYYMMDD>-<NNN>`: `^API-VER-[0-9]{8}-[0-9]{3,}$`
  - API versioning artifact
- `API-CDC-<YYYYMMDD>-<NNN>`: `^API-CDC-[0-9]{8}-[0-9]{3,}$`
  - Consumer-driven contract testing artifact
- `API-CMP-<YYYYMMDD>-<NNN>`: `^API-CMP-[0-9]{8}-[0-9]{3,}$`
  - Compliance evidence package for API changes

## Issuance Rules
- Allocate IDs sequentially per prefix.
- Keep ID history append-only.
- Never reuse retired IDs.
- On collision, issue a new ID and mark the previous ID as invalid with reason.

## Lifecycle States
- `API-RES-*`, `API-GQL-*`, `API-ERR-*`, `API-VER-*`: `draft`, `reviewed`, `approved`, `deprecated`
- `API-CDC-*`: `draft`, `active`, `blocked`, `deprecated`
- `API-CMP-*`: `draft`, `reviewed`, `approved`, `expired`

## Compatibility Policy
- Treat additive schema changes as the default path.
- Treat these as breaking changes:
  - field or enum removal
  - type narrowing
  - required field addition without default migration path
  - status/error contract behavior change
- For breaking changes, require all:
  - explicit version transition strategy
  - migration guide for consumers
  - deprecation window of at least 90 days

## Naming Policy
- Enforce a single naming convention per API surface and document it explicitly.
- REST naming baseline:
  - paths use stable resource nouns and avoid action verbs
  - path segments are lowercase and hyphen-safe
  - query parameter names are consistent across pagination/filtering patterns
- GraphQL naming baseline:
  - type and enum names are `PascalCase`
  - field and argument names are `camelCase`
  - mutation names express domain intent and avoid transport leakage
- Error naming baseline:
  - error codes are stable, machine-readable, and namespaced
  - do not encode environment-specific details in error identifiers

## Interaction Model and Transport Selection
- Selection must cover both internal and external API use cases (`internal`, `external`, `both`).
- Explicitly classify the interaction model:
  - `sync` (request-response)
  - `async` (event-driven, deferred processing)
  - `streaming` (server push with ordered flow)
  - `bidirectional_realtime` (stateful duplex channel)
- Select primary transport from:
  - `rest`
  - `graphql`
  - `grpc`
  - `websocket`
  - `sse`
  - `queue`
- Record rationale and rejected alternatives for every transport choice.
- Additional mandatory controls by transport/mode:
  - `websocket` or `sse`: define connection lifecycle, heartbeat, and disconnect handling.
  - `queue`: define delivery semantics, deduplication/idempotency, and replay policy.
  - `async`, `streaming`, `bidirectional_realtime`: define backpressure and consumer lag strategy.

## Threshold Policy (Type and Derivation)
Do not hardcode one-size-fits-all thresholds in this contract. Instead, require explicit derivation methods for:
- latency target (for example p95/p99 by user journey criticality)
- availability target and error budget policy
- timeout budget across client/network/server layers
- throughput and capacity headroom policy
- payload size limits
- concurrency limits (requests, streams, or active sessions)
- retry and backoff budget
- delivery semantics (ordering, at-least-once/exactly-once intent, duplicate handling)

Each API artifact must document:
- which threshold types are applicable
- how each threshold value is derived from SLO, business risk, and system constraints
- owner and re-evaluation trigger for threshold revisions

## Security and Operability Gates
- Authentication and authorization rules are explicit per endpoint or operation.
- Error contracts are machine-actionable and include trace correlation fields.
- External/public APIs define rate-limit policy.
- Runbook updates exist for operationally significant contract changes.
- New design work does not rely on fallback logic to mask contract errors.

## Approval Matrix
- Required for all API artifacts:
  - `API Owner`
  - `Engineering Owner`
- Required when `checks.handles_sensitive_data` is `true`:
  - `Security Reviewer`
- Required when `checks.external_public_api` is `true`:
  - `API Governance Reviewer`
- Required when `checks.regulated_jurisdiction_impact` is `true`:
  - `Legal Reviewer`

## Machine Validation
- Run: `python3 skills/api-design-rest/scripts/validate_api_contract.py --manifest <path/to/manifest.json>`
- For batch validation, run: `python3 scripts/run_contract_validators.py --api-manifest <path/to/manifest.json>`

Manifest requirements:
- Required root fields:
  - `artifact_id`
  - `state`
  - `approvers`
  - `checks`
- `checks` must include booleans:
  - `id_format_validated`
  - `backward_compatibility_reviewed`
  - `transport_selection_documented`
  - `naming_convention_defined`
  - `authz_modeled`
  - `error_contract_defined`
  - `observability_fields_defined`
  - `runbook_updated`
  - `timeout_budget_defined`
  - `delivery_semantics_defined`
  - `backpressure_strategy_defined`
  - `connection_lifecycle_defined`
  - `consumer_idempotency_defined`
  - `no_fallback_logic`
  - `rate_limit_policy_defined`
  - `handles_sensitive_data`
  - `external_public_api`
  - `regulated_jurisdiction_impact`
- Required object `decision_context`:
  - `api_audience` (`internal` | `external` | `both`)
  - `interaction_mode` (`sync` | `async` | `streaming` | `bidirectional_realtime`)
  - `primary_transport` (`rest` | `graphql` | `grpc` | `websocket` | `sse` | `queue`)
  - `selection_rationale` (non-empty string)
  - `alternatives_considered` (non-empty array of strings)
  - `naming_convention_summary` (non-empty string)
  - `threshold_method_summary` (non-empty string)
- Required object `threshold_policy`:
  - `latency_target_derivation`
  - `availability_target_derivation`
  - `timeout_budget_derivation`
  - `capacity_headroom_derivation`
  - `payload_limit_derivation`
  - `concurrency_limit_derivation`
  - `retry_backoff_derivation`
  - `delivery_semantics_derivation`
- Prefix-specific `checks`:
  - `API-RES-*`: `http_semantics_validated`, `idempotency_strategy_defined`
  - `API-GQL-*`: `query_cost_limits_defined`, `n_plus_one_guard_defined`
  - `API-ERR-*`: `status_mapping_complete`, `error_code_registry_updated`
  - `API-VER-*`: `compatibility_matrix_updated`, `deprecation_policy_defined`, `has_breaking_change`
  - `API-CDC-*`: `consumer_matrix_current`, `ci_blocking_enabled`
- `API-VER-*` and `API-CDC-*` require `compatibility_matrix` with:
  - `supported_producer_versions`
  - `tested_consumers`
- `API-VER-*` with `checks.has_breaking_change = true` requires `deprecation_plan` with:
  - `target_version`
  - `deprecation_window_days`
  - `migration_guide_link`
- `API-CMP-*` requires `compliance_evidence` with:
  - `lawful_basis_or_contract`
  - `data_categories`
  - `retention_policy`
  - `cross_border_transfer_control`
  - `audit_log_location`

## Valid Manifest Templates
- `skills/api-design-rest/assets/api-res-manifest.valid.json`
- `skills/api-design-rest/assets/api-gql-manifest.valid.json`
- `skills/api-design-rest/assets/api-err-manifest.valid.json`
- `skills/api-design-rest/assets/api-ver-manifest.valid.json`
- `skills/api-design-rest/assets/api-cdc-manifest.valid.json`
- `skills/api-design-rest/assets/api-cmp-manifest.valid.json`

## Implementation Templates
- `skills/api-design-rest/assets/openapi-rest-template.yaml`
- `skills/api-design-rest/assets/graphql-schema-template.graphql`
- `skills/api-design-rest/assets/asyncapi-queue-template.yaml`
- `skills/api-design-rest/assets/websocket-message-contract-template.yaml`
- `skills/api-design-rest/assets/sse-event-contract-template.yaml`
- `skills/api-design-rest/assets/api-error-catalog-template.yaml`
- `skills/api-design-rest/assets/api-versioning-policy-template.md`
- `skills/api-design-rest/assets/api-contract-test-matrix-template.yaml`

## Gate Policy
- Block release when ID schema, state, or approver requirements fail.
- Block release when decision context omits transport rationale or threshold derivation methods.
- Block release when required compatibility evidence is missing.
- Block release when breaking changes have no deprecation plan.
- Block release when API-CMP evidence is incomplete.
