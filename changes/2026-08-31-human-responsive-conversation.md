# Governed change: human-responsive conversational behaviour

Date: 2026-08-31  
Status: CANONICAL PATCH PROPOSED — LIVE INSTANCE UPDATE PENDING  
Class: BEHAVIOUR PATCH  
Owner accountability: Anthony  
Owner approval: Explicitly requested integration in the Kollabor8 operating conversation on 2026-08-31  
Release manager: Renee Archer  
Governance gate: Sentinel — REQUIRED  
Behavioural acceptance: Mira — REQUIRED  
Provenance: Atlas

## Intended outcome

Make every K8 AI interaction warm, proportionate and responsive without weakening specialist judgement, evidence requirements, independent gates or owner authority.

## Canonical change

The shared guardrail is stored in `shared/CONVERSATIONAL-BEHAVIOUR.md` and applies to Renee plus all eight accountable K8 GPT leads.

It requires context acknowledgement, plain-language goal reflection, no more than one high-value question when needed, proportionate response modes, recovery before formal workflow when the user is frustrated or uncertain, and one bounded useful close.

## Evidence and tests

- Six unit, adversarial and cross-seat cases are defined in `tests/conversational-behaviour.json`.
- The validator must confirm the shared contract, owner/release invariants, required test types and live-update boundary.
- Existing specialist decision contracts remain unchanged.

## No live mutation

This canonical patch does not itself alter the live Custom GPT instances. Each live GPT Builder instruction set must receive the exact shared guardrail and pass a brief canary before runtime commissioning can be claimed.

## Rollback

Last known-good baseline: `main` immediately before this change.

Rollback if the patch causes unnecessary questions, coaching instead of requested execution, hidden material risk, weakened specialist verdicts, false consensus, or premature claims that a live GPT was updated.
