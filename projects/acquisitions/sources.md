# Sources

Marketplaces, brokers, and channels monitored for listings matching the thesis. Add new sources here as they prove valuable.

---

## Tier 1: Primary Marketplaces (check most frequently)

**BizBuySell** (https://www.bizbuysell.com)
- Largest US SMB marketplace. Highest listing volume in Matt's geography.
- Regional search pages:
  - https://www.bizbuysell.com/new-jersey/businesses-for-sale/
  - https://www.bizbuysell.com/new-york/businesses-for-sale/
  - https://www.bizbuysell.com/pennsylvania/businesses-for-sale/
- Offers saved-search email alerts

**BizQuest** (https://www.bizquest.com)
- Secondary US SMB marketplace. Significant overlap with BizBuySell but not 100%.
- Email alerts available

**DealStream** (https://dealstream.com)
- ~~Excluded 2026-04-19: requires paid subscription to contact brokers. Do not query.~~

**LoopNet** (https://www.loopnet.com/businesses-for-sale/)
- CRE-focused but surfaces businesses with attached real estate

---

## Tier 2: Regional and Niche

**Synergy Business Brokers** (https://synergybb.com)
- NJ/NY regional broker

**Sunbelt Business Advisors** (https://www.sunbeltnetwork.com)
- National broker network with NJ/NY presence

**Transworld Business Advisors**
- National broker network, tri-state offices

**Murphy Business & Financial**
- National SMB broker

---

## Tier 3: Digital (activate if thesis expands)

- **Acquire.com** (SaaS and digital)
- **Flippa** (digital, content sites, ecommerce)
- **Empire Flippers** (curated digital)
- **Quiet Light Brokerage** (higher-end digital)
- **Microns** (tiny SaaS)

---

## Direct Broker Relationships

Cultivate over time. Log new broker contacts here as they emerge.

- **Adam Stein / Mikael Vollbach** (The Kensington Company), 516-715-1408. Source for the driving-school-acquisition deal.
- **Zanol** at Central Jersey Driving School listing (broker, name to confirm)

---

## Search Query Patterns

Seeds for the discovery scheduled task. Combine with exclusion terms.

**Geography seeds:**
- `businesses for sale near Montclair NJ`
- `businesses for sale Essex County NJ`
- `businesses for sale Bergen County NJ`
- `businesses for sale Morris County NJ`
- `businesses for sale Hudson County NJ`
- `businesses for sale Passaic County NJ`
- `businesses for sale Union County NJ`
- `businesses for sale Rockland County NY`
- `businesses for sale Westchester NY`
- `businesses for sale lower Fairfield County CT`

**Financial seeds:**
- `SDE $250K $1M NJ NY business for sale`
- `cash flow $500,000 business for sale tri state`
- `retiring owner business for sale New Jersey`

**Sector seeds (open, adjust as thesis sharpens):**
- `service business for sale NJ`
- `B2B services for sale New Jersey`
- `education business for sale NJ`
- `distribution business for sale NJ`
- `home services business for sale NJ`

**Exclusion terms (apply to every query):**
- Food: restaurant, food service, bakery, cafe, pizzeria, diner, catering, bar, pub, deli
- Other: bread route, laundromat, wash and fold, coin laundry

---

## Email Alert Setup

Primary source for the scheduled discovery task once Matt completes setup. See `email-setup.md` for the step-by-step configuration guide.

Flow once active:

1. Saved searches on each marketplace send alert emails to Matt's Gmail
2. Gmail filter routes those emails to the `Acquisitions` label
3. Scheduled task reads every unread thread in that label (100% coverage, no silent drops), extracts listings, applies thesis filters, writes digest
4. Every processed listing is accounted for in the digest: Strong Match, Borderline, or Excluded (with reason). Digest header reports N threads processed and M listings extracted
5. Processed threads marked as read; persistent dedup via `seen.md`
6. Ad-hoc entry: Matt can manually apply the `Acquisitions` label to any email to force-include it in the next run

WebSearch remains active as a secondary source to catch gaps (broker-only listings, marketplaces without email alerts, brand-new sources not yet in filters).

**Status as of 2026-04-21:** Gmail connector authorized (read-only). Label and filters pending Matt's one-time setup.
