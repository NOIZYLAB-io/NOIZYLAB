# Webhook AI Analysis Upgrade 🚀

## ✅ New Features Added

### 1. **AI-Powered Event Analysis**
- ✅ Cloudflare Workers AI integration
- ✅ Llama 3.1 8B Instruct model support
- ✅ Event emotion, vibe, intent analysis
- ✅ Engagement and loyalty scoring
- ✅ Purchase likelihood prediction
- ✅ Spam and bot detection
- ✅ Actionable recommendations

### 2. **Enhanced Webhook Processing**
- ✅ Platform detection (Ko-fi, YouTube, Instagram, SoundCloud, Stripe, GitHub, PayPal, Patreon, TikTok)
- ✅ Webhook normalization into consistent format
- ✅ AI enrichment pipeline
- ✅ Automatic forwarding to MC96 endpoints
- ✅ Comprehensive audit trail

### 3. **Resilience & Reliability**
- ✅ Circuit breakers for AI calls (per-model)
- ✅ Retry logic with exponential backoff
- ✅ Timeout protection (30s for AI)
- ✅ Graceful degradation (falls back to normalization if AI fails)
- ✅ Error handling and validation

### 4. **New Packages**

#### `packages/ai-analyzer/`
- `types.ts` - TypeScript definitions for analysis results
- `prompt.ts` - Prompt building and response parsing
- `index.ts` - Main analysis engine with circuit breakers

#### `packages/webhook-normalizer/`
- `types.ts` - Webhook type definitions
- `detector.ts` - Platform detection logic
- `normalizers.ts` - Platform-specific normalizers
- `enrich.ts` - AI enrichment functions
- `index.ts` - Main processing pipeline

### 5. **Worker Endpoints**

#### `/webhook` (default)
- Accepts POST requests
- Detects platform automatically
- Normalizes webhook
- Optionally enriches with AI
- Stores in KV storage
- Forwards to MC96_ENDPOINT if configured

#### `/analyze`
- Requires valid JSON
- Forces AI analysis
- Returns enriched event

#### `/healthz` & `/metrics`
- Health check and metrics endpoints

## 📊 AI Analysis Output

```json
{
  "emotion": "happy",
  "vibe": "positive",
  "intent": "support",
  "engagement_score": 0.85,
  "loyalty_score": 0.90,
  "purchase_likelihood": "high",
  "spam_score": 0.05,
  "bot_probability": 0.02,
  "recommended_action": "thank_user"
}
```

## 🔧 Configuration

### Environment Variables

```toml
ENABLE_AI_ANALYSIS = "true"  # Enable/disable AI enrichment
AI_MODEL = "@cf/meta/llama-3.1-8b-instruct"  # AI model to use
MC96_ENDPOINT = "https://your-endpoint.com/webhook"  # Forwarding endpoint
```

### KV Namespaces

- `NOIZY_EVENTS` - Stores normalized and enriched events
  - Keys: `norm-{timestamp}-{platform}-{id}` or `ai-{timestamp}-{platform}-{id}`
  - Values: JSON stringified events

### AI Binding

```toml
[ai]
binding = "AI"
```

## 🎯 Usage Examples

### Basic Webhook (Auto-detect & Normalize)
```bash
curl -X POST https://your-worker.workers.dev/webhook \
  -H "Content-Type: application/json" \
  -d '{
    "platform": "kofi",
    "payload": {
      "type": "Donation",
      "from_name": "User123",
      "amount": "10.00",
      "currency": "USD"
    }
  }'
```

### Force AI Analysis
```bash
curl -X POST https://your-worker.workers.dev/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "platform": "kofi",
    "type": "donation",
    "user": "User123",
    "message": "Keep up the great work!",
    "timestamp": 1234567890
  }'
```

## 🔄 Processing Flow

1. **Receive** → Parse incoming webhook
2. **Detect** → Identify platform (Ko-fi, Stripe, etc.)
3. **Normalize** → Convert to standard format
4. **Analyze** → AI enrichment (if enabled)
5. **Store** → Save to KV with retry logic
6. **Forward** → Send to MC96_ENDPOINT (if configured)
7. **Audit** → Log all steps for traceability

## 🛡️ Error Handling

- **Invalid JSON**: Returns 400 error
- **AI Unavailable**: Falls back to normalization only
- **KV Storage Failures**: Retries with exponential backoff
- **Forwarding Failures**: Logged but doesn't block response
- **Circuit Breaker Open**: Returns default analysis

## 📈 Metrics Tracked

- Request latency
- Success/error rates
- Platform distribution
- AI analysis success rate
- Circuit breaker states

## 🧪 Testing

```bash
npm test webhook-normalizer
npm test ai-analyzer
```

Tests cover:
- Platform detection
- Normalization for each platform
- AI response parsing
- Error handling
- Circuit breaker behavior

## 🚀 Deployment

```bash
# Setup Cloudflare config
node mc96-cli.mjs setup:cloudflare

# Deploy to staging
npm run deploy:staging

# Deploy to production
npm run deploy:prod
```

## 📝 Supported Platforms

| Platform | Detection Method | Normalized Fields |
|----------|-----------------|-------------------|
| Ko-fi | `verification_token` | type, user, message, amount, currency |
| Stripe | `stripe-signature` header | type, user, amount, currency, event_id |
| GitHub | `x-github-event` header | type, user, message, repository, event |
| YouTube | `x-goog-resource-id` header | type, user, message, video_id |
| Instagram | `object === 'instagram'` | type, user, message, post_id, media_url |
| SoundCloud | `track` or `user.username` | type, user, message, track |
| PayPal | `event_type.includes('PAYPAL')` | type, user, amount, currency |
| Patreon | `data.attributes.patron_status` | type, user, pledge_amount, status |
| TikTok | `event.includes('tiktok')` | type, user, message, video_id |

---

**Status**: ✅ **COMPLETE**  
**AI-Powered webhook processing is ready for production!** 🎉

