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
- Archived: Manalapan/Marlboro driving schools (`/archive/driving-school-acquisition/`). Matt moved on from this deal as of 2026-05-01.
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
- Logged `driving-school-acquisition` as graduated deal in pipeline.md; later archived at `/archive/driving-school-acquisition/`
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

### 2026-05-15

- Gmail-primary run: 18 threads processed. 5 BizBuySell alerts (snippet-only, bodies not retrievable); 2 SMB Deal Hunter newsletters (educational, no specific listings); 1 Acquire.com alert (already in seen.md); 10 East Coast Business Brokers / Synergy / broker threads (full content parsed).
- **Primary Strong Matches:** 0 new
- **Passive Strong Matches:** 0 new
- **Borderline:** 0 new this run (Turnkey Auto Shop #12618 Nassau County from 2026-05-04 remains under review; all new readable emails contained already-catalogued listings)
- **Total excluded:** 4 new listings (Burger Shop Queens #12609, Restaurant Flatironnomad #12711, Tap Room Nassau #12665, Liquor License Bergen #12712 - all food except license, which is non-operating)
- **WebSearch supplement:** 3 queries (general NJ businesses, self-storage tri-state, car wash tri-state). Returned marketplace directory links only; no specific new standalone listings identified. Self-storage and car wash inventory confirmed as robust in tri-state region but asking prices noted above Primary SDE ceiling ($1.2M-$4.6M range).
- Gmail connector blocker: 7th consecutive run with BizBuySell snippet-only issue (2026-04-27 through 2026-05-15). Estimated 15+ specific listings remain embedded in inaccessible HTML bodies across BizBuySell alerts.
- Pattern: 13-day discovery cycle (2026-05-01 through 2026-05-15) shows zero new Primary Strong Matches. Two strong candidates remain from 2026-05-01 run (Elite Landscape $850K SDE, Kitchen Cabinet Mfg $1M SDE). Thin deal flow persists. Broker newsletter volume is high but low-fit (food/hospitality dominant).
- Tuning observation: Prior run notes (2026-05-13) flagged Renna Media deal congesting the Acquisitions label. That deal should be migrated to its own project folder to reduce label noise and improve digest signal-to-noise ratio.
- Digest output: 2026-05-15.md. Zero new promotions (Auto Shop #12618 flagged as Borderline pending verification). Recommendation: Matt contact Ralph Galdorski (516-707-4670) at East Coast Business Brokers to verify auto shop owner involvement ("semi-absentee" claim requires substantiation).
- Pattern note: Marketplace refresh continues to be slow; 7+ days between new strong matches. Mon/Wed/Fri cadence is appropriate. Off-market broker outreach (Kensington, Argus, M&M, Sunbelt direct) should be prioritized over newsletter monitoring.

### 2026-05-20

- Gmail-primary run: 20 threads processed. 8 BizBuySell alerts (snippet-only, no body content retrievable); 2 inquiry confirmations (Local Advertising, Local Magazine - Matt already submitted inquiries); 2 SMB Deal Hunter newsletters (educational, no specific listings); 3 broker email threads with food/already-seen listings; 2 East Coast Business Brokers newsletters (top-X lists, mostly food or already-seen); 1 Synergy featured list (already catalogued 2026-05-01).
- **Primary Strong Matches:** 0 new
- **Passive Strong Matches:** 0 new
- **Borderline:** 0 new
- **Total excluded:** 23 (8 BizBuySell inaccessible, 3 food, 4 already-seen/dedup, 2 out-of-geography, 1 SDE-above-ceiling, 1 non-operating, 2 educational-no-listing, 2 inquiry-confirmation)
- **WebSearch supplement:** 4 queries (NJ SDE range, self-storage/car wash, equipment rental/vending, retiring owner Montclair). Returned marketplace directories only; no specific new standalone listings identified.
- Gmail connector blocker: 8th consecutive run with BizBuySell snippet-only issue (2026-04-27 through 2026-05-20). Estimated 15+ specific listings remain embedded in inaccessible HTML bodies.
- Pattern: 19-day discovery cycle (2026-05-01 through 2026-05-20) with zero new Primary or Passive Strong Matches. Two prior strong candidates remain in pipeline (Elite Landscape $850K, Cabinet Mfg $1M). Thin deal flow continues.
- Digest output: 2026-05-20.md. Zero new promotions. Auto Shop #12618 remains flagged for Borderline verification. Recommendation: direct BizBuySell.com monitoring as interim workaround until Gmail connector blocker is resolved.
- Next scheduled run: 2026-05-22 (Friday).

### 2026-05-22

- Gmail-primary run: 0 threads in `label:Acquisitions`. No new unread messages.
- **Primary Strong Matches:** 0 new
- **Passive Strong Matches:** 0 new
- **Borderline:** 0 new
- **Total excluded:** 0 new (no novel listings this run)
- **WebSearch supplement:** 4 queries run (retiring owner, owner-financed service, automated car wash, equipment rental). Returned marketplace directory links and generic business summaries already catalogued in prior runs; no specific new standalone listings identified.
- Pattern: 21-day discovery cycle (2026-05-01 through 2026-05-22) with zero new Primary or Passive Strong Matches. Two prior strong candidates remain in pipeline (Elite Landscape $850K, Cabinet Mfg $1M). Thin deal flow continues.
- Gmail connector blocker persists: 8th consecutive run with BizBuySell snippet-only issue. Estimated 15-20 listings/week remain embedded in inaccessible HTML bodies.
- Digest output: 2026-05-22.md. Zero new promotions. Auto Shop #12618 remains flagged for review.
- Next scheduled run: 2026-05-24 (Monday).

### 2026-05-25

- Gmail-primary run: 21 threads processed. 50+ listings extracted. 6 broker email threads fully parsed (BizBuySell, Synergy, East Coast Business Brokers, Transworld). 15 threads accounted for without full body retrieval (marketing/educational emails, duplicate alerts, inquiry confirmations).
- **Primary Strong Matches:** 0 new
- **Passive Strong Matches:** 0 new
- **Borderline:** 3 new (Pharmacy Jersey City $1.5M ask $4.8M revenue, Medical Practice Multi-Disciplinary NJ $700K ask $1.1M revenue work-ON-not-IN risk, B2B Print & Marketing Turnkey NJ $720K ask franchise SDE unconfirmed)
- **Total excluded:** 21 threads fully accounted for (4 out of geography, 6 food, 1 SDE below, 1 SDE above, 3 no specific listing/marketing, 1 healthcare non-preferred, 5 other/insufficient data)
- **WebSearch supplement:** 4 queries run (Essex County NJ, self-storage NJ, car wash tri-state, Bergen County retiring owner). Returned marketplace platform directories and summary inventory data; no specific new standalone listings identified beyond marketplace confirmation. School bus company Essex County (already in seen.md 2026-04-27).
- Gmail connector blocker: Persists on BizBuySell alerts (thread 19e57111e8b2cbd6 121KB, 19e54f904fb42085 112KB). Worked around by parsing available thread previews and categorizing unprocessed threads by type.
- Pattern: 24-day discovery cycle (2026-05-01 through 2026-05-25) with zero new Primary or Passive Strong Matches. Two prior strong candidates remain in pipeline (Elite Landscape $850K, Cabinet Mfg $1M). Thin deal flow continues. Marketplace refresh rate sub-daily.
- Tuning note: Medical practice sector appearing with increasing frequency (3 instances this run) but all carry work-ON-not-IN risk (service delivery dependent, licensing requirements, staff retention). Consider tightening sector filter on medical practices in future runs.
- Tuning note: BizBuySell alert volume high (50+ listings across 21 threads) but low thesis fit (heavy food/medical/non-geographic bias). Consider deprioritizing in favor of direct marketplace browsing or off-market broker outreach.
- Digest output: 2026-05-25.md. Zero promotions. Borderline candidates (Pharmacy, Medical Practice, B2B Print) flagged for Matt review per template. Next scheduled run: 2026-05-27 (Wednesday).

### 2026-05-27

- Gmail-primary run: 28 threads processed. ~60 individual listings extracted and triaged. Most threads were BizBuySell and East Coast Business Brokers multi-listing alert emails spanning dates 2026-05-01 through 2026-05-26.
- **Primary Strong Matches:** 0 new (two prior strong candidates remain from 2026-05-01: Elite Landscape $850K SDE, Cabinet Mfg $1M SDE)
- **Passive Strong Matches:** 0 new
- **Borderline:** 0 new (prior Borderline candidates from 2026-05-25 remain: Pharmacy $4.8M revenue, Medical Practice $1.1M revenue, B2B Print franchise)
- **Total excluded:** 55 listings (21 food, 4 franchises, 8 out-of-geography, 3 SDE-below-range, 1 under-5-years, 4 no-specific-listing, 14 already-in-pipeline/deduped)
- **WebSearch supplement:** 3 queries run (general NJ SDE $250-$1M range, self-storage tri-state, car wash Bergen County). Returned marketplace platform directories and general marketplace data; no specific new standalone listings identified beyond confirmation of existing marketplace landscape (218+ businesses on SMERGERS, 507 on BFS, 1,500+ on BizBuySell).
- Gmail connector blocker: Persists on large BizBuySell emails (19e65ac8d98acb3b 72KB, 19e57111e8b2cbd6 121KB). Partial content and subject lines extracted where possible.
- Pattern: 26-day discovery cycle (2026-05-01 through 2026-05-27) with zero new Primary or Passive Strong Matches. Two prior strong candidates remain in pipeline (Elite Landscape $850K, Cabinet Mfg $1M). Deal flow thin; marketplace refresh rate sub-daily.
- Email quality pattern: East Coast Business Brokers (Henry Galasso) and BizBuySell dominate unread volume (80%+ of threads) but thesis fit remains poor. High food/franchise density, limited non-food service listings. Synergy and Transworld also active but with similar low-fit patterns.
- Tuning observation: May 2026 email volume strongly skewed toward franchises and food service, both excluded by thesis. Newsletter content quality remains low for Primary and Passive Holds sourcing.
- Broker relationship opportunity: Henry Galasso (East Coast) remains most prolific contact. Recommend follow-up call to discuss SDE/sector filtering to improve signal-to-noise ratio on future alerts.
- Recommendation: Prioritize off-market broker outreach (Kensington, Argus, M&M, Sunbelt direct), direct marketplace browsing (BizBuySell.com, BizQuest, SMERGERS filtering), and warm introductions from existing broker relationships over newsletter monitoring.
- Digest output: 2026-05-27.md. Zero promotions recommended. Auto Shop #12618 remains flagged for review from 2026-05-04 run. Next scheduled run: 2026-05-29 (Friday).

### 2026-05-27 (routing review)

- Reviewed Granola meeting-note routing after project-list drift.
- Updated active `granola-notes-sync` prompt plus root task docs: Renna Media Acquisition is now an active routing destination; Driving School Acquisition is archived.
- Added dedupe rule: if a Granola meeting ID exists anywhere in active or historical meeting folders, do not create another copy; log misfiles instead.
- Cleaned prior routing drift: Renna/Cheryl/Eric/Mike/David/YGS/Shapco/Maria acquisition notes now live under Renna Media; Juris Digital remains under Montclair Digital; Driving School moved out of active projects to `/archive/driving-school-acquisition/`.

### 2026-05-29

- Gmail-primary run: 33 threads processed. Approximately 40+ individual listings extracted across BizBuySell, East Coast Business Brokers, Synergy, and Transworld emails spanning 2026-05-01 through 2026-05-27.
- **Primary Strong Matches:** 0 new (two prior strong candidates remain from 2026-05-01: Elite Landscape $850K SDE, Cabinet Mfg $1M SDE)
- **Passive Strong Matches:** 0 new
- **Borderline:** 3 new (Exterior Services Restoration Bergen County $1.26M ask SDE unconfirmed; Medical Practice multi-disciplinary $450K ask $1.1M revenue work-ON-not-IN risk; B2B Print Marketing franchise $720K ask franchise concentration risk). Plus previously flagged from 2026-05-25 (Pharmacy, Medical Practice, B2B Print).
- **Total excluded:** 35+ listings (15 food, 8 out-of-geography, 2 SDE below, 3 SDE above, 1 laundromat, 1 under-5-years, 2 no-specific-listing, 3 already-in-pipeline/deduped)
- **WebSearch supplement:** 3 queries run (Essex County NJ, services businesses NJ 2026, self-storage equipment rental tri-state). Returned marketplace platform directories and general business data summaries; no specific new standalone listings beyond marketplace landscape confirmation.
- Gmail connector blocker: Persists on large BizBuySell and Synergy emails (token limits on multiple threads). Partial content extracted; full-body parsing incomplete.
- Pattern: 28-day discovery cycle (2026-05-01 through 2026-05-29) with zero new Primary or Passive Strong Matches. Two prior strong candidates remain in pipeline (Elite Landscape $850K, Cabinet Mfg $1M). Deal flow thin; marketplace refresh rate sub-daily.
- Tuning observation: Exterior Services Bergen County (New for 2026-05-29, $1.26M ask) is highest-priority lead this cycle. Services sector alignment, in-geography, but SDE unconfirmed. Recommend broker contact for financials.
- Email quality pattern: East Coast Business Brokers and BizBuySell continue to dominate volume (80%+ of threads) with heavy food/franchise bias. Low thesis fit. Marketplace newsletter content quality remains poor for Primary / Passive Holds sourcing.
- Broker contact opportunity: Henry Galasso (East Coast Business Brokers, 516-779-8900, henry@eastcoastbusinessbrokers.com) remains most prolific contact. Follow-up call recommended to discuss SDE/sector filtering and improve signal-to-noise ratio.
- Email hygiene tuning: 33 unread threads in label:Acquisitions represent 5+ weeks of accumulation. Recommend label refinement: create sub-labels for validated brokers (e.g., East Coast, Synergy) to reduce main-label noise; unsubscribe from low-signal newsletters (mass franchise promos, educational emails); prioritize marketplace direct access and off-market broker outreach.
- Recommendation: Prioritize direct BizBuySell.com browsing (NJ filter), off-market broker outreach (Kensington, Argus, M&M, Sunbelt), and warm introductions from validated brokers over newsletter monitoring.
- Digest output: 2026-05-29.md. Zero promotions recommended. Exterior Services $1.26M ask flagged for priority broker research. Auto Shop #12618 remains flagged from 2026-05-04 run. Next scheduled run: 2026-05-31 (Sunday - off-cycle; next on-schedule run is 2026-06-02 Monday).

### 2026-06-01

- Gmail-primary run: 30 threads processed. 20+ individual listings extracted and triaged across BizBuySell, East Coast Business Brokers, Synergy, and Transworld emails spanning 2026-05-26 through 2026-05-31.
- **Primary Strong Matches:** 0 new (two prior strong candidates remain from 2026-05-01: Elite Landscape $850K SDE, Cabinet Mfg $1M SDE)
- **Passive Strong Matches:** 0 new
- **Borderline:** 0 new this run (Exterior Services Bergen County $1.26M ask, Medical Practice $1.1M revenue, B2B Print $720K ask remain from prior runs)
- **Total excluded:** ~20 listings (6 food, 1 laundromat, 1 SDE below, 13+ already-in-pipeline/deduped)
- **WebSearch supplement:** 3 queries run (NJ SDE range, self-storage tri-state, Bergen County recent). Returned marketplace platform directories and aggregator pages; no specific new standalone listings identified. Self-storage inventory confirmed as limited in sub-$1M SDE range (statewide ave sale price $5.4M).
- Gmail connector blocker: Persists on BizBuySell HTML emails (thread 19e7bc84e7e22a3e 121KB, 19e6a80957df5c0f 115KB). Partial content extraction only.
- Pattern: 31-day discovery cycle (2026-05-01 through 2026-06-01) with zero new Primary or Passive Strong Matches. Two prior strong candidates remain in pipeline (Elite Landscape $850K, Cabinet Mfg $1M). Deal flow remains thin. Marketplace refresh rate sub-daily.
- Email quality pattern: East Coast Business Brokers and BizBuySell dominate volume (80%+) with persistent heavy food/franchise/hospitality bias. Low thesis fit continues. Broker newsletter content quality remains poor for Primary and Passive Holds sourcing.
- Alert fatigue observation: 30 unread threads in label:Acquisitions represent 6 weeks of accumulation (2026-05-26 through 2026-06-01). Nearly all represent broker newsletters with low-fit listings. Recommended action: create email sub-labels to separate broker newsletters from direct deal inquiries; deprioritize newsletter monitoring in favor of direct marketplace access and off-market broker outreach.
- Recommendation: Prioritize direct BizBuySell.com/BizQuest.com browsing with tight sector filters, direct contact with validated off-market brokers (Kensington, Argus, M&M, Sunbelt), and selective follow-up on prior Borderline candidates (Exterior Services, Medical Practice, B2B Print, Auto Shop #12618). Reduce reliance on broker newsletter monitoring.
- Digest output: 2026-06-01.md. Zero promotions recommended. Prior Borderline candidates carry forward for Matt's review. Next scheduled run: 2026-06-04 (Wednesday, per Mon/Wed/Fri cadence).

### 2026-06-03

- Gmail-primary run: 28 threads processed. 0 new listings extracted (all listings present in seen.md from prior runs).
- **Primary Strong Matches:** 0 new (two prior strong candidates remain from 2026-05-01: Elite Landscape $850K SDE, Cabinet Mfg $1M SDE)
- **Passive Strong Matches:** 0 new
- **Borderline:** 0 new (Exterior Services, Medical Practice, B2B Print, Auto Shop remain from prior runs)
- **Total accounted for:** 28 threads (2 specific listings already deduped, 3 educational/marketing newsletters with no specific listing, remainder broker alerts within marketplace coverage)
- **WebSearch supplement:** 3 queries run (NJ SDE range, self-storage tri-state, equipment rental updates). Returned marketplace directories only; no specific new standalone listings identified.
- Gmail connector status: Large BizBuySell HTML emails confirmed retrievable in FULL_CONTENT mode (threads 19e6a80957df5c0f, 19e65ac8d98acb3b). BizBuySell 5/27 email contained Exterior Services and Dynamic Organization (both already in seen.md 2026-05-29). Email parsing improved vs prior runs.
- Pattern: 33-day discovery cycle (2026-05-01 through 2026-06-03) with zero new Primary or Passive Strong Matches. Thin deal flow continues. Marketplace refresh rate sub-daily.
- Email volume pattern: 28 unread threads represent 5+ weeks of broker newsletters (5/1 through 5/27, plus old 2025 threads). East Coast Business Brokers and BizBuySell dominate (80%+, heavy food/hospitality bias, low fit). Synergy and Transworld also present but low-fit patterns. Newsletter content quality remains poor for Primary and Passive Holds.
- Broker observation: Henry Galasso (East Coast, 516-779-8900, henry@eastcoastbusinessbrokers.com) remains prolific source; warm call recommended for filter tuning.
- Digest output: 2026-06-03.md. Zero promotions recommended. Four Borderline candidates carry forward for Matt's review. No action on specific listings this cycle.

### 2026-06-05

- Gmail-primary run: 0 unread threads in `label:Acquisitions`. Label empty.
- **Primary Strong Matches:** 0 new
- **Passive Strong Matches:** 0 new
- **Borderline:** 0 new
- **Total extracted:** 0 listings
- **WebSearch supplement:** 4 queries run (self-storage NJ, service businesses Bergen County retiring owner, equipment rental tri-state, automated car wash NJ/PA). Returned marketplace platform directories and general inventory summaries (Crexi 26+ self-storage, 41 total NJ facilities at avg $5.4M; LoopNet/Showcase/BizBuySell active on car wash and equipment rental; Synergy/Business Brokers maintain Bergen County service category pipelines). No specific new standalone listings with price/SDE/owner detail identified.
- Pattern: 35-day discovery cycle (2026-05-01 through 2026-06-05) with zero new Primary or Passive Strong Matches. Two prior strong candidates remain in pipeline (Elite Landscape $850K SDE from 2026-05-01, Cabinet Mfg $1M SDE from 2026-05-01). Four Borderline candidates carry forward (Exterior Services Bergen County $1.26M ask, Medical Practice $1.1M revenue, B2B Print Marketing franchise, Auto Shop #12618 Nassau County $314K SDE). Deal flow remains thin; marketplace refresh rate sub-daily.
- Email hygiene note: 0 unread threads suggests label has been cleared (either processed/read externally or label manually cleaned). Prior run (2026-06-03) had 28 unread threads representing 5+ weeks of accumulation.
- Gmail connector status: Per prior run (2026-06-03), FULL_CONTENT retrieval confirmed working. BizBuySell alerts and multi-listing broker emails now parse correctly. No blocker on email body content.
- Marketplace observation: WebSearch returned robust inventory across all Passive Holds categories (self-storage 41+ NJ facilities, car wash multiple tri-state listings, equipment rental platforms active). However, specimen-level detail (price, SDE, owner terms) remains inaccessible via WebSearch API. Direct marketplace browsing (BizBuySell.com, LoopNet.com, Crexi.com, Synergy.com) or broker outreach required to extract specific deals.
- Tuning recommendation: Email-based discovery has been muted since 2026-05-29 (36 days of zero Primary or Passive strong matches). Recommend Matt initiate direct broker outreach calls (Henry Galasso / East Coast, Blake / Synergy, Kensington off-market) or dedicated BizBuySell.com browsing session with tight SDE/sector filters to activate pipeline. Current broker newsletter model (high volume, low fit) has not produced Primary strong match in 35 days.
- Digest output: 2026-06-05.md. Zero promotions recommended. Four prior Borderline candidates remain available for Matt review if needed. Next scheduled run: 2026-06-07 (Friday, per Mon/Wed/Fri cadence).
