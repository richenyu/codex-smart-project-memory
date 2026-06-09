from __future__ import annotations

import argparse
from pathlib import Path

from memory_common import render_template_tree, today


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize a Codex smart project memory workspace.")
    parser.add_argument("--root", required=True, help="Workspace root to create.")
    parser.add_argument("--root-name", default="Codex Project Memory", help="Human-friendly workspace name.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing template files.")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    values = {
        "ROOT_NAME": args.root_name,
        "ROOT_PATH": str(root),
        "CREATED_DATE": today(),
    }
    written = render_template_tree("root", root, values, overwrite=args.overwrite)
    print(f"Initialized memory workspace: {root}")
    print(f"Files written: {len(written)}")
    print("Next: run new_project.py to add the first project.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
