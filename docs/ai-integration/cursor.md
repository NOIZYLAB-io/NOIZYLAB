# Cursor prompt pack (local-first)

## Agent scaffold

"Create a new agent named VisionFast: vision + text. Strict types, resilience (retries, timeouts, circuit breaker), unit tests, audit hooks. Wire into attribute-router and adapters."

## Reliability refactor

"Convert adapters to async/await, add exponential backoff with jitter and per-adapter timeouts. Implement circuit breaker. Generate Vitest coverage for error paths."

## Accessibility audit

"WCAG 2.2 AA: aria-live narration, focus-visible, switch scanning interval control, keyboard-only navigation tests."

## Observability

"Add tiles for latency, error rate, queue depth, circuit state. Write labeled audit traces and show cockpit summaries."

