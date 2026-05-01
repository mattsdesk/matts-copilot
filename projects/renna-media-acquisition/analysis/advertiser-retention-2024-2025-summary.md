# Advertiser Retention Analysis - 2024 and 2025

## Outputs

- `analysis/advertiser-retention-2024-2025.xlsx`
- `analysis/advertiser-retention-2024-2025-placements.csv`
- `analysis/build_2024_2025_retention_analysis.py`

## Scope

- Issues scanned: 652
- Paid/potential-paid placements: 14220
- Paid/potential-paid advertiser fingerprints: 957
- Rows requiring visual review: 10768

## Retention Signals

- Advertisers/fingerprints seen in both 2024 and 2025: 111
- Advertisers/fingerprints active 12+ months: 58
- Advertisers/fingerprints active 18+ months: 31
- Average next-month retention across observed months: 0.617

## Top Cross-Paper Buyers

| Advertiser / Fingerprint | Active Months | Max Papers In Month | Avg Papers When Active | Primary Size |
|---|---:|---:|---:|---|
| GUTTERS SIDING MASONRY STEPS FOUNDATIONS MURSELI PRO CONSTRUCTION | 18 | 30 | 25.0 | 18FP |
| KENZA ROOFING & CHIMNEY | 13 | 30 | 24.31 | 18FP |
| MAGIC IMPROVEMENTS (800) 206-8529 With this coupon. May not be combined with any | 10 | 30 | 25.0 | 1U |
| 528 N. Michigan Ave. Kenilworth, NJ | 10 | 30 | 28.0 | 18FP |
| Estates Roadshow | 8 | 30 | 24.75 | 18FP |
| We need 30 Ugly Homes with Ugly Kitchens, Bathrooms, Siding, Window, etc., Insid | 8 | 30 | 25.38 | 2U |
| princetonair.com | 8 | 30 | 27.25 | 1U |
| tigerroofingnj.com | 6 | 30 | 18.17 | 1U |
| ATTN: FORMER EMPLOYEES OF HYATT ROLLER BEARING FOUNDRY!!! If you know of or work | 1 | 30 | 30.0 | 1U |
| Unknown full-page creative d09f93747559 | 17 | 26 | 20.12 | 18FP |
| dancedemolitionandcleanupnj.com | 10 | 24 | 15.1 | 1U |
| chessinmillburn.com | 4 | 23 | 17.5 | 1U |
| Glenn Buys Motorcycles | 24 | 22 | 13.5 | 1U |
| woolleyfuel.com | 12 | 22 | 18.75 | 9HP |
| NJ Antique Buyers | 5 | 19 | 11.2 | 4U |

## Caveats

- This is a directional census built from PDFs, not a billing export.
- Phone fingerprints are better for retention than image-only creative hashes. If a full-page advertiser changes creative, this may split one customer into multiple fingerprints.
- Some PSAs/community notices can look like ads. They are filtered heuristically and retained in `Ad Placements` for audit.
- Reconcile against Joe's customer/invoice export before using for valuation.
