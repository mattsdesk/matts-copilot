# Ad Inventory Schema (Jan 2026 advertiser census)

One row per ad observed across the 30 active Jan 2026 editions. Excludes Renna self-promo unless otherwise noted (flagged with `is_renna_self`).

## Columns

| Field | Type | Notes |
|---|---|---|
| paper_slug | str | folder name under `inputs/editions/`, e.g. `westfield-monthly` |
| paper_display | str | "Westfield Monthly" |
| circulation | int | from page 14 rate sheet |
| month | str | "2026-01" |
| page | int | 1-16 |
| advertiser_raw | str | as printed on the ad (preserve casing, suffix) |
| advertiser_normalized | str | canonical form for cross-paper rollup, e.g. "Magnolia Home Remodeling" |
| category | enum | services, real_estate, healthcare, food, retail, automotive, education, financial, professional, public_notice, renna_self, other |
| size_class | enum | 1U, 2U, 4U, 6U, 9HP, 12U, 18FP, BACK, BANNER, FPBOX, 2PG |
| size_dims | str | e.g. "6.5x4" |
| size_sq_in | float | computed from dims |
| position | enum | front_strip, front_box, full_page, half_top, half_bottom, quarter, eighth, banner, back_cover, inline |
| is_renna_self | bool | TRUE for Renna Media own promotional ads (NJLocalInfo, Renna Media flyer service, Mind Your Own Local Business with Joe Renna, etc.) |
| phone | str | extracted phone number if present (helps fingerprint duplicate advertisers) |
| website | str | URL on the ad |
| confidence | enum | high, medium, low - how confident we are about size_class and advertiser identity |
| notes | str | any qualifiers |
| source_pdf | str | full path |

## Size class taxonomy (from rate card)

| Class | Dimensions | Sq In |
|---|---|---|
| 1U | 3.25 x 2 | 6.5 |
| 2U | 6.5 x 2 or 3.25 x 4 | 13 |
| 4U | 3.25 x 8 or 6.5 x 4 | 26 |
| 6U | 6.5 x 6.25 or 10 x 4 | 40.6 / 40 |
| 9HP | 6.5 x 9 or 10 x 7 | 58.5 / 70 |
| 12U | 6.5 x 14 | 91 |
| 18FP | 10 x 14 | 140 |
| 2PG | 21 x 14 | 294 |
| BACK | 10 x 14 (back cover) | 140 |
| BANNER | 8.25 x 2 (front page banner) | 16.5 |
| FPBOX | 1.5 x 4 (front page box) | 6 |

## Methodology

1. Render every page of every Jan 2026 PDF to PNG at 110 DPI for human-readable cataloging (see `outputs/page-renders/`)
2. Visually classify each ad on each page into a size class by matching against the rate card grid
3. Capture advertiser name, phone, website where visible
4. Flag Renna self-promo ads separately so they don't inflate "paid advertiser" counts
5. Normalize advertiser names: strip LLC/Inc/&, standardize casing, merge obvious duplicates
6. Count unique advertisers per paper (paid only) and across all papers (paid only)

## Outputs

- `analysis/jan-2026-ad-inventory.xlsx` - tidy ad inventory + advertiser pivot + bundle distribution + revenue estimate
- This file is built incrementally. Westfield Monthly is seeded in this session; other papers added as cataloged.

## Cross-paper advertiser identification

Ads that look identical on different papers are usually the same advertiser running a multi-town buy. Use phone number + headline + visual style as the fingerprint. Examples observed in Westfield Monthly Jan 2026 that very likely run in other papers:

- Estates Roadshow (taking 2 full pages: one promotes Clark Holiday Inn show, one Kenilworth Hotel show. Same buyer, two ad creatives, both running widely)
- Magnolia Home Remodeling (full page, central NJ regional)
- Mr Handyman (half page, regional)
- Spring Grove Rehab (half page, real estate market driven)
- Marano & Sons Auto Sales (full page back cover, Garwood-based)
- Best Places Expo (full page, regional event)
- Coldwell Banker / Frank Isoldi (full page, town-specific)
- NJ Antique Buyers (half page, regional)

Town-specific advertisers (single paper buys) are typically smaller sizes (1U-4U) with local phone numbers and addresses tied to the host town.
