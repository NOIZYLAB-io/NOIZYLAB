# ⚡ NOIZYLAB GOD MODE SYSTEM
**PROTOCOL:** ZERO LATENCY | **AUTHORITY:** SHIRL & ENGR

> [!IMPORTANT]
> **SYSTEM STATUS:** GOD MODE ACTIVE.
> **INSTRUCTION:** ADHERE TO ZERO LATENCY & PREDICTIVE ACTIONS.

# MC96 Stack - Local-First Super-Cursor Scaffold

A production-ready, resilient AI agent routing system with circuit breakers, retry logic, observability, and Cloudflare Workers deployment.

## Features

✅ **Resilience**
- Circuit breaker pattern for fault tolerance
- Exponential backoff retry with jitter
- Per-agent timeout configuration
- Comprehensive error handling

✅ **Observability**
- Real-time metrics dashboard
- Latency, error rate, queue depth tracking
- Circuit state monitoring
- Audit logging with D1 integration

✅ **Accessibility (WCAG 2.2 AA)**
- Voice recognition support
- Switch scanning for assistive devices
- Keyboard-only navigation
- ARIA labels and live regions
- Reduced motion support

✅ **Type Safety**
- Full TypeScript support
- Strict type checking
- Type-safe adapters and routing

✅ **Testing**
- Vitest test suite
- Circuit breaker tests
- Retry logic tests
- Adapter tests with error paths

✅ **Deployment**
- Cloudflare Workers ready
- Wrangler configuration
- D1 database integration
- Multi-environment support (staging/production)

## Quick Start

### 1. Initialize Project

```bash
node mc96-cli.mjs init --scope @mc96 --name mc96-stack
node mc96-cli.mjs generate all
```

### 2. Create an Agent

```bash
node mc96-cli.mjs agent VisionFast --kind modern --mods vision,text
```

### 3. Setup Cloudflare (Optional)

```bash
node mc96-cli.mjs setup:cloudflare
# Edit wrangler.toml with your database IDs
# Copy .dev.vars.example to .dev.vars and add credentials
```

### 4. Run Tests

```bash
npm test
npm run test:coverage
```

### 5. Deploy

```bash
npm run deploy:staging
npm run deploy:prod
```

## Project Structure

```
mc96-stack/
├── apps/
│   ├── cockpit-ui/          # React dashboard with metrics
│   └── worker-edge/          # Cloudflare Worker
├── packages/
│   ├── attribute-router/     # Agent routing logic
│   ├── audit-core/           # Audit logging
│   ├── circuit-breaker/      # Circuit breaker implementation
│   ├── retry/                # Retry logic with backoff
│   ├── observability/        # Metrics collection
│   └── accessibility/        # Voice & switch scanning hooks
├── infra/
│   └── schemas/              # D1 database schemas
├── tests/                    # Test suite
└── manifests/
    ├── agents/               # Agent definitions
    └── prompts/              # Cursor prompt packs
```

## Architecture

### Request Flow

1. Request arrives at worker
2. Attributes extracted (modality, latency target, etc.)
3. Agent selected via weighted scoring
4. Circuit breaker checks agent health
5. Retry logic handles transient failures
6. Result returned with audit trail
7. Metrics updated in real-time

### Circuit Breaker States

- **CLOSED**: Normal operation, requests flow through
- **OPEN**: Too many failures, requests rejected immediately
- **HALF_OPEN**: Testing if service recovered, limited requests allowed

### Retry Strategy

- Exponential backoff: `baseDelay * (backoffFactor ^ attempt)`
- Jitter: Random variation to prevent thundering herd
- Configurable max attempts and delays
- Error filtering for retryable vs. non-retryable errors

## Development

### Local Development

```bash
# Start worker locally
npm run dev

# Start UI (if configured)
npm run dev:ui
```

### Testing

```bash
# Run all tests
npm test

# Watch mode
npm run test:watch

# Coverage report
npm run test:coverage
```

## Environment Variables

Copy `.env.example` to `.env` and configure:

- `CLOUDFLARE_ACCOUNT_ID`: Your Cloudflare account ID
- `CLOUDFLARE_API_TOKEN`: API token with Workers permissions
- `CLOUDFLARE_D1_DATABASE_ID`: D1 database ID for audit logs

## Cursor Integration

Use prompts from `manifests/prompts/cursor.md` in Cursor to:
- Create new agents
- Refactor for reliability
- Audit accessibility
- Add observability features

## License

MIT

