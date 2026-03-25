# Apex App

**Status:** 🟢 On Track
**Owner:** Matt Saunders
**Last updated:** 2026-03-19

---

## Components

| Component | Status | Owner | Notes |
|-----------|--------|-------|-------|
| iOS App | 🟢 On Track | Lewis / Fantasy Co | Released Feb 2026; live event testing ongoing |
| Android App | 🟢 On Track | Lewis / Fantasy Co | Released alongside iOS |
| Connected Devices | 🟡 At Risk | Andrew | Phase 2; Apple TV quality issues via third parties |
| ViewLift SDK Removal | 🟡 At Risk | Andrew | In progress; test environment being set up |
| Fantasy Co Vendor Management | 🟡 At Risk | Matt / Katherine | Ways of working process; daily standups required |

---

> Apex is LIV Golf's flagship iOS/Android app launched in February 2026 after a complete infrastructure rebuild. It provides real-time leaderboards, player data, video, fantasy features, and merchandising. The app is on track with strong engagement, though ViewLift integration remains a pain point being systematically reduced.

### Goal
Deliver a stable, feature-rich mobile platform for fan engagement during live events and expand to connected device support by year-end.

### Status
The app successfully launched in Riyadh despite significant technical challenges and has been performing well since Hong Kong with strong user engagement. The team deployed multiple hotfixes to resolve leaderboard delays, video player freezes, authentication problems, and hole number mapping. Current focus is refinement through live event testing, with South Africa designated as the critical testing phase for leaderboard and video functionality before the May web cutover. The team operates a dual-layer support model with existing team on shift duty and vendor augmentation when needed.

### Key Decisions
- **Late January 2026:** Launched with reduced feature set to maintain deadline
- **Early February 2026:** Implemented 24/7 event support with single communication channel across all teams
- **February 2026:** Ran parallel infrastructure testing in Hong Kong before full web cutover
- **March 2026:** Established dual-layer support model for event coverage
- **March 10, 2026:** Committed to South Africa testing phase for critical features before final cutover

### Open Questions
- When will ViewLift SDK dependencies be fully eliminated?
- What is the long-term team structure for maintenance vs. new features (Chris Dee recommends 3-pillar model)?
- How will connected devices reach feature parity with mobile?
- What is the succession plan post-Denise for app oversight?

---
---

## Tactical Detail

### Recent Updates
- **March 19, 2026:** Lewis 1:1 — Round status management documentation created by Lewis to define front-end behaviour for each round status; will be shared with Sporting Pulse for app implementation and has 3x reuse value (app + web + future connected devices). Design system debt identified: missing historical scores in standings and global remaining holes indicator — post-launch cleanup needed. Aaron confirmed as additional design support. Lewis continuing daily reviews with Haley covering edge cases previously missed.
- **March 18, 2026:** David 1:1 — App feedback pipeline established: David and Aaron identify UX issues, escalate to Arthur for backlog prioritisation. Issues flagged: confusing dots in discover feed, "all done" navigation problems, profile drawer issues, golf ball loading animation too long/repetitive. Aaron performing well — probing existing processes, presenting improvement ideas, strong communication with David. Arthur owns mobile platform prioritisation; Lewis owns web (temporary structure during stabilisation). Balanced sprints needed: big features + cleanup + fixes. Arthur and David to continue coordination call structure.
- **March 11, 2026:** Nick and Andrew onboarded to web/app project; BFF (Backend for Frontend) already exists with GraphQL router powering 95% of leaderboard requirements; Andrew focused on ViewLift SDK and OTT components; secured test environment to be set up for ViewLift player validation
- **March 11, 2026:** Lewis/Matt 1:1 identified three strategic product buckets: event experiences (player tracking, interactive maps), stats hub relaunch, and native ticketing via Fever SDK. Lewis frustrated with manual content work; automation of repeatable event experiences prioritised post-launch
- **March 10, 2026:** South Africa live testing designated as priority phase for leaderboard and video functionality before Virginia cutover; parallel infrastructure testing proved successful in Hong Kong
- **March 3, 2026:** TestFlight build ready; app launch delayed in parallel with web cutover; Hong Kong event successfully tested new infrastructure
- **February 19, 2026:** Two-layer event support strategy approved with existing team on duty plus vendor augmentation; tech lead to start first
- **February 6, 2026:** Multiple critical builds deployed (6.07, 6.08, 7.0) to fix hole number mapping, landscape video freezes, and leaderboard delays during Riyadh event
- **February 3, 2026:** ViewLift SDK fix required testing; app build 0.3 deployed; new maintenance team starts Feb 16th
- **January 21, 2026:** Apex launch confirmed for early February with friends and family rollout; production build ready
- **January 16, 2026:** Staging environment showcased with visual QA beginning; aggressive launch timeline with numerous fixes needed

### Meeting History
| Date | Meeting | Key Outcome |
|------|---------|-------------|
| 2026-03-19 | [Lewis / Matt 1:1](../meetings/2026/2026-03-19-lewis-1-1.md) | Round status management doc; design system debt (historical scores, remaining holes); Aaron design support confirmed |
| 2026-03-18 | [David 1:1](../meetings/2026/2026-03-18-david-1-1.md) | Feedback pipeline established; UX issues catalogued; Aaron onboarded; balanced sprint structure needed |
| 2026-03-11 | [Ways of Working Chat w Fantasy Co](../meetings/2026/2026-03-11-ways-of-working-chat-fantasy.md) | Ways of working alignment with Fantasy Co team |
| 2026-03-11 | [Apex Web: Nick and Andrew Onboarding](../meetings/2026/2026-03-11-apex-web-nick-andrew-onboarding.md) | BFF status; ViewLift SDK focus; live event testing requirements |
| 2026-03-11 | [Lewis / Matt 1:1](../meetings/2026/2026-03-11-lewis-matt-1-1.md) | Product strategy buckets; Denise departure; automation priority |
| 2026-03-10 | [Web Cutover Plan w/ Denise, Nick, Andrew](../meetings/2026/2026-03-10-web-cutover-plan-denise-nick-andrew.md) | Leaderboard priority #1; South Africa live testing before cutover |
| 2026-03-03 | [Firdosh/Steve Chat about Timelines](../meetings/2026/2026-03-03-firdosh-steve-chat-timelines.md) | TestFlight ready; Hong Kong infrastructure testing successful |
| 2026-02-27 | [LIV Golf Catch Up](../meetings/2026/2026-02-27-liv-golf-catchup.md) | GlobalLogic proposal refocus on web/mobile |
| 2026-02-19 | [Sync with Global Logic](../meetings/2026/2026-02-19-sync-global-logic.md) | Two-layer support; escalation protocol approved |
| 2026-02-06 | [Riyadh Day 3 Standup](../meetings/2026/2026-02-06-riyadh-day-3-standup.md) | Hole number fix urgent; pre-round integration failed |
| 2026-02-06 | [LIV Golf Version 6.07 Priority and Release Planning](../meetings/2026/2026-02-06-livgolf-v607-priority-release-planning.md) | Hole fix ready; full screen video disabled; 6.08 release planned |
| 2026-02-05 | [Denise Ops Huddle Up](../meetings/2026/2026-02-05-denise-ops-huddle-up.md) | Leaderboard delays, landscape freezes, events tab locked |
| 2026-02-03 | [OTT Sync](../meetings/2026/2026-02-03-ott-sync.md) | ViewLift SDK testing needed; maintenance team transition Feb 16 |
| 2026-01-21 | [Quick Sync w/ Denise and Team](../meetings/2026/2026-01-21-quick-sync-denise-and-team.md) | Launch confirmed early February; production build ready |
| 2026-01-16 | [Apex Demo Meeting](../meetings/2026/2026-01-16-apex-demo-meeting.md) | Staging showcased; visual QA beginning; aggressive timeline |

---
*Part of the [notes repo](../README.md)*
