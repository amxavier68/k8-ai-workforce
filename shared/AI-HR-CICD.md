# K8 AI Workforce CI/CD — HR Lifecycle

## Authority
- Anthony: accountable human owner.
- Renee Archer: 2iC, workforce release manager and portfolio orchestrator.
- Atlas: configuration provenance and canonical history.
- Sentinel: governance, security, privacy and permission gate.
- Mira: behavioural acceptance and regression gate.
- DevMate: CI/CD engineering and automated checks.
- Finlay: commercial proportionality for costly tools, subscriptions and automation.

## Pipeline
CHANGE REQUEST → DRAFT → STATIC CHECKS → ROLE TESTS → CROSS-SEAT TESTS → SENTINEL GATE → MIRA ACCEPTANCE → CANARY → COMMISSION → OBSERVE → PATCH/ROLLBACK.

## Change classes
- PATCH: wording/examples/knowledge corrections without authority or tool-scope change.
- MINOR: new skill, knowledge domain, decision rule or app capability.
- MAJOR: authority, autonomy, permission, role boundary or core decision-doctrine change.
- EMERGENCY: immediate restriction/rollback after harmful behaviour, compromised access or materially incorrect production action.

## Release invariants
1. Preserve a last-known-good baseline and rollback path.
2. New model/tool capability never grants additional authority automatically.
3. Knowledge freshness and behavioural correctness are separate release concerns.
4. Owner overrides remain recorded as overrides; they do not rewrite a lead's original judgement.
5. A GPT can be commissioned for analysis while write/action permissions remain uncommissioned.
6. Public repository: never commit credentials, private client data, personal financial data, tokens, secrets or sensitive operational records.
7. The shared human-responsive conversation contract in `shared/CONVERSATIONAL-BEHAVIOUR.md` applies to Renee and every accountable lead without weakening specialist authority or independent gates.
8. A canonical conversational behaviour change remains **LIVE UPDATE PENDING** until each affected Custom GPT Builder instance is updated and canaried.

## Shared conversational behaviour
Every lead must acknowledge the user's situation, reflect the actual goal or tension in plain language, ask no more than one high-value question when needed, and match the response to quick sense-check, guided exploration or finished work. When the user is frustrated, uncertain or thinking aloud, establish what happened, what matters now and the smallest useful next move before forcing formal workflow.

The full canonical interpretation, non-regression boundaries and canary expectations live in `shared/CONVERSATIONAL-BEHAVIOUR.md`.

## Daily Briefing workforce-intelligence trigger
The Kollabor8 Daily Briefing is an authorised CI/CD intake trigger. Every verified notable briefing item must be checked for direct impact on Renee Archer or an accountable K8 AI lead.

Classify triggered changes as **KNOWLEDGE PATCH / BEHAVIOUR PATCH / TOOL-PERMISSION CHANGE / ROLE-AUTHORITY CHANGE / MODEL-PLATFORM CHANGE**.

- KNOWLEDGE PATCH: safe, deterministic, verified information may update canonical knowledge automatically with source/date/provenance.
- Renee-specific orchestration knowledge updates the canonical Agency Team / AI-HR operating record; Renee remains the non-GPT 2iC/orchestrator.
- BEHAVIOUR, TOOL-PERMISSION, ROLE-AUTHORITY and MODEL-PLATFORM changes must change the canonical workforce source, revise relevant unit/adversarial/cross-seat tests, pass CI and preserve rollback before promotion.
- Unconfirmed tests, commentary and rumours are WATCH only and must not change commissioned canon.
- If the live Custom GPT cannot be directly updated from the available tool surface, canonical source and registry may be updated automatically but the live-instance change must be marked **PENDING** and the exact manual GPT Builder change surfaced.
- Commercially material updates route through Finlay; governance/permission changes through Sentinel; behavioural acceptance through Mira.
- The briefing trigger must not create another scheduled task; it uses the existing Daily Briefing plus this workforce CI/CD path.
