# GABRIEL

**NOIZYLAB's AI-Powered Operations Platform**

Built for Rob Plowman's M2 Ultra Mac Studio | 192GB RAM | GORUNFREE Protocol

---

## Directory Structure

```
GABRIEL/
├── src/workers/                 # Core Cloudflare Workers
│   ├── noizylab/               # Full-featured API (3,955 LOC)
│   └── noizylab-v1/            # Simplified v1 refactor (1,984 LOC)
│
├── noizylab-os/workers/         # 67 Specialized AI Workers (50,636 LOC)
│   ├── brain/                  # Central intelligence
│   ├── vision/                 # Image/document analysis
│   ├── voice/                  # Voice processing
│   ├── chat-agent/             # Conversational AI
│   ├── api-gateway/            # API routing
│   ├── inventory/              # Parts management
│   ├── pricing/                # Dynamic pricing
│   ├── audio-engine/           # Audio processing
│   ├── video-codec/            # Video encoding
│   └── ... (57 more workers)
│
├── ANTIGRAVITY_COMPLETE/        # 10 Creative Workers (5,569 LOC)
│   ├── command-center/         # Central control
│   ├── sonic-engine/           # Audio synthesis
│   ├── media-vault/            # Media management
│   ├── neural-gateway/         # AI gateway
│   ├── dazeflow/               # Workflow automation
│   └── mc96-network/           # Network integration
│
├── portal/                      # Web Applications
│   ├── api/                    # Backend API
│   ├── frontend/               # React dashboard
│   ├── landing/                # Marketing site
│   └── sdk/                    # Client SDK
│
├── mcp_servers/                 # MCP Tools
│   └── gabriel_mcp/
│       └── turbo.py            # Parallel code scanner
│
├── scripts/                     # Shell Utilities (5,582 LOC)
│   ├── deploy.sh               # Deployment
│   ├── backup.sh               # Backup routines
│   ├── health_alerts.sh        # System monitoring
│   └── noizylab-sync.sh        # Repo synchronization
│
├── projects/                    # Active Projects
│   ├── SystemGuardian/         # System health monitoring
│   ├── universal-ingestion/    # Data ingestion pipeline
│   └── universal-blocker/      # Content filtering
│
├── tools/                       # Development Tools
│   ├── ai-dev-toolkit/         # AI development helpers
│   └── claude-voice-pack/      # Voice integration
│
├── docs/                        # Documentation
├── config/                      # Configuration files
├── archive/                     # Legacy code (75MB)
└── memory/                      # Agent memory storage
```

---

## Active Codebase Stats

| Component | Lines of Code | Files |
|-----------|---------------|-------|
| NoizyLab OS Workers | 50,636 | 67 workers |
| Core Workers | 5,939 | 2 workers |
| ANTIGRAVITY Creative | 5,569 | 10 workers |
| Shell Scripts | 5,582 | 30 scripts |
| MCP Servers | 848 | 3 tools |
| **Total Active** | **~70,000** | **~110** |

---

## Technology Stack

### Backend
- **Runtime**: Cloudflare Workers (Edge)
- **Framework**: Hono
- **Database**: D1 (SQLite)
- **Storage**: R2
- **AI**: Workers AI (Llama 3.1, Claude)
- **Validation**: Zod

### Frontend
- **Framework**: React 18
- **Styling**: Tailwind CSS
- **State**: Zustand
- **API**: Hono RPC

### AI/ML
- **Models**: Llama 3.1 8B Instruct, Claude 3.5 Sonnet
- **Vision**: Workers AI Vision
- **Voice**: Voice pipeline (TTS/STT)

---

## Key Features

### NoizyLab OS
- 12 persona-based ticket triage (Tab Tornado, Storage Closet, etc.)
- 12 playbook-driven remediation
- AI-powered calm messaging
- Real-time WebSocket updates

### ANTIGRAVITY
- Creative workflow automation
- Audio/video processing
- Media vault management
- Network-wide sync

### GABRIEL TURBO
- Parallel code validation
- Auto-fix with black/isort
- TypeScript/JavaScript/Python/Shell support
- ThreadPoolExecutor for speed

---

## Quick Commands

```bash
# Deploy all workers
./scripts/deploy.sh

# Sync to GitHub
./scripts/noizylab-sync.sh

# Run TURBO scanner
python mcp_servers/gabriel_mcp/turbo.py scan .

# Health check
./scripts/health_alerts.sh
```

---

## Network: MC96ECOUNIVERSE

| System | Role | Specs |
|--------|------|-------|
| GOD | Primary workstation | Mac Studio M2 Ultra, 192GB RAM |
| GABRIEL | Windows bridge | HP Omen |
| DaFixer | Repair station | MacBook Pro |

---

## Contact

- Primary: rsplowman@icloud.com
- Business: rob@noizylab.ca
- Legacy: rob@fishmusicinc.com

---

*Built with GORUNFREE philosophy. Ship it.*
