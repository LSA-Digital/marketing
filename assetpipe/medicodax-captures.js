/**
 * MEDICODAX / HAI-EM Screenshot Captures
 * Product: Human-AI E&M Coder (localhost:3000)
 * Auth: Auto-login (no action needed)
 *
 * Each export is an `async (page) => { ... }` function compatible with
 * Playwright MCP's browser_run_code.
 *
 * Posts served: T-019, T-020, T-035
 *
 * Usage via Playwright MCP:
 *   skill_mcp(mcp_name="playwright", tool_name="browser_run_code",
 *     arguments={ "code": "<paste function body>" })
 */

// ============================================================
// T-019: MEDICODAX JWT & Multi-EHR
// Assets: JWT flow, token lifecycle, FHIR access control
// ============================================================

// T-019 Asset 1: Dashboard showing EHR integration (Epic sync visible)
// Shows: Time savings metrics, record count, EHR sync status
const T019_dashboard = async (page) => {
  await page.goto('http://localhost:3000/dashboard');
  await page.waitForTimeout(3000);
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-019_medicoda-jwt-multi-ehr/assets/medicoda-dashboard-ehr-integration.png'
  });
};

// T-019 Asset 2: Audit Logs showing secure access trail
// Shows: Timestamped audit entries — evidence of JWT-secured operations
const T019_audit_logs = async (page) => {
  await page.goto('http://localhost:3000/audit-logs');
  await page.waitForTimeout(3000);
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-019_medicoda-jwt-multi-ehr/assets/medicoda-audit-logs-security.png'
  });
};

// T-019 Asset 3: User menu showing authenticated user context
// Shows: User identity, role (Certified Coder), EHR connection
const T019_user_context = async (page) => {
  await page.goto('http://localhost:3000/dashboard');
  await page.waitForTimeout(2000);
  // Click user menu to show auth context
  const userMenu = page.locator('button:has-text("User menu")');
  if (await userMenu.isVisible()) await userMenu.click();
  await page.waitForTimeout(1000);
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-019_medicoda-jwt-multi-ehr/assets/medicoda-user-auth-context.png'
  });
};


// ============================================================
// T-020: Dynamic Workflow Adaptation
// Assets: 3-step pipeline, voice vs direct entry, audit logging
// ============================================================

// T-020 Asset 1: Dashboard with time savings and record overview
// Shows: The AI pipeline output — time savings metrics, pending submissions
const T020_dashboard_metrics = async (page) => {
  await page.goto('http://localhost:3000/dashboard');
  await page.waitForTimeout(3000);
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-020_medicoda-dynamic-workflow-adaptation/assets/medicoda-dashboard-time-savings.png'
  });
};

// T-020 Asset 2: Mobile Queue (voice submission path)
// Shows: MobileEMNote submissions from iPhone — the voice workflow branch
const T020_mobile_queue = async (page) => {
  await page.goto('http://localhost:3000/mobile-queue');
  await page.waitForTimeout(3000);
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-020_medicoda-dynamic-workflow-adaptation/assets/medicoda-mobile-queue-voice.png'
  });
};

// T-020 Asset 3: New E&M Record wizard (direct entry path)
// Shows: The structured entry workflow — EMClaimPacket path
const T020_wizard = async (page) => {
  await page.goto('http://localhost:3000/wizard-v2');
  await page.waitForTimeout(3000);
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-020_medicoda-dynamic-workflow-adaptation/assets/medicoda-wizard-direct-entry.png'
  });
};


// ============================================================
// T-035: HITL UX Patterns at Scale
// Assets: Review queue, agent evidence, stakeholder-ready UI
// ============================================================

// T-035 Asset 1: Dashboard with AI agent sidebar (Claims Defender, Missing Docs)
// Shows: HITL pattern — AI agents as assistants, not replacements
const T035_agent_sidebar = async (page) => {
  await page.goto('http://localhost:3000/dashboard');
  await page.waitForTimeout(3000);
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-035_hitl-ux-patterns-scale/assets/medicoda-agent-sidebar-hitl.png'
  });
};

// T-035 Asset 2: Claims Defender panel open (AI Denial Defense)
// Shows: Agent presenting evidence for human review
const T035_claims_defender = async (page) => {
  await page.goto('http://localhost:3000/dashboard');
  await page.waitForTimeout(2000);
  // Click Claims Defender sidebar button
  const claimsBtn = page.locator('button:has-text("Claims Defender")');
  if (await claimsBtn.isVisible()) await claimsBtn.click();
  await page.waitForTimeout(2000);
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-035_hitl-ux-patterns-scale/assets/medicoda-claims-defender-evidence.png'
  });
};

// T-035 Asset 3: Missing Docs Agent panel (Documentation Tracker)
// Shows: Agent identifying gaps, human reviews and acts
const T035_missing_docs = async (page) => {
  await page.goto('http://localhost:3000/dashboard');
  await page.waitForTimeout(2000);
  // Click Missing Docs Agent sidebar button
  const docsBtn = page.locator('button:has-text("Missing Docs Agent")');
  if (await docsBtn.isVisible()) await docsBtn.click();
  await page.waitForTimeout(2000);
  await page.screenshot({
    path: 'posts/2026/02/2026-02-15_2026-T-035_hitl-ux-patterns-scale/assets/medicoda-missing-docs-tracker.png'
  });
};
