# Software Development Agent Skills

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](./LICENSE)

Agent Skills for software development.

[日本語](docs/README.ja.md) | [中文](docs/README.zh-CN.md)

## Overview

This repository provides:

- A standard structure for reusable skills
- Release-distributed reusable skills for Codex, Claude Code, and OpenCode
- Validation scripts for link/path integrity

## Repository Structure

- `skills/<skill-name>/SKILL.md`: required skill definition
- `skills/<skill-name>/scripts/`: optional helper scripts
- `skills/<skill-name>/references/`: optional reference documents
- `scripts/`: validator and maintenance scripts
- `docs/`: localized README files

## Quick Start (Download a Release)

```bash
TAG=vX.Y.Z  # replace with the release tag
curl -L -o sw-agent-skills.tar.gz "https://github.com/KentoShimizu/sw-agent-skills/archive/refs/tags/${TAG}.tar.gz"
tar -xzf sw-agent-skills.tar.gz
cd "sw-agent-skills-${TAG#v}"
```

After extraction, pick the skill directories you need (for example `skills/testing-unit`) and install them per agent.

### Agent Setup (Official References)

1. Codex ([openai/skills](https://github.com/openai/skills), [Codex Skills docs](https://developers.openai.com/codex/skills))
   - Personal skills: `~/.agents/skills/<skill-name>/SKILL.md`
   - Project skills: `<project>/.agents/skills/<skill-name>/SKILL.md`
   - `SKILL.md` must include frontmatter with at least `name` and `description`.
2. Claude Code ([Claude Code Skills](https://docs.claude.com/en/docs/claude-code/skills))
   - Global skills: `~/.claude/skills/<skill-name>/SKILL.md`
   - Project skills: `<project>/.claude/skills/<skill-name>/SKILL.md`
   - `SKILL.md` must include frontmatter with at least `name` and `description`.
3. OpenCode ([OpenCode Skills](https://open-code.ai/en/docs/skills))
   - Global skills: `~/.config/opencode/skills/<skill-name>/SKILL.md`
   - Project skills: `<project>/.opencode/skills/<skill-name>/SKILL.md`
   - `SKILL.md` must include frontmatter with at least `name` and `description`.
   - OpenCode also discovers `.claude/skills` and `.agents/skills`.

## Validation

```bash
python3 scripts/validate_skill_links.py
python3 scripts/validate_no_absolute_paths.py
```

## References

- [Releases](https://github.com/KentoShimizu/sw-agent-skills/releases)
- [Agent Skills](https://agentskills.io/home)
- [Codex Skills (openai/skills)](https://github.com/openai/skills)
- [Codex Skills docs](https://developers.openai.com/codex/skills)
- [Claude Code Skills](https://docs.claude.com/en/docs/claude-code/skills)
- [OpenCode Skills](https://open-code.ai/en/docs/skills)
