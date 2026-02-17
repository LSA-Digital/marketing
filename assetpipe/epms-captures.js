/**
 * EPMS Screenshot Captures
 * Product: Enterprise Product Management System (localhost:5173)
 * Auth: Proxy auth bypass via REMOTE_USER header (see setup below)
 *
 * CRITICAL: Before running any capture, set the auth header:
 *   await page.setExtraHTTPHeaders({ 'REMOTE_USER': 'admin@lsadigital.com' });
 *
 * Each export is an `async (page) => { ... }` function compatible with
 * Playwright MCP's browser_run_code.
 *
 * Posts served: T-017, T-018, T-021, T-022, T-038
 *
 * Usage via Playwright MCP:
 *   skill_mcp(mcp_name="playwright", tool_name="browser_run_code",
 *     arguments={ "code": "<paste function body>" })
 */

// ============================================================
// Auth Setup — MUST run before any EPMS capture
// ============================================================

const EPMS_AUTH_SETUP = async (page) => {
  await page.setExtraHTTPHeaders({ 'REMOTE_USER': 'admin@lsadigital.com' });
};


// ============================================================
// T-017: EPMS MCP + HUX/AUX Day 0
// Assets: MCP tool definitions, 13-router architecture, Kanban
// ============================================================

// T-017 Asset 1: Kanban board showing product lifecycle
// Shows: Product management workflow — the HUX surface
const T017_kanban = async (page) => {
  await EPMS_AUTH_SETUP(page);
  await page.goto('http://localhost:5173/kanban');
  await page.waitForTimeout(3000);
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-017_epms-mcp-hux-aux-day0/assets/epms-kanban-hux.png'
  });
};

// T-017 Asset 2: Product detail view (click first product card)
// Shows: Entity relationships, artifacts, features — what MCP tools interact with
const T017_product_detail = async (page) => {
  await EPMS_AUTH_SETUP(page);
  await page.goto('http://localhost:5173/kanban');
  await page.waitForTimeout(3000);
  // Click the first product card to open detail view
  const firstCard = page.locator('[data-testid="product-card"]').first();
  if (await firstCard.isVisible()) {
    await firstCard.click();
    await page.waitForTimeout(2000);
  }
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-017_epms-mcp-hux-aux-day0/assets/epms-product-detail-entities.png'
  });
};

// T-017 Asset 3: Full page with navigation showing all routes
// Shows: The 13-router architecture visible via sidebar/nav
const T017_navigation = async (page) => {
  await EPMS_AUTH_SETUP(page);
  await page.goto('http://localhost:5173');
  await page.waitForTimeout(3000);
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-017_epms-mcp-hux-aux-day0/assets/epms-navigation-routes.png',
    fullPage: true
  });
};


// ============================================================
// T-018: HUX + AUX = CE + CI/CD
// Assets: HUX/AUX coupling, error recovery hints, system design
// ============================================================

// T-018 Asset 1: Kanban board (HUX surface)
// Shows: The human-facing product management interface
const T018_hux_surface = async (page) => {
  await EPMS_AUTH_SETUP(page);
  await page.goto('http://localhost:5173/kanban');
  await page.waitForTimeout(3000);
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-018_hux-aux-ce-ci-cd/assets/epms-hux-kanban.png'
  });
};

// T-018 Asset 2: Product detail view (the data the AUX surface accesses)
// Shows: Same data exposed differently for humans vs agents
const T018_product_data = async (page) => {
  await EPMS_AUTH_SETUP(page);
  await page.goto('http://localhost:5173/kanban');
  await page.waitForTimeout(3000);
  const firstCard = page.locator('[data-testid="product-card"]').first();
  if (await firstCard.isVisible()) {
    await firstCard.click();
    await page.waitForTimeout(2000);
  }
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-018_hux-aux-ce-ci-cd/assets/epms-product-data-hux-aux.png'
  });
};


// ============================================================
// T-021: EPMS Artifact Portal + QA
// Assets: Guest Portal, AI chat, artifact library
// ============================================================

// T-021 Asset 1: Main app showing artifact management
// Shows: The artifact library powering the guest portal
const T021_artifact_library = async (page) => {
  await EPMS_AUTH_SETUP(page);
  await page.goto('http://localhost:5173/kanban');
  await page.waitForTimeout(3000);
  // Navigate to a product to see its artifacts
  const firstCard = page.locator('[data-testid="product-card"]').first();
  if (await firstCard.isVisible()) {
    await firstCard.click();
    await page.waitForTimeout(2000);
  }
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-021_epms-artifact-portal-qa/assets/epms-artifact-library.png'
  });
};

// T-021 Asset 2: App overview with feature count
// Shows: "5 of 13 features" — staged rollout of AI-powered product management
const T021_feature_overview = async (page) => {
  await EPMS_AUTH_SETUP(page);
  await page.goto('http://localhost:5173/kanban');
  await page.waitForTimeout(3000);
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-021_epms-artifact-portal-qa/assets/epms-feature-overview.png'
  });
};


// ============================================================
// T-022: Vibe Engineering Dial (CE/CI/CD)
// Assets: Kill story visualization, dial concept, eval harness
// ============================================================

// T-022 Asset 1: Kanban showing product lifecycle (the system that survived the dial turn)
const T022_survived_system = async (page) => {
  await EPMS_AUTH_SETUP(page);
  await page.goto('http://localhost:5173/kanban');
  await page.waitForTimeout(3000);
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-022_vibe-engineering-dial-ce-ci-cd/assets/epms-kanban-survived.png'
  });
};

// T-022 Asset 2: Product detail showing structured data (what replaced the killed NL query)
const T022_structured_data = async (page) => {
  await EPMS_AUTH_SETUP(page);
  await page.goto('http://localhost:5173/kanban');
  await page.waitForTimeout(3000);
  const firstCard = page.locator('[data-testid="product-card"]').first();
  if (await firstCard.isVisible()) {
    await firstCard.click();
    await page.waitForTimeout(2000);
  }
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-022_vibe-engineering-dial-ce-ci-cd/assets/epms-structured-tools.png'
  });
};


// ============================================================
// T-038: API Design as Agent UX
// Assets: Pydantic models, MCP tool endpoints, error recovery
// ============================================================

// T-038 Asset 1: Kanban board (the UI built on the 14-tool MCP API)
const T038_api_surface = async (page) => {
  await EPMS_AUTH_SETUP(page);
  await page.goto('http://localhost:5173/kanban');
  await page.waitForTimeout(3000);
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-038_api-design-agent-ux/assets/epms-kanban-api-surface.png'
  });
};

// T-038 Asset 2: Product detail (entity relationships the API exposes)
const T038_entity_relations = async (page) => {
  await EPMS_AUTH_SETUP(page);
  await page.goto('http://localhost:5173/kanban');
  await page.waitForTimeout(3000);
  const firstCard = page.locator('[data-testid="product-card"]').first();
  if (await firstCard.isVisible()) {
    await firstCard.click();
    await page.waitForTimeout(2000);
  }
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-038_api-design-agent-ux/assets/epms-entity-relationships.png'
  });
};
