#!/usr/bin/env python3
"""Unit tests for absolute-path leak validation defaults."""

from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "validate_no_absolute_paths.py"
MODULE_NAME = "validate_no_absolute_paths_module"


def load_validator_module():
    spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"failed to load module spec: {MODULE_PATH}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[MODULE_NAME] = module
    spec.loader.exec_module(module)
    return module


class ValidateNoAbsolutePathsDefaultsTest(unittest.TestCase):
    def test_default_patterns_scan_references_markdown(self) -> None:
        module = load_validator_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            reference_doc = root / "references" / "guide.md"
            reference_doc.parent.mkdir(parents=True, exist_ok=True)
            leaked_path = "/" + "Users/example/workspace/private-file"
            reference_doc.write_text(
                f"non-portable sample path: {leaked_path}\n",
                encoding="utf-8",
            )

            findings = module.find_host_absolute_paths(
                root=root,
                patterns=module.DEFAULT_PATTERNS,
            )

            self.assertTrue(findings, "expected absolute-path finding under references/**/*.md")
            self.assertTrue(
                any(finding.file == reference_doc for finding in findings),
                "expected finding to point to references/guide.md",
            )


if __name__ == "__main__":
    unittest.main()
