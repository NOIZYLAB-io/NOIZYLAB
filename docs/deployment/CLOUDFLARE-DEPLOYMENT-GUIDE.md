# ☁️ CLOUDFLARE WORKERS - COMPLETE GUIDE ☁️

## 📋 TABLE OF CONTENTS
1. [Quick Start](#quick-start)
2. [What's Included](#whats-included)
3. [Prerequisites](#prerequisites)
4. [Deployment](#deployment)
5. [Configuration](#configuration)
6. [Testing](#testing)
7. [Management](#management)
8. [Troubleshooting](#troubleshooting)

---

## 🚀 QUICK START

### One-Command Deployment
```bash
cd cloudflare-workers
chmod +x deploy-all-workers.sh
./deploy-all-workers.sh
```

**Time:** ~5 minutes  
**Cost:** $0 (Free tier covers everything)  
**Result:** 3 workers deployed + D1 database + KV storage

---

## 📦 WHAT'S INCLUDED

### 1. AI GENIUS Cloud Worker
**File:** `ai-genius-worker.js` (15KB)

**Features:**
- 30+ AI models (Claude, Gemini, GPT, Perplexity, Mistral, Cohere, DeepSeek)
- Universal AI routing
- Health monitoring
- Model listing endpoint
- CORS enabled
- Error handling

**Endpoints:**
- `/health` - Health check
- `/models` - List available models
- `/query` - Main AI query endpoint

**Usage:**
```bash
curl -X POST https://ai-genius-cloud.YOUR-ACCOUNT.workers.dev/query \
  -H 'Content-Type: application/json' \
  -d '{"model":"claude-sonnet-4","prompt":"Hello!"}'
```

**Response:**
```json
{
  "success": true,
  "model": "claude-sonnet-4",
  "response": "Hello! How can I help you today?",
  "timing": {
    "duration_ms": 1234,
    "timestamp": "2024-11-24T12:00:00.000Z"
  }
}
```

---

### 2. NOIZYLAB Business Portal
**File:** `noizylab-business-worker.js` (20KB)

**Features:**
- Customer intake form
- Repair tracking
- Status updates
- Dashboard analytics
- Email notifications (AI-generated)
- Beautiful landing page
- Mobile responsive

**Endpoints:**
- `/` - Landing page
- `/submit` - Submit repair form
- `/intake` - API endpoint for intake
- `/status/:id` - Check repair status
- `/repairs` - List all repairs
- `/dashboard` - Analytics dashboard

**Usage:**
```bash
# Submit repair
curl -X POST https://noizylab-business.YOUR-ACCOUNT.workers.dev/intake \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "555-0100",
    "device": "Laptop",
    "issue": "Won'\''t boot"
  }'

# Check status
curl https://noizylab-business.YOUR-ACCOUNT.workers.dev/status/NZL-ABC123
```

**Landing Page:**
- Professional design
- Purple gradient theme
- Feature highlights
- $89 pricing display
- Submit button

---

### 3. NOIZYLAB Workflow Worker
**File:** `noizylab-workflow-worker.js` (18KB)

**Features:**
- 16-step automated workflow
- AI-powered diagnostics
- Email automation
- Payment processing hooks
- Shipping integration
- Analytics tracking

**Workflow Steps:**
1. Initial Assessment (AI)
2. Customer Confirmation (Email)
3. Generate Shipping Label
4. Wait for Device Arrival
5. Device Inspection
6. AI Diagnostics
7. Parts Ordering (if needed)
8. Repair Execution
9. Quality Testing
10. Final Inspection
11. Documentation (AI)
12. Customer Update
13. Payment Processing
14. Return Shipping
15. Ship Device
16. Follow-up & Analytics

**Usage:**
```bash
# Trigger workflow
curl -X POST https://noizylab-workflow.YOUR-ACCOUNT.workers.dev/trigger \
  -H 'Content-Type: application/json' \
  -d '{"repair_id":"NZL-ABC123"}'
```

---

## ✅ PREREQUISITES

### Required
1. **Cloudflare Account** (free)
   - Sign up: https://dash.cloudflare.com/sign-up

2. **Node.js** (v16+)
   ```bash
   node --version  # Should be v16 or higher
   ```

3. **Wrangler CLI**
   ```bash
   npm install -g wrangler
   ```

4. **API Keys**
   - **Anthropic API Key** (required for Claude)
     - Get it: https://console.anthropic.com/
   - **Google API Key** (required for Gemini)
     - Get it: https://makersuite.google.com/app/apikey
   - **OpenAI API Key** (optional for GPT)
     - Get it: https://platform.openai.com/api-keys

### Optional
- Perplexity API Key
- Mistral API Key
- Cohere API Key
- DeepSeek API Key

---

## 🚀 DEPLOYMENT

### Method 1: Automated (Recommended)
```bash
cd cloudflare-workers
chmod +x deploy-all-workers.sh
./deploy-all-workers.sh
```

This script will:
1. Check Wrangler installation
2. Authenticate with Cloudflare
3. Prompt for API keys
4. Create D1 database
5. Create KV namespaces
6. Deploy all 3 workers
7. Save configuration

**Time:** ~5 minutes  
**Interaction:** Minimal (login + API keys)

---

### Method 2: Manual Deployment

#### Step 1: Login
```bash
wrangler login
```

#### Step 2: Set API Keys
```bash
echo "YOUR_ANTHROPIC_KEY" | wrangler secret put ANTHROPIC_API_KEY
echo "YOUR_GOOGLE_KEY" | wrangler secret put GOOGLE_API_KEY
echo "YOUR_OPENAI_KEY" | wrangler secret put OPENAI_API_KEY
```

#### Step 3: Create Database
```bash
wrangler d1 create noizylab-db
wrangler d1 execute noizylab-db --file=schema.sql --remote
```

#### Step 4: Create KV Namespace
```bash
wrangler kv:namespace create REPAIRS
```

#### Step 5: Deploy Workers
```bash
# AI GENIUS
wrangler deploy ai-genius-worker.js --config wrangler-ai-genius.toml

# Business Portal
wrangler deploy noizylab-business-worker.js --config wrangler-business.toml

# Workflow
wrangler deploy noizylab-workflow-worker.js --config wrangler-workflow.toml
```

---

## ⚙️ CONFIGURATION

### Wrangler Configuration Files

**wrangler.toml** (AI GENIUS)
```toml
name = "ai-genius-cloud"
main = "ai-genius-worker.js"
compatibility_date = "2024-11-01"
```

**wrangler-business.toml** (Business Portal)
```toml
name = "noizylab-business"
main = "noizylab-business-worker.js"
compatibility_date = "2024-11-01"

[[kv_namespaces]]
binding = "REPAIRS"
id = "YOUR_KV_ID"

[[d1_databases]]
binding = "DB"
database_name = "noizylab-db"
database_id = "YOUR_DB_ID"
```

**wrangler-workflow.toml** (Workflow)
```toml
name = "noizylab-workflow"
main = "noizylab-workflow-worker.js"
compatibility_date = "2024-11-01"

[[workflows]]
binding = "REPAIR_WORKFLOW"
name = "repair-workflow"
class_name = "RepairWorkflow"

[[kv_namespaces]]
binding = "REPAIRS"
id = "YOUR_KV_ID"

[[d1_databases]]
binding = "DB"
database_name = "noizylab-db"
database_id = "YOUR_DB_ID"
```

### Environment Variables (Secrets)

Set via Wrangler CLI:
```bash
wrangler secret put ANTHROPIC_API_KEY
wrangler secret put GOOGLE_API_KEY
wrangler secret put OPENAI_API_KEY
wrangler secret put PERPLEXITY_API_KEY
wrangler secret put MISTRAL_API_KEY
wrangler secret put COHERE_API_KEY
wrangler secret put DEEPSEEK_API_KEY
```

List secrets:
```bash
wrangler secret list
```

Delete secret:
```bash
wrangler secret delete SECRET_NAME
```

---

## 🧪 TESTING

### Health Checks
```bash
# AI GENIUS
curl https://ai-genius-cloud.YOUR-ACCOUNT.workers.dev/health

# Business Portal
curl https://noizylab-business.YOUR-ACCOUNT.workers.dev/health
```

### AI Query Test
```bash
curl -X POST https://ai-genius-cloud.YOUR-ACCOUNT.workers.dev/query \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "claude-sonnet-4",
    "prompt": "What is GORUNFREE?"
  }'
```

### Business Portal Test
```bash
# Submit test repair
curl -X POST https://noizylab-business.YOUR-ACCOUNT.workers.dev/intake \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Test User",
    "email": "test@example.com",
    "phone": "555-0100",
    "device": "Laptop",
    "issue": "Test issue"
  }'
```

### Database Query
```bash
# View all repairs
wrangler d1 execute noizylab-db \
  --command="SELECT * FROM repairs LIMIT 10" \
  --remote
```

### View Live Logs
```bash
# AI GENIUS
wrangler tail ai-genius-cloud

# Business Portal
wrangler tail noizylab-business

# Workflow
wrangler tail noizylab-workflow
```

---

## 🛠️ MANAGEMENT

### Update Worker
```bash
wrangler deploy WORKER_FILE.js --config CONFIG.toml
```

### View Deployments
```bash
wrangler deployments list
```

### Delete Worker
```bash
wrangler delete WORKER_NAME
```

### Database Management
```bash
# Query database
wrangler d1 execute noizylab-db \
  --command="SELECT * FROM repairs WHERE status='pending'" \
  --remote

# Backup database
wrangler d1 export noizylab-db --remote --output=backup.sql

# Import data
wrangler d1 execute noizylab-db --file=data.sql --remote
```

### KV Management
```bash
# List keys
wrangler kv:key list --namespace-id=YOUR_KV_ID

# Get value
wrangler kv:key get "repair:NZL-ABC123" --namespace-id=YOUR_KV_ID

# Put value
wrangler kv:key put "test:key" "value" --namespace-id=YOUR_KV_ID

# Delete key
wrangler kv:key delete "test:key" --namespace-id=YOUR_KV_ID
```

### Monitor Usage
```bash
# View analytics in Cloudflare Dashboard
# https://dash.cloudflare.com/
# Navigate to: Workers & Pages → Your Worker → Metrics
```

---

## 🐛 TROUBLESHOOTING

### Common Issues

**1. "Not authenticated"**
```bash
wrangler login
```

**2. "Worker not found"**
- Check worker name matches deployment
- View list: `wrangler deployments list`

**3. "API key invalid"**
```bash
# Re-set the secret
wrangler secret put ANTHROPIC_API_KEY
```

**4. "Database not found"**
```bash
# List databases
wrangler d1 list

# Create if missing
wrangler d1 create noizylab-db
```

**5. "KV namespace not found"**
```bash
# List namespaces
wrangler kv:namespace list

# Create if missing
wrangler kv:namespace create REPAIRS
```

**6. "Worker exceeds size limit"**
- Minify code
- Remove unused dependencies
- Use webpack to bundle

**7. "CORS errors"**
- CORS is already enabled in workers
- Check browser console for specific error
- Verify request headers

**8. "Timeout errors"**
- AI queries can take time
- Consider increasing timeout in fetch options
- Use streaming for long responses

### Debug Mode
```bash
# Run locally
wrangler dev WORKER_FILE.js

# View detailed logs
wrangler tail WORKER_NAME --format=pretty
```

### Get Help
```bash
# Wrangler help
wrangler --help

# Command-specific help
wrangler deploy --help
```

---

## 📊 PRICING

### Cloudflare Workers
- **Free Tier:** 100,000 requests/day
- **Paid:** $5/month for 10M requests
- **Our Usage:** ~1,000-5,000 requests/day = FREE

### D1 Database
- **Free Tier:** 5GB storage, 5M reads/day, 100K writes/day
- **Our Usage:** <1MB, <10K operations/day = FREE

### KV Storage
- **Free Tier:** 100K reads/day, 1K writes/day, 1GB storage
- **Our Usage:** <1K operations/day = FREE

### Total Cost
**$0/month** (well within free tiers)

---

## 🎯 NEXT STEPS

### 1. Update Local Scripts
```bash
# Edit universal-ai-selector.py
WORKER_URL = 'https://ai-genius-cloud.YOUR-ACCOUNT.workers.dev'
```

### 2. Test Everything
```bash
# Run test script
./test-all-workers.sh
```

### 3. Open Business Portal
```bash
open https://noizylab-business.YOUR-ACCOUNT.workers.dev
```

### 4. Monitor Usage
- Open Cloudflare Dashboard
- Go to Workers & Pages
- Click on each worker
- View metrics

---

## 🏆 SUCCESS CRITERIA

✅ All 3 workers deployed  
✅ Health endpoints responding  
✅ AI queries working  
✅ Business portal accessible  
✅ Database tables created  
✅ KV storage configured  
✅ Workflow triggers functional  

---

## 📚 ADDITIONAL RESOURCES

- [Cloudflare Workers Docs](https://developers.cloudflare.com/workers/)
- [Wrangler CLI Reference](https://developers.cloudflare.com/workers/wrangler/)
- [D1 Database Docs](https://developers.cloudflare.com/d1/)
- [KV Storage Docs](https://developers.cloudflare.com/workers/runtime-apis/kv/)
- [Workflows Docs](https://developers.cloudflare.com/workflows/)

---

## 🔥 FINAL NOTES

**This is production-ready code.**

- Error handling: ✅
- CORS enabled: ✅
- Health checks: ✅
- Monitoring: ✅
- Scalable: ✅
- Cost-effective: ✅

**Deploy once. Run forever. Pay nothing.**

---

**🚀 GORUNFREE - ONE COMMAND = EVERYTHING DEPLOYED 🚀**
