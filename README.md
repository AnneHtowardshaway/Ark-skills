# Ark Codex Skill

`ark` is a Codex skill for frontend delivery with a strict
spec-first workflow. It pushes Codex to read the project,
write a short requirement sheet, investigate root causes,
implement carefully, and verify with evidence before claiming
success.

## What It Enforces

- Spec Coding before implementation
- Read the real project before asking for missing input
- Root-cause investigation for bug fixes
- Clear impact scope and rollback thinking
- Verification before completion

## Repository Layout

```text
ark/
  SKILL.md
  agents/openai.yaml
  references/spec-coding.md
  references/vibe-coding.md
scripts/
  validate_skill.py
.github/workflows/
  validate.yml
```

## Install

### Option 1: Manual

1. Clone this repository.
2. Copy the `ark` folder into `$CODEX_HOME/skills`.
3. If `CODEX_HOME` is unset, use `~/.codex/skills`.
4. Restart Codex.

### Option 2: GitHub installer script

Run the built-in installer from your local Codex setup:

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo <owner>/codex-ark-skill \
  --path ark
```

On Windows, replace `~/.codex` with
`%USERPROFILE%\\.codex` or your custom `CODEX_HOME`.

## Validate Locally

```bash
python scripts/validate_skill.py ark
```

## Publish To GitHub

1. Create an empty GitHub repository named `codex-ark-skill`.
2. Initialize git locally if needed.
3. Commit the files.
4. Add the GitHub remote.
5. Push `main`.

Example:

```bash
git init
git add .
git commit -m "feat: publish ark codex skill"
git branch -M main
git remote add origin https://github.com/<owner>/codex-ark-skill.git
git push -u origin main
```

## Notes

- This repo only contains the publishable skill package.
- Keep private paths, company-only details, and local-only
  dependencies out of `SKILL.md`.
- GitHub Actions runs the local validator on every push and pull
  request.
