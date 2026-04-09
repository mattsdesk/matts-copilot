# Web Cutover Plan w/ Denise, Nick, Andrew

**Date:** March 10, 2026
**Attendees:** Matt Saunders (LIV Golf)
**Source:** Granola — `707e31da-914c-474a-a4da-80374c47d424`

---

## Web Cutover Timeline & Constraints

- Cannot miss cutover date — technical standpoint requires pushing through, ok with some risk and uncertainty
- Fantasy Co proposing soft cutover for **Mexico City (mid-April)** as testing phase, then full cutover for **Virginia (May 7th weekend)**
- Denise strongly opposed to timeline extension due to cost and complexity
- Current state: app runs on Fantasy, web still on D3

> **Private note:** Get it out so we can get to bugs. Priority: leaderboard has to work, then viewing experience is #2 (including VOD, livestream, shot callback).

---

## Technical Priorities & Requirements

- **Priority #1:** Leaderboard must work (critical requirement)
- **Priority #2:** Viewing experience — VOD, livestream, shot callback
- Fantasy Co already owns SDK knowledge from app development — same integrations and data flows, just different platform
- Backend for Frontend (BFF) already built for data handling

---

## Key Risk Areas & Testing Strategy

Fantasy Co is gun-shy after Riyadh/Adelaide issues and wants extra caution. Four main concern areas:

1. Behind schedule due to mobile scramble
2. Gun-shy from previous painful launches
3. Leaderboard testing complexity with live data transitions
4. ViewLift SDK integration (different from their custom build)

Push for accelerated timeline to test components in **South Africa** — leaderboard and video player priority for live event testing. "Doesn't have to be pretty, just functional."

---

## Action Items

- [ ] **Matt:** Schedule meeting with Steve for tomorrow 10:30 Eastern — discuss how Nick/Andrew can embed with Fantasy Co team; explore accelerating leaderboard/video features for South Africa testing
- [ ] **Nick/Andrew:** Brief teams on technical support requirements
- [ ] **Denise:** Follow up with Fantasy Co Thursday/Friday for project details
- [ ] **Andrew:** Own ViewLift coordination and timeline alignment
- [ ] **All:** Review Fantasy Co deck and Jira tickets for technical requirements

---

*Notes captured via Granola · Exported to markdown repo*
