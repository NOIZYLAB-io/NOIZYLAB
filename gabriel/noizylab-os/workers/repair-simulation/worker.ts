/**
 * NoizyLab OS - Repair Simulation Worker
 * Digital Twin Repair Testing Engine
 * 
 * Features:
 * - Digital twin device modeling
 * - Virtual repair scenario simulation
 * - Outcome probability prediction
 * - Risk assessment before repair
 * - What-if analysis engine
 * - Technician training simulations
 * - Repair strategy optimization
 * - Failure cascade prediction
 */

import { Hono } from 'hono';

interface Env {
  SIMULATION_KV: KVNamespace;
  DB: D1Database;
  AI: Ai;
}

interface DeviceTwin {
  id: string;
  deviceType: string;
  model: string;
  manufacturer: string;
  components: ComponentState[];
  age: number;
  usageHours: number;
  environmentalFactors: EnvironmentFactors;
  repairHistory: RepairRecord[];
  currentCondition: number;
  failureProbabilities: Map<string, number>;
}

interface ComponentState {
  id: string;
  name: string;
  health: number;
  wearLevel: number;
  dependencies: string[];
  failureModes: FailureMode[];
  replacementHistory: Date[];
  mtbf: number;
  currentStress: number;
}

interface FailureMode {
  id: string;
  name: string;
  probability: number;
  severity: number;
  cascadeRisk: string[];
  symptoms: string[];
  preventiveMeasures: string[];
}

interface EnvironmentFactors {
  temperature: number;
  humidity: number;
  dustLevel: number;
  vibration: number;
  electricalStability: number;
}

interface RepairRecord {
  id: string;
  date: Date;
  type: string;
  components: string[];
  outcome: 'success' | 'partial' | 'failed';
  technicianSkillLevel: number;
  duration: number;
  cost: number;
}

interface SimulationScenario {
  id: string;
  name: string;
  repairAction: RepairAction;
  constraints: SimulationConstraints;
  iterations: number;
}

interface RepairAction {
  type: 'replace' | 'repair' | 'refurbish' | 'clean' | 'calibrate' | 'software_update';
  targetComponents: string[];
  tools: string[];
  estimatedDuration: number;
  technicianSkillRequired: number;
  partsNeeded: PartRequirement[];
}

interface PartRequirement {
  partId: string;
  quantity: number;
  quality: 'oem' | 'aftermarket' | 'refurbished';
  criticalPath: boolean;
}

interface SimulationConstraints {
  maxBudget?: number;
  maxTime?: number;
  availableSkillLevel: number;
  availableParts: string[];
  environmentalConditions: EnvironmentFactors;
}

interface SimulationResult {
  scenarioId: string;
  successProbability: number;
  expectedOutcome: SimulationOutcome;
  riskAssessment: RiskAssessment;
  alternativeStrategies: AlternativeStrategy[];
  trainingRecommendations: TrainingRecommendation[];
  costAnalysis: CostAnalysis;
  timelineAnalysis: TimelineAnalysis;
  cascadeAnalysis: CascadeAnalysis;
}

interface SimulationOutcome {
  deviceHealthAfter: number;
  componentHealthAfter: Map<string, number>;
  expectedLifespan: number;
  recurringIssueRisk: number;
  customerSatisfactionPrediction: number;
}

interface RiskAssessment {
  overallRisk: 'low' | 'medium' | 'high' | 'critical';
  riskScore: number;
  riskFactors: RiskFactor[];
  mitigationStrategies: string[];
  worstCaseScenario: string;
  bestCaseScenario: string;
}

interface RiskFactor {
  factor: string;
  probability: number;
  impact: number;
  riskScore: number;
  mitigation: string;
}

interface AlternativeStrategy {
  name: string;
  description: string;
  successProbability: number;
  cost: number;
  duration: number;
  tradeoffs: string[];
}

interface TrainingRecommendation {
  skill: string;
  currentLevel: number;
  requiredLevel: number;
  trainingModule: string;
  estimatedTrainingTime: number;
  impactOnSuccess: number;
}

interface CostAnalysis {
  laborCost: number;
  partsCost: number;
  toolsCost: number;
  overheadCost: number;
  totalCost: number;
  roi: number;
  breakEvenTime: number;
  costVariance: { min: number; max: number; expected: number };
}

interface TimelineAnalysis {
  estimatedDuration: number;
  bestCase: number;
  worstCase: number;
  criticalPath: CriticalPathStep[];
  parallelizableSteps: string[];
  bottlenecks: string[];
}

interface CriticalPathStep {
  step: string;
  duration: number;
  dependencies: string[];
  riskLevel: number;
}

interface CascadeAnalysis {
  cascadeRisk: number;
  affectedComponents: string[];
  cascadeSequence: CascadeEvent[];
  containmentStrategies: string[];
}

interface CascadeEvent {
  component: string;
  failureMode: string;
  triggerProbability: number;
  timeToFailure: number;
  impactSeverity: number;
}

const app = new Hono<{ Bindings: Env }>();

// ==================== DIGITAL TWIN MANAGEMENT ====================

app.post('/twin/create', async (c) => {
  const { deviceId, deviceType, model, manufacturer, specifications } = await c.req.json();
  
  // Create digital twin from device specifications
  const twin: DeviceTwin = {
    id: `twin_${deviceId}`,
    deviceType,
    model,
    manufacturer,
    components: await generateComponentTree(c.env, deviceType, model, specifications),
    age: specifications?.age || 0,
    usageHours: specifications?.usageHours || 0,
    environmentalFactors: specifications?.environment || {
      temperature: 25,
      humidity: 50,
      dustLevel: 0.2,
      vibration: 0.1,
      electricalStability: 0.95
    },
    repairHistory: [],
    currentCondition: 100,
    failureProbabilities: new Map()
  };
  
  // Calculate initial failure probabilities
  twin.failureProbabilities = await calculateFailureProbabilities(c.env, twin);
  
  // Store twin
  await c.env.SIMULATION_KV.put(`twin:${deviceId}`, JSON.stringify(twin));
  
  // Store in D1 for analytics
  await c.env.DB.prepare(`
    INSERT INTO digital_twins (id, device_id, device_type, model, manufacturer, components, created_at)
    VALUES (?, ?, ?, ?, ?, ?, datetime('now'))
  `).bind(
    twin.id,
    deviceId,
    deviceType,
    model,
    manufacturer,
    JSON.stringify(twin.components)
  ).run();
  
  return c.json({
    success: true,
    twin: {
      id: twin.id,
      componentCount: twin.components.length,
      initialCondition: twin.currentCondition,
      failureProbabilities: Object.fromEntries(twin.failureProbabilities)
    }
  });
});

app.get('/twin/:deviceId', async (c) => {
  const deviceId = c.req.param('deviceId');
  const twinJson = await c.env.SIMULATION_KV.get(`twin:${deviceId}`);
  
  if (!twinJson) {
    return c.json({ error: 'Digital twin not found' }, 404);
  }
  
  const twin: DeviceTwin = JSON.parse(twinJson);
  
  return c.json({
    twin,
    healthSummary: generateHealthSummary(twin),
    riskAreas: identifyRiskAreas(twin)
  });
});

app.put('/twin/:deviceId/update', async (c) => {
  const deviceId = c.req.param('deviceId');
  const updates = await c.req.json();
  
  const twinJson = await c.env.SIMULATION_KV.get(`twin:${deviceId}`);
  if (!twinJson) {
    return c.json({ error: 'Digital twin not found' }, 404);
  }
  
  let twin: DeviceTwin = JSON.parse(twinJson);
  
  // Apply updates (component states, environmental factors, etc.)
  if (updates.componentUpdates) {
    for (const update of updates.componentUpdates) {
      const component = twin.components.find(c => c.id === update.componentId);
      if (component) {
        Object.assign(component, update.changes);
      }
    }
  }
  
  if (updates.environmentalFactors) {
    Object.assign(twin.environmentalFactors, updates.environmentalFactors);
  }
  
  if (updates.repairRecord) {
    twin.repairHistory.push(updates.repairRecord);
  }
  
  // Recalculate probabilities
  twin.failureProbabilities = await calculateFailureProbabilities(c.env, twin);
  
  // Store updated twin
  await c.env.SIMULATION_KV.put(`twin:${deviceId}`, JSON.stringify(twin));
  
  return c.json({
    success: true,
    updatedTwin: twin,
    newRiskAssessment: identifyRiskAreas(twin)
  });
});

// ==================== REPAIR SIMULATION ====================

app.post('/simulate', async (c) => {
  const scenario: SimulationScenario = await c.req.json();
  
  // Get the digital twin
  const twinId = scenario.name.split('_')[0];
  const twinJson = await c.env.SIMULATION_KV.get(`twin:${twinId}`);
  
  if (!twinJson) {
    return c.json({ error: 'Digital twin not found' }, 404);
  }
  
  const twin: DeviceTwin = JSON.parse(twinJson);
  
  // Run Monte Carlo simulation
  const results = await runMonteCarloSimulation(c.env, twin, scenario);
  
  // Generate comprehensive analysis
  const simulationResult: SimulationResult = {
    scenarioId: scenario.id,
    successProbability: results.successRate,
    expectedOutcome: await predictOutcome(c.env, twin, scenario, results),
    riskAssessment: await assessRisks(c.env, twin, scenario, results),
    alternativeStrategies: await generateAlternatives(c.env, twin, scenario),
    trainingRecommendations: generateTrainingRecommendations(scenario.constraints.availableSkillLevel, scenario.repairAction.technicianSkillRequired),
    costAnalysis: await analyzeCosts(c.env, scenario, results),
    timelineAnalysis: analyzeTimeline(scenario, results),
    cascadeAnalysis: await analyzeCascadeRisk(c.env, twin, scenario)
  };
  
  // Store simulation result
  await c.env.DB.prepare(`
    INSERT INTO simulation_results (scenario_id, twin_id, success_probability, risk_score, cost_estimate, created_at)
    VALUES (?, ?, ?, ?, ?, datetime('now'))
  `).bind(
    scenario.id,
    twinId,
    simulationResult.successProbability,
    simulationResult.riskAssessment.riskScore,
    simulationResult.costAnalysis.totalCost
  ).run();
  
  return c.json(simulationResult);
});

app.post('/simulate/whatif', async (c) => {
  const { deviceId, scenarios } = await c.req.json();
  
  const twinJson = await c.env.SIMULATION_KV.get(`twin:${deviceId}`);
  if (!twinJson) {
    return c.json({ error: 'Digital twin not found' }, 404);
  }
  
  const twin: DeviceTwin = JSON.parse(twinJson);
  
  // Run all what-if scenarios in parallel
  const results = await Promise.all(
    scenarios.map(async (scenario: SimulationScenario) => {
      const simResults = await runMonteCarloSimulation(c.env, twin, scenario);
      return {
        scenarioName: scenario.name,
        successProbability: simResults.successRate,
        expectedCost: simResults.averageCost,
        expectedDuration: simResults.averageDuration,
        riskLevel: simResults.riskLevel
      };
    })
  );
  
  // Rank scenarios
  const rankedScenarios = results.sort((a, b) => {
    // Score based on success probability, cost, and risk
    const scoreA = a.successProbability * 0.5 - (a.expectedCost / 1000) * 0.3 - (a.riskLevel === 'high' ? 0.2 : a.riskLevel === 'medium' ? 0.1 : 0);
    const scoreB = b.successProbability * 0.5 - (b.expectedCost / 1000) * 0.3 - (b.riskLevel === 'high' ? 0.2 : b.riskLevel === 'medium' ? 0.1 : 0);
    return scoreB - scoreA;
  });
  
  return c.json({
    deviceId,
    scenarioCount: scenarios.length,
    rankedScenarios,
    recommendation: rankedScenarios[0],
    comparisonMatrix: generateComparisonMatrix(results)
  });
});

app.post('/simulate/cascade', async (c) => {
  const { deviceId, failureComponent, propagationDepth = 3 } = await c.req.json();
  
  const twinJson = await c.env.SIMULATION_KV.get(`twin:${deviceId}`);
  if (!twinJson) {
    return c.json({ error: 'Digital twin not found' }, 404);
  }
  
  const twin: DeviceTwin = JSON.parse(twinJson);
  
  // Simulate failure cascade
  const cascadeSimulation = await simulateFailureCascade(c.env, twin, failureComponent, propagationDepth);
  
  return c.json({
    initialFailure: failureComponent,
    cascadeDepth: propagationDepth,
    affectedComponents: cascadeSimulation.affectedComponents,
    cascadeTimeline: cascadeSimulation.timeline,
    totalDamageEstimate: cascadeSimulation.totalDamage,
    containmentOptions: cascadeSimulation.containmentOptions,
    preventiveMeasures: cascadeSimulation.preventiveMeasures
  });
});

// ==================== TRAINING SIMULATIONS ====================

app.post('/training/scenario', async (c) => {
  const { deviceType, difficulty, focusAreas, technicianId } = await c.req.json();
  
  // Generate training scenario
  const trainingScenario = await generateTrainingScenario(c.env, deviceType, difficulty, focusAreas);
  
  // Create virtual device with intentional issues
  const trainingTwin = await createTrainingTwin(c.env, deviceType, trainingScenario.issues);
  
  // Store training session
  const sessionId = `training_${Date.now()}_${technicianId}`;
  await c.env.SIMULATION_KV.put(`training:${sessionId}`, JSON.stringify({
    sessionId,
    technicianId,
    scenario: trainingScenario,
    twin: trainingTwin,
    startTime: Date.now(),
    actions: [],
    hints: trainingScenario.hints,
    expectedSolution: trainingScenario.solution
  }));
  
  return c.json({
    sessionId,
    deviceType,
    difficulty,
    symptoms: trainingScenario.symptoms,
    availableTools: trainingScenario.availableTools,
    timeLimit: trainingScenario.timeLimit,
    objectiveDescription: trainingScenario.objective
  });
});

app.post('/training/:sessionId/action', async (c) => {
  const sessionId = c.req.param('sessionId');
  const action = await c.req.json();
  
  const sessionJson = await c.env.SIMULATION_KV.get(`training:${sessionId}`);
  if (!sessionJson) {
    return c.json({ error: 'Training session not found' }, 404);
  }
  
  const session = JSON.parse(sessionJson);
  
  // Record action
  session.actions.push({
    ...action,
    timestamp: Date.now()
  });
  
  // Simulate action result on training twin
  const actionResult = await simulateTrainingAction(c.env, session.twin, action);
  
  // Check if problem is solved
  const isSolved = checkSolution(session.twin, session.expectedSolution, session.actions);
  
  // Update session
  await c.env.SIMULATION_KV.put(`training:${sessionId}`, JSON.stringify(session));
  
  return c.json({
    actionResult,
    deviceStateUpdate: actionResult.stateChanges,
    feedback: actionResult.feedback,
    hintAvailable: session.actions.length > 5 && !isSolved,
    isSolved,
    score: isSolved ? calculateTrainingScore(session) : null
  });
});

app.get('/training/:sessionId/hint', async (c) => {
  const sessionId = c.req.param('sessionId');
  
  const sessionJson = await c.env.SIMULATION_KV.get(`training:${sessionId}`);
  if (!sessionJson) {
    return c.json({ error: 'Training session not found' }, 404);
  }
  
  const session = JSON.parse(sessionJson);
  const hintIndex = Math.min(Math.floor(session.actions.length / 5), session.hints.length - 1);
  
  return c.json({
    hint: session.hints[hintIndex],
    hintsRemaining: session.hints.length - hintIndex - 1,
    penaltyApplied: true
  });
});

app.post('/training/:sessionId/complete', async (c) => {
  const sessionId = c.req.param('sessionId');
  
  const sessionJson = await c.env.SIMULATION_KV.get(`training:${sessionId}`);
  if (!sessionJson) {
    return c.json({ error: 'Training session not found' }, 404);
  }
  
  const session = JSON.parse(sessionJson);
  session.endTime = Date.now();
  
  // Calculate comprehensive score
  const score = calculateTrainingScore(session);
  const analysis = analyzeTrainingPerformance(session);
  
  // Store results
  await c.env.DB.prepare(`
    INSERT INTO training_results (session_id, technician_id, device_type, difficulty, score, duration, actions_count, hints_used, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, datetime('now'))
  `).bind(
    sessionId,
    session.technicianId,
    session.scenario.deviceType,
    session.scenario.difficulty,
    score.total,
    session.endTime - session.startTime,
    session.actions.length,
    analysis.hintsUsed
  ).run();
  
  return c.json({
    sessionId,
    score,
    analysis,
    recommendations: generateSkillRecommendations(analysis),
    certificateEarned: score.total >= 85
  });
});

// ==================== HELPER FUNCTIONS ====================

async function generateComponentTree(env: Env, deviceType: string, model: string, specs: any): Promise<ComponentState[]> {
  // Generate component tree based on device type
  const componentTemplates: Record<string, ComponentState[]> = {
    smartphone: [
      { id: 'display', name: 'Display Assembly', health: 100, wearLevel: 0, dependencies: ['motherboard'], failureModes: [], replacementHistory: [], mtbf: 25000, currentStress: 0.2 },
      { id: 'battery', name: 'Battery', health: 100, wearLevel: 0, dependencies: [], failureModes: [], replacementHistory: [], mtbf: 15000, currentStress: 0.3 },
      { id: 'motherboard', name: 'Logic Board', health: 100, wearLevel: 0, dependencies: ['battery'], failureModes: [], replacementHistory: [], mtbf: 50000, currentStress: 0.15 },
      { id: 'charging_port', name: 'Charging Port', health: 100, wearLevel: 0, dependencies: ['motherboard'], failureModes: [], replacementHistory: [], mtbf: 20000, currentStress: 0.4 },
      { id: 'camera', name: 'Camera Module', health: 100, wearLevel: 0, dependencies: ['motherboard'], failureModes: [], replacementHistory: [], mtbf: 40000, currentStress: 0.1 },
      { id: 'speaker', name: 'Speaker', health: 100, wearLevel: 0, dependencies: ['motherboard'], failureModes: [], replacementHistory: [], mtbf: 30000, currentStress: 0.15 }
    ],
    laptop: [
      { id: 'display', name: 'LCD Panel', health: 100, wearLevel: 0, dependencies: ['motherboard'], failureModes: [], replacementHistory: [], mtbf: 35000, currentStress: 0.2 },
      { id: 'battery', name: 'Battery Pack', health: 100, wearLevel: 0, dependencies: [], failureModes: [], replacementHistory: [], mtbf: 12000, currentStress: 0.35 },
      { id: 'motherboard', name: 'Motherboard', health: 100, wearLevel: 0, dependencies: ['battery'], failureModes: [], replacementHistory: [], mtbf: 45000, currentStress: 0.2 },
      { id: 'ssd', name: 'SSD Storage', health: 100, wearLevel: 0, dependencies: ['motherboard'], failureModes: [], replacementHistory: [], mtbf: 100000, currentStress: 0.25 },
      { id: 'ram', name: 'RAM Modules', health: 100, wearLevel: 0, dependencies: ['motherboard'], failureModes: [], replacementHistory: [], mtbf: 200000, currentStress: 0.1 },
      { id: 'keyboard', name: 'Keyboard', health: 100, wearLevel: 0, dependencies: ['motherboard'], failureModes: [], replacementHistory: [], mtbf: 25000, currentStress: 0.3 },
      { id: 'cooling', name: 'Cooling System', health: 100, wearLevel: 0, dependencies: [], failureModes: [], replacementHistory: [], mtbf: 20000, currentStress: 0.4 },
      { id: 'dc_jack', name: 'DC Jack', health: 100, wearLevel: 0, dependencies: ['motherboard'], failureModes: [], replacementHistory: [], mtbf: 18000, currentStress: 0.35 }
    ],
    gaming_console: [
      { id: 'gpu', name: 'GPU', health: 100, wearLevel: 0, dependencies: ['motherboard', 'cooling'], failureModes: [], replacementHistory: [], mtbf: 40000, currentStress: 0.5 },
      { id: 'cpu', name: 'CPU', health: 100, wearLevel: 0, dependencies: ['motherboard', 'cooling'], failureModes: [], replacementHistory: [], mtbf: 60000, currentStress: 0.4 },
      { id: 'motherboard', name: 'Main Board', health: 100, wearLevel: 0, dependencies: ['psu'], failureModes: [], replacementHistory: [], mtbf: 50000, currentStress: 0.25 },
      { id: 'psu', name: 'Power Supply', health: 100, wearLevel: 0, dependencies: [], failureModes: [], replacementHistory: [], mtbf: 35000, currentStress: 0.3 },
      { id: 'cooling', name: 'Cooling System', health: 100, wearLevel: 0, dependencies: [], failureModes: [], replacementHistory: [], mtbf: 25000, currentStress: 0.45 },
      { id: 'optical_drive', name: 'Optical Drive', health: 100, wearLevel: 0, dependencies: ['motherboard'], failureModes: [], replacementHistory: [], mtbf: 15000, currentStress: 0.2 },
      { id: 'hdd', name: 'Hard Drive', health: 100, wearLevel: 0, dependencies: ['motherboard'], failureModes: [], replacementHistory: [], mtbf: 30000, currentStress: 0.35 }
    ]
  };
  
  const components = componentTemplates[deviceType] || componentTemplates.smartphone;
  
  // Add failure modes to each component
  for (const component of components) {
    component.failureModes = generateFailureModes(component.id, deviceType);
  }
  
  return components;
}

function generateFailureModes(componentId: string, deviceType: string): FailureMode[] {
  const failureModeTemplates: Record<string, FailureMode[]> = {
    display: [
      { id: 'dead_pixels', name: 'Dead Pixels', probability: 0.05, severity: 3, cascadeRisk: [], symptoms: ['black dots', 'stuck colors'], preventiveMeasures: ['avoid pressure', 'temperature control'] },
      { id: 'backlight_failure', name: 'Backlight Failure', probability: 0.08, severity: 7, cascadeRisk: [], symptoms: ['dim screen', 'no display'], preventiveMeasures: ['voltage regulation', 'thermal management'] },
      { id: 'touch_malfunction', name: 'Touch Malfunction', probability: 0.1, severity: 6, cascadeRisk: ['motherboard'], symptoms: ['ghost touches', 'unresponsive areas'], preventiveMeasures: ['connector inspection', 'ESD protection'] }
    ],
    battery: [
      { id: 'capacity_degradation', name: 'Capacity Degradation', probability: 0.3, severity: 4, cascadeRisk: [], symptoms: ['short battery life', 'unexpected shutdowns'], preventiveMeasures: ['proper charging cycles', 'temperature control'] },
      { id: 'swelling', name: 'Battery Swelling', probability: 0.05, severity: 9, cascadeRisk: ['display', 'motherboard'], symptoms: ['bulging case', 'loose display'], preventiveMeasures: ['replace old batteries', 'avoid overcharging'] },
      { id: 'charging_failure', name: 'Charging Failure', probability: 0.1, severity: 6, cascadeRisk: ['charging_port'], symptoms: ['wont charge', 'slow charging'], preventiveMeasures: ['use certified chargers', 'clean contacts'] }
    ],
    motherboard: [
      { id: 'component_failure', name: 'Component Failure', probability: 0.03, severity: 9, cascadeRisk: ['all'], symptoms: ['no power', 'boot loops'], preventiveMeasures: ['surge protection', 'thermal management'] },
      { id: 'liquid_damage', name: 'Liquid Damage', probability: 0.08, severity: 8, cascadeRisk: ['all'], symptoms: ['corrosion', 'intermittent issues'], preventiveMeasures: ['waterproofing', 'immediate drying'] },
      { id: 'solder_joint_failure', name: 'Solder Joint Failure', probability: 0.05, severity: 7, cascadeRisk: ['gpu', 'cpu'], symptoms: ['freezing', 'artifacts'], preventiveMeasures: ['reflow prevention', 'thermal cycling avoidance'] }
    ],
    cooling: [
      { id: 'fan_failure', name: 'Fan Failure', probability: 0.15, severity: 6, cascadeRisk: ['cpu', 'gpu'], symptoms: ['loud noise', 'overheating'], preventiveMeasures: ['dust cleaning', 'lubrication'] },
      { id: 'thermal_paste_degradation', name: 'Thermal Paste Degradation', probability: 0.2, severity: 5, cascadeRisk: ['cpu', 'gpu'], symptoms: ['high temps', 'throttling'], preventiveMeasures: ['periodic replacement', 'quality paste'] },
      { id: 'heatsink_blockage', name: 'Heatsink Blockage', probability: 0.25, severity: 5, cascadeRisk: ['cpu', 'gpu'], symptoms: ['dust buildup', 'overheating'], preventiveMeasures: ['regular cleaning', 'filtered environment'] }
    ]
  };
  
  return failureModeTemplates[componentId] || [];
}

async function calculateFailureProbabilities(env: Env, twin: DeviceTwin): Promise<Map<string, number>> {
  const probabilities = new Map<string, number>();
  
  for (const component of twin.components) {
    // Base failure probability from MTBF
    let baseProbability = twin.usageHours / component.mtbf;
    
    // Adjust for component health
    baseProbability *= (100 - component.health) / 100 + 1;
    
    // Adjust for environmental factors
    const envMultiplier = calculateEnvironmentalMultiplier(twin.environmentalFactors);
    baseProbability *= envMultiplier;
    
    // Adjust for stress level
    baseProbability *= (1 + component.currentStress);
    
    // Cap at 95%
    probabilities.set(component.id, Math.min(baseProbability, 0.95));
  }
  
  return probabilities;
}

function calculateEnvironmentalMultiplier(env: EnvironmentFactors): number {
  let multiplier = 1;
  
  // Temperature effects (optimal 20-25°C)
  if (env.temperature < 10 || env.temperature > 35) {
    multiplier *= 1.5;
  } else if (env.temperature < 15 || env.temperature > 30) {
    multiplier *= 1.2;
  }
  
  // Humidity effects (optimal 40-60%)
  if (env.humidity < 20 || env.humidity > 80) {
    multiplier *= 1.4;
  } else if (env.humidity < 30 || env.humidity > 70) {
    multiplier *= 1.1;
  }
  
  // Dust effects
  multiplier *= (1 + env.dustLevel);
  
  // Vibration effects
  multiplier *= (1 + env.vibration * 2);
  
  // Electrical stability effects
  multiplier *= (2 - env.electricalStability);
  
  return multiplier;
}

function generateHealthSummary(twin: DeviceTwin): any {
  const componentHealths = twin.components.map(c => c.health);
  const avgHealth = componentHealths.reduce((a, b) => a + b, 0) / componentHealths.length;
  const minHealth = Math.min(...componentHealths);
  const criticalComponents = twin.components.filter(c => c.health < 50);
  
  return {
    overallHealth: avgHealth,
    weakestComponent: twin.components.find(c => c.health === minHealth),
    criticalComponents: criticalComponents.map(c => ({ id: c.id, name: c.name, health: c.health })),
    healthTrend: 'stable', // Would calculate from history
    estimatedLifespan: calculateEstimatedLifespan(twin)
  };
}

function calculateEstimatedLifespan(twin: DeviceTwin): number {
  const avgHealth = twin.components.reduce((sum, c) => sum + c.health, 0) / twin.components.length;
  const degradationRate = 0.01; // 1% per month base rate
  return Math.floor(avgHealth / degradationRate);
}

function identifyRiskAreas(twin: DeviceTwin): any[] {
  const risks = [];
  
  for (const component of twin.components) {
    if (component.health < 70) {
      risks.push({
        component: component.name,
        riskLevel: component.health < 50 ? 'high' : 'medium',
        reason: `Component health at ${component.health}%`,
        recommendation: `Schedule ${component.health < 50 ? 'immediate' : 'preventive'} maintenance`
      });
    }
    
    if (component.wearLevel > 0.7) {
      risks.push({
        component: component.name,
        riskLevel: component.wearLevel > 0.9 ? 'critical' : 'high',
        reason: `Wear level at ${(component.wearLevel * 100).toFixed(0)}%`,
        recommendation: 'Consider replacement'
      });
    }
  }
  
  return risks;
}

async function runMonteCarloSimulation(env: Env, twin: DeviceTwin, scenario: SimulationScenario): Promise<any> {
  const iterations = scenario.iterations || 1000;
  const results = {
    successes: 0,
    partialSuccesses: 0,
    failures: 0,
    costs: [] as number[],
    durations: [] as number[],
    failureReasons: new Map<string, number>()
  };
  
  for (let i = 0; i < iterations; i++) {
    const outcome = simulateSingleRepair(twin, scenario);
    
    if (outcome.success) {
      results.successes++;
    } else if (outcome.partial) {
      results.partialSuccesses++;
    } else {
      results.failures++;
      const reason = outcome.failureReason || 'unknown';
      results.failureReasons.set(reason, (results.failureReasons.get(reason) || 0) + 1);
    }
    
    results.costs.push(outcome.cost);
    results.durations.push(outcome.duration);
  }
  
  return {
    successRate: results.successes / iterations,
    partialRate: results.partialSuccesses / iterations,
    failureRate: results.failures / iterations,
    averageCost: results.costs.reduce((a, b) => a + b, 0) / iterations,
    averageDuration: results.durations.reduce((a, b) => a + b, 0) / iterations,
    costStdDev: calculateStdDev(results.costs),
    durationStdDev: calculateStdDev(results.durations),
    topFailureReasons: Array.from(results.failureReasons.entries()).sort((a, b) => b[1] - a[1]).slice(0, 5),
    riskLevel: results.failures / iterations > 0.3 ? 'high' : results.failures / iterations > 0.15 ? 'medium' : 'low'
  };
}

function simulateSingleRepair(twin: DeviceTwin, scenario: SimulationScenario): any {
  const skillGap = scenario.repairAction.technicianSkillRequired - scenario.constraints.availableSkillLevel;
  const skillFactor = skillGap > 0 ? Math.pow(0.9, skillGap) : 1;
  
  // Base success probability
  let successProbability = 0.85 * skillFactor;
  
  // Adjust for part quality
  for (const part of scenario.repairAction.partsNeeded) {
    if (part.quality === 'refurbished') successProbability *= 0.9;
    else if (part.quality === 'aftermarket') successProbability *= 0.95;
  }
  
  // Adjust for environmental conditions
  const envFactor = calculateEnvironmentalMultiplier(scenario.constraints.environmentalConditions);
  successProbability /= envFactor;
  
  // Simulate outcome
  const random = Math.random();
  const success = random < successProbability;
  const partial = !success && random < successProbability + 0.15;
  
  // Calculate cost with variance
  let cost = scenario.repairAction.partsNeeded.reduce((sum, p) => sum + getPartCost(p), 0);
  cost += scenario.repairAction.estimatedDuration * 50; // Labor at $50/hour
  cost *= 0.8 + Math.random() * 0.4; // 20% variance
  
  // Calculate duration with variance
  let duration = scenario.repairAction.estimatedDuration;
  duration *= 0.7 + Math.random() * 0.6; // 30% variance
  if (skillGap > 0) duration *= (1 + skillGap * 0.1);
  
  return {
    success,
    partial,
    failureReason: success ? null : generateFailureReason(scenario, skillGap),
    cost,
    duration
  };
}

function getPartCost(part: PartRequirement): number {
  const baseCosts: Record<string, number> = {
    display: 150,
    battery: 50,
    motherboard: 300,
    charging_port: 30,
    camera: 80,
    speaker: 25,
    keyboard: 60,
    cooling: 40,
    ssd: 100,
    gpu: 400,
    cpu: 250
  };
  
  const base = baseCosts[part.partId] || 50;
  const qualityMultiplier = part.quality === 'oem' ? 1.5 : part.quality === 'aftermarket' ? 0.7 : 0.5;
  
  return base * qualityMultiplier * part.quantity;
}

function generateFailureReason(scenario: SimulationScenario, skillGap: number): string {
  const reasons = [
    'Part installation error',
    'Incompatible replacement part',
    'Hidden secondary damage discovered',
    'Tool damage during repair',
    'ESD damage',
    'Connector damage',
    'Calibration failure'
  ];
  
  if (skillGap > 2) {
    reasons.push('Insufficient technician skill');
    reasons.push('Procedure error');
  }
  
  return reasons[Math.floor(Math.random() * reasons.length)];
}

function calculateStdDev(values: number[]): number {
  const avg = values.reduce((a, b) => a + b, 0) / values.length;
  const squaredDiffs = values.map(v => Math.pow(v - avg, 2));
  return Math.sqrt(squaredDiffs.reduce((a, b) => a + b, 0) / values.length);
}

async function predictOutcome(env: Env, twin: DeviceTwin, scenario: SimulationScenario, results: any): Promise<SimulationOutcome> {
  const componentHealthAfter = new Map<string, number>();
  
  for (const component of twin.components) {
    if (scenario.repairAction.targetComponents.includes(component.id)) {
      // Repaired component gets health boost
      componentHealthAfter.set(component.id, Math.min(100, component.health + 60 * results.successRate));
    } else {
      // Other components unchanged
      componentHealthAfter.set(component.id, component.health);
    }
  }
  
  const avgHealthAfter = Array.from(componentHealthAfter.values()).reduce((a, b) => a + b, 0) / componentHealthAfter.size;
  
  return {
    deviceHealthAfter: avgHealthAfter,
    componentHealthAfter,
    expectedLifespan: Math.floor(avgHealthAfter / 0.01),
    recurringIssueRisk: 1 - results.successRate,
    customerSatisfactionPrediction: results.successRate * 0.6 + (1 - results.failureRate) * 0.4
  };
}

async function assessRisks(env: Env, twin: DeviceTwin, scenario: SimulationScenario, results: any): Promise<RiskAssessment> {
  const riskFactors: RiskFactor[] = [];
  
  // Skill gap risk
  const skillGap = scenario.repairAction.technicianSkillRequired - scenario.constraints.availableSkillLevel;
  if (skillGap > 0) {
    riskFactors.push({
      factor: 'Skill gap',
      probability: 0.3 * skillGap,
      impact: 0.7,
      riskScore: 0.3 * skillGap * 0.7,
      mitigation: 'Provide additional training or assign senior technician'
    });
  }
  
  // Part quality risk
  const lowQualityParts = scenario.repairAction.partsNeeded.filter(p => p.quality === 'refurbished');
  if (lowQualityParts.length > 0) {
    riskFactors.push({
      factor: 'Refurbished parts',
      probability: 0.15 * lowQualityParts.length,
      impact: 0.5,
      riskScore: 0.15 * lowQualityParts.length * 0.5,
      mitigation: 'Source OEM or quality aftermarket parts'
    });
  }
  
  // Environmental risk
  const envMultiplier = calculateEnvironmentalMultiplier(scenario.constraints.environmentalConditions);
  if (envMultiplier > 1.2) {
    riskFactors.push({
      factor: 'Adverse environmental conditions',
      probability: (envMultiplier - 1) * 0.5,
      impact: 0.4,
      riskScore: (envMultiplier - 1) * 0.5 * 0.4,
      mitigation: 'Improve workspace conditions'
    });
  }
  
  const totalRiskScore = riskFactors.reduce((sum, rf) => sum + rf.riskScore, 0);
  
  return {
    overallRisk: totalRiskScore > 0.5 ? 'critical' : totalRiskScore > 0.3 ? 'high' : totalRiskScore > 0.15 ? 'medium' : 'low',
    riskScore: totalRiskScore,
    riskFactors,
    mitigationStrategies: riskFactors.map(rf => rf.mitigation),
    worstCaseScenario: `Complete repair failure with ${(results.failureRate * 100).toFixed(1)}% probability, potential additional damage`,
    bestCaseScenario: `Successful repair with ${(results.successRate * 100).toFixed(1)}% probability, device restored to full functionality`
  };
}

async function generateAlternatives(env: Env, twin: DeviceTwin, scenario: SimulationScenario): Promise<AlternativeStrategy[]> {
  const alternatives: AlternativeStrategy[] = [];
  
  // Alternative 1: Replace vs Repair
  if (scenario.repairAction.type === 'repair') {
    alternatives.push({
      name: 'Full Component Replacement',
      description: 'Replace the entire component instead of repairing',
      successProbability: 0.95,
      cost: getPartCost({ partId: scenario.repairAction.targetComponents[0], quantity: 1, quality: 'oem', criticalPath: true }) * 1.5,
      duration: scenario.repairAction.estimatedDuration * 0.7,
      tradeoffs: ['Higher part cost', 'Lower skill requirement', 'Better long-term reliability']
    });
  }
  
  // Alternative 2: Refurbished parts
  if (!scenario.repairAction.partsNeeded.some(p => p.quality === 'refurbished')) {
    alternatives.push({
      name: 'Use Refurbished Parts',
      description: 'Use quality-tested refurbished parts to reduce cost',
      successProbability: 0.85,
      cost: scenario.repairAction.partsNeeded.reduce((sum, p) => sum + getPartCost({ ...p, quality: 'refurbished' }), 0),
      duration: scenario.repairAction.estimatedDuration,
      tradeoffs: ['Lower cost', 'Slightly reduced reliability', 'May affect warranty']
    });
  }
  
  // Alternative 3: Comprehensive repair
  alternatives.push({
    name: 'Comprehensive Overhaul',
    description: 'Address all wear items during this repair',
    successProbability: 0.9,
    cost: scenario.repairAction.partsNeeded.reduce((sum, p) => sum + getPartCost(p), 0) * 2,
    duration: scenario.repairAction.estimatedDuration * 1.8,
    tradeoffs: ['Higher upfront cost', 'Prevents future issues', 'Better customer satisfaction']
  });
  
  return alternatives;
}

function generateTrainingRecommendations(currentLevel: number, requiredLevel: number): TrainingRecommendation[] {
  const recommendations: TrainingRecommendation[] = [];
  
  if (requiredLevel > currentLevel) {
    const gap = requiredLevel - currentLevel;
    
    recommendations.push({
      skill: 'Component-level repair',
      currentLevel,
      requiredLevel,
      trainingModule: `Advanced Repair Techniques Level ${requiredLevel}`,
      estimatedTrainingTime: gap * 8, // 8 hours per level
      impactOnSuccess: gap * 0.1
    });
    
    recommendations.push({
      skill: 'Diagnostic skills',
      currentLevel,
      requiredLevel,
      trainingModule: 'Advanced Diagnostics Certification',
      estimatedTrainingTime: gap * 4,
      impactOnSuccess: gap * 0.05
    });
  }
  
  return recommendations;
}

async function analyzeCosts(env: Env, scenario: SimulationScenario, results: any): Promise<CostAnalysis> {
  const laborCost = scenario.repairAction.estimatedDuration * 50;
  const partsCost = scenario.repairAction.partsNeeded.reduce((sum, p) => sum + getPartCost(p), 0);
  const toolsCost = 0; // Assuming tools are available
  const overheadCost = laborCost * 0.2;
  const totalCost = laborCost + partsCost + toolsCost + overheadCost;
  
  return {
    laborCost,
    partsCost,
    toolsCost,
    overheadCost,
    totalCost,
    roi: 2.5, // Assuming device value is 2.5x repair cost
    breakEvenTime: 6, // months
    costVariance: {
      min: totalCost * 0.8,
      max: totalCost * 1.3,
      expected: results.averageCost
    }
  };
}

function analyzeTimeline(scenario: SimulationScenario, results: any): TimelineAnalysis {
  const estimatedDuration = scenario.repairAction.estimatedDuration;
  
  return {
    estimatedDuration,
    bestCase: estimatedDuration * 0.7,
    worstCase: estimatedDuration * 1.5,
    criticalPath: [
      { step: 'Diagnosis', duration: 0.5, dependencies: [], riskLevel: 0.1 },
      { step: 'Disassembly', duration: 0.5, dependencies: ['Diagnosis'], riskLevel: 0.2 },
      { step: 'Part replacement', duration: estimatedDuration * 0.5, dependencies: ['Disassembly'], riskLevel: 0.3 },
      { step: 'Reassembly', duration: 0.5, dependencies: ['Part replacement'], riskLevel: 0.2 },
      { step: 'Testing', duration: 0.5, dependencies: ['Reassembly'], riskLevel: 0.1 }
    ],
    parallelizableSteps: ['Component testing', 'Documentation'],
    bottlenecks: scenario.repairAction.targetComponents.length > 2 ? ['Multiple component repair coordination'] : []
  };
}

async function analyzeCascadeRisk(env: Env, twin: DeviceTwin, scenario: SimulationScenario): Promise<CascadeAnalysis> {
  const affectedComponents: string[] = [];
  const cascadeSequence: CascadeEvent[] = [];
  
  // Analyze cascade potential for target components
  for (const targetId of scenario.repairAction.targetComponents) {
    const targetComponent = twin.components.find(c => c.id === targetId);
    if (!targetComponent) continue;
    
    for (const failureMode of targetComponent.failureModes) {
      for (const cascadeTarget of failureMode.cascadeRisk) {
        if (!affectedComponents.includes(cascadeTarget)) {
          affectedComponents.push(cascadeTarget);
          cascadeSequence.push({
            component: cascadeTarget,
            failureMode: `Secondary failure from ${targetComponent.name}`,
            triggerProbability: failureMode.probability * 0.3,
            timeToFailure: 24, // hours
            impactSeverity: failureMode.severity * 0.7
          });
        }
      }
    }
  }
  
  const cascadeRisk = cascadeSequence.reduce((sum, e) => sum + e.triggerProbability * e.impactSeverity, 0) / 10;
  
  return {
    cascadeRisk,
    affectedComponents,
    cascadeSequence,
    containmentStrategies: [
      'Inspect connected components during repair',
      'Test all related functions post-repair',
      'Document any signs of stress on adjacent parts'
    ]
  };
}

async function simulateFailureCascade(env: Env, twin: DeviceTwin, failureComponent: string, depth: number): Promise<any> {
  const affected = new Set<string>();
  const timeline: any[] = [];
  let totalDamage = 0;
  
  const queue = [{ component: failureComponent, depth: 0, time: 0 }];
  
  while (queue.length > 0) {
    const current = queue.shift()!;
    if (current.depth >= depth || affected.has(current.component)) continue;
    
    affected.add(current.component);
    const component = twin.components.find(c => c.id === current.component);
    
    if (component) {
      const damage = (100 - component.health) * 10;
      totalDamage += damage;
      
      timeline.push({
        time: current.time,
        component: component.name,
        event: `Failure cascade reaches ${component.name}`,
        damage
      });
      
      // Add dependent components to queue
      for (const dependent of twin.components.filter(c => c.dependencies.includes(current.component))) {
        queue.push({
          component: dependent.id,
          depth: current.depth + 1,
          time: current.time + 1
        });
      }
    }
  }
  
  return {
    affectedComponents: Array.from(affected),
    timeline,
    totalDamage,
    containmentOptions: ['Isolate power supply', 'Disconnect cascading components', 'Emergency shutdown'],
    preventiveMeasures: ['Regular maintenance', 'Component isolation', 'Redundancy planning']
  };
}

async function generateTrainingScenario(env: Env, deviceType: string, difficulty: string, focusAreas: string[]): Promise<any> {
  const scenarios: Record<string, any> = {
    easy: {
      issues: [{ component: 'battery', problem: 'capacity_degradation', severity: 4 }],
      symptoms: ['Device shutting down at 20% battery', 'Battery draining quickly'],
      hints: ['Check battery health in diagnostics', 'Battery may need replacement'],
      solution: { action: 'replace', component: 'battery' },
      timeLimit: 30,
      objective: 'Diagnose and resolve battery issue'
    },
    medium: {
      issues: [
        { component: 'charging_port', problem: 'loose_connection', severity: 5 },
        { component: 'battery', problem: 'charging_failure', severity: 4 }
      ],
      symptoms: ['Intermittent charging', 'Cable needs to be held at angle', 'Sometimes doesnt charge at all'],
      hints: ['Inspect charging port for debris', 'Test with different cables', 'Check for port damage'],
      solution: { action: 'replace', component: 'charging_port' },
      timeLimit: 45,
      objective: 'Diagnose charging issues and repair'
    },
    hard: {
      issues: [
        { component: 'motherboard', problem: 'solder_joint_failure', severity: 7 },
        { component: 'display', problem: 'backlight_failure', severity: 6 }
      ],
      symptoms: ['Random shutdowns', 'Display flickering', 'Device runs hot', 'Occasional boot failures'],
      hints: ['Multiple symptoms may indicate motherboard issue', 'Check thermal readings', 'Inspect for cold solder joints'],
      solution: { action: 'reball', component: 'motherboard' },
      timeLimit: 90,
      objective: 'Diagnose complex multi-symptom issue'
    }
  };
  
  const scenario = scenarios[difficulty] || scenarios.medium;
  scenario.deviceType = deviceType;
  scenario.difficulty = difficulty;
  scenario.availableTools = ['multimeter', 'screwdriver_set', 'heat_gun', 'microscope', 'power_supply'];
  
  return scenario;
}

async function createTrainingTwin(env: Env, deviceType: string, issues: any[]): Promise<DeviceTwin> {
  const twin: DeviceTwin = {
    id: `training_twin_${Date.now()}`,
    deviceType,
    model: 'Training Simulator',
    manufacturer: 'NoizyLab Training',
    components: await generateComponentTree(env, deviceType, 'training', {}),
    age: 2,
    usageHours: 5000,
    environmentalFactors: {
      temperature: 25,
      humidity: 50,
      dustLevel: 0.3,
      vibration: 0.1,
      electricalStability: 0.95
    },
    repairHistory: [],
    currentCondition: 70,
    failureProbabilities: new Map()
  };
  
  // Apply training issues
  for (const issue of issues) {
    const component = twin.components.find(c => c.id === issue.component);
    if (component) {
      component.health = 100 - issue.severity * 10;
      component.wearLevel = issue.severity / 10;
    }
  }
  
  return twin;
}

async function simulateTrainingAction(env: Env, twin: DeviceTwin, action: any): Promise<any> {
  const result = {
    success: false,
    stateChanges: {},
    feedback: ''
  };
  
  switch (action.type) {
    case 'diagnose':
      result.success = true;
      result.stateChanges = {
        diagnosticData: twin.components.find(c => c.id === action.target)
      };
      result.feedback = 'Diagnostic data retrieved';
      break;
    
    case 'inspect':
      result.success = true;
      const inspectedComponent = twin.components.find(c => c.id === action.target);
      result.stateChanges = {
        visualInspection: inspectedComponent ? {
          health: inspectedComponent.health,
          wearVisible: inspectedComponent.wearLevel > 0.5
        } : null
      };
      result.feedback = inspectedComponent ? `Inspected ${inspectedComponent.name}` : 'Component not found';
      break;
    
    case 'replace':
      const componentToReplace = twin.components.find(c => c.id === action.target);
      if (componentToReplace) {
        componentToReplace.health = 100;
        componentToReplace.wearLevel = 0;
        result.success = true;
        result.stateChanges = { componentReplaced: action.target };
        result.feedback = `Successfully replaced ${componentToReplace.name}`;
      } else {
        result.feedback = 'Component not found';
      }
      break;
    
    default:
      result.feedback = 'Unknown action type';
  }
  
  return result;
}

function checkSolution(twin: DeviceTwin, expectedSolution: any, actions: any[]): boolean {
  // Check if the expected repair action was performed
  const correctAction = actions.find(a => 
    a.type === expectedSolution.action && 
    a.target === expectedSolution.component
  );
  
  if (!correctAction) return false;
  
  // Check if component is now healthy
  const component = twin.components.find(c => c.id === expectedSolution.component);
  return component ? component.health >= 95 : false;
}

function calculateTrainingScore(session: any): any {
  const timeTaken = (session.endTime - session.startTime) / 1000 / 60; // minutes
  const timeLimit = session.scenario.timeLimit;
  
  let score = 100;
  
  // Time penalty
  if (timeTaken > timeLimit) {
    score -= Math.min(30, (timeTaken - timeLimit) * 2);
  } else {
    score += Math.min(10, (timeLimit - timeTaken) * 0.5); // Bonus for finishing early
  }
  
  // Action efficiency penalty
  const optimalActions = 5; // Assume optimal is 5 actions
  if (session.actions.length > optimalActions * 2) {
    score -= (session.actions.length - optimalActions * 2) * 2;
  }
  
  // Hint penalty
  const hintsUsed = session.actions.filter((a: any) => a.type === 'hint').length;
  score -= hintsUsed * 5;
  
  return {
    total: Math.max(0, Math.min(100, score)),
    timeScore: Math.max(0, 100 - (timeTaken > timeLimit ? (timeTaken - timeLimit) * 2 : 0)),
    efficiencyScore: Math.max(0, 100 - Math.max(0, session.actions.length - optimalActions) * 5),
    accuracyScore: 100 - hintsUsed * 10
  };
}

function analyzeTrainingPerformance(session: any): any {
  return {
    totalTime: (session.endTime - session.startTime) / 1000 / 60,
    actionsPerformed: session.actions.length,
    hintsUsed: session.actions.filter((a: any) => a.type === 'hint').length,
    diagnosticSteps: session.actions.filter((a: any) => a.type === 'diagnose').length,
    incorrectAttempts: session.actions.filter((a: any) => a.type === 'replace' && !a.wasCorrect).length,
    strengthAreas: ['Diagnosis', 'Component identification'],
    improvementAreas: ['Time management', 'Systematic troubleshooting']
  };
}

function generateSkillRecommendations(analysis: any): string[] {
  const recommendations = [];
  
  if (analysis.totalTime > 30) {
    recommendations.push('Practice timed diagnostic exercises');
  }
  
  if (analysis.hintsUsed > 2) {
    recommendations.push('Review component failure patterns');
  }
  
  if (analysis.incorrectAttempts > 1) {
    recommendations.push('Complete systematic troubleshooting course');
  }
  
  if (recommendations.length === 0) {
    recommendations.push('Ready for advanced certification');
  }
  
  return recommendations;
}

function generateComparisonMatrix(results: any[]): any {
  return {
    headers: ['Scenario', 'Success %', 'Cost', 'Duration', 'Risk'],
    rows: results.map(r => [
      r.scenarioName,
      `${(r.successProbability * 100).toFixed(1)}%`,
      `$${r.expectedCost.toFixed(2)}`,
      `${r.expectedDuration.toFixed(1)}h`,
      r.riskLevel
    ])
  };
}

export default app;
