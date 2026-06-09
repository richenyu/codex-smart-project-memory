from __future__ import annotations

from datetime import date
from pathlib import Path
import re
import unicodedata


SKILL_DIR = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = SKILL_DIR / "assets" / "templates"

ROOT_REQUIRED_FILES = [
    "AGENTS.md",
    "00_START_HERE.md",
    "00_AUTO_RECOVERY.md",
    "00_PROJECT_DASHBOARD.md",
    "00_SMART_ROUTER.md",
    "00_CATEGORY_REGISTRY.md",
    "00_PROJECT_REGISTRY.md",
    "00_RECOVERY_TEST.md",
    "00_shared_knowledge/00_rules/00_CORE_MEMORY.md",
    "00_shared_knowledge/00_rules/10_USER_PREFERENCES.md",
]

PROJECT_REQUIRED_FILES = [
    "AGENTS.md",
    "00_project_brief.md",
    "01_current_status.md",
    "02_decisions.md",
    "03_cross_links.md",
    "04_context_pack.md",
    "05_conversation_memory.md",
    "06_memory_maintenance.md",
    "07_asset_index.md",
]

CATEGORY_ALIASES = {
    "software": ("C02", "software"),
    "code": ("C02", "software"),
    "app": ("C02", "software"),
    "agent": ("C02", "software"),
    "ai": ("C02", "software"),
    "content": ("C01", "content"),
    "video": ("C01", "content"),
    "writing": ("C01", "content"),
    "creative": ("C01", "content"),
    "business": ("X01", "business"),
    "growth": ("X01", "business"),
    "marketing": ("X01", "business"),
}


def today() -> str:
    return date.today().isoformat()


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
    ascii_value = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_value).strip("-").lower()
    return ascii_value or "project"


def category_pair(category: str) -> tuple[str, str]:
    key = category.strip().lower()
    if key in CATEGORY_ALIASES:
        return CATEGORY_ALIASES[key]
    if re.fullmatch(r"[A-Z]\d{2}", category.strip().upper()):
        return category.strip().upper(), "custom"
    return "C02", slugify(category)


def render_text(text: str, values: dict[str, str]) -> str:
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", value)
    return text


def render_template_tree(template_name: str, destination: Path, values: dict[str, str], overwrite: bool = False) -> list[Path]:
    source = TEMPLATE_DIR / template_name
    if not source.exists():
        raise FileNotFoundError(f"Template folder not found: {source}")
    written: list[Path] = []
    for item in sorted(source.rglob("*")):
        if item.is_dir():
            continue
        rel = item.relative_to(source)
        rendered_parts = [render_text(part, values) for part in rel.parts]
        target = destination.joinpath(*rendered_parts)
        if target.exists() and not overwrite:
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        content = render_text(item.read_text(encoding="utf-8"), values)
        target.write_text(content, encoding="utf-8")
        written.append(target)
    return written


def find_next_project_id(root: Path) -> str:
    highest = 0
    if root.exists():
        for child in root.iterdir():
            if child.is_dir():
                match = re.match(r"P(\d{2})_", child.name)
                if match:
                    highest = max(highest, int(match.group(1)))
    return f"P{highest + 1:02d}"


def append_unique(path: Path, marker: str, text: str) -> bool:
    existing = path.read_text(encoding="utf-8") if path.exists() else ""
    if marker in existing:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(existing.rstrip() + "\n" + text.rstrip() + "\n", encoding="utf-8")
    return True
