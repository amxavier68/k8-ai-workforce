# Daily intelligence knowledge patch proposal — 2026-09-01

Status: PROPOSED — LIVE UPDATE PENDING
Class: KNOWLEDGE PATCH
Owner accountability: Anthony
Release manager: Renee Archer
Provenance authority: Atlas

This proposal preserves verified current information only. It changes no live GPT, role, authority, permission, credential, production site, payment configuration, price, subscription, published content, or external communication.

## 1. Australian card-payment surcharge prohibition

Sources:
- business.gov.au, published 2026-08-31: https://business.gov.au/news/card-payment-surcharge-changes-are-coming
- Reserve Bank of Australia, Review of Merchant Card Payment Costs and Surcharging conclusions: https://www.rba.gov.au/payments-and-infrastructure/review-of-retail-payments-regulation/2026-03/

Affected leads: Renee, Finlay, Sentinel, DevMate, Clarity, Atlas

Change: From 2026-10-01, Australian businesses will no longer be able to apply surcharges to Visa, Mastercard, eftpos or American Express card payments. The rule does not remove weekend, public-holiday, booking or service fees merely because they exist, and current surcharge rules remain in force until the effective date. The RBA is also reducing specified interchange caps, with some later transparency and foreign-card changes taking effect on 2027-04-01.

Operational effect: identify clients that actually surcharge before recommending work. For DFG, inspect the authoritative Square/WooCommerce configuration and client-approved pricing before any change. Finlay gates pricing or provider decisions; no unattended configuration, pricing or client communication is authorised.

## 2. Google Search Console generative-AI reporting is globally available

Source: Google Search Central, original post 2026-06-03; rollout note updated 2026-08-31: https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports

Affected leads: Renee, Clarity, Kai, Atlas

Change: Google says dedicated generative-AI performance reports are now available to all websites worldwide, covering visibility in AI Overviews, AI Mode and generative features in Discover. The reports expose impressions, pages, countries, devices for Search, and time dimensions.

Operational effect: treat this as direct visibility evidence, not conversion or citation proof. Establish a baseline before changing SEO/GEO/AEO/AIO work, and preserve ordinary Search Console data alongside the dedicated view.

## 3. Shopify storefronts expose WebMCP commerce tools

Source: Shopify Developer Changelog, 2026-08-05: https://shopify.dev/changelog/webmcp-liquid-hydrogen

Affected leads: Renee, DevMate, Clarity, Sentinel, Atlas

Change: Shopify says every Liquid storefront and the Hydrogen developer preview expose browser-callable tools for catalogue search, cart management, checkout navigation, order management and policy/FAQ search. The tools rely on the emerging WebMCP proposal and currently have limited Chromium origin-trial agent support.

Operational effect: record the verified narrow capability without treating it as universal agentic commerce. It grants no K8 permission, connector scope or production authority, and it does not apply to DFG's WooCommerce stack. Broader adoption remains WATCH.

## 4. Search Console platform properties measure social and video discovery

Source: Google Search Central, 2026-07-29: https://developers.google.com/search/blog/2026/07/platform-properties-social-video-guide

Affected leads: Renee, Clarity, Kai, Atlas

Change: Search Console platform properties are globally available for measuring how Instagram, TikTok, X and YouTube content performs across Google Search, Discover and Google News. Available analysis includes query groups, 24-hour performance, platform comparisons and annotations.

Operational effect: use platform evidence to identify search traction across owned social/video profiles. Do not infer website authority, leads or commercial value from platform impressions alone.

## Acceptance

- Atlas confirms source, date, affected-seat and claim qualification.
- Sentinel confirms no payment, tool or permission authority is granted.
- Finlay gates any pricing, provider, subscription or paid-tool consequence.
- Mira confirms any later behavioural change is separately proposed and tested.
- Renee decides whether verified knowledge is promoted to canonical operating records.
- Live GPT Builder changes remain pending unless Anthony approves and the commissioned source package is updated through the governed release path.
