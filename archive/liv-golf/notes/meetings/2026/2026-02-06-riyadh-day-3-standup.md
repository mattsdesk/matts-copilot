# Riyadh Day 3 Standup

**Date:** February 6, 2026
**Attendees:** Matt Saunders (LIV Golf)
**Source:** Granola — `89411e94-a155-4de0-80c9-4a2091200c04`

---

## Critical Priority Fixes

- **Pre-round hole situation** — overnight integration attempt failed and broke existing functionality; Victor confirmed issue is on their side (logic problem with start hole field calculation); current hole field still working (verified); not urgent for today's round
- **Countdown timer broken on homepage** — currently tied to event start instead of round start; goes to 00s when activated; needs to tie to upcoming round start time only, remove manual overrides

**Agreed action plan:** Drop all other development work except these two fixes; package together in 7.0 release; push out ASAP before moving to other items.

---

## Countdown Timer Workaround Options

- Replace homepage with event landing page temporarily
  - Pros: working countdown timer, space for additional content
  - Cons: loses hamburger nav and Fan Caddy access during implementation (Fan Caddy could move to bottom nav)
- CMS flexibility available but requires significant reconfiguration
- Decision pending Denise's input on risk tolerance vs. user experience trade-offs

---

## Overnight Updates

- D3 authentication issues resolved — team worked through the night; server-side cache purge completed; header refresh added for all users
- Denise's 4.31 error resolved (power user-specific issue)
- Audio issues flagged as ongoing concern for broadcast

---

## Action Items

- [ ] Someone to discuss homepage switching option with Denise before standup
- [ ] Reset development priorities with team on Zoom call
- [ ] Breakout session to clarify: requirements for hole data fix, data source specs, logic causing data source breaks

---

*Notes captured via Granola · Exported to markdown repo*
