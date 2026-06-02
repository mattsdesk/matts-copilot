# Deals

One folder per listing that has been promoted from a digest or inbox item.

Folder name: `YYYY-MM-[slug]` (year-month prefix helps sort chronologically; use the month the listing was promoted).

Standard contents:

- `listing.md`: intake using `../templates/listing-intake.md`
- `triage.md`: scorecard using `../templates/triage-scorecard.md`
- `vet.md`: deep diligence using `../templates/vet-report.md` (only if triage passes)
- `source.md`: original inbox file or broker email if applicable
- Any attached CIMs, financials, or broker communications

Killed deals move to `../archive/[same-slug]/` with a reason captured in triage.md or vet.md.

Graduated deals (serious enough for LOI or deep engagement) move to their own top-level project folder, e.g., `/projects/[deal-slug]-acquisition/`. See `/projects/renna-media-acquisition/` as the current example.
