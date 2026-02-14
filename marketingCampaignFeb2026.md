## LSA Digital — Marketing Campaign Organizing Doc (Feb 2026)

### Purpose
Generate interest from **business + technical audiences** in the LSA Digital brand, and convert that interest into **qualified conversations** that lead to **custom Human‑AI solution development** work.

### Principles:  North Star positioning (rebrand anchor)
- **Core thesis**: **Enterprise Heritage. Startup Velocity.**
- **Operating model**: Human‑AI **Develop → Deploy → Disrupt** concept-to-scale cycle.
- **Differentiator**: aim for speed **and** compliance/scale (the “LSA Zone”), not “fast prototypes that die in governance.”
- **Experience first** Everything must show experience to differentiate from “armchair quarterbacks”  who post stuff but haven’t actually done this before
- **Dual audiences** Must differentiate between tech / business audiences 

Primary sources for high-level LSA Digital & product messaging
- `https://www.lsadigital.com/`
- `https://www.lsadigital.com/products`

### Constraints
- **Low budget**: rely on partner reposts, founder networks, and repurposing one artifact into many formats.
- **Show evidence**: when practical, use real artifacts (screenshots, demo clips, architectures, tests, validation, workflow steps) first; “lessons learned” second.

---

## Audience map (write for both without sounding split-brained)
### Business readers
Founders, GMs, ops leaders, innovation leaders, VPs/Directors, program owners.
- Want: credible speed, reduced risk, clear pilot path, stakeholder-ready narrative.

### Technical readers
Enterprise architects, eng leads, platform teams, AI/ML leads, security/compliance, product managers.
- Want: architecture clarity, integration realities, auditability, evaluation/testing evidence.

---

## Offer + conversion path (keep it simple)
- **Primary CTA**: “Book a 20–30 min working session” (map your idea to Develop/Deploy/Disrupt + pilot path).
- **Secondary CTA**: “Request a demo” (LSARS / HSRA / EPMS / ReimagineIt / MEDICODA).
- **Proof CTA**: “See the artifacts” (short clips + screenshots + brief technical notes).

---

### Messaging Themes (tags)

see @messagingThemes.md for more granular messaging themes.  These can be tagged per-post.  They are more narrow than "Content Pillars" below.

-- 

## Content pillars 

### Pillar 1 — Experts + AI (Human‑in‑the‑Loop done for real)
**Message**: AI accelerates; experts provide judgment + safety. We design workflows where **AI proposes and experts dispose**.

Anchor partnership/proof:
- LSARS principals on `https://lsars.com/`:
  - **Nelson Smith** (Principal; 35+ yrs environmental & legal / mass tort)
  - **Dr. Thad Perry** (Principal; 30+ yrs healthcare informatics & research; backed by clinical experts)
  - **Mike Idengren** (Principal; 28+ yrs digital transformation + AI tech; Human‑AI.com founder)

Products to spotlight under this theme:
- **LSARS** (expert verification + permitting/compliance workflows): `https://www.lsadigital.com/products/lsars` and `https://lsars.com/`
- **HSRA** (regulatory-grade health & social risk analysis; validated parity): `https://www.lsadigital.com/products/hra`
- **MEDICODA** (coding force-multiplier; clinics + SLMs): `https://www.lsadigital.com/products/medicoda`

High-performing formats:
- “Before → after” workflow screenshots
- Expert review/verification step (what is checked, how, and why)
- Validation/evidence posts (parity, tests, E2E, audit trail)

### Pillar 2 — AI technology (agentic + productized + enterprise-aware)
**Message**: We don’t just “use AI,” we build **systems**—agentic workflows, measurable outputs, governance hooks, and product UX where humans drive intent.

Anchor proof:
- Human‑in‑the‑Loop outreach system webinar recap: `https://www.lsadigital.com/insights/how-we-built-a-human-in-the-loop-ai-system-webinar-recap`
  - Includes: GQM method, agentic architecture, integrations (GPT‑4o, Apify, Tavily, Google CSE), closed feedback loop demo.


High-performing formats:
- Simple architecture diagrams (roles → agents → tools → data → governance)
- “How we evaluated it” (tests, parity checks, regression harness, E2E)
- “How humans steer it” (intent capture, review queues, audit logs, approvals)


### Pillar 3 (recommended) — Speed, security & compliance at scale
**Message**: “Fast” doesn’t mean fragile. We design for pilot readiness and enterprise realities (security, auditability, integration).
Use carefully phrased claims (“in progress”, “prototype”, “public beta”) and show artifacts.

---

## Content rules (non‑negotiables)

Generally, **No AI slop**:  The content must feel authentic; no formulaic mechanical posts or recycled garbage.  It has to be anchored in real experience for real outcomes, including the domain expertise from real partners/experts when appropriate (e.g., business domain problem-solving posts).

- **Experience-first**: include at least one of (text description, screenshot, short clip, diagram, test/validation snippet) in every major post.
- **Then interpretation**: lessons learned, best practices derived from the experience.
- **No generic hype**: if it can be posted by any AI consultancy, it doesn’t ship.
- **Claims discipline**: keep stages accurate (DEVELOP/DEPLOY/public beta/in progress).

---

## Single source of truth: Expert ↔ product alignment
Maintain and reference:
- `./lsaProductExpertAlignment.md`

Writing agents must pull expert names/roles/claim boundaries from that file only.

---

## Content inventory (primary sources for agents)
Brand and portfolio:
- `https://www.lsadigital.com/`
- `https://www.lsadigital.com/products`

Products:
- LSARS: `https://www.lsadigital.com/products/lsars`
- HSRA: `https://www.lsadigital.com/products/hra`
- EPMS: `https://www.lsadigital.com/products/epms`
- MEDICODA: `https://www.lsadigital.com/products/medicoda`
- Human‑AI Concept Lab: `https://www.lsadigital.com/products/human-ai-optimizer`
- ReimagineIt: `https://www.lsadigital.com/products/reimagineit`

Proof / “what we built”:
- Webinar recap (Human‑in‑the‑Loop outreach system): `https://www.lsadigital.com/insights/how-we-built-a-human-in-the-loop-ai-system-webinar-recap`
- Partner site (bios + LSARS proof): `https://lsars.com/`

Note:
- There is also an LSA Digital insight post titled “LSA ProspectPilot Human‑AI Marketing Solution” listed on the LSA Digital homepage insights section. If used, link directly:
  - `https://www.lsadigital.com/insights/lsa-prospectpilot-human-ai-marketing-solution`

---

## Content creation standard (simple + durable)
### Rule: every post lives in `./posts/`
- **All post content goes in `posts/`** so it’s searchable, reusable, and easy to ship.
- **Each post gets its own sub-folder** under `posts/`.
- A “post” is defined by **one Markdown file** (the canonical post text) plus any supporting assets (images/video/etc).
- The Markdown file may include **local assets** and **remote links**:
  - **Local assets** (preferred for screenshots/exports you control) must live **in the same post folder** as the Markdown file.
  - **Remote links** are allowed for canonical sources (product pages, partner sites, YouTube, etc.).

### Recommended folder structure (stands the test of time)
Use a date + slug so posts naturally sort and are stable across weeks/months/years.

- `posts/YYYY/MM/YYYY-MM-DD_slug/`
  - `post.md` (canonical post text + notes)
  - `assets/` (optional; images, gifs, video, diagrams, exported PDFs)
  - `links.md` (optional; curated remote URLs, citations, UTMs)
  - `notes.md` (optional; research, SME feedback, approvals, claim boundaries)

Example:
- `posts/2026/02/2026-02-03_lsars-expert-verification/`
  - `post.md`
  - `assets/lsars_workflow_before_after.png`
  - `assets/outreach_loop.mp4`
  - `links.md`

### Post Markdown conventions (keep it lightweight)
At the top of `post.md`, include a small metadata block so it’s easy to plan and review:
- **Title**
- **Channel** (LinkedIn post | demo clip script | longer artifact)
- **Theme** (Experts+AI | AI technology | Compliance+scale)
- **Status** (draft | in_review | approved | published)
- **Publish target** (date + time + poster)
- **SME reviewer** (from `./lsaProductExpertAlignment.md` when relevant)
- **Artifacts** (local file paths + remote links)
- **Claim boundaries** (prototype / beta / in progress; “what we did” only)

---

## Distribution plan (low budget, partner-forward)
Primary channel:
- LinkedIn (company + founders/SMEs)

Partner amplification (make it easy):
- Build “repost kits” per post (3 suggested captions + 1 image + 3 bullets + 1 link with UTM).
- Tag partners/SMEs when relevant (pre-coordinate so it’s not a surprise).

Secondary (optional):
- YouTube shorts (unlisted clips embedded in posts)
- Newsletter repost (same content, different intro)
- Targeted community posts (product mgmt, enterprise architecture, compliance, environmental permitting)

Always:
- Use **UTMs** on outbound links (including partner repost kits).

---

## Publication cadence (Feb 2026 baseline)
Sustainable starter cadence:
- **3 LinkedIn posts/week** (**Mon + Wed + Fri**)
- **2 short demo clips/week** (recommend Tue + Thu)
- **1 longer artifact drop/week** (blog/insight-style post OR PDF “artifact drop”)

### Feb 2026 editorial calendar (starter)
Week 1
- **Mon post**: Theme 1: LSARS — expert verification workflow (“AI proposes; experts dispose”)
- **Tue clip**: Develop → Deploy → Disrupt in 60–90s using one product as example
- **Wed post**: Theme 2: Human‑in‑the‑Loop outreach system — architecture + why GQM worked
- **Thu clip**: Outreach system loop diagram + narration (60–90s)
- **Fri post**: Theme 3: Speed with compliance & scale — “what makes it enterprise-ready” checklist (artifact-first)
- **Longer artifact (weekly)**: 1–2 page “Artifact drop” PDF: outreach system architecture (roles → agents → tools → governance) + 3 key lessons

Week 2
- **Mon post**: Theme 1: HSRA — what “parity validated” means (explain simply + show evidence types)
- **Tue clip**: HSRA evidence types walkthrough (tests/parity/audit trail) in 60–90s (no over-claims)
- **Wed post**: Theme 2: ReimagineIt — clarity score prevents fast wrong solutions
- **Thu clip**: “Clarity score” demo snippet / storyboard (60–90s)
- **Fri post**: Theme 3: Speed with compliance & scale — how humans steer + approve (review queues + audit logs)
- **Longer artifact (weekly)**: Blog/insight-style post: “What parity validation means (and what it doesn’t)” + screenshots/artifacts

Week 3
- **Mon post**: Theme 1: MEDICODA — clinic partnership realities (burnout, accuracy, auditing)
- **Tue clip**: Human final decision loop + real-time auditing (60–90s)
- **Wed post**: Theme 2: EPMS — AI-assisted discovery while PM intent stays in control
- **Thu clip**: “From idea to pilot-ready” mapped to Develop/Deploy/Disrupt (60–90s; avoid over-claims)
- **Fri post**: Theme 2: EPMS — “artifact capture” mini-checklist (intent → tool calls → outputs → traceability)
- **Longer artifact (weekly)**: EPMS artifact drop: intent entry screenshot + example outputs + boundary/governance notes

Week 4
- **Mon post**: Theme 3: Speed vs compliance — practical checklist (auditability, tests, approvals)
- **Tue clip**: “What makes Human‑AI enterprise-ready?” (short, concrete; 60–90s)
- **Wed post**: Theme 1+2: LSARS unified platform story (trust + HSRA + AI tooling)
- **Thu clip**: LSARS workflow “before → after” (60–90s)
- **Fri post**: Theme 1: Experts + AI — how to request SME soundbites + review flow (lightweight process, artifact-first)
- **Longer artifact (weekly)**: End-of-month round-up: “Feb artifacts” gallery post (links + 1 paragraph per artifact)

---

## Brief template for content-writing agents (copy/paste)
- Audience: business / technical / mixed
- Theme: Experts+AI / AI technology / Compliance+scale
- Primary artifacts to cite: (paste 1–3 URLs)
- One concrete “what we did”: (screenshot? test? workflow? clip? architecture?)
- Claim boundaries: prototype vs public beta vs “in progress”
- CTA: demo request / working session / artifact download
- Format: LinkedIn short / LinkedIn long / carousel script / 60s clip script
- SME reviewer: (from `./lsaProductExpertAlignment.md`)

---

## Publishing checklist for publishing agents
- Visual attached (screenshot/clip/diagram)
- Hook is problem-first, not hype-first
- Includes one measurable detail (tests, parity, workflow step, time saved, accuracy target—only if provable)
- Partner repost kit prepared (3 alt captions)
- UTM link used
- Seed 2 comments (artifact detail + a question)

### UTM convention + repost kit template (low budget amplification)
#### UTM convention (simple, consistent)
Use:
- `utm_source`: linkedin | partner | newsletter | youtube
- `utm_medium`: organic | repost | comment
- `utm_campaign`: feb_2026_human_ai
- `utm_content`: short_slug_for_post (e.g., lsars_expert_verify_01)

#### Repost kit (paste into a shared doc/thread for partners)
- **Post link**: <URL with UTM>
- **1 image / 1 clip**: <asset link>
- **3 suggested captions**:
  1) (business-leaning) …
  2) (technical-leaning) …
  3) (partner voice) …
- **3 proof bullets (artifact-based)**:
  - …
  - …
  - …
- **1 question prompt** (to drive comments):
  - …

---

## KPI + feedback loop (minimal viable)
- Top-of-funnel: impressions, saves, meaningful comments, partner reposts
- Mid-funnel: clicks to demo/Let’s Talk, time on page
- Bottom-funnel: booked calls, pilot requests, intros

Every 2 weeks:
- Identify top 2 posts by saves/comments
- Publish “Part 2” deeper on one artifact (not broader)

---

## Additional planning angles (recommended)
- ICP slices + message matrix:
  - “Ops bottleneck” (ReimagineIt), “Permit risk” (LSARS/HSRA), “PM discovery speed” (EPMS), “Compliance-heavy workflow” (Human‑AI Concept Lab), “Clinical admin burden” (MEDICODA)
- Proof library:
  - “Artifact gallery” page: screenshots, short clips, diagrams, validation/testing evidence
- Objection handling posts:
  - “Is this secure?”, “How do we audit it?”, “What’s the human’s role?”, “What’s real vs prototype?”
- Partner-forward calendar:
  - 1–2 posts/month explicitly co-authored with partner SMEs (max repost leverage)
