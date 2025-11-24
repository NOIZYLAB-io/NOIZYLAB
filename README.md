# NOIZYLAB Email System

Production-ready email system built for Cloudflare Workers with comprehensive test coverage.

[![CI](https://github.com/noizyfish/NOIZYLAB/actions/workflows/ci.yml/badge.svg)](https://github.com/noizyfish/NOIZYLAB/actions/workflows/ci.yml)
[![Deploy](https://github.com/noizyfish/NOIZYLAB/actions/workflows/deploy.yml/badge.svg)](https://github.com/noizyfish/NOIZYLAB/actions/workflows/deploy.yml)
[![codecov](https://codecov.io/gh/noizyfish/NOIZYLAB/branch/main/graph/badge.svg)](https://codecov.io/gh/noizyfish/NOIZYLAB)

## Features

- **Multiple Email Providers**: MailChannels (free), Resend, SendGrid
- **Template Engine**: Variable substitution, conditionals, loops, HTML escaping
- **Rate Limiting**: Sliding window algorithm with KV storage
- **Email Logging**: Full audit trail with D1 database
- **Async Processing**: Queue-based email delivery
- **Scheduled Emails**: Send emails at a specific time
- **Idempotency**: Prevent duplicate sends
- **Health Checks**: Detailed component status
- **TypeScript**: Full type safety with strict mode
- **80%+ Test Coverage**: Unit and integration tests

## Quick Start

### Prerequisites

- Node.js 18+
- Cloudflare account
- Wrangler CLI

### Installation

```bash
# Clone the repository
git clone https://github.com/noizyfish/NOIZYLAB.git
cd NOIZYLAB

# Install dependencies
npm install

# Create KV namespace
wrangler kv:namespace create EMAIL_KV
wrangler kv:namespace create EMAIL_KV --preview

# Create D1 database
wrangler d1 create noizylab-email-logs

# Run migrations
wrangler d1 migrations apply noizylab-email-logs

# Update wrangler.toml with your namespace/database IDs

# Start development server
npm run dev
```

### Configuration

Update `wrangler.toml` with your Cloudflare resources:

```toml
[[kv_namespaces]]
binding = "EMAIL_KV"
id = "your-kv-namespace-id"

[[d1_databases]]
binding = "EMAIL_DB"
database_name = "noizylab-email-logs"
database_id = "your-d1-database-id"
```

Set secrets for email providers:

```bash
# Optional: Resend API key
wrangler secret put RESEND_API_KEY

# Optional: SendGrid API key
wrangler secret put SENDGRID_API_KEY

# Optional: DKIM configuration
wrangler secret put DKIM_PRIVATE_KEY
wrangler secret put DKIM_DOMAIN
wrangler secret put DKIM_SELECTOR
```

## API Reference

### Send Email

```bash
POST /emails
Content-Type: application/json

{
  "to": "recipient@example.com",
  "subject": "Hello World",
  "html": "<h1>Hello!</h1>",
  "text": "Hello!"
}
```

**Response:**

```json
{
  "success": true,
  "data": {
    "messageId": "noizy_abc123_xyz789",
    "status": "sent",
    "timestamp": "2025-01-01T00:00:00.000Z"
  },
  "meta": {
    "requestId": "req_abc123",
    "rateLimit": {
      "remaining": 99,
      "limit": 100,
      "resetAt": 1704067200
    }
  }
}
```

### Send with Template

```bash
POST /emails
Content-Type: application/json

{
  "to": "recipient@example.com",
  "subject": "Welcome",
  "templateId": "welcome-email",
  "templateData": {
    "name": "John",
    "company": "Acme Inc"
  }
}
```

### Get Email Status

```bash
GET /emails/{messageId}
```

### List Emails

```bash
GET /emails?limit=50&offset=0&status=sent
```

### Create Template

```bash
POST /templates
Content-Type: application/json

{
  "id": "welcome-email",
  "name": "Welcome Email",
  "subject": "Welcome to {{company}}, {{name}}!",
  "html": "<h1>Hello {{name}}!</h1><p>Welcome to {{company}}.</p>",
  "text": "Hello {{name}}! Welcome to {{company}}."
}
```

### Preview Template

```bash
POST /templates/{id}/preview
Content-Type: application/json

{
  "data": {
    "name": "John",
    "company": "Acme Inc"
  }
}
```

### Health Check

```bash
GET /health          # Simple health check
GET /health/detailed # Component status
GET /health/live     # Liveness probe
GET /health/ready    # Readiness probe
```

## Template Syntax

### Variables

```html
{{name}}              <!-- Simple variable -->
{{user.name}}         <!-- Nested property -->
{{name|Guest}}        <!-- Default value -->
```

### Conditionals

```html
{{#if premium}}
  <p>Premium feature!</p>
{{/if}}
```

### Loops

```html
<ul>
{{#each items}}
  <li>{{@index}}: {{name}}</li>
{{/each}}
</ul>
```

Loop variables:
- `{{@index}}` - Current index (0-based)
- `{{@first}}` - True if first item
- `{{@last}}` - True if last item

## Email Providers

### MailChannels (Default)

Free email sending for Cloudflare Workers. No API key required.

```javascript
// Automatically used when no other provider is configured
```

### Resend

```bash
wrangler secret put RESEND_API_KEY
# Enter your API key starting with "re_"
```

### SendGrid

```bash
wrangler secret put SENDGRID_API_KEY
# Enter your API key starting with "SG."
```

## Rate Limiting

Default: 100 requests per hour per client.

Configure in `wrangler.toml`:

```toml
[vars]
RATE_LIMIT_MAX_REQUESTS = "100"
RATE_LIMIT_WINDOW_SECONDS = "3600"
```

Rate limit headers:
- `X-RateLimit-Limit` - Maximum requests
- `X-RateLimit-Remaining` - Remaining requests
- `X-RateLimit-Reset` - Reset timestamp
- `Retry-After` - Seconds until reset (when limited)

## Development

### Commands

```bash
npm run dev           # Start development server
npm run test          # Run tests
npm run test:watch    # Run tests in watch mode
npm run test:coverage # Run tests with coverage
npm run lint          # Run ESLint
npm run lint:fix      # Fix ESLint issues
npm run typecheck     # Run TypeScript check
npm run format        # Format code with Prettier
npm run validate      # Run all checks
```

### Project Structure

```
NOIZYLAB/
├── src/
│   ├── index.ts           # Main entry point
│   ├── types/             # TypeScript types & Zod schemas
│   ├── errors/            # Custom error classes
│   ├── utils/             # Utility functions
│   ├── services/          # Business logic
│   │   ├── email-service.ts
│   │   ├── rate-limiter.ts
│   │   ├── template-engine.ts
│   │   └── providers/     # Email providers
│   ├── routes/            # API routes
│   └── middleware/        # Hono middleware
├── tests/
│   ├── unit/              # Unit tests
│   └── integration/       # Integration tests
├── migrations/            # D1 database migrations
├── .github/workflows/     # CI/CD pipelines
├── wrangler.toml          # Cloudflare config
├── vitest.config.ts       # Test config
└── package.json
```

## Deployment

### Manual Deployment

```bash
# Deploy to staging
npm run deploy -- --env staging

# Deploy to production
npm run deploy -- --env production
```

### Automated Deployment

Push to `main` branch triggers:
1. CI checks (lint, typecheck, test)
2. Deploy to staging
3. Health check
4. Deploy to production
5. Create release

## Error Codes

| Code | Description |
|------|-------------|
| `VALIDATION_ERROR` | Invalid request data |
| `RATE_LIMIT_EXCEEDED` | Too many requests |
| `AUTHENTICATION_ERROR` | Invalid credentials |
| `PROVIDER_ERROR` | Email provider failed |
| `TEMPLATE_NOT_FOUND` | Template doesn't exist |
| `TEMPLATE_RENDER_ERROR` | Template rendering failed |
| `ATTACHMENT_TOO_LARGE` | Attachment exceeds limit |
| `RECIPIENT_BLOCKED` | Email address blocked |
| `IDEMPOTENCY_CONFLICT` | Duplicate request |
| `INTERNAL_ERROR` | Server error |

## License

MIT License - see [LICENSE](LICENSE) for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Write tests for your changes
4. Ensure all tests pass
5. Submit a pull request

## Support

- [GitHub Issues](https://github.com/noizyfish/NOIZYLAB/issues)
- [Documentation](https://docs.noizylab.com)
