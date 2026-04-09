# Manish Interview

**Date:** January 23, 2026
**Attendees:** Matt Saunders (LIV Golf)
**Source:** Granola — `0bbf000e-df6f-40e0-b6a4-40e71f823bae`

---

## Candidate Background

- 15+ years in next-gen mobile tech and entertainment streaming
- Career: coding/assembly → DRM/streaming → full-stack platform at Discovery/Eurosport
- Co-founded TV startup (failed due to funding) → current AI consultancy role
- Specialization: serving millions of users on streaming platforms

---

## Technical Architecture & Global Distribution

- Content delivery: Fragmented MP4 formats (HLS, FMP4), CDNs positioned globally, Netflix-style ISP caching for extreme cases
- DRM: signed URLs with time expiration, stream encryption with separate license server, AES-based keys via embedded player libraries
- Global scalability: multi-region deployment with geo-based routing, Kubernetes/serverless auto-scaling, availability zone distribution

---

## Crisis Management Scenario

- Safari HLS streaming issue: jumping to 2-hour countdown instead of live event
- Diagnostic approach: rule out platforms → examine manifest files (UTC time issues) → check Safari-specific caching → implement workarounds
- P0 vs. P1 classification based on user impact scale; typical resolution: 8–10 hours including testing

---

## Data Compliance & Operations

- All PII must remain in London (GDPR) — proposed pseudo-anonymized IDs for global replication with UK data vault
- 300–500ms latency acceptable threshold for entitlement checks

---

## Current Team Structure Context

- Matt's DTC team: product people, 1 designer, PMO, occasional Yorick support; heavy reliance on vendors, no internal engineers
- Nick's enterprise team provides shared infrastructure (data pipelines, content management)
- 24/7 sports schedule demands weekend work and global timezone flexibility

---

*Notes captured via Granola · Exported to markdown repo*
