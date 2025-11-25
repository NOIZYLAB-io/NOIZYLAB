# NOIZYLAB

```
    ╔═╗╔═╗╔═╗╔═╗╔═╗  ╦  ╔═╗╔╗   v2.0
    ║║║║ ║║╔╝╚═╗╠═╝  ║  ╠═╣╠╩╗  AI Command Center
    ╝╚╝╚═╝╚╝ ╚═╝╩    ╩═╝╩ ╩╚═╝  ━━━━━━━━━━━━━━━━━
```

**AI-Powered Email Command Center** with Multi-Agent Routing, Spam Detection, and Real-time Analytics.

## Features

- 🤖 **6 AI Agents** - Specialized personalities for different tasks
- 📧 **Smart Email Processing** - AI-powered analysis and routing
- 🚫 **Spam Detection** - Pattern-based filtering with trusted domains
- 📊 **Dashboard API** - Real-time stats and monitoring
- 🔔 **Webhook Notifications** - Discord/Slack integration
- ⚡ **Rate Limiting** - Protection against email floods
- 💬 **Interactive Shell** - Chat directly with agents

## AI Agents

| Agent | Role | Specialty |
|-------|------|-----------|
| 🎨 **LUCY** | Creative Director | Branding, design, visual concepts |
| ⚙️ **KEITH** | Technical Lead | Code, architecture, debugging |
| 📋 **WARDY** | Project Manager | Planning, scheduling, coordination |
| 🚨 **RED_ALERT** | Security Handler | Emergencies, security, urgent issues |
| 🔬 **NOVA** | Research Analyst | Data analysis, research, insights |
| 📢 **ECHO** | Communications Lead | Client relations, PR, messaging |

## Quick Start

```bash
# Install dependencies
npm install

# Initialize project
./noizy.js init

# Configure KV namespaces in wrangler.toml
# Then deploy
./noizy.js deploy all
```

## CLI Commands

```bash
noizy help              # Show all commands
noizy init              # Initialize project
noizy status            # System status check
noizy deploy [target]   # Deploy workers (email|api|all)
noizy agent <NAME> <TASK>  # Summon an AI agent
noizy agents            # List all agents
noizy logs [--tail]     # View email logs
noizy shell             # Interactive agent chat
noizy config [get|set]  # Manage configuration
noizy kv [list|get|del] # Manage KV store
noizy webhook <msg>     # Test webhooks
```

## API Endpoints

```
GET  /health              # Health check
GET  /stats               # Email statistics
GET  /emails              # List emails
GET  /emails/:id          # Get email details
GET  /agents              # List all agents
GET  /agents/:name        # Agent details
POST /agents/:name/task   # Call agent with task
GET  /spam                # Spam logs
GET  /search?q=<term>     # Search emails
GET  /dashboard           # Full dashboard data
POST /chat                # Chat with agent
```

## Configuration

Edit `wrangler.toml` to configure:

```toml
[vars]
FORWARD_EMAIL = "your@email.com"
WEBHOOK_ENABLED = "true"
SPAM_THRESHOLD = "7"
MAX_EMAILS_PER_HOUR = "100"
```

Set secrets:
```bash
npx wrangler secret put WEBHOOK_URL
npx wrangler secret put ADMIN_API_KEY
```

## Project Structure

```
NOIZYLAB/
├── noizy.js              # CLI entry point
├── package.json          # Dependencies
├── wrangler.toml         # Cloudflare config
├── workers/
│   ├── email-worker.js   # Email processing
│   └── api-dashboard.js  # REST API
├── agents/
│   └── agent-definitions.js
├── templates/
│   └── email-templates.js
├── lib/
│   └── utils.js
├── config/
│   └── noizylab.json
└── tests/
    └── test-agents.js
```

## How It Works

1. **Email arrives** → Cloudflare Email Worker receives it
2. **Spam check** → Pattern matching + trusted domain verification
3. **AI Analysis** → Mistral AI analyzes intent, urgency, sentiment
4. **Agent routing** → Best agent selected based on content
5. **Logging** → Full analysis stored in KV
6. **Webhook** → Notification sent to Discord/Slack
7. **Forward** → Email forwarded to your inbox
8. **Auto-reply** → Urgent emails get immediate response

## Requirements

- Node.js 18+
- Cloudflare account with:
  - Workers
  - Email Routing
  - KV Namespaces
  - Workers AI

## License

MIT

---

Built with ⚡ by NoizyLab
