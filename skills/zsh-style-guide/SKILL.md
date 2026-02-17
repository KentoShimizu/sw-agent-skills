---
name: zsh-style-guide
description: "Style, review, and refactoring standards for Zsh scripting. Trigger when `.zsh`, `.zshrc`, `.zprofile`, `.zshenv`, `.zlogin`, `.zlogout` files, files with `#!/usr/bin/env zsh` or `#!/bin/zsh`, or CI workflow blocks with `shell: zsh` are created, modified, or reviewed and Zsh-specific quality controls must be enforced. Do not use for POSIX `sh`, Bash-specific, or PowerShell-specific style rules. In multi-language pull requests, run together with other applicable `*-style-guide` skills."
---

# ZSH Style Guide

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

Use this skill to write and review Zsh scripts that intentionally rely on Zsh behavior while staying safe and maintainable.

## Trigger And Co-activation Reference

- If available, use `references/trigger-matrix.md` for canonical co-activation rules.
- If available, resolve style-guide activation from changed files with `python3 scripts/resolve_style_guides.py <changed-path>...`.
- If available, validate trigger matrix consistency with `python3 scripts/validate_trigger_matrix_sync.py`.

## Quality Gate Command Reference

- If available, use `references/quality-gate-command-matrix.md` for CI check-only and local autofix mapping.

## Quick Start Snippets

### Script skeleton for Zsh entrypoints

```zsh
#!/usr/bin/env zsh
set -euo pipefail

SCRIPT_NAME="${0:t}"
TEMP_DIR="$(mktemp -d)"

cleanup() {
  rm -rf -- "${TEMP_DIR}"
}

on_error() {
  local line_number="$1"
  local exit_code="$2"
  print -u2 -- "${SCRIPT_NAME}: failed at line ${line_number} (exit=${exit_code})"
}

trap cleanup EXIT
TRAPERR() {
  on_error "$LINENO" "$?"
}

main() {
  print -- "temp dir: ${TEMP_DIR}"
}

main "$@"
```

### Required environment variable check

```zsh
: "${API_TOKEN:?API_TOKEN is required}"
: "${API_BASE_URL:?API_BASE_URL is required}"
```

### Safe external command with arrays

```zsh
local -a curl_args=(
  --fail
  --silent
  --show-error
  --header "Authorization: Bearer ${API_TOKEN}"
  "${url}"
)

curl "${curl_args[@]}"
```

### Bounded retry helper

```zsh
typeset -ri MAX_ATTEMPTS=5
typeset -ri RETRY_DELAY_SECONDS=2

retry_command() {
  local -i attempt=1
  while (( attempt <= MAX_ATTEMPTS )); do
    if "$@"; then
      return 0
    fi

    if (( attempt == MAX_ATTEMPTS )); then
      print -u2 -- "command failed after ${MAX_ATTEMPTS} attempts"
      return 1
    fi

    sleep "${RETRY_DELAY_SECONDS}"
    (( attempt++ ))
  done
}
```

## Structure And Readability

1. Use explicit Zsh shebang for executable scripts.
2. Use strict mode for executable entrypoints.
3. Keep functions small and orchestration in `main`.
4. Use `local` and typed variables where it improves safety.
5. Keep comments short and focused on intent.

## Data Handling And Quoting

1. Quote parameter expansions by default.
2. Use arrays for argument safety.
3. Avoid `eval` unless unavoidable and validated.
4. Replace magic numbers with named constants including units.
5. Validate external input before command execution.

## Error Handling And Safety

1. Use explicit failure paths and non-zero return codes.
2. Use trap-based cleanup for temporary resources.
3. Avoid silent suppression patterns.
4. Fail early for missing required configuration.
5. Avoid exposing secrets in logs.

## Testing And Verification

1. Add shell tests (`zunit`/project equivalent) for core and failure paths.
2. Cover edge cases: empty input, whitespace paths, missing env vars, timeout/retry exhaustion.
3. Document manual verification when automation is insufficient.
4. Check idempotency for scripts run by automation.

## CI Required Quality Gates (check-only)

1. Run `zsh -n` on modified scripts.
2. Run lint checks configured by the repository (`shellcheck` where applicable).
3. Run shell tests (`zunit`/project equivalent).
4. Reject changes that hide failures or rely on implicit behavior.

## Optional Autofix Commands (local)

1. Run repository formatter/lint autofix commands where available.
2. Re-run all check-only gates after autofix.
