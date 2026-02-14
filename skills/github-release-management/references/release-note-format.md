# Release Note Format

## Header
- Release version
- Release date
- Commit range

## Sections
- Breaking Changes
- Features
- Fixes
- Documentation
- Maintenance

## Entry Template
`- <summary> (<impact>) [<scope>]`

Example:
`- Add token-based session invalidation (auth hardening) [api]`

## Rules
- Mention user-visible impact first.
- Call out migrations or operator actions explicitly.
- Link issue/PR when available.
- Avoid internal-only noise unless it affects behavior.
