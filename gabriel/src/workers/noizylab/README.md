# NoizyLab OS Worker

## Quick Start

```bash
# Install dependencies
npm install

# Run locally
npm run dev

# Deploy to Cloudflare
npm run deploy
```

## Setup

### 1. Create D1 Database

```bash
wrangler d1 create noizylab-db
```

Update `wrangler.toml` with the database ID.

### 2. Create R2 Bucket

```bash
wrangler r2 bucket create noizylab-uploads
```

### 3. Run Migrations

```bash
# Local development
npm run db:migrate:local

# Production
npm run db:migrate
```

### 4. Set Secrets

```bash
wrangler secret put TURNSTILE_SECRET_KEY
wrangler secret put STRIPE_WEBHOOK_SECRET
wrangler secret put EMAIL_API_KEY
wrangler secret put STAFF_API_KEY
```

## API Endpoints

### Tickets
- `POST /api/tickets` - Create ticket
- `GET /api/tickets` - List tickets
- `GET /api/tickets/:id` - Get ticket
- `PUT /api/tickets/:id` - Update ticket
- `POST /api/tickets/:id/events` - Add event

### Status (Public)
- `GET /api/status/:ticketId/public` - Public status
- `GET /api/status/:ticketId/timeline` - Event timeline

### Uploads
- `POST /api/uploads/presign` - Get upload URL
- `POST /api/uploads/complete` - Confirm upload

### Live Help
- `POST /api/live/session/create` - Start session
- `GET /api/live/session/:id` - Get session
- `POST /api/live/session/:id/join` - Join session
- `POST /api/live/session/:id/mode` - Change mode
- `POST /api/live/session/:id/end` - End session
- `GET /api/live/room/:id` - WebSocket room

### AI
- `POST /api/ai/triage` - Auto-triage ticket
- `POST /api/ai/draft` - Generate reply
- `POST /api/ai/summary` - Summarize session
- `POST /api/ai/followups` - Suggest followups

### Staff
- `GET /api/staff/board` - Kanban board
- `POST /api/staff/ticket/:id/action` - Quick actions
- `GET /api/staff/metrics` - Dashboard metrics

### Webhooks
- `POST /api/webhooks/email/inbound` - Email webhook
- `POST /api/webhooks/stripe` - Stripe webhook

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      Cloudflare Edge                        │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌──────────────┐  ┌─────────────────────┐│
│  │   Worker    │  │   D1 (SQL)   │  │   R2 (Files)        ││
│  │   (Hono)    │◀▶│   Tickets    │  │   Screenshots       ││
│  │             │  │   Events     │  │   Attachments       ││
│  └──────┬──────┘  └──────────────┘  └─────────────────────┘│
│         │                                                   │
│  ┌──────▼──────┐  ┌──────────────┐  ┌─────────────────────┐│
│  │  Durable    │  │  AI Gateway  │  │   Turnstile         ││
│  │  Objects    │  │  (GPT-4)     │  │   (Bot Protection)  ││
│  │  ChatRoom   │  │  Triage      │  │                     ││
│  │  Presence   │  │  Drafts      │  │                     ││
│  └─────────────┘  └──────────────┘  └─────────────────────┘│
└─────────────────────────────────────────────────────────────┘
```

## Personas (P1-P12)

| ID | Name | Description |
|----|------|-------------|
| P1 | Tab Tornado | 50+ tabs, memory problems |
| P2 | Storage Closet | Never deletes, can't find files |
| P3 | Click-Yes Optimizer | Has 5 "optimizer" tools |
| P4 | Update Avoider | Windows 7 forever |
| P5 | Password Spiral | Can't remember anything |
| P6 | Wi-Fi Whiplash | Always switching networks |
| P7 | Peripheral Collector | Too many devices |
| P8 | Cloud Sync Tangle | Files everywhere |
| P9 | Thermal Throttler | Laptop burns, fan screams |
| P10 | Creative Chaos | Designer in app hell |
| P11 | Fine Yesterday | Nothing changed, everything broken |
| P12 | Hardware Failing Quietly | Denial phase |

## Playbooks (PB1-PB12)

| ID | Name | Persona |
|----|------|---------|
| PB1 | Browser Diet | P1 |
| PB2 | Space Guard | P2 |
| PB3 | No Snake Oil | P3 |
| PB4 | Update Safe-Window | P4 |
| PB5 | Password Cleanroom | P5 |
| PB6 | Wi-Fi Stabilizer | P6 |
| PB7 | Peripheral Detox | P7 |
| PB8 | Cloud Sync Sanity | P8 |
| PB9 | Thermal Rescue | P9 |
| PB10 | Creative Workstation Tune | P10 |
| PB11 | Hardware Truth Test | P11 |
| PB12 | Backup Bulletproof | P12 |
