---
name: bash-style-guide
description: "Style, review, and refactoring standards for Bash shell scripting. Use when editing or reviewing Bash artifacts such as `.sh` files, files with a Bash shebang (`#!/usr/bin/env bash` or `#!/bin/bash`), or CI script blocks explicitly executed by Bash. Do not use for generic POSIX `sh`, PowerShell, or language-specific application style rules. In multi-language pull requests, run together with other applicable `*-style-guide` skills."
---

# Bash Style Guide

Apply this checklist when writing or reviewing bash code.

## Trigger Reference

- Use `references/trigger-matrix.md` as the canonical trigger and co-activation matrix.
- Resolve skill activation from changed files with `python3 scripts/resolve_style_guides.py <changed-path>...` when automation is available.
- Validate trigger matrix consistency with `python3 scripts/validate_trigger_matrix_sync.py`.

## Structure and readability
## Quality Gate Reference

- Use `references/quality-gate-command-matrix.md` for CI check-only vs local autofix command mapping.

1. Start scripts with `#!/usr/bin/env bash` and strict mode: `set -euo pipefail`.
2. Use small functions with one responsibility; keep `main` orchestration-focused.
3. Keep constants uppercase (`MAX_RETRIES`) and local variables lowercase (`retry_count`).
4. Use `local` in functions to avoid leaking state.
5. Document non-obvious command pipelines with short intent comments.

## Data handling and quoting

1. Quote expansions by default: `"${var}"`, `"${array[@]}"`.
2. Use arrays for argument lists; avoid string-concatenated command assembly.
3. Replace magic numbers with named constants and include units in names (`TIMEOUT_SECONDS`).
4. Avoid `eval`; treat it as a security-sensitive last resort.
5. Fail early for required environment variables:
   - `: "${API_TOKEN:?API_TOKEN is required}"`
   - Do not provide silent fallback defaults for required config.

## Error handling and control flow

1. Return explicit non-zero exit codes for expected failure modes.
2. Use `trap` for cleanup and emit actionable error messages.
3. Handle command failures intentionally (`if ! cmd; then ... fi`) instead of masking them.
4. Avoid broad `|| true`; suppress failures only with explicit rationale.
5. Let failures surface when root cause should be fixed, not hidden.

## Security and operational safety

1. Treat all external input as untrusted; validate before use.
2. Use `--` before positional paths in destructive commands (`rm -- "$target"`).
3. Avoid unbounded globbing and unsafe temporary file handling; prefer `mktemp`.
4. Minimize secret exposure in logs; never echo credentials.
5. Use least-privilege command execution and avoid unnecessary `sudo`.

## Performance and scalability

1. Avoid spawning subshells inside tight loops when builtins suffice.
2. Prefer single-pass text processing over repeated `grep | awk | sed` chains.
3. Batch filesystem operations where possible.
4. Add bounded retry loops with explicit backoff constants.

## Testing and verification

1. Add `bats` tests for critical functions and failure paths.
2. Cover edge cases: empty input, whitespace paths, missing env vars, command timeouts.
3. Document manual verification for system-dependent behavior.
4. Verify scripts are idempotent when run repeatedly.

## CI required quality gates (check-only)

1. Run `shellcheck` with warnings treated as actionable.
2. Run `shfmt -d` (or equivalent check mode) and require zero diff.
3. Run test suite (for example `bats test/`).
4. Reject changes with implicit behavior that obscures failures.

## Optional autofix commands (local)

1. Run `shfmt -w` to apply formatting.
2. Apply safe mechanical fixes suggested by `shellcheck` and re-run checks.
