# 🚀 CODEMASTER

> **Evidence-First Remote Control + Asset Vault System**
> 
> Every action produces an Evidence Pack. No hallucinations. No guessing.

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         CODEMASTER                               │
├─────────────────────────────────────────────────────────────────┤
│  🖥️ PORTAL (8080)                                               │
│     TeamViewer-style remote control UI                          │
├─────────────────────────────────────────────────────────────────┤
│  📦 VAULT (8000)       │  📚 CATALOG (8001)   │  📋 EVIDENCE     │
│  Ingest + Storage      │  Asset Index         │  (8002)          │
│  Dedupe + Sidecars     │  Search + Tags       │  Truth System    │
├─────────────────────────────────────────────────────────────────┤
│  🧠 AI GATEWAY (8100)  │  🚀 FLEET (8200)     │  🌐 MC96 (8300)  │
│  Proxy to GOD AI       │  Device Registry     │  Network Control │
│  Rate Limits + Cache   │  Sessions + Audit    │  Runbooks        │
└─────────────────────────────────────────────────────────────────┘
           │                      │                      │
           ▼                      ▼                      ▼
    ┌──────────────────────────────────────────────────────────┐
    │  🧠 GOD (M2 Ultra)                                       │
    │  Ollama + Llama 3.2 + Embeddings + STT + TTS            │
    └──────────────────────────────────────────────────────────┘
```

## 🎯 Core Principles

1. **Evidence-First**: Every claim backed by evidence or marked UNSUPPORTED
2. **Vault-Centric**: All data flows through the vault with full provenance
3. **Audit Everything**: Complete audit trail for every action
4. **Air-Gap Ready**: Works fully offline with local AI

## 📦 Services

| Service | Port | Description |
|---------|------|-------------|
| Portal | 8080 | Web UI - TeamViewer-style remote control |
| Vault | 8000 | Ingest, storage, dedup, sidecars |
| Catalog | 8001 | Asset index, search, tags |
| Evidence | 8002 | Evidence packs, verification |
| AI Gateway | 8100 | Rate-limited proxy to GOD AI |
| Fleet | 8200 | Device registry, sessions |
| MC96 | 8300 | Network control, runbooks |

## 🚀 Quick Start

```bash
# Clone and install
cd /Users/m2ultra/NOIZYLAB/CODEMASTER
pip install -r requirements.txt

# Check status
python codemaster.py status

# Start services (Docker)
python codemaster.py start

# Or run individual services (dev mode)
python services/vault/vault_service.py serve
python services/catalog/catalog_service.py serve
# etc...
```

## 📋 CLI Commands

```bash
# Status & Health
codemaster status          # All service statuses
codemaster health          # Health check

# Service Control
codemaster start           # Start all (Docker)
codemaster start --dev     # Dev mode
codemaster stop            # Stop all
codemaster logs [service]  # View logs

# Vault Operations
codemaster vault status
codemaster vault ingest --path /path/to/files
codemaster vault find -q "search term"

# Catalog Operations
codemaster catalog status
codemaster catalog search -q "query"
codemaster catalog stats

# Evidence Operations
codemaster evidence status
codemaster evidence list
codemaster evidence verify --pack-id <id>

# Fleet Operations
codemaster fleet status
codemaster fleet list
codemaster fleet sessions

# MC96 Network Operations
codemaster mc96 status
codemaster mc96 devices
codemaster mc96 runbooks
codemaster mc96 backup

# AI Operations
codemaster ai status
codemaster ai stats
codemaster ai test --prompt "Hello"
```

## 📁 Storage Layout

```
/Users/m2ultra/NOIZY_AI/
├── vault/
│   ├── raw/              # Append-only raw files
│   ├── derived/          # Generated sidecars
│   ├── index/            # Search indices
│   └── staging/          # Quarantine, dedupe
├── catalog/              # SQLite catalog
├── evidence_packs/       # Immutable evidence
├── fleet/                # Device registry
├── mc96/
│   ├── configs/          # Network config backups
│   └── runbooks/         # Automation scripts
├── cache/ai/             # AI response cache
└── logs/
    ├── audit/
    ├── ingest/
    ├── mc96/
    └── portal/
```

## 📋 Evidence Pack Structure

Every action produces an Evidence Pack:

```json
{
  "pack_id": "pack-abc123",
  "question": "What files contain password info?",
  "claims": [
    {
      "claim_text": "config.py contains a database password",
      "sources": ["vault:abc123"],
      "status": "supported"
    }
  ],
  "actions": [
    {
      "action": "search",
      "params": {"query": "password"},
      "result": "found 3 matches"
    }
  ],
  "answer": "Found password references in 3 files...",
  "verification": {
    "status": "verified",
    "confidence": 0.95
  }
}
```

## 🔧 Configuration

Copy `.env.example` to `.env` and customize:

```bash
cp infra/compose/.env.example infra/compose/.env
```

Key settings:
- `NOIZY_ROOT` - Storage root directory
- `GOD_HOST` - Ollama endpoint
- `GOD_MODEL` - Default model

## 🌐 Network Runbooks

Pre-built runbooks in MC96:

1. **backup_configs_nightly** - Backup all device configs
2. **get_interface_status** - Check interface states
3. **quarantine_device** - Emergency interface shutdown

## 📊 Roadmap

### v0.1 (Current)
- [x] Vault service
- [x] Catalog service
- [x] Evidence service
- [x] AI Gateway
- [x] Fleet service
- [x] MC96 service
- [x] CLI
- [x] Docker Compose

### v0.2
- [ ] Portal UI
- [ ] WebRTC remote control
- [ ] Redis + Celery queues
- [ ] Prometheus metrics
- [ ] Grafana dashboards

### v0.3
- [ ] MeshCentral integration
- [ ] Netmiko network automation
- [ ] Multi-user RBAC
- [ ] Postgres migration

## 🔐 Security Notes

1. Change all secrets in production
2. Use proper certificates for services
3. Network runbooks require credential vault
4. All actions audited with user identity

---

**CODEMASTER** - Evidence-First Remote Control

*Built for NOIZYLAB by GOD (M2 Ultra) + GABRIEL*
