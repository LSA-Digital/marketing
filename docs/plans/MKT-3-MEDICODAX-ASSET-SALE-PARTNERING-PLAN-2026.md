# MKT-3: MEDICODAX Asset Sale and Partnering Plan 2026

**Last Updated:** 2026-03-11
**Jira Ticket:** [MKT-3](https://lsadigital.atlassian.net/browse/MKT-3)
**Type:** Story
**Status:** Completed


---

## Overview

Retroactively track the 2026 MEDICODAX asset-sale / partnering planning work that produced the strategy, channel, outreach, and execution documents under `docs/strategic-plan/medicodax/`.

This work framed MEDICODAX as a strategic Human-AI medical coding and workflow solution, defined the buyer/channel model, prioritized relationship-rich routes over traditional brokers, and built the tactical outreach system needed to support LinkedIn-first, website-contact-form-second, email-last execution.

---

## Scope

### In Scope

- Define MEDICODAX 2026 strategic sale / partnering positioning
- Reframe MEDICODAX around strategic transaction plus post-close implementation support by LSA Digital
- Build the wholesale marketing and sales plan for MEDICODAX
- Build the MEDICODAX strategy briefing
- Build the MEDICODAX channel and advisor guide
- Build the MEDICODAX tactical contact playbook
- Build the MEDICODAX 30-day outreach execution plan
- Create all marketing/sales strategic, tactical, and execution-level plan artifacts needed for repeatable MEDICODAX deployment
- Make outpatient and home-health lanes explicit in planning and outreach materials
- Prioritize LinkedIn-first outreach with contact-form fallback and email as last priority
- Capture named individuals, public routes, and outreach copy for target organizations
- Include execution-level target content such as prioritized targets, channels, and JSON-based message content for organization contact forms plus individual LinkedIn/email outreach
- Create reusable templates for JSON, tactical playbook, and execution plan in `docs/strategic-plan/templates/`
- Create test JSON for marketing deployment tool testing
- Upload MEDICODAX strategic docs to EPMS and keep the outreach execution plan synced
- Mirror per-product EPMS content into `docs/strategic-plan/` and keep EPMS in sync when docs change
- Store MEDICODAX JSON artifacts in EPMS alongside the markdown planning artifacts

### Out of Scope

- Production application changes to MEDICODAX itself
- Automated CRM integration
- Fully automated outbound execution beyond planning and data preparation
- Legal transaction structuring beyond planning guidance
- Final buyer diligence package or signed transaction documents

---

## Deliverables

- `docs/strategic-plan/medicodax/medicodax-wholesale-marketing-and-sales-plan.md`
- `docs/strategic-plan/medicodax/medicodax-wholesale-marketing-and-sales-briefing.md`
- `docs/strategic-plan/medicodax/medicodax-wholesale-brokers.md`
- `docs/strategic-plan/medicodax/medicodax-tactical-contact-playbook.md`
- `docs/strategic-plan/medicodax/medicodax-30-day-outreach-execution-plan.md`
- `docs/strategic-plan/medicodax/medicodax-all-contacts.json`
- `docs/strategic-plan/medicodax/medicodax-test-contacts.json`
- `outreach/examples/medicodax-all-contacts.json`
- `outreach/examples/medicodax-test-contacts.json`
- EPMS research entries for the MEDICODAX planning documents under product `24898511-0fd9-4681-80ed-de545189e987`
- `docs/strategic-plan/templates/`

---

## Acceptance Criteria

- [x] Jira issue exists for the MEDICODAX 2026 asset-sale / partnering planning work
- [x] Local plan file exists in `docs/plans/` and references the Jira key
- [x] MEDICODAX strategy docs exist under `docs/strategic-plan/medicodax/`
- [x] Channel guidance reflects relationship-rich channels first and traditional brokers downgraded
- [x] Outreach guidance explicitly covers both outpatient and home-health lanes
- [x] Execution guidance prioritizes LinkedIn first, website contact forms second, and email last
- [x] EPMS contains the MEDICODAX strategic planning research artifacts
- [x] Create all marketing/sales strategic, tactical, and execution-level plans, with execution-level content including prioritized targets, channels, and JSON message content for organization contact forms plus individual LinkedIn/email outreach
- [x] Create templates for JSON, tactical playbook, and execution plan under `docs/strategic-plan/templates/`
- [x] Create test JSON for marketing deployment tool testing
- [x] Treat EPMS MCP as the source of truth for product content, mirror per-product EPMS content in `docs/strategic-plan/`, keep EPMS synced when docs change, and store the related MEDICODAX JSON in EPMS

---

## Implementation Todo List

- [x] Build MEDICODAX wholesale marketing and sales plan
- [x] Build MEDICODAX strategy briefing
- [x] Build MEDICODAX channel and advisor guide
- [x] Build MEDICODAX tactical contact playbook with named contacts and routes
- [x] Build MEDICODAX 30-day outreach execution plan
- [x] Rewrite execution plan around LinkedIn-first and contact-form-agent handoff
- [x] Extend execution-level JSON so it includes organization-form content and individual LinkedIn/email outreach content in the acceptance-criteria shape
- [x] Create reusable templates in `docs/strategic-plan/templates/` for JSON, tactical playbook, and execution plan
- [x] Create test JSON for marketing deployment tool testing
- [x] Sync planning docs to EPMS
- [x] Sync the MEDICODAX JSON artifacts to EPMS and formalize EPMS/docs mirroring rules for this product
- [x] Retroactively create Jira ticket and local plan file for traceability

---

## Key Decisions Captured

- MEDICODAX should be positioned as a strategic Human-AI medical coding and workflow solution, not a generic SaaS blast
- The transaction framing is best treated as a strategic transaction with post-close implementation support by LSA Digital
- Traditional brokers should be downgraded relative to relationship-rich coding, training, home-health, outpatient, and advisor channels
- Both outpatient and home-health are viable lanes and must remain explicit in the strategy
- LinkedIn should be the primary first-touch route, with website contact forms as the operational fallback and email last

---

## Evidence / Related Files

- `docs/strategic-plan/medicodax/medicodax-wholesale-marketing-and-sales-plan.md`
- `docs/strategic-plan/medicodax/medicodax-wholesale-marketing-and-sales-briefing.md`
- `docs/strategic-plan/medicodax/medicodax-wholesale-brokers.md`
- `docs/strategic-plan/medicodax/medicodax-tactical-contact-playbook.md`
- `docs/strategic-plan/medicodax/medicodax-30-day-outreach-execution-plan.md`
- `docs/strategic-plan/medicodax/medicodax-all-contacts.json`
- `docs/strategic-plan/medicodax/medicodax-test-contacts.json`
- `outreach/examples/medicodax-all-contacts.json`
- `outreach/examples/medicodax-test-contacts.json`
- `docs/plans/MKT-2-AI-CONTACT-FORM-OUTREACH.md`
- `docs/strategic-plan/templates/strategic-outreach-json-template.json`
- `docs/strategic-plan/templates/tactical-contact-playbook-template.md`
- `docs/strategic-plan/templates/outreach-execution-plan-template.md`

---

## Test Matrix

| Test | Type | Evidence | Status |
|------|------|----------|--------|
| `test_docs_exist` | Manual verification | MEDICODAX strategy docs present under `docs/strategic-plan/medicodax/` | 🟢 |
| `test_epms_sync` | Manual verification | MEDICODAX research artifacts visible in EPMS product research list | 🟢 |
| `test_execution_plan_priority_model` | Manual verification | Execution plan reflects LinkedIn-first, form-second, email-last | 🟢 |
| `test_medicodax_test_json_exists` | Manual verification | `outreach/examples/medicodax-test-contacts.json` exists for deployment-tool testing | 🟢 |
| `test_strategy_templates_exist` | Manual verification | `docs/strategic-plan/templates/` contains JSON, tactical-playbook, and execution-plan templates | 🟢 |
| `test_epms_json_sync` | Manual verification | MEDICODAX JSON artifacts stored in EPMS and mirrored rules documented | 🟢 |
| `test_local_plan_created` | Manual verification | `docs/plans/MKT-3-MEDICODAX-ASSET-SALE-PARTNERING-PLAN-2026.md` created and linked to Jira | 🟢 |
| `test_jira_ticket_created` | Manual verification | `MKT-3` exists in Jira with the expected summary and description | 🟢 |

---

## Status Updates

| Date | Phase | Update |
|------|-------|--------|
| 2026-03-11 | Planning | MEDICODAX strategy, channel, contact, and outreach execution docs produced in the repo. |
| 2026-03-11 | EPMS Sync | MEDICODAX planning artifacts uploaded to EPMS and execution plan later re-synced after LinkedIn-first rewrite. |
| 2026-03-11 | Traceability | Retroactive Jira story `MKT-3` created and paired local plan file added under `docs/plans/`. |
| 2026-03-11 | Scope Expansion | Acceptance criteria expanded to cover strategic-plan templates, execution-level JSON content, deployment-test JSON, and EPMS/docs source-of-truth sync expectations. |
| 2026-03-12 | Completion | Strategic-plan templates created, legacy templates moved under `docs/strategic-plan/templates/`, MEDICODAX JSON mirrors created under `docs/strategic-plan/medicodax/`, individual LinkedIn/email outreach content added to the JSON datasets, and both JSON mirrors saved into EPMS. |
| 2026-03-12 | Completed | All A/C verified, tests passing, Jira closed |

