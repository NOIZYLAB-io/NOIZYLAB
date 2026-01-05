# NOIZYLAB AI Copilot - Slack Bot

🤖 **AI-powered disk repair & monitoring bot for MC96 Digi Universe**

Integrates with TechTool Pro 21, DiskWarrior, and all NOIZYLAB automation scripts.

---

## ⚡ Quick Start

### 1. Install Dependencies

```bash
cd ~/NOIZYLAB/slack-bot
npm install
```

### 2. Configure Environment

```bash
# Copy example config
cp .env.example .env

# Edit with your Slack tokens
nano .env
```

**Get your tokens from:** https://api.slack.com/apps

### 3. Run Bot

**Development mode (auto-restart):**

```bash
npm run dev
```

**Production mode:**

```bash
npm start
```

---

## 🔑 Slack App Setup

### Create App

1. Go to https://api.slack.com/apps
2. Click **Create New App** → **From scratch**
3. Name: `Nbash ~/NOIZYLAB/scripts/import_gemini_backups.sh ~/Downloads/folder-nameOIZYLAB AI Copilot`
4. Workspace: `MC96 Digi Universe`

### Enable Socket Mode (No public endpoint needed!)

1. Go to **Socket Mode** in app settings
2. Toggle **Enable Socket Mode** ON
3. Generate **App-Level Token** (name: `noizylab-socket`)
4. Copy token → Add to `.env` as `SLACK_APP_TOKEN`

### Configure Bot Permissions

Go to **OAuth & Permissions** → Add these Bot Token Scopes:

- `app_mentions:read` - Detect @noizylab mentions
- `chat:write` - Post messages
- `commands` - Slash commands
- `files:read` - Read status files
- `files:write` - Save reports
- `channels:read` - List channels
- `channels:history` - Read channel messages

### Add Slash Commands

Go to **Slash Commands** → Create these commands:

| Command                  | Description                                |
| ------------------------ | ------------------------------------------ |
| `/disk-status`           | Quick health check of all drives           |
| `/noizylab-repair`       | TechTool Pro 21 hot rod repair             |
| `/cleanup-all`           | Aggressive cleanup (empty folders, caches) |
| `/diskwarrior-emergency` | DiskWarrior backup repair algorithm        |

**Note:** With Socket Mode, you don't need Request URLs!

### Enable Events

Go to **Event Subscriptions** → Subscribe to these bot events:

- `app_mention` - Respond to @noizylab mentions
- `message.channels` - Listen to channel messages (optional)

### Install to Workspace

1. Go to **Install App**
2. Click **Install to Workspace**
3. Authorize permissions
4. Copy **Bot User OAuth Token** → Add to `.env` as `SLACK_BOT_TOKEN`

---

## 🎯 Commands

### Slash Commands

**Health Check:**

```
/disk-status
```

Returns: Quick health report of all volumes (2-sec timeout)

**Repair Drive:**

```
/noizylab-repair 12TB
/noizylab-repair all
```

Runs TechTool Pro 21 hot rod repair (6-10x faster than default)

**Cleanup:**

```
/cleanup-all
```

Runs ULTRA_AGGRESSIVE.sh (requires admin access)

**Emergency Repair:**

```
/diskwarrior-emergency
```

DiskWarrior guide when TTP21 fails (dual-tool strategy)

### Natural Language Interface

Just mention `@noizylab` and describe your issue:

```
@noizylab my 12TB drive is frozen
→ Suggests diagnostic steps + repair commands

@noizylab check disk status
→ Runs QUICK_STATUS.sh

@noizylab how much space left?
→ Shows storage capacity report

@noizylab help
→ Lists all available commands
```

---

## 🔐 Security

### User Authorization

**Admin users** (can run destructive commands):

```bash
# Add to .env
ADMIN_USERS=U01234567,U01234568
```

**Allowed users** (can run read-only commands):

```bash
ALLOWED_USERS=U01234567,U01234568,U01234569
```

**Get Slack user IDs:**

1. Click user's profile in Slack
2. Click **More** → **Copy member ID**

### Token Security

- ✅ Tokens stored in `.env` (not committed to Git)
- ✅ `.env` added to `.gitignore`
- ✅ Socket Mode = no public endpoint needed
- ✅ Commands require authorization check
- ✅ Admin-only commands for destructive operations

---

## 📊 Monitoring

### Daily Health Reports

Bot automatically posts daily reports at 9am:

```bash
# Enable in .env
ENABLE_DAILY_REPORTS=true
DAILY_REPORT_CHANNEL=#disk-health
```

### SMART Failure Alerts

Bot monitors for SMART failures and alerts immediately:

```bash
ALERT_CHANNEL=#tech-support
```

---

## 🛠️ Development

### Run with Auto-Restart

```bash
npm run dev
```

Uses `nodemon` to restart on file changes.

### Test Commands Locally

```bash
# Set env vars
export SLACK_BOT_TOKEN="xoxb-..."
export SLACK_SIGNING_SECRET="..."
export SLACK_APP_TOKEN="xapp-..."

# Run bot
node app.js
```

### Debug Mode

```bash
NODE_ENV=development npm start
```

---

## 🚀 Deployment

### Local Development

```bash
npm run dev
```

### Production Server

**Option 1: PM2 (Process Manager)**

```bash
npm install -g pm2
pm2 start app.js --name noizylab-bot
pm2 save
pm2 startup
```

**Option 2: systemd Service**

```bash
# Create service file
sudo nano /etc/systemd/system/noizylab-bot.service

# Add:
[Unit]
Description=NOIZYLAB AI Copilot Slack Bot
After=network.target

[Service]
Type=simple
User=m2ultra
WorkingDirectory=/Users/m2ultra/NOIZYLAB/slack-bot
ExecStart=/usr/local/bin/node app.js
Restart=on-failure

[Install]
WantedBy=multi-user.target

# Enable and start
sudo systemctl enable noizylab-bot
sudo systemctl start noizylab-bot
```

**Option 3: Docker**

```bash
# Coming soon...
```

---

## 🎖️ Features

### Phase 1: Basic Commands ✅

- [x] `/disk-status` - Quick health check
- [x] `/noizylab-repair` - TTP21 hot rod repair
- [x] `/cleanup-all` - Aggressive cleanup
- [x] `/diskwarrior-emergency` - Backup repair

### Phase 2: Natural Language 🔄

- [x] `@noizylab` mentions
- [x] Basic keyword matching
- [ ] GPT-4 integration for advanced understanding
- [ ] Context-aware responses

### Phase 3: Proactive Monitoring 🎯

- [x] Daily health reports (9am)
- [ ] Real-time SMART alerts
- [ ] Capacity warnings (>90% full)
- [ ] Performance degradation detection

### Phase 4: Advanced Automation 🚀

- [ ] Scheduled cleanups (nightly)
- [ ] Auto-backup on SMART warnings
- [ ] Predictive failure analysis
- [ ] Multi-user support

---

## 🏆 Phineas Potts Standard

This bot meets the **Phineas Potts Standard** for MAGICAL performance:

✅ **Fast** - Responds in <2 seconds  
✅ **Smart** - Natural language interface  
✅ **Reliable** - Auto-retry on failures  
✅ **Secure** - User authorization required  
✅ **Proactive** - Monitors 24/7 for issues  
✅ **Helpful** - Clear, actionable responses

🚗✨ **"Good enough" is NOT acceptable. Only MAGICAL will do!**

---

## 📚 Resources

- Slack Bolt Framework: https://slack.dev/bolt-js/
- Socket Mode: https://api.slack.com/apis/connections/socket
- Slack API: https://api.slack.com/
- NOIZYLAB Scripts: `~/NOIZYLAB/`

---

## 🆘 Troubleshooting

**Bot not responding:**

1. Check bot is running: `ps aux | grep node`
2. Check logs: `tail -f ~/NOIZYLAB/slack-bot/logs/bot.log`
3. Verify tokens in `.env`
4. Check Socket Mode is enabled

**Permission denied:**

1. Check user ID in `ALLOWED_USERS` or `ADMIN_USERS`
2. Get user ID: Click profile → More → Copy member ID

**Script execution fails:**

1. Verify script paths in `.env`
2. Check scripts are executable: `chmod +x ~/NOIZYLAB/*.sh`
3. Test script manually: `bash ~/NOIZYLAB/QUICK_STATUS.sh`

---

**Version:** 1.0.0  
**Author:** Gabriel Almeida  
**License:** MIT  
**Repository:** https://github.com/NOIZYLAB-io/NOIZYLAB
