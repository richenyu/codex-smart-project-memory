# Codex Smart Project Memory

A lightweight smart memory system for Codex that helps new sessions understand your projects, route context, and continue work without bloating the prompt.

Give Codex smarter project memory with `AGENTS.md`, smart routing, session snapshots, asset indexes, and lightweight context recovery.

> Unofficial community project. Not affiliated with OpenAI.

## What It Does

Codex is powerful, but new sessions can lose project context unless the important logic is written down. This project provides a small memory architecture that turns project context into durable files Codex can read quickly.

It helps Codex:

- recover context in new chats
- understand many projects without scanning everything
- route vague requests to the right project
- preserve important decisions and user preferences
- write end-of-session handoffs
- keep memory useful without filling every prompt with old context

## Repository Layout

```text
skill/codex-smart-project-memory/
  SKILL.md
  agents/openai.yaml
  scripts/
  references/
  assets/templates/
```

The Skill lives in `skill/codex-smart-project-memory`. The outer repository exists for GitHub discovery, documentation, and community use.

## Quick Start

After installing the Skill in Codex, ask:

```text
Use $codex-smart-project-memory to initialize a smart project memory workspace for my Codex projects.
```

You can also run the scripts directly:

```bash
python skill/codex-smart-project-memory/scripts/init_memory_workspace.py --root ./CodexProjectMemory --root-name "My Codex Memory"
python skill/codex-smart-project-memory/scripts/new_project.py --root ./CodexProjectMemory --name "My First Project" --category software
python skill/codex-smart-project-memory/scripts/validate_memory_workspace.py --root ./CodexProjectMemory
```

## The Memory Model

Each workspace has a short startup chain:

```text
00_START_HERE.md
00_AUTO_RECOVERY.md
00_PROJECT_DASHBOARD.md
00_SMART_ROUTER.md
00_PROJECT_REGISTRY.md
00_shared_knowledge/00_rules/00_CORE_MEMORY.md
00_shared_knowledge/00_rules/10_USER_PREFERENCES.md
```

Each project has a small set of memory files:

```text
00_project_brief.md
01_current_status.md
02_decisions.md
03_cross_links.md
04_context_pack.md
05_conversation_memory.md
06_memory_maintenance.md
07_asset_index.md
AGENTS.md
```

The rule is simple: read the smallest useful context first, then load deeper files only when the task needs them.

## Why This Helps

Many users try to solve memory by pasting huge prompts into every new chat. That works briefly, then becomes slow, stale, and hard to maintain.

This project uses durable files instead:

- small startup files for speed
- project-level context packs for continuity
- registries for routing
- snapshots for handoff
- compaction rules for long-term maintenance

## Who It Is For

- developers using Codex across multiple repositories
- creators managing scripts, prompts, videos, and assets
- founders building several AI products at once
- teams that want Codex to understand project structure without leaking private details into every prompt

## Community

Star this repository if it helps you. Open an Issue for bugs, missing templates, or workflow ideas. Use Discussions for examples and setup questions.

More demo videos and advanced templates can be added as the project grows.

## License

MIT
