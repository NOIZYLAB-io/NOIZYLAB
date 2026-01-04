# NOIZYLAB SLACK INTEGRATION GUIDE

## SETUP STEPS

### 1. Create Workspace
Go to: https://slack.com/get-started
- Workspace name: `NOIZYLAB`
- URL: `noizylab.slack.com`

### 2. Create Channels
```
#mission-control    - GORUNFREE executions, system commands
#daily-flow         - DAZEFLOW updates
#heaven-status      - noizy.ai system health
#gabriel            - AI agent conversations
#dev                - Technical work
#lifeluv            - M3 project
#noizykidz          - Accessibility projects
#anthropic          - Fellows program
```

### 3. Install Apps
From Slack App Directory:
- **Claude** (Anthropic) - Add to workspace
- **GitHub** - Connect repos
- **Google Calendar** - Schedule sync

### 4. Enable Webhooks (for automation)
1. Go to: https://api.slack.com/apps
2. Create New App → "NOIZYLAB Bot"
3. Enable Incoming Webhooks
4. Add webhook to #mission-control
5. Save webhook URL to: `~/NOIZYLAB/config/slack_webhook.txt`

### 5. Connect GORUNFREE to Slack
Once webhook is saved, notifications will auto-post to Slack.

---

## WEBHOOK USAGE

```bash
# Post to Slack from command line
curl -X POST -H 'Content-type: application/json' \
  --data '{"text":"⚡ GORUNFREE executed"}' \
  $(cat ~/NOIZYLAB/config/slack_webhook.txt)
```

---

## FUTURE: GABRIEL SLACK BOT

When ready, we'll build a full Slack bot that:
- Responds to `/gabriel [prompt]`
- Responds to `/gorunfree [task]`
- Posts automated health updates
- Handles voice commands via integration

Code location: `~/NOIZYLAB/GABRIEL/src/slack-bot/`

---

🔥 GORUNFREE
