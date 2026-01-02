/**
 * ███████╗ ██████╗██╗  ██╗███████╗███╗   ███╗ █████╗ ████████╗██╗ ██████╗
 * ██╔════╝██╔════╝██║  ██║██╔════╝████╗ ████║██╔══██╗╚══██╔══╝██║██╔════╝
 * ███████╗██║     ███████║█████╗  ██╔████╔██║███████║   ██║   ██║██║     
 * ╚════██║██║     ██╔══██║██╔══╝  ██║╚██╔╝██║██╔══██║   ██║   ██║██║     
 * ███████║╚██████╗██║  ██║███████╗██║ ╚═╝ ██║██║  ██║   ██║   ██║╚██████╗
 * ╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝
 *        █████╗ ███╗   ██╗ █████╗ ██╗  ██╗   ██╗███████╗███████╗██████╗ 
 *       ██╔══██╗████╗  ██║██╔══██╗██║  ╚██╗ ██╔╝╚══███╔╝██╔════╝██╔══██╗
 *       ███████║██╔██╗ ██║███████║██║   ╚████╔╝   ███╔╝ █████╗  ██████╔╝
 *       ██╔══██║██║╚██╗██║██╔══██║██║    ╚██╔╝   ███╔╝  ██╔══╝  ██╔══██╗
 *       ██║  ██║██║ ╚████║██║  ██║███████╗██║   ███████╗███████╗██║  ██║
 *       ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝   ╚══════╝╚══════╝╚═╝  ╚═╝
 * 
 * NoizyLab OS - Schematic Analyzer Worker
 * AI-powered schematic analysis, circuit tracing, and component identification
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

// ═══════════════════════════════════════════════════════════════════════════
// TYPES & INTERFACES
// ═══════════════════════════════════════════════════════════════════════════

interface Env {
  NOIZYLAB_KV: KVNamespace;
  NOIZYLAB_DB: D1Database;
  NOIZYLAB_SCHEMATICS: R2Bucket;
  AI: Ai;
  ANTHROPIC_API_KEY: string;
}

interface Schematic {
  id: string;
  name: string;
  deviceMake: string;
  deviceModel: string;
  boardId: string;
  version: string;
  pages: SchematicPage[];
  components: ComponentIndex[];
  netList: NetEntry[];
  searchIndex: SearchIndexEntry[];
  metadata: SchematicMetadata;
  createdAt: string;
  updatedAt: string;
}

interface SchematicPage {
  pageNumber: number;
  title: string;
  section: string;
  r2Key: string;
  thumbnail?: string;
  annotations?: Annotation[];
  components: string[]; // Component IDs on this page
}

interface ComponentIndex {
  id: string;
  designator: string;  // R1234, C5678, U12, etc.
  type: ComponentType;
  value?: string;      // 10K, 100nF, etc.
  package?: string;    // 0402, 0603, BGA, etc.
  description?: string;
  partNumber?: string;
  pages: number[];     // Which pages it appears on
  coordinates: {
    page: number;
    x: number;
    y: number;
  }[];
  connectedNets: string[];
  powerRail?: string;
  criticalPath?: boolean;
}

type ComponentType = 
  | 'resistor' | 'capacitor' | 'inductor' | 'diode' | 'transistor'
  | 'mosfet' | 'ic' | 'connector' | 'crystal' | 'fuse' | 'led'
  | 'transformer' | 'relay' | 'switch' | 'test_point' | 'other';

interface NetEntry {
  name: string;
  type: 'power' | 'ground' | 'signal' | 'clock' | 'data' | 'analog';
  voltage?: string;
  components: string[];  // Component designators
  pins: NetPin[];
  description?: string;
}

interface NetPin {
  component: string;
  pin: string;
}

interface SearchIndexEntry {
  term: string;
  type: 'component' | 'net' | 'value' | 'description' | 'function';
  reference: string;
  page?: number;
}

interface SchematicMetadata {
  totalPages: number;
  totalComponents: number;
  totalNets: number;
  powerRails: string[];
  majorICs: string[];
  boardRevision?: string;
  releaseDate?: string;
}

interface Annotation {
  id: string;
  type: 'highlight' | 'note' | 'measurement' | 'path_trace';
  x: number;
  y: number;
  width?: number;
  height?: number;
  color: string;
  content?: string;
  createdBy: string;
  createdAt: string;
}

interface CircuitTrace {
  id: string;
  name: string;
  startComponent: string;
  endComponent: string;
  path: TraceNode[];
  signalFlow: 'forward' | 'reverse' | 'bidirectional';
  category: 'power' | 'signal' | 'data' | 'clock' | 'control';
}

interface TraceNode {
  component: string;
  pin: string;
  net: string;
  page: number;
  coordinates: { x: number; y: number };
}

interface AnalysisResult {
  id: string;
  schematicId: string;
  query: string;
  analysisType: 'component_lookup' | 'circuit_trace' | 'fault_diagnosis' | 'power_analysis' | 'signal_flow';
  results: any;
  aiInsights: string[];
  relatedComponents: string[];
  suggestedMeasurements: Measurement[];
  createdAt: string;
}

interface Measurement {
  point: string;
  type: 'voltage' | 'resistance' | 'continuity' | 'signal' | 'current';
  expectedValue?: string;
  testCondition?: string;
}

// ═══════════════════════════════════════════════════════════════════════════
// SCHEMATIC AI ENGINE
// ═══════════════════════════════════════════════════════════════════════════

class SchematicAI {
  private env: Env;

  constructor(env: Env) {
    this.env = env;
  }

  async analyzeCircuit(
    schematic: Schematic,
    query: string,
    context?: { symptom?: string; measurements?: Record<string, string> }
  ): Promise<{
    analysis: string;
    components: ComponentIndex[];
    traces: CircuitTrace[];
    measurements: Measurement[];
    insights: string[];
  }> {
    const systemPrompt = `You are an expert electronics engineer specializing in board-level repair and schematic analysis.

Schematic: ${schematic.name}
Device: ${schematic.deviceMake} ${schematic.deviceModel}
Board ID: ${schematic.boardId}

Power Rails Available:
${schematic.metadata.powerRails.join(', ')}

Major ICs:
${schematic.metadata.majorICs.join(', ')}

Component Count: ${schematic.metadata.totalComponents}
Net Count: ${schematic.metadata.totalNets}

${context?.symptom ? `Reported Symptom: ${context.symptom}` : ''}
${context?.measurements ? `Measurements Taken: ${JSON.stringify(context.measurements)}` : ''}

Analyze the query and provide detailed circuit analysis.

Return JSON:
{
  "analysis": "detailed explanation of the circuit/issue",
  "relevantComponents": ["list of component designators"],
  "circuitPath": ["step-by-step signal/power flow"],
  "measurements": [
    {"point": "testpoint/component", "type": "voltage|resistance|etc", "expectedValue": "value", "testCondition": "when/how to test"}
  ],
  "possibleFaults": ["potential failure points if symptoms provided"],
  "repairDifficulty": "easy|moderate|advanced|expert",
  "insights": ["additional observations"]
}`;

    const netContext = schematic.netList.slice(0, 50).map(n => 
      `${n.name}: ${n.type} - ${n.components.slice(0, 5).join(', ')}`
    ).join('\n');

    const componentContext = schematic.components.slice(0, 100).map(c =>
      `${c.designator}: ${c.type} ${c.value || ''} - Nets: ${c.connectedNets.slice(0, 3).join(', ')}`
    ).join('\n');

    try {
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
          system: systemPrompt,
          messages: [{
            role: 'user',
            content: `Query: ${query}\n\nRelevant Nets:\n${netContext}\n\nRelevant Components:\n${componentContext}`
          }]
        })
      });

      const data = await response.json() as any;
      const content = data.content[0].text;

      const jsonMatch = content.match(/\{[\s\S]*\}/);
      if (jsonMatch) {
        const result = JSON.parse(jsonMatch[0]);

        // Find actual components
        const components = result.relevantComponents
          .map((d: string) => schematic.components.find(c => c.designator === d))
          .filter(Boolean);

        // Build circuit trace
        const traces: CircuitTrace[] = result.circuitPath ? [{
          id: crypto.randomUUID(),
          name: query,
          startComponent: result.circuitPath[0] || '',
          endComponent: result.circuitPath[result.circuitPath.length - 1] || '',
          path: result.circuitPath.map((step: string, i: number) => ({
            component: step.split('.')[0],
            pin: step.split('.')[1] || '',
            net: '',
            page: 1,
            coordinates: { x: 0, y: 0 }
          })),
          signalFlow: 'forward',
          category: 'signal'
        }] : [];

        return {
          analysis: result.analysis,
          components,
          traces,
          measurements: result.measurements || [],
          insights: result.insights || []
        };
      }

      return {
        analysis: content,
        components: [],
        traces: [],
        measurements: [],
        insights: []
      };

    } catch (error) {
      console.error('Schematic AI error:', error);
      return {
        analysis: 'AI analysis failed',
        components: [],
        traces: [],
        measurements: [],
        insights: ['Please try again or perform manual analysis']
      };
    }
  }

  async identifyComponent(
    imageData: ArrayBuffer,
    schematic: Schematic
  ): Promise<{
    identified: boolean;
    component?: ComponentIndex;
    alternatives?: ComponentIndex[];
    confidence: number;
  }> {
    // Use vision to identify component from board photo
    const base64Image = btoa(String.fromCharCode(...new Uint8Array(imageData)));

    const response = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': this.env.ANTHROPIC_API_KEY,
        'anthropic-version': '2023-06-01'
      },
      body: JSON.stringify({
        model: 'claude-sonnet-4-20250514',
        max_tokens: 1024,
        messages: [{
          role: 'user',
          content: [
            {
              type: 'image',
              source: { type: 'base64', media_type: 'image/jpeg', data: base64Image }
            },
            {
              type: 'text',
              text: `Identify this component from a ${schematic.deviceMake} ${schematic.deviceModel} board.
              
Look for:
- Component designator (printed text like R1234, C567, U12)
- Component type (resistor, capacitor, IC, etc)
- Package type
- Any visible markings

Return JSON:
{
  "designator": "detected designator or null",
  "type": "component type",
  "package": "package size/type",
  "markings": "visible text/codes",
  "confidence": 0.0-1.0
}`
            }
          ]
        }]
      })
    });

    const data = await response.json() as any;
    const content = data.content[0].text;

    try {
      const jsonMatch = content.match(/\{[\s\S]*\}/);
      if (jsonMatch) {
        const result = JSON.parse(jsonMatch[0]);

        if (result.designator) {
          const component = schematic.components.find(c => 
            c.designator.toLowerCase() === result.designator.toLowerCase()
          );

          if (component) {
            return {
              identified: true,
              component,
              confidence: result.confidence
            };
          }

          // Search for alternatives
          const alternatives = schematic.components.filter(c =>
            c.type === result.type || c.package === result.package
          ).slice(0, 5);

          return {
            identified: false,
            alternatives,
            confidence: result.confidence * 0.5
          };
        }
      }
    } catch {}

    return { identified: false, confidence: 0 };
  }

  async tracePowerRail(
    schematic: Schematic,
    railName: string
  ): Promise<{
    rail: NetEntry | null;
    sourceComponents: ComponentIndex[];
    consumerComponents: ComponentIndex[];
    filterComponents: ComponentIndex[];
    testPoints: { component: string; expectedVoltage: string }[];
    faultIndicators: string[];
  }> {
    const rail = schematic.netList.find(n => 
      n.name.toLowerCase().includes(railName.toLowerCase()) || 
      n.voltage === railName
    );

    if (!rail) {
      return {
        rail: null,
        sourceComponents: [],
        consumerComponents: [],
        filterComponents: [],
        testPoints: [],
        faultIndicators: []
      };
    }

    const railComponents = rail.components.map(d => 
      schematic.components.find(c => c.designator === d)
    ).filter(Boolean) as ComponentIndex[];

    // Categorize components
    const sourceComponents = railComponents.filter(c => 
      c.type === 'ic' && (c.description?.toLowerCase().includes('regulator') || 
                         c.description?.toLowerCase().includes('pmic') ||
                         c.description?.toLowerCase().includes('buck') ||
                         c.description?.toLowerCase().includes('ldo'))
    );

    const filterComponents = railComponents.filter(c =>
      c.type === 'capacitor' || c.type === 'inductor' || c.type === 'fuse'
    );

    const consumerComponents = railComponents.filter(c =>
      !sourceComponents.includes(c) && !filterComponents.includes(c) && c.type === 'ic'
    );

    // Generate test points
    const testPoints = [
      ...sourceComponents.map(c => ({
        component: c.designator,
        expectedVoltage: rail.voltage || 'Check schematic'
      })),
      ...filterComponents.filter(c => c.type === 'inductor').map(c => ({
        component: c.designator,
        expectedVoltage: rail.voltage || 'Check schematic'
      }))
    ];

    // Fault indicators
    const faultIndicators = [
      `If ${rail.name} is low: Check ${sourceComponents[0]?.designator || 'source IC'} enable and input`,
      `If ${rail.name} is shorted: Check ${filterComponents.filter(c => c.type === 'capacitor').map(c => c.designator).join(', ')} for shorts`,
      `If ${rail.name} is noisy: Check ${filterComponents.filter(c => c.type === 'inductor').map(c => c.designator).join(', ')} inductors`
    ];

    return {
      rail,
      sourceComponents,
      consumerComponents,
      filterComponents,
      testPoints,
      faultIndicators
    };
  }
}

// ═══════════════════════════════════════════════════════════════════════════
// COMPONENT DATABASE
// ═══════════════════════════════════════════════════════════════════════════

const COMMON_FAULTS: Record<string, { symptoms: string[]; tests: Measurement[]; causes: string[] }> = {
  'no_power': {
    symptoms: ['Device won\'t turn on', 'No LED indicators', 'No response to power button'],
    tests: [
      { point: 'Battery connector', type: 'voltage', expectedValue: '3.7-4.2V', testCondition: 'Battery installed' },
      { point: 'Main power rail', type: 'voltage', expectedValue: 'Per schematic', testCondition: 'Power applied' },
      { point: 'PMIC output rails', type: 'voltage', expectedValue: 'Per schematic', testCondition: 'After power button press' }
    ],
    causes: ['Dead battery', 'Faulty charging circuit', 'Shorted capacitor', 'Failed PMIC', 'Broken power button']
  },
  'no_charge': {
    symptoms: ['Won\'t charge', 'Charging indicator doesn\'t appear', 'Gets hot when plugged in'],
    tests: [
      { point: 'USB connector', type: 'voltage', expectedValue: '5V', testCondition: 'Charger connected' },
      { point: 'Charge IC input', type: 'voltage', expectedValue: '5V', testCondition: 'Charger connected' },
      { point: 'Battery terminals', type: 'voltage', expectedValue: 'Increasing', testCondition: 'While charging' }
    ],
    causes: ['Damaged USB port', 'Faulty charge IC', 'Shorted battery', 'Damaged charging flex']
  },
  'no_display': {
    symptoms: ['Screen is black', 'Backlight but no image', 'Screen flickers'],
    tests: [
      { point: 'Display connector', type: 'continuity', testCondition: 'Connector seated' },
      { point: 'Backlight voltage', type: 'voltage', expectedValue: '15-20V', testCondition: 'Screen on' },
      { point: 'Display data lines', type: 'signal', testCondition: 'Device booted' }
    ],
    causes: ['Bad display', 'Display connector damage', 'Backlight driver failure', 'GPU/SoC failure']
  },
  'no_touch': {
    symptoms: ['Touch not responding', 'Erratic touch', 'Partial touch response'],
    tests: [
      { point: 'Touch connector', type: 'continuity', testCondition: 'Connector seated' },
      { point: 'Touch IC power', type: 'voltage', expectedValue: '1.8V/3.3V', testCondition: 'Device on' },
      { point: 'Touch I2C lines', type: 'signal', testCondition: 'Touch active' }
    ],
    causes: ['Damaged digitizer', 'Touch IC failure', 'Connector damage', 'Flex cable tear']
  }
};

// ═══════════════════════════════════════════════════════════════════════════
// HONO APP
// ═══════════════════════════════════════════════════════════════════════════

const app = new Hono<{ Bindings: Env }>();

app.use('*', cors());

// Health check
app.get('/health', (c) => c.json({ 
  status: 'healthy', 
  service: 'schematic-analyzer',
  version: '1.0.0'
}));

// ═══════════════════════════════════════════════════════════════════════════
// SCHEMATIC MANAGEMENT
// ═══════════════════════════════════════════════════════════════════════════

app.get('/schematics', async (c) => {
  const make = c.req.query('make');
  const model = c.req.query('model');

  let query = 'SELECT * FROM schematics WHERE 1=1';
  const params: any[] = [];

  if (make) {
    query += ' AND device_make = ?';
    params.push(make);
  }
  if (model) {
    query += ' AND device_model LIKE ?';
    params.push(`%${model}%`);
  }

  query += ' ORDER BY device_make, device_model';

  const { results } = await c.env.NOIZYLAB_DB.prepare(query).bind(...params).all();

  return c.json({
    schematics: results.map(r => ({
      id: r.id,
      name: r.name,
      deviceMake: r.device_make,
      deviceModel: r.device_model,
      boardId: r.board_id,
      version: r.version,
      pageCount: r.page_count,
      componentCount: r.component_count
    }))
  });
});

app.get('/schematics/:id', async (c) => {
  const schematicId = c.req.param('id');

  // Try cache
  const cached = await c.env.NOIZYLAB_KV.get(`schematic:${schematicId}`);
  if (cached) {
    return c.json({ schematic: JSON.parse(cached) });
  }

  const row = await c.env.NOIZYLAB_DB.prepare(
    'SELECT * FROM schematics WHERE id = ?'
  ).bind(schematicId).first();

  if (!row) {
    return c.json({ error: 'Schematic not found' }, 404);
  }

  const schematic: Schematic = {
    id: row.id as string,
    name: row.name as string,
    deviceMake: row.device_make as string,
    deviceModel: row.device_model as string,
    boardId: row.board_id as string,
    version: row.version as string,
    pages: JSON.parse(row.pages as string),
    components: JSON.parse(row.components as string),
    netList: JSON.parse(row.net_list as string),
    searchIndex: JSON.parse(row.search_index as string),
    metadata: JSON.parse(row.metadata as string),
    createdAt: row.created_at as string,
    updatedAt: row.updated_at as string
  };

  // Cache for 1 hour
  await c.env.NOIZYLAB_KV.put(`schematic:${schematicId}`, JSON.stringify(schematic), { expirationTtl: 3600 });

  return c.json({ schematic });
});

// Get page image
app.get('/schematics/:id/pages/:page', async (c) => {
  const schematicId = c.req.param('id');
  const pageNum = parseInt(c.req.param('page'));

  const row = await c.env.NOIZYLAB_DB.prepare(
    'SELECT pages FROM schematics WHERE id = ?'
  ).bind(schematicId).first();

  if (!row) {
    return c.json({ error: 'Schematic not found' }, 404);
  }

  const pages = JSON.parse(row.pages as string) as SchematicPage[];
  const page = pages.find(p => p.pageNumber === pageNum);

  if (!page) {
    return c.json({ error: 'Page not found' }, 404);
  }

  const image = await c.env.NOIZYLAB_SCHEMATICS.get(page.r2Key);
  if (!image) {
    return c.json({ error: 'Page image not found' }, 404);
  }

  return new Response(image.body, {
    headers: {
      'Content-Type': 'image/png',
      'Cache-Control': 'public, max-age=86400'
    }
  });
});

// ═══════════════════════════════════════════════════════════════════════════
// SEARCH & LOOKUP
// ═══════════════════════════════════════════════════════════════════════════

app.get('/schematics/:id/search', async (c) => {
  const schematicId = c.req.param('id');
  const query = c.req.query('q')?.toLowerCase();

  if (!query) {
    return c.json({ error: 'Search query required' }, 400);
  }

  const cached = await c.env.NOIZYLAB_KV.get(`schematic:${schematicId}`);
  if (!cached) {
    return c.json({ error: 'Schematic not found' }, 404);
  }

  const schematic: Schematic = JSON.parse(cached);

  // Search components
  const componentResults = schematic.components.filter(c =>
    c.designator.toLowerCase().includes(query) ||
    c.value?.toLowerCase().includes(query) ||
    c.description?.toLowerCase().includes(query) ||
    c.partNumber?.toLowerCase().includes(query)
  );

  // Search nets
  const netResults = schematic.netList.filter(n =>
    n.name.toLowerCase().includes(query) ||
    n.description?.toLowerCase().includes(query)
  );

  // Search index
  const indexResults = schematic.searchIndex.filter(e =>
    e.term.toLowerCase().includes(query)
  );

  return c.json({
    components: componentResults.slice(0, 20),
    nets: netResults.slice(0, 10),
    indexed: indexResults.slice(0, 20),
    totalResults: componentResults.length + netResults.length + indexResults.length
  });
});

// Component lookup
app.get('/schematics/:id/components/:designator', async (c) => {
  const schematicId = c.req.param('id');
  const designator = c.req.param('designator').toUpperCase();

  const cached = await c.env.NOIZYLAB_KV.get(`schematic:${schematicId}`);
  if (!cached) {
    return c.json({ error: 'Schematic not found' }, 404);
  }

  const schematic: Schematic = JSON.parse(cached);

  const component = schematic.components.find(c => 
    c.designator.toUpperCase() === designator
  );

  if (!component) {
    return c.json({ error: 'Component not found' }, 404);
  }

  // Get connected components
  const connectedComponents = schematic.components.filter(c =>
    c.designator !== designator &&
    c.connectedNets.some(n => component.connectedNets.includes(n))
  );

  // Get relevant nets
  const relevantNets = schematic.netList.filter(n =>
    component.connectedNets.includes(n.name)
  );

  return c.json({
    component,
    connectedComponents: connectedComponents.slice(0, 20),
    nets: relevantNets,
    pages: component.pages
  });
});

// Net lookup
app.get('/schematics/:id/nets/:name', async (c) => {
  const schematicId = c.req.param('id');
  const netName = c.req.param('name');

  const cached = await c.env.NOIZYLAB_KV.get(`schematic:${schematicId}`);
  if (!cached) {
    return c.json({ error: 'Schematic not found' }, 404);
  }

  const schematic: Schematic = JSON.parse(cached);

  const net = schematic.netList.find(n => 
    n.name.toLowerCase() === netName.toLowerCase()
  );

  if (!net) {
    return c.json({ error: 'Net not found' }, 404);
  }

  // Get all components on this net
  const netComponents = net.components.map(d =>
    schematic.components.find(c => c.designator === d)
  ).filter(Boolean);

  return c.json({
    net,
    components: netComponents,
    pinouts: net.pins
  });
});

// ═══════════════════════════════════════════════════════════════════════════
// AI ANALYSIS
// ═══════════════════════════════════════════════════════════════════════════

app.post('/schematics/:id/analyze', async (c) => {
  const schematicId = c.req.param('id');
  const { query, symptom, measurements } = await c.req.json();

  const cached = await c.env.NOIZYLAB_KV.get(`schematic:${schematicId}`);
  if (!cached) {
    return c.json({ error: 'Schematic not found' }, 404);
  }

  const schematic: Schematic = JSON.parse(cached);
  const ai = new SchematicAI(c.env);

  const result = await ai.analyzeCircuit(schematic, query, { symptom, measurements });

  // Save analysis
  const analysisId = `analysis_${Date.now()}_${Math.random().toString(36).substring(7)}`;

  await c.env.NOIZYLAB_DB.prepare(`
    INSERT INTO schematic_analyses (id, schematic_id, query, analysis_type, results, created_at)
    VALUES (?, ?, ?, ?, ?, ?)
  `).bind(
    analysisId,
    schematicId,
    query,
    symptom ? 'fault_diagnosis' : 'circuit_trace',
    JSON.stringify(result),
    new Date().toISOString()
  ).run();

  return c.json({
    analysisId,
    ...result
  });
});

// Power rail analysis
app.get('/schematics/:id/power/:rail', async (c) => {
  const schematicId = c.req.param('id');
  const railName = c.req.param('rail');

  const cached = await c.env.NOIZYLAB_KV.get(`schematic:${schematicId}`);
  if (!cached) {
    return c.json({ error: 'Schematic not found' }, 404);
  }

  const schematic: Schematic = JSON.parse(cached);
  const ai = new SchematicAI(c.env);

  const result = await ai.tracePowerRail(schematic, railName);

  return c.json(result);
});

// Identify component from image
app.post('/schematics/:id/identify', async (c) => {
  const schematicId = c.req.param('id');
  const formData = await c.req.formData();
  const imageFile = formData.get('image') as File;

  if (!imageFile) {
    return c.json({ error: 'Image file required' }, 400);
  }

  const cached = await c.env.NOIZYLAB_KV.get(`schematic:${schematicId}`);
  if (!cached) {
    return c.json({ error: 'Schematic not found' }, 404);
  }

  const schematic: Schematic = JSON.parse(cached);
  const ai = new SchematicAI(c.env);

  const imageData = await imageFile.arrayBuffer();
  const result = await ai.identifyComponent(imageData, schematic);

  return c.json(result);
});

// ═══════════════════════════════════════════════════════════════════════════
// FAULT DIAGNOSIS
// ═══════════════════════════════════════════════════════════════════════════

app.get('/faults', (c) => {
  return c.json({
    faults: Object.entries(COMMON_FAULTS).map(([id, data]) => ({
      id,
      ...data
    }))
  });
});

app.post('/schematics/:id/diagnose', async (c) => {
  const schematicId = c.req.param('id');
  const { symptom, measurements } = await c.req.json();

  const cached = await c.env.NOIZYLAB_KV.get(`schematic:${schematicId}`);
  if (!cached) {
    return c.json({ error: 'Schematic not found' }, 404);
  }

  const schematic: Schematic = JSON.parse(cached);
  const ai = new SchematicAI(c.env);

  // Find relevant common fault
  const matchingFault = Object.entries(COMMON_FAULTS).find(([_, data]) =>
    data.symptoms.some(s => symptom.toLowerCase().includes(s.toLowerCase().split(' ')[0]))
  );

  // AI analysis
  const aiResult = await ai.analyzeCircuit(schematic, `Diagnose: ${symptom}`, {
    symptom,
    measurements
  });

  return c.json({
    symptom,
    commonFault: matchingFault ? {
      id: matchingFault[0],
      ...matchingFault[1]
    } : null,
    aiAnalysis: aiResult,
    suggestedTests: [
      ...(matchingFault?.[1].tests || []),
      ...aiResult.measurements
    ],
    possibleCauses: [
      ...(matchingFault?.[1].causes || []),
      ...aiResult.insights
    ]
  });
});

// ═══════════════════════════════════════════════════════════════════════════
// ANNOTATIONS
// ═══════════════════════════════════════════════════════════════════════════

app.post('/schematics/:id/pages/:page/annotations', async (c) => {
  const schematicId = c.req.param('id');
  const pageNum = parseInt(c.req.param('page'));
  const annotation = await c.req.json() as Omit<Annotation, 'id' | 'createdAt'>;

  const row = await c.env.NOIZYLAB_DB.prepare(
    'SELECT pages FROM schematics WHERE id = ?'
  ).bind(schematicId).first();

  if (!row) {
    return c.json({ error: 'Schematic not found' }, 404);
  }

  const pages = JSON.parse(row.pages as string) as SchematicPage[];
  const pageIndex = pages.findIndex(p => p.pageNumber === pageNum);

  if (pageIndex === -1) {
    return c.json({ error: 'Page not found' }, 404);
  }

  const newAnnotation: Annotation = {
    ...annotation,
    id: crypto.randomUUID(),
    createdAt: new Date().toISOString()
  };

  pages[pageIndex].annotations = [...(pages[pageIndex].annotations || []), newAnnotation];

  await c.env.NOIZYLAB_DB.prepare(
    'UPDATE schematics SET pages = ?, updated_at = ? WHERE id = ?'
  ).bind(
    JSON.stringify(pages),
    new Date().toISOString(),
    schematicId
  ).run();

  // Invalidate cache
  await c.env.NOIZYLAB_KV.delete(`schematic:${schematicId}`);

  return c.json({ annotation: newAnnotation }, 201);
});

// ═══════════════════════════════════════════════════════════════════════════
// BATCH OPERATIONS
// ═══════════════════════════════════════════════════════════════════════════

app.post('/schematics/:id/batch-lookup', async (c) => {
  const schematicId = c.req.param('id');
  const { designators } = await c.req.json();

  const cached = await c.env.NOIZYLAB_KV.get(`schematic:${schematicId}`);
  if (!cached) {
    return c.json({ error: 'Schematic not found' }, 404);
  }

  const schematic: Schematic = JSON.parse(cached);

  const results = designators.map((d: string) => {
    const component = schematic.components.find(c => 
      c.designator.toUpperCase() === d.toUpperCase()
    );
    return { designator: d, found: !!component, component };
  });

  return c.json({ results });
});

export default app;
