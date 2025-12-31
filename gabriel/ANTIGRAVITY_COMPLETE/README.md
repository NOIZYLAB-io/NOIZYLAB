# ═══════════════════════════════════════════════════════════════════════════════
# ANTIGRAVITY COMPLETE - MC96ECOUNIVERSE Deployment Package
# ═══════════════════════════════════════════════════════════════════════════════

## Overview

4 Cloudflare Workers forming the MC96ECOUNIVERSE infrastructure:

| Worker | Purpose | Key Features |
|--------|---------|--------------|
| **antigravity** | Command Hub | Circle of 8, DAZEFLOW, LIFELUV, NOIZYVOX, Dashboard |
| **gorunfree** | Voice Processor | Whisper AI transcription, command detection |
| **noizylab** | Repair System | Equipment registration, work orders |
| **mc96-network** | Orchestrator | Service discovery, health monitoring, relay |

## Quick Deploy

```bash
# From this directory
./DEPLOY_ALL.sh
```

Or deploy individually:

```bash
cd antigravity && npm install && wrangler deploy
cd gorunfree && npm install && wrangler deploy
cd noizylab && npm install && wrangler deploy
cd mc96-network && npm install && wrangler deploy
```

## Prerequisites

1. **Wrangler CLI**
   ```bash
   npm install -g wrangler
   wrangler login
   ```

2. **Create Resources** (one-time setup)
   ```bash
   # D1 Databases
   wrangler d1 create antigravity-db
   wrangler d1 create noizylab-db

   # KV Namespaces
   wrangler kv:namespace create "KV" --preview false
   ```

3. **Update wrangler.toml files** with your resource IDs

4. **Set Secrets**
   ```bash
   wrangler secret put ANTHROPIC_API_KEY
   ```

## Circle of 8

The core AI entities in ANTIGRAVITY:

| ID | Name | Role | Domain |
|----|------|------|--------|
| gabriel | GABRIEL | Warrior/Memory | Protection, memory, execution |
| shirl | SHIRL | Aunt/Guide | Guidance, nurture, wisdom |
| pops | POPS | Dad/Wisdom | Wisdom, patience, foundation |
| engr_keith | ENGR_KEITH | Engineering/R.K. | Engineering, systems, precision |
| dream | DREAM | Vision/Future | Vision, possibility, future |
| heaven | HEAVEN | Orchestrator | Harmony, coordination, flow |
| lucy | LUCY | Code Watcher | Code, quality, vigilance |
| sonic | SONIC | Audio/Creative | Sound, creativity, expression |

### Invoke Circle Members

```bash
curl -X POST https://antigravity.YOUR_SUBDOMAIN.workers.dev/circle/gabriel/invoke \
  -H "Content-Type: application/json" \
  -d '{"message": "Status report"}'
```

## Endpoints

### ANTIGRAVITY (Command Hub)

- `GET /` - Service info
- `GET /health` - Health check
- `GET /circle` - List Circle of 8
- `GET /circle/:id` - Get member info
- `POST /circle/:id/invoke` - Invoke member (AI chat)
- `GET /daze` - DAZEFLOW entries
- `GET /daze/today` - Today's truth
- `POST /daze` - Capture truth
- `POST /lifeluv/checkin` - Check-in for M3
- `GET /lifeluv/:user_id` - Get check-ins
- `POST /noizyvox/signup` - Artist signup
- `POST /ai/chat` - General AI chat
- `POST /ai/whisper` - Voice transcription
- `GET /dashboard` - Web dashboard
- `GET /init` - Initialize D1 tables

### GORUNFREE (Voice)

- `GET /` - Service info
- `GET /health` - Health check
- `POST /transcribe` - Transcribe audio (multipart)
- `POST /process` - Process text command
- `POST /speak` - Get TTS commands
- `GET /commands` - Command history

### NOIZYLAB (Repair)

- `GET /` - Service info
- `GET /health` - Health check
- `GET /equipment` - List equipment
- `POST /equipment` - Register equipment
- `GET /equipment/:id` - Get equipment
- `PUT /equipment/:id` - Update equipment
- `GET /workorders` - List work orders
- `POST /workorders` - Create work order
- `GET /workorders/:id` - Get work order
- `PUT /workorders/:id` - Update work order
- `POST /workorders/:id/notes` - Add note
- `GET /stats` - System stats
- `GET /init` - Initialize D1 tables

### MC96-NETWORK (Orchestrator)

- `GET /` - Service info
- `GET /health` - Health check
- `GET /services` - List all services with health
- `GET /services/:name` - Get service details
- `POST /discover` - Register service
- `GET /discover` - List registered services
- `POST /relay` - Relay request to service
- `POST /broadcast` - Broadcast to all services

## Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                     MC96-NETWORK                             │
│              (Service Discovery & Relay)                     │
└─────────────────────┬────────────────────────────────────────┘
                      │
      ┌───────────────┼───────────────┬───────────────┐
      ▼               ▼               ▼               ▼
┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
│ANTIGRAVITY│   │GORUNFREE │   │ NOIZYLAB │   │  OTHER   │
│  (Hub)   │   │ (Voice)  │   │ (Repair) │   │ Workers  │
├──────────┤   ├──────────┤   ├──────────┤   └──────────┘
│Circle of 8│   │Whisper AI│   │Equipment │
│DAZEFLOW  │   │Commands  │   │WorkOrders│
│LIFELUV   │   │TTS       │   │Stats     │
│NOIZYVOX  │   └──────────┘   └──────────┘
│Dashboard │
└──────────┘
```

## Local Development

```bash
# Terminal 1 - ANTIGRAVITY
cd antigravity && npm install && npm run dev
# Runs on http://localhost:8787

# Terminal 2 - GORUNFREE
cd gorunfree && npm install && wrangler dev --port 8788

# Terminal 3 - NOIZYLAB
cd noizylab && npm install && wrangler dev --port 8789

# Terminal 4 - MC96-NETWORK
cd mc96-network && npm install && wrangler dev --port 8790
```

## Post-Deploy Setup

1. **Initialize databases**
   ```bash
   curl https://antigravity.YOUR_SUBDOMAIN.workers.dev/init
   curl https://noizylab.YOUR_SUBDOMAIN.workers.dev/init
   ```

2. **Update MC96-NETWORK URLs** in wrangler.toml with actual deployed URLs

3. **Test health**
   ```bash
   curl https://mc96-network.YOUR_SUBDOMAIN.workers.dev/services
   ```

## License

MIT - NOIZYLAB / MC96ECOUNIVERSE 2025
