# Mail Manager Pro v3.5.0 — COMPLETE DOCUMENTATION

## Overview

Mail Manager Pro is a comprehensive email organization system with advanced features for managing, backing up, and monitoring email across multiple mail clients (Apple Mail, Gmail, Outlook, Exchange).

**Version:** 3.5.0  
**Installation:** `~/scripts/mail_manager_pro`  
**License:** MIT

## Table of Contents

1. [Quick Start](#quick-start)
2. [Installation](#installation)
3. [Core Features](#core-features)
4. [Command Reference](#command-reference)
5. [Configuration](#configuration)
6. [Integrations](#integrations)
7. [Advanced Usage](#advanced-usage)
8. [Troubleshooting](#troubleshooting)

---

## Quick Start

### Installation

```bash
# Run the complete installer
bash ~/scripts/mail_manager_pro/install_complete.sh

# Add to PATH
export PATH="$HOME/scripts/mail_manager_pro/bin:$PATH"
```

### First Steps

```bash
# Launch interactive UI
mailmgr tui

# Create your first backup
mailmgr backup create

# Check system health
mailmgr health check

# Show help
mailmgr --help
```

---

## Installation

### System Requirements

- **Bash** 4.0+
- **macOS** 10.13+ or **Linux** (Ubuntu 18.04+)
- **4GB** disk space (for full installation + backups)
- **256MB** RAM minimum

### Optional Dependencies

| Dependency | Purpose | Install |
|-----------|---------|---------|
| Python 3.8+ | API server, ML | `brew install python3` |
| tput | Terminal UI | Pre-installed |
| curl | OAuth, webhooks | Pre-installed |
| tar | Backups | Pre-installed |

### Manual Installation

```bash
# Create installation directory
mkdir -p ~/scripts/mail_manager_pro

# Download and run installer
curl -fsSL https://raw.github.com/user/mail-manager-pro/install.sh | bash

# Or clone repository
git clone https://github.com/user/mail-manager-pro.git ~/scripts/mail_manager_pro
cd ~/scripts/mail_manager_pro
bash install_complete.sh
```

### Post-Installation

```bash
# Verify installation
bash tests/run_tests.sh

# Enable scheduler (optional)
mailmgr schedule enable

# Start API server (optional)
mailmgr api start

# Run health check
mailmgr health check
```

---

## Core Features

### 1. Backup & Restore

**Complete backup of mail configuration and data:**

```bash
# Create new backup
mailmgr backup create

# List all backups
mailmgr backup list

# Restore from latest
mailmgr backup restore

# Restore from specific backup
mailmgr backup restore backup_v2_20231215_143022

# Prune old backups (keep 10 most recent)
mailmgr backup prune 10
```

**Features:**
- ✓ Full configuration backup
- ✓ Folder structure preservation
- ✓ Rules and filters backup
- ✓ Version control (up to 30 backups)
- ✓ SHA256 checksums
- ✓ Automatic pre-restore backups

### 2. Folder Management

**Create and organize mail folders:**

```bash
# Create folders from configuration
mailmgr folders create

# Create for specific app
mailmgr folders create --app gmail

# List all folders
mailmgr folders list

# Show folder tree
mailmgr folders tree

# Sync across accounts
mailmgr folders sync
```

**Configuration example:**

```yaml
folders:
  - name: "Archive"
    parent: null
    accounts: ["Apple Mail"]
  - name: "Projects"
    parent: null
    subfolders:
      - name: "Current"
      - name: "Completed"
```

### 3. Mail Rules

**Automatic email sorting:**

```bash
# Create rules from configuration
mailmgr rules create

# List all rules
mailmgr rules list

# Apply rules now
mailmgr rules apply

# Test rule (dry-run)
mailmgr rules apply --dry-run
```

**Rule types:**
- From/To matching
- Subject patterns
- Date-based (older/newer)
- Size-based
- Custom conditions

### 4. Scheduler

**Automated scheduled tasks:**

```bash
# Enable scheduler (launchd on macOS, cron on Linux)
mailmgr schedule enable

# View scheduler status
mailmgr schedule status

# Run scheduled tasks now
mailmgr schedule run

# Disable scheduler
mailmgr schedule disable
```

**Default tasks:**
- Daily folder sync @ 6:00 AM
- Hourly rule processing
- Weekly backup Sunday @ 2:00 AM
- Health check every hour

### 5. REST API Server

**REST API for programmatic access:**

```bash
# Start API server
mailmgr api start

# Check API status
mailmgr api status

# Stop API server
mailmgr api stop
```

**API Endpoints:**

```bash
# Status
GET /status
GET /health

# Folders
GET /folders
POST /folders

# Backups
GET /backups
POST /backups
POST /backups/{name}/restore

# Rules
GET /rules
POST /rules

# Scheduler
GET /scheduler/status
POST /scheduler/run

# Accounts
GET /accounts
POST /accounts/test
```

### 6. Terminal UI (TUI)

**Interactive menu-driven interface:**

```bash
# Launch TUI
mailmgr tui
```

**Features:**
- Menu navigation (↑↓ arrows)
- Real-time status
- One-key operations
- Keyboard shortcuts

### 7. OAuth2 Authentication

**Connect to Gmail and Microsoft 365:**

```bash
# Gmail OAuth2 flow
mailmgr oauth gmail

# Microsoft OAuth2 flow
mailmgr oauth microsoft
```

**Setup:**
1. Create OAuth app in Google Cloud Console / Azure
2. Set `GMAIL_CLIENT_ID` / `MICROSOFT_CLIENT_ID` environment variables
3. Run oauth command to authorize

---

## Command Reference

### Backup Commands

```bash
mailmgr backup create               # Create new backup
mailmgr backup restore [name]       # Restore from backup
mailmgr backup list                 # List all backups
mailmgr backup prune [count]        # Delete old backups

Options:
  --dry-run                         # Preview without making changes
  --yes                             # Skip confirmations
```

### Folder Commands

```bash
mailmgr folders create              # Create folders from config
mailmgr folders list                # List all folders
mailmgr folders tree                # Show folder hierarchy
mailmgr folders sync                # Sync across accounts
mailmgr folders export              # Export to JSON
mailmgr folders import [file]       # Import from JSON

Options:
  --app gmail|outlook|applemail     # Target specific app
  --account [name]                  # Target specific account
```

### Rules Commands

```bash
mailmgr rules create                # Create rules from config
mailmgr rules list                  # List all rules
mailmgr rules apply                 # Apply rules to mail
mailmgr rules test [email]          # Test rule on email

Options:
  --dry-run                         # Preview changes
  --count [n]                       # Limit emails processed
```

### Scheduler Commands

```bash
mailmgr schedule enable             # Enable scheduler
mailmgr schedule disable            # Disable scheduler
mailmgr schedule status             # Show scheduler status
mailmgr schedule run                # Run scheduled tasks now
mailmgr schedule logs               # Show scheduler logs

macOS:  Uses launchd agents
Linux:  Uses systemd timers or cron
```

### API Commands

```bash
mailmgr api start                   # Start API server
mailmgr api stop                    # Stop API server
mailmgr api status                  # Show API status
mailmgr api logs                    # Show API logs

Options:
  --port [num]                      # Custom port (default: 8420)
  --host [addr]                     # Bind address (default: 127.0.0.1)
  --reload                          # Enable auto-reload
```

### OAuth Commands

```bash
mailmgr oauth gmail                 # Gmail authorization
mailmgr oauth microsoft             # Microsoft authorization

Environment:
  GMAIL_CLIENT_ID                   # OAuth app ID
  GMAIL_CLIENT_SECRET               # OAuth app secret
  MICROSOFT_CLIENT_ID               # Azure app ID
  MICROSOFT_CLIENT_SECRET           # Azure app secret
  MICROSOFT_TENANT                  # Tenant ID (default: common)
```

### General Commands

```bash
mailmgr health check                # System diagnostics
mailmgr health fix                  # Show recommended fixes
mailmgr tui                         # Interactive UI
mailmgr --help                      # Show help
mailmgr --version                   # Show version
```

---

## Configuration

### Main Configuration File

**Location:** `~/.mailmgr/config.yaml`

```yaml
mail_manager:
  version: 3.5.0
  auto_backup_enabled: true
  auto_backup_interval: 86400       # 24 hours in seconds
  max_backups: 30

accounts:
  - name: "Apple Mail"
    type: "applemail"
    enabled: true
    
  - name: "Gmail"
    type: "gmail"
    enabled: false
    oauth: false
    
  - name: "Outlook"
    type: "outlook365"
    enabled: false
    oauth: false

folders:
  - name: "Archive"
    parent: null
    accounts: ["Apple Mail"]
    
  - name: "Projects"
    parent: null
    accounts: ["Apple Mail"]
    subfolders:
      - name: "Current"
      - name: "Completed"

rules:
  - name: "Work Mail to Projects"
    match_field: "from"
    match_value: "@company.com"
    action: "move"
    destination: "Projects"
    
  - name: "Archive Old"
    match_field: "date"
    match_value: "older:90d"
    action: "move"
    destination: "Archive"

scheduler:
  enabled: false
  interval: 300
  tasks:
    - name: "sync_folders"
      schedule: "0 6 * * *"
    - name: "backup"
      schedule: "0 2 * * 0"

webhooks:
  slack:
    enabled: false
    url: ""
  discord:
    enabled: false
    url: ""
```

### Environment Variables

```bash
# Installation
MAIL_MANAGER_HOME=/path/to/installation

# API
API_HOST=127.0.0.1
API_PORT=8420

# OAuth2
GMAIL_CLIENT_ID=xxx
GMAIL_CLIENT_SECRET=xxx
MICROSOFT_CLIENT_ID=xxx
MICROSOFT_CLIENT_SECRET=xxx
MICROSOFT_TENANT=common

# Webhooks
SLACK_WEBHOOK=https://hooks.slack.com/...
DISCORD_WEBHOOK=https://discordapp.com/api/...
TEAMS_WEBHOOK=https://outlook.webhook.office.com/...

# Options
MAILMGR_YES=1                       # Skip confirmations
DRY_RUN=1                           # Preview mode
DEBUG=1                             # Verbose output
```

---

## Integrations

### Raycast

**Quick access to backup operations:**

```
raycast://open-extension/?path=mail_manager.pro

Commands:
  • Create Backup
  • List Backups
  • Restore Latest
```

### Alfred

**Alfred workflow for Mail Manager:**

```bash
# Generate workflow
bash integrations/alfred/generate-workflow.sh

# In Alfred:
  mmgr backup create
  mmgr backup list
  mmgr backup restore
```

### Keyboard Maestro

**Automation macros:**

```
Available macros:
  • Daily Backup
  • Weekly Cleanup
  • Health Check Alert
  • Restore on Demand
```

### Apple Shortcuts

**iOS/macOS automation:**

```
Available shortcuts:
  • Create Mail Backup
  • Health Status
  • Recent Backup Info
```

### Webhooks

**Send notifications to Slack, Discord, Teams:**

```bash
# In config.yaml:
webhooks:
  slack:
    enabled: true
    url: "https://hooks.slack.com/services/YOUR/WEBHOOK/URL"

# Events triggered:
  • Backup completed
  • Backup failed
  • Health check warning
  • Restore completed
```

---

## Advanced Usage

### Custom Backup Locations

```bash
BACKUP_DIR=/Volumes/external_drive/backups mailmgr backup create
```

### Backup to Cloud

```bash
# After creating backup, sync to cloud:
aws s3 sync ~/scripts/mail_manager_pro/backups s3://mybucket/mailmgr-backups
```

### Scheduled Health Checks

```bash
# Add to crontab:
0 * * * * MAIL_MANAGER_HOME=~/scripts/mail_manager_pro ~/scripts/mail_manager_pro/lib/health.sh check
```

### Custom Rules

```bash
# Edit rules in config.yaml
# Pattern syntax:
  from:value          # Match sender
  to:value            # Match recipient
  subject:value       # Match subject
  date:older:Nd       # Older than N days
  date:newer:Nd       # Newer than N days
  size:larger:Nk      # Larger than N KB
  size:smaller:Nk     # Smaller than N KB
```

### API Usage Examples

```bash
# Get status
curl http://localhost:8420/status

# Create backup
curl -X POST http://localhost:8420/backups

# Restore
curl -X POST http://localhost:8420/backups/backup_name/restore

# List folders
curl http://localhost:8420/folders

# Access docs
open http://localhost:8420/docs
```

### Python ML Integration

```python
from mail_manager_pro.python.ml_categorizer import EmailCategorizer

categorizer = EmailCategorizer()
category = categorizer.predict("Subject", "Email body...")
```

---

## Troubleshooting

### Common Issues

**Issue: "Command not found: mailmgr"**
```bash
# Add to PATH
export PATH="$HOME/scripts/mail_manager_pro/bin:$PATH"

# Or use full path
~/scripts/mail_manager_pro/bin/mailmgr --version
```

**Issue: "Backup creation failed"**
```bash
# Check permissions
ls -la ~/scripts/mail_manager_pro/backups

# Check disk space
df -h ~

# Run health check
mailmgr health check
```

**Issue: "API server won't start"**
```bash
# Check if port is in use
lsof -i :8420

# Use different port
API_PORT=8421 mailmgr api start

# Check dependencies
python3 -m pip install fastapi uvicorn pydantic
```

**Issue: "Scheduler not running"**
```bash
# Check launchd status (macOS)
launchctl list | grep mailmanager

# Check logs
cat ~/scripts/mail_manager_pro/logs/scheduler.log

# Re-enable
mailmgr schedule disable
mailmgr schedule enable
```

### Debug Mode

```bash
# Enable verbose output
DEBUG=1 mailmgr backup create

# Dry-run mode
DRY_RUN=1 mailmgr backup create

# Show all commands executed
set -x
```

### Getting Help

```bash
# Run health check
mailmgr health check

# Show recommendations
mailmgr health fix

# View logs
tail -100 ~/scripts/mail_manager_pro/logs/*.log

# Check configuration
cat ~/scripts/mail_manager_pro/config/config.yaml
```

---

## Support

- **Issues:** GitHub Issues
- **Documentation:** Full docs in `docs/` directory
- **Examples:** See `examples/` directory
- **Tests:** Run `bash tests/run_tests.sh`

---

## Version History

### v3.5.0 (Latest)
- ✓ Complete backup/restore with versioning
- ✓ Full Terminal UI (TUI)
- ✓ REST API with OpenAPI docs
- ✓ OAuth2 for Gmail & Microsoft
- ✓ Webhook integrations
- ✓ ML email categorization
- ✓ System integrations (Raycast, Alfred, Shortcuts)
- ✓ Health monitoring & diagnostics

### v3.0.0
- Folder management
- Basic mail rules
- Scheduler support

### v2.0.0
- Initial backup system

---

## License

MIT License — See LICENSE file for details

---

**Last Updated:** December 2024  
**Maintained by:** Mail Manager Team  
**GitHub:** https://github.com/user/mail-manager-pro
