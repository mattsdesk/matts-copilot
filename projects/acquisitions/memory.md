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
- Archived: Manalapan/Marlboro driving schools (`/projects/driving-school-acquisition/`). Matt moved on from this deal as of 2026-05-01.
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

### 2026-04-23

- `acquisitions-digest` off-cycle run (Thursday; scheduled cadence is Mon/Wed/Fri). Produced `digests/2026-04-23.md`. 0 new Primary Strong Matches, 0 new Passive Strong Matches, 3 new Borderline (Essex County absentee hand/brushless car wash 30+ years; Morris County 37-year residential pool service $1.85M SBA; Morris County unspecified service business $1.6M SBA). Total excluded approximately 30+ across food, laundromat, routes, SDE below range, multiple above ceiling, out-of-geography, solo operator, full-service car wash, and previously-excluded resurfacing.
- Pattern: fourth consecutive run showing sub-daily marketplace inventory refresh. Mon/Wed/Fri cadence remains correct; off-cycle runs continue to yield diminishing new items.
- Pattern: Morris County listings clustering across runs. Consider sub-radius filter (eastern Morris only) rather than blanket county inclusion when triaging.
- Essex County car wash (Listing #37316) is the first Passive-adjacent Essex County listing across four runs; worth a click-through to resolve Passive vs excluded based on automated-vs-full-service revenue split.
- Synergy Business Brokers direct outreach to Joe Coculo remains the highest-leverage coverage improvement available.

### 2026-04-27

- Gmail-primary run: 2 threads processed, 1 listing partially extracted (BizBuySell NJ alert body not retrieved by connector -- snippet-only returned; full body parsing is still blocked), 1 thread was outbound inquiry confirmation for "Established Niche Marketing Agency" (already in pipeline).
- 0 Primary Strong Matches, 0 Passive Strong Matches. 3 Borderline (school bus company Essex/Middlesex, northern NJ exterior car wash $1.2M ask, NE regional equipment rental NJ).
- School bus company in Essex/Middlesex is the highest-priority lead this run: geography ideal, contractual revenue, retiring owner, staff model -- only missing SDE confirmation.
- Gmail connector body retrieval still not working (get_thread returns snippet only despite FULL_CONTENT format request). This is a recurring blocker for email-alert-based discovery.
- "Established Niche Marketing Agency" inquiry was sent 2026-04-23; Matt should check for seller response.

### 2026-04-29

- Gmail-primary run: 1 unread thread in `label:Acquisitions` processed (SMB Deal Hunter alumni-interview newsletter, Helen Guo - educational/marketing, no specific listing). 0 listings extracted from Gmail. WebSearch supplement: 5 queries, 3 net-new Borderline listings after dedup.
- 0 Primary Strong Matches, 0 Passive Strong Matches. 3 Borderline (Tenafly bridal boutique 23 yrs; Bergen County gas station + garage + EV; Bergen County day spa) - all Bergen County, all SDE unconfirmed.
- Pattern: second consecutive Gmail-primary run with zero usable broker-alert volume. Saved-search alerts are not flowing into the labeled inbox. Highest-leverage fix: confirm BizBuySell / BizQuest / LoopNet saved-search emails are delivered (check spam, verify filters).
- Bergen County clustering this run mirrors Morris County clustering from 2026-04-23 - county-level density patterns are showing up. Consider sub-radius / sub-county tuning when triaging.
- NJ self-storage sub-$1M deal flow remains thin (statewide avg sale $5.4M); off-market broker outreach (Argus, M&M) is the realistic path for Passive Holds storage track.

### 2026-05-01

- Gmail-primary run: 5 threads processed, 8 listings extracted.
- **Primary Strong Matches:** 2 (Elite Landscape & Design Build $850K SDE Nassau County; Kitchen Cabinet Mfg $1M SDE Queens)
- **Passive Strong Matches:** 0
- **Borderline:** 3 (Education Company $487K SDE NY location TBD; Art Publishing $343K SDE remotely operated; Retail/Rental Albany $500K SDE)
- **Total excluded:** 12 (4 out of geography, 5 food, 1 SDE below, 2 non-listing/development)
- Pattern: Gmail connector working fully again after prior snippet-only blocks (2026-04-27 and 2026-04-29). Both Synergy and East Coast alerts parsed multi-listing cleanly.
- Pattern: Equipment-heavy businesses (manufacturing, landscaping) showing consistent listings. Thesis fit is clear for these sectors.
- Next: Verify Education Company location, pressure-test Art Publishing on AI durability, clarify retail property sector/geography. Consider warm intro to Synergy for filter tuning.

### 2026-05-04

- Gmail-primary run: 10 threads processed; 3 BizBuySell alerts blocked by Gmail connector (snippet-only retrieval, full body not accessible).
- **Primary Strong Matches:** 0 (none new this run)
- **Passive Strong Matches:** 0
- **Borderline:** 1 (Turnkey auto shop Nassau County #12618, $314K SDE, "semi-absentee" -- requires diligence on whether owner is truly removed from daily operations)
- **Total excluded:** 16 (5 food, 3 out-of-geography, 1 SDE-below, 1 non-operating-business, 5 already-seen/deduped, 2 educational-no-listing, 3 retrieval-limitation)
- Pattern: Gmail connector retrieval limitation with BizBuySell is recurring issue. Full bodies not parsing despite FULL_CONTENT format request. This caps coverage of what is otherwise a primary discovery source.
- Pattern: East Coast Business Brokers and Synergy newsletters are high-volume but low-fit (mostly food/hospitality or out-of-radius). Deprioritizing in favor of direct marketplace browsing.
- Data point: Auto repair sector showing as a borderline test case. Need to clarify "work ON not IN" bar for inherently skill-dependent trades. Recommend declining unless owner is genuinely delegated and technicians are the revenue generators.

### 2026-04-19 (first discovery run)

- Strong matches: 3 (school bus company Essex County; commercial HVAC Bergen County; commercial HVAC Passaic County)
- Borderline: 2 (drug and alcohol testing services NJ; Bergen County landscaping at 4.7x multiple)
- Total excluded: 13+ (food businesses, SDE below range, multiple above ceiling, routes, laundromats, geography uncertain)
- Notable pattern: Essex County school bus sector has multiple simultaneous listings from retiring owners -- generational transition underway, worth a thesis opinion on this sector
- Notable pattern: NJ HVAC sector active with 3+ listings across Passaic/Bergen counties; commercial-heavy profiles with recurring contracts align well
- Source constraint: all marketplace direct pages blocked by egress proxy (BizBuySell, BizQuest, DealStream, Synergy, Sunbelt, VestedBB); all data sourced via WebSearch summaries -- verify financials before acting

### 2026-05-06

- Gmail-primary run: 13 threads processed. 4 BizBuySell alerts (snippet-only, no body text retrievable); 2 SMB Deal Hunter newsletters (editorial, no specific listings); 1 Renna Media internal thread (Matt's in-process deal, excluded); 6 broker email threads with full content (all listings already in seen.md from prior runs).
- **Primary Strong Matches:** 0 new
- **Passive Strong Matches:** 0 new
- **Borderline:** 0 new
- **Total excluded:** 0 new (no novel listings this run; prior exclusions still valid)
- **WebSearch supplement:** 3 queries run (Essex County, Bergen County, SDE $500K range). Returned general marketplace links, no specific new listings.
- Pattern: 5-day gap since last run (2026-05-04). Marketplace inventory refresh is slow; no new listings surfaced despite active broker traffic. Confirms Mon/Wed/Fri cadence is appropriate.
- Gmail connector blocker confirmed: BizBuySell alerts (4 threads) returned subject lines only; full HTML bodies not retrieved despite FULL_CONTENT format request. This is a recurring issue. Marketplace alerts are reaching the label, but parsing them via Gmail API is limited. Workaround: monitor BizBuySell.com directly if specific alerts are critical.
- Next digest: 2026-05-08 (Wednesday, per schedule).

### 2026-05-08

- Gmail-primary run: 19 threads processed. 10 BizBuySell alerts (snippet-only, no body content retrievable); 2 SMB Deal Hunter newsletters (editorial); 1 Renna Media internal (excluded); 6 broker email threads with full content.
- **Primary Strong Matches:** 0
- **Passive Strong Matches:** 0
- **Borderline:** 0 new (Turnkey Auto Shop #12618 from 2026-05-04 remains under review)
- **Total excluded:** 10 new listings, all food or SDE-out-of-range
- Pattern: 2-day gap since 2026-05-06 run. No new Primary or Passive strong matches. Thin discovery week. East Coast Business Brokers newsletter batch (2026-05-07) contained 8 listings, all food or already-seen. Dryer vent service re-appeared at same SDE ($148K, sub-floor).
- Gmail connector blocker persists: 10 BizBuySell alerts across dates 2026-05-02 through 2026-05-07, all snippet-only. This is third consecutive run with this blocker pattern. Full body retrieval unavailable; direct marketplace monitoring remains recommended.
- Tuning note: Synergy and East Coast Brokers broker email volume is high but thesis fit is poor (hospitality/food dominant, geographic radius mostly out of scope). Deprioritize broker newsletters; emphasize direct marketplace + off-market broker outreach (Kensington, Argus, M&M, Sunbelt).
- Digest output: 2026-05-08.md. Zero promotions recommended. Renna Media coordination thread excluded. Next scheduled run: 2026-05-10 (Friday).

### 2026-05-11

- Gmail-primary run: 18 threads processed. 10 BizBuySell alerts (snippet-only, no body content); 2 SMB Deal Hunter newsletters (editorial, no specific listings); 1 Renna Media internal thread; 1 Acquire.com alert (already seen); 4 East Coast Business Brokers threads (mostly food or already seen).
- **Primary Strong Matches:** 0
- **Passive Strong Matches:** 0
- **Borderline:** 0 new
- **Total excluded:** 16 (10 BizBuySell inaccessible, 2 food, 2 editorial, 1 internal, 1 already-seen)
- **WebSearch supplement:** 3 queries (NJ SDE range, NJ self-storage, Bergen County retiring owner). Returned generic marketplace links, no specific new listings identified.
- Gmail connector blocker (critical): 5th consecutive run with BizBuySell snippet-only issue (2026-04-27, 4/29, 5/6, 5/8, 5/11). BizBuySell alerts indicate 15-20 listings per week are embedded in inaccessible full HTML bodies. This is a blocking issue for email-primary discovery.
- Recommendation: Switch to direct BizBuySell.com monitoring (NJ filter, $250K-$1M SDE, work-ON-not-IN screens) as interim workaround. Off-market broker outreach (Argus, M&M, Kensington) remains highest-leverage discovery path.
- Digest output: 2026-05-11.md. Zero promotions recommended.

### 2026-05-13

- Gmail-primary run: 18 threads processed. 5 BizBuySell alerts (snippet-only, no body content retrievable); 2 SMB Deal Hunter newsletters (educational case studies, no specific listings); 2 CPA introduction threads (Renna Media internal); 2 Renna Media internal threads (in-process deal); 7 East Coast Business Brokers threads (full content parsed).
- **Primary Strong Matches:** 0 new (Elite Landscape #12581 and Kitchen Cabinet Mfg #12570 from 2026-05-01 remain strong; already in pipeline)
- **Passive Strong Matches:** 0
- **Borderline:** 0 new (Turnkey Auto Shop #12618 remains under review from 2026-05-04 run)
- **Total excluded:** 2 new listings (both food: Boston Bakery #12731, Merrimack Valley Bakery #12730)
- **WebSearch supplement:** None (short run)
- Gmail connector blocker persists: 6th consecutive run with BizBuySell snippet-only issue (now spans 2026-04-27 through 2026-05-13). Five alerts returned subject line only; estimated 5-8 specific listings embedded in inaccessible HTML bodies. Pattern is consistent and unresolved.
- Pattern: Two-week stretch (2026-05-01 through 2026-05-13) with zero new Primary Strong Matches. Thin discovery cycle. Prior two strong matches from 2026-05-01 remain best options in pipeline (Landscape $850K SDE, Cabinet Mfg $1M SDE).
- Note: Renna Media deal dominating unread count (4 threads across May 4-13), reflecting internal work on that transaction. This deal should migrate to its own project folder once LOI signed to decongest the Acquisitions label.
- Digest output: 2026-05-13.md. Zero new promotions recommended. Auto shop #12618 and prior Borderline candidates carry forward for Matt's judgment.
- Next scheduled run: 2026-05-15 (Wednesday). Recommend testing BizBuySell.com direct access or reaching out to Blake at Synergy / Henry at East Coast for priority feed setup.
