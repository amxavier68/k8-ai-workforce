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
