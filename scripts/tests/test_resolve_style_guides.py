#!/usr/bin/env python3
"""Table-driven tests for style-guide routing resolution."""

from __future__ import annotations

import importlib.util
import sys
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
        ]

        for case_name, changed_paths, expected in cases:
            with self.subTest(case_name=case_name):
                actual = resolve_skills(changed_paths)
                self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
