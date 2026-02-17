# Asset Execution Plan — Pillar II Posts (T-017 through T-041)

**Created:** 2026-02-15
**Acceptance Criteria:** 2-3 assets per post so the user can pick favorites.
**Pipeline docs:** `docs/asset-creation-pipeline.md`
**Capture scripts:** `assetpipe/` (reusable Playwright scripts + examples)

---

## Summary

| Category | Posts | Assets per Post | Total Assets | Method |
|----------|-------|-----------------|--------------|--------|
| LSARS screenshots | 6 | 2-3 | 16 | Playwright (`assetpipe/lsars-captures.js`) |
| MEDICODA screenshots | 3 | 3 | 9 | Playwright (`assetpipe/medicoda-captures.js`) |
| EPMS screenshots | 5 | 2-3 | 12 | Playwright (`assetpipe/epms-captures.js`) |
| Codebase-derived | 11 | 2-3 | 28 | Code snippets, Mermaid diagrams, markdown tables |
| **Total** | **25** | **2-3** | **~65** | |

---

## Batch 1: LSARS HRA Screenshots (6 posts, 16 assets)

Script: `assetpipe/lsars-captures.js` | URL: `http://localhost:3230` | Auth: none

| Post | Asset | Type | Filename | What It Shows |
|------|-------|------|----------|---------------|
| **T-024** | 1. Welcome modal | Screenshot | `lsars-welcome-methodology.png` | Logo, CA-OEHHA vs EPA methodology selector |
| | 2. Full map view | Screenshot | `lsars-map-full-view.png` | US map with state boundaries, sidebar, search |
| | 3. MA county drilldown | Screenshot | `lsars-ma-county-drilldown.png` | County-level detail after state selection |
| **T-027** | 1. California complexity | Screenshot | `lsars-california-complexity.png` | Full app with data loaded — scale of the codebase |
| | 2. Hotspot Analysis | Screenshot | `lsars-hotspot-analysis.png` | Analytical capability requiring deep code understanding |
| | 3. Health Risk Advisor | Screenshot | `lsars-health-risk-advisor.png` | AI chatbot — the agent surface built on codebase memory |
| **T-029** | 1. Welcome context | Screenshot | `lsars-welcome-context-summary.png` | Compact context summary (the app's "checkpoint") |
| | 2. ZIP search | Screenshot | `lsars-zip-search-boston.png` | Direct navigation via ZIP code — efficient context use |
| | 3. NY full UI | Screenshot | `lsars-ny-full-ui.png` | Full page with all panels visible |
| **T-032** | 1. Methodology selector | Screenshot | `lsars-methodology-selector.png` | EPA vs CA-OEHHA — the calculation system being validated |
| | 2. CA risk data | Screenshot | `lsars-ca-risk-data.png` | State with risk data loaded — output validated against HARP2 |
| **T-033** | 1. PA layered view | Screenshot | `lsars-pa-layered-architecture.png` | Map with data — shows the 4-layer architecture in action |
| | 2. Chatbot observable | Screenshot | `lsars-chatbot-observable.png` | Agent interaction showing request/response tracing |
| **T-039** | 1. FL sandboxed app | Screenshot | `lsars-fl-sandboxed-app.png` | Full app — demonstrates the microservice architecture |
| | 2. Sandboxed entry | Screenshot | `lsars-sandboxed-entry.png` | Welcome modal — isolated entry point |

---

## Batch 2: MEDICODA Screenshots (3 posts, 9 assets)

Script: `assetpipe/medicoda-captures.js` | URL: `http://localhost:3000` | Auth: auto-login

| Post | Asset | Type | Filename | What It Shows |
|------|-------|------|----------|---------------|
| **T-019** | 1. Dashboard | Screenshot | `medicoda-dashboard-ehr-integration.png` | Time savings, record count, EHR sync status |
| | 2. Audit Logs | Screenshot | `medicoda-audit-logs-security.png` | Timestamped audit trail — JWT-secured operations |
| | 3. User context | Screenshot | `medicoda-user-auth-context.png` | User identity, role, EHR connection (user menu open) |
| **T-020** | 1. Dashboard metrics | Screenshot | `medicoda-dashboard-time-savings.png` | AI pipeline output — time savings, pending submissions |
| | 2. Mobile Queue | Screenshot | `medicoda-mobile-queue-voice.png` | MobileEMNote voice submissions — the voice workflow |
| | 3. Wizard | Screenshot | `medicoda-wizard-direct-entry.png` | Structured entry workflow — EMClaimPacket path |
| **T-035** | 1. Agent sidebar | Screenshot | `medicoda-agent-sidebar-hitl.png` | Dashboard with Claims Defender + Missing Docs Agent |
| | 2. Claims Defender | Screenshot | `medicoda-claims-defender-evidence.png` | AI Denial Defense panel open — agent presenting evidence |
| | 3. Missing Docs | Screenshot | `medicoda-missing-docs-tracker.png` | Documentation Tracker panel — agent identifying gaps |

---

## Batch 3: EPMS Screenshots (5 posts, 12 assets)

Script: `assetpipe/epms-captures.js` | URL: `http://localhost:5173` | Auth: `REMOTE_USER: admin@lsadigital.com`

| Post | Asset | Type | Filename | What It Shows |
|------|-------|------|----------|---------------|
| **T-017** | 1. Kanban HUX | Screenshot | `epms-kanban-hux.png` | Product lifecycle kanban — the HUX surface |
| | 2. Product detail | Screenshot | `epms-product-detail-entities.png` | Entity relationships, artifacts — what MCP tools interact with |
| | 3. Navigation | Screenshot | `epms-navigation-routes.png` | Full page showing all routes — 13-router architecture |
| **T-018** | 1. HUX surface | Screenshot | `epms-hux-kanban.png` | Human-facing product management interface |
| | 2. Product data | Screenshot | `epms-product-data-hux-aux.png` | Same data exposed for humans vs agents |
| **T-021** | 1. Artifact library | Screenshot | `epms-artifact-library.png` | Product artifacts powering the guest portal |
| | 2. Feature overview | Screenshot | `epms-feature-overview.png` | "5 of 13 features" — staged AI-powered rollout |
| **T-022** | 1. Survived system | Screenshot | `epms-kanban-survived.png` | Kanban — the system that survived the dial turn |
| | 2. Structured data | Screenshot | `epms-structured-tools.png` | Product detail — what replaced the killed NL query |
| **T-038** | 1. API surface | Screenshot | `epms-kanban-api-surface.png` | UI built on the 14-tool MCP API |
| | 2. Entity relations | Screenshot | `epms-entity-relationships.png` | Product detail — entity relationships the API exposes |

---

## Batch 4: Codebase-Derived Assets (11 posts, 28 assets)

No Playwright needed — these are code snippets, Mermaid diagrams, and markdown tables extracted from source repos and written directly into post markdown.

| Post | Asset | Type | Source | What It Shows |
|------|-------|------|--------|---------------|
| **T-023** | 1. Plan doc screenshot | Code snippet | `~/dev/lsars-hra/docs/plans/` | A real plan doc referencing Jira ticket |
| | 2. Playwright test output | Code snippet | `~/dev/lsars-hra/apps/ui/e2e/` | E2E test with screenshot artifacts |
| | 3. Traceability loop | Mermaid diagram | Architecture knowledge | Jira ↔ Plan ↔ Commit ↔ Test |
| **T-025** | 1. Lazy-MCP architecture | Mermaid diagram | `~/dev/common/lazy-mcp/config.json` | Agent → Proxy → 5 Servers |
| | 2. Tool categorization | Code snippet | `~/dev/common/lazy-mcp/config.json` | 5 categories, 126 tools |
| | 3. AGENTS.md excerpt | Code snippet | `~/dev/marketing/AGENTS.md` | Context rehydration structure |
| **T-026** | 1. Agent tools matrix | Markdown table | Architecture knowledge | Tools × cost/speed/reasoning depth |
| | 2. Model config | Code snippet | `~/dev/marketing/.Claude/oh-my-Claude.json` | Agent model assignments |
| | 3. Portability checklist | Markdown checklist | Architecture knowledge | Artifacts for portable agent workflow |
| **T-028** | 1. Safe sandbox audit | Markdown checklist | Architecture knowledge | Audit checklist for agentic workflows |
| | 2. Blast radius diagram | Mermaid diagram | Docker knowledge | Local Docker sandbox vs Production |
| | 3. MCP allowlist config | Code snippet | `~/dev/marketing/.Claude/` or agent config | Tool allowlist for "High Vibe" mode |
| **T-030** | 1. Identity-aware proxy | Mermaid diagram | `~/dev/epms/` Apache OIDC config | Proxy vs traditional perimeter |
| | 2. MCP_ALLOWED_ROLES | Code snippet | `~/dev/epms/` config | Route → identity → permission mapping |
| | 3. Auth methods flow | Mermaid diagram | Architecture knowledge | 3 auth methods in single request |
| **T-031** | 1. Context7 resolution | Code snippet | Real Context7 MCP call | Library ID resolution in real-time |
| | 2. Before/after comparison | Markdown table | Dev experience | Guess-driven vs Context7-informed |
| | 3. Enforcement loop | Mermaid diagram | `~/dev/marketing/.claude/rules/context7-first.mdc` | The "Context7 First" enforcement loop |
| **T-034** | 1. Attack tree | Mermaid diagram | Security knowledge | Prompt injection → tool misuse → data exfil |
| | 2. Token lifetimes | Markdown table | `~/dev/em-lab/` FHIR client | Epic vs eCW token comparison |
| | 3. Audit logging | Code snippet | `~/dev/em-lab/backend/app/` | SQLAlchemy event listener |
| **T-036** | 1. Config diff | Code snippet | Git history / config files | MCP_ALLOWED_ROLES changes |
| | 2. Canary rollout flow | Mermaid diagram | Architecture knowledge | Canary → observe → promote/rollback |
| | 3. Pre-flight checklist | Markdown checklist | Architecture knowledge | Requirements for prompt/config changes |
| **T-037** | 1. Architecture template | Mermaid diagram | Architecture knowledge | Roles → Agents → Tools |
| | 2. Eval plan sample | Markdown table | Architecture knowledge | Golden task thresholds |
| | 3. Security boundaries | Markdown table | Architecture knowledge | Agent permission worksheet |
| **T-040** | 1. Compliance workflow | Mermaid diagram | Architecture knowledge | Drift → Alert → Remediate → Evidence |
| | 2. Control checklist | Markdown checklist | Architecture knowledge | Top 5 automated controls |
| | 3. Evidence update pattern | Code snippet | Architecture knowledge | Continuous evidence collection |
| **T-041** | 1. Jira ticket template | Markdown template | Architecture knowledge | Security bug report structure |
| | 2. Verification evidence | Code snippet | Redacted example | Real "fix verified" section |
| | 3. Security fix checklist | Markdown checklist | Architecture knowledge | 5 things every fix needs |

---

## Execution Order

1. **Batch 1 (LSARS)** — No auth, simplest. Run all `lsars-captures.js` functions.
2. **Batch 2 (MEDICODA)** — Auto-login. Run all `medicoda-captures.js` functions.
3. **Batch 3 (EPMS)** — Requires auth header. Run all `epms-captures.js` functions.
4. **Batch 4 (Codebase)** — Read source files, write Mermaid/snippets/tables directly into posts.
5. **Embed all** — After all assets exist, inject `![alt](assets/filename.png)` into every post.
6. **Verify** — `ls` every assets/ directory, confirm 2-3 files per post.

---

## Directories to Create Before Execution

```bash
# All 25 asset directories (idempotent — mkdir -p)
for slug in \
  epms-mcp-hux-aux-day0 hux-aux-ce-ci-cd medicoda-jwt-multi-ehr \
  medicoda-dynamic-workflow-adaptation epms-artifact-portal-qa \
  vibe-engineering-dial-ce-ci-cd jira-plan-docs-evidence-hooks \
  architecture-docs-vibe-dial mcp-proxy-context-window agent-tool-diversity \
  codebase-memory-graph-vector safe-sandbox-agentic-dev context-window-4mb-ram \
  zero-trust-reverse-proxy-example context7-must-have agent-evaluation-harness \
  agent-observability-tracing agent-security-threat-model hitl-ux-patterns-scale \
  prompt-config-rollout prototype-to-pilot-artifact-pack api-design-agent-ux \
  sandboxed-tool-execution-policy automated-compliance-drata \
  security-bug-evidence-required; do
  mkdir -p "posts/2026/02/2026-02-15_2026-T-0*_${slug}/assets" 2>/dev/null
done
```

Or more reliably:

```bash
for dir in posts/2026/02/2026-02-15_2026-T-0*/; do
  mkdir -p "${dir}assets"
done
```
