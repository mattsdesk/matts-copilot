# Ways of Working Chat w Fantasy

**Date:** March 11, 2026
**Attendees:** Matt Saunders
**Source:** Granola — `8dc03b0b-e0ab-4704-8817-4126a8b190e8`

---

## Development Process & Collaboration

Fantasy's internal ticket review process is extremely time-intensive — cross-checking requirements against old implementations for edge cases takes as long as writing the original ticket. Developers begin their day without Haley's context and can only work from ticket documentation, creating a bottleneck when complex features require subject matter expertise.

For the leaderboard, the plan is to reverse-engineer existing battle-tested logic from the current app and port it to React/Next.js — this gives Matt more time to review for gaps before development starts.

---

## Meeting Structure & Communication

Fantasy will continue running internal daily standups independently; developers need space for candid conversations about task assignments without client participation. In place of client standups, a middle-ground model was agreed:

- Matt reviews the JIRA board for status updates
- Direct developer outreach for complex ticket clarifications
- Daily Matt–Haley sync for 2-minute team status updates, main questions from dev sessions, and edge case coverage

---

## Ticket Complexity & Resource Allocation

Simple tickets (CMS mapping, events pages) don't require deep collaboration. Matt's involvement is reserved for complex features: leaderboard logic, shot tracing with edge cases (drop balls, penalties, slope calculations), and scorecard functionality. Risk identification process agreed: Matt flags high-risk/complex tickets during review; Haley marks tickets requiring pre-development developer consultation; time zone handoff coordination for morning discussions.

---

## Quality Assurance Workflow

A new JIRA UAT column has been added to the workflow. Process flow: Development → QA approval → assigned to Matt in UAT column → Matt reviews daily or every other day with design team → final approval before release. Matt owns final UAT sign-off on all features. A separate product approval column is available if needed.

---

## Project Constraints

This is a fixed-fee contract — Fantasy owns full scope delivery responsibility, not an augmentation model. Limited overlap hours create scheduling challenges. Steph/Victor collaboration time with Haley's team must be protected. Matt's involvement is focused on high-value subject matter expertise rather than general status updates.

---

## Action Items

- [ ] Matt reviews JIRA board daily for status updates
- [ ] Matt and Haley to establish daily 2-minute sync rhythm
- [ ] Matt flags high-risk tickets during review; Haley marks tickets requiring pre-dev developer consultation
- [ ] Fantasy: maintain internal standups without client participation
- [ ] Fantasy: reverse-engineer leaderboard logic from app for web port

---

*Notes captured via Granola · Exported to markdown repo*
