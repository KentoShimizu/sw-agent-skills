# Software Development Agent Skills

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](../LICENSE)

面向软件开发的 Agent Skills。

[英文](../README.md) | [日文](README.ja.md)

## 概览

本仓库提供以下内容：

- 可复用 skills 的标准目录结构
- 面向 Codex、Claude Code、OpenCode 可分发的 skills
- 用于校验链接与路径完整性的验证脚本

## 仓库结构

- `skills/<skill-name>/SKILL.md`: 必需的技能定义
- `skills/<skill-name>/scripts/`: 可选辅助脚本
- `skills/<skill-name>/references/`: 可选参考文档
- `scripts/`: 校验与维护脚本
- `docs/`: 多语言 README

## 快速安装（下载 Release）

```bash
TAG=vX.Y.Z  # 替换为 Releases 页面中的标签
curl -L -o sw-agent-skills.tar.gz "https://github.com/KentoShimizu/sw-agent-skills/archive/refs/tags/${TAG}.tar.gz"
tar -xzf sw-agent-skills.tar.gz
cd "sw-agent-skills-${TAG#v}"
```

解压后，请先选择需要的 skill 目录（例如 `skills/testing-unit`），再按各服务官方说明添加到对应环境。

### 按代理配置（官方参考）

1. Codex（[openai/skills](https://github.com/openai/skills)、[Codex settings: Skills](https://developers.openai.com/codex/settings#skills)）
   - 个人技能：`~/.agents/skills/<skill-name>/SKILL.md`
   - 项目级：`<project>/.agents/skills/<skill-name>/SKILL.md`
   - `SKILL.md` 至少需要包含 `name` 和 `description` 的 frontmatter。
2. Claude Code（[Claude Code Skills](https://docs.claude.com/en/docs/claude-code/skills)）
   - 全局：`~/.claude/skills/<skill-name>/SKILL.md`
   - 项目级：`<project>/.claude/skills/<skill-name>/SKILL.md`
   - `SKILL.md` 至少需要包含 `name` 和 `description` 的 frontmatter。
3. OpenCode（[OpenCode Skills](https://open-code.ai/en/docs/skills)）
   - 全局：`~/.config/opencode/skills/<skill-name>/SKILL.md`
   - 项目级：`<project>/.opencode/skills/<skill-name>/SKILL.md`
   - `SKILL.md` 至少需要包含 `name` 和 `description` 的 frontmatter。
   - OpenCode 也会发现 `.claude/skills` 和 `.agents/skills`。

## 校验

```bash
python3 scripts/validate_skill_links.py
python3 scripts/validate_no_absolute_paths.py
```

## 参考资料

- [Releases](https://github.com/KentoShimizu/sw-agent-skills/releases)
- [Agent Skills 官网](https://agentskills.io/home)
- [Codex Skills (openai/skills)](https://github.com/openai/skills)
- [Codex Settings: Skills](https://developers.openai.com/codex/settings#skills)
- [Claude Code Skills](https://docs.claude.com/en/docs/claude-code/skills)
- [OpenCode Skills](https://open-code.ai/en/docs/skills)

## 许可证

Apache License 2.0。详见 `LICENSE`。
