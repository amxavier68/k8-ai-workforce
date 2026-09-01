import fs from "node:fs";

const files = [
  "knowledge-patches/2026-08-26-daily-intelligence.md",
  "knowledge-patches/2026-08-27-daily-intelligence.md",
  "knowledge-patches/2026-08-28-daily-intelligence.md",
  "knowledge-patches/2026-08-31-weekend-rollup.md",
  "knowledge-patches/2026-09-01-daily-intelligence.md",
  "knowledge-patches/2026-09-01-audit-promotion.md",
  "knowledge-patches/2026-09-02-daily-intelligence.md"
];

const fail = (message) => {
  console.error(`STATIC_CI_FAIL: ${message}`);
  process.exit(1);
};

for (const path of files) {
  if (!fs.existsSync(path)) fail(`missing ${path}`);
  const text = fs.readFileSync(path, "utf8");
  if (!text.includes("Owner accountability: Anthony")) fail(`${path}: owner accountability missing`);
  if (!text.includes("Renee Archer")) fail(`${path}: release manager missing`);
  if (!text.includes("http")) fail(`${path}: no source URL present`);
}

for (const path of files.slice(0, 5)) {
  const text = fs.readFileSync(path, "utf8");
  if (!text.includes("Status: CANONICAL KNOWLEDGE — OWNER APPROVED 2026-09-01")) {
    fail(`${path}: canonical approval status missing`);
  }
  if (text.includes("Status: PROPOSED") || text.includes("LIVE UPDATE PENDING")) {
    fail(`${path}: stale proposed/live-pending status remains`);
  }
}

const aug28 = fs.readFileSync(files[2], "utf8");
if (!aug28.includes("official stable releases page still listed 11.0.1 as stable")) {
  fail("WooCommerce scheduled-vs-stable qualifier missing");
}
if (!aug28.includes("broader K8/client implications remain WATCH")) {
  fail("Ask Maps WATCH boundary missing");
}

const aug27 = fs.readFileSync(files[1], "utf8");
if (!aug27.includes("Australian Securities and Investments Commission, 2026-08-05")) {
  fail("ASIC corrected source date missing");
}

const sep1 = fs.readFileSync(files[4], "utf8");
if (!sep1.includes("Broader adoption remains WATCH")) fail("WebMCP WATCH boundary missing");

const audit = fs.readFileSync(files[5], "utf8");
for (const phrase of ["No live mutation", "Sentinel — ACCEPTED", "Mira — ACCEPTED", "Finlay"] ) {
  if (!audit.includes(phrase)) fail(`audit missing: ${phrase}`);
}

const sep2 = fs.readFileSync(files[6], "utf8");
for (const phrase of [
  "Status: CANONICAL KNOWLEDGE — OWNER APPROVED 2026-09-02",
  "not a new operative general product-safety law",
  "Dynamic Search Ads sunset and auto-upgrade until February 2027",
  "does not authorise K8",
  "Atlas: VERIFIED",
  "Sentinel: ACCEPTED",
  "Finlay: GATE RETAINED",
  "Mira: ACCEPTED",
  "Renee: PROMOTED"
]) {
  if (!sep2.includes(phrase)) fail(`2 Sep canonical record missing: ${phrase}`);
}
if (sep2.includes("Status: PROPOSED") || sep2.includes("LIVE UPDATE PENDING") || sep2.includes("Acceptance required")) {
  fail("2 Sep canonical record retains stale proposal state");
}

console.log(`STATIC_CI_PASS: ${files.length} knowledge records validated`);
