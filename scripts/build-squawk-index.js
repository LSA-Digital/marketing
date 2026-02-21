const fs = require("fs");
const path = require("path");

// Load MCP data
const mcpPath = process.argv[2] || "/Users/idengrenme/.local/share/opencode/tool-output/tool_c7d8cfc360012e4yQZHnqX1bKL";
const mcp = JSON.parse(fs.readFileSync(mcpPath, "utf8"));

// Build doc ID -> MCP item map
const docMap = {};
for (const item of mcp.items) {
  docMap[item.id] = item;
}

// Doc CUID mapping
const mapping = {
  "2026-B-001":"cmla2aisk002kqk3jypq1n0wl","2026-T-001":"cmla416ds0038qk3jxq4sgb3g","2026-B-002":"cmla2budz002mqk3jwwavd2uy","2026-T-002":"cmla42gnc003aqk3j1ly3vfti",
  "2026-B-003":"cmla2db1y002oqk3jo5seogpx","2026-T-003":"cmla43rpr003cqk3jvp6r4ave","2026-B-004":"cmla2f91z002qqk3jj9gvfpd0","2026-B-005":"cmla2grdq002sqk3j0gqtdlad",
  "2026-T-004":"cmla451pz003eqk3jtwbd5p7j","2026-B-006":"cmla2idd2002uqk3jd93a6iq4","2026-T-005":"cmla469s6003gqk3jrs2ojysp","2026-B-007":"cmla2jr4j002wqk3jdrwsrhma",
  "2026-T-006":"cmla47pai003iqk3j126wurji","2026-B-008":"cmlldih7z001aq7s4ymrip3w3","2026-T-008":"cmla491yk003kqk3jm4o5wkf0","2026-B-009":"cmlldjdft001cq7s41w6llife",
  "2026-T-009":"cmlldkqu9001gq7s478kh37lp","2026-B-010":"cmlldk3bq001eq7s4sqafs50t","2026-T-010":"cmlldlemw001iq7s4w6dvt059","2026-B-011":"cmla3u662002yqk3jsbtlglwz",
  "2026-T-011":"cmla4abku003mqk3ja7swehax","2026-B-012":"cmla3vfy50030qk3jhjntqgh0","2026-T-012":"cmla4bpkq003oqk3jlt8hil4o","2026-B-013":"cmla3wtgc0032qk3jcvou3vx0",
  "2026-T-013":"cmla4d1rh003qqk3jm8iknja6","2026-B-014":"cmla3ydeh0034qk3jeeugq26v","2026-T-014":"cmla4ets3003sqk3jo9c5s5sk","2026-B-015":"cmla3zqvn0036qk3jxxclenpj",
  "2026-T-015":"cmla4gfin003uqk3j4c47i8rl","2026-B-016":"cmlvbruo0000004lbdu6ci88e","2026-B-017":"cmlvgl8fr000304l4pqaaa7qc","2026-B-018":"cmlvglrtb000604l4vi4fvavg",
  "2026-B-019":"cmlvgmeun000904l4tcjcg2cy","2026-B-020":"cmlldm6d3001kq7s4rfuutxk9","2026-B-021":"cmlvgnznu000c04l4uz99nlte","2026-B-022":"cmlmj2yd800226gs49ic4xthf",
  "2026-B-023":"cmlmj3je800256gs4uvesyi3j","2026-B-024":"cmlmj41p000286gs4xr1bswgu","2026-B-025":"cmlvgqidg000f04l48mqizwdh","2026-B-026":"cmlmly411001hbzs4ux0rihl9",
  "2026-B-027":"cmlmlyn99001kbzs49kb4rq8x","2026-B-028":"cmlmlz417001nbzs4bi4v0d7n","2026-B-029":"cmlvirqai000i04l4fxmznbmw","2026-B-030":"cmlvis9y1000l04l40ftntlqo",
  "2026-B-031":"cmlvisuk8000o04l4hgseu5ar","2026-B-032":"cmlmlznm8001qbzs4jgep40pi","2026-B-033":"cmlmm06u0001tbzs43ube312u","2026-B-034":"cmlviuq41000r04l43zac9uir",
  "2026-B-035":"cmlvivcb5000u04l44c8cq35o","2026-T-016":"cmlvj1ft1000x04l4tiq65kmd","2026-B-036":"cmlvj1wmh001004l4avx2mdti","2026-T-017":"cmlo55m0u002gxds4b1xc8a36",
  "2026-T-018":"cmlvbs7x7000104lbbvyoz41w","2026-T-019":"cmlvj3xky001304l467xp03q1","2026-T-020":"cmlvj4gb8001604l4xnkg2rf1","2026-T-021":"cmlvj56c6001904l4rfmbm5at",
  "2026-T-022":"cmlvj5nll001c04l4tty4zuzm","2026-T-023":"cmlvj6blm001f04l4h1zph36j","2026-T-024":"cmlvj6uq7001i04l4kr9rs17z","2026-T-025":"cmlvj7iqr001l04l4datg9u6b",
  "2026-T-026":"cmlvj7xhu001o04l4sccvdnlu","2026-T-027":"cmlvj8oa4001r04l4l6p5g9ye","2026-T-028":"cmlvj9716001u04l4tbm05qjd","2026-T-029":"cmlvj9vz8001x04l4zpcj3eq4",
  "2026-T-030":"cmlo56x6i002jxds4mkjuj075","2026-T-031":"cmlvjazyt002004l41w8uab58","2026-T-032":"cmlvjbgbu002304l4yb7wjvst","2026-T-033":"cmlvjc6j1002604l4cqa94wiq",
  "2026-T-034":"cmlvjckx3002904l40nn1or17","2026-T-035":"cmlvjdae4002c04l4jf4ie75g","2026-T-036":"cmlvjdobk002f04l4urp2jz4q","2026-T-037":"cmlvjecnd002i04l4ih95r644",
  "2026-T-038":"cmlvjese9002l04l478tpfpcp","2026-T-039":"cmlvjfhy3002o04l4h7uxogy1","2026-T-040":"cmlvjfveq002r04l4g3r1r9m1","2026-T-041":"cmlvjgl7i002u04l43y9tdp9r",
  "2026-T-042":"cmlvjh2e4002x04l4mphv36dc","2026-T-043":"cmlvjhp40003004l4fcmihzrz","2026-B-037":"cmlvji9e4003304l4h46ds1iu","2026-T-044":"cmlvjj489003604l4f8cgsqvo",
  "2026-B-038":"cmlvjjpfq000004kv3b4f2xic","2026-T-045":"cmlvjkcsb000304kvdmxigw5j"
};

// Parse post-index.md
const postIndex = {};
const piContent = fs.readFileSync("/Users/idengrenme/dev/marketing/post-index.md", "utf8");
const piLines = piContent.split("\n");
for (const line of piLines) {
  const m = line.match(/^\| (2026-[BT]-\d+)\s*\|/);
  if (!m) continue;
  const rawCols = line.split("|").map(c => c.trim());
  if (rawCols[0] === "") rawCols.shift();
  if (rawCols[rawCols.length - 1] === "") rawCols.pop();
  const cols = rawCols;
  if (cols.length < 13) { console.error("Skipping", cols[0], "only", cols.length, "cols"); continue; }
  postIndex[cols[0]] = {
    audience: cols[5] || "",
    product: cols[7] || "",
    themes: cols[8] || "",
    dependsOn: cols[9] || "",
    depName: cols[10] || "",
    relationship: cols[11] || "",
    expert: cols[12] || ""
  };
}

// Sort post IDs: B first then T, numeric
const postIds = Object.keys(mapping);
postIds.sort((a, b) => {
  const [, ta, na] = a.match(/2026-([BT])-(\d+)/);
  const [, tb, nb] = b.match(/2026-([BT])-(\d+)/);
  if (ta !== tb) return ta === "B" ? -1 : 1;
  return parseInt(na) - parseInt(nb);
});

function trunc(s, n) {
  if (!s) return "—";
  if (s.length <= n) return s;
  return s.slice(0, n) + "...";
}

function esc(s) {
  if (!s) return "—";
  return s.replace(/\|/g, "\\|").replace(/\n/g, " ");
}

function clean(s) {
  if (!s || s === "—" || s.trim() === "" || s.trim() === "—") return "—";
  return s.trim();
}

function getAssetsPreview(pid) {
  const postsBase = "/Users/idengrenme/dev/marketing/posts/2026/02";
  let assetsDir = null;
  try {
    const dirs = fs.readdirSync(postsBase);
    for (const dir of dirs) {
      if (dir.includes(`_${pid}_`) || dir.endsWith(`_${pid}`)) {
        const candidate = `${postsBase}/${dir}/assets`;
        if (fs.existsSync(candidate)) {
          assetsDir = candidate;
          break;
        }
      }
    }
  } catch (e) { return "—"; }

  if (!assetsDir) return "—";

  let files;
  try { files = fs.readdirSync(assetsDir); } catch (e) { return "—"; }

  const EXCLUDE = new Set(["README.md", ".DS_Store"]);
  const IMAGE_EXTS = new Set([".png", ".jpg", ".jpeg", ".gif", ".svg"]);
  const VIDEO_EXTS = new Set([".mp4", ".webm"]);

  const relBase = `posts/2026/02`;
  const dirName = assetsDir.replace(`${postsBase}/`, "").replace("/assets", "");

  let images = [], pdfs = [], videos = [];
  for (const f of files) {
    if (EXCLUDE.has(f) || f.startsWith(".")) continue;
    const ext = path.extname(f).toLowerCase();
    const relPath = `${relBase}/${dirName}/assets/${f}`;
    if (IMAGE_EXTS.has(ext)) {
      images.push(`<img src="${relPath}" width="60">`);
    } else if (ext === ".pdf") {
      const label = f.length > 25 ? f.slice(0, 22) + "..." : f;
      pdfs.push(`[📄 ${label}](${relPath})`);
    } else if (VIDEO_EXTS.has(ext)) {
      const type = ext.slice(1);
      videos.push(`<video width="120" controls><source src="${relPath}" type="video/${type}"></video>`);
    }
  }

  if (images.length === 0 && pdfs.length === 0 && videos.length === 0) return "—";

  let parts = [];
  if (images.length > 3) {
    parts.push(...images.slice(0, 3));
    parts.push(`+${images.length - 3}`);
  } else {
    parts.push(...images);
  }
  parts.push(...pdfs);
  parts.push(...videos);

  return parts.join(" ");
}

let rows = [];
for (const pid of postIds) {
  const docId = mapping[pid];
  const doc = docMap[docId];
  const pi = postIndex[pid] || {};

  if (!doc) { console.error("Missing doc for", pid, docId); continue; }

  const title = esc(doc.title);
  const reviewStatus = doc.reviewStatus || "—";
  const readiness = doc.readinessScore || "—";
  const readinessNotes = trunc(esc(doc.readinessSummary), 80);
  const audience = clean(pi.audience);
  const firstProduct = clean((pi.product || "").split(",")[0]);
  const firstExpert = clean((pi.expert || "").split(",")[0]);
  const themes = (doc.declaredThemes || []).join(", ") || "—";
  const dependsOn = clean(pi.dependsOn);
  const depName = dependsOn !== "—" ? esc(clean(pi.depName)) : "—";
  const relationship = (dependsOn !== "—" && clean(pi.relationship) !== "—") ? esc(trunc(clean(pi.relationship), 80)) : "—";
  const repostBy = clean(pi.expert);
  const updated = doc.updatedAt ? doc.updatedAt.slice(0, 10) : "—";

  const assetsPreview = getAssetsPreview(pid);
  rows.push(`| ${pid} | ${title} | ${assetsPreview} | ${reviewStatus} | ${readiness} | ${readinessNotes} | ${audience} | ${firstProduct} | ${firstExpert} | ${themes} | ${dependsOn} | ${depName} | ${relationship} | ${repostBy} | ${updated} |`);
}

const header = `# Squawk Index

> **Auto-generated from Squawk MCP** — Do not edit manually. Rebuilt from scratch on each sync.
> 
> Last rebuilt: 2026-02-21

| Post ID | Title | Assets Preview | Review Status | Readiness | Readiness Notes | Audience | Product | Expert | Themes | Depends On | Dep. Name | Relationship | Repost By | Updated |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
`;

const md = header + rows.join("\n") + "\n";
fs.writeFileSync("/Users/idengrenme/dev/marketing/squawk-index.md", md);
console.log("Wrote " + rows.length + " rows to squawk-index.md");
