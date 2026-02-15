# The Vibe Engineering Dial: Map 80/20 -> 20/80 to CE/CI/CD

## Metadata
- **Post ID**: 2026-T-022
- **CTA**: book a working session at [lsadigital.com](https://lsadigital.com)

## Post

This isn't theory - we've used this dial while building real systems (for example, EPMS workflows and our Human-in-the-Loop outreach system build).

Vibe coding is powerful.

It's also how teams accidentally ship fragile systems.

The move is not "vibe" or "engineering." It's a dial.

We use a simple framing:

- **80/20 (vibe/engineering):** Continuous Exploration (CE). Kill infeasible ideas early.
- **60/40:** prototype with enough structure to learn the right lessons.
- **40/60:** Continuous Integration / Continuous Deployment (CI/CD) starts to dominate.
- **20/80:** production discipline (security, reliability, auditability) becomes non-negotiable.

Note: **deployment is not delivery/release.** Product controls if/when deployed code is exposed to end users (and which ones).

Here's how it shows up in a real lifecycle:

- **Start:** people research in natural conversation (often in ChatGPT), then use MCP to interface with EPMS so the work becomes an artifact.
- **Iteration 1 (80/20):** "skin-deep" mockups and UI demos.
- **Iteration 2 (60/40):** sharpen with product management + stakeholders into a prototype.
- **Iteration 3 (40/60):** MVP funded for a pilot; anything touching real users/data needs day-0 pilot security/compliance.
- **Iteration 4 (20/80):** pivot from pilot lessons learned; scale up.

**What changes as the dial shifts (the receipts):**
- **Artifacts:** from sketches -> workflows -> architecture diagrams -> runbooks.
- **Evals/tests:** from "does it work" -> regression harness -> end-to-end coverage.
- **Security:** from sandbox -> scoped tokens -> least privilege by default.
- **Observability:** from none -> traces -> budgets and alerts.

The critical design choice: **CE isn't an excuse to be sloppy.** It's permission to be fast *where the risk is low*.

If you're trying to move fast without paying the production penalty later, set the dial deliberately and show the artifacts that justify it.

https://lsadigital.com

## Artifacts
- Remote:
  - https://www.lsadigital.com/insights/how-we-built-a-human-in-the-loop-ai-system-webinar-recap
  - https://lsadigital.com

## Post asset ideas
- [ ] One graphic: the Vibe Engineering dial with CE/CI/CD mapping
- [ ] Table: what artifacts are required at 80/20 vs 60/40 vs 40/60 vs 20/80
- [ ] Example: "deployment != release" rollout sketch (flags, staged rollout)
