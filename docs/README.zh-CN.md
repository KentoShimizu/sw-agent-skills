# Software Development Agent Skills

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](../LICENSE)

面向软件开发的 Agent Skills。

[英文](../README.md) | [日文](README.ja.md)

## 概览

本仓库提供以下内容：

- 可复用 skills 的标准目录结构
- 面向 Codex、Claude Code、OpenCode 的安装脚本

## 仓库结构

- `skills/<skill-name>/SKILL.md`: 必需的技能定义
- `skills/<skill-name>/scripts/`: 可选辅助脚本
- `skills/<skill-name>/references/`: 可选参考文档
- `scripts/`: 安装脚本
- `docs/`: 多语言 README

## 快速安装

从 GitHub Releases 下载最新发布归档并解压后，执行：

```bash
bash /path/to/sw-agent-skills-<version>/scripts/install-skills.sh --agent all --scope global
```

Windows PowerShell：

```powershell
powershell -ExecutionPolicy Bypass -File C:\path\to\sw-agent-skills-<version>\scripts\install-skills.ps1 -Agent all -Scope global
```

下载发布归档并将 `skills` 目录放到任意路径：

```bash
TAG=vX.Y.Z # 例如: v0.1.0
DEST=/path/to/skills
curl -fsSL -o sw-agent-skills.zip "https://github.com/KentoShimizu/sw-agent-skills/archive/refs/tags/${TAG}.zip"
unzip -q sw-agent-skills.zip
mkdir -p "${DEST}"
cp -R "sw-agent-skills-${TAG#v}/skills/." "${DEST}/"
```

## 安装选项

### Bash（`scripts/install-skills.sh`）

| 选项 | 必填 | 说明 | 默认值 |
| --- | --- | --- | --- |
| `--agent <all/codex/claude/opencode>` | 否 | 要安装的目标代理。 | `all` |
| `--scope <global/local>` | 否 | 安装范围。`local` 安装到 `--project-root` 下。 | `global` |
| `--project-root <path>` | 否 | 仅在 `--scope local` 时使用的项目根目录。 | 当前目录 |
| `-h`, `--help` | 否 | 显示帮助。 | 关闭 |

### PowerShell（`scripts/install-skills.ps1`）

| 选项 | 必填 | 说明 | 默认值 |
| --- | --- | --- | --- |
| `-Agent <all/codex/claude/opencode>` | 否 | 要安装的目标代理。 | `all` |
| `-Scope <global/local>` | 否 | 安装范围。`local` 安装到 `-ProjectRoot` 下。 | `global` |
| `-ProjectRoot <path>` | 否 | 仅在 `-Scope local` 时使用的项目根目录。 | 当前目录 |

管理更新说明：安装器会在每个目标目录下使用 `.sw-agent-skills-managed` 跟踪其管理的技能目录。未被该清单跟踪的目录会保留；若与未管理目录发生同名冲突，安装会停止。

## 参考资料

- [Agent Skills 官网](https://agentskills.io/home)
- [Codex 文档](https://developers.openai.com/codex/skills)
- [Claude 文档](https://docs.claude.com/en/docs/claude-code/skills)
- [OpenCode 文档](https://opencode.ai/docs/skills)

## 许可证

Apache License 2.0。详见 `LICENSE`。
