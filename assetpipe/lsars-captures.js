/**
 * LSARS HRA Screenshot Captures
 * Product: LSARS Health Risk Assessment (localhost:3230)
 * Auth: None required
 *
 * Each export is an `async (page) => { ... }` function compatible with
 * Playwright MCP's browser_run_code.
 *
 * Posts served: T-024, T-027, T-029, T-032, T-033, T-039
 *
 * Usage via Playwright MCP:
 *   skill_mcp(mcp_name="playwright", tool_name="browser_run_code",
 *     arguments={ "code": "<paste function body>" })
 */

// ============================================================
// T-024: Architecture Docs & Vibe Dial
// Assets: AGENTS.md context rehydration, map view, architecture
// ============================================================

// T-024 Asset 1: Welcome modal with methodology selector
// Shows: LSARS logo, CA-OEHHA vs EPA methodology, Enter System button
const T024_welcome_modal = async (page) => {
  await page.goto('http://localhost:3230');
  await page.waitForTimeout(2000);
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-024_architecture-docs-vibe-dial/assets/lsars-welcome-methodology.png'
  });
};

// T-024 Asset 2: Full map view after dismissing modal
// Shows: US map with state boundaries, sidebar, search controls
const T024_map_view = async (page) => {
  await page.goto('http://localhost:3230');
  await page.waitForTimeout(2000);
  // Dismiss welcome modal
  const enterBtn = page.locator('button:has-text("Enter System")');
  if (await enterBtn.isVisible()) await enterBtn.click();
  await page.waitForTimeout(2000);
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-024_architecture-docs-vibe-dial/assets/lsars-map-full-view.png'
  });
};

// T-024 Asset 3: State drilldown (Massachusetts) showing county boundaries
// Shows: County-level detail, populated county selector, tract search
const T024_state_drilldown = async (page) => {
  await page.goto('http://localhost:3230');
  await page.waitForTimeout(2000);
  const enterBtn = page.locator('button:has-text("Enter System")');
  if (await enterBtn.isVisible()) await enterBtn.click();
  await page.waitForTimeout(1000);
  // Select Massachusetts from state dropdown
  await page.selectOption('select', 'Massachusetts');
  await page.waitForTimeout(3000);
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-024_architecture-docs-vibe-dial/assets/lsars-ma-county-drilldown.png'
  });
};


// ============================================================
// T-027: Codebase Memory (Graph + Vector)
// Assets: Memgraph visualization, semantic search results
// ============================================================

// T-027 Asset 1: LSARS map with data loaded (shows the app complexity)
// Shows: Full app with map, sidebar, search — demonstrates the scale of what agents must understand
const T027_app_complexity = async (page) => {
  await page.goto('http://localhost:3230');
  await page.waitForTimeout(2000);
  const enterBtn = page.locator('button:has-text("Enter System")');
  if (await enterBtn.isVisible()) await enterBtn.click();
  await page.waitForTimeout(1000);
  await page.selectOption('select', 'California');
  await page.waitForTimeout(3000);
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-027_codebase-memory-graph-vector/assets/lsars-california-complexity.png'
  });
};

// T-027 Asset 2: Hotspot Analysis button and panel
// Shows: The analytical capability that requires deep codebase understanding
const T027_hotspot_analysis = async (page) => {
  await page.goto('http://localhost:3230');
  await page.waitForTimeout(2000);
  const enterBtn = page.locator('button:has-text("Enter System")');
  if (await enterBtn.isVisible()) await enterBtn.click();
  await page.waitForTimeout(1000);
  await page.selectOption('select', 'Texas');
  await page.waitForTimeout(3000);
  // Click Hotspot Analysis
  const hotspotBtn = page.locator('button:has-text("Hotspot Analysis")');
  if (await hotspotBtn.isVisible()) await hotspotBtn.click();
  await page.waitForTimeout(2000);
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-027_codebase-memory-graph-vector/assets/lsars-hotspot-analysis.png'
  });
};

// T-027 Asset 3: Health Risk Advisor chatbot open
// Shows: AI-powered chat interface — the agent surface built on codebase memory
const T027_chatbot = async (page) => {
  await page.goto('http://localhost:3230');
  await page.waitForTimeout(2000);
  const enterBtn = page.locator('button:has-text("Enter System")');
  if (await enterBtn.isVisible()) await enterBtn.click();
  await page.waitForTimeout(1000);
  // Open the chatbot
  const chatBtn = page.locator('button:has-text("Open LSA Health Risk Advisor")');
  if (await chatBtn.isVisible()) await chatBtn.click();
  await page.waitForTimeout(2000);
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-027_codebase-memory-graph-vector/assets/lsars-health-risk-advisor.png'
  });
};


// ============================================================
// T-029: Context Window as 4MB RAM
// Assets: Context compression, AGENTS.md, checkpoint
// ============================================================

// T-029 Asset 1: Welcome modal (compact context summary of the whole app)
const T029_welcome_context = async (page) => {
  await page.goto('http://localhost:3230');
  await page.waitForTimeout(2000);
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-029_context-window-4mb-ram/assets/lsars-welcome-context-summary.png'
  });
};

// T-029 Asset 2: ZIP search showing direct navigation (efficient context use)
const T029_zip_search = async (page) => {
  await page.goto('http://localhost:3230');
  await page.waitForTimeout(2000);
  const enterBtn = page.locator('button:has-text("Enter System")');
  if (await enterBtn.isVisible()) await enterBtn.click();
  await page.waitForTimeout(1000);
  // Type a ZIP code
  const zipInput = page.locator('input[placeholder="12345"]');
  await zipInput.fill('02101');
  await page.locator('button:has-text("Go")').first().click();
  await page.waitForTimeout(3000);
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-029_context-window-4mb-ram/assets/lsars-zip-search-boston.png'
  });
};

// T-029 Asset 3: Full page with all UI panels visible
const T029_full_ui = async (page) => {
  await page.goto('http://localhost:3230');
  await page.waitForTimeout(2000);
  const enterBtn = page.locator('button:has-text("Enter System")');
  if (await enterBtn.isVisible()) await enterBtn.click();
  await page.waitForTimeout(1000);
  await page.selectOption('select', 'New York');
  await page.waitForTimeout(3000);
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-029_context-window-4mb-ram/assets/lsars-ny-full-ui.png',
    fullPage: true
  });
};


// ============================================================
// T-032: Agent Evaluation Harness
// Assets: HARP2 parity, regression tests, golden tasks
// ============================================================

// T-032 Asset 1: LSARS with EPA methodology (shows the calculation system being validated)
const T032_epa_methodology = async (page) => {
  await page.goto('http://localhost:3230');
  await page.waitForTimeout(2000);
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-032_agent-evaluation-harness/assets/lsars-methodology-selector.png'
  });
};

// T-032 Asset 2: State with risk data loaded (the output being validated against HARP2)
const T032_risk_data = async (page) => {
  await page.goto('http://localhost:3230');
  await page.waitForTimeout(2000);
  const enterBtn = page.locator('button:has-text("Enter System")');
  if (await enterBtn.isVisible()) await enterBtn.click();
  await page.waitForTimeout(1000);
  await page.selectOption('select', 'California');
  await page.waitForTimeout(3000);
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-032_agent-evaluation-harness/assets/lsars-ca-risk-data.png'
  });
};


// ============================================================
// T-033: Agent Observability & Tracing
// Assets: Trace timeline, structured logs, 4-layer architecture
// ============================================================

// T-033 Asset 1: Map with zoom info (shows the layered architecture in action)
const T033_layered_view = async (page) => {
  await page.goto('http://localhost:3230');
  await page.waitForTimeout(2000);
  const enterBtn = page.locator('button:has-text("Enter System")');
  if (await enterBtn.isVisible()) await enterBtn.click();
  await page.waitForTimeout(1000);
  await page.selectOption('select', 'Pennsylvania');
  await page.waitForTimeout(3000);
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-033_agent-observability-tracing/assets/lsars-pa-layered-architecture.png'
  });
};

// T-033 Asset 2: Chatbot showing request/response (observable agent interaction)
const T033_chatbot_trace = async (page) => {
  await page.goto('http://localhost:3230');
  await page.waitForTimeout(2000);
  const enterBtn = page.locator('button:has-text("Enter System")');
  if (await enterBtn.isVisible()) await enterBtn.click();
  await page.waitForTimeout(1000);
  const chatBtn = page.locator('button:has-text("Open LSA Health Risk Advisor")');
  if (await chatBtn.isVisible()) await chatBtn.click();
  await page.waitForTimeout(2000);
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-033_agent-observability-tracing/assets/lsars-chatbot-observable.png'
  });
};


// ============================================================
// T-039: Sandboxed Tool Execution Policy
// Assets: Network isolation, Docker microservices, tool policy
// ============================================================

// T-039 Asset 1: Full app (demonstrates the microservice architecture being sandboxed)
const T039_full_app = async (page) => {
  await page.goto('http://localhost:3230');
  await page.waitForTimeout(2000);
  const enterBtn = page.locator('button:has-text("Enter System")');
  if (await enterBtn.isVisible()) await enterBtn.click();
  await page.waitForTimeout(1000);
  await page.selectOption('select', 'Florida');
  await page.waitForTimeout(3000);
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-039_sandboxed-tool-execution-policy/assets/lsars-fl-sandboxed-app.png'
  });
};

// T-039 Asset 2: Welcome modal showing the isolated entry point
const T039_entry_point = async (page) => {
  await page.goto('http://localhost:3230');
  await page.waitForTimeout(2000);
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-039_sandboxed-tool-execution-policy/assets/lsars-sandboxed-entry.png'
  });
};
