"""Validate the small Claude Code plugin package without external dependencies."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / ".claude-plugin" / "plugin.json"
SKILLS = ROOT / "skills"
FORBIDDEN = (".claude/plugins/cache", "USERPROFILE", "xsec_token", "baoyu-fetch")


def frontmatter(text: str) -> tuple[dict[str, str], str]:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("SKILL.md must begin with YAML frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError as error:
        raise ValueError("SKILL.md frontmatter is missing its closing delimiter") from error

    fields: dict[str, str] = {}
    for line in lines[1:end]:
        match = re.fullmatch(r"([a-z][a-z0-9-]*):\s*(.+)", line)
        if not match:
            raise ValueError(f"Unsupported or invalid frontmatter line: {line}")
        fields[match.group(1)] = match.group(2)
    return fields, "\n".join(lines[end + 1 :])


def validate() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for field in ("name", "version", "description"):
        if not isinstance(manifest.get(field), str) or not manifest[field].strip():
            raise ValueError(f"plugin.json requires a non-empty {field}")

    skill_files = sorted(SKILLS.glob("*/SKILL.md"))
    if not skill_files:
        raise ValueError("No skills/<name>/SKILL.md files found")

    for skill_file in skill_files:
        fields, body = frontmatter(skill_file.read_text(encoding="utf-8"))
        name = fields.get("name", "")
        description = fields.get("description", "")
        if name != skill_file.parent.name:
            raise ValueError(f"Skill name must match its directory: {skill_file}")
        if not description:
            raise ValueError(f"Skill description is required: {skill_file}")
        if "xhs-video-transcribe" not in body:
            raise ValueError(f"Skill must invoke the published CLI: {skill_file}")
        content = fields["description"] + "\n" + body
        for value in FORBIDDEN:
            if value.lower() in content.lower():
                raise ValueError(f"Private downloader or local-path reference found: {value}")


if __name__ == "__main__":
    validate()
    print("Claude Code plugin structure and skill boundaries are valid.")
