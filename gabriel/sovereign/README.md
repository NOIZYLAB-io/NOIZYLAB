# NOIZYLAB SOVEREIGN REPAIR PORTAL

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║              MONEY WHILE YOU SLEEP. FOCUS ON FLOW.                            ║
║                                                                               ║
║                           GORUNFREE.                                          ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

## Overview

The Sovereign Repair Portal is an AI-powered system for premium electronics repair documentation and automation. When you click **COMPLETE** on a repair, it automatically:

1. **Generates a Success Manifest PDF** - Premium forensic proof of the repair
2. **Captures Biometric Telemetry** - Stability, jitter compensation, session metrics
3. **Creates Forensic Comparisons** - Before/after visual evidence with AI analysis
4. **Sends Invoice via Stripe** - Automated billing
5. **Emails Customer** - With manifest attached and portal link
6. **Updates Customer Portal** - They can view/download their manifest

## Architecture

```
sovereign/
├── manifest_generator.py     # PDF Success Manifest generation
├── sovereign_dashboard.py    # Main control interface
├── vision/
│   └── forensic_capture.py   # Image capture and comparison
├── workers/
│   └── manifest-api/         # Cloudflare Worker for API
│       ├── src/index.ts
│       ├── wrangler.toml
│       └── package.json
├── GORUNFREE.sh              # Launch script
└── requirements.txt          # Python dependencies
```

## Quick Start

### 1. Install Dependencies

```bash
cd ~/NOIZYLAB/GABRIEL/sovereign
pip install -r requirements.txt
```

### 2. Run Demo

```bash
./GORUNFREE.sh --demo
```

This generates a sample manifest PDF in `manifests/`.

### 3. Full Startup

```bash
./GORUNFREE.sh
```

## Usage

### Python API

```python
from manifest_generator import complete_repair_session

# Called when clicking COMPLETE on dashboard
manifest_path = complete_repair_session(
    ticket_id="NZL-240101-A1B2",
    device_type="MacBook Pro",
    device_model="A2141 16-inch 2019",
    customer_name="John Doe",
    customer_email="john@example.com",
    diagnosis="No power, shorted PPBUS_G3H",
    root_cause="U8900 PMU thermal damage",
    components=["U8900", "C8901"],
    voltage_readings={"PPBUS_G3H": 12.58, "PP3V3_S5": 3.31}
)

print(f"Manifest: {manifest_path}")
```

### Dashboard Flow

```python
from sovereign_dashboard import SovereignDashboard

dashboard = SovereignDashboard()

# 1. Intake
ticket = dashboard.intake(
    customer_name="Customer",
    customer_email="customer@email.com",
    device_type="MacBook Pro",
    device_model="A2141"
)

# 2. Start diagnosis
dashboard.start_diagnosis(ticket)

# 3. Enter flow (repair mode)
dashboard.enter_flow(
    ticket,
    diagnosis="Shorted rail",
    root_cause="PMU failure",
    components=["U8900"]
)

# 4. Capture images
dashboard.capture_vision(ticket, "pre_image.jpg", is_pre=True)

# 5. Log telemetry during repair
dashboard.log_voltage(ticket, "PPBUS_G3H", 12.58)
dashboard.log_stability(ticket, 99.1)

# 6. Post-repair capture
dashboard.capture_vision(ticket, "post_image.jpg", is_pre=False)

# 7. COMPLETE - generates manifest, sends invoice, emails customer
manifest = dashboard.complete(ticket)
```

## API Endpoints

Deploy the Cloudflare Worker:

```bash
cd workers/manifest-api
npm install
wrangler deploy
```

### Endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | `/api/manifests` | Create new manifest |
| GET | `/api/manifests/:caseId` | Get manifest by ID |
| GET | `/api/manifests/:caseId/verify` | Verify authenticity |
| GET | `/api/manifests/:caseId/pdf` | Download PDF |
| POST | `/api/manifests/:caseId/images` | Upload forensic image |
| POST | `/api/billing/invoice` | Create Stripe invoice |
| GET | `/api/analytics/stats` | Get repair statistics |

## Environment Variables

```bash
# Gemini Vision API
export GEMINI_API_KEY="your-key"

# Stripe
export STRIPE_SECRET="sk_..."

# SendGrid
export SENDGRID_API_KEY="SG..."

# Cloudflare
export CF_ACCOUNT_ID="..."
export CF_API_TOKEN="..."
```

## Pricing Tiers

| Service | Price | Description |
|---------|-------|-------------|
| Standard Repair | $89 CAD | Base repair price |
| Sovereign Repair | $222.50 CAD | Premium with full manifest |
| Complex (4+ components) | +25% | Multiplier for complexity |

## Success Manifest Contents

The PDF includes:

1. **Header** - Case ID, device info, timestamps
2. **Status Banner** - RECOVERY COMPLETE / VERIFIED
3. **Forensic Comparison** - Before/after images with correction delta
4. **Biometric Stability Report** - Session telemetry
5. **Repair Specifications** - Diagnosis, components, technique
6. **Voltage Verification** - Measured rail voltages
7. **Cryptographic Proof** - Verification hash, signature
8. **Architect's Note** - AI-generated summary

## Customer Portal

Customers access their manifests at:

```
https://portal.noizylab.ca/manifests/{caseId}
```

Features:
- View full manifest details
- Download PDF
- Pay invoice
- Verify authenticity

---

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║                    THE MACHINE IS COMPLETE                                    ║
║                                                                               ║
║                    Your hardware has been restored                            ║
║                    to Sovereign Purity.                                       ║
║                                                                               ║
║                              GORUNFREE!                                       ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```
