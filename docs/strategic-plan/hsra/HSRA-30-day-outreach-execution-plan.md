# HSRA 30-Day Outreach Execution Plan

**Last Updated:** 2026-03-12

## Purpose

This document is the 30-day operational runbook for HSRA outreach. It turns the HSRA strategic ranking and tactical playbook into a disciplined state-by-state execution sequence.

Use this with:

- `docs/strategic-plan/hsra/HSRA-marketing-and-sales-plan.md`
- `docs/strategic-plan/hsra/HSRA-marketing-and-sales-briefing.md`
- `docs/strategic-plan/hsra/HSRA-state-prioritization-ranking-2026.md`
- `docs/strategic-plan/hsra/HSRA-tier-1-state-account-scorecard.md`
- `docs/strategic-plan/hsra/HSRA-tactical-contact-playbook.md`

## Core Operating Rule

HSRA is a 50-state campaign. The working unit is not a generic target row. The working unit is:

`state -> account -> contact -> route -> next action`

Default channel order for this campaign:

1. `website contact form or official public inbox first`
2. `LinkedIn second`
3. `verified direct email third`
4. `calling fourth`

That order reflects the reality of state and public-health outreach: official routes often produce better routing than cold commercial outreach, while LinkedIn and direct email work best after the team has identified the right state function and message lane.

## Linked Assets

- Strategic plan: `docs/strategic-plan/hsra/HSRA-marketing-and-sales-plan.md`
- Briefing: `docs/strategic-plan/hsra/HSRA-marketing-and-sales-briefing.md`
- State prioritization: `docs/strategic-plan/hsra/HSRA-state-prioritization-ranking-2026.md`
- Active-pursuit scorecard: `docs/strategic-plan/hsra/HSRA-tier-1-state-account-scorecard.md`
- Tactical playbook: `docs/strategic-plan/hsra/HSRA-tactical-contact-playbook.md`
- Runtime JSON template: `docs/strategic-plan/templates/strategic-outreach-json-template.json`
- Tier A live dataset: `docs/strategic-plan/hsra/hsra-tier-a-state-packets.json`

## State Launch Model

| Tier | Coverage | Execution treatment |
| --- | --- | --- |
| `Tier A` | top-priority active pursuit states | deep research, official-route launch, named-contact buildout, live follow-up |
| `Tier B` | fast followers | moderate research, launch coverage, promote when signal improves |
| `Tier C` | broad-launch states | minimal credible launch coverage, monitor for trigger events |

## Tier A States For First 30 Days

| Rank | State | Tier | Message lane | First account types | Owner |
| --- | --- | --- | --- | --- | --- |
| 1 | Tennessee | A | S1, S5 | state health department, Tennessee Tech collaborators | Thad |
| 2 | Texas | A | S1 | state health department, rural transformation stakeholders | Thad + Mike |
| 3 | Mississippi | A | S1, S4 | state health department, rural health, health-gap, and planning stakeholders | Thad + intern |
| 4 | Alabama | A | S1, S2 | state health department, rural health, and planning stakeholders | Thad + intern |
| 5 | Georgia | A | S4, S1 | state health department, cancer-control, and rural-health stakeholders | Thad + Mike |
| 6 | Arkansas | A | S1, S2 | state health department, rural health, and PHAB-adjacent stakeholders | Thad + intern |
| 7 | Kentucky | A | S1, S2, S4 | rural, equity, and planning stakeholders | Thad + intern |
| 8 | West Virginia | A | S1, S4 | state health department, rural health, and disparity stakeholders | Thad + intern |
| 9 | Kansas | A | S1, S2 | state health department, rural health, and planning stakeholders | Thad + intern |
| 10 | North Carolina | A | S2, S6 | planning, local health, hospital planning | Thad + intern |
| 11 | New York | A | S2, S4 | prevention, reporting, and cancer-control stakeholders | Thad + Mike |

## Required Data Per Active State Account

Do not launch outreach on an account until the following is documented.

| Field | Why it matters |
| --- | --- |
| `state_name` | top-level parent account |
| `tier` | controls cadence and effort |
| `message_lane` | keeps copy focused |
| `organization` | identifies the child account |
| `buyer_type` | clarifies the use case |
| `documented_priority` | ties outreach to a real state problem |
| `official_contact_form_url` or `official_public_inbox` | preferred first route |
| `named_contact` | enables LinkedIn and direct email |
| `functional_role` | clarifies why the contact matters |
| `verified_email` | controlled fallback |
| `public_phone` | routing and nonresponse recovery |
| `status` | prevents duplicate touches |
| `next_allowed_action` | enforces route order |
| `owner` | keeps the work assigned |

## Status Model

Use only these statuses in the runtime tracker.

- `research`
- `ready`
- `sent-official-route`
- `sent-linkedin`
- `sent-email`
- `called`
- `replied-positive`
- `replied-neutral`
- `replied-negative`
- `needs-human`
- `paused`
- `closed`

## Route Priority Rules

| Situation | Route to use |
| --- | --- |
| Official form or public inbox exists and no better named route is known | official route first |
| Tier A state with a clearly relevant named leader | LinkedIn second after official route, or same-day if strategic value is high |
| Verified public email exists for a named leader | email after official route and LinkedIn unless the relationship is already warm |
| Account remains strategically important after no digital response | calling for routing and confirmation |
| Research is incomplete or route quality is low | pause and enrich the state packet |

## 30-Day Cadence

### Week 1 - Highest-urgency Tier A research and official-route launch

**Goal:** build credible packets for the highest-urgency Tier A states and launch the first official-route touches.

- finalize state packets for the first `5` Tier A states: Tennessee, Texas, Mississippi, Alabama, and Georgia
- verify official routing pages, public inboxes, and first named roles
- send approved official-route notes for those `5` states
- prepare LinkedIn follow-ups for named contacts where role fit is high

### Week 2 - Finish Tier A launch and begin bridge-state coverage

**Goal:** complete first-wave Tier A coverage and open first-touch coverage for the strongest bridge states.

- complete official-route launch for the remaining Tier A states in the top `11`
- send LinkedIn notes for named contacts in states already touched through official routes
- begin research and official-route outreach for `3-5` bridge Tier B states such as Pennsylvania, Colorado, Massachusetts, California, or Washington when partner paths or in-person meeting opportunities improve access quality
- use coordinator follow-up where official routing produced partial direction but no owner yet

### Week 3 - Add verified email and calling where justified

**Goal:** turn silence into routing progress instead of generic extra touches.

- use verified direct email for high-priority nonresponders when the role and address are clearly public and relevant
- call offices for routing help where forms or public inboxes have not moved
- refresh state rankings if new public signals or campaign responses emerge
- prepare short state-specific briefing offers for positive or neutral replies

### Week 4 - Escalation and next-cycle queue shaping

**Goal:** move real opportunities into human follow-up and cleanly reprioritize the next wave.

- escalate positive replies to Thad and Mike the same day
- convert promising states into discovery, briefing, or pilot-shaping conversations
- pause low-signal states that still lack a credible route after research and follow-up
- refresh the top-state queue for the next 30-day cycle based on signal quality

## Daily Rhythm

1. Select `2-4` states for the day.
2. Confirm that each account is `ready` and tied to one message lane.
3. Execute the next allowed route in order.
4. Log the result in the state dataset the same day.
5. Escalate all positive replies, redirects, and ambiguous responses to a human owner immediately.

## Weekly Operating Rhythm

| Cadence | Participants | Output |
| --- | --- | --- |
| Monday pipeline standup | Thad, intern, marketing manager, Mike | updated state queue and owner assignments |
| Wednesday content review | marketing manager + Thad | state-specific asset and webinar queue |
| Friday revenue review | Mike + Thad + intern | escalation list and next-step plans |
| Monthly strategy review | all core owners | tier adjustments and next 30-day priorities |

## What The Runtime System Needs

The runtime system or AI assistant should receive structured records only. It should not decide the state strategy on its own.

For the current Tier A wave, use `docs/strategic-plan/hsra/hsra-tier-a-state-packets.json` as the active dataset.

### Required handoff fields

| Field | Description |
| --- | --- |
| `state_name` | top-level campaign state |
| `tier` | Tier A, B, or C |
| `message_lane` | S1-S7 |
| `organization` | child account name |
| `buyer_type` | state agency, university, hospital, collaborator, etc. |
| `official_contact_form_url` | exact form to open if present |
| `official_public_inbox` | public inbox if no form exists |
| `named_contact` | person already identified for LinkedIn or email |
| `approved_subject` | approved subject line |
| `approved_message_body` | approved message body |
| `submitter_name` | sender name |
| `submitter_email` | sender email |
| `public_phone` | phone used for routing or follow-up |
| `next_allowed_action` | official route, LinkedIn, email, or calling |
| `source_confidence` | high, medium, low |
| `notes` | routing notes, state sensitivities, or follow-up instructions |

### The runtime system should do

- open the approved official route or queue the approved follow-up step
- populate approved fields only
- record success, failure, redirect, or manual-block state
- capture timestamp, route used, and resulting status

### The runtime system should not do

- decide which states to prioritize
- rewrite the state message lane
- improvise new copy beyond approved variants
- skip official-route-first logic unless a human owner changes the state plan

## Success Criteria For 30 Days

- `11` Tier A states have complete state packets
- `11` Tier A states receive official-route first touches
- `20-30` child accounts across Tier A states are researched to named-role quality
- `10-15` LinkedIn follow-ups are completed for named leaders
- `8-12` coordinator or routing follow-ups occur
- `3-5` live conversations, redirects, or clearly qualified next steps emerge

## Practical Rules

- do not treat official forms as mass-blast substitutes for weak research
- do not jump to direct email because an address exists
- do not call before the team knows what functional role it is trying to reach
- do not stack official route, LinkedIn, email, and calling on the same day for the same account without a clear reason
- do not move a state into active pursuit without a documented message lane and official route

## Sources

- `docs/strategic-plan/hsra/HSRA-marketing-and-sales-plan.md`
- `docs/strategic-plan/hsra/HSRA-marketing-and-sales-briefing.md`
- `docs/strategic-plan/hsra/HSRA-state-prioritization-ranking-2026.md`
- `docs/strategic-plan/hsra/HSRA-tier-1-state-account-scorecard.md`
- `docs/strategic-plan/hsra/HSRA-tactical-contact-playbook.md`
- `docs/strategic-plan/hsra/hsra-tier-a-state-packets.json`
- `docs/strategic-plan/hsra/HSRA-outreach-email-set.md`
