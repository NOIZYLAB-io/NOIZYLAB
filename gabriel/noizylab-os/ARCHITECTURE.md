# 🏗️ NoizyLab OS - System Architecture

## 🌐 Overview

NoizyLab OS is a distributed, AI-powered hardware restoration platform built entirely on Cloudflare's edge infrastructure. The system consists of 17 specialized Cloudflare Workers that communicate via service bindings, providing near-zero latency inter-service communication.

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                                   INTERNET                                          │
└─────────────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                              🌍 CLOUDFLARE EDGE                                     │
│                                                                                     │
│   ┌─────────────────────────────────────────────────────────────────────────────┐   │
│   │                        🚪 API GATEWAY WORKER                                │   │
│   │  • Authentication (JWT + API Keys)                                          │   │
│   │  • Rate Limiting (Per-key/per-user)                                        │   │
│   │  • Request Routing                                                          │   │
│   │  • Response Aggregation                                                     │   │
│   └─────────────────────────────────────────────────────────────────────────────┘   │
│                                       │                                             │
│         ┌─────────────────────────────┼─────────────────────────────┐              │
│         │                             │                             │              │
│         ▼                             ▼                             ▼              │
│   ┌───────────┐               ┌───────────────┐             ┌───────────────┐      │
│   │  MAIN     │               │   WORKFLOW    │             │   CUSTOMER    │      │
│   │  WORKER   │◄─────────────►│ ORCHESTRATOR  │◄───────────►│    PORTAL     │      │
│   └─────┬─────┘               └───────┬───────┘             └───────────────┘      │
│         │                             │                                             │
│         │    ┌────────────────────────┼────────────────────────┐                   │
│         │    │                        │                        │                   │
│         ▼    ▼                        ▼                        ▼                   │
│   ┌──────────────────────────────────────────────────────────────────────────┐     │
│   │                        🤖 AI SERVICES TIER                               │     │
│   │                                                                          │     │
│   │  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌──────────────────────┐  │     │
│   │  │   BRAIN   │  │  VISION   │  │   VOICE   │  │   SCHEMATIC          │  │     │
│   │  │  Claude   │  │  PCB AI   │  │  Eleven   │  │    ANALYZER          │  │     │
│   │  │  Opus 4   │  │  Analysis │  │   Labs    │  │   Circuit Trace      │  │     │
│   │  └───────────┘  └───────────┘  └───────────┘  └──────────────────────┘  │     │
│   │                                                                          │     │
│   │  ┌───────────┐  ┌───────────┐                                           │     │
│   │  │    AR     │  │   CHAT    │                                           │     │
│   │  │   GUIDE   │  │   AGENT   │                                           │     │
│   │  │   3D AR   │  │  WebSocket│                                           │     │
│   │  └───────────┘  └───────────┘                                           │     │
│   └──────────────────────────────────────────────────────────────────────────┘     │
│                                       │                                             │
│         ┌─────────────────────────────┼─────────────────────────────┐              │
│         │                             │                             │              │
│         ▼                             ▼                             ▼              │
│   ┌──────────────────────────────────────────────────────────────────────────┐     │
│   │                     💼 BUSINESS SERVICES TIER                            │     │
│   │                                                                          │     │
│   │  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌──────────────────────┐  │     │
│   │  │  PRICING  │  │ INVENTORY │  │   EBAY    │  │     ANALYTICS        │  │     │
│   │  │  Engine   │  │  Manager  │  │  SNIPER   │  │    Dashboard         │  │     │
│   │  │  Quotes   │  │  ML Pred  │  │  Deals    │  │    BI Engine         │  │     │
│   │  └───────────┘  └───────────┘  └───────────┘  └──────────────────────┘  │     │
│   │                                                                          │     │
│   │  ┌───────────┐  ┌───────────┐  ┌───────────┐                            │     │
│   │  │    QC     │  │  TRAINING │  │NOTIFICATIONS│                           │     │
│   │  │ INSPECTOR │  │ SIMULATOR │  │    HUB    │                            │     │
│   │  │  Quality  │  │  Gamified │  │ Multi-Chan│                            │     │
│   │  └───────────┘  └───────────┘  └───────────┘                            │     │
│   └──────────────────────────────────────────────────────────────────────────┘     │
│                                       │                                             │
│         ┌─────────────────────────────┼─────────────────────────────┐              │
│         │                             │                             │              │
│         ▼                             ▼                             ▼              │
│   ┌──────────────────────────────────────────────────────────────────────────┐     │
│   │                    📦 DATA SERVICES TIER                                 │     │
│   │                                                                          │     │
│   │  ┌────────────────┐  ┌────────────────┐  ┌────────────────────────────┐ │     │
│   │  │   D1 DATABASE  │  │  R2 STORAGE    │  │      KV NAMESPACE          │ │     │
│   │  │  • Tickets     │  │  • Images      │  │  • Sessions                │ │     │
│   │  │  • Customers   │  │  • Schematics  │  │  • Cache                   │ │     │
│   │  │  • Inventory   │  │  • Audio       │  │  • Rate Limits             │ │     │
│   │  │  • Analytics   │  │  • Documents   │  │  • API Keys                │ │     │
│   │  └────────────────┘  └────────────────┘  └────────────────────────────┘ │     │
│   │                                                                          │     │
│   │  ┌────────────────┐  ┌────────────────┐                                 │     │
│   │  │    QUEUES      │  │ DURABLE OBJECTS│                                 │     │
│   │  │  • Jobs        │  │  • WebSocket   │                                 │     │
│   │  │  • Workflows   │  │  • State       │                                 │     │
│   │  │  • Events      │  │  • Counters    │                                 │     │
│   │  └────────────────┘  └────────────────┘                                 │     │
│   └──────────────────────────────────────────────────────────────────────────┘     │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🔧 Worker Catalog

### 1. API Gateway (`noizylab-api-gateway`)
**Purpose:** Unified entry point for all API requests
- JWT and API Key authentication
- Per-key rate limiting with sliding windows
- Request routing to appropriate services
- Response aggregation and caching
- Webhook ingestion

### 2. Main Worker (`noizylab-main`)
**Purpose:** Core ticket and workspace management
- Ticket CRUD operations
- Workspace management
- User authentication
- Real-time updates

### 3. Brain AI (`noizylab-brain`)
**Purpose:** AI-powered diagnostic engine
- Claude 3.5 Opus integration
- Extended thinking for complex problems
- Diagnostic report generation
- Repair plan recommendations

### 4. Vision AI (`noizylab-vision`)
**Purpose:** Computer vision for PCB analysis
- Golden reference comparison
- Defect detection
- Component identification
- Board condition assessment

### 5. Voice AI (`noizylab-voice`)
**Purpose:** Text-to-speech synthesis
- ElevenLabs integration
- Multiple voice profiles
- Real-time streaming
- Audio caching

### 6. Pricing Engine (`noizylab-pricing`)
**Purpose:** Smart quote generation
- Competitor price analysis
- Dynamic pricing algorithms
- Quote templates
- Margin optimization

### 7. Inventory Manager (`noizylab-inventory`)
**Purpose:** Parts tracking and prediction
- Barcode/QR scanning
- ML reorder predictions
- Parts compatibility mapping
- Supplier management

### 8. eBay Sniper (`noizylab-ebay-sniper`)
**Purpose:** Parts deal hunting
- Real-time listing monitoring
- Profit margin analysis
- Auto-bid capabilities
- Price alerts

### 9. Analytics Dashboard (`noizylab-analytics`)
**Purpose:** Business intelligence
- Real-time KPIs
- Technician performance
- Revenue analysis
- Trend forecasting

### 10. AR Guide (`noizylab-ar-guide`)
**Purpose:** Augmented reality repair guides
- 3D model overlays
- Step-by-step instructions
- Live annotation sharing
- Progress tracking

### 11. Training Simulator (`noizylab-training`)
**Purpose:** Gamified technician training
- Interactive simulations
- XP and leveling system
- Certifications
- Leaderboards

### 12. Chat Agent (`noizylab-chat-agent`)
**Purpose:** Real-time AI assistant
- WebSocket connections
- Context-aware responses
- Human escalation
- Typing indicators

### 13. Notifications Hub (`noizylab-notifications`)
**Purpose:** Multi-channel notifications
- Email (Mailgun/SendGrid)
- SMS (Twilio)
- Push (VAPID)
- Slack/Discord webhooks
- In-app notifications

### 14. QC Inspector (`noizylab-qc-inspector`)
**Purpose:** Automated quality control
- Checkpoint-based inspections
- AI defect detection
- Pass/fail determination
- Report generation

### 15. Customer Portal (`noizylab-customer-portal`)
**Purpose:** Customer self-service
- Account management
- Ticket tracking
- Quote approval
- Payment processing
- Loyalty program

### 16. Schematic Analyzer (`noizylab-schematic-analyzer`)
**Purpose:** Circuit analysis and fault diagnosis
- Component lookup
- Net tracing
- Power rail analysis
- Common fault patterns

### 17. Workflow Orchestrator (`noizylab-workflow-orchestrator`)
**Purpose:** Automation engine
- Visual workflow builder
- Event-driven triggers
- Conditional branching
- Human task integration

---

## 📊 Data Flow Examples

### Repair Intake Flow
```
Customer submits repair request
         │
         ▼
┌─────────────────┐
│  Customer Portal │
│  (Create ticket) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐    ┌─────────────────┐
│    Workflow     │───►│    Vision AI    │
│  Orchestrator   │    │  (Analyze PCB)  │
└────────┬────────┘    └────────┬────────┘
         │                      │
         ▼                      ▼
┌─────────────────┐    ┌─────────────────┐
│    Brain AI     │◄───│  (Image data)   │
│   (Diagnose)    │    └─────────────────┘
└────────┬────────┘
         │
         ▼
┌─────────────────┐    ┌─────────────────┐
│  Pricing Engine │───►│    Inventory    │
│ (Generate Quote)│    │ (Check parts)   │
└────────┬────────┘    └─────────────────┘
         │
         ▼
┌─────────────────┐
│  Notifications  │
│ (Send to cust.) │
└─────────────────┘
```

### Parts Sourcing Flow
```
Low inventory detected
         │
         ▼
┌─────────────────┐
│    Inventory    │
│  (Trigger hunt) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐    ┌─────────────────┐
│   eBay Sniper   │───►│    Brain AI     │
│ (Search deals)  │    │ (Analyze deals) │
└────────┬────────┘    └────────┬────────┘
         │                      │
         ▼                      ▼
┌─────────────────┐    ┌─────────────────┐
│    Workflow     │◄───│  (Recommend)    │
│  (Approval req) │    └─────────────────┘
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Human approval  │
│  (Manager)      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   eBay Sniper   │
│  (Purchase)     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    Inventory    │
│ (Update stock)  │
└─────────────────┘
```

---

## 🔐 Security Architecture

### Authentication Layers
1. **API Gateway Level**
   - JWT validation
   - API Key verification
   - Rate limiting

2. **Service Level**
   - Service binding authentication (internal only)
   - Request signature verification

3. **Data Level**
   - D1 encryption at rest
   - R2 access controls
   - KV TTL enforcement

### Authorization Model
```typescript
interface Scopes {
  // Ticket operations
  'tickets:read': boolean;
  'tickets:write': boolean;
  'tickets:delete': boolean;
  
  // AI services
  'ai:diagnose': boolean;
  'ai:vision': boolean;
  'ai:voice': boolean;
  
  // Business operations
  'pricing:read': boolean;
  'pricing:write': boolean;
  'inventory:read': boolean;
  'inventory:write': boolean;
  
  // Admin
  'admin': boolean;
  'workflows:manage': boolean;
}
```

---

## 📈 Scaling Considerations

### Auto-scaling
- All workers auto-scale to 0 when idle
- Burst capacity handled by Cloudflare edge
- No cold starts with Workers (< 50ms)

### Performance Targets
| Metric | Target | Strategy |
|--------|--------|----------|
| P99 Latency | < 200ms | Edge caching, KV |
| Cold Start | < 50ms | Workers runtime |
| AI Diagnosis | < 10s | Parallel processing |
| WebSocket Connect | < 100ms | Durable Objects |

### Cost Optimization
- KV caching for frequently accessed data
- R2 for large file storage (cheaper than S3)
- Queues for async processing
- Service bindings (no network cost)

---

## 🚀 Deployment

### Prerequisites
```bash
# Install Wrangler
npm install -g wrangler

# Authenticate
wrangler login

# Create resources
wrangler d1 create noizylab-db
wrangler r2 bucket create noizylab-uploads
wrangler kv:namespace create NOIZYLAB_KV
```

### Deploy All Workers
```bash
./deploy.sh deploy
```

### Deploy Individual Worker
```bash
cd workers/brain
npm install
wrangler deploy
```

---

## 📁 Repository Structure

```
noizylab-os/
├── src/
│   └── worker.ts              # Main worker
├── workers/
│   ├── api-gateway/           # API Gateway
│   ├── brain/                 # Claude AI
│   ├── vision/                # PCB Vision
│   ├── voice/                 # ElevenLabs TTS
│   ├── pricing/               # Quote generation
│   ├── inventory/             # Parts management
│   ├── analytics/             # Business intelligence
│   ├── notifications/         # Multi-channel notifications
│   ├── qc-inspector/          # Quality control
│   ├── customer-portal/       # Customer self-service
│   ├── schematic-analyzer/    # Circuit analysis
│   ├── ar-guide/              # AR repair guides
│   ├── training/              # Gamified training
│   ├── ebay-sniper/           # Parts hunting
│   ├── chat-agent/            # Real-time chat
│   └── workflow-orchestrator/ # Automation engine
├── migrations/
│   └── schema.sql             # D1 database schema
├── tools/
│   └── tts-hotrod/            # Python TTS client
├── deploy.sh                  # Master deployment
├── wrangler.toml              # Main config
├── package.json
├── tsconfig.json
└── README.md
```

---

## 🔮 Future Enhancements

1. **Mobile Apps** - React Native clients for technicians
2. **IoT Integration** - Smart workbench sensors
3. **Blockchain** - Repair history verification
4. **ML Models** - Custom Workers AI fine-tuning
5. **Multi-region** - Geographic redundancy
6. **Video Analysis** - Real-time repair video processing

---

<p align="center">
  <strong>NoizyLab OS</strong> - The Future of Hardware Restoration 🔧⚡
</p>
