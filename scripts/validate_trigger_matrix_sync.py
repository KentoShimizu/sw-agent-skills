#!/usr/bin/env python3
"""Validate consistency between style-guide trigger descriptions and trigger matrix files."""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
    from yaml import YAMLError
except ModuleNotFoundError:  # pragma: no cover - optional dependency path
    yaml = None

    class YAMLError(Exception):
        """Fallback error type when PyYAML is unavailable."""

SKILLS_ROOT = Path("skills")
TRIGGER_MATRIX_RELATIVE = Path("references/trigger-matrix.md")

EXPECTED_DESCRIPTION_TOKENS: dict[str, tuple[str, ...]] = {
    "bash-style-guide": (".sh", "#!/usr/bin/env bash", "#!/bin/bash"),
    "csharp-style-guide": (".cs", ".csproj", ".sln", ".props", ".targets", ".razor"),
    "go-style-guide": (".go", "go.mod", "go.sum", "go.work"),
    "java-style-guide": (".java", "pom.xml", "build.gradle", "build.gradle.kts"),
    "javascript-style-guide": (".js", ".jsx", ".mjs", ".cjs", "typescript-style-guide"),
    "python-style-guide": (".py", "pyproject.toml", "requirements*.txt", "uv.lock"),
    "rust-style-guide": (".rs", "Cargo.toml", "Cargo.lock"),
    "sql-style-guide": (".sql",),
    "terraform-style-guide": (".tf", ".tfvars"),
    "typescript-style-guide": (".ts", ".tsx", ".d.ts", "tsconfig*.json", "javascript-style-guide"),
}

MATRIX_SKILL_PATTERN = re.compile(r"\|[^|]+\|\s*`([a-z0-9-]+-style-guide)`\s*\|")


FRONTMATTER_PATTERN = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
BLOCK_SCALAR_MARKERS = {"|", ">", "|-", ">-", "|+", ">+"}


def unquote_yaml_scalar(value: str) -> str:
    stripped = value.strip()
    if len(stripped) >= 2 and stripped[0] == stripped[-1] and stripped[0] in {"'", '"'}:
        return stripped[1:-1]
    return stripped


def parse_frontmatter_without_pyyaml(frontmatter_text: str) -> dict[str, object] | None:
    lines = frontmatter_text.splitlines()
    index = 0
    parsed: dict[str, object] = {}

    while index < len(lines):
        line = lines[index]
        index += 1

        if not line.strip() or line.lstrip().startswith("#"):
            continue

        match = re.match(r"^([A-Za-z0-9_-]+)\s*:\s*(.*)$", line)
        if not match:
            continue

        key = match.group(1)
        value = match.group(2).strip()

        if value in BLOCK_SCALAR_MARKERS:
            block_lines: list[str] = []
            while index < len(lines):
                block_line = lines[index]
                if block_line.startswith(("  ", "\t")):
                    block_lines.append(block_line.lstrip())
                    index += 1
                    continue
                if not block_line.strip():
                    block_lines.append("")
                    index += 1
                    continue
                break

            parsed[key] = " ".join(part.strip() for part in block_lines if part.strip())
            continue

        parsed[key] = unquote_yaml_scalar(value)

    return parsed if parsed else None


def parse_frontmatter_yaml(text: str) -> dict[str, object] | None:
    normalized_text = text.replace("\r\n", "\n")
    if not normalized_text.startswith("---\n"):
        return None

    match = FRONTMATTER_PATTERN.match(normalized_text)
    if match is None:
        return None

    frontmatter_text = match.group(1)
    if yaml is not None:
        try:
            loaded = yaml.safe_load(frontmatter_text)
        except YAMLError:
            loaded = None
        if isinstance(loaded, dict):
            return loaded

    return parse_frontmatter_without_pyyaml(frontmatter_text)


def validate_matrix_content(style_dirs: list[Path]) -> list[str]:
    errors: list[str] = []
    canonical_file = style_dirs[0] / TRIGGER_MATRIX_RELATIVE

    if not canonical_file.exists():
        errors.append(f"missing canonical trigger matrix: {canonical_file}")
        return errors

    canonical_text = canonical_file.read_text(encoding="utf-8")

    declared_skills = set(MATRIX_SKILL_PATTERN.findall(canonical_text))
    expected_skills = {path.name for path in style_dirs}
    if declared_skills != expected_skills:
        errors.append(
            "trigger matrix skill rows do not match style-guide set: "
            f"declared={sorted(declared_skills)} expected={sorted(expected_skills)}"
        )

    for style_dir in style_dirs[1:]:
        matrix_path = style_dir / TRIGGER_MATRIX_RELATIVE
        if not matrix_path.exists():
            errors.append(f"missing trigger matrix: {matrix_path}")
            continue

        text = matrix_path.read_text(encoding="utf-8")
        if text != canonical_text:
            errors.append(f"trigger matrix drift detected: {matrix_path}")

    return errors


def validate_skill_files(style_dirs: list[Path]) -> list[str]:
    errors: list[str] = []

    for style_dir in style_dirs:
        skill_name = style_dir.name
        skill_md = style_dir / "SKILL.md"

        if not skill_md.exists():
            errors.append(f"missing SKILL.md: {skill_md}")
            continue

        text = skill_md.read_text(encoding="utf-8")
        frontmatter = parse_frontmatter_yaml(text=text)
        if frontmatter is None:
            errors.append(f"frontmatter YAML not found or invalid: {skill_md}")
            continue

        description = frontmatter.get("description")
        if not isinstance(description, str):
            errors.append(f"frontmatter description not found or not a string: {skill_md}")
            continue

        if "references/trigger-matrix.md" not in text:
            errors.append(f"missing trigger-matrix reference in SKILL.md: {skill_md}")

        if "scripts/resolve_style_guides.py" not in text:
            errors.append(f"missing resolve_style_guides.py reference in SKILL.md: {skill_md}")

        expected_tokens = EXPECTED_DESCRIPTION_TOKENS.get(skill_name)
        if expected_tokens is None:
            errors.append(f"no expected description token mapping for {skill_name}")
            continue

        missing_tokens = [token for token in expected_tokens if token not in description]
        for token in missing_tokens:
            errors.append(f"description token missing in {skill_md}: {token}")

    return errors


def main() -> int:
    style_dirs = sorted(path for path in SKILLS_ROOT.glob("*-style-guide") if path.is_dir())
    if not style_dirs:
        print("validation=failed")
        print("- no *-style-guide directories found under skills/")
        return 1

    errors = validate_matrix_content(style_dirs)
    errors.extend(validate_skill_files(style_dirs))

    if errors:
        print("validation=failed")
        for error in errors:
            print(f"- {error}")
        return 1

    print("validation=ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
