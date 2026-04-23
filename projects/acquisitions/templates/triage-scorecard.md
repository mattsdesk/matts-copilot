# Triage: [Business Name]
**Date:** YYYY-MM-DD
**Listing ref:** [path to listing.md or URL]

Goal: 60 second kill or pass decision. If genuinely unsure, default to pass and let vetting resolve it.

---

## Hard Filters (any fail equals kill)

- [ ] SDE in $250K to $1M range, or credible path to that within 12 months
- [ ] Located within ~1 hour drive of Montclair, NJ
- [ ] Not a food business; not a bread route; not a laundromat
- [ ] 5+ years in operation (or documented exception)
- [ ] Financials available for diligence (tax returns, not just seller-reported P&L)
- [ ] Not "buying a job": staff/management deliver the revenue, or there is a clear 6-12 month path to a structure where Matt works ON the business (strategy, growth, oversight) rather than IN it (frontline operations)

## Quality Signals (count positives, target 4+)

- [ ] Recurring or repeat revenue model
- [ ] Owner is not the sole revenue generator
- [ ] No customer above ~25% of revenue
- [ ] Seller financing offered
- [ ] Documented systems and SOPs
- [ ] Seller willing to stay through transition (6 to 12 months)
- [ ] Business growing or stable (not declining)
- [ ] Management or supervisor layer in place

## Red Flags (count concerns)

- [ ] Single key employee or license holder
- [ ] Declining revenue or margins
- [ ] Heavy regulatory exposure tied to the owner personally
- [ ] Concentrated customer base
- [ ] Thin or inconsistent financial documentation
- [ ] Vague "reason for sale"
- [ ] Owner's actual role understated in listing

---

## Decision

**Outcome:** [Kill / Pass to Vet / Need More Info]

**Reasoning (2 to 3 sentences):**

**If Pass:** Create `deals/[slug]/vet.md` from template. Update `pipeline.md` status to Vet.
**If Kill:** Move `deals/[slug]/` to `archive/[slug]/`. Update `pipeline.md` archived table with reason.
**If Need More Info:** List specific questions, stay in Triage until resolved.
