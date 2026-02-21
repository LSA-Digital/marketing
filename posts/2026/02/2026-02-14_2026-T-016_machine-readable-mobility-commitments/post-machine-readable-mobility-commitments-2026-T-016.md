# Machine-Readable Mobility Commitments Beat PDFs

## Metadata
- **Post ID**: 2026-T-016
- **Audience**: tech
- **Product**: LSARS
- **Themes**: COMMUNITY_TRANSPARENCY, DASHBOARD_ACCOUNTABILITY, SMART_MOBILITY, TRANSPORTATION
- **Expert**: Mike, Keith
- **Depends On**: 2026-B-035
- **Dependency Name**: Your Work Zone Plan Isn't Real Until It's a Feed
- **Relationship**: Shows how standard feeds + versioned rule schemas produce auditable mobility commitment compliance
- **Assets**: —
- **CTA**: see artifacts

## Post
Most "mobility commitments" are written as prose. Prose can't be validated, diffed, or monitored.

We built a standards-backed approach for turning mobility commitments into machine-readable rules and auditable compliance signals.

**How it works:**
- **Rule schema layer**: express commitments as versioned policy objects (where, when, who, exemptions, evidence requirements).
- **Event ingestion layer**: ingest authoritative feeds (work zones, closures) and operational signals (parking/enforcement/curb events).
- **Evaluation + audit layer**: compute compliance KPIs with provenance and keep an exception-first log reviewers can inspect.

The critical design choice: **unknown is not compliant**. Missing data produces "cannot verify" states that trigger escalation instead of silent pass-through.

**Result:** you get compliance proof you can defend, not dashboards you have to explain away.

See the artifacts: https://lsadigital.com

## Artifacts
- Remote:
  - https://lsadigital.com

## Post asset ideas
- [ ] Diagram: policy objects -> event streams -> compliance evaluation -> public scorecard
- [ ] One-pager: mobility rule schema (fields, versioning, provenance)
- [ ] Screenshot: exception log with evidence links and closure state

## Citations / Sources
- https://github.com/usdot-jpo-ode/wzdx (Work Zone Data Exchange specification)
- https://ops.fhwa.dot.gov/wz/wzdx/index.htm (FHWA WZDx program overview)
- https://www.openmobilityfoundation.org/announcing-curb-data-specification-version-1-0/ (Curb Data Specification; structured curb policy data)
- https://rosap.ntl.bts.gov/view/dot/58181/dot_58181_DS1.pdf (FHWA Curbside Inventory Report; inventories as inputs to curb rules)
