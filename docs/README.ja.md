# Software Development Agent Skills

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](../LICENSE)

ソフトウェア開発向けの Agent Skills です。

[English](../README.md) | [中国語](README.zh-CN.md)

## 概要

このリポジトリには、次の内容が含まれます。

- 再利用可能な skills の標準ディレクトリ構成
- Codex、Claude Code、OpenCode 向けインストールスクリプト

## リポジトリ構成

- `skills/<skill-name>/SKILL.md`: 必須のスキル定義
- `skills/<skill-name>/scripts/`: 任意の補助スクリプト
- `skills/<skill-name>/references/`: 任意の参考資料
- `scripts/`: インストーラー
- `docs/`: 多言語 README

## クイックセットアップ

```bash
git clone https://github.com/KentoShimizu/sw-agent-skills.git
cd sw-agent-skills
bash scripts/install-skills.sh --agent all --scope global
```

リリースアーカイブを取得して `skills` フォルダを任意パスへ配置する場合:

```bash
TAG=vX.Y.Z # 例: v0.1.0
DEST=/path/to/skills
curl -fsSL -o sw-agent-skills.zip "https://github.com/KentoShimizu/sw-agent-skills/archive/refs/tags/${TAG}.zip"
unzip -q sw-agent-skills.zip
mkdir -p "${DEST}"
cp -R "sw-agent-skills-${TAG#v}/skills/." "${DEST}/"
```

チェックアウト済みリポジトリの内容をそのまま使う場合:

```bash
bash scripts/install-skills.sh --agent all --scope global --source skills
```

Windows PowerShell:

```powershell
git clone https://github.com/KentoShimizu/sw-agent-skills.git
Set-Location sw-agent-skills
powershell -ExecutionPolicy Bypass -File .\scripts\install-skills.ps1 -Agent all -Scope global
```

## インストールオプション

### Bash (`scripts/install-skills.sh`)

| オプション | 必須 | 説明 | デフォルト |
| --- | --- | --- | --- |
| `--agent <all/codex/claude/opencode>` | いいえ | インストール対象のエージェント。 | `all` |
| `--scope <global/local>` | いいえ | インストール範囲。`local` は `--project-root` 配下へ配置。 | `global` |
| `--source <path>` | いいえ | スキルのソースディレクトリ。`SKILL.md` を持つサブディレクトリを含む必要があります。 | 公式リポジトリの最新安定リリーススナップショット |
| `--project-root <path>` | いいえ | `--scope local` 時に使うプロジェクトルート。 | カレントディレクトリ |
| `--force` | いいえ | 既存の配置先スキルディレクトリを置換。 | 無効 |
| `-h`, `--help` | いいえ | ヘルプを表示。 | 無効 |

### PowerShell (`scripts/install-skills.ps1`)

| オプション | 必須 | 説明 | デフォルト |
| --- | --- | --- | --- |
| `-Agent <all/codex/claude/opencode>` | いいえ | インストール対象のエージェント。 | `all` |
| `-Scope <global/local>` | いいえ | インストール範囲。`local` は `-ProjectRoot` 配下へ配置。 | `global` |
| `-Source <path>` | いいえ | スキルのソースディレクトリ。`SKILL.md` を持つサブディレクトリを含む必要があります。 | 公式リポジトリの最新安定リリーススナップショット |
| `-ProjectRoot <path>` | いいえ | `-Scope local` 時に使うプロジェクトルート。 | カレントディレクトリ |
| `-Force` | いいえ | 既存の配置先スキルディレクトリを置換。 | 無効 |

## 参考資料

- [Agent Skills](https://agentskills.io/home)
- [Codex](https://developers.openai.com/codex/skills)
- [Claude](https://docs.claude.com/en/docs/claude-code/skills)
- [OpenCode](https://opencode.ai/docs/skills)

## ライセンス

Apache License 2.0。`LICENSE` を参照してください。
