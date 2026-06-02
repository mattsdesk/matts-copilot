# Scheduled Tasks

> Record of automated Claude tasks that operate on this project. Use this to recreate the setup on a new machine.
>
> **Last updated:** 2026-05-27

---

## How Scheduled Tasks Work

Scheduled tasks are created in the Claude desktop app (Cowork mode). Each task:

- Has a unique `taskId` (kebab-case)
- Runs on a cron schedule evaluated in **local time (ET)**
- Stores its full prompt in a SKILL.md file on the Mac at: `~/Documents/Claude/Scheduled/{taskId}/SKILL.md`

To recreate a task on a new machine, start a Cowork session, invoke the **Schedule** skill, and paste the prompt from this file.

---

## Active Tasks

### `granola-notes-sync`

| Field | Value |
|-------|-------|
| **Description** | Sync new Granola meetings into Matt's CoPilot project folders |
| **Schedule** | Weekdays (Mon-Fri) at 8:30 AM and 5:30 PM ET |
| **Cron** | `30 8,17 * * 1-5` |
| **Status** | Enabled |
| **Prompt file** | `~/Documents/Claude/Scheduled/granola-notes-sync/SKILL.md` |

**Purpose:** Pulls new Granola meeting notes and routes them into the correct project's `meetings/2026/` folder. Active routing destinations are Montclair Digital, Renna Media Acquisition, and Personal. Also updates the relevant project's memory.md when meaningful.

**Important:** Driving school acquisition is archived at `archive/driving-school-acquisition/`. Do not route new notes to `projects/driving-school-acquisition/`.

**Routing table:**

| Context | Route to | Triggers |
|---------|----------|----------|
| Montclair Digital | `<base>/projects/montclair-digital/meetings/2026/` | Einhorn Barbarito staff (Liz Lindley, Alissa Hascup, Ashley Hitch), Flyosophy (Mara Scott), or consulting client discussions |
| Renna Media Acquisition | `<base>/projects/renna-media-acquisition/meetings/2026/` | Renna Media, Joe/Tina Renna, Eric Sharret, Murphy Business, Cheryl Venezia, David Bohlander, Mike Pierson, acquisition financing, Maria/KRS accountant when focused on the newspaper acquisition, printing/mail vendors for the newspaper project including YGS and Shapco, LOI, diligence, offer, APA, closing, USPS/EDDM, advertiser analysis |
| Acquisitions Pipeline | no meeting file by default | General business-for-sale sourcing, broker newsletters, thesis conversations, or deal exploration before a specific project is opened. Log only in `projects/acquisitions/memory.md` if meaningful. Once a deal has its own project folder, route there. |
| Personal | `<base>/projects/personal/meetings/2026/` | Job interviews, financial planning not tied to a specific deal, family, life admin, personal networking, anything not covered by a more specific active project |

If a meeting ID already exists in any active meeting folder, do not create a duplicate in another project. Use archived folders only to avoid re-importing archived project notes, not as active destinations.

If a meeting doesn't fit an active context, skip and note it in the sync report.

---

### `music-biz-monitor`

| Field | Value |
|-------|-------|
| **Description** | Weekly scan for music-related small businesses for sale near Montclair, NJ |
| **Schedule** | Fridays at 9:00 AM ET |
| **Cron** | `0 9 * * 5` |
| **Status** | Disabled (last run 2026-04-17). Superseded by `acquisitions-digest`. |
| **Prompt file** | `~/Documents/Claude/Scheduled/music-biz-monitor/SKILL.md` |

**Purpose:** Weekly automated search for music-related small business acquisition opportunities (studios, shops, schools) within ~1 hour of Montclair, NJ. Output saved as a weekly digest markdown file at project root (see `music-biz-digest-2026-04-*.md`).

Full prompt archived in `archive/liv-golf/notes/scheduled-tasks.md` (section: `music-biz-monitor`). Re-enable from Cowork scheduled tasks panel when wanted.

---

### `acquisitions-digest`

| Field | Value |
|-------|-------|
| **Description** | Gmail-primary digest of business-for-sale listings matching Matt's acquisition thesis |
| **Schedule** | Mon/Wed/Fri at 2:00 AM ET |
| **Cron** | `0 2 * * 1,3,5` |
| **Status** | Enabled (created 2026-04-19; Gmail-primary since 2026-04-22; rescheduled to overnight 2026-05-06) |
| **Prompt file** | `~/Documents/Claude/Scheduled/acquisitions-digest/SKILL.md` |

**Purpose:** Generates a 3x/week digest of new business-for-sale listings against Matt's barbell thesis (Primary Operating Business + Passive Holds). Gmail is the primary source: the task reads every thread in the `Acquisitions` label (100% coverage guarantee), extracts listings, applies the thesis, and writes a segmented digest to `projects/acquisitions/digests/YYYY-MM-DD.md`. WebSearch is a secondary supplement to catch marketplaces without email alerts. Thesis is re-read from disk every run so the task evolves with Matt's view.

**Coverage guarantee:** every thread in `label:Acquisitions` is accounted for in the digest. Each listing lands in exactly one bucket (Primary Strong, Passive Strong, Borderline, Excluded with reason). Digest header reports total threads processed and listings extracted so coverage is auditable.

**Full prompt:**

```
You are running the Matt's CoPilot acquisitions discovery task. Produce a digest of business-for-sale listings matching Matt's thesis.

## Step 1: Load the current thesis

Read `/projects/acquisitions/thesis.md` every run. The thesis evolves. Use the live version of the document as the filter, not any version you remember from prior runs.

Matt's thesis runs two tracks (barbell):
- **Primary Operating Business**: $250K to $1M SDE, hands-on CEO role, "work ON not IN" filter, broad sector scope
- **Passive Holds**: $100K to $300K SDE, structurally passive only (self-storage, automated car washes, vending/ATM/amusement routes, equipment rental, RV parks/marinas, structurally passive digital)

Hard global excludes: food businesses (all forms), bread routes, laundromats. Geography: 1 hour drive from Montclair, NJ (NJ, NY Westchester/Rockland/lower Hudson Valley/lower Manhattan/western Queens/Nassau western edge, PA Bucks/Northampton, CT lower Fairfield).

## Step 2: Gmail-primary discovery (required)

Query Gmail for every thread in the Acquisitions label that has not yet been processed.

- Use the Gmail connector's `search_threads` tool with query: `label:Acquisitions is:unread`
- Page through ALL results (pageSize 50, follow nextPageToken if returned). Do not cap at the first page.
- For each thread, call `get_thread` to pull the full message body. Listings alert emails from BizBuySell, BizQuest, LoopNet, etc. typically contain multiple listings per message. Parse them all.

**Coverage rule (critical):** every thread returned by the Gmail query MUST be accounted for in the output. No silent drops. Every listing extracted lands in exactly one bucket:
- Primary: Strong Match
- Passive Holds: Strong Match
- Borderline
- Excluded (with reason)

If a thread is ambiguous (e.g., broker newsletter with no specific listing), count it under Excluded with reason "no specific listing" and summarize briefly in the notes section.

**Dedup:** check `/projects/acquisitions/seen.md` (create it if missing). Before adding a listing to the digest, check if the same listing ID or business name appears there. If yes, skip it (but still count it in coverage). After the run, append every NEW listing you surfaced to `seen.md` with: date, business name, source URL or email subject, bucket assigned.

## Step 3: WebSearch supplement (secondary)

After processing Gmail, run a short round of WebSearch queries to catch marketplaces that don't email alerts and broker-only listings. Keep this light; Gmail is primary. Suggested queries (pick 3 to 5, rotate across runs):

- "businesses for sale Essex County NJ [date range last 7 days]"
- "businesses for sale Bergen County NJ"
- "self storage for sale New Jersey"
- "car wash for sale tri state"
- "SDE 500000 business for sale NJ"
- "retiring owner business for sale New Jersey"

Skip any WebSearch result already covered by a Gmail listing (use business name as match key). Add unique WebSearch finds into the same buckets.

## Step 4: Write the digest

Output path: `/projects/acquisitions/digests/YYYY-MM-DD.md` (today's date in America/New_York).

Use the template at `/projects/acquisitions/templates/daily-digest.md`. Populate every section.

Header must include:
- Thesis version (read from `thesis.md`)
- Gmail coverage line: "N threads in label:Acquisitions processed, M listings extracted"
- WebSearch coverage line: "K queries run, L unique listings added"
- Run time

Body sections in order:
1. Primary: Strong Matches (0 to N)
2. Passive Holds: Strong Matches (0 to N)
3. Borderline (either track, labeled)
4. Excluded This Run (counts by reason: out of geography, food, SDE below, SDE above, under 5 years, already seen, no specific listing, other)
5. Notes and Tuning Suggestions (patterns, source quality, new marketplaces appearing)
6. Promotion Actions (checkboxes for Matt)

For each Strong Match and Borderline listing, include: business name, type, location, asking price, SDE, years in operation (if known), source link or email subject, 2-3 sentence initial read, which specific thesis criteria it hits, and (for Passive Holds) the mechanism that makes it structurally passive.

## Step 5: Append to memory.md

Append a short Session Log entry to `/projects/acquisitions/memory.md` under the Session Log section:
- Date
- Gmail coverage numbers
- Strong match count per track
- Any notable patterns (new sector emerging, geography cluster, broker relationship opportunity)

Keep it to 3 to 5 lines.

## Step 6: DO NOT mark emails as read

The Gmail connector in this environment is read-only. Do not attempt to mark threads as read or apply labels. Dedup is handled by `seen.md`, not by read status.

## Notes

- If Gmail returns zero unread threads, proceed with WebSearch only and note "Gmail label empty this run" in the digest header.
- If Gmail connector fails entirely, fall back to WebSearch-only mode and flag this at the top of the digest.
- Do not promote any listing to `/projects/acquisitions/deals/`. Promotion is Matt's decision, made via the checkboxes in the digest.
- Date handling: use the current date in America/New_York for the digest filename. If env wall clock is off, use the most recent sensible date.
```

---

### `linkedin-job-digest`

| Field | Value |
|-------|-------|
| **Description** | Daily LinkedIn job alert digest from the Job Hunt Gmail label |
| **Schedule** | Daily at 8:00 AM ET |
| **Cron** | `0 8 * * *` |
| **Status** | Enabled (created 2026-04-29) |
| **Prompt file** | `~/Documents/Claude/Scheduled/linkedin-job-digest/SKILL.md` |

**Purpose:** Reads all LinkedIn job alert emails from the `Job Hunt` Gmail label received in the last 24 hours (sender: `jobalerts-noreply@linkedin.com`). Parses each listing (title, company, location, salary, inferred industry, direct LinkedIn URL) and updates a persistent Cowork sidebar artifact (`linkedin-job-digest`) with a sortable Grid.js table for daily review.

**Full prompt:**

```
Check the Gmail "Job Hunt" label for LinkedIn job alert emails received in the last 24 hours, parse all job listings, and create or update the LinkedIn Job Digest artifact.

## Step 1: Fetch emails

Call `search_threads` with:
  query: label:"Job Hunt" from:jobalerts-noreply@linkedin.com newer_than:1d
  pageSize: 20

If no threads are returned, proceed to Step 4 with an empty job list and display a "No new job alerts in the last 24 hours" message in the artifact.

## Step 2: Get full content

For each thread ID returned, call `get_thread` with:
  messageFormat: FULL_CONTENT

## Step 3: Parse job listings

Each email plain text body contains job listings separated by dashed lines (`---`). For each listing block, extract:

- **Title**: First non-empty line of the block
- **Company**: Second line
- **Location**: Third line
- **Salary**: Check the email subject line for salary info (formats like "up to $250K/year" or "$200K-$250K / year"). Salary is not listed per-job in the body -- apply the subject line value to all jobs in that email. If no salary found, use "Not listed"
- **Industry**: Infer from your knowledge of the company (e.g., Samsung Ads -> Advertising/Tech, Mastercard -> Financial Services, Merck -> Pharmaceuticals, Uber -> Transportation/Tech). Use "Unknown" if unsure
- **Link**: Extract the URL from the "View job: [URL]" line in each block. Use the URL as-is (do not shorten or modify it)

Skip the final "See all jobs on LinkedIn" block -- it is not a job listing.

Deduplicate across multiple emails: if the same job title + company combination appears more than once, keep only one entry.

## Step 3b: Filter listings

After parsing and deduplicating, apply these filters. Drop any job that matches either rule:

1. **Salary ceiling at or below $250K**: If a salary is listed and it tops out at $250K or less (e.g., "up to $250K/year", "$200K-$250K/year"), exclude the job. If salary is "Not listed", keep it.
2. **Finance industry**: Exclude jobs at companies whose primary business is financial services -- banks, investment banks, asset managers, payment networks, insurance companies, and similar. Examples: BNY, JPMorgan, Goldman Sachs, Mastercard, Visa, Fidelity, BlackRock, Morgan Stanley. Companies that use finance as a tool (e.g., a fintech selling software, a tech company with a payments product) are not automatically excluded -- use judgment.

## Step 4: Build the artifact

First, call `list_artifacts` to check whether an artifact with id `linkedin-job-digest` already exists.
- If it exists: call `update_artifact`
- If not: call `create_artifact`

Use id: `linkedin-job-digest`
Description: "Daily LinkedIn job alert digest -- refreshed each morning from the Job Hunt Gmail label"

The HTML artifact must be a complete self-contained page. Use Grid.js for the sortable table. Include these exact CDN tags:

<script src="https://cdn.jsdelivr.net/npm/gridjs@5.0.2/dist/gridjs.umd.js" integrity="sha384-/XXDzxe4FsGiAe50i/u9pY/Vy/uX654MHB1xoc1BJNnH1WXHhqHga9g3q5tF4gj7" crossorigin="anonymous"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/gridjs@5.0.2/dist/theme/mermaid.min.css" integrity="sha384-jZvDSsmGB9oGGT/4l9bHXGoAv1OxvG/cFmSo0dZaSqmBgvQTKDBFAMftlXTmMbNW" crossorigin="anonymous">

The artifact should include:
- A heading: "LinkedIn Job Digest" with today's date (format: "April 29, 2026")
- A Grid.js sortable table with these columns: Title, Company, Industry, Location, Salary, Link
- The Link column should render as a small "View" button/link that opens the LinkedIn URL in a new tab. Use Grid.js html() formatter for this column
- The job data should be hardcoded as a JavaScript array in the HTML -- do not make live network calls
- Clean light-mode styling: white background, dark text, readable font (system-ui or sans-serif), subtle header row shading
- A footer line: "Last updated: [timestamp of run]"
- Include `:root { color-scheme: light }` in the styles

If there are no jobs (empty list), show a centered message: "No new LinkedIn job alerts in the last 24 hours." instead of an empty table.

mcp_tools to declare: mcp__39aab7ae-d187-4013-b383-36d53c16c374__search_threads, mcp__39aab7ae-d187-4013-b383-36d53c16c374__get_thread
```

---

## Setup Checklist for a New Machine

1. Install the Claude desktop app and sign in
2. Enable Cowork mode
3. Mount the CoPilot folder (`~/.../matts-copilot/`)
4. For each active task above:
   - Start a new Cowork session, invoke the **Schedule** skill
   - Paste the prompt from this file and configure the same cron expression
5. Verify tasks appear in the scheduled tasks panel

---

## Notes

- Cron expressions use **local time (ET)**, not UTC
- Full prompts live here as the portable source; the Mac-local SKILL.md files are authoritative for the runtime
- When a task's behavior changes, update both the SKILL.md and this file
