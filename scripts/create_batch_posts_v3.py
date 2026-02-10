import os
import datetime
import sys

posts_data = [
    {
        "id": "2026-B-020",
        "slug": "sdoh-mobility-acceptance",
        "title": "How does LSARS + Smart Mobility turn SDOH into mobility investments communities will accept?",
        "node_id": "e1c4b9f03fb7495bbe7ee53c42",
        "expert": "Dr. Thad Perry",
        "product": "LSARS, Smart Mobility",
        "content": """# Mobility investments fail when they ignore reality

"We added a bus stop" is useless if the community needs wheelchair vans. Mobility investments fail when they don't match community reality.

We integrated SDOH data to target mobility investments where they are needed most—and where they will be accepted.

**How it works:**
- **Vulnerability Mapping**: Highlights no-vehicle households, language isolation, and disability concentrations.
- **Targeted Interventions**: Recommends specific solutions (shuttles, multilingual wayfinding) based on identified gaps.
- **Trust Building**: Demonstrates understanding of local needs beyond generic "improvements".

**Why this matters for stakeholders:**
- **Community** Gets useful infrastructure that solves daily struggles, not just checkboxes.
- **Permit Requestor** Reduces opposition by solving real problems for neighbors.
- **Government** Sees equitable investment of permit fees.

**Result:** Mobility becomes a community asset, not a gentrification signal.

See the map at https://lsars.com
""",
        "synopsis": "Use SDOH (no-vehicle households, disability/elderly concentration, language isolation) to target shuttles, vouchers, multilingual wayfinding, and access-to-services improvements that build trust and reduce permit opposition.",
    },
    {
        "id": "2026-B-021",
        "slug": "measurable-construction-traffic",
        "title": "How does Smart Mobility make construction traffic commitments measurable for faster permits?",
        "node_id": "4c5cbff04d124704954536d5ed",
        "expert": "Keith Mangold + Nelson Smith",
        "product": "LSARS, Smart Mobility",
        "content": """# "Construction traffic" shouldn't be a mystery

"Construction traffic" is a top NIMBY weapon because it's usually unmanaged chaos. Promises to "be careful" are ignored.

We track truck routes and delivery windows in the Permit Intelligence Portal to make traffic commitments measurable.

**How it works:**
- **Route Fencing**: GPS enforcement ensures trucks stick to approved arterials.
- **Window Management**: Scheduling system blocks deliveries during school drop-off or commute hours.
- **Public Violation Log**: Transparent reporting of infractions and corrective actions.

**Why this matters for stakeholders:**
- **Government** Enforces constraints without expensive road patrols.
- **Community** Sees valid complaints addressed instantly.
- **Permit Requestor** Eliminates "traffic chaos" as a valid objection.

**Result:** Construction logistics become a transparent operation, not a neighborhood menace.

Track the fleet at https://lsars.com
""",
        "synopsis": 'Commit to truck routes and delivery windows, then publish violations, corrective actions, and congestion KPIs through LSARS Permit Intelligence Portal to prevent "traffic + disruption" from stalling approvals.',
    },
    {
        "id": "2026-B-022",
        "slug": "mobility-kpi-scorecards",
        "title": "How does LSARS publish mobility KPIs as part of a CBA scorecard to ensure transparency?",
        "node_id": "61575784e0f643a1839990cb7d",
        "expert": "Keith Mangold + Nelson Smith",
        "product": "LSARS, Smart Mobility",
        "content": """# Complex traffic studies hide reality—KPIs reveal it

300-page traffic studies are where transparency goes to die. Communities trust what they can understand.

We publish understandable mobility KPIs as enforceable CBA scorecards.

**How it works:**
- **Idling Proxies**: Measures congestion impact without privacy-invasive tracking.
- **Parking Utilization**: Real-time occupancy metrics for agreed-upon lots.
- **Service Reliability**: Tracking shuttle and transit on-time performance against promises.

**Why this matters for stakeholders:**
- **Community** Understands the data without a traffic engineering degree.
- **Permit Requestor** Demonstrates operational excellence transparently.
- **Government** Has a simple dashboard for CBA compliance.

**Result:** Traffic impact becomes a shared fact, not a debate.

See the scorecard at https://lsars.com
""",
        "synopsis": "Combine LSARS accountability with Smart Mobility operations to publish KPIs the public understands (idling proxies, congestion hotspots, parking utilization, service reliability) as enforceable Community Benefit Agreement scorecards.",
    },
    {
        "id": "2026-B-023",
        "slug": "emergency-access-equity",
        "title": "How does LSARS + Smart Mobility improve emergency access (cooling centers/clinics)?",
        "node_id": "1ce6f5df5644445186fc1a1f7e",
        "expert": "Dr. Thad Perry",
        "product": "LSARS, Smart Mobility",
        "content": """# A cooling center is useless if you can't get there

In high-vulnerability tracts, distance is a health hazard. Building a facility isn't enough—you have to solve the "last mile."

We use SDOH heat vulnerability layers to plan and execute emergency access mobility.

**How it works:**
- **Heat Mapping**: Overlays temperature spikes with elderly and disability census tracts.
- **Route Planning**: Deploys shuttles to bridge the gap during emergencies.
- **Public Reporting**: Tracks accessibility metrics during events to prove effectiveness.

**Why this matters for stakeholders:**
- **Community** Lifesaving access during climate extremes.
- **Government** Improves resilience scores for the district.
- **Permit Requestor** Demonstrates profound community care.

**Result:** Infrastructure investments actually reach the people they are meant to save.

Map the gap at https://lsars.com
""",
        "synopsis": "Use SDOH to identify heat/medical vulnerability, then implement and track access-to-services mobility plans (shuttle routes, park-and-ride integration, mobility vouchers) with public reporting to increase CPS confidence.",
    },
    {
        "id": "2026-B-024",
        "slug": "gov-mobility-visibility",
        "title": "How does LSARS give under-resourced governments one-click mobility visibility?",
        "node_id": "32787c6c006b472a989233a01c",
        "expert": "Keith Mangold + Nelson Smith",
        "product": "LSARS, Smart Mobility",
        "content": """# Small agencies shouldn't fly blind

Small permitting agencies can't afford big traffic command centers. They shouldn't have to to manage a large project.

We ingest Smart Mobility feeds into LSARS so agencies get situational awareness for free.

**How it works:**
- **Unified Dashboard**: Permit status alongside live traffic and parking signals.
- **Incident Detection**: Automated alerts for congestion anomalies near the site.
- **No-Cost Access**: The permit applicant covers the platform cost as part of the application.

**Why this matters for stakeholders:**
- **Government** Sophisticated monitoring without the procurement nightmare.
- **Permit Requestor** Faster approvals from confident, informed agencies.

**Result:** Agencies get the visibility they need to say "yes" without blowing their budget.

See the view at https://lsars.com
""",
        "synopsis": "Ingest Smart Mobility feeds into LSARS dashboards so agencies can see permit status + traffic/parking compliance + incident response signals without buying new government software.",
    },
    {
        "id": "2026-B-025",
        "slug": "parking-spillover-control",
        "title": "How does Smart Mobility reduce parking spillover and quality-of-life opposition?",
        "node_id": "f4d2743f5bc24709af0f316a35",
        "expert": "Keith Mangold + Nelson Smith",
        "product": "LSARS, Smart Mobility",
        "content": """# "They'll park on our streets" kills projects

Fear of parking spillover is a project-killer. Signs aren't enough—you need a system.

We use regulated parking operations and enforcement to guarantee neighborhood protection.

**How it works:**
- **Permit Zones**: Digital enforcement of resident-only areas.
- **Occupancy Tracking**: Proves project vehicles stay on-site.
- **Complaint Resolution**: Rapid response to reported violations.

**Why this matters for stakeholders:**
- **Community** Protects quality of life and driveway access.
- **Permit Requestor** Eliminates a durable source of neighborhood friction.
- **Government** Reduces parking enforcement burden.

**Result:** Parking spillover is managed, measured, and prevented.

Clear the curb at https://lsars.com
""",
        "synopsis": "Use regulated on-street/off-street parking operations and clear enforcement rules during construction/operations, then publish outcomes and complaints resolution in LSARS to reduce durable NIMBY coalitions.",
    },
    {
        "id": "2026-B-026",
        "slug": "lez-compliance-proof",
        "title": "How do Low Emission Zone / access-control systems become a compliance proof point?",
        "node_id": "2cd2f41876a44972b2d8fd0006",
        "expert": "Keith Mangold + Nelson Smith",
        "product": "LSARS, Smart Mobility",
        "content": """# Low Emission Zones need more than a sign

Low Emission Zones (LEZ) are often just rules on paper. Without enforcement, they are ignored.

We connect access control systems to public scorecards to prove LEZ compliance.

**How it works:**
- **Gated Access**: Validates vehicle emission class at entry.
- **Public Logs**: Anonymized counts of compliant vs non-compliant attempts.
- **Trend Analysis**: Shows improvement over time to prove policy effectiveness.

**Why this matters for stakeholders:**
- **Government** "Green" policies that actually work.
- **Community** Measurable air quality protection they can verify.
- **Permit Requestor** Automates compliance reporting.

**Result:** LEZ rules become physical reality, not just regulatory aspirations.

Check the gate at https://lsars.com
""",
        "synopsis": "Connect access control + LEZ compliance data to LSARS public scorecards so 'rules on paper' become measurable compliance in practice, reducing re-litigating facts and speeding approvals.",
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
                f.write(f"- Next business post:`2026-B-027`\n")
            else:
                f.write(line)

    print("Updated post-index.md")


if __name__ == "__main__":
    create_posts()
