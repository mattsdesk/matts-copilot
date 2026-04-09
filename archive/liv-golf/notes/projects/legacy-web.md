# Legacy Web

**Status:** 🟡 At Risk
**Owner:** Matt Saunders
**Last updated:** 2026-03-25

---

## Components

| Component | Status | Owner | Notes |
|-----------|--------|-------|-------|
| D3 / Current Site | 🟡 At Risk | — | Running until Apex Web cutover (May 4) |
| Cutover & Decommission Plan | ⏳ Pending | — | Needs defined plan post-May 4 |

---

> The legacy LIV Golf website (D3 platform) is the current live site running until the Apex Web cutover in May 2026. It will be decommissioned after the Virginia event (May 7). Risk is primarily around continuity during the transition window and ensuring nothing falls through the cracks between old and new platforms.

### Goal
Maintain stability of the current site through the May cutover and ensure a clean decommission with no content or functionality gaps.

### Status
The legacy D3 site remains live and is the public-facing LIV Golf website until the Apex Web cutover at the Virginia/DC event (May 4). Content migration from D3 to Sanity is blocked pending legal sign-off to formally notify D3 of the transition. Once legal acts, a 1.5–2 week minimum migration window is expected. A Sanity CLI script is ready to execute the migration. URL redirect mapping is due April 3 to ensure no broken links post-cutover. The Delta Tray decommission (separate vendor providing services to the legacy stack) has been triggered with a 60-day notice letter going out in late March.

### Key Decisions
- **March 20, 2026:** Delta Tray termination initiated — 60-day notice letter being sent by Denise; March/April team redistribution required
- **March 12, 2026:** D3 content migration blocked pending legal sign-off; Sanity CLI script ready; 1.5–2 weeks post-notification to complete
- **March 12, 2026:** Legacy site to remain live through May 4 Virginia event before full Apex Web cutover

### Open Questions
- When will legal sign-off be given to formally notify D3 and begin content migration?
- What is the formal decommission plan post-May 4 cutover?
- Are there legacy integrations or content that won't carry over to Apex Web?
- Who owns sign-off on the legacy site being fully decommissioned?
- Can URL redirect mapping be completed by the April 3 deadline?

---
---

## Tactical Detail

### Recent Updates
- **March 20, 2026:** Katherine 1:1 — Delta Tray termination within the week; Denise sending 60-day notice letter; enhanced team redistribution planned for March/April.
- **March 13, 2026:** Katherine/Matt — D3 migration process ready but cannot start until departure notice is sent. Sanity CLI script prepared; 1.5–2 week window once D3 is notified.
- **March 12, 2026:** Web cutover plan — Apex Web three-phase plan confirmed: South Africa (skeleton testing), Mexico (soft launch ~90%), Virginia May 4 (full public cutover). Legacy site runs in parallel through May 4.
- **March 12, 2026:** URL redirect mapping task identified; due April 3 to support SEO continuity.

### Meeting History
| Date | Meeting | Key Outcome |
|------|---------|-------------|
| 2026-03-20 | [Katherine 1:1](../meetings/2026/2026-03-20-katherine-1-1.md) | Delta Tray termination letter imminent; 60-day notice clause |
| 2026-03-13 | [Katherine / Matt Catch Up & Nick/Jesse Catch Up](../meetings/2026/2026-03-13-katherine-matt-catch-up.md) | D3 migration blocked on legal sign-off; CLI script ready |
| 2026-03-12 | [Web Cutover Plan w/ Denise, Nick, Andrew](../meetings/2026/2026-03-10-web-cutover-plan-denise-nick-andrew.md) | Three-phase plan confirmed; legacy site runs through May 4 |

---
*Part of the [notes repo](../README.md)*
