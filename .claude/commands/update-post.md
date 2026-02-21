# Update Post

Update any post-level field through Squawk MCP.

## Usage
`/update-post <post-id> <field> <value>`

## Examples
- `/update-post 2026-B-001 status approved`
- `/update-post 2026-T-013 expert "Mike, Keith"`
- `/update-post 2026-B-006 product "LSARS, HSRA"`
- `/update-post 2026-B-014 themes "DASHBOARD_ACCOUNTABILITY, COMMUNITY_TRANSPARENCY"`
- `/update-post 2026-T-001 depends-on 2026-B-001`
- `/update-post 2026-B-006 content` (re-ingest post file)

## Supported Fields

| Field | Squawk Tool | Notes |
|-------|------------|-------|
| status | Conditional | Maps to Squawk actions (see below) |
| expert | update_post_draft | Resolve name → CUID from lookup table |
| product | update_post_draft | Resolve name → CUID from lookup table |
| themes | upsert_document_draft | Re-ingest with updated referenceContext.themes |
| depends-on | update_post_draft | Resolve target post ID → post CUID |
| content | upsert_document_draft | Re-ingest the post file to update extracted text |

## Status Transitions

| Status Value | Squawk Action | Precondition |
|-------------|--------------|--------------|
| draft | No Squawk action | — |
| in_review | No Squawk action | — |
| approved | approve_content_item | readinessScore MUST be "ready" |
| published | No Squawk action | Must already be APPROVED |

## Instructions

When the user invokes this command:

### 1. Parse args
- `post-id`: Required. Format: 2026-B-NNN or 2026-T-NNN
- `field`: Required. One of: status, expert, product, themes, depends-on, content
- `value`: Required. The new value.

### 2. Resolve post CUID
To call Squawk MCP, you need the document CUID and post CUID for the given post-id.
Use the CUID mapping table below, or query Squawk:
```
execute_tool("squawk.list_review_queue", {"includeApproved": true, "limit": 100})
```
Search the response for the item matching the post-id in its title or metadata.

### 3. Execute the update

**For `status` field:**
- If value = "approved":
  1. FIRST check readiness: `execute_tool("squawk.get_content_item", {"id": "<document-cuid>", "itemType": "document"})`
  2. Check readinessScore in response
  3. If readinessScore ≠ "ready": **REFUSE** with message: "Cannot approve: readiness is '{score}'. Address readiness issues first. Check readinessSummary for guidance."
  4. If readinessScore = "ready": `execute_tool("squawk.approve_content_item", {"id": "<document-cuid>"})`
- If value = "draft" or "in_review" or "published": No Squawk action needed. Confirm the status change.

**For `expert` field:**
```
execute_tool("squawk.update_post_draft", {
  "postId": "<post-cuid>",
  "expertId": "<expert-cuid-from-table>"
})
```

**For `product` field:**
```
execute_tool("squawk.update_post_draft", {
  "postId": "<post-cuid>",
  "productId": "<product-cuid-from-table>"
})
```

**For `themes` field:**
Re-ingest the post with updated themes:
```
execute_tool("squawk.upsert_document_draft", {
  "filePath": "posts/2026/02/<folder>/post-<slug>-<postid>.md",
  "referenceContext": {
    "postId": "<post-id>",
    "themes": "<new-theme-tags>"
  }
})
```

**For `depends-on` field:**
1. Resolve the dependency post-id to its post CUID (use CUID mapping or list_review_queue)
2. Execute:
```
execute_tool("squawk.update_post_draft", {
  "postId": "<post-cuid>",
  "dependsOnPostId": "<dependency-post-cuid>"
})
```

**For `content` field:**
Re-ingest the post file:
```
execute_tool("squawk.upsert_document_draft", {
  "filePath": "posts/2026/02/<folder>/post-<slug>-<postid>.md",
  "referenceContext": {
    "postId": "<post-id>"
  }
})
```

### 4. Verify the update
```
execute_tool("squawk.get_content_item", {"id": "<document-cuid>", "itemType": "document"})
```
Confirm the field was updated in the response.

### 5. Suggest index rebuild
After any update, suggest: "Run `node scripts/build-squawk-index.js` to refresh squawk-index.md."

## Expert CUIDs

| Expert | CUID |
|--------|------|
| Keith Mangold | cml8m3t3e00020ys4ml0dfbl8 |
| Mike Idengren | cmksysncp000c67s4v38u04d0 |
| Nelson Smith | cmksysdl4000a67s4m1u7625r |
| Thad Perry | cmksysl3d000b67s4rd4kuhbq |

## Product CUIDs

| Product | CUID |
|---------|------|
| LSARS Permit Intelligence | cmksy89a7000367s4e634xb3k |
| Health Risk Assessment (HSRA) | cml77dhiy000g623jup13ylgk |
| EPMS | cmlqx3cm3000hh8s4ujarwpcx |
| ReimagineIt | cmksy7vqw000267s45kk14jq3 |
| MEDICODAX | cmlqx2xq1000gh8s4vkijzvid |
| Human-AI Concept Lab | cmlqx3u2q000ih8s4xcorgqim |

## CUID Mapping (Post ID → Document CUID)

| Post ID | Document CUID |
|---------|---------------|
| 2026-B-001 | cmla2aisk002kqk3jypq1n0wl |
| 2026-T-001 | cmla416ds0038qk3jxq4sgb3g |
| 2026-B-002 | cmla2budz002mqk3jwwavd2uy |
| 2026-T-002 | cmla42gnc003aqk3j1ly3vfti |
| 2026-B-003 | cmla2db1y002oqk3jo5seogpx |
| 2026-T-003 | cmla43rpr003cqk3jvp6r4ave |
| 2026-B-004 | cmla2f91z002qqk3jj9gvfpd0 |
| 2026-B-005 | cmla2grdq002sqk3j0gqtdlad |
| 2026-T-004 | cmla451pz003eqk3jtwbd5p7j |
| 2026-B-006 | cmla2idd2002uqk3jd93a6iq4 |
| 2026-T-005 | cmla469s6003gqk3jrs2ojysp |
| 2026-B-007 | cmla2jr4j002wqk3jdrwsrhma |
| 2026-T-006 | cmla47pai003iqk3j126wurji |
| 2026-B-008 | cmlldih7z001aq7s4ymrip3w3 |
| 2026-T-008 | cmla491yk003kqk3jm4o5wkf0 |
| 2026-B-009 | cmlldjdft001cq7s41w6llife |
| 2026-T-009 | cmlldkqu9001gq7s478kh37lp |
| 2026-B-010 | cmlldk3bq001eq7s4sqafs50t |
| 2026-T-010 | cmlldlemw001iq7s4w6dvt059 |
| 2026-B-011 | cmla3u662002yqk3jsbtlglwz |
| 2026-T-011 | cmla4abku003mqk3ja7swehax |
| 2026-B-012 | cmla3vfy50030qk3jhjntqgh0 |
| 2026-T-012 | cmla4bpkq003oqk3jlt8hil4o |
| 2026-B-013 | cmla3wtgc0032qk3jcvou3vx0 |
| 2026-T-013 | cmla4d1rh003qqk3jm8iknja6 |
| 2026-B-014 | cmla3ydeh0034qk3jeeugq26v |
| 2026-T-014 | cmla4ets3003sqk3jo9c5s5sk |
| 2026-B-015 | cmla3zqvn0036qk3jxxclenpj |
| 2026-T-015 | cmla4gfin003uqk3j4c47i8rl |
| 2026-B-016 | cmlvbruo0000004lbdu6ci88e |
| 2026-B-017 | cmlvgl8fr000304l4pqaaa7qc |
| 2026-B-018 | cmlvglrtb000604l4vi4fvavg |
| 2026-B-019 | cmlvgmeun000904l4tcjcg2cy |
| 2026-B-020 | cmlldm6d3001kq7s4rfuutxk9 |
| 2026-B-021 | cmlvgnznu000c04l4uz99nlte |
| 2026-B-022 | cmlmj2yd800226gs49ic4xthf |
| 2026-B-023 | cmlmj3je800256gs4uvesyi3j |
| 2026-B-024 | cmlmj41p000286gs4xr1bswgu |
| 2026-B-025 | cmlvgqidg000f04l48mqizwdh |
| 2026-B-026 | cmlmly411001hbzs4ux0rihl9 |
| 2026-B-027 | cmlmlyn99001kbzs49kb4rq8x |
| 2026-B-028 | cmlmlz417001nbzs4bi4v0d7n |
| 2026-B-029 | cmlvirqai000i04l4fxmznbmw |
| 2026-B-030 | cmlvis9y1000l04l40ftntlqo |
| 2026-B-031 | cmlvisuk8000o04l4hgseu5ar |
| 2026-B-032 | cmlmlznm8001qbzs4jgep40pi |
| 2026-B-033 | cmlmm06u0001tbzs43ube312u |
| 2026-B-034 | cmlviuq41000r04l43zac9uir |
| 2026-B-035 | cmlvivcb5000u04l44c8cq35o |
| 2026-T-016 | cmlvj1ft1000x04l4tiq65kmd |
| 2026-B-036 | cmlvj1wmh001004l4avx2mdti |
| 2026-T-017 | cmlo55m0u002gxds4b1xc8a36 |
| 2026-T-018 | cmlvbs7x7000104lbbvyoz41w |
| 2026-T-019 | cmlvj3xky001304l467xp03q1 |
| 2026-T-020 | cmlvj4gb8001604l4xnkg2rf1 |
| 2026-T-021 | cmlvj56c6001904l4rfmbm5at |
| 2026-T-022 | cmlvj5nll001c04l4tty4zuzm |
| 2026-T-023 | cmlvj6blm001f04l4h1zph36j |
| 2026-T-024 | cmlvj6uq7001i04l4kr9rs17z |
| 2026-T-025 | cmlvj7iqr001l04l4datg9u6b |
| 2026-T-026 | cmlvj7xhu001o04l4sccvdnlu |
| 2026-T-027 | cmlvj8oa4001r04l4l6p5g9ye |
| 2026-T-028 | cmlvj9716001u04l4tbm05qjd |
| 2026-T-029 | cmlvj9vz8001x04l4zpcj3eq4 |
| 2026-T-030 | cmlo56x6i002jxds4mkjuj075 |
| 2026-T-031 | cmlvjazyt002004l41w8uab58 |
| 2026-T-032 | cmlvjbgbu002304l4yb7wjvst |
| 2026-T-033 | cmlvjc6j1002604l4cqa94wiq |
| 2026-T-034 | cmlvjckx3002904l40nn1or17 |
| 2026-T-035 | cmlvjdae4002c04l4jf4ie75g |
| 2026-T-036 | cmlvjdobk002f04l4urp2jz4q |
| 2026-T-037 | cmlvjecnd002i04l4ih95r644 |
| 2026-T-038 | cmlvjese9002l04l478tpfpcp |
| 2026-T-039 | cmlvjfhy3002o04l4h7uxogy1 |
| 2026-T-040 | cmlvjfveq002r04l4g3r1r9m1 |
| 2026-T-041 | cmlvjgl7i002u04l43y9tdp9r |
| 2026-T-042 | cmlvjh2e4002x04l4mphv36dc |
| 2026-T-043 | cmlvjhp40003004l4fcmihzrz |
| 2026-B-037 | cmlvji9e4003304l4h46ds1iu |
| 2026-T-044 | cmlvjj489003604l4f8cgsqvo |
| 2026-B-038 | cmlvjjpfq000004kv3b4f2xic |
| 2026-T-045 | cmlvjkcsb000304kvdmxigw5j |

Valid status values: draft, in_review, approved, published
