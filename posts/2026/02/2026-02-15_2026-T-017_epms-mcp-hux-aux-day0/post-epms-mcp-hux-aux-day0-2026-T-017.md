# 14 MCP Tools. 118 API Endpoints. 33 Entities.

## Metadata
- **Post ID**: 2026-T-017
- **CTA**: book a working session at [lsadigital.com](https://lsadigital.com)

## Post

14 MCP tool endpoints. 118 REST API endpoints across 13 routers. 33 database entities with 22 relationship types. 556 test functions across 95 files. 29 Playwright E2E tests. 

These aren't just vanity metrics for EPMS; they are the receipts of Vibe Engineering—our approach of vibe coding for exploration + production-grade engineering for shipping. When we built the EPMS 7,294-line MCP server, we didn't just bolt on an AI interface. We designed for two distinct users from day zero.

First, there is Human-UX (HUX), the interface where product managers and investors interact with living artifacts. Then there is Agent-UX (AUX), the interface where tool-using agents execute workflows via structured schemas and response locking. Most "AI products" fail because they only build HUX. They ship a chat box and realize too late that their agents have no reliable surface to actually do work.

In EPMS, the AUX is a first-class citizen. Our 14 specialized MCP tools—covering everything from entity_crud to hierarchy and bulk operations—ensure that agents don't have to guess. They operate within a 7,294-line server architecture that handles streamable HTTP and duplicate suppression. This level of engineering discipline is what allows our Continuous Exploration (CE) to remain fast without sacrificing the stability required for CI/CD. We prove the architecture with 556 tests so that when you move the dial from exploration to production, the system doesn't collapse.

## Artifacts
- Remote:
  - https://www.lsadigital.com/products/epms

## Screenshots

### EPMS Kanban Board (HUX Surface)
![EPMS Kanban board showing product lifecycle stages and the human-facing interface](assets/epms-kanban-hux.png)
*The HUX surface where product managers and investors interact with living artifacts.*

### Product Detail with Entity Relationships
![Product detail view displaying entity relationships and connected artifacts](assets/epms-product-detail-entities.png)
*Entity relationships and artifacts connected across the 33-entity schema.*

### EPMS Navigation Architecture
![Full EPMS navigation showing the 13-router architecture](assets/epms-navigation-routes.png)
*The 13-router API architecture that powers both HUX and AUX surfaces.*

### MCP Tool Definitions
![MCP tool definitions endpoint showing schema-strict tools](assets/epms-mcp-tool-list.png)
*14 specialized MCP tools with strict schemas ensure agents operate reliably without guessing.*

## Post asset ideas
- [ ] Diagram: EPMS 13-router API architecture mapping to HUX/AUX surfaces
- [ ] Screenshot: MCP tool definitions showing schema-strict entity_link and hierarchy tools
- [ ] Code snippet: Streamable HTTP implementation in the 7,294-line MCP server
