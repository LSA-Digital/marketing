# HUX and AUX Are Not Buzzwords. They Are System Design Constraints.

## Metadata
- **Post ID**: 2026-T-018
- **Audience**: tech
- **Product**: EPMS
- **Themes**: TECH_UX, AGENTICAI_DEVOPS, FUTUREAI_PRODDEV
- **Expert**: Mike
- **Depends On**: —
- **Dependency Name**: —
- **Relationship**: Defines HUX vs AUX; why they power the CE/CI/CD loop
- **Assets**: epms-hux-kanban.png, epms-product-data-hux-aux.png
- **CTA**: book a working session at [lsadigital.com](https://lsadigital.com)

## Post

Stop treating Human-UX (HUX) and Agent-UX (AUX) as a terminology exercise. They are the two primary system design constraints for any modern agentic application. If you build for humans but ignore the agents, you are designing a system that will inevitably fail when you try to automate it.

At LSA Digital, we use Vibe Engineering—vibe coding for Continuous Exploration (CE) + production-grade CI/CD engineering for shipping.  Human-UX is the interface for humans to review, decide, and intervene. Agent-UX is the interface for agents to execute via tool calls, schemas, and permissions. The problem is that most teams treat AUX as an afterthought, exposing a few random endpoints and calling it an "agent integration."

In EPMS, we proved that AUX requires the same level of engineering rigor as HUX. We implemented two distinct auth methods (API Key and X-API-Key MCP OAuth), to ensure that every agentic action is authenticated and scoped. We backed this with 556 test functions to ensure that when an agent calls a tool, the result is predictable and idempotent. When your AUX is broken, your HUX suffers because humans end up debugging invisible agent failures instead of doing high-value work. By treating HUX and AUX as a single, coupled system design problem, we ensure that Continuous Exploration (CE) leads to reliable CI/CD without the "agent tax" that kills most AI projects.

## Artifacts
- Remote:
  - https://www.lsadigital.com/products/epms

## Screenshots

### EPMS Kanban as HUX Interface
![EPMS Kanban board serving as the human-facing interface](assets/epms-hux-kanban.png)
*Human-UX (HUX) is the interface where humans review, decide, and intervene.*

### Product Data Accessible to Both HUX and AUX
![Product detail showing data accessible by both HUX and AUX surfaces](assets/epms-product-data-hux-aux.png)
*The same product data serves both human and agent interfaces with different auth methods and response formats.*

## Post asset ideas
- [ ] Diagram: The coupling of HUX and AUX in a shared system design
- [ ] Comparison: Standard API error vs. AUX-optimized error with recovery hints
- [ ] Checklist: System design requirements for a production-grade AUX surface
