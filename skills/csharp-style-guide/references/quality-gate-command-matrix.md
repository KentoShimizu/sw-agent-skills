# Quality Gate Command Matrix

## Purpose
Use this matrix to run check-only CI gates and optional local autofix commands consistently across all `*-style-guide` skills.

| Skill | CI required (check-only) | Optional local autofix |
| --- | --- | --- |
| `bash-style-guide` | `shellcheck`<br>`shfmt -d`<br>`bats test/` (or project test path) | `shfmt -w` |
| `sh-style-guide` | `shellcheck -s sh`<br>`shfmt -d -ln posix`<br>`shunit2`/project shell tests | `shfmt -w -ln posix` |
| `zsh-style-guide` | `zsh -n` (syntax check)<br>`shellcheck` where applicable<br>`zunit`/project shell tests | formatter/lint autofix where project tooling supports it |
| `powershell-style-guide` | `Invoke-ScriptAnalyzer` (fail on issues)<br>`Invoke-Formatter -Check` (or repo equivalent)<br>`Invoke-Pester` | `Invoke-Formatter`<br>`Invoke-ScriptAnalyzer -Fix` |
| `csharp-style-guide` | `dotnet format --verify-no-changes`<br>`dotnet build -warnaserror`<br>`dotnet test` | `dotnet format` |
| `go-style-guide` | `gofmt -l .` (empty output)<br>`go vet ./...`<br>`staticcheck ./...` (if available)<br>`go test ./... -race` | `gofmt -w .` or `go fmt ./...` |
| `java-style-guide` | `spotlessCheck` (or equivalent formatter check)<br>`checkstyle`/configured lint<br>`errorprone`/`spotbugs` (if configured)<br>`./gradlew test` or `mvn test` | `spotlessApply` (or project formatter autofix) |
| `javascript-style-guide` | `prettier --check .`<br>`eslint . --max-warnings=0`<br>`npm test`/`pnpm test` | `prettier --write .`<br>`eslint . --fix` |
| `python-style-guide` | `uv run ruff format --check .`<br>`uv run ruff check .`<br>`uv run mypy .` (or project equivalent)<br>`uv run pytest -q` | `uv run ruff format .`<br>`uv run ruff check --fix .` |
| `rust-style-guide` | `cargo fmt --all -- --check`<br>`cargo clippy --all-targets --all-features -- -D warnings`<br>`cargo test --all-targets --all-features` | `cargo fmt --all` |
| `sql-style-guide` | `sqlfluff lint` (or project check-only linter)<br>migration validation in CI/staging<br>critical query plan verification | `sqlfluff fix` |
| `terraform-style-guide` | `terraform fmt -check -recursive`<br>`terraform validate`<br>`tflint`<br>`tfsec`/`checkov` | `terraform fmt -recursive` |
| `typescript-style-guide` | `prettier --check .`<br>`eslint . --max-warnings=0`<br>`tsc --noEmit`<br>`pnpm test`/`npm test` | `prettier --write .`<br>`eslint . --fix` |

## Notes
- Keep CI gates check-only; fail the pipeline on violations.
- Run autofix commands locally, then rerun check-only commands before merge.
- Prefer project-specific wrappers when repositories define standardized task runners.
