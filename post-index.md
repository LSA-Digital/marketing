# Post Index

| Post ID    | Name                                                                               | Link                                                                                                               | Status | Type     | Product    | Depends On | Dependency Name                                        |
| ---------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------ | -------- | ---------- | ---------- | ------------------------------------------------------ |
| 2026-B-001 | Trust Through Auditable AI                                                         | [post](posts/2026/02/2026-02-04_auditable-ai-trust/post-auditable-ai-trust-2026-B-001.md)                             | draft  | business | LSARS, HRA | —         | —                                                     |
| 2026-T-001 | How We Built Auditable AI                                                          | [post](posts/2026/02/2026-02-04_auditable-ai-implementation/post-auditable-ai-implementation-2026-T-001.md)           | draft  | tech     | LSARS, HRA | 2026-B-001 | Trust Through Auditable AI                             |
| 2026-B-002 | Permit dates aren't dates. They're probabilities.                                  | [post](posts/2026/02/2026-02-04_permitability-score/post-permitability-score-2026-B-002.md)                           | draft  | business | LSARS      | —         | —                                                     |
| 2026-T-002 | Stop shipping "confidence." Ship bounds + drivers.                                 | [post](posts/2026/02/2026-02-04_uncertainty-bounds-drivers/post-uncertainty-bounds-drivers-2026-T-002.md)             | draft  | tech     | LSARS      | 2026-B-002 | Permit dates aren't dates. They're probabilities.      |
| 2026-B-003 | Data Center Permit Fights Aren't About Pollutants—They're About Trust             | [post](posts/2026/02/2026-02-04_data-center-permit-trust/post-data-center-permit-trust-2026-B-003.md)                 | draft  | business | LSARS      | —         | —                                                     |
| 2026-B-004 | Regulatory Alignment Isn't One-Size-Fits-All—That's the Point                     | [post](posts/2026/02/2026-02-04_regulatory-alignment/post-regulatory-alignment-2026-B-004.md)                         | draft  | business | LSARS, HRA | —         | —                                                     |
| 2026-T-003 | Unit Tests Aren't Enough When Correctness Is the Whole Point                       | [post](posts/2026/02/2026-02-04_gold-standard-validation/post-gold-standard-validation-2026-T-003.md)                 | draft  | tech     | LSARS, HRA | 2026-B-004 | Regulatory Alignment Isn't One-Size-Fits-All           |
| 2026-B-005 | Flexible, faster permit options - over 100x the speed!                             | [post](posts/2026/02/2026-02-04_permit-scenarios-faster-cheaper/post-permit-scenarios-faster-cheaper-2026-B-005.md)   | draft  | business | LSARS      | —         | —                                                     |
| 2026-T-004 | Reinforcement learning for mitigation strategy discovery—only if it’s auditable. | [post](posts/2026/02/2026-02-04_mitigation-strategy-optimization/post-mitigation-strategy-optimization-2026-T-004.md) | draft  | tech     | LSARS      | 2026-B-005 | Flexible, faster permit options - over 100x the speed! |
| 2026-B-006 | Governments can do more with less—without buying new software                       | [post](posts/2026/02/2026-02-04_governments-more-done-with-less/post-governments-more-done-with-less-2026-B-006.md)    | draft  | business | LSARS      | —         | —                                                     |
| 2026-T-005 | Route questions by data priority (highest-confidence first)                         | [post](posts/2026/02/2026-02-04_data-priority-routing/post-data-priority-routing-2026-T-005.md)                        | draft  | tech     | LSARS      | 2026-B-006 | Governments can do more with less—without buying new software |
| 2026-B-007 | Regulatory transparency that reviewers can verify                                   | [post](posts/2026/02/2026-02-04_regulatory-transparency-reports/post-regulatory-transparency-reports-2026-B-007.md)    | draft  | business | LSARS      | —         | —                                                     |
| 2026-T-006 | Data manifests beat implicit semantics                                               | [post](posts/2026/02/2026-02-04_data-manifest/post-data-manifest-2026-T-006.md)                                        | draft  | tech     | LSARS      | 2026-B-007 | Regulatory transparency that reviewers can verify      |

---

## Instructions for Post Index Maintenance

### Post ID System

**Format**: `YYYY-T-NNN`

| Component | Meaning           | Values                                               |
| --------- | ----------------- | ---------------------------------------------------- |
| `YYYY`  | Year              | 2026, 2027, ...                                      |
| `T`     | Type/Channel      | `B` = Business (LSARS), `T` = Tech (LSA Digital) |
| `NNN`   | Sequential number | 001, 002, ... (resets each year per type)            |

**Next IDs**:

- Next business post:`2026-B-008`
- Next tech post:`2026-T-007`

### Channel Strategy

| Type                   | Channel     | LinkedIn Page                                                                | Audience                                                     | Content Focus                                                      |
| ---------------------- | ----------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------ |
| **B** (Business) | LSARS       | [linkedin.com/company/lsars](https://www.linkedin.com/company/lsars)            | Permit requestors, regulators, community leaders, executives | "What we do" — outcomes, trust, stakeholder value                 |
| **T** (Tech)     | LSA Digital | [linkedin.com/company/lsadigital](https://www.linkedin.com/company/lsadigital/) | AI/tech audience, architects, engineers, QA                  | "How we did it" — AI best practices, architecture, implementation |

**Dependency pattern**: Tech posts (`T`) typically repost/expand on a business post (`B`) to show the implementation behind the outcome. The `Depends On` column links them.

### Workflow

1. **Create business post** (`B`) for LSARS channel — focus on stakeholder outcomes
2. **Create tech post** (`T`) for LSA Digital channel — reference business post, explain "how"

### Status Definitions

| Status        | Meaning                              |
| ------------- | ------------------------------------ |
| `draft`     | Initial creation, not yet reviewed   |
| `in_review` | Sent to SME reviewer(s) for feedback |
| `approved`  | SME approved, ready to publish       |
| `published` | Live on LinkedIn                     |

### Adding a Post

Use `/new-post` command, which will:

1. Create the post folder and file
2. Add a row to the Post Index table above
3. Increment the "Next IDs" counters

### Related Files

- `posts/README.md` — folder structure standards
- `lsaProductExpertAlignment.md` — SME reviewers and tagging rules
- `marketingCampaignFeb2026.md` — campaign context and goals
