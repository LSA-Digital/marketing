# Squawk Content Index

**Organization:** `cmksfis0z0000b6s4vq6p5gbg` | **Last synced:** 2026-02-20 | **Source:** Squawk MCP (`list_review_queue` + `get_content_item` + `list_messaging_themes`) | **Rendering rules:** `docs/squawk-migration-process.md`

> **This file is a derived artifact.** It is reconstructed FROM SCRATCH every time data is pulled from Squawk MCP. Never edit by hand.

---

## Summary

| Metric | Count |
|--------|-------|
| Migrated (test batch) | 4 |
| Remaining | 78 |
| Approved | 1 |
| Pending review | 3 |
| Delayed | 2 |

---

## Documents

| Post ID | CUID | Title | Review Status | Doc Status | Readiness | Readiness Notes | Critical | Posts | Published | Audience | Product | Expert | Depends On | Dep. Name | Relationship | Repost By | Themes | Updated |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-B-001 | cmla2aisk002kqk3jypq1n0wl | [Trust Through Auditable AI: Why "Show Your Work" Beats "Trust Me"](posts/2026/02/2026-02-04_2026-B-001_auditable-ai-trust/post-auditable-ai-trust-2026-B-001.md) | APPROVED | INGESTED | needs_work | Lacks visual assets for polished publication | 0 | 1 | 0 | business | LSARS, HSRA | Nelson, Thad, Mike | — | — | — | — | AGENT_GUARDRAILS, COMMUNITY_TRANSPARENCY | 2026-02-20 |
| 2026-T-013 | cmla4d1rh003qqk3jm8iknja6 | [Graph neural networks for community "network effects"](posts/2026/02/2026-02-04_2026-T-013_graph-neural-network-effects/post-graph-neural-network-effects-2026-T-013.md) | PENDING_REVIEW | INGESTED | needs_work | DELAYED: No direct relationship, but leave this article as future placeholder after LSARS-532 Permit Location Optimizer has made some progress. | 0 | 3 | 0 | tech | LSARS, HSRA | Mike, Keith | — | — | — | Mike, Keith | LOCATION_INTELLIGENCE, RISK_INVESTMENTS, SMART_MOBILITY | 2026-02-20 |
| 2026-B-016 | cmlvbruo0000004lbdu6ci88e | [How does LSARS make water use and drought triggers transparent (potable vs reclaimed)?](posts/2026/02/2026-02-10_2026-B-016_data-center-water-transparency/post-data-center-water-transparency-2026-B-016.md) | PENDING_REVIEW | INGESTED | needs_work | DELAYED: We have not yet developed a water use dashboard. | 1 | 1 | 0 | business | LSARS | Nelson, Julian, Mike | — | — | — | Nelson, Julian, Mike | COMMUNITY_TRANSPARENCY, DASHBOARD_ACCOUNTABILITY, DATA_CENTER | 2026-02-20 |
| 2026-T-018 | cmlvbs7x7000104lbbvyoz41w | [HUX and AUX Are Not Buzzwords. They Are System Design Constraints.](posts/2026/02/2026-02-15_2026-T-018_hux-aux-ce-ci-cd/post-hux-aux-ce-ci-cd-2026-T-018.md) | PENDING_REVIEW | INGESTED | needs_work | Defines HUX vs AUX; why they power the CE/CI/CD loop | 0 | 1 | 0 | tech | EPMS | Mike | — | — | — | Mike | TECH_UX, AGENTICAI_DEVOPS, FUTUREAI_PRODDEV | 2026-02-20 |

---

## Data Provenance (per column)

Shows which source and merge rule produced each column value.

| Column | Source | Merge Rule |
|--------|--------|------------|
| Post ID | Squawk `extraction.externalPostId` | Read from Squawk |
| CUID | Squawk `document.id` | Read from Squawk |
| Title | Squawk `extraction.title` + `sourcePath` for link | Rule 7: linkify via sourcePath |
| Review Status | Mapped from post-index Status | Rule 2: all draft-family→PENDING_REVIEW, approved→APPROVED, published→PUBLISHED |
| Doc Status | Squawk `document.status` | Rule 6: don't touch |
| Readiness | Squawk `readinessScore`, override to `needs_work` if delayed | Rule 4: readiness for delayed |
| Readiness Notes | Content-based: if post has no dependency, comments go here. `DELAYED:` prefix if delayed. | Rule 3: content-based routing |
| Critical | Squawk `criticalConcernCount` | Rule 6: don't touch |
| Posts | Squawk `postsCount` | Rule 6: don't touch |
| Published | Squawk `publishedPostsCount` | Rule 6: don't touch |
| Audience | post-index `Audience` | Rule 1: post-index wins |
| Product | post-index `Product` | Rule 1: post-index wins |
| Expert | post-index `Expert` | Rule 1: post-index wins |
| Depends On | post-index `Depends On` | Rule 1: post-index wins |
| Dep. Name | post-index `Dependency Name` | Rule 1: post-index wins |
| Relationship | Only when post HAS `Depends On`: post-index `Relationship/Comments` | Rule 3: content-based routing |
| Repost By | Squawk `extraction.repostByNames` | Rule 6: don't touch |
| Themes | post-index `Themes` | Rule 5: post-index master, overwrite all |
| Updated | Squawk `updatedAt` | Rule 6: don't touch |

---

## Migration Status

- **Test batch:** B-001, T-013, B-016, T-018 — migrated and verified
- **Remaining:** 78 posts pending migration
- **Next step:** User confirmation of this sample, then full migration

### Observations from test batch

1. **B-001 `declaredThemes` is empty in Squawk** — it was ingested before `referenceContext` was available. Full migration will re-ingest with referenceContext. The Themes column above uses post-index (Rule 3) so the display is correct regardless.
2. **B-001 `repostByNames` is empty** — same reason (pre-referenceContext ingestion). Will be populated during full migration re-ingestion.
3. **T-013 has `postsCount: 3`** — multiple post records from duplicate ingestions. Not blocking; the primary post has correct expertId/productId.
4. **B-016 Readiness Notes overridden** — Squawk's AI assessment said "requires clarification on dashboard status." Merge Rule 2 replaced this with `DELAYED: We have not yet developed a water use dashboard.` because post-index status is `draft/delayed`.
