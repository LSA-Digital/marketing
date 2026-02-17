# The Golden Rule of Security: No Evidence, No Fix

## Metadata
- **Post ID**: 2026-T-041
- **CTA**: book a working session at [lsadigital.com](https://lsadigital.com)

## Post

In the world of Vibe Engineering, we move fast by using vibe coding for exploration, but we never compromise on the production-grade engineering required for security. One of our simplest and most non-negotiable rules is this: a security bug is not considered "fixed" until the verification evidence is shipped and documented.

We don't rely on verbal assurances or "it looks good" Slack messages. Every security vulnerability must be tracked in Jira with a complete audit trail. This discipline ensures that our Continuous Integration (CI/CD) pipeline remains a source of truth, not just a series of successful builds.

**The Security Fix Ticket Template:**
- **Impact + Scope:** A clear definition of what was at risk and what data or systems were potentially exposed.
- **Root Cause Analysis:** A technical breakdown of why the bug existed in the first place.
- **Fix Summary:** A description of the code changes and why they effectively close the vulnerability.
- **Verification Evidence:** The most critical part. This includes automated test results, reproduction logs, or screenshots that prove the fix works as intended.
- **Deployment Note:** Precise details on when and where the fix was deployed to production.

By requiring this level of detail for every security bug, we eliminate security debt and ensure that our systems remain compliant and resilient under pressure.

## Artifacts
- Remote:
  - https://lsadigital.com

## Post asset ideas
- [ ] Jira ticket template for security bug reporting
- [ ] Example: A redacted "Verification Evidence" section from a real fix
- [ ] Checklist: 5 things every security fix must include before closing

### Template: Jira Security Bug Report

```markdown
## Security Bug Report
**Severity:** [Critical/High/Medium/Low]
**Component:** [service name]
**Discovery:** [How found - scan/pentest/code review/incident]

### Impact
[What can an attacker do? What data is at risk?]

### Root Cause
[Technical explanation of the vulnerability]

### Fix Summary
[What was changed and why]

### Verification Evidence
- [ ] Unit test added covering the fix
- [ ] Integration test verifying the attack vector is blocked
- [ ] Security scan passes (no new findings)
- [ ] PR reviewed by security-aware engineer
- [ ] Deployed to staging, verified manually

### Deployment Note
[Any special deployment steps, feature flags, rollback plan]
```

### Checklist: Security Fix Closure Requirements

- [ ] Root cause identified (not just symptom patched)
- [ ] Regression test added (proves the fix works and prevents reintroduction)
- [ ] Related code audited (same pattern elsewhere?)
- [ ] Security scan clean (no new vulnerabilities introduced)
- [ ] Post-mortem documented (what happened, why, how to prevent)

### Code: Redacted Verification Evidence (EPMS MCP Auth Pattern)

```python
class TestMCPAuthenticationDenied:
    """Test that MCP endpoints deny access without proper authentication."""

    def test_mcp_info_with_invalid_token(self):
        response = requests.get(
            f"{MCP_BASE_URL}/",
            headers={"Authorization": "Bearer [REDACTED_INVALID_TOKEN]"},
        )

        assert response.status_code == 401
```
