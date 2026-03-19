# Einhorn Proposal Generator

> **Template type:** Agent Instructions + Output Structure
> **Usage:** Read this file when generating any new proposal for Einhorn — new services, expanded scope, new practice groups, or new campaigns.
> **Output:** PDF saved to `/einhorn/proposals/` (create folder if it doesn't exist)

---

## AGENT INSTRUCTIONS — DO NOT INCLUDE IN FINAL OUTPUT

### Step 1: Load Project Context

Read these files before writing anything:

1. `client-profile.md` — client identity, practice areas, stakeholders, constraints
2. `memory.md` — recent decisions, campaign history, open questions, new contacts

Extract and hold in mind:
- Current active channels and performance signals
- Any new stakeholders or scope discussions relevant to this proposal
- Strategic decisions that should inform scope, framing, or positioning
- Any open questions (e.g., practice area priorities) that may affect recommendations

### Step 2: Gather Proposal Inputs

If the user has not already provided the following, ask before writing:

| Field | Notes |
|---|---|
| Service type | What is being proposed? (paid search / SEO advisory / content & social / multi-track) |
| Sub-project / practice area | Family law, criminal, PI, firm-wide, etc. |
| Primary contact | Who receives this proposal? (Steven, Alissa, Mat, etc.) |
| Monthly media budget | If paid campaign is included — paid to Google |
| Monthly management fee | Matt's fee |
| Initial term length | How long is the commitment? |
| Launch timeline | Expected days to launch after approval |
| Any special scope notes | Custom inclusions, exclusions, or context |

If the user provides partial inputs (e.g., budget and service but not term), fill in sensible defaults from existing engagement context and note them.

### Step 3: Select the Right Framing

Adjust tone and emphasis based on service type:

- **Paid Search (conquest or acquisition):** Lead gen via search, keyword expansion, bid strategy, conversion tracking
- **SEO / AI Advisory:** Organic visibility, AI surface presence, content structure, advisory-only scope
- **Social / Content / Personal Brand:** Content production, distribution, personal brand building, audience development
- **Criminal group or practice group expansion:** Reference existing firm engagement, structure as expansion or parallel track
- **Multi-track:** Combine relevant section language, be clear about what's bundled and what's separate

### Step 4: Write Rules

- Do NOT use marketing buzzwords
- Do NOT mention internal files, this template, or "this engagement" in a meta way
- Do NOT be overly verbose — every sentence should earn its place
- Keep tone: confident, direct, advisory
- Assume reader is smart but non-technical
- Primary objective is always: **qualified client leads**
- Note website dependency wherever relevant — it impacts conversion outcomes
- Separate traffic generation from on-site conversion performance throughout

### Step 5: Generate the PDF

After drafting the content, generate a PDF using `reportlab` (Python).

**Visual style:**
- Font family: Helvetica for body, Helvetica-Bold for headings
- Body text: 10pt, 14pt leading
- Section headings: 12pt bold, followed by a 1pt horizontal rule
- Colors: `#1a1a1a` for body text, `#000000` for section headers
- Page margins: 72pt (1 inch) on all sides
- Page size: Letter (8.5 × 11 in)
- No decorative borders or design flourishes — clean and professional
- Page numbers: bottom center, format "Page X of Y"

**Header block (top of page 1):**
- Left: "Proposal" in 20pt bold
- Below that: "Prepared for Einhorn" in 11pt regular
- Right-aligned: date in MM/DD/YYYY format
- Full-width 1pt rule below header block

**File naming:** `einhorn-proposal-[service-slug]-[YYYY-MM-DD].pdf`
(e.g., `einhorn-proposal-criminal-seo-2026-03-19.pdf`)

**Save location:** `/sessions/focused-lucid-bell/mnt/einhorn/proposals/`
(Create the folder if it doesn't exist)

### Step 6: Log the Deliverable

After saving, append to `memory.md`:

- **Deliverables Log:** `[date] | [sub-project] | Proposal PDF | [one-line description]`
- **Session Log:** Note that a proposal was created and for whom

---

## OUTPUT STRUCTURE

Use the sections below in order. Section titles are final. Customize body content based on context and inputs.

---

### 1. Overview

Write 2–3 short paragraphs. Focus on lead generation through search. Reference the specific channel or service being proposed. If this builds on existing activity, note the continuity briefly. Avoid recapping what the client already knows at length.

---

### 2. Context

Tailor this section based on the specific proposal:

- If tied to paid search → reference performance signals from existing campaigns where available (e.g., strong CTR on generic queries, low CPC, identified keyword opportunities)
- If SEO → reference organic opportunity, current visibility gaps, competitive landscape
- If social/content/personal brand → reference existing presence, channel opportunity, what's working
- If new practice group → reference the expansion context and what's driving it

Keep to 3–5 bullets or a short paragraph. Include 1–2 data points if available from memory. Do not manufacture data.

---

### 3. Strategy

Always include these four components. Customize the examples to match the service type and practice area.

**1. [Primary Channel or Focus]**
Describe the core targeting or content approach. For paid search: keyword focus, match types, intent signals. For SEO: content structure, visibility targets, off-site vs. on-site priorities. For social: content types, platform focus, publishing cadence.

**2. Ad or Content Development**
How will messaging be developed? For paid: ad copy strategy and alignment with user intent. For SEO: content brief and structure. For social: content format, personal brand angle, tone.

**3. Optimization**
How will performance be managed over time? For paid: keyword refinement, bid adjustments, negative keywords. For SEO: iterative updates based on ranking signals. For social: content testing, engagement analysis.

**4. Conversion Tracking**
How will leads be measured? Always include phone calls and form submissions as primary conversion actions. Note any tracking dependencies.

---

### 4. Measurement Framework

Always include both layers. Keep language simple and non-technical.

**Traffic Quality**
- Click-through rate (CTR)
- Cost per click (CPC) [paid only]
- Search query relevance [paid] / Keyword ranking progress [SEO]

**Lead Conversion**
- Form submissions
- Phone calls

Note that successful outcomes depend on both traffic quality and the website's ability to convert that traffic.

---

### 5. Important Considerations

Always include this section. Keep tone advisory, not defensive.

Website performance plays a critical role in overall results. Messaging clarity, trust signals, and ease of contact directly affect conversion rates. While [this campaign / this work] drives qualified traffic, converting that traffic into leads depends on the on-site experience. Where relevant, recommendations will be provided to improve conversion performance.

---

### 6. Scope of Work

Always include both Included and Not Included. Adjust line items to match service type.

**Included:**
- [List service-specific items — e.g., campaign setup, keyword research, ad creation, content briefs, advisory hours, etc.]
- Ongoing performance management
- Reporting and insights

**Not Included (unless otherwise agreed):**
- Website redesign or development
- Landing page creation
- Advanced analytics or CRM integration
- [Any other service-specific exclusions]

---

### 7. Investment

Populate with provided values. If a value was not provided, use `[TBD]`. Maintain this exact structure.

**Monthly Media Budget:**
$[MEDIA_BUDGET] (paid directly to Google)
*(Omit this line entirely if no media budget applies — e.g., SEO advisory only)*

**Management Fee:**
$[MANAGEMENT_FEE] / month

**Initial Term:**
[TERM_LENGTH]

- Month 1–2: Calibration and optimization
- Month 3+: Scaled performance
*(Adjust milestone language to match service type if needed)*

---

### 8. Timeline

Keep simple. Adjust only if the user specifies otherwise.

- Launch / kickoff: Within [X] days of approval
- Initial performance review: After ~30 days
- Ongoing optimization thereafter

---

### 9. Next Steps

Keep to 3 steps. Align with the Einhorn workflow.

1. Confirm approval of scope and budget
2. [Service-specific: e.g., "Ensure conversion tracking is properly installed and validated" / "Align on initial content priorities" / "Confirm target practice area and audience focus"]
3. Align on launch timeline and initial priorities

---

### 10. Signature

Always include exactly as follows:

---

Approved by: ___________________________

Date: ___________________________

---

*Prepared by Matt Saunders*
