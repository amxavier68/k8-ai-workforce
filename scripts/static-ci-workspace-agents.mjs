import fs from "node:fs";

const testPath = "tests/2026-09-01-workspace-agent-transition.json";
const proposalPath = "changes/2026-09-01-workspace-agent-transition.md";

const fail = (message) => {
  console.error(`STATIC_CI_FAIL: ${message}`);
  process.exit(1);
};

for (const path of [testPath, proposalPath]) {
  if (!fs.existsSync(path)) fail(`missing ${path}`);
}

const doc = JSON.parse(fs.readFileSync(testPath, "utf8"));
const proposal = fs.readFileSync(proposalPath, "utf8");

if (doc.live_update !== "pending") fail("live_update must remain pending");
if (doc.owner !== "Anthony") fail("owner accountability changed");
if (doc.release_manager !== "Renee Archer") fail("release manager changed");

for (const gate of ["Sentinel", "Mira", "Finlay"]) {
  if (!doc.gates?.includes(gate)) fail(`missing ${gate} gate`);
}

for (const type of ["unit", "adversarial", "cross-seat"]) {
  if (!doc.tests?.some((test) => test.type === type)) fail(`missing ${type} test`);
}

if (new Set(doc.tests.map((test) => test.id)).size !== doc.tests.length) {
  fail("duplicate test IDs");
}

for (const test of doc.tests) {
  for (const field of ["id", "type", "seat", "scenario", "rollback"]) {
    if (!test[field]) fail(`${test.id ?? "unknown"} missing ${field}`);
  }
  if (!Array.isArray(test.expected) || test.expected.length === 0) {
    fail(`${test.id} missing expected outcomes`);
  }
}

for (const phrase of [
  "Availability is not entitlement",
  "Evolution is not forced migration",
  "Capability grants no authority",
  "Manual GPT Builder action required today",
  "Last-known-good baseline"
]) {
  if (!proposal.includes(phrase)) fail(`proposal missing: ${phrase}`);
}

console.log(`STATIC_CI_PASS: ${doc.tests.length} workspace-agent tests validated`);
