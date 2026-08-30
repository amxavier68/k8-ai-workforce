# Weekend intelligence knowledge patch proposal — 2026-08-31

Status: PROPOSED — LIVE UPDATE PENDING
Class: KNOWLEDGE PATCH
Coverage: consequential verified developments identified after the 2026-08-28 briefing
Owner accountability: Anthony
Release manager: Renee Archer
Provenance authority: Atlas

This proposal changes no live GPT, role, permission, credential, production site, published content, subscription or external communication.

## 1. Australian government-backed market education now explicitly joins SEO and AI search

Source: business.gov.au, page published 2026-08-28  
URL: https://business.gov.au/events-and-training/being-found-through-seo-and-ai-search-in-2026

Affected leads: Renee, Clarity, Finlay, Atlas

Change: an Australian Government-sponsored small-business workshop now explicitly teaches visibility across Google, ChatGPT, Claude, Gemini, TikTok and off-site discovery factors. The event listing establishes current market education demand; it does not validate every statistic or tactic repeated by the third-party organiser.

Operational effect: treat combined SEO/AI-search literacy as a recognisable client education need. K8 recommendations must still be evidence-led, platform-specific and scoped through Finlay before any paid offer or spend.

## 2. Google's site reputation enforcement now differs inside and outside the EEA

Source: Google Search Quality team, 2026-08-28; change effective 2026-08-30  
URL: https://developers.google.com/search/blog/2026/08/update-site-reputation-policy

Affected leads: Renee, Clarity, Kai, Atlas

Change: outside the EEA, a site-reputation manual action continues to affect the relevant site section. Inside the EEA, the manual-action effect will not apply, but Google may separate the affected section so it ranks independently from the host site's reputation.

Operational effect: do not interpret hosted third-party content, parasite SEO or borrowed-domain publishing as safe. Record geography and Search Console evidence before diagnosing an affected property.

## 3. Shopify token refresh gains a bounded recovery path

Source: Shopify Developer Changelog, 2026-08-28  
URL: https://shopify.dev/changelog/more-resilient-refreshes-for-expiring-offline-access-tokens

Affected leads: Renee, DevMate, Sentinel, Atlas

Change: Shopify apps using expiring offline access tokens can retry the previously stored refresh token until the replacement is used, bounded by 30 days from first use and the normal 90-day token lifetime.

Operational effect: this is recovery behaviour, not permission expansion. Continue serialising refresh operations, storing token pairs atomically and using the newest token. No DFG action applies because DFG remains on WooCommerce.

## 4. Chrome email verification remains an origin trial with explicit compatibility limits

Source: Chrome for Developers, 2026-08-13  
URL: https://developer.chrome.com/blog/email-verification-august-2026

Affected leads: Renee, DevMate, Mira, Sentinel, Atlas

Change: Chrome's Email Verification origin trial can reduce email-link/OTP switching, but remains desktop-only through Chrome 152, lacks third-party origin-trial support, and introduces an HTTP Message Signatures format change in Chrome 153.

Operational effect: treat it as progressive-enhancement research, not a replacement for cross-browser email verification or 2FA. Do not introduce it into K8 or client production flows without compatibility, fallback, privacy and security testing.

## Acceptance

- Atlas verifies source/date/scope and preserves test-vs-release qualifiers.
- Sentinel verifies that recovery behaviour and origin trials grant no new permission or authority.
- Mira validates any later UX behaviour proposal separately.
- Finlay gates any commercial packaging or paid-tool implication.
- Renee decides whether these proposals are promoted to canonical workforce knowledge.
