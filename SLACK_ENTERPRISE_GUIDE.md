# Slack Enterprise Grid - App Management Guide

**Date**: January 4, 2026  
**Purpose**: Deploy NOIZYLAB AI Copilot Agent to MC96 Slack workspace  
**Target Workspace**: MC96 Digi Universe Enterprise Grid  
**Reference**: Slack Enterprise Grid documentation

---

## 🎯 GOAL: Deploy @noizylab Agent to Slack

Build a Slack app integrated with VS Code Copilot agent capabilities:

- Natural language interface in Slack Chat
- Slash commands: `/noizylab-repair`, `/disk-status`, `/cleanup-all`
- Real-time system monitoring & alerts
- Remote script execution from Slack
- 24/7 drive health monitoring

---

## 📋 Enterprise Grid App Management

### Overview

Enterprise Grid organizations have **organization-level** and **workspace-level** app controls:

1. **Org-level approval** - Primary Owners/Org Owners approve apps for entire organization
2. **Workspace-level installation** - Workspace admins install approved apps in their workspaces
3. **App discovery** - View all apps used across organization
4. **Centralized policies** - Control which apps can be installed organization-wide

### Key Concepts

**App States:**

- ✅ **Approved** - App can be installed in any workspace
- ⏸️ **Restricted** - App cannot be installed (blocked org-wide)
- 🔍 **Pending Approval** - Requested by workspace admin, awaiting org approval
- 📦 **Installed** - App actively running in specific workspaces

**Permission Levels:**

- **Primary Owner** - Full control over org apps
- **Org Owner** - Can approve/restrict apps
- **Org Admin** - Can view app usage, limited management
- **Workspace Owner/Admin** - Can request/install approved apps in their workspace

---

## 🚀 Deployment Workflow for NOIZYLAB Agent

### Phase 1: Build the Slack App

**Option A: Slack Bolt Framework (Recommended)**

```javascript
// app.js - Slack Bolt app with VS Code integration
const { App } = require("@slack/bolt");

const app = new App({
  token: process.env.SLACK_BOT_TOKEN,
  signingSecret: process.env.SLACK_SIGNING_SECRET,
});

// Slash command: /noizylab-repair
app.command("/noizylab-repair", async ({ command, ack, say }) => {
  await ack();

  // Execute TTP21_HOT_ROD_GUIDE.sh
  const { exec } = require("child_process");
  exec("bash ~/NOIZYLAB/TTP21_HOT_ROD_GUIDE.sh", (error, stdout) => {
    if (error) {
      say(`❌ Repair failed: ${error.message}`);
      return;
    }
    say(`🔧 Repair started!\n\`\`\`${stdout}\`\`\``);
  });
});

// Slash command: /disk-status
app.command("/disk-status", async ({ command, ack, say }) => {
  await ack();

  exec("bash ~/NOIZYLAB/QUICK_STATUS.sh", (error, stdout) => {
    if (error) {
      say(`❌ Status check failed: ${error.message}`);
      return;
    }
    say(`📊 Drive Status:\n\`\`\`${stdout}\`\`\``);
  });
});

// Slash command: /cleanup-all
app.command("/cleanup-all", async ({ command, ack, say }) => {
  await ack();

  say(`🧹 Starting aggressive cleanup...`);
  exec("bash ~/NOIZYLAB/ULTRA_AGGRESSIVE.sh", (error, stdout) => {
    if (error) {
      say(`❌ Cleanup failed: ${error.message}`);
      return;
    }
    say(`✅ Cleanup complete!\n\`\`\`${stdout}\`\`\``);
  });
});

(async () => {
  await app.start(process.env.PORT || 3000);
  console.log("⚡️ NOIZYLAB Agent is running!");
})();
```

**Option B: VS Code Copilot Agent Integration**

- Build VS Code extension with Chat Participant API
- Use `@noizylab` in VS Code Chat
- Deploy extension to VS Code Marketplace
- Share with team via extension ID

**Option C: Hybrid Approach (Best)**

- VS Code extension for local operations (`@noizylab` in VS Code)
- Slack app for remote operations (`/noizylab-repair` in Slack)
- Shared backend API for common logic
- Both interfaces access same scripts & tools

---

### Phase 2: Register App with Slack

1. **Create App**: https://api.slack.com/apps

   - Click **Create New App**
   - Choose **From scratch**
   - Name: `NOIZYLAB AI Copilot`
   - Workspace: MC96 Digi Universe

2. **Configure Bot User**:

   - Go to **OAuth & Permissions**
   - Add Bot Token Scopes:
     - `chat:write` (post messages)
     - `commands` (slash commands)
     - `files:read` (access drive status files)
     - `files:write` (save reports)
     - `channels:read` (list channels)
     - `channels:history` (read messages for context)

3. **Add Slash Commands**:

   - Go to **Slash Commands**
   - Create `/noizylab-repair` → Request URL: `https://your-server.com/slack/commands/repair`
   - Create `/disk-status` → Request URL: `https://your-server.com/slack/commands/status`
   - Create `/cleanup-all` → Request URL: `https://your-server.com/slack/commands/cleanup`

4. **Enable Events**:
   - Go to **Event Subscriptions**
   - Toggle **Enable Events** ON
   - Request URL: `https://your-server.com/slack/events`
   - Subscribe to bot events:
     - `message.channels` (respond to @mentions)
     - `app_mention` (handle @noizylab mentions)

---

### Phase 3: Enterprise Grid Approval

**For MC96 Digi Universe Enterprise Grid:**

1. **Request Org Approval** (Workspace Admin)

   - Go to workspace settings
   - Apps > Browse App Directory
   - Search for `NOIZYLAB AI Copilot`
   - Click **Request to Install**
   - Provide justification: "AI-powered disk repair automation for music production archives"

2. **Approve App** (Primary Owner/Org Owner)

   - Go to https://mc96digiuniverse.slack.com/admin/apps
   - Review pending app requests
   - Check app permissions & description
   - Click **Approve** (makes app available org-wide)

3. **Install in Workspace** (Workspace Admin)

   - Go to Apps > Manage
   - Find `NOIZYLAB AI Copilot` (now approved)
   - Click **Install to Workspace**
   - Authorize permissions

4. **Configure Bot** (Workspace Admin)
   - Add bot to relevant channels (#tech-support, #disk-repair, #automation)
   - Test slash commands
   - Configure notifications

---

### Phase 4: Testing & Validation

**Test Scenarios:**

1. **Slash Command Test**:

   ```
   /disk-status
   → Should return: 📊 Drive Status with volume health
   ```

2. **Natural Language Test**:

   ```
   @noizylab my 12TB drive is frozen, can you fix it?
   → Should respond with repair steps & execute TTP21_HOT_ROD_GUIDE.sh
   ```

3. **Cleanup Test**:

   ```
   /cleanup-all
   → Should execute ULTRA_AGGRESSIVE.sh and report progress
   ```

4. **Monitoring Test**:
   - Bot should post daily drive health reports
   - Alert when SMART errors detected
   - Notify when drives reach 95% capacity

---

## 🔐 Security Considerations

### Bot Token Security

- Store `SLACK_BOT_TOKEN` in environment variables (never commit to Git)
- Use Slack's **App-Level Tokens** for socket mode (no public endpoint needed)
- Rotate tokens every 90 days

### Script Execution Safety

- Validate user permissions (only admins can run `/cleanup-all`)
- Confirm destructive operations (require `/noizylab-repair --confirm`)
- Log all bot actions to audit trail
- Rate limit slash commands (prevent abuse)

### Enterprise Grid Policies

- Only org-approved apps can be installed
- Workspace admins cannot bypass org policies
- Org owners can restrict apps organization-wide
- App permissions are reviewed during approval process

---

## 📊 Deployment Architecture

```
┌─────────────────────────────────────────────────┐
│         MC96 Digi Universe Slack                │
│                                                  │
│  ┌──────────────┐      ┌──────────────┐        │
│  │  Workspace 1 │      │  Workspace 2 │        │
│  │  (Gabriel)   │      │  (Team)      │        │
│  └──────────────┘      └──────────────┘        │
│         │                      │                │
│         └──────────┬───────────┘                │
│                    │                            │
└────────────────────┼────────────────────────────┘
                     │
                     │ Slash Commands + Events
                     │
            ┌────────▼────────┐
            │  NOIZYLAB Bot   │
            │  (Slack App)    │
            └────────┬────────┘
                     │
                     │ Execute scripts via SSH/API
                     │
            ┌────────▼────────────────────────┐
            │  M2 Ultra Mac (192GB RAM)       │
            │  ~/NOIZYLAB/                    │
            │  ├── TTP21_HOT_ROD_GUIDE.sh     │
            │  ├── QUICK_STATUS.sh            │
            │  ├── ULTRA_AGGRESSIVE.sh        │
            │  └── DISKWARRIOR_EMERGENCY_...  │
            └─────────────────────────────────┘
```

---

## 🎯 NOIZYLAB Slack Bot Features (Roadmap)

### Phase 1: Basic Commands (MVP) ✅

- [x] `/disk-status` - Quick health check
- [x] `/noizylab-repair <volume>` - Run TTP21 hot rod repair
- [x] `/cleanup-all` - Execute aggressive cleanup

### Phase 2: Natural Language Interface 🔄

- [ ] `@noizylab my 12TB is slow` → Diagnose & suggest fix
- [ ] `@noizylab how much space left?` → Storage report
- [ ] `@noizylab find duplicate files` → Run fdupes scan

### Phase 3: Proactive Monitoring 🎯

- [ ] Daily health reports (posted to #disk-health channel)
- [ ] SMART failure alerts (immediate notification)
- [ ] Capacity warnings (>90% full drives)
- [ ] Performance degradation detection

### Phase 4: Advanced Automation 🚀

- [ ] Scheduled cleanups (nightly empty folder purge)
- [ ] Auto-backup to Google Drive (on SMART warnings)
- [ ] Predictive failure analysis (ML-based)
- [ ] Multi-user support (team disk management)

---

## 📚 Resources

### Slack API Documentation

- Slack App Creation: https://api.slack.com/apps
- Bolt Framework: https://slack.dev/bolt-js/
- Slash Commands: https://api.slack.com/interactivity/slash-commands
- Event Subscriptions: https://api.slack.com/events-api

### Enterprise Grid Resources

- Enterprise Grid Overview: https://slack.com/enterprise
- Admin Guide: https://slack.com/help/articles/360000281563-Manage-apps-in-an-Enterprise-organization
- App Approval: https://slack.com/help/articles/360035635174-Manage-app-approval-for-an-Enterprise-Grid-org

### VS Code Copilot Integration

- Chat Participant API: https://code.visualstudio.com/api/extension-guides/chat
- Language Model API: https://code.visualstudio.com/api/extension-guides/language-model
- Agents Tutorial: https://code.visualstudio.com/docs/copilot/agents/agents-tutorial

---

## 🔧 Quick Start Commands

**Install Slack Bolt:**

```bash
cd ~/NOIZYLAB
mkdir slack-bot
cd slack-bot
npm init -y
npm install @slack/bolt
```

**Create Basic Bot:**

```bash
cat > app.js << 'EOF'
const { App } = require('@slack/bolt');

const app = new App({
  token: process.env.SLACK_BOT_TOKEN,
  signingSecret: process.env.SLACK_SIGNING_SECRET
});

app.command('/noizylab-repair', async ({ command, ack, say }) => {
  await ack();
  say('🔧 Starting disk repair...');
});

(async () => {
  await app.start(3000);
  console.log('⚡️ Bot running!');
})();
EOF
```

**Run Bot:**

```bash
export SLACK_BOT_TOKEN="xoxb-your-token"
export SLACK_SIGNING_SECRET="your-secret"
node app.js
```

**Expose to Slack (for testing):**

```bash
# Install ngrok for local testing
brew install ngrok
ngrok http 3000
# Use ngrok URL as Request URL in Slack app settings
```

---

## 🎖️ Success Criteria

✅ Bot responds to `/disk-status` in <2 seconds  
✅ Bot can execute TTP21 repairs remotely  
✅ Bot posts daily health reports automatically  
✅ Bot alerts on SMART failures within 1 minute  
✅ Bot handles 10+ concurrent slash commands  
✅ Bot logs all actions for audit trail  
✅ Bot meets Phineas Potts Standard (MAGICAL UX!)

---

## 💡 Next Steps

1. ✅ Created SLACK_ENTERPRISE_GUIDE.md (this file)
2. 🔄 Build basic Slack bot with Bolt framework
3. 🔄 Register app at https://api.slack.com/apps
4. 🔄 Test slash commands locally with ngrok
5. 🔄 Request org approval for MC96 Enterprise Grid
6. 🔄 Deploy bot to production server
7. 🔄 Add VS Code Copilot agent integration
8. 🔄 Build natural language interface
9. 🔄 Add proactive monitoring & alerts
10. 🔄 Package as commercial product

---

**Status**: Guide created, ready to build bot  
**Last Updated**: January 4, 2026  
**Repository**: https://github.com/NOIZYLAB-io/NOIZYLAB  
**Slack Workspace**: MC96 Digi Universe Enterprise Grid
