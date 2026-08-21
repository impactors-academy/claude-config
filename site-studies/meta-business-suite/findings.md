# Site Study: Meta Business Suite (Admin/SaaS Tool Audit)

**Tool:** business.facebook.com — Meta Business Suite + Ads Manager + Events Manager
**Date:** 2026-08-21
**Method:** Live walkthrough (logged into a real account) plus 56 screenshots captured by
the user across every major section, reviewed in full.

**No screenshots in this copy.** The captures were of a real, live Impactors Academy
account — real follower counts, real handles, one real DM conversation with a person's
bio and photo. This is the public `claude-config` mirror, so the images stay out of it
on purpose; only the pattern-level write-up below is shared here. The full study with
screenshots (`screenshots/image.png` through `image copy 55.png`, in capture order —
`image.png` is an unrelated LinkedIn screen) lives in the private `impactors-academy`
repo at `docs/site-studies/meta-business-suite/`, PR #20, for anyone with access who
wants the visual reference behind a specific finding below.

---

## Why this study uses a different structure than the other 12

Every other file in `docs/site-studies/` audits a marketing/landing site — hero, scroll
narrative, 3D, micro-interactions. Meta Business Suite is a different genre entirely: a
multi-tenant SaaS admin tool for managing several businesses' social presence from one
account. There is no hero, no scroll story, no 3D. The thing worth studying here is
**information architecture and workflow patterns** — exactly what the impactors-academy
mother dashboard needs as it grows past three platforms. Sections below replace
nav/hero/scroll/micro-interactions/typography/tech-fingerprint/mobile with the questions
that actually matter for an admin tool.

---

## 1. The Switcher — top-level context scoping

**Screenshots:** `image copy 2.png` (dropdown open), `image copy 3.png` (collapsed icon
rail)

A pill button (small avatar + name + chevron) sits above the sidebar. Clicking it opens a
**two-pane dropdown**:
- Left pane: every "business portfolio" the account belongs to (list of businesses, each
  showing an asset count — "10 business assets")
- Right pane: the individual Pages/assets *inside* whichever portfolio is selected on the
  left, each row showing an avatar with a small platform badge (FB/IG) overlaid
  bottom-right, the asset name + handle, a radio-style selector, and what looks like an
  unread-activity dot

Selecting an asset changes the browser URL's `page_id`/`asset_id` query params and
**re-renders the entire interface** around that selection — different cover photo,
different follower counts, different alert banners, different Inbox conversations. This
was confirmed live (not inferred from screenshots): switching from "Impactors Academy" to
"Loc" changed everything on the page in one navigation.

**What doesn't change:** the sidebar's tool *categories* (Home, Notifications, Content,
Inbox, Insights, Ads, …) stay structurally the same regardless of which asset is
selected — only the data behind each one changes. Meta's Pages are structurally
identical to each other (every Page gets the same tool set), which is why this works as
"same nav, different data" rather than "different nav per selection."

**Already built, this session:** `impactors-academy/src/components/admin/PlatformSwitcher.tsx`.
Deliberately *not* a copy of the two-pane portfolio/asset split — we have 3 flat options
(mother + 2 daughters), and our platforms genuinely have different entity types (Loc
manages Experiences/Properties/Products, IA Pro manages Projects), so our switcher
changes *which nav items show*, not just the data behind identical items. That's a
correct adaptation, not a shortcut — matching the two-pane picker here would be
over-engineering for 3 items and would misrepresent our actual architecture.

---

## 2. Sidebar shapes — icon rail vs. labeled, and where each shows up

**Screenshots:** `image copy 3.png` (icon-only, hover reveals label), `image copy 55.png`
(fully labeled, "Meta Business Suite" top-level)

Two sidebar treatments exist depending on which sub-app you're in:
- **Icon-only rail** (Ads Manager, Events Manager, most of Business Suite's own tool
  pages): narrow fixed-width column, icons only, a label tooltip/flyout on hover. Cheap
  on horizontal space, works because there are 10+ icons and no room for labels at that
  density.
- **Fully labeled** (Meta Business Suite's own top-level shell, `image copy 55.png`):
  wider sidebar, icon + text label per item, sections separated by thin rules, a "Create"
  item with a chevron that opens a flyout of quick actions (Ad / Post / Reel / Story / Go
  live / Post reel across pages / Bulk upload reels).

**For us:** our own sidebar (`AdminShell.tsx`) is already the labeled variant, and at 3-8
items per platform we're nowhere near the density that would justify an icon rail. Not
worth adopting — flagging only because it explains *why* Meta uses two different shapes,
so a future audit doesn't mistake it for inconsistency.

---

## 3. Nested flyout submenus on sidebar items

**Screenshot:** `image copy 10.png`

Ads Manager's sidebar icon for "Ads Manager" itself expands into a secondary flyout panel
listing its own sub-items (Account overview, Campaigns, Audiences, Billing & payments,
Ads Reporting, Ad account settings, Events Manager) — a nav item that is itself a small
nav. This is a two-level nesting pattern, distinct from our flat "select platform → flat
list of that platform's items" model.

**For us:** not needed yet. Our deepest platform (Loc) has 3 items (Experiences,
Properties, Products) — a flat list reads fine. Worth remembering as the pattern to reach
for *if* a single platform's item count grows past ~6-7 and starts needing its own
grouping (e.g., if Loc later gets Leads, Referrals, Blog management on the mother too).

---

## 4. The "All tools" mega-directory

**Screenshots:** `image copy 19.png`, `image copy 20.png`, `image copy 33.png`,
`image copy 34.png`

A full-screen (or large panel) directory of *every* tool across the whole product,
organized into named categories: Business products, Engage audience, Advertise, Manage,
Analyze and report, Sell products and services. A "Recently used" row of icons sits at
the top. A search box filters by keyword. This is the answer to "there are 40+ tools,
more than any sidebar can show" — it's the overflow valve, reached via a single "All
tools" / hamburger item that's always present regardless of which asset is selected.

**For us:** directly relevant once Phase B/C of the unified-admin plan keeps adding
platforms and entity types. Right now 3 platforms × a few items each is still
sidebar-sized. The trigger to build an "All tools" style directory isn't a fixed item
count — it's when a team member says "I don't remember where X lives." Not needed today;
worth keeping as the answer when that day comes, rather than trying to jam every future
entity into the sidebar indefinitely.

---

## 5. Notifications panel

**Screenshots:** `image copy 8.png`, `image copy 9.png`

A slide-in panel triggered from a sidebar bell icon (not top-right, which is where most
products put it). Tabs: All / Business / Ads / Profiles. An "Unread" toggle switch.
Filter/settings icons top-right of the panel itself. Empty state: a friendly bell
illustration + one line of explanatory copy, no dead silence.

**For us:** we don't have a notifications system today. If one gets built (e.g., "a new
inquiry came in on Loc," "n8n workflow failed"), this tabbed-panel-with-toggle shape is a
reasonable reference — but that's a real feature to scope separately, not something to
retrofit speculatively.

---

## 6. List/table view conventions (the pattern most relevant to our own CRUD pages)

**Screenshots:** `image copy 14.png` (Audiences), `image copy 12.png`/`13.png` (Ads
Reporting), `image copy 17.png` (Billing)

Every data table in this product follows the same shape:
- A row of **filter chips** above the table (e.g., "All audiences / Active ads / Action
  needed / Unlabeled audiences")
- A **search box** for name/ID
- A **bulk-action toolbar** that activates once at least one row is checked (Edit / Share
  / Delete), disabled/greyed when nothing's selected
- **Filter** and **Columns** dropdown buttons on the right, letting a user customize which
  fields show
- Rows can be **grouped/nested** with an expand chevron (Audiences groups by
  Customers/Engaged/Other/Unlabelled/Lookalikes/Saved)
- Genuinely empty states get a **custom illustration + one-line explanation + primary
  CTA**, never a bare "no results" — this repeats identically across Reports, Exports,
  Clips, Playlists, Series, Ads, Content: a small telescope/puzzle-piece illustration
  family reused everywhere, so it reads as one system rather than 15 different
  "nothing here" screens.

**For us — this is the one section with a direct, actionable comparison.** Our
`/admin/loc/experiences`, `/properties`, `/products`, and `/admin/ia-pro/projects` (built
this session) already have the empty-state-with-explanation pattern
(`daughter-crud.ts`'s `configured`/`error`/`data` contract renders "not connected" or
"couldn't reach it" with an explanation, never a silent blank). What we don't have yet,
and what would be the next honest step up if these lists grow past a handful of rows:
search/filter above the list, and a real Columns-style customization. At today's row
counts (single digits to low tens per entity) that would be premature — Meta's tables are
built for potentially thousands of rows. Worth revisiting once any one entity list is
large enough that scrolling to find a row is the actual complaint, not before.

---

## 7. Settings-as-status-cards

**Screenshots:** `image copy 15.png`, `image copy 16.png`, `image copy 52.png`

Rather than a traditional settings form, Advertising Settings and Monetization render
settings as a **grid of cards**, each showing: an icon, a title, one line of what it does,
and — critically — **the current value inline** ("No account controls set," "Test new
creative features: Off," "Datasets and pixels: 1," "No Monetization Violations"). You see
the state of every setting at a glance without opening any of them; clicking a card is
the only way to change it.

**For us:** this is a genuinely strong pattern worth adopting, and cheap to build. Our
current settings-adjacent surfaces (env-var-driven "not connected" states on
content-requests/automations) already show *whether something is configured* but not in
this card-grid-with-inline-value shape. If a real Settings page gets built for the mother
dashboard (Coolify env status, which daughters are connected, key rotation dates), this
card format — status visible without a click — is the one pattern from this whole study
worth deliberately copying, not just noting.

---

## 8. Gamified progress / weekly plan

**Screenshots:** `image copy 22.png`, `image copy 23.png`

Insights Overview leads with a "Weekly plan" card: a progress bar, "N of 7 tasks
completed," and a row of task cards (icon + task name + "0/1" counter + a direct-action
button like "Create ad"). Completed tasks get a green checkmark badge instead of a
button. This is deliberately motivational, not just informational — it's nudging
specific next actions, not reporting a static state.

**For us:** interesting but not a fit right now. This makes sense for Meta because the
audience is millions of small businesses who need onboarding nudges. Our dashboard's
audience is the founder and a small team who already know what needs doing — a gamified
checklist would read as noise, not help. Filing this as a deliberate skip, not an
oversight.

---

## 9. Locked/gated data states with an honest reason

**Screenshot:** `image copy 25.png`

Audience Demographics doesn't just hide data when there isn't enough of it — it explains
*why*: "You need 100 followers who are not also friends to see this demographic data. To
protect the privacy of people who follow your profile, you need to have at least 100
followers who are not also friends among the top 45 cities to see these insights." Same
treatment repeats for every locked metric on the page.

**For us:** this is the same spirit as our own `NotConnected`/`FetchError` components in
`src/lib/metrics.ts` and `daughter-crud.ts` — never a silent zero, always a stated reason.
Confirms we already have the right instinct here; nothing new to build, just a good
cross-check that we're consistent with it everywhere (worth an audit pass: does every
"empty" state across all admin pages explain why, or do any still just show "0"?).

---

## 10. Benchmarking / percentile comparison

**Screenshots:** `image copy 26.png`, `image copy 27.png`

A bar chart plotting "your business" against 25th/50th/75th percentile bars for similar
businesses, plus a colored status pill ("Lower than others" / "Similar to others") next
to each headline metric. A second tab lets you manually add specific competitor accounts
to track side by side in a table.

**For us:** not applicable — we have no peer/competitor data source, and inventing one
would be hallucination-adjacent (there's no real "businesses like Loc" dataset to compare
against). Skip entirely, not a gap.

---

## 11. Unified inbox with a lightweight CRM layer

**Screenshot:** `image copy 33.png` *(labeled in capture order as the Inbox screen — the
one with Messenger/Instagram/WhatsApp tabs and a right-side contact panel)*

All platforms' DMs and comments (Messenger, Instagram, WhatsApp, Facebook comments,
Instagram comments) unify into one inbox with per-channel unread counts as tab badges. A
right-side panel per conversation adds "Contact details," Instagram profile info, and two
small CRM fields: **Lead stage** ("Mark as lead") and **Order status** (a select
dropdown). This turns a plain messaging inbox into a lightweight sales-pipeline tool
without being a full CRM.

**For us:** genuinely relevant, but a real feature, not a styling note — this maps to
Emmanuel's still-open "Daughter enquiries on the mother" bullet (unified contacts/
enquiries/inquiries view, filterable by platform, per
`[workspace]/MASTER-CHECKLIST.md` Phase B). If that gets built, the "Lead stage" /
"Order status" side-panel fields are worth considering as a cheap, high-value addition —
turns a read-only contacts list into something that tracks follow-up state. Not scoped
for this session; flagging for whoever picks up that bullet.

---

## 12. Content calendar (Planner)

**Screenshot:** `image copy 38.png` *(week view, date navigation, Goals/Moments/Drafts
side tabs)*

A week/month calendar for scheduled content, with a right-side panel offering Goals /
Moments / Drafts as separate tabs, and a suggested-posting-time card ("your followers are
most active at this time").

**For us:** relevant to the content-automation pipeline (`docs/CONTENT-AUTOMATION.md`,
n8n workflows) once posts are actually scheduling through it — right now nothing posts
automatically yet (per this session's earlier status check: Postiz has no platform
credentials wired, n8n has no activated workflows). A calendar view of what's queued
would be a natural companion to `/admin/content-requests` once WF-07 is actually live.
Premature to build against a pipeline that can't post yet.

---

## Recommendation for Impactors Academy

Given our actual situation — 3 platforms today, small team, admin tool not a
multi-tenant SaaS product — most of Meta Business Suite's complexity exists to serve a
scale we don't have and shouldn't build for speculatively. The concrete take:

**Already correctly adapted, not copied (this session, before this study even ran):**
- Platform switcher — 3-item flat list instead of the two-pane portfolio/asset picker
- "Not connected"/error states with a stated reason — matches Section 9 exactly
- Daughter entity CRUD pages already follow the empty-state-with-illustration-and-CTA
  shape (Section 6), just without search/filter/columns, which is correct at our row
  counts

**Worth adopting deliberately, next time a Settings surface gets built:**
- Card-grid settings with the current value shown inline (Section 7) — cheapest, highest
  signal-to-effort pattern in this whole study

**Worth remembering as the answer to a future, specific problem — not building now:**
- Nested flyout submenus (Section 3) — only if one platform's item count grows past ~6-7
- "All tools" mega-directory (Section 4) — only once someone can't find something in the
  sidebar
- Lead stage / Order status fields in a unified contacts view (Section 11) — tied to
  Emmanuel's still-open "daughter enquiries on the mother" bullet, a real feature to scope
  when picked up, not a styling addition
- Content calendar view (Section 12) — tied to the content-automation pipeline actually
  going live, which it isn't yet

**Deliberately not adopting:**
- Gamified weekly-plan checklist (Section 8) — wrong audience fit, we're not onboarding
  millions of small businesses
- Benchmarking against peer businesses (Section 10) — no real data source, would require
  fabricating comparison data
