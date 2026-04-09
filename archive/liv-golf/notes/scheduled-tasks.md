# Scheduled Tasks

> A record of all automated Claude tasks. Use this to recreate your setup on a new machine.
>
> **Last updated:** 2026-04-01 (added daily-brain-dump task)

---

## How Scheduled Tasks Work

Scheduled tasks are created in the Claude desktop app (Cowork mode). Each task:
- Has a unique `taskId` (kebab-case)
- Runs on a cron schedule (evaluated in your **local timezone**)
- Stores its full prompt in a SKILL.md file on your Mac at:
  `~/Documents/Claude/Scheduled/{taskId}/SKILL.md`

To recreate tasks on a new machine, use the **Schedule skill** in a Cowork session and paste the prompt from the SKILL.md file.

---

## Active Tasks

### `granola-notes-sync`

| Field | Value |
|-------|-------|
| **Description** | Sync new Granola meetings to the markdown notes repo |
| **Schedule** | Weekdays (Mon–Fri) at 8:30 AM and 5:30 PM |
| **Cron** | `30 8,17 * * 1-5` |
| **Status** | ✅ Enabled |
| **Prompt file** | `~/Documents/Claude/Scheduled/granola-notes-sync/SKILL.md` |

**Purpose:** Pulls new Granola meeting notes and syncs them into the local markdown knowledge base (this notes repo), keeping `notes/meetings/2026/` up to date automatically.

**Full prompt:**

```
## Start here

Find the notes repo by running:
```
ls "/sessions/*/mnt/Vibe Coded Stuff/Matt's CoPilot/projects/liv-golf/notes/"
```
Use the result as `<base>`.

Then read the agent instructions file before doing anything else:
```
<base>/AGENTS.md
```

AGENTS.md contains the full specification for this repo — meeting note format, project doc format, people doc format, inbox processing rules, and everything else you need. Follow it precisely.

## Your job this run

1. **Sync Granola** — pull any new meeting notes using the Granola MCP `list_meetings` tool (`time_range: "last_30_days"`), compare against existing files in `<base>/meetings/2026/`, fetch and write any new ones

2. **Process inbox** — check `<base>/inbox/` for any files (excluding README.md and the `processed/` subfolder), process each one, move to `inbox/processed/` when done

3. **Update project docs** — update relevant files in `<base>/projects/` for all new content; create new project files if needed

4. **Update people docs** — for every new meeting or inbox file, update the relevant person docs in `<base>/people/`; add to Interaction History, update Key Themes and Open Items; create a new person doc if someone new appears who warrants one; add them to `people/README.md`

5. **Update README.md** — add new meetings to Meetings Index; add new projects to Projects Index if any were created

Full instructions for all of the above are in AGENTS.md.
```

---

### `music-biz-monitor`

| Field | Value |
|-------|-------|
| **Description** | Weekly scan for music-related small businesses for sale near Montclair, NJ |
| **Schedule** | Fridays at 9:00 AM |
| **Cron** | `0 9 * * 5` |
| **Status** | ✅ Enabled |
| **Prompt file** | `~/Documents/Claude/Scheduled/music-biz-monitor/SKILL.md` |

**Purpose:** Weekly automated search for music-related small business acquisition opportunities (studios, shops, schools, etc.) near Montclair, NJ.

**Full prompt:**

```
You are monitoring business-for-sale listings for music-related small businesses within approximately 1 hour's drive of Montclair, New Jersey (Essex County, NJ).

## Important: Search-Only Approach
Direct access to listing sites (BizBuySell, BizQuest, etc.) is blocked. You must rely entirely on **web search results** — do NOT attempt to use WebFetch to open any listing URLs. Extract all available information (business type, location, asking price, description, URL) directly from the search result snippets returned by WebSearch. The URLs in search results will be direct links to individual listings, which is what we want.

## Objective
Run targeted web searches to surface music retail or music school/lessons businesses listed for sale within the target geography. Compile a clean weekly digest with direct listing URLs so the user can click through and verify details themselves.

## Target Business Types
- **Music retail**: instrument shops, guitar stores, pro audio/gear shops, sheet music stores, DJ/PA equipment retailers, music accessory shops
- **Music schools / lessons**: music academies, lesson studios, tutoring centers with music focus, after-school music programs, private lesson businesses

## Target Geography
Within approximately 1 hour drive of Montclair, NJ 07042:
- Northern/central New Jersey (Essex, Bergen, Morris, Passaic, Union, Somerset, Middlesex, Monmouth counties)
- New York City boroughs (Manhattan, Brooklyn, Queens, Staten Island, Bronx)
- Westchester County, NY
- Rockland County, NY

## Search Queries to Run
Run ALL of the following searches using the WebSearch tool:

1. `site:bizbuysell.com music store New Jersey`
2. `site:bizbuysell.com music school New Jersey`
3. `site:bizbuysell.com instrument shop New Jersey`
4. `site:bizbuysell.com music store New York City`
5. `site:bizbuysell.com music lessons New York`
6. `site:bizquest.com music New Jersey for sale`
7. `site:bizquest.com music school New York for sale`
8. `site:businessesforsale.com music New Jersey`
9. `site:businessbroker.net music New Jersey`
10. `site:sunbeltnetwork.com music New Jersey`
11. `"music store" "for sale" "New Jersey" 2026`
12. `"music school" "for sale" "New Jersey" 2026`
13. `"guitar shop" "for sale" New Jersey`
14. `"instrument store" "for sale" NJ OR "New Jersey"`
15. `"music academy" "for sale" "New Jersey" OR "New York"`
16. `music business for sale "Essex County" OR "Bergen County" OR "Morris County" OR "Passaic County"`

For each search, carefully extract from the result snippets:
- The **direct URL** to the listing page (not the homepage)
- Business type and any description text available
- Location (city, state)
- Asking price (if shown in snippet)
- Any date info (listed date, updated date)

## Output Format

---
# 🎵 Music Business Listings Digest — [Date]
**Area:** Within 1 hour of Montclair, NJ | **Categories:** Music Retail & Music Schools

## Listings Found This Week

For each listing include:
- **Business type** (e.g., "Guitar & instrument shop")
- **Location** (city, state)
- **Asking price** (if available in search snippet — otherwise "Not shown")
- **Description** (from search snippet)
- **Source**: [View listing](direct-listing-url)
- **Listed/updated**: (if available)

> ⚠️ *Prices and dates are from search result snippets and may be outdated. Click each link to verify current details directly on the listing site.*

## Summary
- Listings found: X
- Searches run: X
- Sites represented: [list]
- Notes: anything unusual, gaps, or searches that returned no results

---

If no listings are found, say so clearly. Do not fabricate listings or URLs.

Save the output as a markdown file and present it to the user using the present_files tool.
```

---

### `daily-brain-dump`

| Field | Value |
|-------|-------|
| **Description** | Weekday 5pm brain dump to capture decisions, learnings, and context from Slack, email, and side conversations into project memory |
| **Schedule** | Weekdays (Mon-Fri) at 5:00 PM |
| **Cron** | `0 17 * * 1-5` |
| **Status** | Enabled |
| **Prompt file** | `~/Documents/Claude/Scheduled/daily-brain-dump/SKILL.md` |

**Purpose:** End-of-day sync to capture context that doesn't show up in Granola -- Slack threads, email decisions, side conversations. Processes into the right project memory.md files so nothing falls through the cracks.

**Full prompt:**

```
It's end-of-day brain dump time for Matt Saunders.

Your job is to facilitate a structured brain dump and process the information into the right project memory files.

## Objective

Help Matt capture critical decisions, learnings, and context from today that aren't in Granola meeting notes -- things from Slack, email, side conversations, or in-person discussions. Then write that information into the appropriate memory files.

## Steps

1. **Greet and prompt.** Open with something like: "End of day -- what's on your mind? Walk me through anything from today that I should know about: decisions made, things you learned, open questions, or context that came up outside of meetings."

2. **Let Matt dump freely.** Don't interrupt or structure prematurely. Let him talk through it. Ask one follow-up question at a time if something is vague or needs a project assigned to it.

3. **Organize the input** by project. For each item Matt shares, identify:
   - Which project it belongs to (check /sessions/hopeful-wizardly-lovelace/mnt/Matt's CoPilot/projects/ for the project list)
   - Whether it's a fact, a decision, or an open question
   - Whether it changes anything previously recorded

4. **Update memory files.** For each project affected, append to the Session Log section of the relevant `/projects/[project-name]/memory.md` file. Follow this format:
   - Date: YYYY-MM-DD
   - What was learned or decided (tight bullets)
   - Source: e.g., "Slack with [name]", "Side convo with [name]", "Email from [name]"

5. **Confirm what was written.** After updating, summarize what you captured and where it was stored. Keep it brief.

## Constraints

- Do not overwrite existing memory content -- append only
- Do not store low-value or redundant information
- If Matt mentions something that doesn't fit a current project, ask if it warrants a new project or just a note in a general scratchpad
- Keep the tone conversational but efficient -- Matt prefers direct, concise communication
- Do not use em dashes or emoji
```

---

## Setup Checklist for a New Machine

1. Install the **Claude desktop app** and sign in
2. Enable **Cowork mode**
3. Mount your notes folder (the source of truth at `~/Desktop/Vibe Coded Stuff/Matt's CoPilot/projects/liv-golf/notes/`)
4. For each task above:
   - Open the SKILL.md file from your backup/old machine (path above)
   - Start a new Cowork session, invoke the **Schedule skill**
   - Paste the prompt and configure the same cron expression
5. Verify tasks appear in the scheduled tasks panel

---

## Notes

- Full prompts are embedded above — this file is self-contained for recreating tasks on a new machine.
- The original prompt files also live at `~/Documents/Claude/Scheduled/{taskId}/SKILL.md` on your Mac as the authoritative source.
- Cron expressions use **local time (ET)**, not UTC.
