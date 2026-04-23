# Email-First Sourcing Setup

Moves the discovery engine from WebSearch to Gmail. Once set up, the scheduled task reads from your Gmail label and WebSearch becomes a secondary supplement.

Thesis runs two tracks (barbell): **Primary Operating Business** ($250K to $1M SDE, hands-on leadership role) and **Passive Holds** ($100K to $300K SDE, structurally passive only). Each marketplace below shows the saved searches to configure for both tracks.

---

## Matt's one-time setup

Steps 1 and 2 take ~3 minutes. Step 3 takes 30 to 45 minutes depending on how many sources you set up.

### Step 1: Create Gmail label (1 min)

Gmail web → gear → See all settings → Labels tab → Create new label → name it `Acquisitions` → Create.

### Step 2: Create Gmail filter (2 min)

Gmail → gear → See all settings → Filters and Blocked Addresses → Create a new filter.

Paste this in the **From** field:

```
notifications@bizbuysell.com OR noreply@bizbuysell.com OR @email.bizbuysell.com OR @bizbuysell.com OR @bizquest.com OR @dealstream.com OR @loopnet.com OR @em-mail.loopnet.com OR @synergybb.com OR @sunbeltnetwork.com OR @tworld.com OR @murphybusiness.com OR @vestedbb.com OR @acquire.com OR @flippa.com OR @empireflippers.com OR @quietlight.com OR @microns.io OR @dealmaker.com
```

Create filter, then tick:
- Apply the label: `Acquisitions`
- Never send it to Spam
- Also apply filter to matching conversations

Leave "Skip the Inbox" unchecked unless you want these hidden from your primary inbox.

---

### Step 3: Set up saved-search email alerts

Create accounts where needed, then configure the saved searches below. Each marketplace section shows what to set up for the Primary track and (where applicable) the Passive Holds track.

Shared constants across all marketplaces (apply to every search):

- **Geography:** New Jersey (all); New York (Westchester, Rockland, Orange lower, Nassau western, Bronx, Manhattan, Queens western); Pennsylvania (Bucks, Northampton); Connecticut (lower Fairfield)
- **Exclude sectors:** Restaurants, Food Service, Bakeries, Cafes, Bars, Catering, Food Production, Coin Laundries / Laundromats, Bread Routes
- **Alert frequency:** Daily (unless otherwise noted)

---

#### 1. BizBuySell (highest priority)

URL: https://www.bizbuysell.com/searchalerts/
Account: free signup

**Primary search: "Primary Operating NJ-NY-PA-CT"**
- Location: New Jersey; New York; Pennsylvania; Connecticut
- Cash Flow (SDE): $250,000 to $1,000,000
- Asking Price: $500,000 to $3,500,000
- Exclude categories: Restaurants and Food Service, Coin Laundries and Laundromats, Bread and Bagel Routes
- Alert: Daily email
- Save as: `Primary Operating Tri-State`

**Passive Holds search: "Self Storage Tri-State"**
- Location: same
- Category: Self Storage / Mini Storage only
- Cash Flow: any
- Asking Price: $300,000 to $2,000,000
- Save as: `Passive Self Storage`

**Passive Holds search: "Car Wash Tri-State"**
- Location: same
- Category: Car Washes only
- Cash Flow: any (filter manually on automated vs full-service)
- Save as: `Passive Car Wash`

**Passive Holds search: "Vending / Route Tri-State"**
- Location: same
- Category: Vending, ATM, Amusement & Game Routes
- Cash Flow: $100,000 to $300,000
- Save as: `Passive Routes`

**Passive Holds search: "Equipment Rental Tri-State"**
- Location: same
- Category: Equipment Rental
- Cash Flow: $100,000 to $300,000
- Save as: `Passive Equipment Rental`

---

#### 2. BizQuest

URL: https://www.bizquest.com/myaccount/savedsearches/
Account: free signup

**Primary search**
- States: NJ, NY, PA, CT
- Cash Flow: $250K to $1M
- Exclude: Restaurants, Food Service, Bakeries
- Alert: Daily
- Save as: `Primary Operating Tri-State`

**Passive Holds searches** (one each):
- Self Storage, tri-state, any cash flow → `Passive Self Storage`
- Car Wash, tri-state → `Passive Car Wash`
- Vending/Route, tri-state → `Passive Routes`

---

#### 3. DealStream

URL: https://dealstream.com/account/preferences
Account: free signup

- Preferences: New Jersey, New York, Pennsylvania, Connecticut
- Categories: all except Food
- Alert: Daily or Weekly (their feed is broker-heavy and lumpy)
- DealStream's saved-search tool is less granular than BizBuySell, so set one broad search here rather than multiple per track. The scheduled task will segment Primary vs Passive in the digest.

---

#### 4. LoopNet Businesses

URL: https://www.loopnet.com/profile/alerts
Account: free signup (LoopNet is CoStar-owned; you may need a CoStar-lite profile)

**Primary search**
- Property Type: Business for Sale
- State: NJ, NY, PA, CT
- Price Range: $500K to $3.5M
- Save as: `Primary Operating Tri-State`

**Passive Holds search**
- Property Type: Business for Sale
- Category: Self Storage Facilities, Car Wash, Campground/RV Park, Marina
- State: NJ, NY, PA, CT
- Price Range: $250K to $2M
- Save as: `Passive Holds Tri-State`

LoopNet is strongest for real-estate-anchored passive holds specifically.

---

#### 5. Synergy Business Brokers

URL: https://synergybb.com/
Account: free signup

- Sign up for their general email newsletter. No granular filtering available.
- They cover NJ/NY and occasionally PA/CT.
- Tag on intake: check radius, exclude food, route to Primary or Passive based on type.

---

#### 6. Sunbelt Business Advisors

URL: https://www.sunbeltnetwork.com/
Regional offices: NJ (several), NY (Manhattan, Long Island, Westchester)

- Sign up for newsletters from the NJ and NY-metro office sites directly.
- No fine-grained filter; the scheduled task will filter incoming emails against the thesis.

---

#### 7. Transworld Business Advisors

URL: https://www.tworld.com/
- Request to be added to the buyer list for NJ and NY metro offices.
- Email address for buyer lists: usually listed on each regional office page.

---

#### 8. Murphy Business

URL: https://www.murphybusiness.com/
- Request buyer-list email for NJ and NY metro offices.

---

#### 9. VestedBB

URL: https://vestedbb.com/
- Regional (mostly NJ). Sign up for listings email.

---

#### 10. (Optional: Digital track, if you keep digital in scope)

These feed the Primary track's digital sector (with the AI-durability lens):

- **Acquire.com** (https://acquire.com): set alerts by revenue range $100K-$5M, SaaS preferred
- **Flippa** (https://flippa.com): set alerts by SaaS and Apps, revenue $10K+ MRR
- **Empire Flippers** (https://empireflippers.com): join newsletter, their listings are curated
- **Quiet Light** (https://quietlightbrokerage.com): join newsletter, higher-end digital
- **Microns** (https://microns.io): join newsletter, small SaaS

---

### Step 4: Tell Claude when a few are live

You don't need all of the above running before we flip. Minimum viable state:

- `Acquisitions` label exists in Gmail
- Filter is routing mail to it
- BizBuySell saved searches set up (Primary + at least one Passive)
- One or two other marketplaces configured

Tell me when that state is reached. I'll:
1. Verify the label exists via the connector
2. Sample a few threads in it to confirm parsing works
3. Rewrite the `acquisitions-digest` scheduled task to read Gmail as the primary source and segment output into Primary vs Passive Holds
4. Update `sources.md` and `/scheduled-tasks.md` to reflect the new architecture

---

## Coverage Guarantee

Every thread in `label:Acquisitions` is processed on every digest run. Zero silent drops.

How it works:

1. Scheduled task queries `label:Acquisitions is:unread` via the Gmail connector and pulls every matching thread
2. Each thread's full content is read (subject + body, including multi-listing alert emails where one message contains several listings)
3. Every listing extracted from those threads is routed into one of four buckets in the digest:
   - Primary Strong Match
   - Passive Holds Strong Match
   - Borderline
   - Excluded (with reason)
4. Digest header reports: "N threads processed, M listings extracted" so total coverage is auditable
5. Processed threads are marked read so the next run only sees new email
6. Dedup is per-thread (Gmail thread ID) plus a running `seen.md` ledger, so a listing that re-circulates across marketplaces is flagged once

What this means in practice: if a broker sends an off-thesis listing (say, a restaurant) and it hits the label, it shows up in the digest's "Excluded This Run" count with reason "food business." You see it was seen, filtered, and killed. Nothing disappears.

Ad-hoc adds: if you manually apply the `Acquisitions` label to any email (say, a cold broker message, a forwarded tip, a newsletter that slipped past the filter), it gets processed the same way on the next run.

## Reminders

- Saved-search criteria on the marketplaces are intentionally set slightly wider than the thesis. Let the thesis do the final filtering in the digest, not the marketplace.
- If a marketplace's email volume overwhelms the label, tighten the saved search there first. Don't tighten the thesis.
- Add new marketplaces by dropping their sender domain into the Gmail filter and adding a saved search on their side. No code change needed.
- Sender domains occasionally change. If a new one shows up (e.g., a marketplace switches email providers), update the Gmail filter From-field.
- To manually feed a listing into the pipeline, apply the `Acquisitions` label to any email. It will be picked up on the next run.
