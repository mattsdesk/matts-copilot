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
