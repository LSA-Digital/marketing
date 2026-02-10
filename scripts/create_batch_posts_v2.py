import os
import datetime
import sys

posts_data = [
    {
        "id": "2026-B-016",
        "slug": "data-center-water-transparency",
        "title": "How does LSARS make water use and drought triggers transparent (potable vs reclaimed)?",
        "node_id": "11958049f2bf41cbb9cb10012d",
        "expert": "Keith Mangold + Nelson Smith",
        "product": "LSARS",
        "content": """# Water transparency that communities can verify

Verbal assurances about data center water use don't build trust—data does. When communities fear drought impact, "we promise to be efficient" isn't enough.

We built the LSARS Water Dashboard to turn drought triggers and reclamation commitments into public, verifiable records.

**How it works:**
- **Drought Triggers**: Automatic operating rule adjustments based on state drought levels.
- **Source Tracking**: Real-time split between potable and reclaimed water usage.
- **Compliance History**: Public log of cap adherence.

**Why this matters for stakeholders:**
- **Community** Stops relying on "trust us" and starts verifying.
- **Government** Automates compliance monitoring without new staff.
- **Permit Requestor** Proves responsible stewardship with hard numbers.

**Result:** Permits move faster when water impact is a known quantity, not a black box.

See the dashboard at https://lsars.com
""",
        "synopsis": "Publish a simple public water dashboard (caps, potable vs reclaimed, drought-trigger operating rules, compliance history) so the community isn't asked to rely on verbal assurances.",
    },
    {
        "id": "2026-B-017",
        "slug": "enforceable-noise-commitments",
        "title": "How does LSARS make noise commitments enforceable (decibel limits + continuous monitoring)?",
        "node_id": "2c599ff6142f434abbf782b0e3",
        "expert": "Nelson Smith + Keith Mangold",
        "product": "LSARS",
        "content": """# Make the "hum" measurable and managed

The "hum" is the #1 community fear for data centers. PDF acoustic reports don't fix it—enforceable data does.

We built continuous noise monitoring into the Permit Intelligence Portal to make decibel limits enforceable and transparent.

**How it works:**
- **Continuous Monitoring**: IoT integration for real-time decibel tracking at property lines.
- **Setback Logic**: Automated validation of acoustic design against community zoning.
- **Public Scorecards**: Red/Green status visible to residents.

**Why this matters for stakeholders:**
- **Community** Validated peace of mind, not just promises.
- **Permit Requestor** Proves compliance to avoid costly injunctions.
- **Government** Reduces noise complaint triage time.

**Result:** Noise becomes a managed metric, not a project-killing emotional argument.

Hear the difference at https://lsars.com
""",
        "synopsis": "Convert 'the hum will never stop' into measurable commitments: setbacks, acoustic design, decibel limits, continuous monitoring, and public scorecards tracked in the Permit Intelligence Portal.",
    },
    {
        "id": "2026-B-018",
        "slug": "diesel-backup-credibility",
        "title": "How does LSARS handle diesel backup generator credibility (construction + testing) with HRA baseline risk?",
        "node_id": "7458aa90612a4f1785663840db",
        "expert": "Nelson Smith + Mike Idengren",
        "product": "LSARS, HRA",
        "content": """# Credibility means counting the backup generators too

"Clean" data centers still have diesel backups. Ignoring them destroys credibility. Communities know they exist, so we track them.

We integrated diesel backup testing schedules and construction emissions into the HRA baseline model.

**How it works:**
- **Cumulative Burden**: Models backup emissions on top of existing community pollution load.
- **Testing Windows**: Schedules testing for low-impact times, enforced by the system.
- **Mitigation Tracking**: Logs filter upgrades and runtime limits.

**Why this matters for stakeholders:**
- **Community** Sees the *whole* picture, not just the "clean" days.
- **Government** Ensures emergency prep doesn't violate air quality goals.
- **Permit Requestor** Builds trust by acknowledging reality.

**Result:** Credibility is maintained by acknowledging and managing the dirty parts of clean infra.

See the model at https://lsars.com
""",
        "synopsis": "Even if normal operations are clean, diesel backup and construction emissions can be politically material in high-burden tracts. LSARS anchors the conversation in baseline HRA + cumulative burden and tracks mitigation/compliance transparently.",
    },
    {
        "id": "2026-B-019",
        "slug": "rural-workforce-commitments",
        "title": "How does LSARS make rural-region workforce commitments believable (apprenticeships + supports + reporting)?",
        "node_id": "0afcd997212046bbbe68dde82d",
        "expert": "Nelson Smith + Dr. Thad Perry",
        "product": "LSARS, HRA",
        "content": """# "Jobs" isn't a magic word—access is

"It creates jobs" is a tired line if locals can't access them due to skills or transport gaps.

We built SDOH-driven workforce targeting to identify and remove barriers to entry for rural communities.

**How it works:**
- **Barrier ID**: Maps transport, childcare, and education gaps in the local labor pool.
- **Support Integration**: Pairs apprenticeships with shuttles or childcare vouchers.
- **Local Spend**: Tracks payroll zip codes to prove local economic impact.

**Why this matters for stakeholders:**
- **Community** Real jobs for real neighbors, not just fly-in contractors.
- **Permit Requestor** "Economic benefit" becomes an irrefutable fact.
- **Government** Sees actual ROI on tax incentives.

**Result:** Workforce commitments turn from vague promises into audited local victories.

Build the workforce at https://lsars.com
""",
        "synopsis": "Use SDOH to identify barriers (transport, childcare, language, education), then pair paid apprenticeships with real supports and publish completion + local spend + procurement metrics so 'few jobs' skepticism is addressed with evidence.",
    },
]


def create_posts():
    today = datetime.date.today().strftime("%Y-%m-%d")
    year = "2026"
    month = "02"

    for post in posts_data:
        dir_name = f"{today}_{post['id']}_{post['slug']}"
        dir_path = os.path.join("posts", year, month, dir_name)
        os.makedirs(dir_path, exist_ok=True)

        assets_dir = os.path.join(dir_path, "assets")
        os.makedirs(assets_dir, exist_ok=True)
        with open(os.path.join(assets_dir, "README.md"), "w") as f:
            f.write("# Assets\n\n- [ ] Diagram/Screenshot for " + post["slug"])

        file_name = f"post-{post['slug']}-{post['id']}.md"
        file_path = os.path.join(dir_path, file_name)

        content = f"""# {post["title"]}

- **ID**: {post["id"]}
- **Date**: {today}
- **Status**: draft
- **Type**: Business
- **Expert**: {post["expert"]}
- **Product**: {post["product"]}
- **Artifacts**: {post["synopsis"]}

{post["content"]}
"""
        with open(file_path, "w") as f:
            f.write(content)

        print(f"Created {file_path}")

        cmd = f"python3 scripts/update_xmind_labels.py docs/mindmaps/LSARS_posts_v2.xmind {post['node_id']} {post['id']}"
        os.system(cmd)

    update_index(posts_data)


def update_index(posts):
    index_path = "post-index.md"
    with open(index_path, "r") as f:
        lines = f.readlines()

    insert_idx = 0
    for i, line in enumerate(lines):
        if line.strip() == "---":
            insert_idx = i
            break

    if insert_idx == 0:
        insert_idx = len(lines)

    new_rows = []
    for post in posts:
        today = datetime.date.today().strftime("%Y-%m-%d")
        link_path = f"posts/2026/02/{today}_{post['id']}_{post['slug']}/post-{post['slug']}-{post['id']}.md"
        link = f"[post]({link_path})"

        row = f"| {post['id']} | {post['title']} | {link} | draft | business | {post['product']} | — | — | {post['expert']} |\n"
        new_rows.append(row)

    updated_lines = lines[:insert_idx] + new_rows + lines[insert_idx:]

    with open(index_path, "w") as f:
        for line in updated_lines:
            if "Next business post:" in line:
                f.write(f"- Next business post:`2026-B-020`\n")
            else:
                f.write(line)

    print("Updated post-index.md")


if __name__ == "__main__":
    create_posts()
