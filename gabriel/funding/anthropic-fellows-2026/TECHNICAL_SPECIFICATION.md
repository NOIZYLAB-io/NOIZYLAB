# GABRIEL Technical Specification

## Generative Adversarial Board Inspection for Electronic Logic

**Version:** 1.0  
**Date:** January 2026  
**Classification:** Fellowship Application - Technical Appendix

---

## 1. System Overview

GABRIEL is a multimodal AI system for hardware integrity verification. It combines computer vision (Gemini 3 Flash) with reasoning (Claude 3.7) to detect:

- Counterfeit components
- Hardware tampering
- Manufacturing defects
- Supply chain anomalies

---

## 2. Architecture Diagram

```
                              ┌─────────────────────────────┐
                              │      USER INTERFACE         │
                              │  (React + Three.js Overlay) │
                              └──────────────┬──────────────┘
                                             │
                              ┌──────────────▼──────────────┐
                              │    CLOUDFLARE WORKERS AI    │
                              │     (Edge Orchestration)    │
                              └──────────────┬──────────────┘
                                             │
              ┌──────────────────────────────┼──────────────────────────────┐
              │                              │                              │
    ┌─────────▼─────────┐      ┌─────────────▼───────────┐    ┌────────────▼────────────┐
    │   VISION ENGINE   │      │    REASONING ENGINE     │    │    REFERENCE DATABASE   │
    │                   │      │                         │    │                         │
    │  Gemini 3 Flash   │      │  Claude 3.7 Extended    │    │  Cloudflare R2          │
    │  • Anomaly detect │      │  • Evidence synthesis   │    │  • Golden references    │
    │  • Pixel diff     │      │  • Tamper probability   │    │  • Component signatures │
    │  • Coordinate map │      │  • Repair guidance      │    │  • Historical data      │
    └───────────────────┘      └─────────────────────────┘    └─────────────────────────┘
```

---

## 3. Data Flow

### 3.1 Input Processing

```typescript
interface HardwareInspectionRequest {
  // Image data
  image: {
    data: Base64String;
    resolution: '12MP' | '48MP' | '108MP';
    type: 'visible' | 'thermal' | 'xray';
  };
  
  // Component identification
  target: {
    component_id?: string;      // e.g., "U8900"
    board_model?: string;       // e.g., "820-01041-A"
    manufacturer?: string;      // e.g., "Apple"
  };
  
  // Inspection parameters
  mode: 'quick_scan' | 'deep_analysis' | 'forensic';
  compare_to_reference: boolean;
}
```

### 3.2 Vision Analysis Output

```typescript
interface VisionAnalysisResult {
  anomalies: Array<{
    type: AnomalyType;
    confidence: number;          // 0.0 - 1.0
    coordinates: BoundingBox;    // [x1, y1, x2, y2]
    severity: 'critical' | 'high' | 'medium' | 'low';
    visual_evidence: string;     // Description
  }>;
  
  component_identification: {
    detected_marking: string;
    expected_marking: string;
    match_confidence: number;
  };
  
  pixel_diff_score: number;      // vs Golden Reference
  processing_time_ms: number;
}

type AnomalyType = 
  | 'die_marking_mismatch'
  | 'solder_reflow_evidence' 
  | 'corrosion_detected'
  | 'physical_damage'
  | 'component_missing'
  | 'component_replaced'
  | 'trace_damage'
  | 'counterfeit_indicators';
```

### 3.3 Reasoning Engine Output

```typescript
interface ReasoningResult {
  thinking_trace: string;        // Extended thinking output
  
  verdict: {
    tamper_probability: number;  // 0.0 - 1.0
    counterfeit_probability: number;
    damage_severity: number;
    recommendation: 'PASS' | 'SUSPECT' | 'REJECT';
  };
  
  evidence_chain: Array<{
    source: string;              // Image reference
    coordinates: BoundingBox;
    interpretation: string;
  }>;
  
  repair_guidance?: {
    issue: string;
    difficulty: 1 | 2 | 3 | 4 | 5;
    steps: string[];
    tools_required: string[];
    estimated_time: string;
  };
}
```

---

## 4. Component Detection Models

### 4.1 Supported Component Types

| Component Type | Detection Method | Reference DB Size |
|---------------|------------------|-------------------|
| CPU/SoC | Die marking + package | 50,000+ images |
| Power Management IC | Footprint + marking | 30,000+ images |
| Memory (RAM/NAND) | Stacking + labels | 40,000+ images |
| Capacitors | Size + markings | 100,000+ images |
| Resistors | SMD codes | 200,000+ images |
| Connectors | Pin patterns | 25,000+ images |

### 4.2 Golden Reference Database Schema

```sql
CREATE TABLE golden_references (
  id UUID PRIMARY KEY,
  component_type VARCHAR(50) NOT NULL,
  manufacturer VARCHAR(100),
  part_number VARCHAR(100) NOT NULL,
  
  -- Image data
  image_url TEXT NOT NULL,
  image_resolution VARCHAR(20),
  capture_conditions JSONB,  -- lighting, angle, equipment
  
  -- Fingerprint data
  visual_fingerprint VECTOR(512),  -- Embedding
  expected_markings TEXT[],
  package_type VARCHAR(50),
  
  -- Metadata
  verified_authentic BOOLEAN DEFAULT true,
  verification_method TEXT,
  created_at TIMESTAMP DEFAULT NOW(),
  
  -- Indexing
  CONSTRAINT unique_part UNIQUE (manufacturer, part_number)
);

CREATE INDEX idx_fingerprint ON golden_references 
  USING ivfflat (visual_fingerprint vector_cosine_ops);
```

---

## 5. API Endpoints

### 5.1 Quick Scan (Consumer-Facing)

```
POST /api/v1/scan/quick
Content-Type: multipart/form-data

Request:
  - image: File (JPEG/PNG, max 50MB)
  - component_hint: string (optional)

Response: {
  "scan_id": "uuid",
  "status": "PASS" | "SUSPECT" | "REJECT",
  "confidence": 0.94,
  "anomalies_found": 2,
  "processing_time_ms": 2340,
  "upgrade_to_deep": boolean
}

Rate Limit: 10/hour (free), 1000/hour (pro)
```

### 5.2 Deep Analysis (Professional)

```
POST /api/v1/scan/deep
Authorization: Bearer <api_key>
Content-Type: multipart/form-data

Request:
  - image: File (RAW/TIFF/PNG, max 200MB)
  - board_model: string
  - compare_reference: boolean
  - include_repair_guidance: boolean

Response: {
  "analysis_id": "uuid",
  "vision_results": VisionAnalysisResult,
  "reasoning_results": ReasoningResult,
  "reference_comparison": {
    "reference_id": "uuid",
    "similarity_score": 0.87,
    "diff_overlay_url": "https://..."
  },
  "report_pdf_url": "https://...",
  "raw_data_url": "https://..."
}

Rate Limit: 100/hour (pro), unlimited (enterprise)
```

### 5.3 Batch Processing (Enterprise)

```
POST /api/v1/scan/batch
Authorization: Bearer <api_key>

Request: {
  "images": ["s3://bucket/image1.png", ...],
  "callback_url": "https://your-server.com/webhook",
  "priority": "standard" | "high",
  "options": { ... }
}

Response: {
  "batch_id": "uuid",
  "estimated_completion": "2026-01-02T18:30:00Z",
  "webhook_configured": true
}
```

---

## 6. Cloudflare Worker Implementation

```javascript
// workers/gabriel-vision/src/index.js
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    
    if (url.pathname === '/api/v1/scan/quick') {
      return handleQuickScan(request, env);
    }
    
    if (url.pathname === '/api/v1/scan/deep') {
      return handleDeepScan(request, env);
    }
    
    return new Response('GABRIEL API v1.0', { status: 200 });
  }
};

async function handleQuickScan(request, env) {
  const formData = await request.formData();
  const image = formData.get('image');
  
  // 1. Upload to R2 for processing
  const imageId = crypto.randomUUID();
  await env.R2_BUCKET.put(`scans/${imageId}`, image.stream());
  
  // 2. Call Gemini for vision analysis
  const visionResult = await analyzeWithGemini(
    env.R2_BUCKET.get(`scans/${imageId}`),
    env.GEMINI_API_KEY
  );
  
  // 3. If anomalies found, get Claude reasoning
  let reasoning = null;
  if (visionResult.anomalies.length > 0) {
    reasoning = await reasonWithClaude(
      visionResult,
      env.ANTHROPIC_API_KEY
    );
  }
  
  // 4. Return result
  return Response.json({
    scan_id: imageId,
    status: reasoning?.verdict.recommendation || 'PASS',
    confidence: reasoning?.verdict.tamper_probability || 0.05,
    anomalies_found: visionResult.anomalies.length,
    processing_time_ms: Date.now() - startTime
  });
}

async function analyzeWithGemini(imageStream, apiKey) {
  const response = await fetch('https://generativelanguage.googleapis.com/v1/models/gemini-3-flash:generateContent', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${apiKey}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      contents: [{
        parts: [
          { text: VISION_PROMPT },
          { inline_data: { mime_type: 'image/png', data: await streamToBase64(imageStream) }}
        ]
      }],
      generationConfig: {
        response_mime_type: 'application/json'
      }
    })
  });
  
  return response.json();
}

async function reasonWithClaude(visionResult, apiKey) {
  const response = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'x-api-key': apiKey,
      'anthropic-version': '2024-01-01',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      model: 'claude-3-7-sonnet-20260101',
      max_tokens: 16000,
      thinking: {
        type: 'enabled',
        budget_tokens: 10000
      },
      messages: [{
        role: 'user',
        content: `Analyze these hardware inspection findings and determine tamper probability:\n\n${JSON.stringify(visionResult, null, 2)}`
      }]
    })
  });
  
  return response.json();
}

const VISION_PROMPT = `You are a hardware inspection AI. Analyze this image for:
1. Component authenticity (die markings, package integrity)
2. Signs of rework (flux residue, solder reflow patterns)
3. Physical damage (corrosion, burns, cracks)
4. Missing or replaced components

Return JSON with coordinates of any anomalies found.`;
```

---

## 7. Frontend Overlay System

```jsx
// components/AnomalyOverlay.jsx
import { useEffect, useRef } from 'react';

export function AnomalyOverlay({ imageUrl, anomalies, selectedAnomaly }) {
  const canvasRef = useRef(null);
  
  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    const img = new Image();
    
    img.onload = () => {
      // Draw base image
      canvas.width = img.width;
      canvas.height = img.height;
      ctx.drawImage(img, 0, 0);
      
      // Draw anomaly boxes
      anomalies.forEach((anomaly, idx) => {
        const [x1, y1, x2, y2] = anomaly.coordinates;
        const isSelected = idx === selectedAnomaly;
        
        // Hot Rod Orange for critical, yellow for medium
        ctx.strokeStyle = anomaly.severity === 'critical' 
          ? '#FF6B00' 
          : '#FFD700';
        ctx.lineWidth = isSelected ? 4 : 2;
        ctx.setLineDash(isSelected ? [] : [5, 5]);
        
        ctx.strokeRect(x1, y1, x2 - x1, y2 - y1);
        
        // Label
        ctx.fillStyle = ctx.strokeStyle;
        ctx.font = '14px monospace';
        ctx.fillText(
          `${anomaly.type} (${(anomaly.confidence * 100).toFixed(0)}%)`,
          x1, y1 - 5
        );
      });
    };
    
    img.src = imageUrl;
  }, [imageUrl, anomalies, selectedAnomaly]);
  
  return (
    <canvas 
      ref={canvasRef}
      className="max-w-full h-auto cursor-crosshair"
      onClick={(e) => handleAnomalyClick(e, anomalies)}
    />
  );
}
```

---

## 8. Voice Guidance Integration

```javascript
// ElevenLabs Professional Voice Clone Integration
async function generateRepairGuidance(analysis, env) {
  const script = buildRepairScript(analysis);
  
  const response = await fetch(
    `https://api.elevenlabs.io/v1/text-to-speech/${env.VOICE_ID}`,
    {
      method: 'POST',
      headers: {
        'xi-api-key': env.ELEVENLABS_API_KEY,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        text: script,
        model_id: 'eleven_turbo_v2_5',
        voice_settings: {
          stability: 0.7,
          similarity_boost: 0.9,
          style: 0.5,  // Professional but warm
          use_speaker_boost: true
        }
      })
    }
  );
  
  const audioBuffer = await response.arrayBuffer();
  const audioId = crypto.randomUUID();
  await env.R2_BUCKET.put(`audio/${audioId}.mp3`, audioBuffer);
  
  return `https://cdn.noizylab.ai/audio/${audioId}.mp3`;
}

function buildRepairScript(analysis) {
  const { anomalies, repair_guidance } = analysis;
  
  let script = `I've completed the analysis. `;
  
  if (anomalies.length === 0) {
    script += `Good news—this board looks clean. No anomalies detected.`;
  } else {
    script += `I found ${anomalies.length} areas that need attention. `;
    
    anomalies.forEach((anomaly, idx) => {
      script += `Issue ${idx + 1}: ${anomaly.visual_evidence}. `;
    });
    
    if (repair_guidance) {
      script += `Here's what I recommend: ${repair_guidance.steps.join('. ')}`;
    }
  }
  
  return script;
}
```

---

## 9. Performance Targets

| Metric | Quick Scan | Deep Analysis |
|--------|------------|---------------|
| Latency (p50) | < 2 seconds | < 15 seconds |
| Latency (p99) | < 5 seconds | < 45 seconds |
| Accuracy | 85% | 95% |
| False Positive Rate | < 10% | < 3% |
| Throughput | 1000 req/min | 100 req/min |

---

## 10. Cost Model

| Operation | Provider | Cost per Request |
|-----------|----------|------------------|
| Vision Analysis | Gemini 3 Flash | $0.0005 |
| Reasoning (Simple) | Claude 3.7 | $0.008 |
| Reasoning (Extended) | Claude 3.7 | $0.04 |
| Voice Generation | ElevenLabs | $0.003 |
| Storage (R2) | Cloudflare | $0.015/GB/month |
| **Total (Quick Scan)** | | **~$0.001** |
| **Total (Deep + Voice)** | | **~$0.05** |

**Revenue Model:**
- Quick Scan: $4.99 (margin: $4.98)
- Deep Analysis: $19.99 (margin: $19.94)
- Enterprise: $499/month unlimited

---

## 11. Security Considerations

- All images encrypted at rest (AES-256)
- API keys rotated monthly
- Audit logs retained 90 days
- GDPR compliance: User can request deletion
- No images shared with third parties
- Model outputs never used for training without consent

---

## 12. Roadmap

| Phase | Timeline | Deliverable |
|-------|----------|-------------|
| MVP | Month 1-2 | Quick Scan API + Basic UI |
| Pro | Month 3-4 | Deep Analysis + Voice |
| Enterprise | Month 5-6 | Batch Processing + Custom Models |
| Research | Month 4-6 | Fellowship deliverables + Paper |

---

*Document prepared for Anthropic Fellows Program 2026*
