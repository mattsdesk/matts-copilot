# Memory: Acquisitions Pipeline

---

## Current Status

v1 of the pipeline system set up on 2026-04-19. Folder structure, templates, thesis v0.5, and sources list in place. No scheduled discovery task yet; will be wired once Matt confirms thesis and digest cadence.

---

## Key Facts

- Primary pain: sourcing volume. Matt currently checks marketplaces manually and worries about missing listings.
- Geography: Montclair, NJ base. Hands-on local only, ~1 hour drive radius (unconfirmed).
- SDE target: $250K to $1M. Multiple ceiling ~3.5x.
- Hard exclude: food businesses.
- Sectors: open minus food, leaning toward services, education, distribution, physical.
- Predecessor: `music-biz-monitor` scheduled task (disabled 2026-04-17) did thematic weekly scans. New system is its generalization.
- Live graduated deal: Manalapan/Marlboro driving schools in `/projects/driving-school-acquisition/`.
- Broker relationships to date: Adam Stein / Mikael Vollbach (Kensington); Zanol (Central Jersey DS listing).

---

## Key Decisions

- 2026-04-19: Pipeline in markdown for v1. Upgrade to xlsx once active listings exceed ~20.
- 2026-04-19: Discovery via scheduled Claude task running web searches (successor pattern to `music-biz-monitor`). Email-alert layer is a future optional enhancement, deferred until Matt picks a Gmail account.
- 2026-04-19: Promoted deals get their own top-level project folder, leaving the acquisitions pipeline. Keeps this project a sourcing tool, not a deal workspace.
- 2026-04-19: Thesis filter is explicit (`thesis.md`). No tacit filters.

---

## Open Questions

- Which Gmail account (if any) will receive marketplace alerts (email-layer is optional future enhancement)
- Minimum gross margin threshold
- Appetite for attached real estate evaluation

---

## Session Log

### 2026-04-19 (system setup)

- Created `projects/acquisitions/` with full structure: CLAUDE.md, thesis.md, sources.md, pipeline.md, memory.md
- Created templates: listing-intake, triage-scorecard, vet-report, daily-digest
- Created empty `digests/`, `inbox/`, `deals/`, `archive/` directories with README stubs
- Logged `driving-school-acquisition` as graduated deal in pipeline.md
- Matt confirmed: 1-hour radius max, "open minus food" approach with a growing exclude list (bread routes and laundromats added), digest cadence 3x/week
- Added digital nuance to thesis: open to digital but lower priority, with extra skepticism on AI-exposed digital (thin SaaS, content sites, SEO-dependent). Prefer durable non-AI moats.
- Bumped thesis to v0.7
- Created `acquisitions-digest` scheduled task: Mon/Wed/Fri at 8:00 AM ET, cron `0 8 * * 1,3,5`. Logged in `/scheduled-tasks.md`.
- First run expected Monday 2026-04-20 morning
- Matt added "work ON the business, not IN it" as a primary filter. Thesis Involvement section rewritten with hard kill for solo operator / unreplaceable owner-held licenses. Triage scorecard hard filter added. Thesis bumped to v0.8.

### 2026-04-20

- `acquisitions-digest` ran on schedule (8:00 AM ET). Produced `digests/2026-04-20.md`. One Strong Match (Morris County Auto Parts Distributor, $950K ask, $325K SDE), three Borderline (Essex County B2B print, Westchester tree service, Rockland private label distribution). 11+ food businesses correctly excluded.
- Second digest also present at `digests/2026-04-19.md` from an earlier on-demand run.

### 2026-04-22

- Coverage guarantee codified: every thread in `label:Acquisitions` is processed on every digest run, no silent drops. Thesis filtering happens in the digest (Strong / Borderline / Excluded with reason), not at ingestion. Digest header will report "N threads processed, M listings extracted" so coverage is auditable. Matt can force-include any email by manually applying the label. Updated `email-setup.md`, `templates/daily-digest.md`, `sources.md` accordingly.
- Verified `Acquisitions` label exists in Gmail (ID `Label_1494692258960118987`). Currently empty (no threads yet -- saved-search alerts haven't started flowing).
- Rewrote `acquisitions-digest` scheduled task prompt: pivoted from WebSearch-primary to Gmail-primary. Task now pulls every unread thread in `label:Acquisitions` (paginated), parses each thread's full body (handling multi-listing alert emails), dedupes via new `seen.md` ledger, and supplements lightly with WebSearch. Digest output segmented into Primary Strong / Passive Strong / Borderline / Excluded with coverage header. Mirrored full prompt into `/scheduled-tasks.md`.
- Next run: Fri 2026-04-24 at 8:00 AM ET. Will run with Gmail-primary architecture even if label is empty (will report "Gmail label empty this run" and fall to WebSearch supplement).

### 2026-04-21

- Matt reconnected Gmail MCP connector (read-only access confirmed; write access still not granted, label creation must be manual).
- Decision: pivot discovery engine from WebSearch-primary to Gmail-primary. Created `email-setup.md` with full step-by-step setup.
- Decision: barbell thesis. Primary Operating Business ($250K to $1M SDE, work-ON-not-IN) + Passive Holds ($100K to $300K SDE, structurally passive only). Thesis bumped to v0.9.
- Updated `sources.md`, `templates/daily-digest.md`, `email-setup.md` to reflect the two-track structure. Each marketplace now has explicit saved-search criteria per track.
- Passive Holds in-scope categories: self-storage, automated car washes, vending/ATM/amusement routes, equipment rental, RV parks/marinas, structurally passive digital.
- Scheduled task prompt will be rewritten after Matt completes Gmail label setup plus at least BizBuySell saved searches. Monday/Wednesday/Friday cadence continues on WebSearch in the interim.
- NOTE: thesis.md still reads v0.7 -- v0.8 changes may not have been saved to file. Verify.
- `acquisitions-digest` off-cycle run (Tuesday, scheduled cadence is Mon/Wed/Fri). Produced `digests/2026-04-21.md`. 0 new Strong Matches, 0 new Borderline. Snippet inventory essentially identical to 2026-04-20 run; marketplace refresh is slower than daily. Suggestion: keep Mon/Wed/Fri cadence; added runs yield diminishing returns. Noted that prior run's file was mis-dated as 2026-04-20 due to env date signal (actual wall clock is 2026-04-21); both files retained since memory log points to 2026-04-20.md.

### 2026-04-19 (first discovery run)

- Strong matches: 3 (school bus company Essex County; commercial HVAC Bergen County; commercial HVAC Passaic County)
- Borderline: 2 (drug and alcohol testing services NJ; Bergen County landscaping at 4.7x multiple)
- Total excluded: 13+ (food businesses, SDE below range, multiple above ceiling, routes, laundromats, geography uncertain)
- Notable pattern: Essex County school bus sector has multiple simultaneous listings from retiring owners -- generational transition underway, worth a thesis opinion on this sector
- Notable pattern: NJ HVAC sector active with 3+ listings across Passaic/Bergen counties; commercial-heavy profiles with recurring contracts align well
- Source constraint: all marketplace direct pages blocked by egress proxy (BizBuySell, BizQuest, DealStream, Synergy, Sunbelt, VestedBB); all data sourced via WebSearch summaries -- verify financials before acting
