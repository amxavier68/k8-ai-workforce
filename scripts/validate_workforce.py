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

# Daily Briefing must remain a governed workforce-intelligence trigger.
hr_text = (ROOT / "shared" / "AI-HR-CICD.md").read_text()
for token in (
    "Daily Briefing workforce-intelligence trigger",
    "KNOWLEDGE PATCH",
    "BEHAVIOUR PATCH",
    "TOOL-PERMISSION CHANGE",
    "ROLE-AUTHORITY CHANGE",
    "MODEL-PLATFORM CHANGE",
    "live-instance change must be marked **PENDING**",
):
    if token not in hr_text:
        errors.append(f"AI-HR lifecycle missing Daily Briefing workforce trigger invariant: {token!r}")

# Shared conversational behaviour must remain canonical, tested and live-evidence gated.
conversation_path = ROOT / "shared" / "CONVERSATIONAL-BEHAVIOUR.md"
conversation_tests_path = ROOT / "tests" / "conversational-behaviour.json"
if not conversation_path.exists():
    errors.append("missing shared/CONVERSATIONAL-BEHAVIOUR.md")
if not conversation_tests_path.exists():
    errors.append("missing tests/conversational-behaviour.json")
if conversation_path.exists():
    conversation_text = conversation_path.read_text()
    for token in (
        "Acknowledge the user’s situation",
        "ask no more than one high-value question",
        "quick sense-check",
        "guided exploration",
        "finished work",
        "smallest useful next move",
        "LIVE UPDATE PENDING",
    ):
        if token not in conversation_text:
            errors.append(f"shared conversational contract missing invariant: {token!r}")
if conversation_tests_path.exists():
    conversation_tests = json.loads(conversation_tests_path.read_text())
    if conversation_tests.get("owner") != "Anthony":
        errors.append("conversational behaviour owner must remain Anthony")
    if conversation_tests.get("release_manager") != "Renee Archer":
        errors.append("conversational behaviour release manager must remain Renee Archer")
    if conversation_tests.get("live_update") != "pending":
        errors.append("conversational live_update must remain pending until runtime evidence exists")
    cases = conversation_tests.get("tests", [])
    case_types = {case.get("type") for case in cases}
    if len(cases) < 6 or case_types != {"unit", "adversarial", "cross-seat"}:
        errors.append("conversational suite must contain at least six unit, adversarial and cross-seat cases")
    for case in cases:
        for field in ("id", "type", "seat", "scenario", "expected", "rollback"):
            if not case.get(field):
                errors.append(f"conversational case {case.get('id', 'unknown')} missing {field}")

if errors:
    print("AI workforce CI FAILED")
    for error in errors: print(f"- {error}")
    sys.exit(1)
print("AI workforce CI PASSED")
print("Validated eight leads, authority invariants, role contracts, 24 commissioning cases, Daily Briefing trigger and shared conversational behaviour contract.")
