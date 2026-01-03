# 🧭 CODEMASTER Quick Navigation Guide

**Fast access to common locations in the organized structure**

---

## 🚀 Common Commands

### View Structure
```bash
# See all categories
cd CODEMASTER && ls -la

# Tree view (if available)
tree -L 2 CODEMASTER/
```

### Find Something
```bash
# Search for a file
find CODEMASTER -name "filename.py"

# Search for content
grep -r "search term" CODEMASTER/
```

---

## 📍 Quick Access Paths

### Core Systems
```bash
cd CODEMASTER/01_CORE
# Contains: unified_integration_bridge.py, master_orchestrator.py, etc.
```

### Run Quick Examples
```bash
cd CODEMASTER/01_CORE
python3 QUICK_START_EXAMPLES.py
```

### Shell Scripts
```bash
cd CODEMASTER/03_SCRIPTS/shell
./autorun.sh
./supersonic.sh
./ultimate.sh
```

### System Scripts
```bash
cd CODEMASTER/03_SCRIPTS/system-scripts
./m2ultra-boot-startup.sh
```

### Gabriel Scripts
```bash
cd CODEMASTER/03_SCRIPTS/scripts
./LAUNCH_NOIZYLAB_COMPLETE.sh
```

### Projects
```bash
# AEON Projects
cd CODEMASTER/12_PROJECTS/aeon-god-kernel
cd CODEMASTER/12_PROJECTS/aeon-power

# Network Tunneling
cd CODEMASTER/12_PROJECTS/noizylab-tunnel

# RepairRob AI
cd CODEMASTER/12_PROJECTS/repairrob_staging

# 10CC Audio
cd CODEMASTER/12_PROJECTS/10cc-room

# System Guardian
cd CODEMASTER/12_PROJECTS/SystemGuardian
```

### Documentation
```bash
cd CODEMASTER/08_DOCS/root_docs

# Key docs
cat README.md
cat INTEGRATION_COMPLETION_REPORT.md
cat NOIZYLAB_INTEGRATION_MAP.md
cat CLAUDE.md
```

### Configuration
```bash
cd CODEMASTER/06_CONFIG

# VS Code settings
cat .vscode/settings.json

# Build config
cat Makefile

# Cloudflare Workers
cat wrangler.toml

# Python deps
cat requirements.txt
```

### Infrastructure
```bash
# Cloudflare Workers
cd CODEMASTER/10_INFRA/cloudflare-workers

# Gabriel Workers
cd CODEMASTER/10_INFRA/workers

# VPN Configs
cd CODEMASTER/10_INFRA/VPN
cat wg0.conf
```

### Web Apps
```bash
# Mission Control Portal
cd CODEMASTER/09_APPS/mission_control_portal
open index.html

# Gabriel Widget
cd CODEMASTER/09_APPS/widget
```

### Brain & Memory
```bash
# Memory data
cd CODEMASTER/11_BRAIN/memory
cat daily/2025-12-10.md

# Memcell data
cd CODEMASTER/11_BRAIN/memcell_data
cat brain.json
```

### AI Agents
```bash
cd CODEMASTER/02_AGENTS/automation

# AI Agents
cd ai-agents/

# MC96 Universe
cd mc96-universe/

# Voice AI
cd voice-first/
```

### Development Tools
```bash
# Gabriel tools
cd CODEMASTER/05_TOOLS/tools

# Go tools
cd CODEMASTER/05_TOOLS/golang
```

---

## 🔍 Finding Specific Files

### Core Integration Files
```
CODEMASTER/01_CORE/unified_integration_bridge.py
CODEMASTER/01_CORE/master_orchestrator.py
CODEMASTER/01_CORE/secure_transport_layer.py
CODEMASTER/01_CORE/unified_auth_system.py
```

### Important Scripts
```
CODEMASTER/03_SCRIPTS/shell/autorun.sh
CODEMASTER/03_SCRIPTS/shell/supersonic.sh
CODEMASTER/03_SCRIPTS/shell/ultimate.sh
CODEMASTER/03_SCRIPTS/scripts/LAUNCH_NOIZYLAB_COMPLETE.sh
CODEMASTER/03_SCRIPTS/system-scripts/m2ultra-boot-startup.sh
```

### Key Documentation
```
CODEMASTER/README.md
CODEMASTER/GITHUB_STRUCTURE.md
CODEMASTER/ORGANIZATION_SUMMARY.md
CODEMASTER/08_DOCS/root_docs/README.md
CODEMASTER/08_DOCS/root_docs/INTEGRATION_COMPLETION_REPORT.md
```

### Configuration Files
```
CODEMASTER/06_CONFIG/Makefile
CODEMASTER/06_CONFIG/wrangler.toml
CODEMASTER/06_CONFIG/requirements.txt
CODEMASTER/06_CONFIG/.github/workflows/
```

### Project READMEs
```
CODEMASTER/12_PROJECTS/noizylab-tunnel/README.md
CODEMASTER/12_PROJECTS/aeon-power/REALITY-CHECK.md
CODEMASTER/12_PROJECTS/SystemGuardian/README.md
```

---

## 📊 Category Overview

| Directory | Content Type | Primary Language |
|-----------|-------------|------------------|
| 01_CORE | Integration Systems | Python |
| 02_AGENTS | AI Automation | Python, JavaScript |
| 03_SCRIPTS | Automation Scripts | Shell, Python |
| 04_MCP | MCP Servers | JavaScript, Python |
| 05_TOOLS | Dev Tools | Go, Python |
| 06_CONFIG | Configuration | YAML, JSON, TOML |
| 07_LEGACY | Archives | Mixed |
| 08_DOCS | Documentation | Markdown |
| 09_APPS | Web Apps | HTML, CSS, JavaScript |
| 10_INFRA | Infrastructure | JavaScript, Python |
| 11_BRAIN | AI Memory | JSON, Python |
| 12_PROJECTS | Projects | Mixed |

---

## 🎯 By Task

### Need to Deploy?
```bash
cd CODEMASTER
cat GITHUB_STRUCTURE.md
./ORGANIZE_FOR_GITHUB.sh
```

### Need to Build?
```bash
cd CODEMASTER/06_CONFIG
make
```

### Need to Run Workers?
```bash
cd CODEMASTER/10_INFRA/cloudflare-workers
npx wrangler dev
```

### Need to Access VPN?
```bash
cd CODEMASTER/10_INFRA/VPN
sudo wg-quick up wg0
```

### Need Documentation?
```bash
cd CODEMASTER/08_DOCS/root_docs
ls *.md
```

### Need to Run Project?
```bash
cd CODEMASTER/12_PROJECTS/<project-name>
# Follow project-specific README
```

---

## 💡 Tips

1. **Use tab completion**: Type partial names and hit TAB
2. **Bookmark common paths**: Add aliases to your shell config
3. **Use find**: `find CODEMASTER -name "*.py"` to find Python files
4. **Use grep**: `grep -r "function_name" CODEMASTER/` to search code
5. **Check READMEs**: Each major section has documentation

---

## 🔗 Related Files

- `CODEMASTER/README.md` - Full structure documentation
- `CODEMASTER/ORGANIZATION_SUMMARY.md` - What was organized
- `CODEMASTER/GITHUB_STRUCTURE.md` - GitHub deployment guide

---

**Quick Reference**: Keep this guide handy for fast navigation! 🚀
