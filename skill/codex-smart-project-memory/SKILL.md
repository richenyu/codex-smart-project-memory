---
name: codex-smart-project-memory
description: Lightweight smart project memory for Codex. Use when the user wants to initialize or maintain persistent Codex project memory, create a multi-project workspace, add a new project with reusable context files, recover context in new chats, write session snapshots, compact important conclusions into durable files, route across projects, or make Codex more useful without bloating every prompt.
---

# Codex Smart Project Memory

## Purpose

Use this skill to create and operate a lightweight project memory system for Codex. The system stores durable context in small, explicit files so new sessions can recover the project logic without rereading every file or relying on invisible chat memory.

## Core Workflow

1. Choose a memory root.
   - For one repo, use a local folder such as `.codex-memory`.
   - For many unrelated projects, use a central folder such as `CodexProjectMemory`.
2. Initialize the workspace with `scripts/init_memory_workspace.py`.
3. Create each project with `scripts/new_project.py`.
4. At the end of meaningful work, append a compact handoff with `scripts/session_snapshot.py`.
5. Validate the system with `scripts/validate_memory_workspace.py`.
6. When a new Codex session starts, read only the startup chain first, then the current project's context pack.

## Read Order

For a fresh session, read only this chain unless the task requires more:

1. `00_START_HERE.md`
2. `00_AUTO_RECOVERY.md`
3. `00_PROJECT_DASHBOARD.md`
4. `00_SMART_ROUTER.md`
5. `00_PROJECT_REGISTRY.md`
6. `00_shared_knowledge/00_rules/00_CORE_MEMORY.md`
7. `00_shared_knowledge/00_rules/10_USER_PREFERENCES.md`
8. Current project `04_context_pack.md`
9. Current project `05_conversation_memory.md` only when old session conclusions are needed
10. Current project `07_asset_index.md` only when concrete files or assets are needed

Do not scan every project by default. Do not read archives by default. Load the smallest file that can answer the routing question.

## Scripts

Run scripts from the skill folder or call them by full path:

```bash
python scripts/init_memory_workspace.py --root ./CodexProjectMemory --root-name "My Codex Memory"
python scripts/new_project.py --root ./CodexProjectMemory --name "AI Stock Agent" --category software
python scripts/session_snapshot.py --project ./CodexProjectMemory/P01_C02_ai-stock-agent --title "End of day" --summary "Built the initial memory workflow."
python scripts/validate_memory_workspace.py --root ./CodexProjectMemory
```

Use `--help` on each script for options.

## File Layers

Root files:

- Startup files: `00_START_HERE.md`, `00_AUTO_RECOVERY.md`, `00_PROJECT_DASHBOARD.md`, `00_SMART_ROUTER.md`
- Registries: `00_CATEGORY_REGISTRY.md`, `00_PROJECT_REGISTRY.md`
- Shared rules: `00_shared_knowledge/00_rules/`
- Workbench: `00_workspace/`

Project files:

- `00_project_brief.md`: stable project identity
- `01_current_status.md`: current status and next action
- `02_decisions.md`: durable decisions
- `03_cross_links.md`: related projects and reusable knowledge
- `04_context_pack.md`: first file to read in a new session
- `05_conversation_memory.md`: session snapshots and handoffs
- `06_memory_maintenance.md`: compaction and health notes
- `07_asset_index.md`: concrete files, repos, datasets, prompts, media
- `AGENTS.md`: project-local startup rule

## Operating Rules

- Write important conclusions into durable files before ending important work.
- Keep `04_context_pack.md` short enough to be read at startup.
- Treat `05_conversation_memory.md` as a chronological handoff log, not a dumping ground.
- When `05_conversation_memory.md` grows long, ask Codex to compact durable conclusions into `01_current_status.md`, `02_decisions.md`, and `04_context_pack.md`.
- Keep private, credential, and customer data out of public templates.
- If memory files conflict, prefer the newest explicit decision and mark the older statement as deprecated instead of silently deleting it.

## References

- Read `references/architecture.md` when designing or customizing the memory structure.
- Read `references/operating-rules.md` when maintaining, compacting, or debugging the memory system.
- Copy or adapt templates from `assets/templates/` when a script is not the right fit.
