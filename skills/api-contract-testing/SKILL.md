---
name: api-contract-testing
description: "Consumer-provider contract testing workflow for validating API compatibility and preventing integration regressions. Use when executable provider-consumer compatibility checks are required between services; do not use for first-pass API shape design before contracts are defined."
---

# Api Contract Testing

## Trigger Boundary
- Use when API compatibility must be continuously validated between producers and consumers.
- Do not use for API schema design from scratch; use `api-design-*`.
- Do not use for end-to-end UI validation.

## Goal
Catch contract drift before deployment impacts consumers.

## Inputs
- Provider API specification and implementation
- Consumer expectations and critical integration cases
- Versioning and deprecation policy constraints

## Outputs
- Executable contract test suite definition
- Compatibility matrix by version and consumer
- Release gate criteria for contract compliance

## Workflow
1. Identify critical consumer-provider interaction contracts.
2. Define executable expectations with version scope.
3. Integrate contract checks into CI gates.
4. Validate backward compatibility and deprecation rules.
5. Publish failures with consumer impact and owner.

## Quality Gates
- Critical contracts are executable and version-scoped.
- CI blocks on incompatible contract changes.
- Failure reports identify impacted consumers clearly.
- Deprecation paths include migration guidance.

## Failure Handling
- Stop release when compatibility-breaking changes are unapproved.
- Escalate when contract ownership is ambiguous.
