# Agentic AI “just-in-time” UX: the information you need, when you need it

## Metadata
- **Post ID**: 2026-T-015
- **Channel**: LinkedIn post
- **Target page**: [LSA Digital](https://www.linkedin.com/company/lsadigital/)
- **Product**: LSARS
- **Theme**: AI technology
- **Audience**: technical
- **Status**: draft
- **Poster**: company page
- **CTA**: see artifacts
- **Depends on**: 2026-B-015

## Post
Most “agentic UX” fails the same way: it either overwhelms the user with context, or it hides the reasoning behind a black box.

We built a pattern where a lead agent pulls in specialized agents **only when needed**, and each specialist is permissioned for the data it’s allowed to touch.

**How it works:**
- **Lead-agent orchestration**: the primary agent owns the user experience and decides when to consult specialists.
- **Specialist agents by domain**: e.g., public relations / community concerns, regulatory alignment, technical calculations—each with narrow responsibilities.
- **Isolated data permissions**: specialists can’t “see everything,” which reduces security risk and limits accidental leakage.

The critical design choice: **“just-in-time” isn’t about clever prompts—it’s about controlled access + deliberate escalation.**

**Result:** users get the right information at the right time, with fewer tool calls and cleaner provenance.

If you’re designing AI systems people must trust, start with orchestration and permissions—not model tricks. See the artifacts: https://lsadigital.com

## Artifacts
- Remote:
  - `https://lsadigital.com`

## Post asset ideas

Add any supporting artifacts for this post here.

### Suggested assets
- Agent graph diagram: lead agent + specialist agents + permissions boundaries
- Example escalation trigger list (what causes specialist invocation)
- Example redacted conversation trace showing provenance + handoffs
