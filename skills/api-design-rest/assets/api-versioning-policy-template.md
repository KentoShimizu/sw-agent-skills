# API Versioning Policy Template

## Scope
- API domain: `<set>`
- Audience: `internal | external | both`
- Transports: `rest | graphql | grpc | websocket | sse | queue`

## Version Channel
- Primary channel: `<uri | header | media-type | schema-tag | topic-version>`
- Version identifier format: `<set>`
- Backward compatibility baseline: `<set>`

## Breaking Change Criteria
- List additive changes treated as non-breaking.
- List breaking changes requiring migration and deprecation.
- Explicitly include status/error behavior changes.

## Support Window and Deprecation
- Minimum support window: `<set>`
- Minimum deprecation window (days): `<set>`
- Sunset communication channels: `<set>`
- Internal and external migration timelines (if different): `<set>`

## Migration Plan Requirements
- Migration guide location: `<set>`
- Compatibility matrix owner: `<set>`
- Rollback criteria and runbook link: `<set>`

## Governance and Gates
- Required approvers: `<set>`
- Required validation artifacts: `<set>`
- CI contract-testing gate: `<set>`
