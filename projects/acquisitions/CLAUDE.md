# Project: Acquisitions Pipeline
**Type:** Research / Client (hybrid: acquisition sourcing and vetting)
**Status:** Active
**Owner:** Matt Saunders
**Last Updated:** 2026-05-27

---

## Brief

Central system for sourcing and vetting businesses Matt is considering buying. Solves the "I have to check every marketplace constantly" problem by automating discovery, then rails the review process so good deals are not missed and bad deals are killed quickly. Parent system to individual deal project folders.

## Goals

- Maximize listing coverage without manual site-by-site checking
- Triage new listings in minutes against a clear thesis
- Graduate qualified deals into their own top-level project folders
- Maintain a factual record of what was reviewed, killed, and why

## Overview

Discovery runs via a scheduled Claude task (successor to the disabled `music-biz-monitor`). Output is a dated markdown digest. Matt skims, flags items worth pursuing. Flagged items promote to `deals/[slug]/` for triage and vet. Serious deals eventually graduate out of this project and get their own folder under `/projects/`.

Thesis lives in `thesis.md` and drives the discovery filter. Sources in `sources.md`. Pipeline state in `pipeline.md`.

Current live deal folder: `/projects/renna-media-acquisition/`. Archived deal folder: `/archive/driving-school-acquisition/`.

---

## Folder Layout

- `thesis.md`: acquisition criteria, refined as Matt's view sharpens
- `sources.md`: marketplaces, brokers, search patterns
- `pipeline.md`: active listings and their triage state
- `digests/YYYY-MM-DD.md`: dated output from discovery scheduled task
- `inbox/`: listings Matt pastes in manually, pre-triage
- `deals/[deal-slug]/`: promoted listings with listing.md, triage.md, vet.md
- `archive/`: killed listings with reason (learning signal)
- `templates/`: listing-intake, triage-scorecard, vet-report, daily-digest

---

## Workflow

1. **Discover.** Scheduled task reads thesis and sources, runs searches, writes `digests/YYYY-MM-DD.md`
2. **Skim.** Matt reviews digest, flags listings worth a closer look
3. **Intake.** Flagged listing copied to `deals/[slug]/listing.md` using template
4. **Triage.** `triage.md` completed with the scorecard. Fast kill or fast pass
5. **Vet.** For passes, `vet.md` completed with deeper diligence
6. **Graduate.** Serious deals get their own top-level project folder and leave the pipeline

Killed listings move to `archive/` with a one-paragraph reason.

---

## Interaction Rules

Do not invent listings. Every entry in the pipeline must come from a real source (digest, inbox paste, broker email, etc.).

Never mark a listing "killed" without the reason captured. The archive is a learning signal and the reason matters.

When working in this project, read `thesis.md` before producing any filter output or digest. The thesis is the source of truth for what counts as "matching."

---

> **INSTRUCTIONS FOR CLAUDE:**
> - Do NOT modify the structure or headings of this file
> - At the start of every session, read `memory.md` and briefly summarize any relevant prior context before starting work
> - Check `/templates/` before creating any new outputs; use an existing template if one fits
> - Reference `/shared/brand-voice.md` and `/shared/tone-guidelines.md` for any written output
> - After completing meaningful work, append a summary to the **Session Log** in `memory.md`
