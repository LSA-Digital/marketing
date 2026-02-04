# Post Index

| Post ID | Name | Link | Status | Type | Product | Publish Target | Depends On | Dependency Name |
|---------|------|------|--------|------|---------|----------------|------------|-----------------|
| 2026-B-001 | Trust Through Auditable AI | [post](posts/2026/02/2026-02-04_auditable-ai-trust/post-auditable-ai-trust-2026-B-001.md) | draft | business | LSARS, HRA | 2026-02-07 | — | — |
| 2026-T-001 | How We Built Auditable AI | [post](posts/2026/02/2026-02-04_auditable-ai-implementation/post-auditable-ai-implementation-2026-T-001.md) | draft | tech | LSARS, HRA | 2026-02-10 | 2026-B-001 | Trust Through Auditable AI |
| 2026-B-002 | Permit dates aren’t dates. They’re probabilities. | [post](posts/2026/02/2026-02-04_permitability-score/post-permitability-score-2026-B-002.md) | draft | business | LSARS | 2026-02-11 | — | — |
| 2026-T-002 | Stop shipping “confidence.” Ship bounds + drivers. | [post](posts/2026/02/2026-02-04_uncertainty-bounds-drivers/post-uncertainty-bounds-drivers-2026-T-002.md) | draft | tech | LSARS | 2026-02-13 | 2026-B-002 | Permit dates aren’t dates. They’re probabilities. |

---

## Instructions for Post Index Maintenance

### Post ID System

**Format**: `YYYY-T-NNN`

| Component | Meaning | Values |
|-----------|---------|--------|
| `YYYY` | Year | 2026, 2027, ... |
| `T` | Type/Channel | `B` = Business (LSARS), `T` = Tech (LSA Digital) |
| `NNN` | Sequential number | 001, 002, ... (resets each year per type) |

**Next IDs**:
- Next business post: `2026-B-003`
- Next tech post: `2026-T-003`

### Channel Strategy

| Type | Channel | LinkedIn Page | Audience | Content Focus |
|------|---------|---------------|----------|---------------|
| **B** (Business) | LSARS | [linkedin.com/company/lsars](https://www.linkedin.com/company/lsars) | Permit requestors, regulators, community leaders, executives | "What we do" — outcomes, trust, stakeholder value |
| **T** (Tech) | LSA Digital | [linkedin.com/company/lsadigital](https://www.linkedin.com/company/lsadigital/) | AI/tech audience, architects, engineers, QA | "How we did it" — AI best practices, architecture, implementation |

**Dependency pattern**: Tech posts (`T`) typically repost/expand on a business post (`B`) to show the implementation behind the outcome. The `Depends On` column links them.

### Workflow

1. **Create business post** (`B`) for LSARS channel — focus on stakeholder outcomes
2. **Publish business post** to LSARS LinkedIn
3. **Create tech post** (`T`) for LSA Digital channel — reference business post, explain "how"
4. **Publish tech post** to LSA Digital LinkedIn (typically 2-3 days after business post)

### Status Definitions

| Status | Meaning |
|--------|---------|
| `draft` | Initial creation, not yet reviewed |
| `in_review` | Sent to SME reviewer(s) for feedback |
| `approved` | SME approved, ready to publish |
| `published` | Live on LinkedIn |

### Adding a Post

Use `/new-post` command, which will:
1. Create the post folder and file
2. Add a row to the Post Index table above
3. Increment the "Next IDs" counters

### Related Files

- `posts/README.md` — folder structure standards
- `lsaProductExpertAlignment.md` — SME reviewers and tagging rules
- `marketingCampaignFeb2026.md` — campaign context and goals
