# NoizyLab Portal

AI-powered circuit board inspection system with real-time AR overlay and voice-guided repair.

## Architecture

```
portal/
├── api/                    # Cloudflare Worker API
│   ├── src/
│   │   ├── index.js        # Main API routes
│   │   ├── stripe.js       # Payment processing
│   │   ├── golden-reference.ts  # Reference image management
│   │   └── voice-guidance.ts    # ElevenLabs voice synthesis
│   └── wrangler.toml       # Worker configuration
├── frontend/               # React + Vite frontend
│   ├── src/
│   │   ├── components/
│   │   │   └── ARCamera.tsx    # Camera with AR overlay
│   │   ├── pages/
│   │   │   ├── Dashboard.tsx   # User dashboard
│   │   │   ├── Pricing.tsx     # Pricing tiers
│   │   │   ├── ScanResult.tsx  # Analysis results
│   │   │   └── Success.tsx     # Payment confirmation
│   │   └── App.tsx             # Main app component
│   └── package.json
├── landing/                # Static landing page
│   └── index.html
├── deploy.sh               # Deployment script
└── .env.example            # Environment variables template
```

## Quick Start

### 1. Install Dependencies

```bash
cd portal/frontend
npm install
```

### 2. Set Environment Variables

```bash
cp .env.example .env
# Edit .env with your API keys
```

### 3. Run Development Server

```bash
# Frontend (port 3000)
cd frontend && npm run dev

# API (port 8787)
cd api && wrangler dev
```

### 4. Deploy

```bash
chmod +x deploy.sh
./deploy.sh
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/scan` | POST | Submit PCB image for analysis |
| `/api/scan/:id` | GET | Get scan results |
| `/api/reference/:board` | GET | Get Golden Reference |
| `/api/reference` | POST | Upload new reference |
| `/api/report/:id` | GET | Generate PDF report |
| `/api/create-checkout-session` | POST | Start Stripe checkout |
| `/api/webhook` | POST | Stripe webhook handler |
| `/api/health` | GET | Health check |

## Pricing Tiers

| Tier | Price | Features |
|------|-------|----------|
| Golden Audit | $4.99/scan | Single scan, PDF report |
| Legacy Kit | $29/bundle | 10 scans, AR overlay, voice guidance |
| Pro | $99/month | Unlimited scans, API access, custom references |

## Tech Stack

- **Frontend**: React 18, Vite, Tailwind CSS, TypeScript
- **API**: Cloudflare Workers
- **Storage**: Cloudflare R2 (images), KV (metadata)
- **AI**: Gemini 3 Flash (vision), Claude 3.7 (reasoning)
- **Voice**: ElevenLabs TTS
- **Payments**: Stripe

## Environment Variables

See `.env.example` for required variables:

- `GEMINI_API_KEY` - Google AI API key
- `ANTHROPIC_API_KEY` - Anthropic API key
- `STRIPE_SECRET_KEY` - Stripe secret key
- `ELEVENLABS_API_KEY` - ElevenLabs API key

## License

Proprietary - NoizyLab 2026
