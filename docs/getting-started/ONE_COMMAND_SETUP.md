# 🚀 ONE COMMAND SETUP - Cloudflare AI + Gemini

## Copy This ONE Command:

```bash
cd /Users/m2ultra/NOIZYLAB/noizylab-os && ./scripts/setup-cloudflare-gemini.sh
```

**That's it!** This single command sets up:
- ✅ Cloudflare AI worker
- ✅ Gemini integration
- ✅ Database setup
- ✅ KV namespace
- ✅ Configuration files
- ✅ Test scripts
- ✅ Everything!

---

## What It Does:

1. Creates complete AI worker with both providers
2. Sets up Cloudflare (login, database, KV)
3. Creates all configuration files
4. Installs dependencies
5. Applies database migrations
6. Creates test scripts

---

## After Running:

1. **Get Gemini API Key:**
   - Go to: https://aistudio.google.com/app/apikey
   - Create key
   - Add to `workers/ai-super-worker/wrangler.toml`

2. **Update wrangler.toml:**
   - Add database_id (from setup output)
   - Add KV namespace id (from setup output)
   - Add GEMINI_API_KEY

3. **Test:**
   ```bash
   cd workers/ai-super-worker
   wrangler dev
   # In another terminal:
   ./scripts/test-ai.sh
   ```

4. **Deploy:**
   ```bash
   cd workers/ai-super-worker
   wrangler deploy
   ```

---

## Usage:

### Cloudflare AI:
```bash
curl -X POST https://ai.noizylab.ca/api/ai/chat \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Hello","provider":"cloudflare"}'
```

### Gemini:
```bash
curl -X POST https://ai.noizylab.ca/api/ai/chat \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Hello","provider":"gemini"}'
```

---

**Just copy and run the ONE command above!** 🚀

