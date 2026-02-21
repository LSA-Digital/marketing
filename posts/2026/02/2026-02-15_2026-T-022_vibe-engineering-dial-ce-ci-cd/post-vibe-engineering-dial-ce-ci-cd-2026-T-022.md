# The Vibe Engineering Dial: Why Most AI Ideas Should Be Killed

## Metadata
- **Post ID**: 2026-T-022
- **Audience**: tech
- **Product**: EPMS
- **Themes**: FUTUREAI_PRODDEV, AGENTICAI_DEVOPS
- **Expert**: Mike
- **Depends On**: —
- **Dependency Name**: —
- **Relationship**: Dial framing mapped to Continuous Exploration vs CI/CD (Continuous Integration / Continuous Deployment)
- **Assets**: epms-kanban-survived.png, epms-structured-tools.png
- **CTA**: book a working session at [lsadigital.com](https://lsadigital.com)

## Post

Vibe coding is the fastest way to explore a new idea, but it's also the fastest way to ship a disaster. At LSA Digital, we use Vibe Engineering—vibe coding for exploration + production-grade engineering for shipping—to manage this risk. The core of this approach is a dial that moves from 80/20 (vibe/engineering) during Continuous Exploration (CE) to 20/80 during CI/CD.

The most important part of CE isn't finding what works; it's killing what doesn't. During EPMS development, we prototyped a natural-language query builder that let agents compose arbitrary database queries from product manager questions. Three days in, the eval harness showed it hallucinated join paths on 40% of multi-entity queries. We killed it and built structured search tools instead—14 of them, each scoped to one entity or relationship type. The structured approach passed 556 tests. The "smart" one would have shipped bugs as features.

This is why we insist that deployment is not delivery/release. We deploy early to test assumptions, but we only release when the engineering dial has moved toward production discipline. As Keith Mangold often points out, early automation fails because it lacks the guardrails of a mature agentic architecture. By setting the dial deliberately, we ensure that our exploration is fast and our delivery is reliable. We don't just build what's possible; we build what's provable. If an idea can't survive our eval harness, it doesn't deserve to reach your users.

## Artifacts
- Remote:
  - https://www.lsadigital.com/insights/how-we-built-a-human-in-the-loop-ai-system-webinar-recap
  - https://lsadigital.com

## Screenshots

### EPMS Kanban Board (The System That Survived)
![EPMS Kanban board showing the structured product system that replaced the killed natural-language query builder](assets/epms-kanban-survived.png)
*The Kanban board represents the 14 structured tools that passed 556 tests—the system that survived the dial turn.*

### Structured Product Data Tools
![Structured product data that replaced the killed natural-language query builder](assets/epms-structured-tools.png)
*Each of the 14 tools is scoped to one entity or relationship type, eliminating hallucinated join paths.*

## Post asset ideas
- [ ] Diagram: The Vibe Engineering dial mapping CE/CI/CD to 80/20 -> 20/80
- [ ] Case study: The "Kill Story" of the natural-language query builder vs. structured tools
- [ ] Checklist: Eval harness requirements for moving the dial from 80/20 to 60/40

