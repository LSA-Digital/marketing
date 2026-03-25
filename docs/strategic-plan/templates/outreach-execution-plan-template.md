# [Product] Outreach Execution Plan Template

**Last Updated:** 2026-03-12

Use this template to turn a state-prioritized strategic plan and tactical playbook into an operational runbook. This document should be execution-grade: who is researched first, which channels move first, what happens each week, and which JSON fields the runtime system depends on.

## Purpose

This document is the operational runbook for `[Product]` outbound outreach.

It should define:

- which states move first
- which accounts must be researched within each state
- which route gets used in what order
- what the team does each day and week
- which JSON artifacts power the execution system

## Core Operating Rule

- Treat `state` as the top-level account.
- Default public-sector route hierarchy: `website contact form or official inbox first -> LinkedIn second -> verified email third -> calling fourth`.
- A state does not move to active outreach until its message lane, account types, and official routes are documented.
- Keep the linked JSON dataset and tactical playbook in sync when this execution plan changes materially.

## Linked Files

- Strategic plan: `docs/strategic-plan/[product]/[plan-file].md`
- Briefing: `docs/strategic-plan/[product]/[briefing-file].md`
- State prioritization: `docs/strategic-plan/[product]/[state-ranking-file].md`
- Tactical playbook: `docs/strategic-plan/[product]/[playbook-file].md`
- Runtime JSON: `[runtime path].json`
- Mirrored product JSON: `docs/strategic-plan/[product]/[json-file].json`

## State Launch Model

| Tier | Coverage | Treatment |
| --- | --- | --- |
| `Tier A` | highest-priority states | deep research, named contacts, tailored sequences, live follow-up |
| `Tier B` | fast followers | research light, official-route first touch, promote on signal |
| `Tier C` | broad-launch coverage | minimum viable but credible coverage, nurture until trigger event |

## Required Data Per State Account

| Field | Why it matters |
| --- | --- |
| `state_name` | canonical parent account |
| `tier` | determines research depth and cadence |
| `priority_rank` | creates a stable queue |
| `message_lane` | controls copy and hooks |
| `organization` | child account identity |
| `buyer_type` | clarifies agency, university, hospital, or partner role |
| `official_contact_form_url` | preferred first route for public-sector outreach |
| `official_public_inbox` | first-touch or fallback route |
| `named_contacts` | enables LinkedIn and direct email |
| `verified_email` | controlled fallback only |
| `public_phone` | routing and follow-up |
| `status` | avoids duplicate touches |
| `next_allowed_action` | enforces route order |
| `owner` | ensures accountability |

## Status Model

Use only these statuses in the tracker.

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
| Official contact form or public inbox exists and no warm named route is known | official route first |
| Named person exists and state is Tier A with strong role fit | LinkedIn may run in parallel after official route |
| Verified public email exists for a clearly relevant named person | email after official route and LinkedIn, unless relationship is warm |
| No digital response and account remains strategically important | calling for routing or follow-up |
| No usable route exists | pause and enrich research before touching the account |

## State-First Workflow

1. Confirm the state's tier, message lane, and documented priority.
2. Identify the first account type to research inside the state.
3. Verify the official contact route and any named functional-role leaders.
4. Send the approved official-route message.
5. Use LinkedIn for named contacts aligned to the same message lane.
6. Use verified direct email only when justified by role and timing.
7. Use calling for routing, office confirmation, and nonresponse recovery.
8. Update status, next action, and notes the same day.

## Top States Table

| Rank | State | Tier | Message lane | Primary account type | Route order | Owner | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [State] | [Tier A] | [S1] | [State agency] | [form -> LinkedIn -> email -> call] | [Owner] | [Research or first touch] |

## Daily Rhythm

1. Select `2-4` states and `3-5` child accounts for the day.
2. Verify route quality before sending anything.
3. Send official-route notes first.
4. Queue LinkedIn, email, or call follow-ups only when the plan allows.
5. Update JSON, tracker, and notes before the day ends.

## Weekly Cadence

### Week 1

- finalize Tier A research packets
- verify official forms, public inboxes, and named contact roles
- launch official-route first touches for the first priority states

### Week 2

- continue Tier A and first Tier B launch coverage
- add LinkedIn touches for named leaders in states already contacted through official routes
- begin routing calls where forms or inboxes do not produce movement

### Week 3

- use verified email for high-priority nonresponders where appropriate
- update state tiering based on new signal
- prepare short state-specific briefing offers for positive or neutral replies

### Week 4

- escalate positive accounts to human discovery
- pause low-signal states that still lack clear routes
- refresh the top-state queue for the next 30-day cycle

## Artifact Handoff

The runtime execution system should consume a JSON dataset organized as:

`state -> campaign -> accounts -> contact_persons -> outreach_content -> calling`

The runtime system should not decide strategy. It should only execute approved steps, record outcomes, and update status.

## Verification Checklist

- [ ] Tier A, Tier B, and Tier C states are current
- [ ] Every active state has a documented message lane
- [ ] Official-route links and public inboxes are verified before use
- [ ] Tactical playbook and execution plan agree on route order
- [ ] JSON dataset contains state-level and account-level fields needed for routing
