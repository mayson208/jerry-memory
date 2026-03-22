"""
memory_saver.py — Auto-save session context to JERRY-MEMORY vault.
Run by Claude Code Stop hook at end of every session.
"""

import os
import json
import datetime

VAULT = r"C:\Users\Rachel\Desktop\JERRY-MEMORY"
SESSIONS_DIR = os.path.join(VAULT, "06-Sessions")
INDEX_FILE = os.path.join(SESSIONS_DIR, "_INDEX.md")


def get_today():
    return datetime.date.today().isoformat()


def ensure_session_file():
    """Create today's session file if it doesn't exist."""
    today = get_today()
    session_file = os.path.join(SESSIONS_DIR, f"{today}.md")

    if not os.path.exists(session_file):
        content = f"""# Session — {today}

## Summary
*(auto-created by memory_saver.py)*

## What Happened
-

## Decisions Made
-

## What Claude Learned
-

## Research Done
*(link to any new files in 02-Research/)*

## Next Steps for Rachel
1.
"""
        with open(session_file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[memory_saver] Created session file: {today}.md")
    else:
        print(f"[memory_saver] Session file already exists: {today}.md")

    return session_file


def update_session_index():
    """Add today's session to the index if not already there."""
    today = get_today()
    entry = f"- [{today}]({today}.md)\n"

    if not os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, "w", encoding="utf-8") as f:
            f.write("# Sessions Index\n\n")

    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    if today not in content:
        with open(INDEX_FILE, "a", encoding="utf-8") as f:
            f.write(entry)
        print(f"[memory_saver] Added {today} to sessions index")


def update_home_dashboard():
    """Update the last-updated timestamp on the vault home."""
    home_file = os.path.join(VAULT, "00-HOME.md")
    if not os.path.exists(home_file):
        return

    with open(home_file, "r", encoding="utf-8") as f:
        content = f.read()

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    import re
    updated = re.sub(
        r"\*\*Last updated:\*\* .*",
        f"**Last updated:** {now}",
        content
    )

    if updated != content:
        with open(home_file, "w", encoding="utf-8") as f:
            f.write(updated)
        print(f"[memory_saver] Updated home dashboard timestamp")


if __name__ == "__main__":
    print("[memory_saver] Running end-of-session save...")
    os.makedirs(SESSIONS_DIR, exist_ok=True)
    ensure_session_file()
    update_session_index()
    update_home_dashboard()
    print("[memory_saver] Done.")
