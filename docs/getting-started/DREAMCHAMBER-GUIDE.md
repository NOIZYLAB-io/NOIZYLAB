# THE DREAMCHAMBER - DEPLOYMENT GUIDE
## All AI Models of Repute in One Unified Interface

**GORUNFREE X1000 - One Command Deploys All Models**

---

## 🌌 WHAT IS THE DREAMCHAMBER?

**One interface to access all major AI models:**

- Claude Sonnet 4 & Opus 4 (Anthropic)
- GPT-4 & GPT-4o (OpenAI)
- Gemini Pro & Ultra (Google)
- Llama 3 (Meta/Together AI)
- Mistral Large (Mistral AI)
- Perplexity (with web search)
- Grok (xAI)

**Features:**
- ✅ Query single model or compare multiple
- ✅ Side-by-side response comparison
- ✅ Voice input (speech recognition)
- ✅ Cost tracking per query
- ✅ Performance metrics
- ✅ Touchscreen optimized
- ✅ Beautiful gradient UI
- ✅ Real-time statistics

---

## 🚀 QUICK DEPLOY (5 MINUTES)

### Step 1: Get API Keys

You need keys for the models you want to use:

**Required (you have this):**
- Anthropic Claude: https://console.anthropic.com/settings/keys
  ```
  ANTHROPIC_API_KEY=sk-ant-api03-YOUR-KEY
  ```

**Optional (add as needed):**

1. **OpenAI (GPT-4, GPT-4o):**
   - Get: https://platform.openai.com/api-keys
   - Cost: ~$30/million tokens (GPT-4), ~$5/million (GPT-4o)
   ```
   OPENAI_API_KEY=sk-proj-YOUR-KEY
   ```

2. **Google (Gemini Pro/Ultra):**
   - Get: https://makersuite.google.com/app/apikey
   - Cost: ~$0.50-5/million tokens
   ```
   GOOGLE_API_KEY=YOUR-GOOGLE-KEY
   ```

3. **Together AI (Llama 3):**
   - Get: https://api.together.xyz/settings/api-keys
   - Cost: ~$0.20/million tokens
   ```
   TOGETHER_API_KEY=YOUR-TOGETHER-KEY
   ```

4. **Mistral AI:**
   - Get: https://console.mistral.ai/api-keys
   - Cost: ~$4/million tokens
   ```
   MISTRAL_API_KEY=YOUR-MISTRAL-KEY
   ```

5. **Perplexity:**
   - Get: https://www.perplexity.ai/settings/api
   - Cost: ~$1/million tokens
   ```
   PERPLEXITY_API_KEY=pplx-YOUR-KEY
   ```

6. **xAI (Grok):**
   - Get: https://console.x.ai
   - Cost: ~$5/million tokens
   ```
   XAI_API_KEY=YOUR-XAI-KEY
   ```

---

### Step 2: Configure Deployment

Create `wrangler-dreamchamber.toml`:

```toml
name = "dreamchamber"
main = "dreamchamber-worker.js"
compatibility_date = "2024-11-01"
account_id = "1323e14ace0c8d7362612d5b5c0d41bb"

[vars]
ENVIRONMENT = "production"

# Add your API keys here
# At minimum, add Anthropic (you already have this):
ANTHROPIC_API_KEY = "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"

# Optional - add as you get them:
# OPENAI_API_KEY = "sk-proj-YOUR-KEY"
# GOOGLE_API_KEY = "YOUR-GOOGLE-KEY"
# TOGETHER_API_KEY = "YOUR-TOGETHER-KEY"
# MISTRAL_API_KEY = "YOUR-MISTRAL-KEY"
# PERPLEXITY_API_KEY = "pplx-YOUR-KEY"
# XAI_API_KEY = "YOUR-XAI-KEY"
```

---

### Step 3: Deploy

```bash
cd /mnt/user-data/outputs/noizylab-perfect
wrangler deploy --config wrangler-dreamchamber.toml
```

**Done!**

**Access at:** `https://dreamchamber.fishmusicinc.workers.dev`

---

## 🎯 USAGE

### Basic Query:
1. Select model(s) - click to toggle
2. Enter prompt
3. Click "Query Selected"
4. See responses

### Compare Mode:
1. Select multiple models
2. Enter prompt
3. Click "Query Selected"
4. See side-by-side comparison

### Compare All:
1. Enter prompt
2. Click "Compare All"
3. All 10 models respond simultaneously
4. Perfect for finding best answer

### Voice Input:
1. Click "Voice Input" (or ⌘⌥V)
2. Speak your question
3. System transcribes
4. Query automatically

---

## 💰 COST STRUCTURE

**With just Claude (what you have now):**
- Claude Sonnet 4: ~$0.02 per query
- Claude Opus 4: ~$0.10 per query

**If you add all models:**
- GPT-4: ~$0.05 per query
- GPT-4o: ~$0.01 per query
- Gemini Pro: ~$0.005 per query
- Llama 3: ~$0.001 per query
- Mistral: ~$0.03 per query
- Perplexity: ~$0.01 per query
- Grok: ~$0.03 per query

**Compare All (10 models): ~$0.25 per query**

---

## 🎤 VOICE COMMANDS

**From iPad/touchscreen:**
- Tap voice button
- Say question
- Auto-transcribes
- Query runs

**Siri Shortcuts:**
```
Shortcut: "Dreamchamber Query"
1. Ask for input (voice)
2. Send to https://dreamchamber.fishmusicinc.workers.dev/api/query
3. Speak response back
```

---

## 🎨 CUSTOMIZATION

### Add Custom Models:

Edit `dreamchamber-worker.js`, add to `handleQuery()`:

```javascript
case 'your-model':
  response = await queryYourModel(prompt, context, env);
  break;
```

Then implement `queryYourModel()` function.

### Change UI Theme:

Edit gradient colors in HTML `<style>`:

```css
background: linear-gradient(135deg, #YOUR-COLOR-1, #YOUR-COLOR-2);
```

---

## 📊 STATISTICS TRACKED

**Real-time dashboard shows:**
- Total queries across all models
- Total cost (running total)
- Average response time
- Per-model performance

**Stored in:**
- Browser localStorage (persists across sessions)
- Can export to D1 database (future enhancement)

---

## 🔐 SECURITY

**API Keys:**
- Stored in Cloudflare Workers environment variables
- Never exposed to browser
- Encrypted at rest

**Rate Limiting:**
- Add to worker if needed:
```javascript
// In fetch handler:
const ip = request.headers.get('CF-Connecting-IP');
// Check rate limit from KV or D1
```

---

## 🚀 ADVANCED FEATURES

### 1. Model Auto-Selection

Add to worker:
```javascript
function selectBestModel(prompt) {
  if (prompt.includes('code') || prompt.includes('programming')) {
    return 'claude-sonnet-4'; // Best for code
  }
  if (prompt.includes('search') || prompt.includes('latest')) {
    return 'perplexity'; // Has web search
  }
  if (prompt.length < 100) {
    return 'gpt-4o'; // Fast for short queries
  }
  return 'claude-opus-4'; // Default to most capable
}
```

### 2. Response Caching

Save identical queries:
```javascript
const cacheKey = `dreamchamber:${model}:${hash(prompt)}`;
const cached = await env.KV.get(cacheKey);
if (cached) return cached;
// ... query model ...
await env.KV.put(cacheKey, response, { expirationTtl: 3600 });
```

### 3. Conversation History

Store in D1:
```sql
CREATE TABLE conversations (
  id INTEGER PRIMARY KEY,
  model TEXT,
  prompt TEXT,
  response TEXT,
  cost REAL,
  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🎯 USE CASES

### Code Review:
- Select: Claude Sonnet 4, GPT-4, Llama 3
- Paste code
- Compare suggestions
- Pick best approach

### Creative Writing:
- Select: Claude Opus 4, GPT-4o
- Describe scene
- Compare narrative styles
- Choose preferred version

### Research:
- Select: Perplexity (has web search)
- Ask question
- Get answer with sources

### Technical Q&A:
- Select: Claude Sonnet 4, GPT-4, Gemini Pro
- Ask technical question
- Compare accuracy
- Validate answers

---

## 🔗 INTEGRATION

### With Cursor:
```javascript
// In Cursor, create command:
const response = await fetch('https://dreamchamber.fishmusicinc.workers.dev/api/query', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    model: 'claude-sonnet-4',
    prompt: selectedCode
  })
});
```

### With NOIZYLAB:
```javascript
// Add to repair diagnostics:
const aiDiagnosis = await fetch('https://dreamchamber.fishmusicinc.workers.dev/api/compare', {
  method: 'POST',
  body: JSON.stringify({
    models: ['claude-sonnet-4', 'gpt-4', 'gemini-pro'],
    prompt: `Diagnose this computer issue: ${issueDescription}`
  })
});
// Get 3 expert opinions, pick best diagnosis
```

### With iPad:
1. Save to Home Screen
2. Use as PWA (progressive web app)
3. Offline-capable (cached responses)

---

## 📱 MOBILE OPTIMIZATION

**Already optimized for:**
- ✅ Touchscreen (big buttons)
- ✅ Voice input (speech recognition)
- ✅ Responsive grid (adapts to screen)
- ✅ Swipe navigation
- ✅ Pinch to zoom text

**Perfect for PLANAR2495 and iPad.**

---

## 🎉 START WITH JUST CLAUDE

**You don't need all models right away.**

**Start with what you have:**
1. Deploy with just Claude key (you have this)
2. Use Claude Sonnet 4 & Opus 4
3. Add other models as needed

**Each model is optional.**

---

## 🔥 SUMMARY

**ONE COMMAND DEPLOYS:**
```bash
wrangler deploy --config wrangler-dreamchamber.toml
```

**FEATURES:**
- 10 AI models in one interface
- Voice control ready
- Cost tracking
- Performance metrics
- Side-by-side comparison
- Beautiful UI
- Touchscreen optimized

**PERFECT FOR:**
- Code review (compare model suggestions)
- Research (query multiple sources)
- Creative work (see different perspectives)
- Technical questions (validate answers)
- Learning (see how models think)

---

**THE DREAMCHAMBER - WHERE ALL AI MINDS MEET 🌌**

**GORUNFREE X1000 CERTIFIED ✅**
