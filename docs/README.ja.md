# Software Development Agent Skills

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](../LICENSE)

ソフトウェア開発向けの Agent Skills です。

[English](../README.md) | [中国語](README.zh-CN.md)

## 概要

このリポジトリには、次の内容が含まれます。

- 再利用可能な skills の標準ディレクトリ構成
- Codex、Claude Code、OpenCode 向けに配布可能な skills
- リンクやパス整合性を確認する検証スクリプト

## リポジトリ構成

- `skills/<skill-name>/SKILL.md`: 必須のスキル定義
- `skills/<skill-name>/scripts/`: 任意の補助スクリプト
- `skills/<skill-name>/references/`: 任意の参考資料
- `scripts/`: バリデーターとメンテナンス用スクリプト
- `docs/`: 多言語 README

## クイックセットアップ（Release ダウンロード）

```bash
TAG=vX.Y.Z  # Releases で確認したタグに置き換え
curl -L -o sw-agent-skills.tar.gz "https://github.com/KentoShimizu/sw-agent-skills/archive/refs/tags/${TAG}.tar.gz"
tar -xzf sw-agent-skills.tar.gz
cd "sw-agent-skills-${TAG#v}"
```

展開後は、必要な skill ディレクトリ（例: `skills/testing-unit`）を選び、各サービスの公式手順で追加してください。

### エージェント別セットアップ（公式リファレンス）

1. Codex（[openai/skills](https://github.com/openai/skills)、[Codex Skills docs](https://developers.openai.com/codex/skills)）
   - 個人スキル: `~/.agents/skills/<skill-name>/SKILL.md`
   - プロジェクト単位: `<project>/.agents/skills/<skill-name>/SKILL.md`
   - `SKILL.md` には最低限 `name` と `description` の frontmatter が必要です。
2. Claude Code（[Claude Code Skills](https://docs.claude.com/en/docs/claude-code/skills)）
   - グローバル: `~/.claude/skills/<skill-name>/SKILL.md`
   - プロジェクト単位: `<project>/.claude/skills/<skill-name>/SKILL.md`
   - `SKILL.md` には最低限 `name` と `description` の frontmatter が必要です。
3. OpenCode（[OpenCode Skills](https://open-code.ai/en/docs/skills)）
   - グローバル: `~/.config/opencode/skills/<skill-name>/SKILL.md`
   - プロジェクト単位: `<project>/.opencode/skills/<skill-name>/SKILL.md`
   - `SKILL.md` には最低限 `name` と `description` の frontmatter が必要です。
   - OpenCode は `.claude/skills` と `.agents/skills` も検出できます。

## 検証

```bash
python3 scripts/validate_skill_links.py
python3 scripts/validate_no_absolute_paths.py
```

## 参考資料

- [Releases](https://github.com/KentoShimizu/sw-agent-skills/releases)
- [Agent Skills](https://agentskills.io/home)
- [Codex Skills (openai/skills)](https://github.com/openai/skills)
- [Codex Skills docs](https://developers.openai.com/codex/skills)
- [Claude Code Skills](https://docs.claude.com/en/docs/claude-code/skills)
- [OpenCode Skills](https://open-code.ai/en/docs/skills)

## ライセンス

Apache License 2.0。`LICENSE` を参照してください。
