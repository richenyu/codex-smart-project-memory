# Operating Rules

## End-of-Session Snapshot

Write a snapshot when the work creates durable value:

- important decision
- user preference
- reusable workflow
- new product direction
- project state change
- file or asset that future sessions must find

Use `scripts/session_snapshot.py` for a structured handoff.

## Compaction

When `05_conversation_memory.md` becomes long:

1. Extract durable decisions into `02_decisions.md`.
2. Update `01_current_status.md` with current state and next action.
3. Rewrite `04_context_pack.md` as the concise starter context.
4. Keep old chronological detail in `05_conversation_memory.md` or move stale detail to archive.

Do not delete useful history silently. Mark deprecated decisions when necessary.

## Conflict Handling

When two memory files conflict:

1. Prefer the newest explicit user-confirmed decision.
2. Preserve the older item with a `Deprecated` note if it may explain past work.
3. Update `04_context_pack.md` so new sessions do not repeat the conflict.

## Privacy

Before publishing templates or examples:

- remove private paths
- remove customer data
- remove credentials and API keys
- replace personal project names with generic examples
- avoid copying private conversation text into public files

## Health Check

Run `scripts/validate_memory_workspace.py` after initialization, after adding projects, and before sharing a workspace template.
