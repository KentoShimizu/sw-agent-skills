# Software Development Agent Skills

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](./LICENSE)

Agent Skills for software development.

[日本語](docs/README.ja.md) | [中文](docs/README.zh-CN.md)

## Overview

This repository provides:

- A standard structure for reusable skills
- Installation scripts for Codex, Claude Code, and OpenCode

## Repository Structure

- `skills/<skill-name>/SKILL.md`: required skill definition
- `skills/<skill-name>/scripts/`: optional helper scripts
- `skills/<skill-name>/references/`: optional reference documents
- `scripts/`: installer scripts
- `docs/`: localized README files

## Quick Start

Download the latest release archive from GitHub Releases, extract it, and run:

```bash
bash /path/to/sw-agent-skills-<version>/scripts/install-skills.sh --agent all --scope global
```

Windows PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -File C:\path\to\sw-agent-skills-<version>\scripts\install-skills.ps1 -Agent all -Scope global
```

Download from a release archive and place the `skills` folder in any path:

```bash
TAG=vX.Y.Z # e.g. v0.1.0
DEST=/path/to/skills
curl -fsSL -o sw-agent-skills.zip "https://github.com/KentoShimizu/sw-agent-skills/archive/refs/tags/${TAG}.zip"
unzip -q sw-agent-skills.zip
mkdir -p "${DEST}"
cp -R "sw-agent-skills-${TAG#v}/skills/." "${DEST}/"
```

## Installation Options

### Bash (`scripts/install-skills.sh`)

| Option | Required | Description | Default |
| --- | --- | --- | --- |
| `--agent <all/codex/claude/opencode>` | No | Target agent to install. | `all` |
| `--scope <global/local>` | No | Install scope. `local` installs under `--project-root`. | `global` |
| `--project-root <path>` | No | Project root used only when `--scope local`. | current directory |
| `--force` | No | Replace existing destination skill directories. | off |
| `-h`, `--help` | No | Show command help. | off |

### PowerShell (`scripts/install-skills.ps1`)

| Option | Required | Description | Default |
| --- | --- | --- | --- |
| `-Agent <all/codex/claude/opencode>` | No | Target agent to install. | `all` |
| `-Scope <global/local>` | No | Install scope. `local` installs under `-ProjectRoot`. | `global` |
| `-ProjectRoot <path>` | No | Project root used only when `-Scope local`. | current directory |
| `-Force` | No | Replace existing destination skill directories. | off |

## References

- [Agent Skills](https://agentskills.io/home)
- [Codex](https://developers.openai.com/codex/skills)
- [Claude](https://docs.claude.com/en/docs/claude-code/skills)
- [OpenCode](https://opencode.ai/docs/skills)
