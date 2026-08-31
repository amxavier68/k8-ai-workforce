# Governed change — OpenAI model retirements

Date opened: 2026-08-25
Approved: 2026-09-01
Class: MODEL / PLATFORM CHANGE
Status: APPROVED FOR CANONICAL MERGE — LIVE INSTANCE UPDATE PENDING
Owner accountability: Anthony
Owner approval: explicit instruction on 2026-09-01 to implement outstanding WORKFORCE changes under existing guard rails
Release manager: Renee Archer
Governance acceptance: Sentinel — ACCEPTED
Behavioural acceptance: Mira — ACCEPTED
Commercial gate: Finlay — NO NEW SPEND / NO SUBSCRIPTION CHANGE
Provenance: Atlas

## Verified triggers

1. OpenAI o3 retired from ChatGPT on 2026-08-26 after a 90-day sunset. OpenAI states that this does not change API access.
   Primary source: https://help.openai.com/en/articles/9624314-model-release-notes
2. GPT-5.4 and GPT-5.4 mini ceased to be available in Codex on 2026-08-31 when signed in with a ChatGPT account. OpenAI directs replacement with GPT-5.6 Terra and GPT-5.6 Luna respectively. OpenAI API access and Codex using an API key are unchanged.
   Primary source: https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan

The source scope is binding: ChatGPT/Codex product availability is not the same as API retirement.

## Affected seats

Renee Archer, DevMate, Mira, Sentinel, Atlas; Finlay only if a replacement path introduces a commercial consequence.

## Canonical behaviour

- Detect model availability at execution time; do not assume a retired model remains selectable.
- Route former GPT-5.4 Codex work to GPT-5.6 Terra and former GPT-5.4 mini Codex work to GPT-5.6 Luna when the Codex session is authenticated with ChatGPT, subject to actual entitlement and availability.
- Do not describe o3, GPT-5.4 or GPT-5.4 mini API access as retired on the basis of these product changes.
- Preserve task acceptance criteria, evidence requirements, PBAC, owner accountability and least privilege through model substitution.
- A replacement model does not inherit extra tools, permissions, scope or authority merely because it is more capable.
- Do not purchase credits, alter subscriptions or raise paid usage without Finlay review and owner authority.
- Safe-stop an affected automation if its required model is unavailable and no accepted replacement path is configured; preserve evidence rather than fabricating completion.

## Inventory evidence

Repository search on 2026-09-01 found no hard-coded `o3`, `GPT-5.4` or `GPT-5.4 mini` references in the canonical workforce source package outside this governed retirement record.

This does **not** prove that every live custom GPT, Codex preference, workspace default, local configuration or external automation is free of legacy references. Those live surfaces remain separately evidence-gated.

## No live mutation

Canonical merge changes no live GPT Builder configuration, Codex setting, model selection, API workflow, credential, connector, subscription or production automation.

Manual GPT Builder action required today: **none proven**. If a later live-instance inventory finds a hard-coded retired model, update only that reference to an accepted available replacement, then run the relevant Mira/Sentinel canary before marking the instance current.

## Acceptance evidence

- Primary OpenAI source and product/API scope: VERIFIED by Atlas rules.
- Sentinel: ACCEPTED — no authority or permission expansion; unavailable models cause bounded substitution or safe-stop.
- Mira: ACCEPTED — acceptance criteria and hand-off behaviour survive substitution; runtime success may not be inferred.
- Finlay: NO NEW SPEND / NO SUBSCRIPTION CHANGE — this canonical patch authorises no commercial action.
- Renee: CONFIRMED — no new specialist GPT and no silent live-instance mutation.
- Deterministic static CI must pass on the final approved branch head before merge.

## Rollback

Last-known-good baseline: `main` immediately before this governed change is merged.

Rollback action: revert the canonical merge if this doctrine creates incorrect routing. If a live instance is later updated and fails acceptance, restore its last accepted configuration, preserve the failed evidence and route work through an available approved model without expanding authority.