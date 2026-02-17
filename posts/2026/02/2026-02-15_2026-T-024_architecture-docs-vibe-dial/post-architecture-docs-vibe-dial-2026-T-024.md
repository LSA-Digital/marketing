# The Vibe Dial: When to Stop Coding and Start Documenting

## Metadata
- **Post ID**: 2026-T-024
- **CTA**: book a working session at [lsadigital.com](https://lsadigital.com)

## Post

In "Vibe Engineering"—where we balance rapid vibe coding (exploration) with production-grade engineering (shipping)—the most expensive mistake is documenting too early or too late. We use a "Vibe Dial" to trigger architecture requirements based on system complexity and risk.

When we built LSARS, we managed 9 Docker microservices (including pgbouncer, redis, and memgraph) and 13 API routers. At that scale, hidden assumptions aren't just bugs; they're system-wide outages.

**The Architecture Decision Tree:**

- **Dial at 80/20 (High Vibe):** You’re in Continuous Exploration (CE). No formal docs required. Use AGENTS.md for rehydration context so your AI knows the current "vibe" of the sandbox.
- **Dial at 50/50 (Balanced):** You’re touching one of the 4 calculation layers or modifying connection pooling (we cap at 300 max connections across 9 providers). **Action:** Create a lightweight "Plan Doc" in the repo. Define the interface and the data flow.
- **Dial at 20/80 (High Engineering):** You’re shipping to production or refactoring core logic covered by our 2,669+ test functions. **Action:** Full architecture alignment required. Update the system map and security boundaries.

Architecture docs aren't bureaucracy; they are the shared contract between humans and agents. By mapping documentation to the dial, we ensure we never slow down exploration, but never ship a "vibe" that we can't support in production.

## Artifacts
- Remote:
  - https://lsadigital.com

## Screenshots

### LSARS Welcome Modal with Methodology Selector
![LSARS welcome modal showing CA-OEHHA vs EPA methodology selector](assets/lsars-welcome-methodology.png)
*The entry point for LSARS, allowing users to choose their preferred regulatory methodology.*

### LSARS Full Map View
![LSARS full map view with state boundaries and search controls](assets/lsars-map-full-view.png)
*The 9-microservice architecture powers this interactive map across 13 API routers.*

### Massachusetts County-Level Drilldown
![Massachusetts county-level drilldown showing granular risk data](assets/lsars-ma-county-drilldown.png)
*Granular risk assessment at the county level, backed by the layered microservices architecture.*

## Post asset ideas
- [ ] Diagram: The Vibe Dial mapping dial settings to doc requirements
- [ ] Screenshot: The AGENTS.md file used for CE context rehydration
- [ ] Example: A "just-enough" architecture map for a new microservice
