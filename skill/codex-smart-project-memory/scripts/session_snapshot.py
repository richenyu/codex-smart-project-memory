from __future__ import annotations

import argparse
from pathlib import Path

from memory_common import today


def main() -> int:
    parser = argparse.ArgumentParser(description="Append a compact session handoff to 05_conversation_memory.md.")
    parser.add_argument("--project", required=True, help="Project memory folder.")
    parser.add_argument("--title", default="Session snapshot", help="Snapshot title.")
    parser.add_argument("--summary", help="Short summary. If omitted, use --summary-file.")
    parser.add_argument("--summary-file", help="Read summary text from a file.")
    parser.add_argument("--next", default="", help="Recommended next action.")
    parser.add_argument("--decisions", default="", help="Key decisions, separated by semicolons.")
    parser.add_argument("--files", default="", help="Important files touched, separated by semicolons.")
    args = parser.parse_args()

    project = Path(args.project).expanduser().resolve()
    if not project.exists():
        raise SystemExit(f"Project folder does not exist: {project}")

    if args.summary:
        summary = args.summary.strip()
    elif args.summary_file:
        summary = Path(args.summary_file).read_text(encoding="utf-8").strip()
    else:
        raise SystemExit("Provide --summary or --summary-file.")

    target = project / "05_conversation_memory.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    if not target.exists():
        target.write_text("# 05 Conversation Memory\n\n", encoding="utf-8")

    block = [
        f"## {today()} - {args.title}",
        "",
        "### Summary",
        summary,
        "",
    ]
    if args.decisions:
        block.extend(["### Decisions", args.decisions, ""])
    if args.files:
        block.extend(["### Files", args.files, ""])
    if args.next:
        block.extend(["### Next", args.next, ""])

    with target.open("a", encoding="utf-8") as handle:
        handle.write("\n" + "\n".join(block).rstrip() + "\n")

    print(f"Appended snapshot: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
