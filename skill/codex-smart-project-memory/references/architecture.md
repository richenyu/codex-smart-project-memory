# Memory Architecture

## Goal

Codex Smart Project Memory stores context in durable, explicit files. The goal is not to remember everything. The goal is to preserve the small set of facts, decisions, preferences, assets, and handoffs that make the next session productive.

## Root Layer

The root layer answers: "What projects exist, how should Codex route this request, and what global rules matter?"

Required root files:

- `00_START_HERE.md`: first file to read
- `00_AUTO_RECOVERY.md`: new-session recovery procedure
- `00_PROJECT_DASHBOARD.md`: status, priority, next action
- `00_SMART_ROUTER.md`: keyword and task routing
- `00_CATEGORY_REGISTRY.md`: category definitions
- `00_PROJECT_REGISTRY.md`: project map
- `00_RECOVERY_TEST.md`: quick self-check
- `AGENTS.md`: root-level startup rule

Required root folders:

- `00_shared_knowledge/00_rules/`: global memory and preferences
- `00_workspace/`: current workbench and daily handoff
- `90_archive/`: old or inactive material, not read by default

## Project Layer

Each project owns its own memory. New sessions should read `04_context_pack.md` first because it is the compact handoff.

Project files:

- `00_project_brief.md`: identity, audience, scope
- `01_current_status.md`: state, blockers, next steps
- `02_decisions.md`: durable decisions and rationale
- `03_cross_links.md`: dependencies and reusable patterns
- `04_context_pack.md`: new-session starter context
- `05_conversation_memory.md`: chronological snapshots
- `06_memory_maintenance.md`: compaction and health checks
- `07_asset_index.md`: concrete files and assets
- `AGENTS.md`: project-local rule

## Memory Levels

Use three levels:

1. Fast memory: tiny global rules and preferences read often.
2. Project memory: stable project context and active decisions.
3. Archive memory: old details read only on request.

This prevents prompt bloat while keeping important continuity.

## Routing Principle

Route before reading deeply:

1. Identify task type.
2. Match project keywords.
3. Read the selected project's `04_context_pack.md`.
4. Read `07_asset_index.md` only when concrete files are needed.
5. Read archived or long conversation history only when needed.
