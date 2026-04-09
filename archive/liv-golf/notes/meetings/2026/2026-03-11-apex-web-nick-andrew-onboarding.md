# Apex Web: Nick and Andrew Onboarding

**Date:** March 11, 2026
**Attendees:** Matt Saunders
**Source:** Granola — `15b027ca-d75c-4332-a8e4-ef1201ab85e9`

> *Meeting goal: figure out how to get Andrew and Nick integrated into the project*

---

## Project Integration Goals

- Need additional support resources to reduce risk and build confidence for web delivery
- Focus on adding value for flow integrations and data delivery
- Support adjustments to delivery approach, especially around ViewLift challenges

---

## Leaderboard Implementation Status

- BFF (Backend for Frontend) already exists and is tested
  - GraphQL router integrates with flow data
  - Schema powers 95% of leaderboard requirements
  - Currently serves mobile app, will extend to web
- Business logic mostly in BFF; display logic remains in front-end
  - Playoff triggers (team vs. player)
  - Withdrawal/DQ states
  - Between-round state management
- Real-time updates via SSE (Server-Sent Events)
  - Pulls flow data and broadcasts changes
  - Updates pushed to CDN for client consumption

---

## Testing Challenges and Requirements

- Live event testing is critical for validation
  - Need to test throughout entire 4-round event plus playoffs
  - PMY simulation testing has been problematic (data inconsistencies, 50x speed issues)
  - Path-to-error testing requires 20-person coordination across time zones
- Key testing scenarios needed:
  1. Between-round states and transitions
  2. Event status changes without score data
  3. Groupings and starting hole assignments
  4. Edge cases not covered in documentation
- South Africa event unlikely for testing due to design delays — implementation in progress

---

## Action Items

- [ ] Schedule follow-up to review project deck in detail
- [ ] Andrew: focus on ViewLift SDK integration and OTT components
- [ ] Set up secured test environment for ViewLift player validation
- [ ] Target end of current event for entitlements and web stream testing across browsers
- [ ] Use next two events (before South Africa gap) for live testing validation
- [ ] Explore live event testing opportunities for upcoming events

---

*Notes captured via Granola · Exported to markdown repo*
