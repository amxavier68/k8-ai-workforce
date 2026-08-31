import fs from "node:fs";

const testPath = "tests/2026-08-25-openai-model-retirements.json";
const changePath = "changes/2026-08-25-openai-model-retirements.md";

const fail = (message) => {
  console.error(`STATIC_CI_FAIL: ${message}`);
  process.exit(1);
};

for (const path of [testPath, changePath]) {
  if (!fs.existsSync(path)) fail(`missing ${path}`);
}

const doc = JSON.parse(fs.readFileSync(testPath, "utf8"));
const change = fs.readFileSync(changePath, "utf8");

if (doc.live_update !== "pending") fail("live_update must remain pending");
if (doc.owner !== "Anthony") fail("owner accountability changed");
if (doc.release_manager !== "Renee Archer") fail("release manager changed");
for (const gate of ["Sentinel", "Mira", "Finlay"]) {
  if (!doc.gates?.includes(gate)) fail(`missing ${gate} gate`);
}
for (const type of ["unit", "adversarial", "cross-seat"]) {
  if (!doc.tests?.some((test) => test.type === type)) fail(`missing ${type} test`);
}
if (doc.tests.length !== 9) fail(`expected 9 tests, found ${doc.tests.length}`);
if (new Set(doc.tests.map((test) => test.id)).size !== doc.tests.length) fail("duplicate test IDs");
for (const test of doc.tests) {
  for (const field of ["id", "type", "seat", "scenario", "rollback"]) {
    if (!test[field]) fail(`${test.id ?? "unknown"} missing ${field}`);
  }
  if (!Array.isArray(test.expected) || test.expected.length === 0) fail(`${test.id} missing expected outcomes`);
}
for (const phrase of [
  "No live mutation",
  "API access",
  "GPT-5.6 Terra",
  "GPT-5.6 Luna",
  "Manual GPT Builder action required today",
  "Last-known-good baseline"
]) {
  if (!change.includes(phrase)) fail(`change record missing: ${phrase}`);
}

console.log(`STATIC_CI_PASS: ${doc.tests.length} model-retirement tests validated`);
