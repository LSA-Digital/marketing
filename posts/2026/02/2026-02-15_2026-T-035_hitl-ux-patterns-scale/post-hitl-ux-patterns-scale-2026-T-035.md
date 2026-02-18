# Designing the Review Queue: A Narrative of Human-in-the-Loop UX

## Metadata
- **Post ID**: 2026-T-035
- **CTA**: book a working session at [lsadigital.com](https://lsadigital.com)

## Post

When we sat down to design our agentic outreach system, Keith Mangold laid out a rule that changed our entire approach: "If you can't show the review queue to a stakeholder and have them understand what the agent proposed and why, the UX isn't done." This wasn't just about aesthetics; it was about building a system where humans could steer autonomy without becoming a bottleneck. We moved away from treating "Human-in-the-Loop" (HITL) as a safety brake and started treating it as a core product surface.

Using the Goal-Question-Metric (GQM) method, we built an architecture that integrates GPT-4o with tools like Apify, Tavily, and Google CSE to gather evidence before proposing an action. The agent doesn't just ask for approval; it packages its intent, the evidence it found, and the specific goal it's trying to achieve. This is where Agent-UX (AUX) meets Human-UX (HUX). If the agent can't explain itself, the human is just guessing.

Keith's perspective on why early automation fails is simple: teams ship autonomy they can't trust because they didn't design the feedback loop. We implemented a closed loop where low-risk actions run automatically, while high-risk steps are gated for explicit human approval. By designing the review experience as a first-class feature, we've created a system that scales with confidence. It's not about slowing down; it's about moving fast because you know you have the right eyes on the right steps.

## Artifacts
- Remote:
  - https://www.lsadigital.com/insights/how-we-built-a-human-in-the-loop-ai-system-webinar-recap

## Post asset ideas
- [ ] Screenshot: A review queue card showing agent evidence and intent
- [ ] Diagram: The GQM-driven agentic architecture
- [ ] Checklist: Keith's "Stakeholder Ready" review queue requirements

### Screenshots

![MEDICODAX dashboard with Claims Defender and Missing Docs Agent sidebar — AI assistants, not replacements](assets/medicodax-agent-sidebar-hitl.png)
*MEDICODAX dashboard — Claims Defender and Missing Docs Agent sidebar (AI assistants, not replacements)*

![Claims Defender panel open showing AI Denial Defense presenting evidence for human review](assets/medicodax-claims-defender-evidence.png)
*Claims Defender panel — AI Denial Defense presenting evidence for human review*

![Missing Docs Agent panel showing documentation gap identification](assets/medicodax-missing-docs-tracker.png)
*Missing Docs Agent panel — documentation gap identification*

