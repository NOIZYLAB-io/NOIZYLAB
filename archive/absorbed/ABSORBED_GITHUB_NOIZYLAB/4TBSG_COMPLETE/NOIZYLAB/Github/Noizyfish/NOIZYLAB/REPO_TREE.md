# NoizyLab OS Repository Structure

```
noizylab-os/
├── .env                          # Environment variables (not in git)
├── .env.template                  # Environment template
├── .gitignore                     # Git ignore rules
├── .bootstrapped                  # Bootstrap marker
├── package.json                   # Root package.json
├── README.md                      # Main documentation
│
├── supercode/                     # ⚡ SUPERCODE — Build & Deploy
│   ├── SUPERBUILD.sh              # Main build script
│   ├── cf-supercode.js            # Cloudflare deployment
│   ├── ai-router-install.sh      # AI CLI installation
│   ├── guardian.sh                # System health check
│   ├── test-harness.sh            # Test suite
│   ├── bootloader.sh              # First-time setup
│   ├── cursor-supercode.json      # Cursor AI rules
│   ├── cloudflare-routes.json     # Routing configuration
│   ├── build-pipeline.yml        # CI/CD pipeline
│   └── REPO_TREE.md               # This file
│
├── workers/                       # Cloudflare Workers
│   ├── ai-super-worker/          # AI processing worker
│   │   ├── src/
│   │   │   └── index.ts
│   │   ├── wrangler.toml
│   │   └── package.json
│   │
│   ├── super-worker/              # Main API worker
│   │   ├── src/
│   │   │   └── index.ts
│   │   ├── wrangler.toml
│   │   └── package.json
│   │
│   ├── intake/                    # Client intake system
│   ├── mc96/                      # MC96 dashboard worker
│   ├── teamviewer/                # Remote access worker
│   ├── agent-arbiter/             # Agent orchestration
│   ├── dreamchamber/              # DreamChamber worker
│   └── events/                    # Event processing
│
├── ai/                            # AI Infrastructure
│   ├── router/                    # Multi-AI router
│   │   ├── src/
│   │   │   └── index.ts
│   │   ├── bin/                   # CLI tools
│   │   │   ├── cfw-cli.js         # Cloudflare AI CLI
│   │   │   ├── gemini-cli.js      # Gemini CLI
│   │   │   └── claude-cli.js       # Claude CLI
│   │   ├── wrangler.toml
│   │   └── package.json
│   │
│   └── agents/                    # AI agents
│       └── (agent definitions)
│
├── d1/                            # D1 Database (legacy)
│   └── (database files)
│
├── db/                            # Database
│   ├── schema/                    # Schema definitions
│   │   └── init.sql
│   └── queries/                   # Query templates
│
├── migrations/                    # Database migrations
│   └── sql/
│       └── 001_initial_schema.sql
│
├── scripts/                       # Utility scripts
│   ├── deploy.sh                  # Deployment script
│   ├── validate-setup.sh          # Setup validation
│   ├── bootstrap.sh              # Bootstrap script
│   ├── ai-router-setup.sh        # AI router setup
│   └── (other scripts)
│
├── portal/                        # Web Portal
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── api/
│   ├── public/
│   └── index.html
│
├── ipad-app/                      # iPad Application
│   ├── Assets/
│   └── SwiftUI/
│
└── .noizy/                        # NoizyLab config
    └── cursor/
        └── rules.json             # Cursor AI rules (symlink)
```

## Key Directories

### `supercode/`
All build, deployment, and system management scripts.

### `workers/`
Individual Cloudflare Workers. Each worker is self-contained with:
- `src/index.ts` - Main worker code
- `wrangler.toml` - Worker configuration
- `package.json` - Dependencies

### `ai/`
AI infrastructure including:
- Multi-provider router (Cloudflare, Gemini, Claude, OpenAI)
- CLI tools for each provider
- Agent definitions

### `scripts/`
Utility scripts for common tasks.

## Quick Commands

```bash
# First time setup
./supercode/bootloader.sh

# Build everything
./supercode/SUPERBUILD.sh

# Check system health
./supercode/guardian.sh

# Run tests
./supercode/test-harness.sh

# Deploy to Cloudflare
node supercode/cf-supercode.js

# Install AI CLI tools
./supercode/ai-router-install.sh
```

## Environment Variables

Required in `.env`:
- `CF_ACCOUNT_ID` - Cloudflare account ID
- `CF_API_TOKEN` - Cloudflare API token
- `GEMINI_API_KEY` - Google Gemini API key (optional)
- `ANTHROPIC_API_KEY` - Anthropic Claude API key (optional)
- `OPENAI_API_KEY` - OpenAI API key (optional)

