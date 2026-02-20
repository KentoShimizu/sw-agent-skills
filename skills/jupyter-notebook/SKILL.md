---
name: jupyter-notebook
description: "Notebook delivery workflow for software teams requiring reproducible execution, clear narrative, and shareable evidence. Use when analysis, experiment, or verification results must be delivered as executable notebook artifacts; do not use for product requirement prioritization or architecture topology selection."
---

# Jupyter Notebook

## Overview
Use this skill to produce notebooks another engineer can execute and trust without hidden assumptions.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- Notebook structure guidance:
  - `references/notebook-structure.md`
- Reproducibility and sanitization rules:
  - `references/reproducibility-and-sanitization-rules.md`

## Templates And Assets
- Notebook run log template:
  - `assets/notebook-run-log-template.md`
- Notebook result summary template:
  - `assets/notebook-summary-template.md`
- Delivery checklist:
  - `assets/notebook-delivery-checklist.md`

## Inputs To Gather
- Notebook purpose (`exploration`, `debug`, `tutorial`, `verification`).
- Runtime constraints (Python version, package policy, data access).
- Expected deliverable shape (single notebook or multi-notebook set).
- Sharing boundary (internal-only vs external audience).

## Deliverables
- Executable notebook with deterministic order.
- Runtime/dependency assumptions and execution log.
- Decision-grade summary linked to output cells.
- Sanitized artifact for sharing when required.

## Workflow
1. Define audience, decision question, and reproducibility constraints.
2. Create scaffold with `scripts/new_notebook.py` when useful.
3. Structure notebook sections per `references/notebook-structure.md`.
4. Execute from fresh kernel and record results in `assets/notebook-run-log-template.md`.
5. Summarize findings with `assets/notebook-summary-template.md`.
6. Validate shareability via `assets/notebook-delivery-checklist.md`.

## Scripts
- Create experiment scaffold:
  - `python3 scripts/new_notebook.py --kind experiment --title 'My Experiment' --out output/notebooks/my-experiment.ipynb`
- Create tutorial scaffold:
  - `python3 scripts/new_notebook.py --kind tutorial --title 'My Tutorial' --out output/notebooks/my-tutorial.ipynb`

## Quality Standard
- Notebook runs top-to-bottom from fresh kernel.
- Claims are tied to explicit output evidence.
- Runtime and data assumptions are reproducible.
- Shared outputs are sanitized for secrets and personal data.

## Failure Conditions
- Stop when runtime/data preconditions cannot be specified precisely.
- Stop when repeated runs produce unstable outputs without explanation.
- Stop external sharing when sensitive output cannot be sanitized.
