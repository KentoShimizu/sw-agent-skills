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

```bash
git clone https://github.com/KentoShimizu/sw-agent-skills.git
cd sw-agent-skills
bash scripts/install-skills.sh --agent all --scope global
```

Install a specific release:

```bash
bash scripts/install-skills.sh --agent all --scope global --version vX.Y.Z
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

Install from the checked-out repository content:

```bash
bash scripts/install-skills.sh --agent all --scope global --source skills --mode symlink
```

Preview only (no file changes):

```bash
bash scripts/install-skills.sh --agent all --scope global --dry-run
```

Windows PowerShell:

```powershell
git clone https://github.com/KentoShimizu/sw-agent-skills.git
Set-Location sw-agent-skills
powershell -ExecutionPolicy Bypass -File .\scripts\install-skills.ps1 -Agent all -Scope global
```

## Installation Options

### Bash (`scripts/install-skills.sh`)

| Option | Required | Description | Default |
| --- | --- | --- | --- |
| `--agent <all/codex/claude/opencode>` | No | Target agent to install. | `all` |
| `--scope <global/local>` | No | Install scope. `local` installs under `--project-root`. | `global` |
| `--mode <symlink/copy>` | No | Install method for each skill directory. | `copy` |
| `--source <path>` | No | Source skills directory. It must contain skill subdirectories with `SKILL.md`. | latest stable release snapshot from official repository |
| `--version <tag/latest>` | No | Release version used when `--source` is omitted. | `latest` |
| `--release-repo <url>` | No | Repository URL used for release resolution when `--source` is omitted. | `https://github.com/KentoShimizu/sw-agent-skills.git` |
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
| `-Mode <symlink/copy>` | No | Install method for each skill directory. | `copy` |
| `-Source <path>` | No | Source skills directory. It must contain skill subdirectories with `SKILL.md`. | latest stable release snapshot from official repository |
| `-Version <tag/latest>` | No | Release version used when `-Source` is omitted. | `latest` |
| `-ReleaseRepo <url>` | No | Repository URL used for release resolution when `-Source` is omitted. | `https://github.com/KentoShimizu/sw-agent-skills.git` |
| `-ProjectRoot <path>` | No | Project root used only when `-Scope local`. | current directory |
| `-DryRun` | No | Show actions without changing files. | off |
| `-VerboseList` | No | Print detailed action output. | off |
| `-Force` | No | Replace existing destination skill directories. | off |

## References

- [Agent Skills](https://agentskills.io/home)
- [Codex](https://developers.openai.com/codex/skills)
- [Claude](https://docs.claude.com/en/docs/claude-code/skills)
- [OpenCode](https://opencode.ai/docs/skills)
