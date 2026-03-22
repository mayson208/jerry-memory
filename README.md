# JERRY-MEMORY — Claude Code Persistent Memory Vault

This folder is Rachel's persistent memory system for Claude Code (JERRY AI assistant sessions).

## How It Works

1. **At session start** — Claude reads CLAUDE.md in the project folder to restore full context
2. **During session** — Claude updates memory files as new info is learned
3. **After session** — Memory files are updated and pushed to GitHub for backup

## Files

| File | Purpose |
|------|---------|
| `projects.md` | Active and queued projects with status |
| `preferences.md` | Rachel's preferences and recurring instructions |
| `session-log.md` | Log of every session with date and summary |
| `people.md` | Important people in Rachel's life |
| `ideas.md` | Future project ideas and plans |

## Manual Memory Load

Run this to print a full context summary in any terminal:

```bash
python memory_loader.py
```

## GitHub Backup

This vault is backed up to GitHub at: https://github.com/mayson208/jerry-memory

Push after every update:
```bash
cd C:\Users\Rachel\Desktop\JERRY-MEMORY
git add -A && git commit -m "memory: update" && git push
```

## Rules for Claude

- Always read CLAUDE.md at the start of every session
- Always update relevant memory files after meaningful changes
- Never store actual API keys — only their locations
- Always commit and push after updates
