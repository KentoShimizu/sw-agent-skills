---
name: git-history-investigation
description: "Specialized workflow for reconstructing change history using log, show, diff, and blame evidence. Use when Git history, branching, synchronization, or recovery workflows are the core concern; do not use for CI workflow design or application behavior implementation."
---

# Git History Investigation

## Trigger Boundary
- Use when regressions, ownership questions, or behavioral drift require historical analysis.
- Do not use for binary-search regression isolation; use `git-bisect-debugging`.
- Do not use for security-only threat analysis; use `security-threat-modeling`.

## Goal
Find the commit-level root cause and decision context behind observed behavior.

## Shared Git Contract (Canonical)
- Use `../git-branch-strategy/references/git-governance-contract.md` as the single schema and gate source.
- Track investigation artifacts with `GIT-HIS-*` IDs.
- Run machine validation: `python3 ../git-branch-strategy/scripts/validate_git_contract.py --manifest <path/to/manifest.json>`.

## Inputs
- Reproducible symptom or unexpected behavior
- Candidate file paths, modules, or time window
- Available issue, PR, or review metadata

## Outputs
- `GIT-HIS-*` chronological evidence trail
- Root-cause candidate commit set with rationale
- Follow-up remediation recommendation

## Workflow
1. Narrow scope by file path, author, and date window.
2. Inspect commit diffs and messages for behavioral shifts.
3. Cross-reference blame data with review and issue context.
4. Validate candidate root cause against symptom timeline.
5. Publish findings with confidence level and contract validation evidence.

## Quality Gates
- Evidence chain links symptom to specific commit behavior.
- Root-cause claim includes reproducible supporting data.
- Alternative hypotheses are documented and ruled out.
- Follow-up actions target root causes, not only symptoms.

## Failure Handling
- Stop when symptom cannot be reproduced or scoped.
- Escalate when history evidence is insufficient for a high-confidence claim.
