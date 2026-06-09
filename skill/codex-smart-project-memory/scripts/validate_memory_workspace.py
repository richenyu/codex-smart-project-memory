from __future__ import annotations

import argparse
from pathlib import Path
import re

from memory_common import PROJECT_REQUIRED_FILES, ROOT_REQUIRED_FILES


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Codex smart project memory workspace.")
    parser.add_argument("--root", required=True, help="Memory workspace root.")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    errors: list[str] = []

    if not root.exists():
        raise SystemExit(f"Workspace root does not exist: {root}")

    for rel in ROOT_REQUIRED_FILES:
        if not (root / rel).exists():
            errors.append(f"Missing root file: {rel}")

    project_dirs = [p for p in root.iterdir() if p.is_dir() and re.match(r"P\d{2}_", p.name)]
    if not project_dirs:
        errors.append("No project memory folders found. Run new_project.py.")

    for project in project_dirs:
        for rel in PROJECT_REQUIRED_FILES:
            if not (project / rel).exists():
                errors.append(f"Missing project file: {project.name}/{rel}")

    if errors:
        print("Memory workspace validation failed:")
        for item in errors:
            print(f"[MISSING] {item}")
        return 1

    print(f"Memory workspace validation passed: {root}")
    print(f"Projects checked: {len(project_dirs)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
