from __future__ import annotations

import re
import sys
from pathlib import Path


FRONTMATTER_RE = re.compile(
    r"\A---\n(.*?)\n---\n",
    re.DOTALL,
)

REQUIRED_FRONTMATTER_KEYS = ("name", "description")
REQUIRED_OPENAI_KEYS = (
    "display_name",
    "short_description",
    "default_prompt",
)

FORBIDDEN_PATTERNS = (
    r"[A-Za-z]:\\",
    r"\.cc-switch",
    r"\.codex",
    r"MiniMax",
    r"obra/",
)


def fail(message: str) -> None:
    print(f"[FAIL] {message}")
    raise SystemExit(1)


def ok(message: str) -> None:
    print(f"[OK] {message}")


def load_text(path: Path) -> str:
    if not path.exists():
        fail(f"Missing file: {path}")
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str, path: Path) -> dict[str, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        fail(f"Invalid frontmatter block: {path}")

    items: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line or ":" not in line:
            continue

        key, value = line.split(":", 1)
        items[key.strip()] = value.strip().strip('"').strip("'")

    for key in REQUIRED_FRONTMATTER_KEYS:
        if not items.get(key):
            fail(f"Missing frontmatter key '{key}' in {path}")

    return items


def validate_openai_yaml(path: Path) -> None:
    text = load_text(path)

    if "interface:" not in text:
        fail(f"Missing 'interface' block in {path}")

    for key in REQUIRED_OPENAI_KEYS:
        if not re.search(rf"^\s*{re.escape(key)}\s*:", text, re.MULTILINE):
            fail(f"Missing key '{key}' in {path}")

    ok(f"openai metadata present: {path}")


def validate_references(skill_text: str, skill_dir: Path) -> None:
    refs = re.findall(r"`(references/[^`]+)`", skill_text)
    for ref in refs:
        ref_path = skill_dir / ref
        if not ref_path.exists():
            fail(f"Referenced file not found: {ref_path}")

    ok("all referenced files exist")


def validate_forbidden_patterns(root: Path) -> None:
    for path in root.rglob("*"):
        if not path.is_file():
            continue

        text = load_text(path)
        for pattern in FORBIDDEN_PATTERNS:
            if re.search(pattern, text):
                fail(
                    f"Forbidden publish pattern '{pattern}' found in {path}"
                )

    ok("no forbidden publish patterns found")


def main() -> None:
    if len(sys.argv) != 2:
        fail("Usage: python scripts/validate_skill.py <skill-path>")

    skill_dir = Path(sys.argv[1]).resolve()
    if not skill_dir.is_dir():
        fail(f"Skill directory not found: {skill_dir}")

    skill_md = skill_dir / "SKILL.md"
    skill_text = load_text(skill_md)
    frontmatter = parse_frontmatter(skill_text, skill_md)

    if frontmatter["name"] != skill_dir.name:
        fail(
            "Skill folder name must match frontmatter name: "
            f"{skill_dir.name} != {frontmatter['name']}"
        )

    ok(f"frontmatter valid: {skill_md}")
    validate_openai_yaml(skill_dir / "agents" / "openai.yaml")
    validate_references(skill_text, skill_dir)
    validate_forbidden_patterns(skill_dir)

    print("[DONE] Skill validation passed")


if __name__ == "__main__":
    main()
