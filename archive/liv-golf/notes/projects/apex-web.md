# Apex Web

**Status:** 🔴 Blocked
**Owner:** Matt Saunders
**Last updated:** 2026-04-01

---

## Components

| Component | Status | Owner | Notes |
|-----------|--------|-------|-------|
| Leaderboard | 🟡 At Risk | Lewis / Nick / Fantasy Co | Reaching parity post-South Africa; leaderboard/scorecard functionality required for cutover (no Delta Tray fallback) |
| Viewing Experience (VOD/Livestream) | 🟢 On Track | Andrew / Fantasy Co | Video streaming parity achieved; more stable than app SDK implementation; path-to-air testing April 7 & 13 (48-hr windows) |
| CMS & Design System | 🔴 Blocked | Steve / Fantasy Co | Sanity entities/modules not structured until ~April 6; FantasyCo content authoring ownership misalignment flagged April 1; D3 content copy requested to unblock Forge → Sanity migration; URL redirect mapping due Apr 3 |
| LIV Golf Music Page | ⏳ Pending | Lewis | New request ahead of Live Nation announcement; needs decision |
| OKGC Rebrand Integration | 🟡 At Risk | — | April 21 deadline; impacts theming/web readiness |
| Fantasy Co Vendor Management | 🟡 At Risk | Matt / Katherine | Fantasy Co not preferred; GlobalLogic vs Pulse Live (England-based, cheaper); Pulse Live proposal due Monday; side-by-side comparison then decision |

---

> The website is a major infrastructure transformation from the legacy D3 platform to a modern Sanity CMS with responsive design and complex scoring/streaming integrations. Originally targeted for April 9 launch, now delayed to May 4 due to responsive design complexity and ViewLift SDK challenges. Three-phase testing plan: skeleton leaderboard at South Africa (live now), ~90% feature soft launch at Mexico City, full public cutover at Virginia (May 4). Denise is pushing hard for Mexico launch before her departure — likely end of April.

### Goal
Launch a stable, responsive LIV Golf website with leaderboard and streaming as core features before the May 4 Virginia/DC event.

### Status
Mexico City is now the confirmed cutover target with Virginia as fallback. The most critical blocker as of April 1 is CMS authoring: Sanity entities and modules are not structured until ~April 6, and FantasyCo appears not to understand that they own the content authoring and asset upload work (resourced for this in two executive calls with Firdosh). Matt is pushing for an immediate call to re-align FantasyCo on this expectation, with leadership available to join. FantasyCo's attempt to exclude team microsites from Mexico scope was rejected. The D3 content migration is now unblocked — LIV owns all D3 content and is requesting a full CMS copy to begin the Forge → Sanity migration. Leaderboard testing via PMY sim starts April 2, with two sessions next week and two sessions before Mexico. Path-to-air testing still scheduled for April 7 and 13.

### Key Decisions
- **March 19, 2026:** Feature cuts confirmed as inevitable for Mexico; critical path prioritised (messaging, video, leaderboard, shot callback)
- **March 19, 2026:** Aaron hired as additional design support; front-end engineering leader hired (start date TBD pending visa)
- **March 17, 2026:** Galleries identified as non-critical and deferrable
- **March 17, 2026:** Outstanding December invoice stuck in finance; backlog contract awaiting Denise signature
- **March 12, 2026:** Three-phase testing plan locked in — South Africa (skeleton), Mexico (soft launch), Virginia (full cutover)
- **March 12, 2026:** Lewis taking end-to-end ownership of standings, stats, and ads
- **March 12, 2026:** Board scrutiny noted; Denise: "This date is not going past here" (May 4)
- **March 11, 2026:** Nick and Andrew formally onboarded to web project
- **March 11, 2026:** Marketing requesting LIV Golf Music/Concerts page ahead of Live Nation announcement — needs prioritisation decision
- **March 10, 2026:** Leaderboard prioritised as critical requirement #1; viewing experience as #2
- **March 9, 2026:** Full public launch delayed to May 4; soft launch April 16; feature completion April 24
- **March 10, 2026:** South Africa designated as priority testing phase before Virginia cutover
- **January 2026:** Website complexity determined to exceed app due to responsive design and ViewLift SDK differences

### Open Questions
- Will FantasyCo align on CMS content authoring ownership and deliver the Sanity module structure by April 6? (Firdosh email to Denise pending — likely triggers a call)
- What exactly does Denise mean by "before Mexico" — April 15, the week before the event, or day-of?
- Can the team execute web cutover within May 4 timeline given board-level pressure?
- What is the fallback plan if Mexico City leaderboard fails during testing?
- When will D3 deliver the full CMS content copy to unblock Forge → Sanity migration?
- Which vendor replaces Fantasy Co — GlobalLogic or Pulse Live? (Pulse Live proposal due Monday; side-by-side comparison then decision; Fantasy Co not preferred)
- Can Pulse Live's proprietary CMS be avoided, and is GCP compatibility confirmed?
- How will content be created for Duels/Four Aces pages that require internal knowledge?
- Can the Google Analytics paid licence (~$40k) be funded from marketing budget?
- Can a LIV Golf Music/Concerts page be prioritised given the Live Nation announcement timing?
- How does the OKGC rebrand (April 21) affect web readiness?

---
---

## Tactical Detail

### Recent Updates
- **April 1, 2026 (alignment call — Firdosh/Steve/Lisa):** Vendor-side alignment meeting confirmed the content migration scope dispute from both directions. Denise expected a "lift and shift" of D3 content into the new CMS; Fantasy had zero prior knowledge of this being in scope — it was not in their SOW (unsigned). New modules don't map 1:1 to legacy content, so editorial judgment is required throughout — not something Fantasy's engineers or designers can own. Three specific features confirmed unlikely for Mexico: (1) team microsites — custom theming only completed in DS on Friday, dev just started this week; fallback is landing page template or keeping legacy Delta Tray URLs with redirects until teams sign off; (2) ads/sponsors — flagged low priority, likely no contractual obligation; (3) where to watch — fallback static country page feasible using existing components. Key risk flagged: premature go-live diverts ~50% dev capacity to production support, roughly doubling timeline for all post-launch work. Firdosh to draft email to Denise to clarify scope (share with Matt before sending), and send live event support proposal by Monday (copy Katherine). "Before Mexico" deadline ambiguity still unresolved — Fantasy needs to know if Denise means April 15, a week before, or day-of.
- **April 1, 2026 (post-meeting):** Lewis Slack notes after Denise meeting — Lewis flagged a "real misconnect" between Denise and ground reality. Four issues: (1) Timeline still not aligned between parties; Steve/Firdosh own this as they're closest to engineering output. (2) Content authoring being on Fantasy is new to Lewis too; Matt taking this up with Fantasy today for immediate clarity -- editorial judgment required across many new modules, not a simple lift and shift. (3) Product-to-dev process called out as broken: poor quality tickets, poor executed designs, QA running exploratory testing instead of ACs, tickets not updated -- Lewis views this as a 3-5 month fix. (4) Fantasy cutting corners on everything to hit the deadline; every conversation with Hayley/Espi and every review with Victor surfaces unconsidered items or out-of-scope gaps (CMS structures, FE requirements, tag and tenant management, UI design). Lewis tracking but says nigh impossible without owning it from the inside. Denise's message taken as a clear signal that the team should be free to run this as needed to get it done.
- **April 1, 2026:** Denise Web Cutover Meeting — Mexico City confirmed as target cutover; Virginia as fallback. Critical CMS authoring blocker: Sanity entities/modules not structured until ~April 6; FantasyCo front-loaded leaderboard and video for South Africa. Major misalignment: FantasyCo doesn't appear to understand they own CMS content authoring (resourced for this in last two exec calls with Firdosh); Matt flagged this morning and pushing for immediate clarification call. FantasyCo proposed excluding team microsites from Mexico scope — deemed unacceptable (standard components, no justification). D3 content migration unblocked: LIV owns all D3 content; requesting full CMS copy from D3 for Forge → Sanity migration. Full leaderboard testing via PMY sim starts tomorrow; two days next week + two days pre-Mexico.
- **March 27, 2026:** LIV Golf Web Sync (with Steve, Nick, Andrew, Lewis, Lisa, Yorick) — leadership-dev gap persists: Denise pushing pre-Mexico launch, team recommends testing during Mexico then launching before Virginia. Player/team pages not ready until week of April 13; 50+ content pieces need QA. Path-to-air testing confirmed for April 7 and 13 (48-hr windows, SA event replay). Video streaming parity achieved — more stable than app SDK. Rollback plan in progress (DNS TTL, CloudFlare, load balancer). Cutover requirements being documented; Delta Tray fallback still required. Priority framework needed for production issues vs roadmap.
- **March 20, 2026:** Katherine 1:1 — Denise pushing pre-Mexico web launch despite technical concerns; scope reduction planning underway; critical path confirmed as leaderboard data, team sites, and press releases. Pulse Live proposal due Monday; Fantasy Co not preferred; GlobalLogic vs Pulse Live decision expected early next week. Delta Tray termination letter going out within the week (60-day notice clause). Matt unavailable March 25–April 6.
- **March 19, 2026:** Lewis 1:1 — leaderboard testing running on local machines, not yet on dev build. Denise pushing hard for Mexico launch (likely her last event before departure). Delta Tray legal trigger needs Denise to action next week. Feature cuts confirmed inevitable; critical path is messaging, video, leaderboard, shot callback. Global Logic 24-headcount proposal vs Fantasy's 5; front-end engineering leader hired (visa pending). Aaron hired as additional design support. LivX relaunch by Jim: auto-membership with account creation; gaming/fantasy under LivX umbrella.
- **March 18, 2026:** David 1:1 — dev build now receiving leaderboard and video data for South Africa confidence testing. Launch window narrowed to Mexico week; Denise wants beginning of week, Fantasy prefers Saturday. Content population starts week of March 23; team pages mostly templated; Mexico event assets being created by David/Aaron this week.
- **March 17, 2026:** Project Apex Production Sync — no consensus on exact Mexico launch date (Steve: mid-Mexico; Denise: before). Insufficient QA, content, and testing time flagged as risks. Galleries non-critical and deferrable. Outstanding December invoice stuck in approval process. URL redirect mapping due April 3. Leaderboard DS integration 95% complete; remaining work first week of April. Dev URL to be shared with LIV team for parallel testing during South Africa.
- **March 17, 2026:** Nick 1:1 — content bottleneck: external team can't create Duels/Four Aces pages without internal knowledge; working with Jesse on solution. Julian offer extended and accepted; 3-month transition. Google Analytics paid licence needed (~$40k, budget unclear). Lewis professional maturity concerns raised — process over execution, bypassing management.
- **March 13, 2026:** Katherine/Matt catch-up — website launch timeline tension: Denise wants launch during Mexico week vs Fantasy preference for 2 weeks later. Delta Tray migration process ready but can't start until departure notice. Fantasy contract ending mid-May; need new vendor onboarded by early-mid April. GlobalLogic claims next-day availability. Matt to follow up with Denise on vendor selection in South Africa.
- **March 13, 2026:** Team dynamics — Lewis and Arthur creating friction during mid-event hotfix; UK team freelancing into others' lanes. Matt planning message to Lewis about giving grace during live fixes and focusing on testing/documentation.
- **March 12, 2026:** Board scrutiny on 6-week delay; Denise firm on May 4 deadline. Three-phase plan locked: South Africa skeleton, Mexico soft launch (~90%), Virginia full cutover.
- **March 12, 2026:** Lewis taking end-to-end ownership of standings, stats, and ads from Monday March 16. Target: functional leaderboard before end of South Africa event.
- **March 12, 2026:** Content migration from D3 blocked pending legal sign-off. Sanity CLI script ready; 1.5–2 weeks minimum after D3 is notified. Matt to discuss with Denise in South Africa.
- **March 12, 2026:** Design system files fragmented across 6–8 locations; slowing development. David to consolidate; Steve to write detailed ACs for standings/leaderboard/scorecard.
- **March 12, 2026:** Production follow/unfollow error (datetime validation) blocking TestFlight approval. Needs urgent fix.
- **March 12, 2026:** Fallback plan required for Mexico City launch. Nick's team assessing config-based data generation for testing without live event dependency.
- **March 11, 2026:** Nick and Andrew onboarding initiated; focus on ViewLift SDK integration, OTT components, and secured test environment. BFF exists and tested with GraphQL router serving 95% of leaderboard requirements
- **March 11, 2026:** Marketing team requesting LIV Golf Music/Concerts page ahead of imminent Live Nation announcement; AJ Dolan suggests renaming to "LIV Golf Music"; requires Ross review before sharing with Live Nation
- **March 11, 2026:** Mexico launch path confirmed at 80–90% completion; 29 themes complexity and zero live exposure highlighted as primary risks
- **March 10, 2026:** Mexico City soft cutover mid-April; Virginia full cutover May 7; leaderboard designated as priority #1 for testing
- **March 9, 2026:** Public launch extended to May 4; soft launch April 16; design system due March 31
- **March 3, 2026:** Team expanded with 2 additional developers plus QA; detailed project plan presented to Denise
- **February 27, 2026:** GlobalLogic proposal restructured to emphasise web/mobile capabilities, removed OTT focus

### Meeting History
| Date | Meeting | Key Outcome |
|------|---------|-------------|
| 2026-04-01 | [[EXT] Project Apex \| Alignment with Matt](../meetings/2026/2026-04-01-project-apex-alignment-with-matt.md) | Vendor alignment: content migration scope dispute (Denise's lift-and-shift expectation vs Fantasy's SOW); three features at risk for Mexico; 50% dev capacity diversion risk flagged; Firdosh to draft email to Denise |
| 2026-04-01 | [Denise Web Cutover Meeting](../meetings/2026/2026-04-01-denise-web-cutover-meeting.md) | Mexico City target confirmed; CMS blocked until ~Apr 6; FantasyCo content authoring misalignment flagged; D3 migration unblocked; team microsites exclusion rejected |
| 2026-03-27 | [[EXT] LIV Golf Web Sync](../meetings/2026/2026-03-27-liv-golf-web-sync.md) | Leadership-dev gap on launch timing; path-to-air testing April 7 & 13; cutover requirements underway; rollback plan in progress |
| 2026-03-20 | [Katherine 1:1](../meetings/2026/2026-03-20-katherine-1-1.md) | Pre-Mexico launch push; scope reduction (leaderboard, team sites, press releases); Pulse Live proposal Monday; Delta Tray termination |
| 2026-03-19 | [Lewis 1:1](../meetings/2026/2026-03-19-lewis-1-1.md) | Mexico pressure; feature cuts confirmed; Delta Tray legal trigger; new vendor search; LivX relaunch |
| 2026-03-18 | [David 1:1](../meetings/2026/2026-03-18-david-1-1.md) | Dev build testing live; content population starts Mar 23; Mexico week launch window |
| 2026-03-17 | [[EXT] Project Apex Production Sync](../meetings/2026/2026-03-17-project-apex-production-sync.md) | No launch date consensus; invoice stuck; URL redirect mapping Apr 3; DS 95% complete |
| 2026-03-17 | [Nick 1:1](../meetings/2026/2026-03-17-nick-1-1.md) | Content bottleneck; Julian accepted; GA licence needed; Lewis maturity concerns |
| 2026-03-13 | [Katherine / Matt Catch Up & Nick/Jesse Catch Up](../meetings/2026/2026-03-13-katherine-matt-catch-up.md) | Mexico week launch target; Fantasy contract ending mid-May; vendor selection; team dynamics |
| 2026-03-12 | [Denise × Russell & Firdosh // Project Apex Check-in](../meetings/2026/2026-03-12-denise-russell-firdosh-apex-check-in.md) | Board pressure on delay; three-phase testing plan; May 4 firm deadline |
| 2026-03-12 | [Apex Web Follow Up](../meetings/2026/2026-03-12-apex-web-follow-up.md) | Leaderboard target for South Africa; testing strategy; fallback plan for Mexico |
| 2026-03-12 | [Lewis / Matt 1:1](../meetings/2026/2026-03-12-lewis-matt-1-1.md) | Lewis ownership of standings/stats/ads; Denise pressure on timeline; D3 migration blocked on legal |
| 2026-03-12 | [Weekly Dev Status](../meetings/2026/2026-03-12-weekly-dev-status.md) | Follow/unfollow production bug; design system fragmentation; ACs needed |
| 2026-03-11 | [Apex Web: Nick and Andrew Onboarding](../meetings/2026/2026-03-11-apex-web-nick-andrew-onboarding.md) | Integration goals, BFF status, ViewLift SDK focus |
| 2026-03-11 | [Lewis / Matt 1:1](../meetings/2026/2026-03-11-lewis-matt-1-1.md) | Denise departing; product strategy; post-launch concerns |
| 2026-03-10 | [Sync on Updated Deck](../meetings/2026/2026-03-10-sync-on-updated-deck.md) | Mexico launch path confirmed; 29 themes complexity; rollback risk |
| 2026-03-10 | [Web Cutover Plan w/ Denise, Nick, Andrew](../meetings/2026/2026-03-10-web-cutover-plan-denise-nick-andrew.md) | Mexico City soft cutover mid-April; Virginia full May 7 |
| 2026-03-09 | [Web Timeline Meeting w/ Denise](../meetings/2026/2026-03-09-web-timeline-meeting-denise.md) | Launch to May 4; soft launch April 16; design system March 31 |
| 2026-03-03 | [Firdosh/Steve Chat about Timelines](../meetings/2026/2026-03-03-firdosh-steve-chat-timelines.md) | Detailed plan presentation; 2 devs + QA added |
| 2026-02-27 | [LIV Golf Catch Up](../meetings/2026/2026-02-27-liv-golf-catchup.md) | Proposal restructured for web/mobile focus |
| 2026-02-06 | [LIV Golf Version 6.07 Priority and Release Planning](../meetings/2026/2026-02-06-livgolf-v607-priority-release-planning.md) | Web launch planning beginning |

---
*Part of the [notes repo](../README.md)*
