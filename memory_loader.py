"""
memory_loader.py — JERRY-MEMORY Context Loader
Reads all markdown files from the JERRY-MEMORY vault and prints a clean
context block. Run this at the start of any Claude Code session to restore full context.

Usage:
    python memory_loader.py
"""

import os
from pathlib import Path
from datetime import datetime

VAULT_PATH = Path(r"C:\Users\Rachel\Desktop\JERRY-MEMORY")

FILES = [
    ("preferences.md", "PREFERENCES & RECURRING INSTRUCTIONS"),
    ("projects.md",    "PROJECTS"),
    ("people.md",      "PEOPLE"),
    ("ideas.md",       "IDEAS & FUTURE PLANS"),
    ("session-log.md", "SESSION LOG"),
]

DIVIDER = "=" * 70


def load_file(filename: str) -> str:
    path = VAULT_PATH / filename
    if path.exists():
        return path.read_text(encoding="utf-8").strip()
    return f"(file not found: {filename})"


def main():
    print(DIVIDER)
    print("  JERRY-MEMORY — Claude Code Context Restore")
    print(f"  Loaded: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(DIVIDER)

    for filename, title in FILES:
        print(f"\n{'─' * 70}")
        print(f"  {title}")
        print(f"{'─' * 70}")
        content = load_file(filename)
        # Print first 80 lines to keep output manageable
        lines = content.splitlines()
        if len(lines) > 80:
            print("\n".join(lines[:80]))
            print(f"\n... ({len(lines) - 80} more lines — open {filename} for full content)")
        else:
            print(content)

    print(f"\n{DIVIDER}")
    print("  Memory loaded. JERRY is ready.")
    print(DIVIDER)


if __name__ == "__main__":
    main()
