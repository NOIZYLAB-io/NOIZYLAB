# NOIZYLAB OS - Core Scripts

Battle-ready, copy-paste scripts. No fluff.

## 🚀 Quick Start

```bash
# 1. Bootstrap entire workspace
./scripts/bootstrap.sh

# 2. Setup super-worker
./scripts/super-worker-setup.sh

# 3. Create D1 migration
./scripts/d1-migration.sh noizylab-db

# 4. Setup AI router
./scripts/ai-router-setup.sh
```

## 📋 Scripts

### 1. `bootstrap.sh`
Creates full repo structure:
- Workers directories
- Portal structure
- AI router setup
- TypeScript config
- Package.json
- Cursor rules

### 2. `super-worker-setup.sh`
Sets up main Cloudflare Worker:
- Routing logic
- D1/KV/R2 bindings
- API handlers

### 3. `d1-migration.sh`
Creates D1 database migrations:
- Initial schema
- Clients, intake, events, AI tables
- Indexes

### 4. `ai-router-setup.sh`
Multi-AI provider router:
- OpenAI
- Anthropic
- Google
- Auto-routing

## ⚡ Usage

All scripts are executable. Run from `noizylab-os/` directory.

```bash
cd noizylab-os
./scripts/bootstrap.sh
```

