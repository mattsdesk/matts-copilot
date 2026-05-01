# January 2026 Ad Analysis - First Pass

## Outputs

- `analysis/jan-2026-ad-analysis.xlsx`
- `analysis/jan-2026-ad-analysis-inventory.csv`
- Builder: `analysis/build_jan_2026_ad_analysis.py`

## Scope

- Month: January 2026
- Papers: 30 active Renna Media editions
- Method: Westfield Monthly was manually cataloged, then all other PDFs were auto-scanned for ad boxes, phone fingerprints, repeated full-page creatives, size class, and paper distribution.

## Headline Findings

- 427 total inventory rows captured, including paid ads, Renna self-promo, PSA/editorial candidates, and review candidates.
- 365 paid or potential-paid ad placements.
- 80 paid or potential-paid advertiser fingerprints.
- 32 rows require visual review, mostly image-only full-page/back-cover creatives with no extractable text.

## Bundle Distribution

| Paper Count | Advertisers |
|---|---:|
| 1 paper | 40 |
| 2-3 papers | 13 |
| 4-6 papers | 13 |
| 7-12 papers | 8 |
| 13-20 papers | 4 |
| 21-30 papers | 2 |

## Largest January Advertisers by Paper Count

| Advertiser | Papers | Primary Size |
|---|---:|---|
| Magnolia Home Remodeling | 28 | 18FP |
| Best Places Expo | 23 | BACK / 18FP |
| VDS NJ Video Tape Transfers | 20 | 2U |
| Glenn Buys Motorcycles | 18 | 1U |
| Estates Roadshow | 16 | 18FP |
| Pizzano Photo Studio | 14 | 9HP |
| Dr. Murphy Suburban Chiropractic | 12 | 2U |
| My Handyman & Painter | 12 | 18FP |
| NJ Antique Buyers | 10 | 6U |
| St Michael School Cranford | 9 | 6U |

## Caveats

- This is a first-pass census, not a fully hand-verified final.
- Westfield rows are manually verified; other papers are matched by phone, visual creative hash, and ad-box geometry.
- Image-only full-page ads without embedded text are preserved as `Unknown full-page creative [id]` and listed in `Needs Review`.
- Counts are advertiser fingerprints, not contracted customer records. One legal entity with multiple creative names may still need normalization after broker/customer-list diligence.

## Diligence Implications

- January shows meaningful concentration in large cross-paper buyers. Two advertisers appear in 21+ papers and five advertisers appear in 13+ papers.
- The book is not just tiny local classifieds. Several regional advertisers buy very large placements across many towns.
- Ask Joe for the January 2026 invoice/customer export to reconcile this census against actual billings, discounts, comps, and unpaid PSAs.
