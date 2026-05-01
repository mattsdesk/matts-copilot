# Memory - Renna Media Acquisition

---

## Current Status

Active engagement. Broker call complete 2026-04-28. **Lunch with Joe Renna scheduled Thursday 2026-04-30 ~12:00 PM in Cranford.** This is the buyer-seller fit meeting. Decision point post-lunch: write LOI or pass.

This is Joe's 4th attempted deal. Three prior buyers died in the last 12 months. Eric is gating buyers carefully. Matt is the first qualified buyer in the new round (Eric remarketed the listing 2026-04-27).

---

## Key Facts

- 30 hyper-local town newspapers, 206K mailings/month across Essex/Morris/Union/Somerset NJ
- 120 active advertisers, ~80% recurring + ~10% seasonal repeat
- Top 15% of advertisers = 60% of revenue (real concentration; CIM understates this)
- Husband-wife team, ~160 hrs/month combined, no office, eliminated only employee in 2024 (social media manager)
- Asking $500K, $250K down, $250K seller note at 8% over 36 months ($7,834/mo)
- 4-week transition; 5yr/25mi non-compete
- Reason for sale: retirement
- Pricing raised once since 2008 (in 2021 due to COVID)
- 6 new papers launched in 2024; revenue dipped that year, recovered in 2025
- Broker: Eric Sharret, Murphy Business - Westfield, 973-245-9445

---

## Key Decisions / Positions

- **Target offer range:** $375K-$425K. Asking is at the top of Main Street SBA range and the 2025 SDE rebound is partly artificial (eliminated headcount).
- **Two intertwined theses:** (a) print as cash flow asset to service debt, (b) Montclair Digital cross-sell to a warm SMB book. Either alone is marginal; together is interesting.
- **Structural protection needed:** holdback or earnout tied to 12-month advertiser retention given concentration risk.
- **Do not assume the "scalable launch" narrative.** 6 papers in 2024 produced negative operating leverage that year. Need unit economics by town before trusting it.

---

## Where ChatGPT memo is wrong or soft

- Said "no customer concentration" - CIM says top 15% = 60% of revenue. Material risk.
- Said "average $140K SDE" - true but the 2025 rebound to $179K is partly headcount cuts, not real improvement. Normalized 2025 SDE ~$130-140K.
- Said valuation is 3.0-3.5x - asking is actually 2.8x recent / 3.6x avg. Top of SBA range for declining-industry asset.
- Soft on COGS structure (70-78% with no pricing power and USPS exposure).
- Soft on the actual operational complexity buried in two heads.
- Discount-tier margin compression hypothesis (38% off at 6 towns drives the gap between theoretical and actual margins): directionally right but assumption-stacked. Treats ~5 towns/advertiser, dominant 6-town tier, 50% rate-card margin, and linear marginal cost as facts. None are confirmed. Need actual bundle distribution from edition sampling and per-issue print/postage breakout before pricing this into LOI. Also undercooks the post-close churn risk of compressing the discount curve in year 1.

---

## Open Questions (priority)

**Top 3 critical unknowns:**
1. Retention driver: relationship vs ROI vs habit (determines if revenue survives transition)
2. Advertiser ROI: do customers see measurable results (determines long-term durability)
3. Operational dependency: end-to-end monthly cycle, what's documented vs in heads

**Secondary:**
- Top 20 advertiser table: name, tenure, annual spend, vertical
- Postage line broken out of COGS (USPS rate exposure)
- Vendor contracts vs handshake (printing + mailing)
- 2024 dip cause: advertiser losses or new launch + headcount
- True normalized labor cost to run as W-2 (probably $70-90K all-in)
- Working capital, AR aging, deferred revenue (cash basis tax returns hide a lot)
- Inbound inquiry volume and conversion rate
- Performance of the 6 papers launched in 2024 - time to breakeven
- Has anyone ever asked Joe/Tina for digital services? How often?

---

## Session Log

### 2026-04-27
- Loaded CIM (18-page PDF) into `inputs/`
- Reviewed CIM and Matt's ChatGPT investment memo
- Produced initial analysis flagging where ChatGPT was wrong (customer concentration, normalized SDE, valuation framing)
- Established the dual thesis: print cash flow + Montclair Digital cross-sell
- Set up project folder following driving-school-acquisition pattern
- Captured Matt's 10-area diligence framework into `analysis/diligence-questions.md`
- Logged graduation in `/projects/acquisitions/pipeline.md`
- Built integration model in `analysis/integration-model.xlsx` with 7 sheets: Cover, Assumptions, Deal_Structure, Print_PnL, MD_CrossSell, Combined_Returns, Sensitivity
- Default model assumes: $400K price, 70% SBA + 10% seller note + 20% buyer equity, $65K operator + 20% burden + $25K social media restoration
- Key output: at $400K price with Print Base + MD Mid (10% advertiser conversion), 75% IRR on $105K buyer equity over 5 years; $113K Y3 owner cash. Sensitivity confirms walk-away price at $550K with low MD conversion (5%).

### 2026-04-29
- Found the rate card: page 14 of every Renna paper is the rate sheet ("Renna Media Newspapers Rate Sheet"). It is the de facto pricing table and circulation card combined. Captured from `westfield-monthly/2026-01.pdf` p14. Transcribed to `analysis/rate-card-2026-01.md` (and `analysis/rate-card-2026-01.xlsx`).
- Calculated effective discount by ad size at the 6-town tier vs running the same ad in 6 separate single-town buys. The "38% discount at 6 towns" framing from ChatGPT is true at the full-page tier (12 Unit FP at 6 towns = $2,100 vs 6 x $600 = $3,600 = 42% off) but is much shallower at the 1-Unit business card tier (6 towns = $560 vs 6 x $110 = $660 = 15% off). Real margin compression is concentrated in the larger ad sizes, not across the board. The right diligence question is: what is the actual size mix in the book?
- Built the Jan 2026 advertiser census. Pilot paper: westfield-monthly cataloged by vision (33 ads incl 7 Renna self-promo). Schema at `analysis/ad-inventory-schema.md`. Pages rendered at `outputs/page-renders/{slug}-2026-01/page-NN.png` (110 DPI, all 30 papers).
- Built phone-number fingerprinting: pypdf text extraction across all 30 Jan 2026 PDFs, regex out (xxx)xxx-xxxx patterns. Found 99 unique phones, of which I labeled 64 as paid advertisers, ~25 as PSAs/community, 2 as Renna self, several editorial. Output at `analysis/jan-2026-phones-tidy.csv` and `analysis/jan-2026-phone-bundle.csv`.
- **Paid-only bundle distribution from phone fingerprinting (Jan 2026):**
  - 1 paper: 27 phones (42%) - long tail of single-paper local advertisers
  - 2-3 papers: 11 phones (17%)
  - 4-6 papers: 15 phones (23%) - cluster at the rate-card 6-town discount tier
  - 7-12 papers: 6 phones (9%)
  - 13-21 papers: 4 phones (6%) - top reach buyers (Estates Roadshow 16, Glenn Motorcycles 17, VDS NJ Video 20, Pizzano Photo 14)
  - Caveat: phone count overstates unique advertisers by ~10-15% (Marano has 3 phones, Reynolds 2-3, Bataille 3, Calderone 2, Hobbie 2). True unique paid advertisers Jan 2026 ~50-55.
- **Revisits the ChatGPT 38% framing:** the 4-6 paper bucket holds 23% of paid phones, NOT a majority. Long-tail single-paper buys (42%) are bigger than expected. Bundle concentration is real but "everyone takes 6 towns" is overstated. The biggest reach buyers (16-20 papers) are 4 specific advertisers - they matter more for revenue concentration than discount strategy generally.
- Floor revenue estimate from rate-card lookup x phone fingerprints x assumed sizes: $31K/month for Jan 2026. CIM-implied monthly is ~$70K. Gap of ~$40K likely sits in (a) full-page color image ads where phone isn't text-extractable (Magnolia, Best Places Expo, Coldwell full-pagers), (b) larger-than-assumed sizes for some advertisers, (c) my default 2U for unclassified advertisers.
- **CIM advertiser count check:** CIM claims 120 active advertisers. Phone scan finds ~50-55 paid in Jan 2026. Either CIM counts annualized unique across all months and seasonal, or Jan is slow, or CIM is generous. Add to Joe questions.
- Built `analysis/jan-2026-ad-inventory.xlsx` with 9 sheets: README, Rate Card, Circulation, Ad Inventory, Coverage Status, Bundle Distribution, Phone Bundle (Auto), Bundle Findings, Revenue Estimate. Zero formula errors.
- Captured the rate card from page 14 of every paper to `analysis/rate-card-2026-01.md` and as the Rate Card sheet in the xlsx. Effective rates 11/1/2024 forward.
- Built a broader first-pass Jan 2026 ad analysis workbook at `analysis/jan-2026-ad-analysis.xlsx` plus CSV at `analysis/jan-2026-ad-analysis-inventory.csv` and summary at `analysis/jan-2026-ad-analysis-summary.md`. Method: manually verified Westfield rows + auto-scanned ad boxes, phone fingerprints, and repeated full-page creative hashes across all 30 active Jan 2026 papers.
- First-pass Jan 2026 results: 427 total inventory rows, 365 paid/potential-paid placements, 80 paid/potential-paid advertiser fingerprints, 32 rows requiring visual review (mostly image-only full-page/back-cover creatives). Bundle distribution: 40 advertisers in 1 paper, 13 in 2-3, 13 in 4-6, 8 in 7-12, 4 in 13-20, 2 in 21-30.
- Largest Jan 2026 reach buyers by paper count: Magnolia Home Remodeling (28 papers, mostly full-page), Best Places Expo (23), VDS NJ Video Tape Transfers (20), Glenn Buys Motorcycles (18), Estates Roadshow (16, 32 full-page placements across two creatives), Pizzano Photo Studio (14), Dr. Murphy Suburban Chiropractic (12), My Handyman & Painter (12).
- Built two longitudinal 2024-2025 advertiser-retention outputs:
  - `analysis/phone-retention-2024-2025.xlsx` / `.csv` / summary: fast phone-fingerprint view, best for retention and cross-paper purchasing.
  - `analysis/advertiser-retention-2024-2025.xlsx` / `.csv` / summary: broader ad-box + full-page creative view, useful for placement/size texture but much noisier (many image-only rows need review).
- Phone-retention results across 652 available 2024-2025 issues: 12,587 paid/potential-paid phone observations, 643 paid/potential-paid phone fingerprints, 442 active in 2024, 391 active in 2025, 190 seen in both years (43.0% of 2024 fingerprints appeared at least once in 2025), 80 active 12+ months, 47 active 18+ months, average next-month retention 69.7%.
- Jan 2024 cohort decay: 129 active phone fingerprints in Jan 2024; 65 still active by Dec 2024 (50.4%), 61 by Jan 2025 (47.3%), 44 by Dec 2025 (34.1%). Average monthly active phone fingerprints fell from 146.6 in 2024 to 113.3 in 2025 despite more active issues in 2025.
- Key retention implication: there is a durable recurring core, but a large transient layer. Diligence should focus on top 25 reach buyers: annual spend, tenure, contract status, Joe/Tina relationship dependency, and whether the 2024-launched papers created new advertisers or mostly spread existing regional buyers across more papers.
- Converted `notes/growth-plan-preview-1.png` / `notes/growth-plan.html` into an editable Word handout at `notes/renna-media-growth-plan-editable.docx`. Built with editable text, tables, shaded callouts, roadmap boxes, and footer/signature. LibreOffice render QA was unavailable on this machine (`soffice` not installed); verified first-page visual layout with macOS Quick Look preview.

### 2026-04-30
- Post-lunch debrief call with Eric Sharret (broker). Meeting with Joe Renna went well; Matt demonstrated serious candidacy. Key takeaway: Joe passion-driven operator; three prior buyers died in last 12 months due to deal complexity.
- Identified three critical risk tiers: (1) staffing dependency on 2 part-time employees (small margins limit hiring); (2) price sensitivity of client base (pricing is perceived as competitive advantage, limits margin expansion); (3) revenue concentration (20% of clients = 80% of revenue, largely relationship-dependent).
- Strategic upside validated: Joe overly focused on print expansion, missing digital service opportunities for existing client base. Montclair Digital cross-sell thesis remains the binding constraint on valuation.
- Eric next steps: connect Matt with SBA brokers from previous discussions; inquire about data room access (typically post-LOI). Matt to develop LOI structure addressing staffing/retention/financing risks before submission.
- Meeting notes at `meetings/2026/2026-04-30-eric-sharret-debrief.md`.

### 2026-04-28
- Scraped rennamedia.com archives for all 32 publication pages and downloaded every monthly PDF from Jan 2022 through May 2026 (1,361 issues, 3.2 GB) into `inputs/editions/{slug}/{YYYY-MM}.pdf`
- Counted pages on every PDF using pypdf; 0 errors after re-fetching 24 truncated downloads
- Built `analysis/pagecount-by-edition.xlsx` with three sheets: Page Counts (pivot, month rows × 32 paper columns, hyperlinks to source PDFs, conditional color scale, row/column totals + average + count rows), Tidy (long-form filterable table), Summary by Paper (first issue, latest issue, # issues, avg/min/max pages)
- Also wrote `analysis/edition-manifest.csv` (URL list) and `analysis/page-counts.csv` (raw counts) for traceability
- Spot-checked 6 random PDFs with pdfinfo against pypdf counts: all match
- Coverage findings worth flagging in diligence:
  - **Peterstown NJ** and **Pride of North Plainfield** are listed on the homepage but have published nothing since 2021 (Pride) / 2009 (Peterstown). Press the broker on whether these are still operating or are dead/legacy. CIM claims 30 active papers; 2 of the 32 listed pages are silent.
  - **Cranford Monthly** archive ends Dec 2025 — no 2026 issues posted on the site; verify whether the paper paused or the archive page is just behind.
  - **Spirit of Union** latest is April 2026 (others have May 2026 published).
  - The **6 papers launched in 2024** are confirmed by the data: East Hanover View (13 issues from Dec 2024), plus Hanover Township Press, Life in Roseland, Livingston Monthly, Morris Township Times, Morristown Monthly (each 18 issues from Dec 2024). East Hanover lagging the others by 5 issues = mid-2025 launch, not 2024.
  - 24 of the established papers show full 53-issue coverage Jan 2022 through May 2026 (no missed months) which supports the "consistent monthly publication" claim.
- Pulled Census ACS 5-Year 2023 housing unit counts and 2022 CBP business establishment counts for the 30 covered municipalities. Built `analysis/mailing-universe-by-town.xlsx` with three sheets: Mailing Universe (per-paper breakdown with population, housing units, occupied/vacant, business estabs, estimated mailing universe, and delta vs CIM-implied per-paper average), Reconciliation (walks from raw Census totals to the 206K claim), and By County.
- **The 206,000 monthly mailings claim holds up.** Census housing units across the 30 active municipalities = 250,176 (incl. all of Elizabeth which overstates Renna's Elmora-only coverage). Excluding Elizabeth full-city = 201,236 housing units + ~20,000 business establishments. Adjusting for a realistic ~10K Elmora slice gets to ~221K combined homes + businesses, comfortably above the 206K claim (which suggests not every business in every ZIP gets a mail copy, which is reasonable).
- Caveat: Census housing units aren't identical to USPS deliverable addresses (apartments split, accessory dwellings, etc.). Get USPS EDDM postage statements from broker for paper-by-paper precision. Filed in `analysis/diligence-questions.md` Section 5 already.
- Patched a scraper bug: rennamedia.com archive labels misname all Jan-May 2026 issues as "2025" for Cranford Monthly and East Hanover View (URLs and filenames are correct as 2026; only the human-readable label is wrong). My label-first parser silently overwrote 5 months of legit 2025 issues with 2026 content. Fixed: moved files to correct slots, downloaded the real 2025 issues, re-counted pages, rebuilt `pagecount-by-edition.xlsx`. Cranford now 53 issues (full 2022-01 → 2026-05), East Hanover 18 (full Dec 2024 → 2026-05). Manifest at 1,371 editions.
- Two minor benign mismatches remain (spirit-of-union 2026-04/05 and summit-times 2025-03/04) where label and URL date disagree but no editions were dropped. Worth a glance later.
- **Broker call with Eric Sharret, ~45 min.** Notes in `notes/broker-call-2026-04-28.md`. Key signals:
  - Listed 2 months. Eric remarketed Mon 2026-04-27 after most recent buyer pulled out over the weekend. Matt is first up in new round.
  - **3 prior deals dead in 12 months.** Joe filters hard for CEO operators with growth vision; last buyer was a sales guy who could not "form a company" per Eric.
  - **Structure is flexible, price is not.** Asking $500K is anchored. The 50% seller note exists because Joe insisted on the headline number.
  - **Stock sale on the table** - Eric raised it unprompted (USPS portability, printer relationship, credit history). Worth modeling.
  - **Printer relationship is new** (~2 years, PA-based, after CT printer shut down). Refutes "deep printer dependency" risk.
  - **Cross-sell thesis validated anecdotally.** Eric: advertisers regularly ask Joe for digital help. Joe refers them away or makes ads for free.
  - **Eric's biggest concern (off sell-side hat):** post-close cash flow squeeze. After ~$94K/yr seller note service, ~$70-80K residual SDE has to fund both operator pay and growth investment.
  - Matt's positioning landed: 20yr media career (Disney/Marvel/fubo/LIV), AP journalism, existing Montclair Digital LLC, just left day job. Eric said the LLC piece "would be music to Joe's ears."
  - njlocalinfo.com still unconfirmed - Eric thinks Joe owns it but defers to Joe.
  - Next step: lunch with Joe in Cranford Thursday 2026-04-30 ~12:00 PM. Prep doc at `notes/joe-meeting-prep.md`.
- Did NOT share with Eric: target price range ($375-425K), integration model details, normalized SDE estimate, mailing universe analysis, page-count analysis. Powder kept dry for diligence and LOI phases.
- Granola transcript synced to `meetings/2026/2026-04-28-renna-media-broker-call.md` (separate from the curated `notes/broker-call-2026-04-28.md`).

### 2026-04-30
- **Lunch with Renna (Joe) in Cranford.** Notes in `meetings/2026/2026-04-30-renna-media-lunch.md`.
- Seller highlighted key themes: staffing bottleneck (graphic designer + editor needed), strong SOP documentation claims, pricing model constraints (multi-town discounts limit growth), untapped digital expansion opportunity, lifestyle-over-growth mentality, single vendor printing dependency, and 80/20 client concentration tied to personal relationships.
- **Key strategic insights from conversation:**
  - Joe explicitly aware of capacity limits and growth requirements (designer/editor hiring). Signals he understands what it takes to scale.
  - Digital "menu" is outsourced today but viewed as crossover opportunity. Advertisers already ask for digital help per broker; Joe hasn't pursued it.
  - Pricing power constrained by low-cost multi-town discount strategy. Room for margin expansion via pricing optimization + digital bundling.
  - Client concentration is real and relationship-dependent with top accounts. Material post-close retention risk.
  - No new information on njlocalinfo.com ownership.
- **Diligence outputs created:**
  - `analysis/post-lunch-diligence-checklist.md`: Structured verification items across documentation, pricing/margins, vendor relationships, unit economics, client concentration, and financial analysis.
  - Checklist maps lunch themes to specific asks: SOP verification, staffing cost modeling, pricing strategy analysis, vendor contracts, per-paper unit economics, client retention strategy, and cash flow/ROI modeling.
- **Next steps:** Request SOP documentation and top-20 advertiser list from broker; analyze per-paper contribution margins to validate incremental revenue assumptions; map client concentration risk and retention levers; prepare valuation negotiation framework based on margin improvement opportunity.
