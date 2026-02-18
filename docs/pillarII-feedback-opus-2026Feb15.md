# Pillar II Credibility Review: Posts 2026-T-017 through 2026-T-041

**Reviewer:** Opus (AI review)
**Date:** 2026-02-15
**Scope:** 25 tech posts against Pillar II objective and campaign credibility standards

---

## Pillar II Objective (reminder)

> Get more software development contracts by proving we can explore and prototype at maximum speed (vibe coding) *and* ship reliable, secure, scalable systems when the idea proves feasible.

> Core message: Most ideas are infeasible. Vibe coding is powerful because it helps you test assumptions fast and stop early.

> Differentiator: the balance — treating "vibe" and "engineering" as a dial that shifts as risk increases.

---

## Executive Summary

These 25 posts cover the right topics for Pillar II. The ideas are solid. But as currently written, they violate several of the campaign's own credibility rules, and the cumulative effect would undermine rather than support the "we actually did this" positioning.

The three biggest problems:

1. **Zero evidence attached.** Every post's "Post asset ideas" checkboxes are empty. The campaign requires "at least one artifact" per major post. Right now these are claims without receipts.

2. **Formulaic structure reads as AI slop.** All 25 posts follow an identical template (opener → problem → bullets → "The critical design choice: **bolded phrase**" → CTA). The campaign explicitly forbids "formulaic mechanical posts."

3. **The core Pillar II message is mostly missing.** The differentiator is "most ideas are infeasible — stop early." Almost no post demonstrates killing an idea, learning from a failure, or showing the "stop" side of the dial. They only show success patterns.

---

## Cross-Cutting Issues (affect most or all posts)

### 1. No artifacts — the biggest credibility gap

| Campaign rule | Current state |
|---|---|
| "Experience-first: include at least one of (screenshot, clip, diagram, test/validation snippet)" | 0 of 25 posts include any artifact |
| "Show evidence: use real artifacts first; 'lessons learned' second" | All 25 posts are lessons-learned only |
| Publishing checklist: "Visual attached (screenshot/clip/diagram)" | Would fail checklist for all 25 posts |

**Recommendation:** Before publishing any of these, create or attach at least one concrete artifact per post. Even a redacted screenshot, a simple diagram, or a code snippet is better than nothing. Prioritize the posts closest to "approved" status first (T-017, T-030).

### 2. Identical template = AI slop signal

Every post follows this exact structure:
1. "We've built/done this in [product] — for example, [vague reference]"
2. Short provocative statement
3. Bulleted "How we do it" list
4. "The critical design choice: **[bolded takeaway]**"
5. Bare URL CTA

This is exactly the pattern the campaign doc warns against: "No AI slop: The content must feel authentic; no formulaic mechanical posts or recycled garbage."

**Recommendation:** Vary the structure across the series. Some posts should lead with a concrete story. Some should open with a technical problem and walk through the solution. Some should be structured as checklists or decision trees. Some should be short and punchy (3 sentences + a diagram). The variety itself signals authenticity.

### 3. "We did this" claims without specifics

Nearly every post starts with "We've built this" or "This is from real work we did" followed by a generic parenthetical like "(for example, our Human-in-the-Loop outreach system build)." But no post includes:
- A specific date or timeline
- A specific metric or measurement
- A specific decision that was made (and why)
- A specific problem that was encountered (and how it was resolved)
- A specific tradeoff that was weighed

**Recommendation:** For each post, add at least one concrete "receipt" — a specific fact that couldn't be written by someone who hadn't done the work. Examples:
- "When we built the EPMS MCP server, we started with 12 tool endpoints. After the first agent integration test, we cut it to 7 — the other 5 were redundant once we got schema contracts right."
- "Our first MEDICODAX JWT implementation used 24-hour tokens. After a threat model review, we moved to 15-minute tokens with refresh. The change took 2 days and broke 3 integration tests."

### 4. Missing the "stop early" narrative

Pillar II's core message is: **"Most ideas are infeasible. Vibe coding is powerful because it helps you test assumptions fast and stop early."**

Of 25 posts, approximately zero demonstrate:
- An idea that was killed because vibe coding revealed it was infeasible
- A prototype that was intentionally not shipped
- A feature that was tested and rejected
- A moment where the dial moved *back* from engineering to exploration (because the approach was wrong)

All 25 posts present success patterns. A reader thinking about hiring LSA Digital for dev contracts needs to see the *discipline* — that you know when to stop, not just when to go.

**Recommendation:** Add 2-3 "kill story" posts or weave failure/stop narratives into existing posts. Examples:
- T-022 (Vibe Engineering Dial): add a concrete example where an 80/20 exploration was killed at 60/40 because the approach proved infeasible
- T-032 (Agent Evaluation Harness): add an example where the eval harness caught a workflow that passed demos but failed golden tasks — and the team stopped and redesigned
- T-037 (Prototype to Pilot): add a brief note about what the artifact pack *prevented* — a pilot that would have failed

### 5. Repetition across posts

Several messages appear verbatim in multiple posts:
- "Deployment is not delivery/release" — appears in T-018, T-022, T-041
- "The critical design choice:" — identical phrasing in all 25 posts
- HUX/AUX definitions — repeated in T-017, T-018, T-020, T-031, T-035, T-038 without enough variation

Some pairs cover substantially the same ground:
- T-025 (MCP proxy context window) and T-029 (context window 4MB RAM) — both on context management
- T-028 (safe sandbox) and T-039 (sandboxed tool execution) — both on sandboxing agents
- T-030 (zero trust reverse proxy) and T-034 (agent security threat model) — both on security architecture

**Recommendation:** Either consolidate the overlapping pairs into single stronger posts, or differentiate them more sharply. For example:
- T-025 could focus on the *pattern* (MCP proxy); T-029 could focus on the *tactics* (specific caching/rehydration code examples)
- T-028 could focus on *development sandbox rules*; T-039 could focus on *production policy enforcement architecture*
- For repeated definitions (HUX/AUX, deployment vs delivery), use a consistent one-liner and link to the canonical definition post (T-018) instead of re-explaining each time

### 6. Expert voices are absent

Almost every post is attributed to Mike and Keith. For Pillar II credibility, these posts would benefit from:
- A Keith Mangold perspective on agentic architecture decisions (he's listed in expert alignment for exactly this)
- Product-specific expert context (Dr. Thad Perry on MEDICODAX clinical workflows, Nelson Smith on compliance/regulatory trust patterns)

Right now the content reads as one voice. The campaign's "partner-forward" strategy and "no AI consultancy could post this" rule both argue for incorporating expert perspectives.

**Recommendation:** For the MEDICODAX posts (T-019, T-020), consider adding a brief "why this matters clinically" perspective from Dr. Perry or a clinic partner. For security/compliance posts (T-030, T-034, T-039, T-040, T-041), Keith's architectural perspective would add weight. These don't need to be quotes — even "Keith's rule of thumb: if the agent can reach it, assume it will touch it" adds a real human voice.

### 7. CTA inconsistency

| CTA used | Posts |
|---|---|
| "book a working session at lsadigital.com" | T-017, T-018, T-019, T-020, T-021, T-022, T-023, T-024, T-025, T-026, T-027, T-028, T-029, T-032, T-035, T-037, T-038, T-040, T-041 |
| "see artifacts" | T-030, T-031, T-033, T-034, T-036, T-039 |

The "see artifacts" CTA points nowhere specific — these posts link to generic lsadigital.com. Until artifacts exist, this CTA is actively damaging to credibility.

**Recommendation:** Standardize CTA to "book a working session" for now. Switch individual posts to "see artifacts" only once those artifacts are actually published at a specific URL.

---

## Post-Specific Recommendations

### Product-Anchored Posts (need product-specific evidence)

| Post | Product | What's missing |
|---|---|---|
| **T-017** (EPMS MCP HUX/AUX) | EPMS | No EPMS screenshot, no MCP tool list, no "here are the 7 tools we ship." This is the flagship Pillar II/EPMS post and it has zero product evidence. |
| **T-019** (MEDICODAX JWT) | MEDICODAX | No architecture diagram showing JWT boundary. No evidence of multi-EHR integration. Claims "architecture and scalability proven" — where's the proof? |
| **T-020** (MEDICODAX dynamic workflow) | MEDICODAX | No workflow diagram. The iPhone voice capture vs direct entry adaptation is a compelling story — but it's told abstractly. A flow diagram would make this 5x more credible. |
| **T-021** (EPMS artifact portal) | EPMS | Claims EPMS stores and indexes artifacts with chatbot Q&A. No screenshot of the artifact library. No example Q&A exchange. This is a "show, don't tell" opportunity being wasted. |

**Priority action:** T-017 and T-021 are the most important EPMS posts for Pillar II. Getting even one real screenshot into each would meaningfully improve credibility.

### Vibe Engineering Dial Posts (need the "stop" narrative)

| Post | What's missing |
|---|---|
| **T-022** (Vibe Engineering Dial) | The dial graphic is the single most important visual for Pillar II. It doesn't exist yet. Also: no example of where the dial moved *backwards* (i.e., an approach was abandoned). |
| **T-023** (Jira + plan docs + evidence hooks) | This is one of the strongest posts conceptually. It would be dramatically more credible with a real (redacted) plan doc template or a real Playwright screenshot evidence example. |
| **T-024** (Architecture docs) | Claims "just-enough" architecture docs. Would benefit from a real, abbreviated example (even 1 page, redacted). |

### DevOps/Security Posts (overlap problem + missing specifics)

| Post | Recommendation |
|---|---|
| **T-030** (Zero trust reverse proxy) | This is "approved" — make sure it has the traffic flow diagram before publishing. Currently text-only. |
| **T-032** (Agent evaluation harness) | Strongest potential Pillar II credibility post. Needs a real golden task example and a real pass/fail output. Referencing HARP2-style validation is good but vague — what specific eval was run? |
| **T-033** (Agent observability) | References "Human-in-the-Loop outreach system architecture" tracing — this is a real proof point. Include an actual (redacted) trace example. |
| **T-034** (Agent security threat model) | Overlaps with T-030 and T-039. Differentiate by focusing on the *threat model* specifically — the attack tree, not just the controls. |
| **T-039** (Sandboxed tool execution) | Overlaps with T-028. Differentiate by focusing on *production runtime* enforcement, not development sandbox rules. |
| **T-040** (Automated compliance / Drata) | Mentions Drata by name — good specificity. Would be much stronger with a redacted dashboard screenshot. |
| **T-041** (Security bug evidence) | Strongest "receipts" post. Would benefit from a redacted Jira ticket template example. |

### Context/Memory Posts (consider consolidation)

| Post | Recommendation |
|---|---|
| **T-025** (MCP proxy context window) | Consolidate with T-029 or sharpen: T-025 = system-level pattern, T-029 = developer-level tactics |
| **T-027** (Codebase memory graph+vector) | One of the most differentiating posts. Needs a diagram showing graph-code + Memgraph + Qdrant architecture. This is real, built tooling — show it. |
| **T-029** (Context window = 4MB RAM) | The analogy is memorable. Keep this as the "tactics" companion to T-025. |
| **T-031** (Context7 must-have) | Good, specific. Include a real before/after code diff showing lookup-driven vs guess-driven implementation. |

### Remaining Posts

| Post | Recommendation |
|---|---|
| **T-018** (HUX/AUX definitions) | Good definitional post. Consider making this the canonical HUX/AUX reference that other posts link to, rather than each post re-defining terms. |
| **T-026** (Agent/tool diversity) | Claims use of Cursor, Claude, ChatGPT Codex, OpenCode, Kimi. Would be credible with a brief "one task, two agents" comparison — even pseudocode-level. |
| **T-028** (Safe sandbox tips) | Practical and concise. Needs a real checklist artifact (even text-based). |
| **T-035** (HITL UX patterns) | Good conceptual post. Links to webinar recap (good). Would benefit from an escalation-level diagram. |
| **T-036** (Prompt/config rollout) | Practical post. Needs a real config diff example — even a few lines of YAML. |
| **T-037** (Prototype to pilot artifact pack) | High-value Pillar II post. The "artifact pack" checklist should be a real, downloadable one-pager. This is the post most likely to convert a dev contract lead. |

---

## Priority Actions (ordered by impact on Pillar II credibility)

1. **Create the Vibe Engineering Dial graphic** (serves T-022 and anchors the whole series)
2. **Attach at least one real artifact to T-017, T-021, T-037** (the three posts most directly tied to winning dev contracts)
3. **Write or weave in 2-3 "kill story" narratives** (demonstrates the "stop early" discipline that is the core Pillar II differentiator)
4. **Vary post structure across the series** (break the template pattern — some story-led, some checklist, some diagram-first, some short+punchy)
5. **Add specific numbers/dates/decisions to "we did this" claims** (at least one concrete receipt per post)
6. **Resolve CTA inconsistency** (remove "see artifacts" until artifacts exist)
7. **Consolidate or sharpen overlapping post pairs** (T-025/T-029, T-028/T-039, T-030/T-034)
8. **Add expert voices to product-specific posts** (Keith on architecture; Dr. Perry on MEDICODAX clinical context)
9. **Create a T-037 "artifact pack" one-pager as a real downloadable** (highest-conversion Pillar II asset)
10. **Add the webinar recap link to more posts** (it's the anchor proof — only 2 of 25 posts link to it)

---

## Conclusion

The ideas in these 25 posts are strong and cover Pillar II well. The credibility gap is execution: no artifacts, no specifics, no variation, no failure stories. Fixing even the top 3-4 items above would significantly improve the series' ability to convince a technical evaluator or business decision-maker that LSA Digital can actually do what it claims.

The campaign doc's own standard is the right bar: "if it can be posted by any AI consultancy, it doesn't ship." Right now, most of these posts could be. The fix is straightforward: add the receipts.
