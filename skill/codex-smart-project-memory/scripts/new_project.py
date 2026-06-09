from __future__ import annotations

import argparse
from pathlib import Path

from memory_common import (
    append_unique,
    category_pair,
    find_next_project_id,
    render_template_tree,
    slugify,
    today,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a project memory folder and register it.")
    parser.add_argument("--root", required=True, help="Existing memory workspace root.")
    parser.add_argument("--name", required=True, help="Project display name.")
    parser.add_argument("--category", default="software", help="Category alias: software, content, business, or custom code like C02.")
    parser.add_argument("--slug", help="Optional URL/folder-safe slug.")
    parser.add_argument("--status", default="New project. Context needs to be filled in.", help="Initial status.")
    parser.add_argument("--priority", default="Medium", help="Initial priority.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing template files.")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    if not root.exists():
        raise SystemExit(f"Workspace root does not exist: {root}")

    project_id = find_next_project_id(root)
    category_code, category_name = category_pair(args.category)
    slug = args.slug or slugify(args.name)
    project_dir = root / f"{project_id}_{category_code}_{slug}"
    values = {
        "PROJECT_ID": project_id,
        "PROJECT_NAME": args.name,
        "PROJECT_SLUG": slug,
        "CATEGORY_CODE": category_code,
        "CATEGORY_NAME": category_name,
        "PROJECT_STATUS": args.status,
        "PROJECT_PRIORITY": args.priority,
        "PROJECT_PATH": str(project_dir),
        "CREATED_DATE": today(),
    }

    written = render_template_tree("project", project_dir, values, overwrite=args.overwrite)

    registry_row = (
        f"\n| {project_id} | {category_code}_{category_name} | {args.name} | "
        f"`{project_dir}` | {args.status} | `04_context_pack.md`, then `00`-`03`, `05`, `06`, and `07` when assets are needed |"
    )
    append_unique(root / "00_PROJECT_REGISTRY.md", f"| {project_id} |", registry_row)

    dashboard_row = (
        f"\n| {project_id} {args.name} | {category_code}_{category_name} | "
        f"{args.status} | Fill project brief, decisions, and asset index | {args.priority} | "
        f"`{project_dir.name}/04_context_pack.md` |"
    )
    append_unique(root / "00_PROJECT_DASHBOARD.md", f"| {project_id} {args.name} |", dashboard_row)

    router_row = (
        f"\n| {args.name}, {slug}, {category_name} | {project_id} {args.name} | "
        f"{category_code}_{category_name} | `{project_dir.name}/04_context_pack.md`, `07_asset_index.md` when needed |"
    )
    append_unique(root / "00_SMART_ROUTER.md", f"| {args.name}, {slug}, {category_name} |", router_row)

    print(f"Created project memory: {project_dir}")
    print(f"Files written: {len(written)}")
    print("Next: edit 04_context_pack.md so new sessions can recover quickly.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
