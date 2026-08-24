# Change proposal — OpenAI model retirements

Date: 2026-08-25
Class: MODEL / PLATFORM CHANGE
Status: PROPOSED — LIVE UPDATE PENDING
Owner accountability: Anthony
Release manager: Renee Archer
Governance acceptance: Sentinel
Behavioural acceptance: Mira

## Verified triggers

1. OpenAI o3 retires from ChatGPT on 2026-08-26 after a 90-day sunset. API access is unchanged.
   Source: https://help.openai.com/en/articles/9624314-model-release-notes
2. GPT-5.4 and GPT-5.4 mini retire in Codex on 2026-08-31 for users signed in with ChatGPT. OpenAI directs migration to GPT-5.6 Terra and GPT-5.6 Luna respectively. API-key Codex and OpenAI API access are unchanged.
   Source: https://help.openai.com/en/articles/11481834-chatgpt-rate-card-business-enterpriseedu

## Affected seats

Renee Archer, DevMate, Mira, Sentinel, Atlas.

## Proposed behaviour

- Detect the available model at execution time; do not assume a retired model remains selectable.
- Route former GPT-5.4 Codex work to GPT-5.6 Terra and former GPT-5.4 mini work to GPT-5.6 Luna when signed in with ChatGPT.
- Do not describe o3 or GPT-5.4 API access as retired.
- Preserve task acceptance criteria, evidence requirements, PBAC, owner accountability and least privilege through a model substitution.
- Do not purchase credits, alter subscriptions, or raise reasoning spend without Finlay review and owner authority.
- Do not modify live custom GPT instructions until the affected live references have been inventoried and Mira/Sentinel acceptance passes.

## Rollback

The main branch before this proposal remains the last-known-good canonical baseline. If replacement-model tests fail, pause the affected automated coding path, retain the existing task specification and evidence, and route execution to an available approved model without expanding authority. API-key workflows remain unchanged unless separately proposed.

## Acceptance gate

All unit, adversarial and cross-seat cases in `tests/2026-08-25-openai-model-retirements.md` pass; Sentinel confirms no authority expansion; Mira confirms equivalent hand-off behaviour; any live GPT Builder reference is updated manually and verified before status changes from LIVE UPDATE PENDING.
