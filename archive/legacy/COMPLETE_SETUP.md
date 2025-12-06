# 🚀 COMPLETE SETUP GUIDE - Cloudflare AI + Gemini

## ONE COMMAND TO RULE THEM ALL

```bash
cd /Users/m2ultra/NOIZYLAB/noizylab-os && ./scripts/setup-cloudflare-gemini.sh
```

**This single command sets up EVERYTHING:**
- ✅ Worker code (production-ready)
- ✅ Cloudflare configuration
- ✅ Database setup
- ✅ KV namespace
- ✅ Dependencies
- ✅ Test scripts
- ✅ Deployment scripts
- ✅ Documentation

---

## 📋 What You Get

### 1. Production-Ready Worker
- **Location:** `workers/ai-super-worker/src/index.ts`
- **Features:**
  - Cloudflare AI integration
  - Gemini integration
  - Smart caching (24-hour TTL)
  - Error handling
  - Usage tracking
  - Streaming support
  - CORS enabled

### 2. Complete Configuration
- `wrangler.toml` - Cloudflare config
- `package.json` - Dependencies
- `tsconfig.json` - TypeScript config
- Database migrations

### 3. Helper Scripts
- `test-ai.sh` - Comprehensive testing
- `deploy-ai.sh` - One-command deployment
- `validate-setup.sh` - Validation checker

---

## 🎯 Quick Start

### Step 1: Run Setup
```bash
cd /Users/m2ultra/NOIZYLAB/noizylab-os
./scripts/setup-cloudflare-gemini.sh
```

### Step 2: Get Gemini API Key
1. Go to: https://aistudio.google.com/app/apikey
2. Create API key
3. Copy it

### Step 3: Update Configuration
Edit `workers/ai-super-worker/wrangler.toml`:
- Replace `REPLACE_WITH_YOUR_DB_ID` with your database ID
- Replace `REPLACE_WITH_YOUR_KV_ID` with your KV namespace ID
- Replace `REPLACE_WITH_YOUR_GEMINI_API_KEY` with your Gemini API key

### Step 4: Test
```bash
cd workers/ai-super-worker
wrangler dev
# In another terminal:
../../scripts/test-ai.sh
```

### Step 5: Deploy
```bash
./scripts/deploy-ai.sh
```

---

## 📊 API Endpoints

### Health Check
```bash
GET /health
```

### List Providers
```bash
GET /api/ai/providers
```

### Chat (Cloudflare AI)
```bash
POST /api/ai/chat
Content-Type: application/json

{
  "prompt": "Your question",
  "provider": "cloudflare",
  "model": "llama-3.1-8b",
  "temperature": 0.7
}
```

### Chat (Gemini)
```bash
POST /api/ai/chat
Content-Type: application/json

{
  "prompt": "Your question",
  "provider": "gemini",
  "model": "gemini-pro"
}
```

### Chat (Auto - uses best available)
```bash
POST /api/ai/chat
Content-Type: application/json

{
  "prompt": "Your question",
  "provider": "auto"
}
```

### Stats
```bash
GET /api/ai/stats
```

---

## ✅ Validation

Check your setup:
```bash
./scripts/validate-setup.sh
```

---

## 🎉 You're Ready!

Everything is production-ready:
- ✅ Error handling
- ✅ Input validation
- ✅ Caching
- ✅ Logging
- ✅ Monitoring
- ✅ Documentation

**Just run the one command and you're done!**

