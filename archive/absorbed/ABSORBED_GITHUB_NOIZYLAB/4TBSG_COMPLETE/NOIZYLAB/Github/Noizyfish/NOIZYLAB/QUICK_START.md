# NOIZYLAB OS - Quick Start

## 🚀 Setup (One Command)

```bash
cd noizylab-os
./scripts/bootstrap.sh
```

## 📋 Core Scripts

### 1. Super-Worker
**Location:** `workers/super-worker/src/index.ts`

Routes:
- `/api/intake` - Client intake system
- `/api/ai-router` - AI routing
- `/api/event` - Event handling

### 2. D1 Database
**Location:** `migrations/sql/001_initial_schema.sql`

Tables:
- `clients` - Client data
- `tickets` - Support tickets
- `devices` - Device inventory
- `events` - Event log

Apply migration:
```bash
wrangler d1 migrations apply noizylab-db --local
wrangler d1 migrations apply noizylab-db --remote
```

### 3. AI Router
**Location:** `ai/router/src/index.ts`

Providers:
- Cloudflare AI (default)
- Claude
- Gemini
- Copilot

### 4. Generate All Components
```bash
./scripts/generate-all.sh
```

Creates:
- Portal UI v2
- Intake iPad App endpoint
- MC96 Dashboard API
- TeamViewer Integration
- Auto-deployment script
- Export script

## 🚀 Deploy

```bash
./scripts/deploy.sh
```

## 📦 Export

```bash
./scripts/export-repo.sh
```

Creates: `noizylab-os-YYYYMMDD_HHMMSS.tar.gz`

## ⚙️ Configuration

Edit `workers/super-worker/wrangler.toml`:
- Add D1 database ID
- Add KV namespace IDs
- Add R2 bucket name
- Add API keys/URLs

