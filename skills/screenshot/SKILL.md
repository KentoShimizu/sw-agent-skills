---
name: screenshot
description: "Visual evidence capture workflow for software development. Use when test or evidence artifacts are the primary output for verification; do not use for product requirement prioritization or architecture topology selection."
---

# Screenshot

## Trigger Boundary
- Use when visual proof is required for engineering decisions or review comments.
- Do not use for DOM-level automation artifacts if browser tooling already captures equivalent evidence.
- Do not use for source design extraction from Figma files.

## Goal
Capture reproducible visual artifacts that make issues understandable without additional context.

## Inputs
- Capture target (display, app window, active window, region)
- Evidence intent (regression proof, before/after comparison, bug report)
- Storage path and sharing requirements

## Outputs
- Screenshot artifact set with stable naming
- Capture metadata (what, where, when, and why)
- Optional comparison pair for change validation

## Workflow
1. Define the exact UI state that must be captured.
2. Capture at the smallest scope that still preserves diagnostic value.
3. Verify legibility of key evidence (labels, errors, version/state markers).
4. Store artifacts under predictable paths for PR/issue references.
5. For external sharing, attach capture context so reviewers can reproduce the same state.

## Quality Gates
- Captures include enough context to identify app state and scenario.
- Local debug capture remains lightweight; apply masking only when artifacts are shared externally.
- Artifact paths and names are consistent across updates.
- Reviewer can map each screenshot to a concrete reproduction step.

## Failure Handling
- Stop when screen-capture permissions are unavailable.
- Stop external sharing when required masking cannot be completed safely.
