# Notebook Structure Guidelines

## Core Sections
1. Context and objective
2. Environment setup
3. Data/input preparation
4. Main analysis or execution
5. Findings and decisions

## Execution Rules
- Notebook must run from a fresh kernel.
- Do not rely on hidden state from manual cell execution order.
- Keep one intent per code cell.

## Output Hygiene
- Keep outputs short and readable.
- For external sharing, remove secrets and personal data from outputs.
- Prefer summary tables over large raw dumps.

## Review Checklist
- Reproducible start-to-end run
- Clear explanation of assumptions
- Results linked to concrete outputs
- Follow-up tasks documented
