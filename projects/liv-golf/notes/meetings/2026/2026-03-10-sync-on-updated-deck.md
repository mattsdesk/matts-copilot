# Sync on Updated Deck

**Date:** March 10, 2026
**Attendees:** Matt Saunders, Firdosh Tangri (LatitudeGo/Fantasy Co), Natsai Mandisodza (Fantasy Co), Russell Hampton (Fantasy Co), Steve Croll (Fantasy Co)
**Source:** Granola — `1d07a761-7ee7-458e-abf4-9f500cdd6fd5`

---

## Web Launch Timeline & Challenges

- Launch pushed from Virginia to Mexico due to development delays
  - Design resources pulled to fix app issues before Riyadh
  - Roster changes days before Riyadh diverted web resources
  - Team branding updates and additional feedback rounds cascaded delays
  - Full requirements gathering revealed larger scope than originally estimated
- Web complexity underestimated initially
  - 29 different themes need re-implementation from app to web
  - More pages, complex layouts, and templates than anticipated
  - Mobile web + desktop testing required across all variations
  - URL structure, redirects, SEO responsibilities don't exist in app

---

## Testing Requirements & Risk Assessment

- Live testing critical after Riyadh experience
  - Multiple P0/P1 bugs only surfaced during live events
  - Simulation testing doesn't replicate real data states and transitions
  - Hong Kong column shift issue was invisible during simulation
  - App hardened through 3 live events; web has zero live exposure
- Rollback/cutover carries unacceptable risk
  - DNS propagation delays prevent instant rollback
  - SEO damage from URL remapping not reversible
  - CMS state divergence creates dual sources of truth
  - Content loss potential during rollback
- Two potential paths discussed:
  1. Rush to Virginia launch (high risk, no testing)
  2. Mexico launch with early cutover at 80–90% completion

---

## Resource Planning & April Timeline

- Additional engineering, design, and PM added at Fantasy Co's cost
- Current app maintenance team already scaled down
- Post-launch: small maintenance team handles both app and web
- April 9th launch would exclude ads, sponsors, subscriptions
- Early smoke test for South Africa leaderboard/video player would divert resources from main development

---

## Action Items

- [ ] Firdosh: send updated deck to Matt via Slack for review
- [ ] Matt: share deck with Denise, Andrew, and Nick before Thursday discussion
- [ ] Firdosh: 1:1 with Denise Thursday to discuss timeline options
- [ ] Steve: add example about 29 themes complexity and Riyadh bug statistics to deck

---

*Notes captured via Granola · Exported to markdown repo*
