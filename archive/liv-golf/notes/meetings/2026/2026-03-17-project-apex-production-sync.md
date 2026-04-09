# [EXT] Project Apex | Production Sync

**Date:** March 17, 2026
**Attendees:** Matt Saunders, Jade Skelton, Katherine Kuo, Natsai Mandisodza (Fantasy), Lisa Collins (Fantasy), Kazandra Bonner (Fantasy)
**Source:** Granola — `3fd390fd-90b2-4f97-bae9-f36428309005`

---

## South Africa Event Preparation

- Testing capabilities confirmed for South Africa event
  - Watch live mainstream group and team streams ✓
  - Leaderboard testing available ✓
  - Scorecard testing not available
- Firdosh followed up with Denise on testing plan today
- Dev URL to be shared with LIV team for parallel testing during live event
  - Side-by-side comparison with live data
  - More thorough bug detection than previous events
- Support coverage aligned well with dev team timezone
- Team playoff remains untested (only saw individual playoff)
  - Previous bugs traced to SMT data issues, not downstream problems

## Web Launch Timeline & Risks

- **Critical misalignment**: No consensus on web launch date
  - Steve advocating for mid-Mexico event
  - Denise preferring before Mexico launch
  - Dates within same week but not finalised
- Timeline pressure creating quality concerns:
  1. Insufficient QA time before launch
  2. Limited content upload window
  3. Compressed testing cycles
- Feature prioritisation review needed post-South Africa
  - Some development ahead of schedule (4-day estimate completed in 1 day)
  - JIRA updates required for Mexico readiness assessment
  - Galleries identified as non-critical, deferrable feature
- Recommendation: Launch timing should allow proper QA (preferably Michigan or later)

## Project Operations & Next Steps

**Contracting & Invoicing**
- Outstanding December invoice stuck in approval process
- Matt to investigate approval bottleneck with finance
- Backlog contract sent to Denise for priority signing
- Web contracts need date updates once launch timing confirmed

**Design System Integration**
- Leaderboard integration 95% complete
- Remaining work: leaderboard and stats components
- Timeline: First week of April (post-Web DS delivery)
- Fantasy investing additional week of designer time

**Content Migration Planning**
- URL redirect mapping doc needed by April 3rd
- Jesse providing D3 messaging today for redirect scope
- Migration pipeline: Delta Tray → Sanity (maintaining historical records)
- Fallback: Top 50 pages if full mapping unavailable

**Push Notifications**
- LIV testing Salesforce Marketing Cloud integration
- Developing in shell app before providing to Fantasy
- Timeline dependent on Salesforce rollout completion

---

## Action Items

- [ ] Matt: Follow up with Denise on launch timing alignment (Friday meeting)
- [ ] Matt: Investigate stuck December invoice with finance team
- [ ] Jade: Provide URL redirect mapping by April 3rd
- [ ] Fantasy: Share dev URL and South Africa support plan
- [ ] Fantasy: Send scope alignment doc for end-of-week feedback

---

*Notes captured via Granola · Exported to markdown repo*
