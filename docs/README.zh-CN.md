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

```bash
git clone https://github.com/KentoShimizu/sw-agent-skills.git
cd sw-agent-skills
bash scripts/install-skills.sh --agent all --scope global
```

仅预览（不修改文件）：

```bash
bash scripts/install-skills.sh --agent all --scope global --dry-run
```

Windows PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-skills.ps1 -Agent all -Scope global
```

## 安装选项

### Bash（`scripts/install-skills.sh`）

| 选项 | 必填 | 说明 | 默认值 |
| --- | --- | --- | --- |
| `--agent <all/codex/claude/opencode>` | 否 | 要安装的目标代理。 | `all` |
| `--scope <global/local>` | 否 | 安装范围。`local` 安装到 `--project-root` 下。 | `global` |
| `--mode <symlink/copy>` | 否 | 每个技能目录的安装方式。 | `symlink` |
| `--source <path>` | 否 | 技能来源目录。必须包含带 `SKILL.md` 的技能子目录。 | `<repo>/skills` |
| `--project-root <path>` | 否 | 仅在 `--scope local` 时使用的项目根目录。 | 当前目录 |
| `--dry-run` | 否 | 仅显示动作，不修改文件。 | 关闭 |
| `--verbose` | 否 | 输出详细命令日志。 | 关闭 |
| `--force` | 否 | 覆盖已存在的目标技能目录。 | 关闭 |
| `-h`, `--help` | 否 | 显示帮助。 | 关闭 |

### PowerShell（`scripts/install-skills.ps1`）

| 选项 | 必填 | 说明 | 默认值 |
| --- | --- | --- | --- |
| `-Agent <all/codex/claude/opencode>` | 否 | 要安装的目标代理。 | `all` |
| `-Scope <global/local>` | 否 | 安装范围。`local` 安装到 `-ProjectRoot` 下。 | `global` |
| `-Mode <symlink/copy>` | 否 | 每个技能目录的安装方式。 | `symlink` |
| `-Source <path>` | 否 | 技能来源目录。必须包含带 `SKILL.md` 的技能子目录。 | `<repo>/skills` |
| `-ProjectRoot <path>` | 否 | 仅在 `-Scope local` 时使用的项目根目录。 | 当前目录 |
| `-DryRun` | 否 | 仅显示动作，不修改文件。 | 关闭 |
| `-VerboseList` | 否 | 输出详细执行日志。 | 关闭 |
| `-Force` | 否 | 覆盖已存在的目标技能目录。 | 关闭 |

## 参考资料

- [Agent Skills 官网](https://agentskills.io/home)
- [Codex 文档](https://developers.openai.com/codex/skills)
- [Claude 文档](https://docs.claude.com/en/docs/claude-code/skills)
- [OpenCode 文档](https://opencode.ai/docs/skills)

## 许可证

Apache License 2.0。详见 `LICENSE`。
