# Codex Smart Project Memory

Make Codex feel less like a blank new chat and more like a project-aware coding partner.

Codex Smart Project Memory is a lightweight Codex Skill and `AGENTS.md` workflow that gives Codex persistent project context, smart routing, session handoffs, decision memory, and asset indexes without stuffing every prompt with old conversation history.

> Unofficial community project. Not affiliated with OpenAI.

Built by **RICH**.

## Your Codex Is Smart. But New Sessions Still Forget.

You open a new Codex window.

It does not know what you decided yesterday.

You start a new project.

It does not understand the important logic from your other projects.

You ask it to continue.

It asks basic questions again, scans the same files again, and sometimes feels strangely less capable even though the model is powerful.

The problem is usually not the model.

The problem is missing project memory.

## This Is Not Just One Big Folder

Many users try to fix Codex memory by dumping every project, note, prompt, document, and old conversation into one shared folder.

That usually makes the problem worse.

When Codex has to scan too much at once, it gets more noise, more stale context, more conflicting instructions, and more irrelevant files. The session becomes slower, the prompt gets bloated, and Codex can feel less intelligent because it is carrying the wrong context.

Codex Smart Project Memory is different.

It is not a folder dump. It is a lightweight routing and memory system:

- root files help Codex understand where to start
- project registries help Codex find the right project
- smart routing prevents unnecessary full-folder scans
- context packs keep each project's active memory small
- session snapshots preserve important handoffs
- asset indexes tell Codex where concrete files live only when needed

The goal is not to make Codex read everything.

The goal is to help Codex read the right thing first.

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

## Beginner-Friendly Codex Starter Kit

New to Codex? This project can also work as a practical Codex starter kit.

It gives beginners a ready-made structure for:

- setting up `AGENTS.md`
- organizing project context
- creating a Codex memory workspace
- avoiding giant prompt dumps
- keeping new Codex chats from starting cold
- learning a real context engineering workflow by example

If you are searching for a Codex beginner tool, Codex setup guide, Codex tutorial, AGENTS.md template, or AI coding agent memory workflow, this project is built for that use case.

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

### 6. Big shared folders create context overload

A single folder full of every project can look organized to a human, but it can overload Codex with irrelevant context.

This workflow separates global memory, project memory, handoffs, and assets so Codex can route first and read selectively.

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

## Memory Intelligence Upgrade Workflow

If you already have a messy project folder, a giant memory prompt, or several scattered Codex workspaces, read the [Memory Intelligence Upgrade Workflow](docs/workflows/memory-intelligence-upgrade-workflow.md).

It explains how to choose one canonical memory root, make `AGENTS.md` a startup contract, add smart routing, create project skeletons, validate the system, and keep private data out of public templates.

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

Codex memory, codex-memory, Codex intelligence, make Codex smarter, smarter Codex, context-aware Codex, project-aware Codex, Codex Skill, OpenAI Codex, Codex starter kit, Codex beginner tool, Codex for beginners, Codex tutorial, Codex setup guide, Codex workflow, Codex project memory, persistent memory, agent memory, AI agent memory, AI coding assistant memory, AI coding agent memory, coding agent memory, coding agent context, coding agent starter kit, repo-local memory, markdown memory, `AGENTS.md`, AGENTS.md template, context engineering, project context, session continuity, context loss between sessions, new chat forgets context, agent amnesia, smart project routing, coding agent workflow.

## Common Questions This Helps Answer

People often search for this problem in question form:

- How do I make Codex remember my project context?
- How do I make Codex smarter across new chats?
- How do I stop Codex from starting from zero every session?
- What is the best `AGENTS.md` template for Codex?
- How do I create persistent memory for Codex?
- How do I manage project memory for AI coding agents?
- How do I avoid context overload from one giant project folder?
- How do I keep coding agents from forgetting decisions between sessions?
- How do I build a context-aware AI coding assistant workflow?

Codex Smart Project Memory is designed for these searches: it combines Codex memory, Codex intelligence, `AGENTS.md`, context engineering, smart routing, and session continuity into one beginner-friendly workflow.

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

Built by **RICH**.

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
