# NoizyLab OS v1

**GO RUN FREE** — AI-managed, fully logged support platform.

## 3-Button Client UX

1. **Create Ticket** → `POST /public/tickets`
2. **Check Status** → `GET /public/status/:publicId?secret=...`
3. **Start Live Help** → `POST /public/live/join`

## Quick Start

```bash
# Install
npm install

# Create resources
npm run db:create
npm run r2:create

# Set secrets
wrangler secret put TURNSTILE_SECRET
wrangler secret put ACCESS_AUD

# Migrate database
npm run db:migrate

# Deploy
npm run deploy
```

## Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                         Cloudflare Edge                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────────┐  │
│  │   Worker     │  │     D1       │  │          R2              │  │
│  │   (Hono)     │◀▶│   Database   │  │   File Uploads           │  │
│  │              │  │              │  │                          │  │
│  └──────┬───────┘  └──────────────┘  └──────────────────────────┘  │
│         │                                                           │
│  ┌──────▼───────┐  ┌──────────────┐  ┌──────────────────────────┐  │
│  │   Durable    │  │  AI Gateway  │  │       Turnstile          │  │
│  │   Objects    │  │  (LLama 3)   │  │   (Bot Protection)       │  │
│  │   LiveRoom   │  │              │  │                          │  │
│  └──────────────┘  └──────────────┘  └──────────────────────────┘  │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │                    Cloudflare Access                          │  │
│  │                 (Staff Authentication)                        │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## API Routes

### Public (Turnstile protected)

| Method | Path | Description |
|--------|------|-------------|
| POST | `/public/tickets` | Create new ticket |
| GET | `/public/status/:publicId?secret=` | Check ticket status |
| POST | `/public/upload` | Upload file to ticket |
| POST | `/public/live/join` | Join live help session |

### Staff (Access-gated)

| Method | Path | Description |
|--------|------|-------------|
| GET | `/staff/tickets` | List tickets |
| GET | `/staff/tickets/:id` | Get ticket details |
| PATCH | `/staff/tickets/:id/status` | Change status |
| POST | `/staff/tickets/:id/message` | Send message |
| POST | `/staff/live/create` | Create live room |
| POST | `/staff/playbooks/apply` | Apply playbook |
| POST | `/staff/playbooks/complete` | Complete playbook |
| POST | `/staff/ai/triage` | Run AI triage |
| POST | `/staff/ai/summarize` | Generate summary |

### WebSocket

| Path | Description |
|------|-------------|
| `/ws/room/:roomId?token=&role=` | Live help room |

## Ticket Status Flow

```
TRIAGE → WAITING_CLIENT → WAITING_PARTS → SCHEDULED → IN_PROGRESS → DONE → BILLING
```

## Personas (P1-P12)

| ID | Name | Description |
|----|------|-------------|
| P1 | Tab Tornado | Too many browser tabs |
| P2 | Storage Closet | Disk full, hoarding files |
| P3 | Click-Yes Optimizer | Installed junk tools |
| P4 | Update Avoider | Refuses updates |
| P5 | Password Spiral | Locked out everywhere |
| P6 | Wi-Fi Whiplash | Connectivity drops |
| P7 | Peripheral Collector | Device chaos |
| P8 | Cloud Sync Tangle | Sync conflicts |
| P9 | Thermal Throttler | Overheating |
| P10 | Creative Chaos | App conflicts |
| P11 | Fine Yesterday | "Nothing changed" |
| P12 | Hardware Failing | Denial stage |

## Playbooks (PB1-PB12)

| ID | Name | For Persona |
|----|------|-------------|
| PB1 | Browser Diet | P1 |
| PB2 | Space Guard | P2 |
| PB3 | No Snake Oil | P3 |
| PB4 | Update Safe-Window | P4 |
| PB5 | Password Cleanroom | P5 |
| PB6 | Wi-Fi Stabilizer | P6 |
| PB7 | Peripheral Detox | P7 |
| PB8 | Cloud Sync Sanity | P8 |
| PB9 | Thermal Rescue | P9 |
| PB10 | Creative Workstation | P10 |
| PB11 | Hardware Truth Test | P11 |
| PB12 | Backup Bulletproof | P12 |

## Tags (≤3 per ticket)

**Performance:** PERF-TABS, PERF-STARTUP, PERF-BACKGROUND, PERF-THERMAL, PERF-LOWRAM

**Storage:** STOR-LOWDISK, STOR-DISKERRORS, STOR-EXTERNALDRIVE, FILE-PERMISSIONS, FILE-CORRUPTION

**Security:** SEC-PUP, SEC-BROWSERHIJACK, SEC-PHISH-ACCOUNT, SEC-AV-CONFLICT

**Accounts:** AUTH-APPLEID, AUTH-MICROSOFT, AUTH-GOOGLE, AUTH-MFA, AUTH-PASSWORDRESET

**Network:** NET-WIFIDROP, NET-DNS, NET-ROUTER, NET-VPN

**Updates:** UPD-OS, UPD-APP, DRV-PRINTER, DRV-USB, DRV-GPU, DRV-AUDIO

**Cloud:** SYNC-ICLOUD, SYNC-ONEDRIVE, SYNC-GDRIVE, SYNC-DUPES

**Hardware:** HW-SSD, HW-RAM, HW-BATTERY, HW-DUSTFAN, HW-LIQUID

**Behavior:** USR-CLICKYES, USR-NOBACKUP, USR-UPDATEAVOID, USR-DOWNLOADSCHAOS, USR-PASSWORDCHAOS

## Live Help Modes

Zero dead ends: automatic fallback when connection issues occur.

```
video → audio → chat+uploads → status-only
```

## Security

- **Turnstile** on: ticket create, upload, live join
- **Short-lived codes**: join code expires in 10 min
- **Secret access**: status page requires hashed secret
- **Staff only**: via Cloudflare Access (SSO/MFA)
