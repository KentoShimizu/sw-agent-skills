#!/usr/bin/env python3
"""Create a fresh Jupyter notebook scaffold."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def markdown_cell(text: str) -> dict[str, object]:
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + "\n" for line in text.splitlines()],
    }


def code_cell(text: str) -> dict[str, object]:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [line + "\n" for line in text.splitlines()],
    }


def build_notebook(kind: str, title: str) -> dict[str, object]:
    intro = markdown_cell(f"# {title}\n\nKind: `{kind}`")
    setup = code_cell(
        "import sys\n"
        "print('python', sys.version)\n"
    )

    if kind == "experiment":
        purpose = markdown_cell("## Hypothesis\n\n- State the hypothesis and measurable outcome.")
        body = code_cell("# Add experiment code here")
        result = markdown_cell("## Findings\n\n- Summarize observations and decisions.")
    else:
        purpose = markdown_cell("## Learning Goals\n\n- State what the reader should learn.")
        body = code_cell("# Add tutorial code steps here")
        result = markdown_cell("## Wrap-Up\n\n- Summarize key takeaways and next steps.")

    return {
        "cells": [intro, purpose, setup, body, result],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "name": "python",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a notebook scaffold")
    parser.add_argument("--kind", choices=["experiment", "tutorial"], required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    out_path = Path(args.out)
    if out_path.exists() and not args.force:
        print(f"output already exists: {out_path}", file=sys.stderr)
        return 2

    out_path.parent.mkdir(parents=True, exist_ok=True)
    notebook = build_notebook(args.kind, args.title)
    out_path.write_text(json.dumps(notebook, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(str(out_path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
