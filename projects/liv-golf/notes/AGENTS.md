# Agent Instructions — Notes Repo

This file tells any AI agent how this repository works and what to do with it. Read this first before touching anything else in the repo.

---

## What this repo is

A personal knowledge management system for Matt Saunders. It captures meeting notes, project status, and action items from multiple sources and organises them into a portable, app-agnostic markdown repository.

**Source of truth:** `/Users/mattsaunders/Library/CloudStorage/OneDrive-Livgolf/notes/`
**Local mirror:** `/Users/mattsaunders/Desktop/Vibe Coded Stuff/notes/`

---

## Repo structure

```
notes/
├── AGENTS.md              ← You are here. Read this first.
├── README.md              ← Index of all meetings and projects
├── meetings/
│   └── 2026/             ← One .md file per meeting, named YYYY-MM-DD-title-slug.md
├── projects/             ← One .md file per project/workstream
├── people/               ← One .md file per person; running 1:1 and relationship notes
│   └── README.md         ← Index of all people docs
├── inbox/                ← Drop zone for emails, attachments, and offline notes
│   ├── README.md         ← Instructions for Matt on how to use the inbox
│   └── processed/        ← Files moved here after processing, with timestamp prefix
└── reference/            ← (future) Evergreen reference docs
```

---

## Input sources

### 1. Granola (automated)
Granola is a meeting notes app. The scheduled task uses the Granola MCP tool to pull new meeting notes automatically. No manual action needed from Matt.

- Use `list_meetings` with `time_range: "last_30_days"` to find new meetings
- Compare against existing files in `meetings/2026/` to identify what's new
- Use `get_meetings` (up to 10 IDs at a time) to fetch full content
- Create one `.md` file per meeting using the meeting note format below

### 2. Inbox drop folder (manual)
Matt drops files into `inbox/` when he wants to capture updates from emails, Teams messages, Slack threads, or offline conversations. He may also paste rough notes into a `.txt` file.

**Supported file types:**
- `.txt` — plain text notes, pasted email bodies, or rough offline notes
- `.eml` / `.msg` — emails dragged from Outlook
- `.pdf` — PDF attachments or documents
- `.docx` — Word documents
- `.pptx` — PowerPoint decks
- `.xlsx` — spreadsheets
- Images (`.png`, `.jpg`) — screenshots, photos of whiteboards

**How Matt captures things:**
- **Emails:** drag from Outlook into `inbox/` as `.eml`, or File → Save As `.txt`
- **Teams/Slack:** copy thread, paste into a `.txt` file, drop in `inbox/`
- **Offline/1:1 conversations:** open TextEdit or any text editor, jot down what happened, save as `.txt` into `inbox/`. No special format required — rough notes are fine.
- **Attachments:** drop alongside the email/notes file; they'll be processed together

**Format of offline notes:**
Matt writes free-form. There is no required structure. A typical file might look like:

```
1:1 with Barry - CRM deck is ready, wants to present to Denise end of next week

Teams thread with Nick re: website - Andrew available to embed with Fantasy Co from Monday

Quick call with Denise - she wants the GlobalLogic proposal to go through legal first,
could add 2 weeks to timeline
```

The agent should extract meaning from context, not rely on formatting.

---

## What to do with inbox files

1. Read the file and extract the key information
2. Identify which project(s) in `projects/` each item relates to
3. Identify which people in `people/` are mentioned or relevant
4. Update the relevant project doc(s) — see project doc format below
5. Update the relevant person doc(s) — see people doc format below
6. Move the processed file to `inbox/processed/YYYY-MM-DD-HH-MM-[original-filename]`
7. If a file represents a genuinely new workstream (not just a one-off), create a new project file
8. If a new person appears who doesn't have a doc yet, create one
9. If a file cannot be read, move it to `inbox/processed/` with a `.unreadable` suffix

---

## Meeting note format

```markdown
# [Meeting Title]

**Date:** [Month DD, YYYY]
**Attendees:** [List from known_participants]
**Source:** Granola — `[meeting-id]`

---

## [Section heading from summary]

[Content...]

---

## Action Items

- [ ] [Action item]

---

*Notes captured via Granola · Exported to markdown repo*
```

**Rules:**
- Use summary sections as-is, reformatted with `##` headers
- If `private_notes` exist, include as a blockquote in a relevant section
- Pull action items into a checklist at the bottom
- Filename: lowercase, hyphens only, no special characters (e.g. `2026-03-10-web-cutover-plan.md`)

---

## Project doc format

Each project doc uses a **Components table + two-level structure**. The Components table gives an at-a-glance status of each sub-workstream. The strategic section is readable in 30 seconds. The tactical section has the full detail.

```markdown
# [Project Title]

**Status:** [🟢 On Track | 🟡 At Risk | 🔴 Blocked | ⏸️ On Hold | ✅ Complete]
**Owner:** [Name]
**Last updated:** [YYYY-MM-DD]

---

## Components

| Component | Status | Owner | Notes |
|-----------|--------|-------|-------|
| [Component name] | 🟢 On Track | [Name] | One-line note |

---

> [2-3 sentence executive summary: what it is, why it matters, where it stands right now.]

### Goal
[One clear sentence: what does success look like for this project?]

### Status
[One tight paragraph — the most important thing happening right now, any critical blockers, and the next major milestone. No bullet points.]

### Key Decisions
- [3-5 most consequential decisions only, with approximate dates.]

### Open Questions
- [Strategic questions requiring a leadership decision only.]

---
---

## Tactical Detail

*Tracks incremental progress, meeting history, and granular action items.*

### Recent Updates
[Bullet list of notable developments, reverse-chronological.]

### Meeting History
| Date | Meeting | Key Outcome |
|------|---------|-------------|
| YYYY-MM-DD | [linked title](../meetings/YYYY/filename.md) | One-line summary |

---
*Part of the [notes repo](../README.md)*
```

**When updating an existing project:**
- **Components table:** update status emoji and notes for any component that changed.
- **Strategic Summary:** only update if something materially changed — a new decision, a new blocker, a milestone hit or missed.
- **Tactical Detail:** always add new meetings to Meeting History and add bullets to Recent Updates for anything noteworthy.
- Always update the overall Status emoji and Last updated date.
- For `misc.md` — update the relevant component row and add a bullet under Recent Updates. Only spin off a new project file if the workstream becomes a primary focus.

**When creating a new project:**
- Use the full template above and add a row to the Projects Index in `README.md`
- For small new workstreams, add as a component to `misc.md` first; graduate to its own file if it grows

---

## People doc format

Each person has a running doc in `people/firstname-lastname.md` that consolidates everything across all interactions.

```markdown
# [Full Name]

**Role:** [Title]
**Organisation:** [Company]
**Relationship:** [Direct report | Manager | Vendor | Partner | External]
**Last interaction:** [YYYY-MM-DD]

---

## Context
[2-3 sentences: who this person is, what their role means for Matt, and the nature of their working relationship.]

## Key Themes
[Bullet list of main topics, tensions, or threads that have come up across interactions. Things worth remembering going into a 1:1.]

## Talking Points
[Bullet list of topics Matt wants to raise in the next interaction. Clear these out after the meeting and move resolved items to 1:1 Notes.]

## Open Items
[Bullet list of anything currently in flight between Matt and this person — commitments, things being waited on, unresolved discussions.]

## 1:1 Notes

*Running log of key points from each 1:1 — most recent first.*

### [YYYY-MM-DD] — [Meeting title or brief description]
[Key points, decisions, things that were said. Free-form prose or bullets. Enough detail to jog memory before the next 1:1.]

## Interaction History
| Date | Meeting | Notes |
|------|---------|-------|
| YYYY-MM-DD | [linked title](../meetings/2026/filename.md) | One-line summary of their role in this meeting |

---
*Part of the [notes repo](../README.md)*
```

**When updating a person doc after a new meeting or inbox file:**
- Add the new meeting/interaction to Interaction History (most recent first)
- Add a dated entry to 1:1 Notes with key points from the meeting
- Update Key Themes if new patterns emerge
- Update Talking Points — add anything that came up to discuss next time
- Update Open Items — add new ones, remove any that are clearly resolved
- Update Last interaction date

**When creating a new person doc:**
- Use the full template above
- Add a row to the relevant section in `people/README.md`
- Only create docs for people with meaningful ongoing relationships — not one-off mentions

---

## Existing projects

| File | Project |
|------|---------|
| `apex-app.md` | Apex App (iOS, Android, Connected Devices) |
| `apex-web.md` | Apex Web (new website; launches May 2026) |
| `legacy-web.md` | Legacy Web (D3 site; running until May cutover) |
| `fantasy-game.md` | Fantasy Game / LIV Golf Play |
| `streaming.md` | Streaming / OTT Infrastructure |
| `nyu-entrepreneurship-lab.md` | NYU Entrepreneurship Lab |
| `personal-projects.md` | Personal Projects |
| `misc.md` | Misc (catch-all: Pulse Live, CRM, OKGC rebrand, GlobalLogic, etc.) |

When routing updates, read the existing project files to understand current context before making changes. When a new meeting or inbox item touches something in `misc.md`, update the relevant component row in the Components table and add a bullet to Recent Updates.

---

## After all updates are complete

1. Update `README.md` — add new meetings to the Meetings Index, add new projects to the Projects Index
2. Mirror to local backup:
```bash
rsync -av --delete \
  "<base>/" \
  "/sessions/<session-id>/mnt/Vibe Coded Stuff/notes/"
```

---

*Last updated: 2026-03-12*
