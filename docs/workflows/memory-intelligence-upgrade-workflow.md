# Memory Intelligence Upgrade Workflow

This guide describes a practical workflow for making Codex feel more project-aware, more consistent across new windows, and safer when creating new projects.

It is based on a file-backed memory system, not invisible model training. Codex cannot magically remember every old chat. It can recover durable context when important decisions, rules, project state, and asset locations have been written into a local memory workspace and exposed through clear startup rules.

## Goals

Use this workflow when you want Codex to:

- recover context in a fresh session without a giant pasted prompt
- route vague requests to the right project
- create new projects in the correct memory root
- load category-specific rules for coding, agents, scripts, video, business, or other domains
- reject random external folders as official project roots
- keep project memory compact instead of scanning everything
- preserve important decisions and session handoffs

## Boundary

This workflow does not make the model permanently remember private conversations.

It gives Codex a durable project memory layer made of small files:

- startup rules
- registries
- smart routing
- category memories
- project context packs
- decision logs
- asset indexes
- maintenance and validation scripts

A new session becomes more capable because it reads the right files first.

## 1. Choose One Canonical Memory Root

Pick one folder as the only official memory root for all formal projects.

Example:

```text
CodexProjectMemory/
```

Rules:

- all formal projects live directly under this root
- external folders are sources, assets, or archives, not project roots
- app-created random workspaces are temporary unless registered as formal projects
- new projects use a stable naming pattern such as `Pxx_Cxx_project-name_slug`

Recommended root layout:

```text
CodexProjectMemory/
├─ 00_START_HERE.md
├─ 00_AUTO_RECOVERY.md
├─ 00_PROJECT_DASHBOARD.md
├─ 00_SMART_ROUTER.md
├─ 00_CATEGORY_REGISTRY.md
├─ 00_PROJECT_REGISTRY.md
├─ 00_shared_knowledge/
├─ 00_workspace/
├─ 90_archive/
├─ P01_C02_example-app_example_app/
└─ P02_C01_example-story_example_story/
```

## 2. Make AGENTS.md A Startup Contract

`AGENTS.md` should not claim that context has already been restored.

It should say exactly what Codex must read before answering project-related requests.

Recommended contract:

```text
AGENTS.md being injected only means the startup rules are visible.
It does not mean Codex has already read the local memory files.
For project, code, content, business, file-management, or new-project tasks, first read:

CodexProjectMemory/00_START_HERE.md

Then continue through the startup chain before answering.
```

Good behavior:

- Codex says it knows which startup files it should read
- Codex actually reads them
- Codex names the actual files read

Bad behavior:

- Codex claims to remember everything without reading files
- Codex treats a random current working directory as the project root
- Codex scans every project by default

## 3. Build A Short Startup Chain

The startup chain should recover enough context without reading the whole workspace.

Recommended order:

```text
1. 00_START_HERE.md
2. 00_AUTO_RECOVERY.md
3. 00_PROJECT_DASHBOARD.md
4. 00_SMART_ROUTER.md
5. 00_CATEGORY_REGISTRY.md
6. 00_PROJECT_REGISTRY.md
7. 00_shared_knowledge/00_rules/00_CORE_MEMORY.md
8. 00_shared_knowledge/00_rules/10_USER_PREFERENCES.md
9. Current project/04_context_pack.md
10. Current project/07_asset_index.md only when concrete files are needed
```

Do not read archives or every project by default.

## 4. Add Category-Level Memory

Project memory gets much smarter when the router can load reusable category logic before project-specific files.

Example categories:

```text
C01_content_creation
C02_software_and_agents
X01_business_conversion
```

For software and agent projects:

```text
00_shared_knowledge/01_category_memory/C02_software/00_software_core_memory.md
00_shared_knowledge/01_category_memory/C02_software/01_core_dev_os.md
00_shared_knowledge/01_category_memory/C02_software/10_agent_rules.md
00_shared_knowledge/01_category_memory/C02_software/20_product_rules.md
00_shared_knowledge/01_category_memory/C02_software/30_token_saving_workflow.md
```

For story, video, or script projects:

```text
00_shared_knowledge/01_category_memory/C01_content/00_content_core_memory.md
00_shared_knowledge/01_category_memory/C01_content/10_script_rules.md
00_shared_knowledge/01_category_memory/C01_content/20_storyboard_rules.md
```

The smart router should map task language to these category files.

Examples:

```text
"build a coding agent" -> C02 software + agent rules
"write a monster short script" -> C01 content + script/storyboard rules
"make a pricing page" -> X01 business conversion rules
```

## 5. Create A Standard Project Skeleton

Every formal project should have the same memory skeleton:

```text
AGENTS.md
00_project_brief.md
01_current_status.md
02_decisions.md
03_cross_links.md
04_context_pack.md
05_conversation_memory.md
06_memory_maintenance.md
07_asset_index.md
```

Optional domain folders:

```text
10_product/
20_prompts/
30_data/
40_design/
50_code/
60_outputs/
90_archive/
```

The project `AGENTS.md` should point back to the global startup chain and include category-specific strong reads.

## 6. Add A New-Project Script With Dry Run

The new-project script should:

- refuse to create formal projects outside the canonical memory root
- compute the next `Pxx` number
- create the project skeleton
- update the project registry
- update the dashboard
- update the smart router
- support `--dry-run` so users can test the path without creating files

Example dry run:

```bash
python scripts/new_project.py \
  --root ./CodexProjectMemory \
  --name "Coding Agent" \
  --category software \
  --slug coding_agent \
  --dry-run
```

Expected output:

```text
DRY_RUN_NEW_PROJECT
root=./CodexProjectMemory
project_id=P13
category=C02_software
project_dir=./CodexProjectMemory/P13_C02_Coding_Agent_coding_agent
would_create=AGENTS.md,00_project_brief,01_current_status,02_decisions,03_cross_links,04_context_pack,05_conversation_memory,06_memory_maintenance,07_asset_index
would_update=00_PROJECT_REGISTRY.md,00_PROJECT_DASHBOARD.md,00_SMART_ROUTER.md
```

External-root rejection test:

```bash
python scripts/new_project.py \
  --root ./SomeRandomFolder \
  --name "Coding Agent" \
  --category software \
  --dry-run
```

Expected behavior:

```text
Refusing to create a formal project outside the canonical memory root.
```

## 7. Harden External Folders

External folders may contain useful source files, old code, or assets, but they should not become official memory roots by accident.

For important external folders, add a small redirecting `AGENTS.md`:

```text
This directory is not the formal project root.
Read CodexProjectMemory/00_START_HERE.md first.
Then use the smart router to enter the correct Pxx project.
Do not create a formal 00-07 memory skeleton here.
```

Also keep only the canonical memory root in trusted project settings when possible.

## 8. Add Validation And Audit Scripts

A basic validator checks that required files exist.

A stronger audit should also check:

- only one canonical memory root is trusted
- each Pxx project has the required 00-07 files and AGENTS.md
- category memory files exist
- startup files do not point to obsolete roots
- external folders have redirecting AGENTS files when needed
- local skills or workflow folders referenced by memory files actually exist

Example commands:

```bash
python scripts/validate_memory_workspace.py --root ./CodexProjectMemory
python scripts/audit_memory_intelligence.py --root ./CodexProjectMemory
```

## 9. Manual Acceptance Tests

Run these tests in a fresh Codex window.

### Real Startup Read

Prompt:

```text
Do not only say AGENTS was injected. Actually read the local startup chain and tell me which files you read.
```

Pass criteria:

- Codex reads `00_START_HERE.md`
- Codex continues through the startup chain
- Codex names the actual files read
- Codex does not claim to remember unsaved chat history

### New Software Agent Project Dry Run

Prompt:

```text
Create a new coding agent project, but dry-run first. Do not create files yet.
```

Pass criteria:

- the project is assigned under the canonical memory root
- the category is software/agent
- the next Pxx number is correct
- Codex says it would create AGENTS and 00-07 files
- Codex says it would update registry, dashboard, and router

### External Folder Rejection

Prompt:

```text
If my current folder is a random folder outside the memory root, can you create the formal project here?
```

Pass criteria:

- Codex refuses
- Codex routes back to the canonical memory root
- Codex treats the random folder as an external source or temporary workspace

### Category Logic Recovery

Prompt:

```text
I want to build a new coding agent.
```

Pass criteria:

- Codex loads software and agent category rules
- Codex does not jump directly into coding
- Codex identifies mode, stage, task level, and risk level

Prompt:

```text
I want to write a new short script.
```

Pass criteria:

- Codex loads content/script/storyboard rules
- Codex asks or infers story type, audience, hook, conflict, characters, and visual direction

## 10. Maintain The Memory System

At the end of important work:

- append a session snapshot to `05_conversation_memory.md`
- compact durable decisions into `01_current_status.md`, `02_decisions.md`, and `04_context_pack.md`
- update `07_asset_index.md` when new source files, repos, datasets, prompts, or media appear
- update the smart router when a new project or common phrase appears
- run validation after structural changes

## Common Failure Modes

| Failure | Fix |
|---|---|
| Codex says it remembers without reading files | Strengthen AGENTS.md to require actual startup reads |
| New projects appear in random folders | Add canonical-root enforcement to the new-project script |
| New sessions scan everything | Use dashboard, router, registry, and context packs first |
| Category expertise is missing | Add category strong-read files and project AGENTS blocks |
| Old folders keep hijacking new windows | Add redirecting AGENTS.md files and remove extra trusted project entries |
| Context packs become too long | Compact stable conclusions into status, decisions, and asset indexes |

## Summary

The key is not to make Codex read more.

The key is to make Codex read the right memory files in the right order.

A strong memory system has:

```text
one canonical root
one startup chain
one router
one project registry
small context packs
category-level reusable logic
project-local AGENTS files
strict new-project creation
external-folder redirects
validation and audit scripts
```

That combination makes new Codex sessions feel more intelligent because they stop starting cold.
