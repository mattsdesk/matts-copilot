# Web Timeline Meeting w/ Denise

**Date:** March 9, 2026
**Attendees:** Matt Saunders (LIV Golf)
**Source:** Granola — `244e1bcd-4067-4c62-b6a7-4e2d2033a614`

---

## Regional Update & Event Success

- Team member safely evacuated from conflict zone — more people able to leave the region safely vs. the prior week
- **Hong Kong event** was highly successful: strong turnout, great crowd engagement
  - Jon Rahm finally secured his victory
  - Notable storylines: Smiley (rookie success) and Anthony Kim comeback — Kim's story went viral and transcended golf
- **Upcoming events:** Singapore (commercial crowd, hot/humid conditions), South Africa

---

## Website Launch Timeline — Major Delay

> Originally expected April 9th. New recommendation pushes full public launch to **May 4th** — a 6+ week delay.

| Milestone | Date |
|---|---|
| Design system completion | March 31 |
| Soft launch (internal testing only) | April 16 |
| Live event testing (Mexico City) | April 16–19 |
| 100% feature completion | April 24 |
| UAT testing window | April 1 – May 1 |
| **Full public launch** | **May 4** (before DC event) |

---

## Technical Justification & Risk Factors

- Website carries **higher risk than the mobile app** — no fallback mechanism if issues occur, and simulated environments don't replicate live scoring/event data
- **Lessons from Riyadh mobile launch:** live event testing caught bugs not found in simulation; Hong Kong parallel testing built confidence before successful launch
- Key complexity differences vs. the app:
  - Different View Lift SDK integrations
  - Responsive design required across web and mobile web
  - Extensive content entry requirements
  - Complex leaderboard integration testing

---

## Cost Impact & Next Steps

- Timeline represents a **significant budget overrun** — resources must be maintained across multiple teams; 2 additional developers being added to accelerate delivery
- Alternative discussed: April 16th cutover with a rollback plan
  - Denise strongly prefers this approach
  - Team recommends against it due to incomplete features

### Action Items

- [ ] Share JIRA board with all tickets
- [ ] Provide detailed breakdown of complexity differences vs. app
- [ ] Schedule **follow-up call Thursday** to discuss cost and logistics

---

*Notes captured via Granola · Exported to markdown repo*
