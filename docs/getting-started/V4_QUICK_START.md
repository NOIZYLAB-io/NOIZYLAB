# 🚀 V4 Quick Start Guide

## What's V4?

NoizyLab V4 is the **Enterprise Edition** with:
- 🔐 **Security**: JWT authentication, API keys, RBAC
- ⚡ **Performance**: Redis caching, database optimization
- 🤖 **Advanced AI**: Multi-model ensemble (Gemini + Claude)
- 📱 **Mobile**: iOS Shortcuts integration
- 🔗 **Integrations**: Webhook hub for Zapier, Make.com, Slack
- 📊 **Enhanced Dashboard**: Login, themes, multi-export

## Quick Start (3 Steps)

### 1. Install Redis (for caching)
```bash
brew install redis
redis-server
```

### 2. Setup Authentication
```bash
cd ~/NOIZYLAB/security
python3 auth-manager.py
# Creates admin user, saves API key
```

### 3. Start Everything
```bash
~/NOIZYLAB/START_V4.sh
```

Or use the launcher:
```bash
~/NOIZYLAB/launch-v3
# Choose option A) Start V4 Everything
```

## Access Points

- **V4 API**: http://localhost:8000
- **V4 Dashboard**: http://localhost:8501 (login required)
- **Mobile API**: http://localhost:8002
- **Webhook Hub**: http://localhost:8001

## First API Call

```bash
# Use the API key from auth-manager.py
curl -H "X-API-Key: your-api-key" \
  http://localhost:8000/validate \
  -d '{"email": "test@example.com"}'
```

## Dashboard Login

1. Go to http://localhost:8501
2. Password: Set in `~/.streamlit/secrets.toml`:
   ```toml
   DASHBOARD_PASSWORD = "your-password"
   ANTHROPIC_API_KEY = "your-claude-key"
   ```

## Mobile (iOS Shortcuts)

1. Open iOS Shortcuts app
2. Create new shortcut
3. Add "Get Contents of URL"
4. URL: `http://your-ip:8002/mobile/validate?email={email}&api_key=mobile-key`

## Webhook Integration

### Zapier
```bash
POST http://localhost:8001/zapier/email-validated
{
  "email": "user@example.com",
  "valid": true
}
```

### Register Webhook
```bash
POST http://localhost:8001/webhook/register
{
  "name": "My Webhook",
  "url": "https://your-webhook-url.com",
  "events": ["email_validated", "email_enriched"]
}
```

## Performance Optimization

Run once to optimize database:
```bash
cd ~/NOIZYLAB/performance
python3 optimizer.py
```

## What's Different from V3?

| Feature | V3 | V4 |
|---------|----|----|
| Auth | ❌ | ✅ JWT + API Keys |
| Caching | Memory | ✅ Redis |
| AI | Gemini only | ✅ Gemini + Claude |
| Mobile | ❌ | ✅ iOS Shortcuts |
| Webhooks | ❌ | ✅ Full Hub |
| Dashboard Auth | ❌ | ✅ Login Required |
| Performance | Basic | ✅ Optimized |

## Troubleshooting

### Redis not running
```bash
brew services start redis
# Or
redis-server
```

### API key not working
```bash
cd ~/NOIZYLAB/security
python3 auth-manager.py
# Creates new user with API key
```

### Dashboard login not working
Check `~/.streamlit/secrets.toml` exists and has password set.

### Claude not working
Add `ANTHROPIC_API_KEY` to environment or secrets.toml.

## Next Steps

1. ✅ Start V4 services
2. ✅ Get API key from auth-manager
3. ✅ Test API endpoint
4. ✅ Login to dashboard
5. ✅ Register webhooks
6. ✅ Setup iOS Shortcuts
7. ✅ Optimize database

---

**NoizyLab V4 is ready!** 🚀✨

