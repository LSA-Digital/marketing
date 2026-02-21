# Production Runtime Sandboxing: Hardening the Agent Boundary

## Metadata
- **Post ID**: 2026-T-039
- **Audience**: tech
- **Product**: LSARS, HSRA
- **Themes**: TECH_SECURITY, AGENTICAI_DEVOPS
- **Expert**: Mike, Keith
- **Depends On**: —
- **Dependency Name**: —
- **Relationship**: Per-tool policy enforcement + ephemeral credentials + isolated execution for production agents
- **Assets**: lsars-fl-sandboxed-app.png, lsars-sandboxed-entry.png
- **CTA**: book a working session at [lsadigital.com](https://lsadigital.com)

## Post

While a development sandbox is for exploration, a production sandbox is for enforcement. In Vibe Engineering, we use vibe coding for rapid exploration, but we rely on production-grade engineering to ensure that runtime execution is safe, predictable, and isolated. When agents move from Continuous Exploration (CE) into live CI/CD environments, the tool boundary must be impenetrable.

Our production architecture for LSARS/HSRA utilizes 9 Docker microservices with strict network isolation. This isn't just about security; it's about ensuring that complex calculations—like the validation of 797 pollutants for HARP2 parity—happen in a controlled environment where side effects are impossible.

**Production Sandbox Enforcement Rules:**
- **Network Egress Control:** We block all arbitrary outbound calls. Agents can only interact with the specific internal services they are authorized to use.
- **Ephemeral Scoped Credentials:** Tools operate using short-lived tokens that are scoped to the minimum permissions required for the task.
- **Execution Isolation:** Every tool call runs in a constrained runtime with a limited blast radius. If a tool fails or is compromised, the rest of the system remains unaffected.
- **Audit Logging by Default:** Every action is recorded with request ID correlation, connecting the agent's intent to the specific policy decision and outcome.

With over 2,669 test functions validating these boundaries, we ensure that "be careful" is never our only line of defense. Safety is built into the infrastructure, not the prompt.

## Artifacts
- Remote:
  - https://lsadigital.com

## Post asset ideas
- [ ] Diagram: Network isolation between the 9 Docker microservices
- [ ] Example: A production tool policy (JSON) showing egress blocks
- [ ] Trace view: Request ID correlation across microservice boundaries

### Screenshots

![LSARS with Florida loaded — the microservice architecture running in sandboxed Docker containers](assets/lsars-fl-sandboxed-app.png)
*LSARS with Florida loaded — microservice architecture running in sandboxed Docker containers*

![Welcome modal showing the isolated application entry point](assets/lsars-sandboxed-entry.png)
*Welcome modal — isolated application entry point*
