# GABRIEL - GitHub Copilot Instructions

## 🎯 Project Overview

**GABRIEL** is the Windows bridge system for NOIZYLAB's MC96ECOUNIVERSE automation framework. It connects the HP Omen (GABRIEL) to the Mac Studio M2 Ultra (GOD) as part of Rob Plowman's complete business and automation ecosystem.

## 🏗️ Architecture

```
GABRIEL/
├── src/                    # Source code
│   ├── core/              # Gabriel core system
│   ├── agents/            # AI agent definitions
│   │   ├── fleet/         # Named agents (POPS, SHIRL, etc.)
│   │   ├── configs/       # Agent configuration JSON
│   │   └── brain/         # AI brain modules
│   ├── mcp/               # MCP server implementations
│   └── workers/           # Cloudflare workers
├── scripts/               # Shell/automation scripts
├── config/                # Configuration files
├── tools/                 # Standalone tools
├── infrastructure/        # Infrastructure as code
├── docs/                  # Documentation
└── archive/               # Historical/deprecated code
```

## 🤖 AI Agents - Circle of 8

The **Circle of 8** is the AI agent collective powering MC96ECOUNIVERSE:

| Agent | Role | Personality | Emoji |
|-------|------|-------------|-------|
| **GABRIEL** | System Bridge & Warrior | Fierce protector, direct, loyal | ⚔️ |
| **SHIRL** | Business Operations | Organized, efficient, warm | 📋 |
| **POPS** | Creative Director | Wise, encouraging, father figure | 🎨 |
| **ENGR_KEITH** | Technical Engineering | Precise, methodical, R.K.'s precision | 🔧 |
| **DREAM** | Strategic Visionary | Future-focused, sees possibilities | 🔮 |
| **HEAVEN** | Orchestrator & Conductor | Harmonious, coordinating, unity | 🎭 |
| **LUCY** | Code Guardian & Watcher | Vigilant, analytical, security-minded | 👁️ |
| **SONIC** | Audio & Creative Engine | Fast, creative, music-driven | 🎵 |

### Agent Configuration
- Full configs: `src/agents/configs/circle_of_8.json`
- DAZEFLOW protocol: `src/agents/configs/dazeflow.json`
- Shell interface: `src/agents/fleet/agent_interface.sh`

### DAZEFLOW Protocol
**1day = 1chat = 1truth**
- Every day starts fresh but carries forward wisdom
- One conversation thread per day maintains context
- Truth is singular - no fabrication, no hallucination

## 📜 Coding Conventions

### Python
- Use Python 3.11+
- Type hints required for all functions
- Docstrings in Google style
- Max line length: 100 characters
- Use `pathlib` for file paths
- Async/await for I/O operations

### JavaScript/TypeScript
- ES2022+ features
- Strict TypeScript mode
- Prefer `const` over `let`
- Use arrow functions for callbacks
- Document with JSDoc

### Shell Scripts
- Use `#!/bin/bash` or `#!/bin/zsh`
- Always quote variables: `"$var"`
- Use `set -euo pipefail` for safety
- Functions in `snake_case`

## 🚫 Anti-Patterns to Avoid

1. **No duplicate files** - Never create `-2`, `-3`, `-4` suffix versions
2. **No UUID filenames** - Use meaningful, descriptive names
3. **No scattered configs** - All configs in `config/` or relevant `configs/` subdirs
4. **No hardcoded paths** - Use environment variables or relative paths
5. **No monolithic files** - Split into logical modules (<500 lines)

## 🔧 Key Technologies

- **Runtime**: Python 3.11+, Node.js 20+
- **AI/ML**: OpenAI, Anthropic Claude, Local LLMs
- **Infrastructure**: Cloudflare Workers, D1, KV
- **Databases**: D1 (SQLite), Redis
- **Message Queue**: Cloudflare Queues
- **Version Control**: Git + GitKraken

## 🌐 Network Context

| System | Hostname | Role |
|--------|----------|------|
| GOD | mac-studio | Primary workstation (M2 Ultra) |
| GABRIEL | hp-omen | Windows bridge |
| DaFixer | macbook-pro | Repair station |

## 📦 Package Management

- Python: `uv` or `pip` with `requirements.txt`
- Node.js: `npm` with `package.json`
- Always pin versions in production

## 🧪 Testing

- Python: `pytest` with `pytest-asyncio`
- JavaScript: `vitest` or `jest`
- Minimum 80% coverage for core modules
- Integration tests for agent interactions

## 🔒 Security Guidelines

1. Never commit secrets or API keys
2. Use `.env` files (gitignored) for local secrets
3. Use Cloudflare secrets for production
4. Validate all external input
5. Sanitize file paths to prevent traversal

## 📝 Commit Message Format

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Examples:
- `feat(agents): add voice command support to POPS`
- `fix(mcp): resolve connection timeout in gabriel_mcp`
- `docs: update agent architecture diagram`

## 🎪 GORUNFREE Philosophy

Every solution should follow the **GORUNFREE** principle:
- **One command = everything done**
- No fragmented steps
- Voice-first accessibility
- Zero fabricated data (Truth Covenant)

## 💡 When Generating Code

1. **Check existing patterns** - Look at similar files first
2. **Follow the structure** - Place files in correct directories
3. **Add appropriate logging** - Use structured logging
4. **Include error handling** - Never let errors silently fail
5. **Document intent** - Comments explain "why", not "what"
6. **Consider the agents** - Code may be invoked by AI agents

## 🔗 Related Repositories

- `NOIZYLAB-io/NOIZYLAB` - Main ecosystem repo
- `NOIZYLAB-io/mc96-universe` - MC96ECOUNIVERSE framework

---

*Last updated: January 2026*
*Branch: `3-set-up-copilot-instructions`*
