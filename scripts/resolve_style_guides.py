#!/usr/bin/env python3
"""Resolve applicable *-style-guide skills from changed file paths."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path, PurePosixPath

BASH = "bash-style-guide"
CSHARP = "csharp-style-guide"
GO = "go-style-guide"
JAVA = "java-style-guide"
JAVASCRIPT = "javascript-style-guide"
POWERSHELL = "powershell-style-guide"
PYTHON = "python-style-guide"
RUST = "rust-style-guide"
SH = "sh-style-guide"
SQL = "sql-style-guide"
TERRAFORM = "terraform-style-guide"
TYPESCRIPT = "typescript-style-guide"
ZSH = "zsh-style-guide"

JAVASCRIPT_EXTENSIONS = {".js", ".jsx", ".mjs", ".cjs"}
TYPESCRIPT_EXTENSIONS = {".ts", ".tsx", ".d.ts"}
CSHARP_EXTENSIONS = {".cs", ".csproj", ".sln", ".props", ".targets", ".razor"}
POWERSHELL_EXTENSIONS = {".ps1", ".psm1", ".psd1"}
ZSH_FILENAMES = {".zshrc", ".zprofile", ".zshenv", ".zlogin", ".zlogout"}

SHARED_JS_TS_CONFIG_BASENAMES = {
    "package.json",
    "package-lock.json",
    "pnpm-lock.yaml",
    "yarn.lock",
    ".eslintrc",
    ".prettierrc",
    ".babelrc",
    ".stylelintrc",
    ".commitlintrc",
    ".lintstagedrc",
    ".lint-stagedrc",
    ".biomerc",
    "biome.json",
    "biome.jsonc",
    "turbo.json",
    "rome.json",
    "rome.jsonc",
    "lint-staged.config.js",
    "lint-staged.config.cjs",
    "lint-staged.config.mjs",
    "lint-staged.config.ts",
    "lint-staged.config.cts",
    "lint-staged.config.mts",
}

SHARED_JS_TS_CONFIG_FILENAME_SUFFIXES = (
    ".config.js",
    ".config.cjs",
    ".config.mjs",
    ".config.ts",
    ".config.cts",
    ".config.mts",
)

SHARED_JS_TS_RC_PREFIXES = (
    ".eslintrc",
    ".prettierrc",
    ".babelrc",
    ".stylelintrc",
    ".commitlintrc",
    ".lintstagedrc",
    ".lint-stagedrc",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Resolve code-style skills for changed files")
    parser.add_argument("paths", nargs="*", help="Changed file paths")
    parser.add_argument(
        "--from-stdin",
        action="store_true",
        help="Read newline-delimited changed paths from stdin",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON output",
    )
    return parser.parse_args()


def load_paths(args: argparse.Namespace) -> list[str]:
    paths = list(args.paths)
    if args.from_stdin:
        import sys

        paths.extend(line.strip() for line in sys.stdin if line.strip())

    if not paths:
        raise SystemExit("no changed paths provided; pass paths or use --from-stdin")

    return paths


def looks_like_shared_js_ts_config(path: PurePosixPath) -> bool:
    name = path.name.lower()
    if name in SHARED_JS_TS_CONFIG_BASENAMES:
        return True

    if any(name.endswith(suffix) for suffix in SHARED_JS_TS_CONFIG_FILENAME_SUFFIXES):
        return True

    return any(name == prefix or name.startswith(f"{prefix}.") for prefix in SHARED_JS_TS_RC_PREFIXES)


def has_shebang(path: PurePosixPath, prefixes: tuple[str, ...]) -> bool:
    file_path = Path(path)
    if not file_path.exists() or not file_path.is_file():
        return False

    try:
        first_line = file_path.read_text(encoding="utf-8").splitlines()[0]
    except (UnicodeDecodeError, IndexError):
        return False

    return any(first_line.startswith(prefix) for prefix in prefixes)


def has_bash_shebang(path: PurePosixPath) -> bool:
    return has_shebang(path, ("#!/usr/bin/env bash", "#!/bin/bash"))


def has_sh_shebang(path: PurePosixPath) -> bool:
    return has_shebang(path, ("#!/usr/bin/env sh", "#!/bin/sh"))


def has_zsh_shebang(path: PurePosixPath) -> bool:
    return has_shebang(path, ("#!/usr/bin/env zsh", "#!/bin/zsh"))


def is_ci_workflow_file(path: PurePosixPath) -> bool:
    if path.suffix.lower() not in {".yml", ".yaml"}:
        return False

    parts = [part.lower() for part in path.parts]
    return ".github" in parts and "workflows" in parts


def workflow_shell_hints(path: PurePosixPath) -> set[str]:
    hints: set[str] = set()
    file_path = Path(path)

    if not is_ci_workflow_file(path) or not file_path.exists() or not file_path.is_file():
        return hints

    try:
        text = file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return hints

    if re.search(r"(?im)^\s*shell\s*:\s*(?:bash|/bin/bash)(?:\s+\{0\})?\s*$", text):
        hints.add(BASH)

    if re.search(r"(?im)^\s*shell\s*:\s*(?:sh|/bin/sh)(?:\s+\{0\})?\s*$", text):
        hints.add(SH)

    if re.search(r"(?im)^\s*shell\s*:\s*(?:zsh|/bin/zsh)(?:\s+\{0\})?\s*$", text):
        hints.add(ZSH)

    if re.search(r"(?im)^\s*shell\s*:\s*(?:pwsh|powershell)(?:\s+\{0\})?\s*$", text):
        hints.add(POWERSHELL)

    return hints


def resolve_skills(changed_paths: list[str]) -> list[str]:
    resolved: set[str] = set()

    js_code_changed = False
    ts_code_changed = False
    shared_js_ts_config_changed = False

    for raw_path in changed_paths:
        normalized_raw_path = raw_path.replace("\\", "/")
        path = PurePosixPath(normalized_raw_path)
        suffix = path.suffix.lower()
        name = path.name
        name_lower = name.lower()
        shared_config = looks_like_shared_js_ts_config(path)
        workflow_hints = workflow_shell_hints(path)

        if workflow_hints:
            resolved.update(workflow_hints)

        bash_shebang = has_bash_shebang(path)
        sh_shebang = has_sh_shebang(path)
        zsh_shebang = has_zsh_shebang(path)

        if suffix == ".sh":
            if bash_shebang:
                resolved.add(BASH)
            elif sh_shebang:
                resolved.add(SH)
            elif zsh_shebang:
                # Explicit zsh shebang is unambiguous even when extension is `.sh`.
                pass
            else:
                # `.sh` without explicit shebang is ambiguous; run both shell style guides.
                resolved.add(BASH)
                resolved.add(SH)
        else:
            if bash_shebang:
                resolved.add(BASH)
            if sh_shebang:
                resolved.add(SH)

        if suffix == ".zsh" or name_lower in ZSH_FILENAMES or zsh_shebang:
            resolved.add(ZSH)

        if suffix in POWERSHELL_EXTENSIONS:
            resolved.add(POWERSHELL)

        if suffix in CSHARP_EXTENSIONS or name_lower in CSHARP_EXTENSIONS:
            resolved.add(CSHARP)

        if suffix == ".go" or name_lower in {"go.mod", "go.sum", "go.work"}:
            resolved.add(GO)

        if suffix == ".java" or name_lower in {"pom.xml", "build.gradle", "build.gradle.kts"}:
            resolved.add(JAVA)

        if suffix in JAVASCRIPT_EXTENSIONS and not shared_config:
            js_code_changed = True

        if (
            suffix == ".py"
            or name_lower == "pyproject.toml"
            or name_lower.startswith("requirements")
            and suffix == ".txt"
            or name_lower == "uv.lock"
        ):
            resolved.add(PYTHON)

        if suffix == ".rs" or name_lower in {"cargo.toml", "cargo.lock"}:
            resolved.add(RUST)

        if suffix == ".sql":
            resolved.add(SQL)

        if suffix in {".tf", ".tfvars"} or name_lower in {"terraform.tfvars", "terraform.tfvars.json"}:
            resolved.add(TERRAFORM)

        if (
            suffix in TYPESCRIPT_EXTENSIONS
            or name_lower.endswith(".d.ts")
            or name_lower.startswith("tsconfig")
            and suffix == ".json"
        ):
            ts_code_changed = True

        if shared_config:
            shared_js_ts_config_changed = True

    if ts_code_changed:
        resolved.add(TYPESCRIPT)
    if js_code_changed:
        resolved.add(JAVASCRIPT)

    if shared_js_ts_config_changed and js_code_changed and ts_code_changed:
        resolved.add(JAVASCRIPT)
        resolved.add(TYPESCRIPT)

    return sorted(resolved)


def main() -> int:
    args = parse_args()
    changed_paths = load_paths(args)
    skills = resolve_skills(changed_paths)

    if args.json:
        print(json.dumps({"skills": skills}, ensure_ascii=False))
    else:
        for skill in skills:
            print(skill)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
