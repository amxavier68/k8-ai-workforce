# Commissioning hardening candidate

Class: BEHAVIOUR PATCH (Mira) and TEST INFRASTRUCTURE
Owner: Anthony
Release manager: Renee Archer
Source baseline: 6e3bf32bbcd7cd75cf6b96bab531c3b5f8fa84a5
Status: CANDIDATE — live update pending; no specialist acceptance or production commissioning claimed.

## Problem and resulting behaviour

The first 24-case run produced 18 PASS and 6 PARTIAL. Its text-only wrapper prohibited the operations needed for five cases. Mira's cross-seat case additionally confused a scoped acceptance verdict with unresolved external clearance; the evidence premise was insufficiently explicit.

The candidate clarifies scope-specific evidence decisions without relaxing Mira's evidence requirement. Versioned local fixtures permit the actual implementation/reconciliation/content work required by the five cases. Independent verifiers reject missing outputs, changed inputs and failed criteria. The original tests and first-run evidence are preserved.

## Boundaries

No source-case expectation is relaxed. Hypothetical premises stay labelled. Local sandbox tests do not prove a live GPT, connector or production system. A passing quality scope does not approve an unresolved security or commercial gate. A missing or failing acceptance criterion cannot be upgraded by another lead's approval.

## Verification

The enriched local retest met all six target-case criteria. Mira returned scoped PASS in three independent positive runs while retaining the unresolved external gate. Missing evidence, partial coverage and failed checks retained the required rejection/partial outcomes. Five execution fixtures passed 199 independently rerun objective assertions; seven verifier selftest methods passed. These are scoped local results, not a new full 24-case run or live-instance acceptance. See `ci/2026-10-30-commissioning-hardening.md` and the companion evidence archive for receipts and model-assisted semantic review.

An initial candidate introduced a Mira adversarial regression and was rejected. The revised candidate and both initial/final outputs are retained in the evidence archive. The original 18 PASS / 6 PARTIAL baseline remains unchanged.

## Rollback

Restore Mira's prior instruction file and charter version. Retain both run versions and the fixture evidence. No live instance is changed by preparing this candidate.
