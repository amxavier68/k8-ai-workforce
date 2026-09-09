# Privacy-respectful customer interaction

Status: PROPOSED — OWNER DIRECTED 2026-09-07
Class: BEHAVIOUR PATCH
Owner: Anthony
Release manager: Renee Archer
Gates: Sentinel, Mira
Implementation authority: Justin / DevMate
Rollback: restore the 2026-08-31 conversational behaviour contract and prior Sentinel/DevMate instructions.

## Change request

The Monday 2026-09-07 intelligence response correctly added Australian privacy provenance and applicability boundaries, but the workforce also requires an explicit customer-experience constraint: privacy controls must not impose unnecessary friction, coerce agreement, harass customers or obstruct legitimate refusal.

## Legal terminology and evidence boundary

The Australian Privacy Principles replaced the National Privacy Principles and Information Privacy Principles on 12 March 2014.

Primary sources:

- OAIC, Australian Privacy Principles: https://www.oaic.gov.au/privacy/australian-privacy-principles/read-the-australian-privacy-principles
- OAIC, APP 3 collection guidance, updated 2026-05-13: https://www.oaic.gov.au/privacy/australian-privacy-principles/australian-privacy-principles-guidelines/chapter-3-app-3-collection-of-solicited-personal-information
- OAIC, APP 7 direct marketing guidance: https://www.oaic.gov.au/privacy/australian-privacy-principles/australian-privacy-principles-guidelines/chapter-7-app-7-direct-marketing
- OAIC, APP 11 security and destruction/de-identification guidance: https://www.oaic.gov.au/privacy/australian-privacy-principles/australian-privacy-principles-guidelines/chapter-11-app-11-security-of-personal-information

This patch does not declare that Kollabor8, every client or every workflow is an APP entity. Applicability remains a scoped assessment and legal conclusions may require professional advice.

## Required behaviour

1. Verify purpose, coverage and necessity before imposing a privacy control or making a compliance claim.
2. Use the least intrusive effective collection and interaction.
3. Keep material notices and choices plain, timely and comprehensible.
4. Reject preselected, bundled, repetitive, obstructive or emotionally manipulative consent and opt-out patterns.
5. Do not require unrelated profiling, marketing agreement or account creation to obtain a requested service without a verified dependency.
6. Honour opt-outs without repeated persuasion or avoidable delay.
7. Preserve protective friction for sensitive information, identity, permissions, payment, consequential decisions, security and irreversible actions.
8. Route uncertain applicability and material privacy risk to Sentinel.
9. Justin / DevMate implements and evidences the data path but cannot self-approve compliance or customer acceptance.
10. Mira retains acceptance authority for comprehension, accessibility, effort and recovery.

## Test and release boundary

Four unit, adversarial and cross-seat cases extend the canonical conversational suite. Static CI must preserve:

- current APP terminology;
- verified applicability rather than blanket claims;
- no coercive or manipulative privacy patterns;
- least-intrusive effective controls;
- necessary protective friction;
- Sentinel governance and Mira acceptance separation;
- LIVE UPDATE PENDING until each affected GPT is patched and canaried.

No live GPT, website, form, collector, privacy policy, marketing workflow or client system changes are authorised by this source patch.
