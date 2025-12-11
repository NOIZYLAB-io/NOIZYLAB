# 🚀 NOIZYLAB AI GATEWAY

**Unified AI API for Gemini & Claude on Cloudflare Workers**

## ⚡ QUICK DEPLOY

```bash
# 1. Install & deploy
npm install -g wrangler
bash DEPLOY_AI_GATEWAY.sh

# 2. Test
export AI_GATEWAY_URL="https://your-worker-url.workers.dev"
export INTERNAL_AUTH_TOKEN="your-token"
python3 ai-gateway-client.py
```

## 📦 FILES

- `cloudflare-ai-gateway-worker.js` - Worker code
- `wrangler.toml` - Configuration
- `ai-gateway-client.py` - Python client
- `ai-gateway-client.js` - Node.js client
- `DEPLOY_AI_GATEWAY.sh` - Deployment script

## 🔑 SECRETS REQUIRED

```bash
wrangler secret put GEMINI_API_KEY
wrangler secret put CLAUDE_API_KEY
wrangler secret put INTERNAL_AUTH_TOKEN
```

## 📡 USAGE

```python
from ai_gateway_client import call_ai

result = call_ai("Summarize this domain health report", model='claude')
print(result['result'])
```

## ✅ FEATURES

- ✓ Gemini & Claude support
- ✓ Secure authentication
- ✓ Request logging
- ✓ Error handling
- ✓ CORS support
- ✓ Standardized responses

