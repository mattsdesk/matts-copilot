# Project: LIV Golf
**Type:** Internal
**Status:** Active
**Owner:** Matt Saunders
**Last Updated:** 2026-03-19

---

## Brief

Matt is SVP of Direct to Consumer at LIV Golf, responsible for the app, website, video streaming, and broader DTC programs. CoPilot supports his work by reading context from the notes mirror and producing polished, immediately usable outputs -- strategy docs, memos, analysis, and meeting prep.

## Goals

- Synthesize meeting and project context into actionable strategy and analysis
- Help Matt prepare for meetings, draft memos, and think through decisions
- Maintain strategic continuity in memory.md across sessions

## Overview

Matt's DTC responsibilities span four workstreams:

| Workstream | Notes Project File(s) |
|---|---|
| App | `notes/projects/apex-app.md` |
| Website | `notes/projects/apex-web.md`, `notes/projects/legacy-web.md` |
| Video / Streaming | `notes/projects/streaming.md` |
| Other DTC Programs | `notes/projects/fantasy-game.md`, `notes/projects/misc.md` |

People and 1:1 history live in `notes/people/`. Meetings live in `notes/meetings/2026/`.

---

## Notes System

The `notes/` folder in this project is a mirror of Matt's full notes system. It is the primary context source for all LIV Golf work.

**Read `notes/AGENTS.md` before working with notes files -- it explains the full structure and conventions.**

Key paths:
- **Projects:** `notes/projects/`
- **People/1:1s:** `notes/people/`
- **Meetings:** `notes/meetings/2026/`
- **Inbox:** `notes/inbox/`

**The notes mirror is read-only in CoPilot.** All updates to notes happen in the source system (`/Users/mattsaunders/Library/CloudStorage/OneDrive-Livgolf/notes/`). To sync the mirror before committing, run:

```bash
rsync -av --delete \
  "/Users/mattsaunders/Desktop/Vibe Coded Stuff/notes/" \
  "/Users/mattsaunders/Desktop/Vibe Coded Stuff/Matt's CoPilot/projects/liv-golf/notes/"
```

---

> **INSTRUCTIONS FOR CLAUDE:**
> - Do NOT modify the structure or headings of this file
> - At the start of every session: read the relevant project file(s) from `notes/projects/` and the relevant person file(s) from `notes/people/` based on what Matt is working on -- then read `memory.md` -- summarize relevant prior context in 1-3 bullets before starting work
> - Do NOT modify any files inside `notes/` -- that is a read-only mirror in this system
> - Pull meeting context by reading specific files from `notes/meetings/2026/`
> - All polished outputs go in `deliverables/`
> - Reference `/shared/brand-voice.md` and `/shared/tone-guidelines.md` for all written output
> - After meaningful work, append a summary to the Session Log in `memory.md`
