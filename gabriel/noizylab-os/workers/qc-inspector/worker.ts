/**
 * ██████╗  ██████╗    ██╗███╗   ██╗███████╗██████╗ ███████╗ ██████╗████████╗ ██████╗ ██████╗ 
 * ██╔═══██╗██╔════╝    ██║████╗  ██║██╔════╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗
 * ██║   ██║██║         ██║██╔██╗ ██║███████╗██████╔╝█████╗  ██║        ██║   ██║   ██║██████╔╝
 * ██║▄▄ ██║██║         ██║██║╚██╗██║╚════██║██╔═══╝ ██╔══╝  ██║        ██║   ██║   ██║██╔══██╗
 * ╚██████╔╝╚██████╗    ██║██║ ╚████║███████║██║     ███████╗╚██████╗   ██║   ╚██████╔╝██║  ██║
 *  ╚══▀▀═╝  ╚═════╝    ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝     ╚══════╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
 * 
 * NoizyLab OS - AI Quality Control Inspector Worker
 * Automated quality assurance with multi-point inspection and defect detection
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

// ═══════════════════════════════════════════════════════════════════════════
// TYPES & INTERFACES
// ═══════════════════════════════════════════════════════════════════════════

interface Env {
  NOIZYLAB_KV: KVNamespace;
  NOIZYLAB_DB: D1Database;
  NOIZYLAB_UPLOADS: R2Bucket;
  NOIZYLAB_QUEUE: Queue;
  AI: Ai;
  ANTHROPIC_API_KEY: string;
}

interface QCCheckpoint {
  id: string;
  name: string;
  category: 'visual' | 'functional' | 'electrical' | 'mechanical' | 'software';
  checkType: 'automated' | 'manual' | 'hybrid';
  criteria: QCCriteria[];
  weight: number;
  required: boolean;
}

interface QCCriteria {
  id: string;
  description: string;
  measurement?: {
    type: 'numeric' | 'boolean' | 'categorical';
    unit?: string;
    min?: number;
    max?: number;
    tolerance?: number;
    acceptedValues?: string[];
  };
  aiPrompt?: string;
}

interface InspectionResult {
  id: string;
  ticketId: string;
  repairId: string;
  technicianId: string;
  inspectorId?: string;
  status: 'pending' | 'in_progress' | 'passed' | 'failed' | 'conditional';
  startedAt: string;
  completedAt?: string;
  checkpoints: CheckpointResult[];
  overallScore: number;
  findings: Finding[];
  recommendation: 'ship' | 'rework' | 'scrap' | 'escalate';
  aiAnalysis: AIQCAnalysis;
  signoff?: Signoff;
}

interface CheckpointResult {
  checkpointId: string;
  status: 'passed' | 'failed' | 'skipped' | 'warning';
  score: number;
  criteriaResults: CriteriaResult[];
  images?: string[];
  notes?: string;
  measuredValues?: Record<string, any>;
  automatedChecks?: AutomatedCheck[];
}

interface CriteriaResult {
  criteriaId: string;
  passed: boolean;
  value?: any;
  deviation?: number;
  notes?: string;
}

interface AutomatedCheck {
  name: string;
  passed: boolean;
  confidence: number;
  details: string;
  imageRegions?: ImageRegion[];
}

interface ImageRegion {
  x: number;
  y: number;
  width: number;
  height: number;
  label: string;
  severity: 'info' | 'warning' | 'critical';
}

interface Finding {
  id: string;
  type: 'defect' | 'observation' | 'improvement' | 'commendation';
  severity: 'critical' | 'major' | 'minor' | 'info';
  description: string;
  location?: string;
  checkpoint?: string;
  images?: string[];
  suggestedAction?: string;
  resolved?: boolean;
}

interface AIQCAnalysis {
  confidenceScore: number;
  defectsDetected: DetectedDefect[];
  qualityPrediction: {
    reliabilityScore: number;
    estimatedLifespan: string;
    riskFactors: string[];
  };
  comparisonToBaseline: {
    deviation: number;
    areas: string[];
  };
  recommendations: string[];
  anomalies: Anomaly[];
}

interface DetectedDefect {
  type: string;
  location: string;
  confidence: number;
  severity: 'critical' | 'major' | 'minor';
  possibleCause: string;
  suggestedFix: string;
  imageAnnotations?: ImageRegion[];
}

interface Anomaly {
  type: string;
  description: string;
  significance: number;
  historicalComparison?: string;
}

interface Signoff {
  signedBy: string;
  signedAt: string;
  role: 'technician' | 'supervisor' | 'qa_manager';
  digitalSignature: string;
  notes?: string;
}

interface QCTemplate {
  id: string;
  name: string;
  deviceCategory: string;
  deviceModel?: string;
  repairType?: string;
  checkpoints: QCCheckpoint[];
  passingScore: number;
  requiresSupervisorSignoff: boolean;
  version: string;
  createdAt: string;
  updatedAt: string;
}

// ═══════════════════════════════════════════════════════════════════════════
// AI QC ENGINE
// ═══════════════════════════════════════════════════════════════════════════

class AIQualityInspector {
  private env: Env;

  constructor(env: Env) {
    this.env = env;
  }

  async analyzeImages(images: string[], deviceInfo: any, checkpoints: QCCheckpoint[]): Promise<Partial<AIQCAnalysis>> {
    const analysisPrompt = `You are an expert Quality Control inspector for electronics repair.

Device: ${deviceInfo.make} ${deviceInfo.model}
Repair Type: ${deviceInfo.repairType}

Analyze the following inspection images and provide a detailed QC assessment.

Checkpoints to verify:
${checkpoints.map(c => `- ${c.name}: ${c.criteria.map(cr => cr.description).join(', ')}`).join('\n')}

Provide your analysis in JSON format:
{
  "confidenceScore": 0.0-1.0,
  "defectsDetected": [
    {
      "type": "defect type",
      "location": "specific location on device",
      "confidence": 0.0-1.0,
      "severity": "critical|major|minor",
      "possibleCause": "likely cause",
      "suggestedFix": "recommended action"
    }
  ],
  "qualityPrediction": {
    "reliabilityScore": 0.0-1.0,
    "estimatedLifespan": "human readable estimate",
    "riskFactors": ["list of risks"]
  },
  "recommendations": ["list of recommendations"],
  "anomalies": [
    {
      "type": "anomaly type",
      "description": "details",
      "significance": 0.0-1.0
    }
  ]
}`;

    try {
      const imageContents = await Promise.all(
        images.map(async (img) => {
          const imageData = await this.env.NOIZYLAB_UPLOADS.get(img);
          if (!imageData) return null;
          const buffer = await imageData.arrayBuffer();
          return {
            type: 'image',
            source: {
              type: 'base64',
              media_type: 'image/jpeg',
              data: btoa(String.fromCharCode(...new Uint8Array(buffer)))
            }
          };
        })
      );

      const validImages = imageContents.filter(Boolean);

      const response = await fetch('https://api.anthropic.com/v1/messages', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'x-api-key': this.env.ANTHROPIC_API_KEY,
          'anthropic-version': '2023-06-01'
        },
        body: JSON.stringify({
          model: 'claude-sonnet-4-20250514',
          max_tokens: 4096,
          messages: [
            {
              role: 'user',
              content: [
                ...validImages,
                { type: 'text', text: analysisPrompt }
              ]
            }
          ]
        })
      });

      if (!response.ok) {
        throw new Error(`Claude API error: ${response.status}`);
      }

      const data = await response.json() as any;
      const content = data.content[0].text;
      
      const jsonMatch = content.match(/\{[\s\S]*\}/);
      if (jsonMatch) {
        return JSON.parse(jsonMatch[0]);
      }

      return {
        confidenceScore: 0.5,
        defectsDetected: [],
        recommendations: ['Manual inspection recommended']
      };

    } catch (error) {
      console.error('AI QC analysis failed:', error);
      return {
        confidenceScore: 0,
        defectsDetected: [],
        recommendations: ['AI analysis failed - manual inspection required']
      };
    }
  }

  async runAutomatedChecks(
    checkpoint: QCCheckpoint,
    images: string[],
    measurements: Record<string, any>
  ): Promise<AutomatedCheck[]> {
    const checks: AutomatedCheck[] = [];

    // Visual checks via AI
    if (checkpoint.category === 'visual' && images.length > 0) {
      const visualCheck = await this.runVisualCheck(checkpoint, images);
      checks.push(visualCheck);
    }

    // Measurement validation
    if (checkpoint.category === 'electrical') {
      for (const criteria of checkpoint.criteria) {
        if (criteria.measurement && measurements[criteria.id]) {
          const check = this.validateMeasurement(criteria, measurements[criteria.id]);
          checks.push(check);
        }
      }
    }

    // Software/functional checks
    if (checkpoint.category === 'functional') {
      const functionalCheck = await this.runFunctionalCheck(checkpoint, measurements);
      checks.push(functionalCheck);
    }

    return checks;
  }

  private async runVisualCheck(checkpoint: QCCheckpoint, images: string[]): Promise<AutomatedCheck> {
    try {
      const criteria = checkpoint.criteria.map(c => c.description).join('; ');
      
      // Use Workers AI for quick visual classification
      const imageData = await this.env.NOIZYLAB_UPLOADS.get(images[0]);
      if (!imageData) {
        return {
          name: `Visual Check: ${checkpoint.name}`,
          passed: false,
          confidence: 0,
          details: 'Image not found'
        };
      }

      const buffer = await imageData.arrayBuffer();
      const result = await this.env.AI.run('@cf/llava-hf/llava-1.5-7b-hf', {
        image: [...new Uint8Array(buffer)],
        prompt: `Inspect this repair image for: ${criteria}. Does it pass quality inspection? Answer with PASS or FAIL and briefly explain.`,
        max_tokens: 256
      });

      const response = result.description || '';
      const passed = response.toUpperCase().includes('PASS');

      return {
        name: `Visual Check: ${checkpoint.name}`,
        passed,
        confidence: passed ? 0.85 : 0.75,
        details: response
      };

    } catch (error) {
      return {
        name: `Visual Check: ${checkpoint.name}`,
        passed: false,
        confidence: 0,
        details: `Check failed: ${error}`
      };
    }
  }

  private validateMeasurement(criteria: QCCriteria, value: any): AutomatedCheck {
    const { measurement } = criteria;
    if (!measurement) {
      return { name: criteria.id, passed: true, confidence: 1, details: 'No measurement required' };
    }

    let passed = false;
    let deviation = 0;

    if (measurement.type === 'numeric') {
      const numValue = parseFloat(value);
      const target = (measurement.min! + measurement.max!) / 2;
      deviation = Math.abs(numValue - target);
      const tolerance = measurement.tolerance || ((measurement.max! - measurement.min!) / 2);
      passed = numValue >= measurement.min! && numValue <= measurement.max!;
    } else if (measurement.type === 'boolean') {
      passed = value === true || value === 'true' || value === 'PASS';
    } else if (measurement.type === 'categorical') {
      passed = measurement.acceptedValues?.includes(value) || false;
    }

    return {
      name: criteria.description,
      passed,
      confidence: 1.0,
      details: `Measured: ${value}${measurement.unit || ''} | Expected: ${measurement.min}-${measurement.max}${measurement.unit || ''} | Deviation: ${deviation.toFixed(3)}`
    };
  }

  private async runFunctionalCheck(checkpoint: QCCheckpoint, testResults: Record<string, any>): Promise<AutomatedCheck> {
    const allPassed = checkpoint.criteria.every(c => {
      if (c.id in testResults) {
        return testResults[c.id] === true || testResults[c.id] === 'PASS';
      }
      return false;
    });

    return {
      name: `Functional Test: ${checkpoint.name}`,
      passed: allPassed,
      confidence: 1.0,
      details: `${checkpoint.criteria.length} criteria tested, ${allPassed ? 'all passed' : 'some failed'}`
    };
  }

  async generateQCReport(inspection: InspectionResult): Promise<string> {
    const prompt = `Generate a professional Quality Control inspection report based on the following data:

Inspection ID: ${inspection.id}
Ticket ID: ${inspection.ticketId}
Status: ${inspection.status}
Overall Score: ${inspection.overallScore}%
Recommendation: ${inspection.recommendation}

Checkpoint Results:
${inspection.checkpoints.map(c => `- ${c.checkpointId}: ${c.status} (${c.score}%)`).join('\n')}

Findings:
${inspection.findings.map(f => `- [${f.severity}] ${f.type}: ${f.description}`).join('\n')}

AI Analysis:
- Confidence: ${inspection.aiAnalysis.confidenceScore * 100}%
- Defects: ${inspection.aiAnalysis.defectsDetected.length} detected
- Reliability Prediction: ${inspection.aiAnalysis.qualityPrediction?.reliabilityScore * 100}%

Generate a formal QC report suitable for documentation and customer delivery.`;

    const response = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': this.env.ANTHROPIC_API_KEY,
        'anthropic-version': '2023-06-01'
      },
      body: JSON.stringify({
        model: 'claude-sonnet-4-20250514',
        max_tokens: 4096,
        messages: [{ role: 'user', content: prompt }]
      })
    });

    const data = await response.json() as any;
    return data.content[0].text;
  }
}

// ═══════════════════════════════════════════════════════════════════════════
// QC TEMPLATE ENGINE
// ═══════════════════════════════════════════════════════════════════════════

const DEFAULT_TEMPLATES: Record<string, QCCheckpoint[]> = {
  'smartphone-screen': [
    {
      id: 'visual-screen',
      name: 'Display Visual Inspection',
      category: 'visual',
      checkType: 'hybrid',
      weight: 25,
      required: true,
      criteria: [
        { id: 'no-dead-pixels', description: 'No dead/stuck pixels' },
        { id: 'no-backlight-bleed', description: 'No backlight bleeding' },
        { id: 'no-scratches', description: 'No visible scratches on glass' },
        { id: 'bezel-alignment', description: 'Screen properly aligned with bezel' },
        { id: 'dust-free', description: 'No dust under display' }
      ]
    },
    {
      id: 'touch-response',
      name: 'Touch Sensitivity Test',
      category: 'functional',
      checkType: 'automated',
      weight: 25,
      required: true,
      criteria: [
        { id: 'multi-touch', description: '10-point multitouch working' },
        { id: 'edge-touch', description: 'Edge touch responsive' },
        { id: 'pressure-sensitivity', description: 'Pressure sensitivity (if applicable)' },
        { id: 'gesture-recognition', description: 'All gestures working' }
      ]
    },
    {
      id: 'display-function',
      name: 'Display Functionality',
      category: 'functional',
      checkType: 'automated',
      weight: 25,
      required: true,
      criteria: [
        { id: 'color-accuracy', description: 'Color accuracy within spec' },
        { id: 'brightness-range', description: 'Full brightness range available' },
        { id: 'true-tone', description: 'True Tone/Auto brightness working' },
        { id: 'refresh-rate', description: 'Refresh rate as specified' }
      ]
    },
    {
      id: 'seal-integrity',
      name: 'Water Resistance Seal',
      category: 'mechanical',
      checkType: 'manual',
      weight: 15,
      required: false,
      criteria: [
        { id: 'adhesive-coverage', description: 'Full adhesive coverage' },
        { id: 'gasket-condition', description: 'Gaskets properly seated' },
        { id: 'port-covers', description: 'Port covers intact' }
      ]
    },
    {
      id: 'final-assembly',
      name: 'Final Assembly Check',
      category: 'visual',
      checkType: 'manual',
      weight: 10,
      required: true,
      criteria: [
        { id: 'screws-torqued', description: 'All screws properly torqued' },
        { id: 'clips-engaged', description: 'All clips engaged' },
        { id: 'no-gaps', description: 'No visible gaps in enclosure' },
        { id: 'buttons-click', description: 'All buttons click properly' }
      ]
    }
  ],
  'laptop-motherboard': [
    {
      id: 'visual-pcb',
      name: 'PCB Visual Inspection',
      category: 'visual',
      checkType: 'hybrid',
      weight: 20,
      required: true,
      criteria: [
        { id: 'solder-joints', description: 'Clean solder joints, no bridges' },
        { id: 'component-placement', description: 'All components properly placed' },
        { id: 'no-corrosion', description: 'No corrosion or oxidation' },
        { id: 'no-burn-marks', description: 'No burn marks or discoloration' },
        { id: 'flux-cleaned', description: 'Flux residue cleaned' }
      ]
    },
    {
      id: 'power-test',
      name: 'Power Rail Testing',
      category: 'electrical',
      checkType: 'automated',
      weight: 25,
      required: true,
      criteria: [
        {
          id: 'vcore',
          description: 'CPU VCore voltage',
          measurement: { type: 'numeric', unit: 'V', min: 0.8, max: 1.4, tolerance: 0.05 }
        },
        {
          id: 'pp3v3',
          description: '3.3V rail',
          measurement: { type: 'numeric', unit: 'V', min: 3.2, max: 3.4, tolerance: 0.05 }
        },
        {
          id: 'pp5v',
          description: '5V rail',
          measurement: { type: 'numeric', unit: 'V', min: 4.9, max: 5.1, tolerance: 0.05 }
        },
        {
          id: 'pp12v',
          description: '12V rail',
          measurement: { type: 'numeric', unit: 'V', min: 11.8, max: 12.2, tolerance: 0.1 }
        }
      ]
    },
    {
      id: 'boot-test',
      name: 'Boot Sequence Test',
      category: 'functional',
      checkType: 'automated',
      weight: 25,
      required: true,
      criteria: [
        { id: 'post-success', description: 'POST completes successfully' },
        { id: 'bios-access', description: 'BIOS accessible' },
        { id: 'os-boot', description: 'OS boots successfully' },
        { id: 'all-devices', description: 'All devices recognized' }
      ]
    },
    {
      id: 'stress-test',
      name: 'Stress Test',
      category: 'functional',
      checkType: 'automated',
      weight: 20,
      required: true,
      criteria: [
        {
          id: 'cpu-temp',
          description: 'CPU temperature under load',
          measurement: { type: 'numeric', unit: '°C', min: 0, max: 90, tolerance: 5 }
        },
        { id: 'no-throttle', description: 'No thermal throttling' },
        { id: 'stable-30min', description: '30 minute stability test passed' },
        { id: 'memory-test', description: 'Memory test passed' }
      ]
    },
    {
      id: 'thermal-paste',
      name: 'Thermal Application',
      category: 'mechanical',
      checkType: 'manual',
      weight: 10,
      required: true,
      criteria: [
        { id: 'paste-coverage', description: 'Full IHS coverage' },
        { id: 'heatsink-mount', description: 'Heatsink properly mounted' },
        { id: 'fan-operation', description: 'Fan spins freely' }
      ]
    }
  ]
};

// ═══════════════════════════════════════════════════════════════════════════
// HONO APP
// ═══════════════════════════════════════════════════════════════════════════

const app = new Hono<{ Bindings: Env }>();

app.use('*', cors());

// Health check
app.get('/health', (c) => c.json({ status: 'healthy', service: 'qc-inspector', version: '1.0.0' }));

// Get QC templates
app.get('/templates', async (c) => {
  const category = c.req.query('category');
  
  const stmt = c.env.NOIZYLAB_DB.prepare(`
    SELECT * FROM qc_templates 
    ${category ? 'WHERE device_category = ?' : ''}
    ORDER BY name
  `);
  
  const { results } = category ? await stmt.bind(category).all() : await stmt.all();
  
  return c.json({
    templates: results,
    defaults: Object.keys(DEFAULT_TEMPLATES)
  });
});

// Get default template for device/repair type
app.get('/templates/default', async (c) => {
  const deviceCategory = c.req.query('device');
  const repairType = c.req.query('repair');
  
  const key = `${deviceCategory}-${repairType}`;
  const template = DEFAULT_TEMPLATES[key];
  
  if (template) {
    return c.json({
      template: {
        id: key,
        name: `${deviceCategory} ${repairType} QC`,
        checkpoints: template
      }
    });
  }
  
  return c.json({ error: 'No default template for this combination' }, 404);
});

// Start inspection
app.post('/inspections', async (c) => {
  const { ticketId, repairId, technicianId, templateId, deviceInfo } = await c.req.json();
  
  // Get template
  let checkpoints: QCCheckpoint[];
  
  if (templateId && DEFAULT_TEMPLATES[templateId]) {
    checkpoints = DEFAULT_TEMPLATES[templateId];
  } else {
    // Load from DB
    const template = await c.env.NOIZYLAB_DB.prepare(
      'SELECT checkpoints FROM qc_templates WHERE id = ?'
    ).bind(templateId).first();
    
    if (template) {
      checkpoints = JSON.parse(template.checkpoints as string);
    } else {
      // Use generic template
      checkpoints = DEFAULT_TEMPLATES['smartphone-screen'];
    }
  }
  
  const inspectionId = `qc_${Date.now()}_${Math.random().toString(36).substring(7)}`;
  
  const inspection: InspectionResult = {
    id: inspectionId,
    ticketId,
    repairId,
    technicianId,
    status: 'pending',
    startedAt: new Date().toISOString(),
    checkpoints: checkpoints.map(cp => ({
      checkpointId: cp.id,
      status: 'skipped' as const,
      score: 0,
      criteriaResults: cp.criteria.map(cr => ({
        criteriaId: cr.id,
        passed: false
      }))
    })),
    overallScore: 0,
    findings: [],
    recommendation: 'rework',
    aiAnalysis: {
      confidenceScore: 0,
      defectsDetected: [],
      qualityPrediction: {
        reliabilityScore: 0,
        estimatedLifespan: 'Unknown',
        riskFactors: []
      },
      comparisonToBaseline: { deviation: 0, areas: [] },
      recommendations: [],
      anomalies: []
    }
  };
  
  // Save to DB
  await c.env.NOIZYLAB_DB.prepare(`
    INSERT INTO qc_inspections (id, ticket_id, repair_id, technician_id, status, data, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?)
  `).bind(
    inspectionId,
    ticketId,
    repairId,
    technicianId,
    'pending',
    JSON.stringify(inspection),
    new Date().toISOString()
  ).run();
  
  // Cache
  await c.env.NOIZYLAB_KV.put(`qc:${inspectionId}`, JSON.stringify(inspection), { expirationTtl: 86400 });
  
  return c.json({ inspection }, 201);
});

// Get inspection
app.get('/inspections/:id', async (c) => {
  const inspectionId = c.req.param('id');
  
  // Try cache first
  const cached = await c.env.NOIZYLAB_KV.get(`qc:${inspectionId}`);
  if (cached) {
    return c.json({ inspection: JSON.parse(cached) });
  }
  
  // Load from DB
  const row = await c.env.NOIZYLAB_DB.prepare(
    'SELECT data FROM qc_inspections WHERE id = ?'
  ).bind(inspectionId).first();
  
  if (!row) {
    return c.json({ error: 'Inspection not found' }, 404);
  }
  
  return c.json({ inspection: JSON.parse(row.data as string) });
});

// Submit checkpoint result
app.post('/inspections/:id/checkpoints/:checkpointId', async (c) => {
  const inspectionId = c.req.param('id');
  const checkpointId = c.req.param('checkpointId');
  const { criteriaResults, images, notes, measurements } = await c.req.json();
  
  // Load inspection
  const cached = await c.env.NOIZYLAB_KV.get(`qc:${inspectionId}`);
  if (!cached) {
    return c.json({ error: 'Inspection not found' }, 404);
  }
  
  const inspection: InspectionResult = JSON.parse(cached);
  const inspector = new AIQualityInspector(c.env);
  
  // Find checkpoint
  const cpIndex = inspection.checkpoints.findIndex(cp => cp.checkpointId === checkpointId);
  if (cpIndex === -1) {
    return c.json({ error: 'Checkpoint not found' }, 404);
  }
  
  // Get template checkpoint
  const templateKey = `${inspection.ticketId.split('-')[0]}-screen`; // Simplified
  const templateCheckpoints = DEFAULT_TEMPLATES[templateKey] || DEFAULT_TEMPLATES['smartphone-screen'];
  const templateCheckpoint = templateCheckpoints.find(tc => tc.id === checkpointId);
  
  // Run automated checks
  let automatedChecks: AutomatedCheck[] = [];
  if (templateCheckpoint) {
    automatedChecks = await inspector.runAutomatedChecks(templateCheckpoint, images || [], measurements || {});
  }
  
  // Calculate score
  const passedCriteria = criteriaResults.filter((cr: any) => cr.passed).length;
  const totalCriteria = criteriaResults.length;
  const automatedScore = automatedChecks.filter(ac => ac.passed).length / Math.max(automatedChecks.length, 1);
  const score = ((passedCriteria / totalCriteria) * 0.7 + automatedScore * 0.3) * 100;
  
  // Update checkpoint
  inspection.checkpoints[cpIndex] = {
    checkpointId,
    status: score >= 80 ? 'passed' : score >= 50 ? 'warning' : 'failed',
    score,
    criteriaResults,
    images,
    notes,
    measuredValues: measurements,
    automatedChecks
  };
  
  // Update overall score
  const completedCheckpoints = inspection.checkpoints.filter(cp => cp.status !== 'skipped');
  if (completedCheckpoints.length > 0) {
    const totalWeight = templateCheckpoints.reduce((sum, tc) => {
      const cpResult = completedCheckpoints.find(cp => cp.checkpointId === tc.id);
      return sum + (cpResult ? tc.weight : 0);
    }, 0);
    
    inspection.overallScore = completedCheckpoints.reduce((sum, cp) => {
      const tc = templateCheckpoints.find(t => t.id === cp.checkpointId);
      return sum + (cp.score * (tc?.weight || 1));
    }, 0) / Math.max(totalWeight, 1);
  }
  
  // Add findings for failed criteria
  criteriaResults.forEach((cr: any) => {
    if (!cr.passed) {
      inspection.findings.push({
        id: `finding_${Date.now()}_${Math.random().toString(36).substring(7)}`,
        type: 'defect',
        severity: templateCheckpoint?.required ? 'major' : 'minor',
        description: cr.notes || `Failed: ${cr.criteriaId}`,
        checkpoint: checkpointId,
        images
      });
    }
  });
  
  // Update inspection status
  const allRequired = templateCheckpoints.filter(tc => tc.required);
  const requiredPassed = allRequired.every(tc => {
    const cp = inspection.checkpoints.find(c => c.checkpointId === tc.id);
    return cp && cp.status === 'passed';
  });
  
  inspection.status = 'in_progress';
  
  // Save
  await c.env.NOIZYLAB_KV.put(`qc:${inspectionId}`, JSON.stringify(inspection), { expirationTtl: 86400 });
  await c.env.NOIZYLAB_DB.prepare(
    'UPDATE qc_inspections SET data = ?, status = ?, updated_at = ? WHERE id = ?'
  ).bind(
    JSON.stringify(inspection),
    inspection.status,
    new Date().toISOString(),
    inspectionId
  ).run();
  
  return c.json({
    checkpoint: inspection.checkpoints[cpIndex],
    overallScore: inspection.overallScore,
    automatedChecks
  });
});

// Run AI analysis on inspection
app.post('/inspections/:id/analyze', async (c) => {
  const inspectionId = c.req.param('id');
  const { deviceInfo } = await c.req.json();
  
  const cached = await c.env.NOIZYLAB_KV.get(`qc:${inspectionId}`);
  if (!cached) {
    return c.json({ error: 'Inspection not found' }, 404);
  }
  
  const inspection: InspectionResult = JSON.parse(cached);
  const inspector = new AIQualityInspector(c.env);
  
  // Collect all images
  const allImages = inspection.checkpoints
    .filter(cp => cp.images && cp.images.length > 0)
    .flatMap(cp => cp.images!);
  
  // Get template checkpoints
  const templateKey = `${deviceInfo?.category || 'smartphone'}-${deviceInfo?.repairType || 'screen'}`;
  const templateCheckpoints = DEFAULT_TEMPLATES[templateKey] || DEFAULT_TEMPLATES['smartphone-screen'];
  
  // Run AI analysis
  const aiAnalysis = await inspector.analyzeImages(allImages, deviceInfo, templateCheckpoints);
  
  // Update inspection
  inspection.aiAnalysis = {
    ...inspection.aiAnalysis,
    ...aiAnalysis
  };
  
  // Determine recommendation
  const criticalDefects = (aiAnalysis.defectsDetected || []).filter(d => d.severity === 'critical');
  const majorDefects = (aiAnalysis.defectsDetected || []).filter(d => d.severity === 'major');
  
  if (criticalDefects.length > 0) {
    inspection.recommendation = 'escalate';
  } else if (majorDefects.length > 0) {
    inspection.recommendation = 'rework';
  } else if (inspection.overallScore >= 90) {
    inspection.recommendation = 'ship';
  } else if (inspection.overallScore >= 70) {
    inspection.recommendation = 'rework';
  } else {
    inspection.recommendation = 'scrap';
  }
  
  // Add AI-detected defects as findings
  for (const defect of aiAnalysis.defectsDetected || []) {
    inspection.findings.push({
      id: `ai_finding_${Date.now()}_${Math.random().toString(36).substring(7)}`,
      type: 'defect',
      severity: defect.severity,
      description: `AI Detected: ${defect.type}`,
      location: defect.location,
      suggestedAction: defect.suggestedFix
    });
  }
  
  // Save
  await c.env.NOIZYLAB_KV.put(`qc:${inspectionId}`, JSON.stringify(inspection), { expirationTtl: 86400 });
  await c.env.NOIZYLAB_DB.prepare(
    'UPDATE qc_inspections SET data = ?, updated_at = ? WHERE id = ?'
  ).bind(
    JSON.stringify(inspection),
    new Date().toISOString(),
    inspectionId
  ).run();
  
  return c.json({
    aiAnalysis: inspection.aiAnalysis,
    recommendation: inspection.recommendation,
    findings: inspection.findings.filter(f => f.id.startsWith('ai_'))
  });
});

// Complete inspection
app.post('/inspections/:id/complete', async (c) => {
  const inspectionId = c.req.param('id');
  const { signoff } = await c.req.json();
  
  const cached = await c.env.NOIZYLAB_KV.get(`qc:${inspectionId}`);
  if (!cached) {
    return c.json({ error: 'Inspection not found' }, 404);
  }
  
  const inspection: InspectionResult = JSON.parse(cached);
  
  // Check if all required checkpoints are completed
  const skippedRequired = inspection.checkpoints.filter(cp => cp.status === 'skipped');
  if (skippedRequired.length > 0) {
    return c.json({
      error: 'Cannot complete inspection with skipped checkpoints',
      skipped: skippedRequired.map(cp => cp.checkpointId)
    }, 400);
  }
  
  // Add signoff
  inspection.signoff = {
    ...signoff,
    signedAt: new Date().toISOString(),
    digitalSignature: crypto.randomUUID() // In production, use proper digital signature
  };
  
  // Determine final status
  const failedRequired = inspection.checkpoints.filter(cp => cp.status === 'failed');
  inspection.status = failedRequired.length > 0 ? 'failed' : 
                      inspection.overallScore >= 80 ? 'passed' : 'conditional';
  
  inspection.completedAt = new Date().toISOString();
  
  // Generate report
  const inspector = new AIQualityInspector(c.env);
  const report = await inspector.generateQCReport(inspection);
  
  // Save report to R2
  const reportKey = `qc-reports/${inspectionId}.md`;
  await c.env.NOIZYLAB_UPLOADS.put(reportKey, report, {
    customMetadata: {
      inspectionId,
      status: inspection.status,
      completedAt: inspection.completedAt
    }
  });
  
  // Save to DB
  await c.env.NOIZYLAB_KV.put(`qc:${inspectionId}`, JSON.stringify(inspection), { expirationTtl: 604800 });
  await c.env.NOIZYLAB_DB.prepare(
    'UPDATE qc_inspections SET data = ?, status = ?, completed_at = ?, updated_at = ? WHERE id = ?'
  ).bind(
    JSON.stringify(inspection),
    inspection.status,
    inspection.completedAt,
    new Date().toISOString(),
    inspectionId
  ).run();
  
  // Queue notification
  await c.env.NOIZYLAB_QUEUE.send({
    type: 'qc_complete',
    inspectionId,
    ticketId: inspection.ticketId,
    status: inspection.status,
    recommendation: inspection.recommendation
  });
  
  return c.json({
    inspection,
    reportUrl: reportKey
  });
});

// Get QC stats
app.get('/stats', async (c) => {
  const range = c.req.query('range') || '30d';
  const technicianId = c.req.query('technician');
  
  const daysMap: Record<string, number> = { '7d': 7, '30d': 30, '90d': 90 };
  const days = daysMap[range] || 30;
  const startDate = new Date(Date.now() - days * 24 * 60 * 60 * 1000).toISOString();
  
  let query = `
    SELECT 
      COUNT(*) as total,
      SUM(CASE WHEN status = 'passed' THEN 1 ELSE 0 END) as passed,
      SUM(CASE WHEN status = 'failed' THEN 1 ELSE 0 END) as failed,
      SUM(CASE WHEN status = 'conditional' THEN 1 ELSE 0 END) as conditional
    FROM qc_inspections
    WHERE created_at >= ?
  `;
  
  const params: any[] = [startDate];
  
  if (technicianId) {
    query += ' AND technician_id = ?';
    params.push(technicianId);
  }
  
  const stats = await c.env.NOIZYLAB_DB.prepare(query).bind(...params).first();
  
  // Calculate pass rate
  const passRate = stats && stats.total ? 
    ((stats.passed as number) / (stats.total as number) * 100).toFixed(1) : 0;
  
  return c.json({
    stats: {
      ...stats,
      passRate,
      range
    }
  });
});

export default app;
