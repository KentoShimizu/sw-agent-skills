# Trigger Matrix

## Purpose
Use this matrix as the canonical trigger reference for `*-style-guide` skills.
When multiple rows match in a single pull request, activate all matched skills.

## Primary Mapping
| Changed artifacts | Trigger skill(s) | Notes |
| --- | --- | --- |
| `.sh` files without explicit shebang, files with `#!/usr/bin/env bash` / `#!/bin/bash`, or workflow files containing `shell: bash` | `bash-style-guide` | Do not infer Bash from directory names alone. |
| Files with `#!/usr/bin/env sh` / `#!/bin/sh`, or workflow files containing `shell: sh` | `sh-style-guide` | Use for POSIX `sh` compatibility and portability-focused checks. |
| `.zsh`, `.zshrc`, `.zprofile`, `.zshenv`, `.zlogin`, `.zlogout`, files with `#!/usr/bin/env zsh` / `#!/bin/zsh`, or workflow files containing `shell: zsh` | `zsh-style-guide` | Use for Zsh-specific syntax and behavior. |
| `.ps1`, `.psm1`, `.psd1`, or workflow files containing `shell: pwsh` / `shell: powershell` | `powershell-style-guide` | Scope is PowerShell syntax and runtime behavior. |
| `.cs`, `.csproj`, `.sln`, `.props`, `.targets`, `.razor` | `csharp-style-guide` | Applies to C#/.NET source and build artifacts. |
| `.go`, `go.mod`, `go.sum`, `go.work` | `go-style-guide` | Applies to Go modules and workspace config. |
| `.java`, Java modules in `pom.xml` / `build.gradle` / `build.gradle.kts` | `java-style-guide` | Java scope only; Kotlin-only modules are out of scope. |
| `.js`, `.jsx`, `.mjs`, `.cjs` | `javascript-style-guide` | Excludes TypeScript-owned modules. |
| `.py`, `pyproject.toml`, `requirements*.txt`, `uv.lock` | `python-style-guide` | Python runtime and packaging scope. |
| `.rs`, `Cargo.toml`, `Cargo.lock` | `rust-style-guide` | Rust crates and binaries. |
| `.sql`, migration directories, schema/query template files | `sql-style-guide` | Can co-activate with language style guides. |
| `.tf`, `.tfvars`, Terraform module/workflow files | `terraform-style-guide` | Can co-activate with application style guides. |
| `.ts`, `.tsx`, `.d.ts`, `tsconfig*.json` | `typescript-style-guide` | TypeScript owns `tsconfig`-scoped modules. |

## Shared JS/TS Configuration Rule
- For shared JS/TS config files (for example `package.json`, shared ESLint/test/prettier config):
  - Activate both `javascript-style-guide` and `typescript-style-guide` when both JS and TS artifacts are changed in the same pull request.
  - If only TS artifacts are changed, activate `typescript-style-guide`.
  - If only JS artifacts are changed, activate `javascript-style-guide`.

## Co-activation Rules
1. In multi-language pull requests, run all matched `*-style-guide` skills.
2. SQL changes do not suppress language-specific style guides.
3. Terraform changes do not suppress application language style guides.
4. If no language/IaC/SQL artifacts match this matrix, do not auto-activate a code-style skill.
