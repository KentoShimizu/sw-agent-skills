# Software Development Agent Skills

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](./LICENSE)

Agent Skills for software development.

[日本語](docs/README.ja.md) | [中文](docs/README.zh-CN.md)

## Overview

This repository provides:

- A standard structure for reusable skills
- Installation scripts for Codex, Claude Code, and OpenCode
- Validation scripts for link/path integrity

## Repository Structure

- `skills/<skill-name>/SKILL.md`: required skill definition
- `skills/<skill-name>/scripts/`: optional helper scripts
- `skills/<skill-name>/references/`: optional reference documents
- `scripts/`: installer and validator scripts
- `docs/`: localized README files

## Quick Start

```bash
git clone https://github.com/KentoShimizu/sw-agent-skills.git
cd sw-agent-skills
bash scripts/install-skills.sh --agent all --scope global
```

Preview only (no file changes):

```bash
bash scripts/install-skills.sh --agent all --scope global --dry-run
```

Windows PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-skills.ps1 -Agent all -Scope global
```

## Installation Options

### Bash (`scripts/install-skills.sh`)

| Option | Required | Description | Default |
| --- | --- | --- | --- |
| `--agent <all/codex/claude/opencode>` | No | Target agent to install. | `all` |
| `--scope <global/local>` | No | Install scope. `local` installs under `--project-root`. | `global` |
| `--mode <symlink/copy>` | No | Install method for each skill directory. | `symlink` |
| `--source <path>` | No | Source skills directory. It must contain skill subdirectories with `SKILL.md`. | `<repo>/skills` |
| `--project-root <path>` | No | Project root used only when `--scope local`. | current directory |
| `--dry-run` | No | Show actions without changing files. | off |
| `--verbose` | No | Print detailed command output. | off |
| `--force` | No | Replace existing destination skill directories. | off |
| `-h`, `--help` | No | Show command help. | off |

### PowerShell (`scripts/install-skills.ps1`)

| Option | Required | Description | Default |
| --- | --- | --- | --- |
| `-Agent <all/codex/claude/opencode>` | No | Target agent to install. | `all` |
| `-Scope <global/local>` | No | Install scope. `local` installs under `-ProjectRoot`. | `global` |
| `-Mode <symlink/copy>` | No | Install method for each skill directory. | `symlink` |
| `-Source <path>` | No | Source skills directory. It must contain skill subdirectories with `SKILL.md`. | `<repo>/skills` |
| `-ProjectRoot <path>` | No | Project root used only when `-Scope local`. | current directory |
| `-DryRun` | No | Show actions without changing files. | off |
| `-VerboseList` | No | Print detailed action output. | off |
| `-Force` | No | Replace existing destination skill directories. | off |

## Validation

```bash
python3 scripts/validate_skill_links.py
python3 scripts/validate_no_absolute_paths.py
```

## References

- [Agent Skills](https://agentskills.io/home)
- [Codex](https://developers.openai.com/codex/skills)
- [Claude](https://docs.claude.com/en/docs/claude-code/skills)
- [OpenCode](https://opencode.ai/docs/skills)
