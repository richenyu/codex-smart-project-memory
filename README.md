# Codex Smart Project Memory

Make Codex feel less like a blank new chat and more like a project-aware coding partner.

Codex Smart Project Memory is a lightweight Codex Skill and `AGENTS.md` workflow that gives Codex persistent project context, smart routing, session handoffs, decision memory, and asset indexes without stuffing every prompt with old conversation history.

> Unofficial community project. Not affiliated with OpenAI.

## Your Codex Is Smart. But New Sessions Still Forget.

You open a new Codex window.

It does not know what you decided yesterday.

You start a new project.

It does not understand the important logic from your other projects.

You ask it to continue.

It asks basic questions again, scans the same files again, and sometimes feels strangely less capable even though the model is powerful.

The problem is usually not the model.

The problem is missing project memory.

## Give Codex A Lightweight Project Brain

Codex Smart Project Memory turns your important project logic into small, durable files that Codex can read quickly at the start of a session.

Instead of pasting a giant prompt every time, you get a clean memory system:

- global startup rules
- project registries
- smart project routing
- context packs for each project
- decision logs
- session snapshots
- asset indexes
- memory maintenance rules
- scripts to initialize and validate everything

The result: Codex can recover context faster, understand your project structure, and continue work with fewer repeated explanations.

## Try It In 3 Minutes

Clone this repository, install or copy the Skill folder, then ask Codex:

```text
Use $codex-smart-project-memory to initialize a smart project memory workspace for my Codex projects.
```

Or run the scripts directly:

```bash
python skill/codex-smart-project-memory/scripts/init_memory_workspace.py --root ./CodexProjectMemory --root-name "My Codex Memory"
python skill/codex-smart-project-memory/scripts/new_project.py --root ./CodexProjectMemory --name "My First Project" --category software
python skill/codex-smart-project-memory/scripts/validate_memory_workspace.py --root ./CodexProjectMemory
```

If it helps you, star the repository so more Codex users can find it.

## What It Fixes

### 1. New chats lose context

A fresh Codex session often does not know your previous decisions, current project state, or next steps.

This system gives each project a `04_context_pack.md` file so new sessions can recover the important context first.

### 2. Multi-project work gets messy

When you manage several apps, agents, content workflows, or business ideas, Codex may not know which project you mean.

This system adds a project registry and smart router so vague requests can be routed to the right project without scanning everything.

### 3. Important decisions disappear

Decisions buried in chat history are hard to reuse.

This system gives you `02_decisions.md` and `05_conversation_memory.md` so durable decisions and handoffs can survive across sessions.

### 4. Prompts become too large

A giant memory prompt can become slow, stale, and painful to maintain.

This system uses small files and progressive context loading, so Codex reads only what the task needs.

### 5. Codex feels less intelligent than it should

When an assistant lacks context, it repeats work, asks basic questions, and misses the user's real intent.

This workflow gives Codex the project context it needs to act more intelligently.

## Before And After

Before:

```text
You: Continue the project.
Codex: What project is this? What did we decide? Where are the files?
You: Let me paste the context again...
```

After:

```text
You: Continue the project.
Codex: I will read the startup chain, route to the project, load the context pack, and continue from the latest snapshot.
```

## What You Get

This repository includes a ready-to-use Codex Skill plus a reusable memory architecture:

```text
skill/codex-smart-project-memory/
  SKILL.md
  agents/openai.yaml
  scripts/
  references/
  assets/templates/
```

Included scripts:

```text
init_memory_workspace.py     Create a memory workspace.
new_project.py               Add a new project with all required memory files.
session_snapshot.py          Append an end-of-session handoff.
validate_memory_workspace.py Check that required files exist.
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

## Who Should Use This

Use Codex Smart Project Memory if you are:

- a developer working across many repositories
- a founder building several AI products at once
- a creator managing scripts, prompts, videos, and assets
- a team using Codex for product, engineering, content, or operations
- a power user who wants Codex memory without giant prompts
- anyone who wants better Codex session continuity and context engineering

## Why It Works

Most AI memory workflows try to save everything.

This one saves the right things:

- what the project is
- what the current state is
- what decisions were made
- where important files live
- what the user prefers
- what the next session should read first

That keeps Codex memory fast, explicit, searchable, and easy to maintain.

## Benefits

- Faster new-session recovery
- Less repeated explanation
- Better multi-project routing
- More durable decisions
- Cleaner handoffs between sessions
- Lower prompt bloat
- Easier onboarding for new Codex users
- Better separation between active context and archived history
- A practical `AGENTS.md` workflow for persistent project memory

## What This Is Not

This is not magic hidden memory.

Codex can only reliably recover what is written into files. This project gives you a practical structure for saving the right things in the right places.

## Search Keywords

Codex memory, Codex Skill, Codex project memory, persistent memory, AI agent memory, `AGENTS.md`, context engineering, project context, session continuity, smart project routing, developer tools, coding agent workflow.

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

## Download And Try It

If you want Codex to stop starting from zero, try Codex Smart Project Memory today:

1. Star this repository.
2. Clone or download the project.
3. Install or copy the Skill folder.
4. Initialize your memory workspace.
5. Add your first project.
6. Start your next Codex session with real project context.

## Community

Open an Issue for bugs, missing templates, or workflow ideas. Use Discussions for examples, setup questions, and improvement suggestions.

## Free Bonus And Setup Help

Want more Codex memory workflows, setup examples, and practical prompt patterns?

I am preparing a free bonus pack for early users, including:

- a Codex memory setup checklist
- extra `AGENTS.md` workflow examples
- project memory templates for different use cases
- session handoff prompt patterns
- tips for making Codex feel smarter across new chats and projects

If you want the bonus pack or need help adapting this workflow to your own projects, contact me:

- WeChat: `snn6882`

WhatsApp and Telegram contact can be added here later.

## License

MIT
