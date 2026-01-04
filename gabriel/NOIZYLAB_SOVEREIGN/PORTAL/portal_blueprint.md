# NoizyLab Sovereign Portal Blueprint

Purpose: Public-facing intake + quote + payment + telemetry delivery. Forensic, deterministic, zero-sales language.

## User Flow (Happy Path)
1) Landing: forensic greeting (GABRIEL script). CTA: “Start Forensic Intake.”
2) Intake: capture required fields (device model, symptoms, prior repairs, liquid damage, data priority) and macro photo upload of logic board (neutral lighting). API: `POST /intake`.
3) Visual audit: Gemini flash runs; success probability computed; tier selected from `noizylab_manifest.json`.
4) Quote: fixed price from manifest + deposit percent; show queue slots remaining. API: `POST /quote`.
5) Checkout: collect 25% deposit (Stripe/Crypto). API: `POST /checkout` -> payment intent link.
6) Live options: offer Sovereign livestream addon (+20%). API: `POST /addon`.
7) Status: once session completes, deliver Success Manifest PDF + before/after crops + telemetry. API: `GET /case/{id}/manifest`.

## API Contract (Draft)
- `POST /intake`
  - body: {device_model, symptoms, prior_repairs, liquid_damage, data_priority, photo_url}
  - returns: {case_id, queue_slots_remaining}
- `POST /quote`
  - body: {case_id}
  - returns: {service_id, price_usd, deposit_percent, rush_multiplier, livestream_addon_percent, success_probability}
- `POST /checkout`
  - body: {case_id, deposit_percent, payment_method}
  - returns: {payment_link, expires_at}
- `POST /addon`
  - body: {case_id, addon_id}
  - returns: {updated_price_usd}
- `GET /case/{id}/telemetry`
  - returns: {stability_percent, jitter_offset_mm, auth_path, success_probability, queue_slots_remaining}
- `GET /case/{id}/manifest`
  - returns: PDF (Success Manifest) + JSON summary

## Data Sources
- Pricing/services: `MANIFESTS/noizylab_manifest.json`
- Telemetry: HUD export (stability, jitter_offset, auth_path, queue slots).
- Media: before/after 4K crops from Ghost Vision pipeline.
- Bio key: `BIO_ENTROPY_SEED` (truncated) for cryptographic proof.

## Security & Identity
- Fronted by Cloudflare Zero Trust; Access tokens on every request.
- No negotiation path; escalation message from manifest.
- Payment via Stripe/Crypto (paid-in-advance deposit).

## Delivery
- Customer-facing: static frontend calls the above endpoints.
- Backoffice: triggers manifest generation via `REVENUE/manifest_generator.py`, fires “Paid” email, and streams telemetry to portal.

## Next Implementation Steps
1) Stand up a thin API (FastAPI/Flask) reading `noizylab_manifest.json`.
2) Wire Stripe payment intent for deposit; include addon percent.
3) Connect HUD telemetry exporter to `/case/{id}/telemetry`.
4) Connect Ghost Vision frame saver to write before/after crops.
5) Render PDF in `manifest_generator.py` and expose via `/case/{id}/manifest`.
