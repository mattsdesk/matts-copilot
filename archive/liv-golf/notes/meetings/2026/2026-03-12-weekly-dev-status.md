# Weekly Dev Status

**Date:** March 12, 2026
**Attendees:** Matt Saunders (web and mobile scope)
**Source:** Granola — `6d662706-3e3b-41b2-acaa-52a01a50e56a`

---

## Production Issue (App)

- Follow/unfollow error discovered in TestFlight build
- Root cause: stricter datetime validation format issue — same codebase unchanged since January
- Blocking full App Store approval
- Needs immediate investigation; production error details to be sent

---

## Design System Issues

- Design files fragmented across multiple locations (sprint UI files, design system files, etc.)
- Developers looking across 6–8 files to understand a single screen
- Many acceptance criteria reference "fits with design files" without specifics — not actionable
- Fix: David to own consolidation; Steve to write detailed ACs for standings, leaderboard, and scorecard with Hannah

---

## Development Process

- Reference implementation approach: porting GraphQL/BFF/SSE from React Native to React — going well
- Need better acceptance criteria for complex components before dev starts
- Espi out sick (key team member); David off today, back Monday
- Geo tickets logged and prioritised

---

## Action Items

- [ ] Matt: send production error details to team immediately
- [ ] Steve: write detailed ACs for standings/leaderboard/scorecard with Hannah
- [ ] David: consolidate design files and fix fragmentation (back Monday)
- [ ] Matt: follow up with Victor on Singapore data
- [ ] Schedule design system discussion with David

---

*Notes captured via Granola · Exported to markdown repo*
