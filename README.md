# Codex Smart Project Memory

A lightweight smart memory system for Codex that helps new sessions understand your projects, route context, and continue work without bloating the prompt.

Give Codex smarter project memory with `AGENTS.md`, smart routing, session snapshots, asset indexes, and lightweight context recovery.

> Unofficial community project. Not affiliated with OpenAI.

## Stop Restarting Every Codex Session From Zero

If you use Codex across more than one project, you have probably felt this problem:

- a new chat does not know what happened before
- important decisions disappear into old conversations
- project context gets pasted again and again
- prompts become too long, slow, and stale
- Codex has to rediscover the same files, rules, and preferences
- multi-project work becomes hard to route and maintain

Codex Smart Project Memory solves this by turning your important project logic into small, durable files that Codex can read quickly at the start of a session.

This is not a giant prompt. It is a lightweight memory architecture.

## What You Get

This repository gives you a ready-to-use Codex Skill and a reusable project memory system:

- a startup chain for new Codex sessions
- a multi-project registry
- a smart router for vague project requests
- project-level context packs
- session handoff snapshots
- decision logs
- asset indexes
- memory maintenance rules
- scripts to initialize, add projects, write snapshots, and validate the workspace

The result: Codex can act less like a blank new assistant and more like a project-aware collaborator.

## The Big Idea

Most AI memory workflows fail because they try to save everything.

This project does the opposite.

It saves only the context that actually helps future work:

- what the project is
- what the current state is
- what decisions were made
- where important files live
- what the user prefers
- what the next session should read first

That keeps the system fast, understandable, and easy to maintain.

## Before And After

Before:

```text
New chat: What is this project again?
You: Let me paste a huge prompt...
Codex: I need to scan the repo again...
You: We already decided this yesterday.
```

After:

```text
New chat: Read the startup chain and this project's context pack.
Codex: I understand the project, current status, decisions, and next action.
You: Continue from where we stopped.
```

## Who This Is For

Use this if you are:

- a developer working across many repositories
- a founder building several AI products at once
- a creator managing scripts, prompts, videos, and assets
- a team using Codex for product, engineering, content, or operations
- a power user who wants Codex to remember project logic without pasting huge prompts

## Why It Works

Codex Smart Project Memory uses a three-layer memory model:

1. **Fast memory**: tiny global rules and user preferences.
2. **Project memory**: each project's status, decisions, context pack, and assets.
3. **Archive memory**: older details that are only loaded when needed.

This gives Codex enough context to be useful without forcing every session to load everything.

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

## Memory Workspace Structure

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

## Example Use Cases

### Multi-project founder

You are building several products at once. Codex can route each request to the right project, read the right context pack, and avoid mixing unrelated decisions.

### Software team

Your team wants Codex to understand project structure, decisions, and active work without putting everything into one enormous prompt.

### Content creator

You manage scripts, prompts, character notes, video assets, and publishing workflows. Codex can find the right project memory before generating new work.

### AI workflow builder

You want a repeatable structure that makes Codex more consistent across new chats, new windows, and new projects.

## Included Scripts

```text
init_memory_workspace.py     Create a memory workspace.
new_project.py               Add a new project with all required memory files.
session_snapshot.py          Append an end-of-session handoff.
validate_memory_workspace.py Check that required files exist.
```

## Benefits

- Faster new-session recovery
- Less repeated explanation
- Better multi-project routing
- More durable decisions
- Cleaner handoffs between sessions
- Lower prompt bloat
- Easier onboarding for new Codex users
- Better separation between active context and archived history

## What This Is Not

This is not magic hidden memory.

Codex can only reliably recover what is written into files. This project gives you a practical structure for saving the right things in the right places.

## Recommended GitHub Topics

If you fork or share this project, useful topics include:

```text
codex
codex-skill
agents-md
project-memory
persistent-memory
ai-agent
context-engineering
developer-tools
session-continuity
```

## Community

If this helps you, star the repository so more Codex users can find it.

Open an Issue for bugs, missing templates, or workflow ideas. Use Discussions for examples, setup questions, and improvement suggestions.

## Contact And Setup Help

Need help setting up Codex Smart Project Memory, customizing it for your own workflow, or building a smarter Codex project system?

Contact:

- WeChat: `snn6882`

WhatsApp contact can be added here later.

Tip: keep the public repository professional. Use contact links for real setup help, examples, support, and community building.

## License

MIT
