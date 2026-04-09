# [EXT] LIV Golf Web Sync

**Date:** March 27, 2026
**Attendees:** Matt Saunders, Steve Croll, Nick Connor, Andrew Lim, Lewis Bouvier, Lisa Loukas, Yorick Demichelis
**Source:** Granola — `2470e291-2095-4ea4-8b3d-e724c24ce4e8`

---

## Website Launch Timeline & Risk Assessment

- Denise pushing for pre-Mexico City launch (March 27th)
- Development team recommends testing during Mexico, launch before Virginia
  - Significant content migration work remains
  - Player/team pages not available until week of April 13th (Mexico week)
  - 50+ pieces of content requiring QA across all devices
- Gap remains between leadership expectations and development timeline
  - Need follow-up meeting to align on specific launch criteria
  - Cost factor driving urgency (Delta Tray contract termination window)
  - Fallback to Delta Tray required regardless of launch approach

## Content Migration Strategy

- Content team structure finalized
  - Lewis, Arthur, Matt, Frank, Lean, John handling 99% of configurations
  - Brian and Mike providing editorial audit support
  - Jesse's team unlikely to provide substantial support
- Migration approach
  - Audit existing content for new page structures
  - Like-for-like content transfer acceptable if editorial updates unavailable
  - All-hands approach once CMS pages pass UAT
  - New content agency being explored for email/events

## Testing Plan — Mexico City Event

- Path to air testing scheduled
  - April 7th and 13th (both Mondays)
  - Full South Africa event replay (rounds 3-4 including playoffs)
  - 48-hour continuous testing windows
  - Fantasy team + LIV internal testing focus
- Simulator documentation expected April 3rd–4th
- Video streaming parity achieved with existing web experience
  - More stable than app SDK implementation
  - Leaderboard/scorecard data reaching parity post-South Africa

## Launch Criteria & Rollback Planning

- Cutover requirements being documented
  - Leaderboard/scorecard functionality (no Delta Tray fallback)
  - Content stability across all devices
  - Full QA completion for migrated content
- Rollback scenarios under development
  - DNS TTL reduction planned
  - CloudFlare routing alternative being investigated
  - Load balancer traffic shifting as backup option
- Production support impact
  - Team shifts from planned work to reactive bug fixes
  - 20% incomplete features may slow further development
  - Priority framework needed for production issues vs roadmap items

---

## Action Items

- [ ] Schedule follow-up meeting to align on specific launch criteria
- [ ] Complete cutover requirements documentation
- [ ] Deliver simulator documentation by April 3rd–4th
- [ ] Complete URL redirect mapping by April 3rd
- [ ] Path to air testing: April 7th and 13th (48-hour windows)
- [ ] Define priority framework for production issues vs roadmap items
- [ ] Develop rollback scenarios (DNS TTL, CloudFlare, load balancer)

---

*Notes captured via Granola · Exported to markdown repo*
