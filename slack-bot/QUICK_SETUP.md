# 🚀 NOIZYLAB Slack Bot - 5 Minute Setup

**Use the App Manifest for instant deployment!**

---

## ⚡ Option 1: Quick Deploy with Manifest (RECOMMENDED)

**Time: 5 minutes**

### Step 1: Create App from Manifest

1. **Go to**: https://api.slack.com/apps?new_app=1
2. **Click**: "From an app manifest"
3. **Select**: Your workspace (MC96 Digi Universe)
4. **Paste**: The entire contents of `noizylab-manifest.yaml`
5. **Click**: "Next" → "Create"

✅ **Done!** Your app is configured with:

- Socket Mode enabled
- All 4 slash commands
- Event subscriptions
- OAuth scopes
- Bot user settings

### Step 2: Get Your 3 Tokens

#### A. Get Bot Token (SLACK_BOT_TOKEN)

1. In your app settings, go to **"OAuth & Permissions"**
2. Click **"Install to Workspace"**
3. Click **"Allow"**
4. Copy the **"Bot User OAuth Token"** (starts with `xoxb-`)
   ```
   SLACK_BOT_TOKEN=xoxb-your-token-here
   ```

#### B. Get Signing Secret (SLACK_SIGNING_SECRET)

1. Go to **"Basic Information"** in the sidebar
2. Scroll to **"App Credentials"**
3. Copy the **"Signing Secret"** (NOT the Client Secret)
   ```
   SLACK_SIGNING_SECRET=your-secret-here
   ```

#### C. Get App Token (SLACK_APP_TOKEN)

1. Go to **"Basic Information"** in the sidebar
2. Scroll to **"App-Level Tokens"**
3. Click **"Generate Token and Scopes"**
4. Name it: `noizylab-socket-token`
5. Add scopes: `connections:write`, `authorizations:read`
6. Click **"Generate"**
7. Copy the token (starts with `xapp-`)
   ```
   SLACK_APP_TOKEN=xapp-your-token-here
   ```

### Step 3: Configure .env File

```bash
cd ~/NOIZYLAB/slack-bot
nano .env
```

Paste your 3 tokens:

```bash
# Slack Tokens (from App Settings)
SLACK_BOT_TOKEN=xoxb-paste-your-token-here
SLACK_SIGNING_SECRET=paste-your-secret-here
SLACK_APP_TOKEN=xapp-paste-your-token-here

# User Authorization (get from Slack)
# Right-click user → "Copy member ID"
ADMIN_USERS=U01234567,U01234568
ALLOWED_USERS=U01234567,U01234568,U01234569

# Script Paths (verify these exist)
TTP21_SCRIPT=/Users/m2ultra/NOIZYLAB/scripts/TTP21_HOT_ROD_GUIDE.sh
QUICK_STATUS_SCRIPT=/Users/m2ultra/NOIZYLAB/scripts/QUICK_STATUS.sh
CLEANUP_SCRIPT=/Users/m2ultra/NOIZYLAB/scripts/ULTRA_AGGRESSIVE.sh
DISKWARRIOR_SCRIPT=/Users/m2ultra/NOIZYLAB/scripts/DISKWARRIOR_EMERGENCY_GUIDE.sh

# Bot Settings
DEFAULT_VOLUME=/Volumes/12TB
DAILY_REPORT_CHANNEL=C01234567
DAILY_REPORT_TIME=09:00
LOG_LEVEL=info
```

**How to get User IDs:**

1. In Slack, right-click any user
2. Click "View profile"
3. Click the ⋯ (three dots)
4. Click "Copy member ID"

**How to get Channel IDs:**

1. Right-click any channel
2. Click "View channel details"
3. Scroll down, copy the Channel ID

### Step 4: Run the Bot

```bash
cd ~/NOIZYLAB/slack-bot
npm run dev
```

**Expected output:**

```
⚡️ NOIZYLAB AI Copilot is running!
✅ Connected to Slack
🤖 Bot User ID: U01234567
📡 Socket Mode: Enabled
🎯 Ready to receive events
```

### Step 5: Test in Slack

Try these commands:

```
/disk-status
/disk-status 12TB
@noizylab what's the disk status?
@noizylab run a repair
```

**If bot responds → SUCCESS! 🎉**

---

## 📋 Option 2: Manual Setup (Old Way)

If you prefer manual configuration, follow the original README.md instructions.

---

## 🔧 Troubleshooting

### Bot doesn't respond to commands

**Check:**

```bash
# Are scripts executable?
ls -la ~/NOIZYLAB/scripts/*.sh

# Make them executable:
chmod +x ~/NOIZYLAB/scripts/*.sh
```

**Check logs:**

```bash
cd ~/NOIZYLAB/slack-bot
npm run dev
# Look for errors in the output
```

### "Invalid token" error

**Fix:**

- Double-check tokens in .env (no extra spaces!)
- Make sure SLACK_BOT_TOKEN starts with `xoxb-`
- Make sure SLACK_APP_TOKEN starts with `xapp-`
- Reinstall app: OAuth & Permissions → "Reinstall to Workspace"

### Bot can't find scripts

**Fix:**

```bash
# Verify script paths
ls -la /Users/m2ultra/NOIZYLAB/scripts/
# Update .env with correct paths
```

### Commands work but no output

**Fix:**

- Check if user ID is in ALLOWED_USERS
- Check if scripts are executable (`chmod +x`)
- Check script paths in .env

---

## 🚀 Production Deployment

### Option A: Run with PM2 (Recommended)

```bash
# Install PM2
npm install -g pm2

# Start bot
cd ~/NOIZYLAB/slack-bot
pm2 start npm --name "noizylab-bot" -- start

# Save PM2 config
pm2 save

# Setup auto-start on reboot
pm2 startup
# Run the command it outputs

# Monitor
pm2 logs noizylab-bot
pm2 monit
```

**PM2 Commands:**

```bash
pm2 status              # Check status
pm2 restart noizylab-bot # Restart
pm2 stop noizylab-bot    # Stop
pm2 logs noizylab-bot    # View logs
pm2 delete noizylab-bot  # Remove
```

### Option B: Run as macOS LaunchAgent

Create `/Users/m2ultra/Library/LaunchAgents/com.noizylab.slackbot.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.noizylab.slackbot</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/node</string>
        <string>/Users/m2ultra/NOIZYLAB/slack-bot/app.js</string>
    </array>
    <key>WorkingDirectory</key>
    <string>/Users/m2ultra/NOIZYLAB/slack-bot</string>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/Users/m2ultra/NOIZYLAB/slack-bot/logs/stdout.log</string>
    <key>StandardErrorPath</key>
    <string>/Users/m2ultra/NOIZYLAB/slack-bot/logs/stderr.log</string>
</dict>
</plist>
```

**Commands:**

```bash
# Load
launchctl load ~/Library/LaunchAgents/com.noizylab.slackbot.plist

# Unload
launchctl unload ~/Library/LaunchAgents/com.noizylab.slackbot.plist

# Check status
launchctl list | grep noizylab
```

---

## 🏢 Enterprise Grid Deployment

If you need org-wide deployment:

1. **Request Org Approval:**

   - App Settings → "Org Level Apps"
   - Click "Request to Publish"
   - Describe: "Internal disk repair automation tool"

2. **Wait for Admin Approval:**

   - Your org admin will review
   - Usually 1-3 business days

3. **Install Org-Wide:**
   - After approval, go to "Org Level Apps"
   - Click "Install to Organization"
   - Select workspaces

See `ENTERPRISE_GRID_DEPLOYMENT.md` for details.

---

## 📊 Monitoring

### View Logs

```bash
# Development
cd ~/NOIZYLAB/slack-bot
npm run dev

# Production (PM2)
pm2 logs noizylab-bot

# LaunchAgent
tail -f ~/NOIZYLAB/slack-bot/logs/stdout.log
tail -f ~/NOIZYLAB/slack-bot/logs/stderr.log
```

### Daily Health Reports

Bot auto-posts daily reports at 9am to specified channel:

```
🏥 NOIZYLAB Daily Health Report - 2026-01-04

✅ Volume: 12TB - Healthy
⚠️  Volume: Time Machine - Needs Repair
🚨 Volume: RAID5 - CRITICAL

🔧 Actions Taken:
- Ran repair on Time Machine
- Sent alert for RAID5

💾 Total Storage: 45.2TB / 50TB (90.4%)
⚡ System Load: Normal
```

Configure channel in .env:

```bash
DAILY_REPORT_CHANNEL=C01234567  # Get from channel details
DAILY_REPORT_TIME=09:00
```

---

## 🎯 Next Steps

1. ✅ **Test all commands** in Slack
2. ✅ **Add all team members** to ALLOWED_USERS
3. ✅ **Set up daily reports** (configure channel)
4. ✅ **Deploy to production** (PM2 or LaunchAgent)
5. ✅ **Monitor for 24 hours** (check logs)
6. ✅ **Request Enterprise Grid approval** (if needed)

---

## 📚 Resources

- **Original README**: `README.md` (comprehensive guide)
- **Manifest File**: `noizylab-manifest.yaml` (app configuration)
- **Enterprise Grid**: `ENTERPRISE_GRID_DEPLOYMENT.md` (org deployment)
- **Deployment Checklist**: `WHAT_WE_NEED.sh` (run to check status)
- **Slack API Docs**: https://api.slack.com/docs

---

## 🆘 Support

**Bot not working?**

1. Run diagnostics:

   ```bash
   cd ~/NOIZYLAB
   bash WHAT_WE_NEED.sh
   ```

2. Check logs:

   ```bash
   cd ~/NOIZYLAB/slack-bot
   npm run dev
   # Watch for errors
   ```

3. Verify tokens:

   ```bash
   cat .env | grep SLACK_
   # All 3 tokens should be present
   ```

4. Test scripts manually:
   ```bash
   bash ~/NOIZYLAB/scripts/QUICK_STATUS.sh
   # Should output disk status
   ```

---

**🎉 You're all set! Deploy NOIZYLAB in under 5 minutes with the app manifest.**
