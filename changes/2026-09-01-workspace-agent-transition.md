# Governed change proposal: ChatGPT workspace-agent transition controls

Date: 2026-09-01
Status: PROPOSED — LIVE UPDATE PENDING
Class: MODEL / PLATFORM CHANGE
Owner accountability: Anthony
Release manager: Renee Archer
Governance gate: Sentinel
Behavioural acceptance: Mira
Commercial gate: Finlay
Provenance: Atlas

## Evidence

Primary source: OpenAI, "Introducing workspace agents in ChatGPT", originally published 2026-04-22 and carrying a current generally-available headline as inspected 2026-09-01.
URL: https://openai.com/index/introducing-workspace-agents-in-chatgpt/

The page states that workspace agents are generally available for ChatGPT Business, Enterprise and Edu and describes them as a Codex-powered evolution of GPTs that can run cloud workflows, use connected tools, preserve memory and be shared across a workspace or Slack. It also says GPTs remain available while teams test workspace agents and that conversion support is coming.

The same page still contains older research-preview and pricing wording. That internal inconsistency must be preserved as an entitlement and commercial verification requirement; it must not be resolved by inference.

## Proposed doctrine changes

1. **Availability is not entitlement.** Verify the actual K8 workspace plan, admin controls, regional availability and credit terms before proposing adoption.
2. **Evolution is not forced migration.** Existing commissioned GPTs remain the last-known-good baseline until a canary workspace agent passes accepted tests and Anthony approves promotion.
3. **Capability grants no authority.** Cloud execution, triggers, memory, Slack presence and connected tools inherit only explicitly approved K8 jurisdiction and permissions.
4. **Configuration is release-controlled.** Agent instructions, skills, connectors, triggers, memory sources and action scopes must be versioned and reviewed as one release package.
5. **Evidence follows the executing system.** A configured agent is implementation evidence; only controlled runs prove behaviour, and live business outcomes require runtime or transactional evidence.
6. **Source inconsistency triggers protective friction.** Conflicting availability or pricing text requires platform/plan verification and Finlay review rather than assumption.
7. **Rollback remains available.** Do not retire, overwrite or weaken the commissioned GPT baseline until canary acceptance and recovery have been demonstrated.

## Seats affected

- Renee: orchestration, release sequencing, canary and rollback ownership.
- Sentinel: connector, trigger, memory, permission and external-action boundaries.
- DevMate: agent configuration, versioning, integration tests and technical recovery.
- Mira: behavioural acceptance, hand-off quality and over/under-refusal testing.
- Atlas: source discrepancy, configuration provenance and evidence strength.
- Finlay: credit usage, plan cost, paid connectors and commercial viability.
- All accountable leads: new workspace-agent reach does not expand role or authority.

## No live mutation

This PR changes no live GPT, workspace agent, model selection, connector, Slack installation, trigger, credential, permission, subscription, production system or external communication.

Manual GPT Builder action required today: **none — do not convert or edit existing commissioned GPTs.**

If Anthony later approves a canary, the manual platform action is: create one private workspace agent from the accepted source package; connect only the minimum approved read scopes; import the accepted test scenarios; disable external actions and triggers until Sentinel and Mira accept the canary; retain the original GPT unchanged as rollback.

## Acceptance path

1. Static contract checks pass.
2. Atlas verifies the current OpenAI page, plan entitlement and the preserved availability/pricing discrepancy.
3. Finlay records YES / NO / FIND ALTERNATIVE for any credits, plan or connector cost.
4. Sentinel accepts permission, memory, trigger, Slack and external-action boundaries.
5. Mira accepts unit, adversarial and cross-seat behaviour.
6. Renee runs one private, reversible canary only after the above gates.
7. Anthony decides whether to commission, retain the existing GPT model, or find an alternative.
8. Observe; rollback to the commissioned GPT package if the canary overreaches, loses provenance, misroutes work or increases owner load.

## Rollback

Last-known-good baseline: the current commissioned GPT source packages and the main-branch workforce registry.

Rollback action: do not merge, or revert the merge if later accepted. If a canary has been created, disable it, disconnect added tools, retain its audit evidence and resume the unchanged commissioned GPT.
