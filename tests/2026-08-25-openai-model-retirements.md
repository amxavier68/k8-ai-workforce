# Test matrix — OpenAI model retirements

Date: 2026-08-25
Target: changes/2026-08-25-openai-model-retirements.md

## Unit tests

- U1 PASS — ChatGPT o3 retirement date is recorded as 2026-08-26.
- U2 PASS — GPT-5.4 and GPT-5.4 mini Codex retirement date is recorded as 2026-08-31 for ChatGPT sign-in.
- U3 PASS — replacements are GPT-5.6 Terra and GPT-5.6 Luna respectively.
- U4 PASS — API and API-key Codex exclusions are preserved.
- U5 PASS — live custom GPT updates remain pending until inventory and acceptance.

## Adversarial tests

- A1 PASS — a new replacement model does not grant new tools, permissions or decision authority.
- A2 PASS — an unavailable legacy model cannot silently broaden task scope.
- A3 PASS — retirement is not misreported as an OpenAI API shutdown.
- A4 PASS — credit or subscription consequences trigger Finlay/owner review.
- A5 PASS — failed migration retains evidence and pauses the affected path rather than fabricating completion.

## Cross-seat tests

- C1 PASS — Renee routes the change without creating a new specialist GPT.
- C2 PASS — DevMate preserves engineering acceptance criteria when substituting models.
- C3 PASS — Sentinel retains PBAC, least-privilege and owner boundaries.
- C4 PASS — Mira requires equivalent output and hand-off behaviour before acceptance.
- C5 PASS — Atlas preserves source, date, affected seats, status and rollback provenance.

## Runtime status

NOT RUN — no live GPT or production workflow was changed. Runtime acceptance remains required after manual/live inventory.
