#!/usr/bin/env python3
"""Table-driven tests for style-guide routing resolution."""

from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "resolve_style_guides.py"
MODULE_NAME = "resolve_style_guides_module"


def load_resolver():
    spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"failed to load module spec: {MODULE_PATH}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[MODULE_NAME] = module
    spec.loader.exec_module(module)
    return module.resolve_skills


class ResolveStyleGuidesRoutingTest(unittest.TestCase):
    def test_table_driven_cases(self) -> None:
        resolve_skills = load_resolver()

        cases: list[tuple[str, list[str], list[str]]] = [
            (
                "docs_migration_plan_does_not_trigger_sql",
                ["docs/migration-plan.md"],
                [],
            ),
            (
                "migration_readme_does_not_trigger_sql",
                ["db/migrations/README.md"],
                [],
            ),
            (
                "db_migration_sql_triggers_sql",
                ["db/migrations/20260214_add_index.sql"],
                ["sql-style-guide"],
            ),
            (
                "package_json_only_does_not_trigger_js_or_ts",
                ["package.json"],
                [],
            ),
            (
                "shared_js_ts_config_only_does_not_trigger_js_or_ts",
                ["eslint.config.cjs"],
                [],
            ),
            (
                "named_js_source_does_not_get_suppressed_by_marker_words",
                ["src/jest_helpers.js", "src/babelize.js"],
                ["javascript-style-guide"],
            ),
            (
                "explicit_jest_config_is_treated_as_shared_config_only",
                ["jest.config.js"],
                [],
            ),
            (
                "mixed_js_ts_with_shared_config_triggers_both",
                ["src/app.ts", "web/app.js", "package.json"],
                ["javascript-style-guide", "typescript-style-guide"],
            ),
            (
                "powershell_script_triggers_powershell_style_guide",
                ["scripts/deploy.ps1"],
                ["powershell-style-guide"],
            ),
            (
                "ambiguous_sh_extension_triggers_bash_and_sh",
                ["scripts/deploy.sh"],
                ["bash-style-guide", "sh-style-guide"],
            ),
            (
                "zsh_extension_triggers_zsh_style_guide",
                ["scripts/deploy.zsh"],
                ["zsh-style-guide"],
            ),
        ]

        for case_name, changed_paths, expected in cases:
            with self.subTest(case_name=case_name):
                actual = resolve_skills(changed_paths)
                self.assertEqual(expected, actual)

    def test_ci_workflow_shell_hints_trigger_shell_specific_skills(self) -> None:
        resolve_skills = load_resolver()

        with tempfile.TemporaryDirectory() as temp_dir:
            workflow_dir = Path(temp_dir) / ".github" / "workflows"
            workflow_dir.mkdir(parents=True, exist_ok=True)

            bash_workflow = workflow_dir / "bash-ci.yml"
            bash_workflow.write_text(
                "jobs:\n"
                "  test:\n"
                "    runs-on: ubuntu-latest\n"
                "    steps:\n"
                "      - run: echo hello\n"
                "        shell: bash\n",
                encoding="utf-8",
            )

            powershell_workflow = workflow_dir / "pwsh-ci.yml"
            powershell_workflow.write_text(
                "jobs:\n"
                "  test:\n"
                "    runs-on: windows-latest\n"
                "    steps:\n"
                "      - run: Write-Host 'hello'\n"
                "        shell: pwsh\n",
                encoding="utf-8",
            )

            sh_workflow = workflow_dir / "sh-ci.yml"
            sh_workflow.write_text(
                "jobs:\n"
                "  test:\n"
                "    runs-on: ubuntu-latest\n"
                "    steps:\n"
                "      - run: echo hello\n"
                "        shell: sh\n",
                encoding="utf-8",
            )

            zsh_workflow = workflow_dir / "zsh-ci.yml"
            zsh_workflow.write_text(
                "jobs:\n"
                "  test:\n"
                "    runs-on: ubuntu-latest\n"
                "    steps:\n"
                "      - run: print hello\n"
                "        shell: zsh\n",
                encoding="utf-8",
            )

            actual = resolve_skills(
                [str(bash_workflow), str(powershell_workflow), str(sh_workflow), str(zsh_workflow)]
            )
            self.assertEqual(
                ["bash-style-guide", "powershell-style-guide", "sh-style-guide", "zsh-style-guide"],
                actual,
            )

    def test_extensionless_shebang_detection_for_shell_scripts(self) -> None:
        resolve_skills = load_resolver()

        with tempfile.TemporaryDirectory() as temp_dir:
            script_dir = Path(temp_dir) / "scripts"
            script_dir.mkdir(parents=True, exist_ok=True)

            sh_script = script_dir / "deploy-sh"
            sh_script.write_text("#!/bin/sh\necho hello\n", encoding="utf-8")

            zsh_script = script_dir / "deploy-zsh"
            zsh_script.write_text("#!/usr/bin/env zsh\nprint hello\n", encoding="utf-8")

            actual = resolve_skills([str(sh_script), str(zsh_script)])
            self.assertEqual(["sh-style-guide", "zsh-style-guide"], actual)


if __name__ == "__main__":
    unittest.main()
