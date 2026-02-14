---
name: jupyter-notebook
description: "Notebook delivery workflow for software teams. Use when test or evidence artifacts are the primary output for verification; do not use for product requirement prioritization or architecture topology selection."
---

# Jupyter Notebook

## Trigger Boundary
- Use when work output is expected as executable notebook artifacts.
- Do not use for production service implementation tasks.
- Do not use for document-only deliverables with no executable cells.

## Goal
Ship notebooks that can be executed end-to-end by another engineer without hidden assumptions.

## Inputs
- Notebook purpose (`exploration`, `debug`, `tutorial`)
- Runtime constraints (Python version, package policy, data access)
- Expected deliverable shape (single notebook or multi-notebook set)

## Outputs
- Notebook file with deterministic execution order
- Runtime preconditions and dependency declaration notes
- Result summary linked to cell outputs

## Workflow
1. Define target audience and the decision this notebook must support.
2. Build a minimal section layout: context, setup, execution, interpretation.
3. Keep one intent per code cell; avoid multi-purpose cells.
4. Add explicit environment cells (imports, version checks, seed settings).
5. Execute all cells top-to-bottom and record non-reproducible constraints.

## Scripts
- Create experiment scaffold:
  - `python3 scripts/new_notebook.py --kind experiment --title 'My Experiment' --out output/notebooks/my-experiment.ipynb`
- Create tutorial scaffold:
  - `python3 scripts/new_notebook.py --kind tutorial --title 'My Tutorial' --out output/notebooks/my-tutorial.ipynb`

## Quality Gates
- Notebook runs from a fresh kernel without manual fixups.
- Cell order reflects dependency order; no hidden state usage.
- Result claims are tied to visible output cells.
- External dependencies and data assumptions are explicit.
- If shared outside local development scope, outputs are sanitized for secrets and personal data.

## Failure Handling
- Stop when required data or runtime cannot be specified precisely.
- Escalate when outputs are unstable across repeated executions.
- Stop external sharing when sensitive output cannot be sanitized safely.

## References
- `references/notebook-structure.md`
