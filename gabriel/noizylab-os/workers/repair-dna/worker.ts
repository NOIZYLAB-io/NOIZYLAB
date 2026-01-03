/**
 * NoizyLab OS - Repair DNA Fingerprinting Worker
 * 🧬 Unique Digital Identity for Every Device
 * 
 * Creates and maintains a unique "DNA" fingerprint for each device
 * that tracks its entire repair history, component lineage, and
 * evolution over time - like a blockchain for device repairs.
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
  REPAIR_DNA_KV: KVNamespace;
  D1_DATABASE: D1Database;
  R2_BUCKET: R2Bucket;
  AI: Ai;
  BRAIN_SERVICE: Fetcher;
  ANALYTICS_SERVICE: Fetcher;
  PREDICTIVE_SERVICE: Fetcher;
}

interface DeviceDNA {
  dna_id: string;
  device_id: string;
  serial_number?: string;
  imei?: string;
  created_at: string;
  last_updated: string;
  fingerprint: DeviceFingerprint;
  repair_genome: RepairGenome;
  component_lineage: ComponentLineage[];
  health_markers: HealthMarker[];
  ancestry: DeviceAncestry;
  mutations: Mutation[];
  risk_alleles: RiskAllele[];
  dna_hash: string;
  verification_chain: VerificationBlock[];
}

interface DeviceFingerprint {
  hardware_signature: string;
  original_components: ComponentSignature[];
  manufacture_batch?: string;
  factory_calibration?: Record<string, any>;
  unique_identifiers: Record<string, string>;
}

interface ComponentSignature {
  component_type: string;
  original_part_number: string;
  original_manufacturer: string;
  original_date_code?: string;
  original_serial?: string;
  signature_hash: string;
}

interface RepairGenome {
  total_repairs: number;
  repair_frequency: number; // repairs per year
  dominant_issues: RepairTrait[];
  repair_success_rate: number;
  technician_diversity: number;
  parts_replaced_count: number;
  total_repair_cost: number;
  genome_complexity_score: number;
}

interface RepairTrait {
  trait_name: string;
  occurrence_count: number;
  first_occurrence: string;
  last_occurrence: string;
  inheritance_pattern: 'dominant' | 'recessive' | 'codominant';
  associated_symptoms: string[];
}

interface ComponentLineage {
  component_type: string;
  generation: number;
  current_component: ComponentState;
  ancestors: ComponentState[];
  replacement_history: ReplacementEvent[];
  genetic_drift: number; // deviation from original spec
}

interface ComponentState {
  part_number: string;
  manufacturer: string;
  quality_tier: 'OEM' | 'OEM-Equivalent' | 'Aftermarket' | 'Refurbished' | 'Unknown';
  install_date: string;
  source: string;
  health_at_install: number;
  current_health: number;
  state_hash: string;
}

interface ReplacementEvent {
  event_id: string;
  timestamp: string;
  previous_part: string;
  new_part: string;
  reason: string;
  technician_id: string;
  repair_ticket_id: string;
  quality_impact: number; // -1 to +1
}

interface HealthMarker {
  marker_id: string;
  marker_type: 'positive' | 'negative' | 'neutral';
  category: string;
  description: string;
  detected_at: string;
  severity: number;
  associated_repairs: string[];
  genetic_correlation: number;
}

interface DeviceAncestry {
  device_model: string;
  device_generation: string;
  model_lineage: string[];
  known_genetic_issues: string[];
  model_siblings?: number;
  family_health_avg?: number;
}

interface Mutation {
  mutation_id: string;
  mutation_type: 'beneficial' | 'neutral' | 'harmful';
  timestamp: string;
  component_affected: string;
  description: string;
  origin: 'repair' | 'upgrade' | 'damage' | 'wear';
  reversible: boolean;
  impact_score: number;
}

interface RiskAllele {
  allele_id: string;
  risk_factor: string;
  probability: number;
  source: 'model' | 'history' | 'components' | 'environment';
  mitigation: string;
  detected_at: string;
}

interface VerificationBlock {
  block_number: number;
  timestamp: string;
  event_type: string;
  event_hash: string;
  previous_hash: string;
  technician_id?: string;
  verified: boolean;
}

interface DNAComparison {
  device_a: string;
  device_b: string;
  similarity_score: number;
  shared_traits: string[];
  divergent_traits: string[];
  common_issues: string[];
  recommendation: string;
}

interface GeneticReport {
  device_dna: DeviceDNA;
  health_assessment: HealthAssessment;
  predicted_traits: PredictedTrait[];
  recommendations: GeneticRecommendation[];
  provenance_verified: boolean;
}

interface HealthAssessment {
  overall_score: number;
  category: 'excellent' | 'good' | 'fair' | 'poor' | 'critical';
  strengths: string[];
  weaknesses: string[];
  genetic_predispositions: string[];
}

interface PredictedTrait {
  trait: string;
  probability: number;
  timeframe: string;
  preventable: boolean;
}

interface GeneticRecommendation {
  priority: number;
  category: string;
  recommendation: string;
  cost_estimate?: number;
  benefit: string;
}

const app = new Hono<{ Bindings: Env }>();

app.use('/*', cors());

// Known genetic issues by device model
const MODEL_GENETIC_ISSUES: Record<string, string[]> = {
  'iPhone 6': ['touch_disease', 'audio_ic_failure', 'battery_gate'],
  'iPhone 6 Plus': ['touch_disease', 'audio_ic_failure', 'bend_gate'],
  'iPhone 7': ['audio_ic_failure', 'loop_disease', 'home_button_failure'],
  'iPhone X': ['face_id_failure', 'oled_burn_in', 'sandwich_flexgate'],
  'iPhone 11': ['display_touch_issues', 'green_tint'],
  'iPhone 12': ['no_sound_speaker', 'ear_speaker_failure'],
  'MacBook Pro 2016': ['keyboard_failure', 'flexgate', 'battery_swell'],
  'MacBook Pro 2017': ['keyboard_failure', 'battery_swell'],
  'MacBook Pro 2018': ['t2_bridge_failure', 'keyboard_failure'],
  'MacBook Air 2018': ['display_cable_failure', 'keyboard_failure'],
};

// ==================== DNA Creation ====================

app.post('/dna/create', async (c) => {
  const { device_id, serial_number, imei, device_model, components, initial_state } = await c.req.json();

  // Generate unique DNA ID
  const dna_id = `DNA-${Date.now()}-${Math.random().toString(36).substring(7)}`;

  // Create hardware fingerprint
  const fingerprint = await generateFingerprint(device_id, serial_number, imei, components);

  // Initialize repair genome
  const genome: RepairGenome = {
    total_repairs: 0,
    repair_frequency: 0,
    dominant_issues: [],
    repair_success_rate: 1.0,
    technician_diversity: 0,
    parts_replaced_count: 0,
    total_repair_cost: 0,
    genome_complexity_score: 0,
  };

  // Create component lineage
  const lineage: ComponentLineage[] = components.map((comp: any, index: number) => ({
    component_type: comp.type,
    generation: 1,
    current_component: {
      part_number: comp.part_number,
      manufacturer: comp.manufacturer || 'OEM',
      quality_tier: 'OEM',
      install_date: initial_state?.manufacture_date || new Date().toISOString(),
      source: 'original',
      health_at_install: 100,
      current_health: 100,
      state_hash: generateHash(`${comp.part_number}-${comp.type}-gen1`),
    },
    ancestors: [],
    replacement_history: [],
    genetic_drift: 0,
  }));

  // Get ancestry information
  const ancestry: DeviceAncestry = {
    device_model,
    device_generation: extractGeneration(device_model),
    model_lineage: getModelLineage(device_model),
    known_genetic_issues: MODEL_GENETIC_ISSUES[device_model] || [],
  };

  // Initialize risk alleles based on model genetics
  const risk_alleles: RiskAllele[] = (MODEL_GENETIC_ISSUES[device_model] || []).map((issue, index) => ({
    allele_id: `RA-${index + 1}`,
    risk_factor: issue,
    probability: calculateInherentRisk(issue, device_model),
    source: 'model',
    mitigation: getMitigationStrategy(issue),
    detected_at: new Date().toISOString(),
  }));

  // Create genesis block
  const genesisBlock: VerificationBlock = {
    block_number: 0,
    timestamp: new Date().toISOString(),
    event_type: 'genesis',
    event_hash: generateHash(`genesis-${dna_id}-${Date.now()}`),
    previous_hash: '0'.repeat(64),
    verified: true,
  };

  const deviceDNA: DeviceDNA = {
    dna_id,
    device_id,
    serial_number,
    imei,
    created_at: new Date().toISOString(),
    last_updated: new Date().toISOString(),
    fingerprint,
    repair_genome: genome,
    component_lineage: lineage,
    health_markers: [],
    ancestry,
    mutations: [],
    risk_alleles,
    dna_hash: '',
    verification_chain: [genesisBlock],
  };

  // Calculate DNA hash
  deviceDNA.dna_hash = generateDNAHash(deviceDNA);

  // Store DNA
  await c.env.D1_DATABASE.prepare(`
    INSERT INTO device_dna (
      dna_id, device_id, serial_number, imei, dna_data, dna_hash, created_at, updated_at
    ) VALUES (?, ?, ?, ?, ?, ?, datetime('now'), datetime('now'))
  `).bind(dna_id, device_id, serial_number || null, imei || null, JSON.stringify(deviceDNA), deviceDNA.dna_hash).run();

  // Cache for quick access
  await c.env.REPAIR_DNA_KV.put(`dna:${device_id}`, JSON.stringify(deviceDNA), { expirationTtl: 86400 * 30 });

  return c.json({
    success: true,
    dna_id,
    device_id,
    dna_hash: deviceDNA.dna_hash,
    known_genetic_issues: ancestry.known_genetic_issues,
    initial_risk_alleles: risk_alleles.length,
  });
});

// ==================== DNA Retrieval ====================

app.get('/dna/:deviceId', async (c) => {
  const deviceId = c.req.param('deviceId');

  // Check cache first
  const cached = await c.env.REPAIR_DNA_KV.get(`dna:${deviceId}`);
  if (cached) {
    return c.json(JSON.parse(cached));
  }

  // Fetch from database
  const result = await c.env.D1_DATABASE.prepare(`
    SELECT dna_data FROM device_dna WHERE device_id = ? ORDER BY updated_at DESC LIMIT 1
  `).bind(deviceId).first();

  if (!result) {
    return c.json({ error: 'Device DNA not found' }, 404);
  }

  const dna = JSON.parse(result.dna_data as string);

  // Cache it
  await c.env.REPAIR_DNA_KV.put(`dna:${deviceId}`, JSON.stringify(dna), { expirationTtl: 86400 * 30 });

  return c.json(dna);
});

// ==================== Record Repair Mutation ====================

app.post('/dna/:deviceId/mutation', async (c) => {
  const deviceId = c.req.param('deviceId');
  const {
    repair_ticket_id,
    technician_id,
    repair_type,
    components_replaced,
    symptoms,
    outcome,
    cost
  } = await c.req.json();

  // Get current DNA
  const cached = await c.env.REPAIR_DNA_KV.get(`dna:${deviceId}`);
  if (!cached) {
    return c.json({ error: 'Device DNA not found - create DNA first' }, 404);
  }

  const dna: DeviceDNA = JSON.parse(cached);

  // Create mutation record
  const mutation: Mutation = {
    mutation_id: `MUT-${Date.now()}`,
    mutation_type: determineMutationType(repair_type, outcome),
    timestamp: new Date().toISOString(),
    component_affected: components_replaced?.[0]?.component_type || repair_type,
    description: `${repair_type} repair - ${outcome}`,
    origin: 'repair',
    reversible: false,
    impact_score: calculateMutationImpact(repair_type, outcome),
  };

  dna.mutations.push(mutation);

  // Update repair genome
  dna.repair_genome.total_repairs++;
  dna.repair_genome.total_repair_cost += cost || 0;
  dna.repair_genome.parts_replaced_count += components_replaced?.length || 0;

  // Update dominant issues
  const existingTrait = dna.repair_genome.dominant_issues.find(t => t.trait_name === repair_type);
  if (existingTrait) {
    existingTrait.occurrence_count++;
    existingTrait.last_occurrence = new Date().toISOString();
    if (existingTrait.occurrence_count >= 3) {
      existingTrait.inheritance_pattern = 'dominant';
    }
  } else {
    dna.repair_genome.dominant_issues.push({
      trait_name: repair_type,
      occurrence_count: 1,
      first_occurrence: new Date().toISOString(),
      last_occurrence: new Date().toISOString(),
      inheritance_pattern: 'recessive',
      associated_symptoms: symptoms || [],
    });
  }

  // Calculate repair frequency
  const daysSinceCreation = daysBetween(dna.created_at, new Date().toISOString());
  dna.repair_genome.repair_frequency = (dna.repair_genome.total_repairs / daysSinceCreation) * 365;

  // Update component lineage for replaced components
  for (const replaced of components_replaced || []) {
    const lineage = dna.component_lineage.find(l => l.component_type === replaced.component_type);
    if (lineage) {
      // Save current component to ancestors
      lineage.ancestors.push(lineage.current_component);

      // Create replacement event
      lineage.replacement_history.push({
        event_id: `REP-${Date.now()}`,
        timestamp: new Date().toISOString(),
        previous_part: lineage.current_component.part_number,
        new_part: replaced.new_part_number,
        reason: repair_type,
        technician_id,
        repair_ticket_id,
        quality_impact: calculateQualityImpact(lineage.current_component.quality_tier, replaced.quality_tier),
      });

      // Update current component
      lineage.current_component = {
        part_number: replaced.new_part_number,
        manufacturer: replaced.manufacturer,
        quality_tier: replaced.quality_tier || 'Unknown',
        install_date: new Date().toISOString(),
        source: replaced.source || 'repair',
        health_at_install: replaced.health || 100,
        current_health: replaced.health || 100,
        state_hash: generateHash(`${replaced.new_part_number}-gen${lineage.generation + 1}`),
      };

      lineage.generation++;

      // Calculate genetic drift
      lineage.genetic_drift = calculateGeneticDrift(lineage);
    }
  }

  // Add health marker if negative outcome
  if (outcome === 'partial' || outcome === 'failed') {
    dna.health_markers.push({
      marker_id: `HM-${Date.now()}`,
      marker_type: 'negative',
      category: repair_type,
      description: `${repair_type} repair ${outcome}`,
      detected_at: new Date().toISOString(),
      severity: outcome === 'failed' ? 0.8 : 0.4,
      associated_repairs: [repair_ticket_id],
      genetic_correlation: 0.5,
    });
  }

  // Update risk alleles based on repair
  await updateRiskAlleles(dna, repair_type, symptoms);

  // Add verification block
  const previousBlock = dna.verification_chain[dna.verification_chain.length - 1];
  const newBlock: VerificationBlock = {
    block_number: previousBlock.block_number + 1,
    timestamp: new Date().toISOString(),
    event_type: 'repair_mutation',
    event_hash: generateHash(`${repair_ticket_id}-${mutation.mutation_id}-${Date.now()}`),
    previous_hash: previousBlock.event_hash,
    technician_id,
    verified: true,
  };
  dna.verification_chain.push(newBlock);

  // Update DNA hash
  dna.last_updated = new Date().toISOString();
  dna.dna_hash = generateDNAHash(dna);

  // Calculate genome complexity
  dna.repair_genome.genome_complexity_score = calculateGenomeComplexity(dna);

  // Store updated DNA
  await c.env.D1_DATABASE.prepare(`
    UPDATE device_dna SET dna_data = ?, dna_hash = ?, updated_at = datetime('now')
    WHERE device_id = ?
  `).bind(JSON.stringify(dna), dna.dna_hash, deviceId).run();

  await c.env.REPAIR_DNA_KV.put(`dna:${deviceId}`, JSON.stringify(dna), { expirationTtl: 86400 * 30 });

  return c.json({
    success: true,
    mutation_id: mutation.mutation_id,
    mutation_type: mutation.mutation_type,
    new_dna_hash: dna.dna_hash,
    genome_complexity: dna.repair_genome.genome_complexity_score,
    verification_block: newBlock.block_number,
  });
});

// ==================== Genetic Report ====================

app.get('/dna/:deviceId/report', async (c) => {
  const deviceId = c.req.param('deviceId');

  const cached = await c.env.REPAIR_DNA_KV.get(`dna:${deviceId}`);
  if (!cached) {
    return c.json({ error: 'Device DNA not found' }, 404);
  }

  const dna: DeviceDNA = JSON.parse(cached);

  // Generate health assessment
  const healthAssessment = generateHealthAssessment(dna);

  // Predict future traits
  const predictedTraits = await predictFutureTraits(c.env, dna);

  // Generate recommendations
  const recommendations = generateGeneticRecommendations(dna, healthAssessment, predictedTraits);

  // Verify provenance chain
  const provenanceVerified = verifyProvenanceChain(dna);

  const report: GeneticReport = {
    device_dna: dna,
    health_assessment: healthAssessment,
    predicted_traits: predictedTraits,
    recommendations,
    provenance_verified: provenanceVerified,
  };

  return c.json(report);
});

// ==================== DNA Comparison ====================

app.post('/dna/compare', async (c) => {
  const { device_a, device_b } = await c.req.json();

  const [dnaA, dnaB] = await Promise.all([
    c.env.REPAIR_DNA_KV.get(`dna:${device_a}`),
    c.env.REPAIR_DNA_KV.get(`dna:${device_b}`),
  ]);

  if (!dnaA || !dnaB) {
    return c.json({ error: 'One or both device DNAs not found' }, 404);
  }

  const dna1: DeviceDNA = JSON.parse(dnaA);
  const dna2: DeviceDNA = JSON.parse(dnaB);

  // Compare genetic profiles
  const comparison = compareDNA(dna1, dna2);

  return c.json(comparison);
});

// ==================== Family Analysis ====================

app.get('/dna/family/:deviceModel', async (c) => {
  const deviceModel = c.req.param('deviceModel');

  // Get all devices of this model
  const devices = await c.env.D1_DATABASE.prepare(`
    SELECT dna_data FROM device_dna 
    WHERE json_extract(dna_data, '$.ancestry.device_model') LIKE ?
  `).bind(`%${deviceModel}%`).all();

  const familyAnalysis = analyzeFamilyGenetics(devices.results || [], deviceModel);

  return c.json({
    device_model: deviceModel,
    family_size: devices.results?.length || 0,
    known_genetic_issues: MODEL_GENETIC_ISSUES[deviceModel] || [],
    analysis: familyAnalysis,
  });
});

// ==================== Certificate of Authenticity ====================

app.get('/dna/:deviceId/certificate', async (c) => {
  const deviceId = c.req.param('deviceId');

  const cached = await c.env.REPAIR_DNA_KV.get(`dna:${deviceId}`);
  if (!cached) {
    return c.json({ error: 'Device DNA not found' }, 404);
  }

  const dna: DeviceDNA = JSON.parse(cached);

  // Generate certificate
  const certificate = {
    certificate_id: `CERT-${dna.dna_id}-${Date.now()}`,
    device_id: dna.device_id,
    serial_number: dna.serial_number,
    imei: dna.imei,
    dna_id: dna.dna_id,
    created_at: dna.created_at,
    verified_at: new Date().toISOString(),
    dna_hash: dna.dna_hash,
    provenance_verified: verifyProvenanceChain(dna),
    chain_length: dna.verification_chain.length,
    repair_history_summary: {
      total_repairs: dna.repair_genome.total_repairs,
      total_cost: dna.repair_genome.total_repair_cost,
      success_rate: dna.repair_genome.repair_success_rate,
    },
    component_authenticity: dna.component_lineage.map(l => ({
      component: l.component_type,
      current_tier: l.current_component.quality_tier,
      generation: l.generation,
      genetic_drift: l.genetic_drift,
    })),
    health_score: calculateOverallHealth(dna),
    digital_signature: generateCertificateSignature(dna),
  };

  return c.json(certificate);
});

// ==================== Health Trend Analysis ====================

app.get('/dna/:deviceId/trend', async (c) => {
  const deviceId = c.req.param('deviceId');

  const cached = await c.env.REPAIR_DNA_KV.get(`dna:${deviceId}`);
  if (!cached) {
    return c.json({ error: 'Device DNA not found' }, 404);
  }

  const dna: DeviceDNA = JSON.parse(cached);

  // Generate health trend from mutation and marker history
  const trend = generateHealthTrend(dna);

  return c.json({
    device_id: deviceId,
    trend_data: trend,
    current_health: calculateOverallHealth(dna),
    trajectory: trend.length > 1 ? (trend[trend.length - 1].health > trend[0].health ? 'improving' : 'declining') : 'stable',
  });
});

// ==================== Bulk DNA Operations ====================

app.post('/dna/bulk/analyze', async (c) => {
  const { device_ids } = await c.req.json();

  const results = await Promise.all(
    device_ids.map(async (deviceId: string) => {
      const cached = await c.env.REPAIR_DNA_KV.get(`dna:${deviceId}`);
      if (!cached) return { device_id: deviceId, status: 'not_found' };

      const dna: DeviceDNA = JSON.parse(cached);
      return {
        device_id: deviceId,
        status: 'analyzed',
        health_score: calculateOverallHealth(dna),
        risk_score: calculateRiskScore(dna),
        genome_complexity: dna.repair_genome.genome_complexity_score,
        provenance_verified: verifyProvenanceChain(dna),
      };
    })
  );

  return c.json({
    total_analyzed: results.filter(r => r.status === 'analyzed').length,
    not_found: results.filter(r => r.status === 'not_found').length,
    results,
    fleet_health_avg: results.reduce((sum, r) => sum + ((r as any).health_score || 0), 0) / results.length,
  });
});

// ==================== Helper Functions ====================

async function generateFingerprint(
  deviceId: string,
  serialNumber: string | undefined,
  imei: string | undefined,
  components: any[]
): Promise<DeviceFingerprint> {
  const componentSignatures: ComponentSignature[] = components.map(comp => ({
    component_type: comp.type,
    original_part_number: comp.part_number,
    original_manufacturer: comp.manufacturer || 'OEM',
    original_date_code: comp.date_code,
    original_serial: comp.serial,
    signature_hash: generateHash(`${comp.part_number}-${comp.type}-${deviceId}`),
  }));

  const hardwareSignature = generateHash(
    `${deviceId}-${serialNumber || ''}-${imei || ''}-${componentSignatures.map(c => c.signature_hash).join('')}`
  );

  return {
    hardware_signature: hardwareSignature,
    original_components: componentSignatures,
    unique_identifiers: {
      device_id: deviceId,
      ...(serialNumber && { serial_number: serialNumber }),
      ...(imei && { imei }),
    },
  };
}

function generateHash(input: string): string {
  // Simple hash for demo - in production use crypto.subtle
  let hash = 0;
  for (let i = 0; i < input.length; i++) {
    const char = input.charCodeAt(i);
    hash = ((hash << 5) - hash) + char;
    hash = hash & hash;
  }
  return Math.abs(hash).toString(16).padStart(16, '0');
}

function generateDNAHash(dna: DeviceDNA): string {
  const hashInput = JSON.stringify({
    fingerprint: dna.fingerprint,
    genome: dna.repair_genome,
    lineage: dna.component_lineage.map(l => l.current_component.state_hash),
    mutations: dna.mutations.map(m => m.mutation_id),
    lastBlock: dna.verification_chain[dna.verification_chain.length - 1]?.event_hash,
  });
  return generateHash(hashInput);
}

function extractGeneration(model: string): string {
  const match = model.match(/\d+/);
  return match ? match[0] : 'Unknown';
}

function getModelLineage(model: string): string[] {
  // Return known model lineage
  if (model.includes('iPhone 14')) return ['iPhone', 'iPhone 13', 'iPhone 14'];
  if (model.includes('iPhone 13')) return ['iPhone', 'iPhone 12', 'iPhone 13'];
  if (model.includes('MacBook Pro')) return ['MacBook', 'MacBook Pro'];
  return [model];
}

function calculateInherentRisk(issue: string, model: string): number {
  // Known high-risk issues
  const highRiskIssues = ['touch_disease', 'audio_ic_failure', 'flexgate', 't2_bridge_failure'];
  const mediumRiskIssues = ['keyboard_failure', 'battery_swell', 'oled_burn_in'];

  if (highRiskIssues.includes(issue)) return 0.7;
  if (mediumRiskIssues.includes(issue)) return 0.5;
  return 0.3;
}

function getMitigationStrategy(issue: string): string {
  const strategies: Record<string, string> = {
    'touch_disease': 'Reinforce IC with underfill, consider preemptive reball',
    'audio_ic_failure': 'Monitor audio function, reball or replace IC if symptoms appear',
    'keyboard_failure': 'Keep keyboard clean, consider keyboard cover or external keyboard',
    'flexgate': 'Avoid extreme display angles, consider flex cable replacement',
    'battery_swell': 'Monitor battery health, replace at 80% capacity',
    'oled_burn_in': 'Use dark mode, avoid static images, reduce brightness',
  };
  return strategies[issue] || 'Monitor for symptoms and address promptly';
}

function determineMutationType(repairType: string, outcome: string): 'beneficial' | 'neutral' | 'harmful' {
  if (outcome === 'failed') return 'harmful';
  if (outcome === 'partial') return 'neutral';

  const beneficialRepairs = ['battery', 'upgrade', 'thermal_paste', 'cleaning'];
  if (beneficialRepairs.some(r => repairType.toLowerCase().includes(r))) return 'beneficial';

  return 'neutral';
}

function calculateMutationImpact(repairType: string, outcome: string): number {
  if (outcome === 'failed') return -0.5;
  if (outcome === 'partial') return -0.1;

  const impactfulRepairs: Record<string, number> = {
    'motherboard': 0.8,
    'display': 0.6,
    'battery': 0.5,
    'charging': 0.4,
  };

  for (const [key, impact] of Object.entries(impactfulRepairs)) {
    if (repairType.toLowerCase().includes(key)) return impact;
  }

  return 0.3;
}

function calculateQualityImpact(previousTier: string, newTier: string): number {
  const tierOrder = ['OEM', 'OEM-Equivalent', 'Aftermarket', 'Refurbished', 'Unknown'];
  const previousIndex = tierOrder.indexOf(previousTier);
  const newIndex = tierOrder.indexOf(newTier);

  return (previousIndex - newIndex) / tierOrder.length;
}

function calculateGeneticDrift(lineage: ComponentLineage): number {
  if (lineage.ancestors.length === 0) return 0;

  let drift = 0;
  for (const replacement of lineage.replacement_history) {
    drift += Math.abs(replacement.quality_impact);
  }

  return Math.min(1, drift / lineage.generation);
}

async function updateRiskAlleles(dna: DeviceDNA, repairType: string, symptoms: string[]): Promise<void> {
  // Add new risk alleles based on repair history
  const existingAllele = dna.risk_alleles.find(a => a.risk_factor === repairType);

  if (existingAllele) {
    existingAllele.probability = Math.min(0.95, existingAllele.probability + 0.1);
  } else {
    dna.risk_alleles.push({
      allele_id: `RA-${dna.risk_alleles.length + 1}`,
      risk_factor: repairType,
      probability: 0.3,
      source: 'history',
      mitigation: `Monitor for ${repairType} issues`,
      detected_at: new Date().toISOString(),
    });
  }
}

function calculateGenomeComplexity(dna: DeviceDNA): number {
  const factors = [
    dna.repair_genome.total_repairs * 0.1,
    dna.mutations.length * 0.05,
    dna.health_markers.length * 0.1,
    dna.component_lineage.reduce((sum, l) => sum + l.generation, 0) * 0.05,
    dna.risk_alleles.length * 0.1,
  ];

  return Math.min(1, factors.reduce((sum, f) => sum + f, 0));
}

function generateHealthAssessment(dna: DeviceDNA): HealthAssessment {
  const overallScore = calculateOverallHealth(dna);

  const strengths: string[] = [];
  const weaknesses: string[] = [];

  // Analyze components
  for (const lineage of dna.component_lineage) {
    if (lineage.current_component.quality_tier === 'OEM' && lineage.generation === 1) {
      strengths.push(`Original ${lineage.component_type} intact`);
    }
    if (lineage.current_component.current_health < 70) {
      weaknesses.push(`${lineage.component_type} health degraded`);
    }
    if (lineage.genetic_drift > 0.5) {
      weaknesses.push(`${lineage.component_type} significantly modified from original`);
    }
  }

  // Analyze mutations
  const harmfulMutations = dna.mutations.filter(m => m.mutation_type === 'harmful');
  if (harmfulMutations.length > 0) {
    weaknesses.push(`${harmfulMutations.length} harmful mutations detected`);
  }

  const beneficialMutations = dna.mutations.filter(m => m.mutation_type === 'beneficial');
  if (beneficialMutations.length > 0) {
    strengths.push(`${beneficialMutations.length} beneficial improvements made`);
  }

  // Genetic predispositions
  const predispositions = dna.risk_alleles
    .filter(a => a.probability > 0.5)
    .map(a => a.risk_factor);

  return {
    overall_score: overallScore,
    category: getCategoryFromScore(overallScore),
    strengths,
    weaknesses,
    genetic_predispositions: predispositions,
  };
}

function calculateOverallHealth(dna: DeviceDNA): number {
  let health = 100;

  // Factor in component health
  const avgComponentHealth = dna.component_lineage.reduce((sum, l) =>
    sum + l.current_component.current_health, 0) / dna.component_lineage.length;
  health = avgComponentHealth;

  // Factor in repair frequency (high frequency = lower health)
  if (dna.repair_genome.repair_frequency > 2) {
    health -= (dna.repair_genome.repair_frequency - 2) * 5;
  }

  // Factor in harmful mutations
  const harmfulMutations = dna.mutations.filter(m => m.mutation_type === 'harmful');
  health -= harmfulMutations.length * 5;

  // Factor in negative health markers
  const negativeMarkers = dna.health_markers.filter(m => m.marker_type === 'negative');
  health -= negativeMarkers.reduce((sum, m) => sum + m.severity * 10, 0);

  // Factor in high-risk alleles
  const highRiskAlleles = dna.risk_alleles.filter(a => a.probability > 0.7);
  health -= highRiskAlleles.length * 3;

  return Math.max(0, Math.min(100, health));
}

function getCategoryFromScore(score: number): 'excellent' | 'good' | 'fair' | 'poor' | 'critical' {
  if (score >= 90) return 'excellent';
  if (score >= 75) return 'good';
  if (score >= 50) return 'fair';
  if (score >= 25) return 'poor';
  return 'critical';
}

async function predictFutureTraits(env: Env, dna: DeviceDNA): Promise<PredictedTrait[]> {
  const predictions: PredictedTrait[] = [];

  // Based on dominant issues and repair frequency
  for (const trait of dna.repair_genome.dominant_issues) {
    if (trait.occurrence_count >= 2) {
      predictions.push({
        trait: trait.trait_name,
        probability: Math.min(0.9, trait.occurrence_count * 0.3),
        timeframe: '6-12 months',
        preventable: true,
      });
    }
  }

  // Based on risk alleles
  for (const allele of dna.risk_alleles) {
    if (allele.probability > 0.5) {
      predictions.push({
        trait: allele.risk_factor,
        probability: allele.probability,
        timeframe: '12-24 months',
        preventable: allele.source !== 'model',
      });
    }
  }

  // Based on component age
  for (const lineage of dna.component_lineage) {
    if (lineage.current_component.current_health < 50) {
      predictions.push({
        trait: `${lineage.component_type}_failure`,
        probability: (100 - lineage.current_component.current_health) / 100,
        timeframe: '3-6 months',
        preventable: true,
      });
    }
  }

  return predictions.sort((a, b) => b.probability - a.probability).slice(0, 10);
}

function generateGeneticRecommendations(
  dna: DeviceDNA,
  health: HealthAssessment,
  predictions: PredictedTrait[]
): GeneticRecommendation[] {
  const recommendations: GeneticRecommendation[] = [];

  // Component-based recommendations
  for (const lineage of dna.component_lineage) {
    if (lineage.current_component.current_health < 70) {
      recommendations.push({
        priority: lineage.current_component.current_health < 50 ? 1 : 2,
        category: lineage.component_type,
        recommendation: `Schedule ${lineage.component_type} inspection or replacement`,
        cost_estimate: getReplacementCost(lineage.component_type),
        benefit: `Prevent ${lineage.component_type} failure and potential cascade damage`,
      });
    }
  }

  // Prediction-based recommendations
  for (const prediction of predictions.filter(p => p.preventable && p.probability > 0.6)) {
    recommendations.push({
      priority: prediction.probability > 0.8 ? 1 : 2,
      category: 'preventive',
      recommendation: `Proactively address ${prediction.trait} risk`,
      benefit: `Reduce ${Math.round(prediction.probability * 100)}% failure probability`,
    });
  }

  // Genetic predisposition recommendations
  for (const predisposition of health.genetic_predispositions) {
    const allele = dna.risk_alleles.find(a => a.risk_factor === predisposition);
    if (allele) {
      recommendations.push({
        priority: 3,
        category: 'genetic',
        recommendation: allele.mitigation,
        benefit: `Mitigate inherent ${predisposition} vulnerability`,
      });
    }
  }

  return recommendations.sort((a, b) => a.priority - b.priority).slice(0, 10);
}

function getReplacementCost(componentType: string): number {
  const costs: Record<string, number> = {
    battery: 49,
    display: 199,
    charging_port: 79,
    motherboard: 299,
    speaker: 59,
    camera: 149,
  };
  return costs[componentType] || 99;
}

function verifyProvenanceChain(dna: DeviceDNA): boolean {
  for (let i = 1; i < dna.verification_chain.length; i++) {
    if (dna.verification_chain[i].previous_hash !== dna.verification_chain[i - 1].event_hash) {
      return false;
    }
  }
  return true;
}

function compareDNA(dna1: DeviceDNA, dna2: DeviceDNA): DNAComparison {
  const sharedTraits: string[] = [];
  const divergentTraits: string[] = [];
  const commonIssues: string[] = [];

  // Compare dominant issues
  for (const trait1 of dna1.repair_genome.dominant_issues) {
    const matching = dna2.repair_genome.dominant_issues.find(t => t.trait_name === trait1.trait_name);
    if (matching) {
      sharedTraits.push(trait1.trait_name);
    } else {
      divergentTraits.push(`${trait1.trait_name} (device A only)`);
    }
  }

  for (const trait2 of dna2.repair_genome.dominant_issues) {
    if (!dna1.repair_genome.dominant_issues.find(t => t.trait_name === trait2.trait_name)) {
      divergentTraits.push(`${trait2.trait_name} (device B only)`);
    }
  }

  // Check for common genetic issues
  for (const issue of dna1.ancestry.known_genetic_issues) {
    if (dna2.ancestry.known_genetic_issues.includes(issue)) {
      commonIssues.push(issue);
    }
  }

  // Calculate similarity
  const totalTraits = new Set([
    ...dna1.repair_genome.dominant_issues.map(t => t.trait_name),
    ...dna2.repair_genome.dominant_issues.map(t => t.trait_name),
  ]).size;

  const similarity = totalTraits > 0 ? sharedTraits.length / totalTraits : 1;

  return {
    device_a: dna1.device_id,
    device_b: dna2.device_id,
    similarity_score: similarity,
    shared_traits: sharedTraits,
    divergent_traits: divergentTraits,
    common_issues: commonIssues,
    recommendation: similarity > 0.7
      ? 'These devices have similar repair profiles - solutions from one may apply to the other'
      : 'These devices have different repair profiles - individual assessment recommended',
  };
}

function analyzeFamilyGenetics(devices: any[], model: string): any {
  const issues: Record<string, number> = {};
  const avgHealthScores: number[] = [];

  for (const device of devices) {
    const dna: DeviceDNA = JSON.parse(device.dna_data);
    avgHealthScores.push(calculateOverallHealth(dna));

    for (const trait of dna.repair_genome.dominant_issues) {
      issues[trait.trait_name] = (issues[trait.trait_name] || 0) + 1;
    }
  }

  return {
    average_health: avgHealthScores.length > 0
      ? avgHealthScores.reduce((a, b) => a + b) / avgHealthScores.length
      : 0,
    most_common_issues: Object.entries(issues)
      .sort(([, a], [, b]) => b - a)
      .slice(0, 5)
      .map(([issue, count]) => ({ issue, occurrence_rate: count / devices.length })),
    health_distribution: {
      excellent: avgHealthScores.filter(h => h >= 90).length,
      good: avgHealthScores.filter(h => h >= 75 && h < 90).length,
      fair: avgHealthScores.filter(h => h >= 50 && h < 75).length,
      poor: avgHealthScores.filter(h => h < 50).length,
    },
  };
}

function generateHealthTrend(dna: DeviceDNA): { date: string; health: number; event: string }[] {
  const trend: { date: string; health: number; event: string }[] = [];

  // Start with creation
  trend.push({
    date: dna.created_at,
    health: 100,
    event: 'Device registered',
  });

  // Add mutation events
  for (const mutation of dna.mutations) {
    const lastHealth = trend[trend.length - 1].health;
    const impact = mutation.mutation_type === 'beneficial' ? 5 : mutation.mutation_type === 'harmful' ? -10 : -2;

    trend.push({
      date: mutation.timestamp,
      health: Math.max(0, Math.min(100, lastHealth + impact)),
      event: mutation.description,
    });
  }

  // Sort by date
  trend.sort((a, b) => new Date(a.date).getTime() - new Date(b.date).getTime());

  return trend;
}

function calculateRiskScore(dna: DeviceDNA): number {
  let risk = 0;

  // Factor in high-probability risk alleles
  for (const allele of dna.risk_alleles) {
    risk += allele.probability * 0.2;
  }

  // Factor in repair frequency
  risk += Math.min(0.3, dna.repair_genome.repair_frequency * 0.1);

  // Factor in harmful mutations
  const harmfulMutations = dna.mutations.filter(m => m.mutation_type === 'harmful');
  risk += harmfulMutations.length * 0.1;

  // Factor in low component health
  const lowHealthComponents = dna.component_lineage.filter(l => l.current_component.current_health < 50);
  risk += lowHealthComponents.length * 0.15;

  return Math.min(1, risk);
}

function generateCertificateSignature(dna: DeviceDNA): string {
  return generateHash(
    `${dna.dna_id}-${dna.dna_hash}-${dna.verification_chain.length}-${new Date().toISOString()}`
  );
}

function daysBetween(date1: string, date2: string): number {
  const d1 = new Date(date1);
  const d2 = new Date(date2);
  return Math.max(1, Math.round(Math.abs(d2.getTime() - d1.getTime()) / (1000 * 60 * 60 * 24)));
}

export default app;
