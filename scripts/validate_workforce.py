#!/usr/bin/env python3
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
workforce = json.loads((ROOT / "workforce.json").read_text())
contracts = json.loads((ROOT / "tests/role-contracts.json").read_text())
behaviour = json.loads((ROOT / "tests/behavioural-commissioning.json").read_text())

if workforce.get("human_accountable") != "Anthony": errors.append("human_accountable must remain Anthony")
if workforce.get("second_in_command") != "Renee Archer": errors.append("second_in_command must remain Renee Archer")
leads = workforce.get("leads", [])
ids = [lead.get("id") for lead in leads]
expected = {"sentinel","finlay","mira","kai","devmate","sammi","atlas","clarity"}
if set(ids) != expected or len(ids) != 8: errors.append(f"workforce must contain exactly the eight canonical leads; got {ids}")

for lead in leads:
    lead_id = lead["id"]
    path = ROOT / "leads" / lead_id / "instructions.md"
    if not path.exists():
        errors.append(f"missing instructions: {path.relative_to(ROOT)}")
        continue
    text = path.read_text()
    for invariant in ("Anthony", "Renee Archer"):
        if invariant not in text: errors.append(f"{lead_id}: missing authority invariant {invariant!r}")
    for token in contracts.get(lead_id, {}).get("required", []):
        if token.lower() not in text.lower(): errors.append(f"{lead_id}: missing required contract token {token!r}")
    cases = behaviour.get(lead_id, [])
    case_types = {c.get("type") for c in cases}
    if len(cases) != 3 or case_types != {"unit","adversarial","cross-seat"}:
        errors.append(f"{lead_id}: commissioning suite must contain exactly unit, adversarial and cross-seat cases")
    for case in cases:
        if not case.get("prompt") or not case.get("expect"): errors.append(f"{lead_id}: incomplete behavioural case")

lookup = {x["id"]: x for x in leads}
if lookup["sentinel"].get("decision_contract") != ["YES","NO","REQUIRES FURTHER CONSIDERATION"]: errors.append("Sentinel decision contract changed")
if lookup["finlay"].get("decision_contract") != ["YES","NO","FIND ALTERNATIVE"]: errors.append("Finlay decision contract changed")
if lookup["mira"].get("decision_contract") != ["PASS","PARTIAL PASS","FAIL"]: errors.append("Mira decision contract changed")
if lookup["kai"].get("decision_contract") != ["ACTION","EXPERIMENT","WATCH","REJECT"]: errors.append("Kai decision contract changed")

if errors:
    print("AI workforce CI FAILED")
    for error in errors: print(f"- {error}")
    sys.exit(1)
print("AI workforce CI PASSED")
print("Validated eight leads, authority invariants, role contracts and 24 commissioning cases.")
