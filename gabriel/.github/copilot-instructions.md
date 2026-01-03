# GABRIEL - GitHub Copilot Instructions

## Project Overview

**GABRIEL** is NoizyLab's AI-powered board inspection and repair assistance system. The codebase includes:
- 17+ Cloudflare Workers for the NoizyLab OS platform
- 10+ ANTIGRAVITY creative workers
- React portal with AI vision capabilities
- Python automation and orchestration scripts
- MCP (Model Context Protocol) servers

## Architecture

```
GABRIEL/
├── src/workers/noizylab-v1/   # Main Cloudflare Worker API
│   ├── routes/                # Hono route handlers
│   ├── lib/                   # Utilities, AI, events
│   └── types.ts               # TypeScript type definitions
├── portal/
│   ├── api/                   # Portal API worker
│   ├── landing/               # Landing page
│   └── app/                   # React frontend
├── noizylab-os/workers/       # 17 specialized workers
├── ANTIGRAVITY_COMPLETE/      # 10 creative workers
├── 10_CORE/gabriel/           # Core Python scripts
├── 11_AGENTS/                 # 100+ AI agent configs
├── 12_MCP/                    # MCP server implementations
├── tools/ai-dev-toolkit/      # Python dev tools
└── automation/                # Workflow automation
```

## Tech Stack

| Layer | Technology |
|-------|------------|
| **Edge Compute** | Cloudflare Workers (TypeScript) |
| **Framework** | Hono (for Workers), React 18 (frontend) |
| **Database** | D1 (SQLite), KV (cache), R2 (storage) |
| **AI** | Claude 3.5/Opus, Gemini Flash, Workers AI |
| **Voice** | ElevenLabs TTS, Whisper transcription |
| **Payments** | Stripe |
| **Email** | Resend |
| **Python** | 3.11+, asyncio, Pydantic |

## Coding Conventions

### TypeScript (Cloudflare Workers)

```typescript
// Use Hono for routing
import { Hono } from 'hono';
import { Env, Ticket } from '../types';

const app = new Hono<{ Bindings: Env }>();

// Typed responses
app.get('/tickets/:id', async (c) => {
  const ticket = await c.env.DB.prepare(`
    SELECT * FROM tickets WHERE id = ?
  `).bind(c.req.param('id')).first<Ticket>();

  return c.json({ ticket });
});
```

- Use strict TypeScript mode
- Define all types in `types.ts`
- Use Zod for runtime validation
- Prefer `type` over `interface`
- Use async/await, never callbacks

### Python

```python
from pathlib import Path
from typing import Optional
from pydantic import BaseModel

class Config(BaseModel):
    """Configuration model with validation."""
    api_key: str
    timeout: int = 30

async def process_file(path: Path) -> Optional[dict]:
    """Process file and return result."""
    ...
```

- Type hints required everywhere
- Use `pathlib` for file operations
- Async/await for I/O
- Pydantic for data validation
- Google-style docstrings

### Shell

```bash
#!/bin/bash
set -euo pipefail

main() {
    local input="$1"
    # Always quote variables
    echo "Processing: ${input}"
}

main "$@"
```

## Key Types (noizylab-v1)

```typescript
// Status flow
type TicketStatus = 'TRIAGE' | 'WAITING_CLIENT' | 'WAITING_PARTS' | 'SCHEDULED' | 'IN_PROGRESS' | 'DONE' | 'BILLING';

// Event types (append-only audit log)
type EventType = 'CREATED' | 'STATUS_CHANGED' | 'MESSAGE_OUT' | 'MESSAGE_IN' | 'UPLOAD' | 'AI_TRIAGE' | 'EMAIL_SENT' | ...;

// Environment bindings
interface Env {
  DB: D1Database;
  UPLOADS: R2Bucket;
  AI: Ai;
  RESEND_API_KEY: string;
  STRIPE_SECRET_KEY: string;
}
```

## AI Integration Patterns

### Workers AI (built-in)
```typescript
const result = await c.env.AI.run('@cf/meta/llama-3.1-8b-instruct', {
  messages: [{ role: 'user', content: prompt }]
});
```

### External AI (Claude/Gemini)
```typescript
const response = await fetch('https://api.anthropic.com/v1/messages', {
  headers: { 'x-api-key': env.ANTHROPIC_KEY },
  body: JSON.stringify({ model: 'claude-3-5-sonnet-20241022', messages })
});
```

## Email Pattern (Resend)

```typescript
await fetch('https://api.resend.com/emails', {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${env.RESEND_API_KEY}`,
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    from: 'NoizyLab GABRIEL <noreply@noizylab.com>',
    to: [email],
    subject: 'Your subject',
    html: `<!DOCTYPE html>...`,
  }),
});
```

## Database Patterns (D1)

```typescript
// Parameterized queries (always)
const ticket = await env.DB.prepare(`
  SELECT * FROM tickets WHERE id = ? AND status = ?
`).bind(id, status).first<Ticket>();

// Batch operations
const results = await env.DB.batch([
  env.DB.prepare('INSERT INTO events ...').bind(...),
  env.DB.prepare('UPDATE tickets ...').bind(...),
]);
```

## File Organization Rules

1. **Types**: All in `types.ts` per worker
2. **Routes**: Split by domain (`/routes/staff.ts`, `/routes/public.ts`)
3. **Utilities**: Shared in `/lib/`
4. **Configs**: In `config/` or worker root
5. **No duplicate files**: Never create `-2`, `-backup` versions

## Anti-Patterns to Avoid

- ❌ Hardcoded API keys (use env vars)
- ❌ `any` type in TypeScript
- ❌ Callback hell (use async/await)
- ❌ Files > 500 lines (split by responsibility)
- ❌ Console.log in production (use structured logging)
- ❌ Untyped D1 queries (always use generics)
- ❌ String concatenation for SQL (use parameterized queries)

## Testing

```typescript
// Vitest for Workers
import { describe, it, expect } from 'vitest';
import { unstable_dev } from 'wrangler';

describe('API', () => {
  it('returns ticket', async () => {
    const worker = await unstable_dev('src/index.ts');
    const resp = await worker.fetch('/tickets/123');
    expect(resp.status).toBe(200);
  });
});
```

## Commit Messages

```
<type>(<scope>): <description>

feat(api): add email notifications for staff messages
fix(portal): resolve upload preview timeout
docs: update API documentation
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

## Circle of 8 Agents

When generating agent-related code, reference these personas:

| Agent | Role | Key Trait |
|-------|------|-----------|
| GABRIEL | System Bridge | Fierce protector |
| SHIRL | Business Ops | Organized, efficient |
| POPS | Creative Director | Wise, encouraging |
| ENGR_KEITH | Engineering | Precise, methodical |
| DREAM | Visionary | Future-focused |
| HEAVEN | Orchestrator | Harmonious |
| LUCY | Code Guardian | Vigilant, analytical |
| SONIC | Audio Engine | Fast, creative |

## Quick Reference

| Task | Location |
|------|----------|
| Add new API route | `src/workers/noizylab-v1/routes/` |
| Add new type | `src/workers/noizylab-v1/types.ts` |
| Email templates | `portal/api/src/email-notifications.ts` |
| Stripe webhooks | `portal/api/src/stripe.js` |
| AI prompts | `src/workers/noizylab-v1/lib/ai.ts` |
| Agent configs | `11_AGENTS/` |

---

*Branch: `3-set-up-copilot-instructions`*
*Updated: January 2026*
