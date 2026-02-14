# CODEOWNERS Patterns

## Recommended Layout
1. Broad defaults first for non-critical paths.
2. Specific sensitive paths next (`.github/workflows/`, `infra/`, auth code).
3. Catch-all `*` at the end only.

## Stable Patterns
- `/apps/web/* @frontend-team @web-backup`
- `/services/api/* @backend-team @api-backup`
- `/.github/workflows/* @platform-team @security-team`
- `/infra/* @platform-team @infra-backup`
- `* @default-maintainers`

## Anti-Patterns
- Catch-all `*` before specific paths.
- Unowned sensitive directories.
- Pattern duplication with conflicting owners.
- Stale owners that no longer exist.

## Governance Tips
- Review CODEOWNERS on every team or directory reorg.
- Validate with PR samples, not only static linting.
- Keep at least two maintainers for critical paths.
- Use lint mode `--policy team` for strict team operation, or `--policy github` when repository follows GitHub-native semantics.
