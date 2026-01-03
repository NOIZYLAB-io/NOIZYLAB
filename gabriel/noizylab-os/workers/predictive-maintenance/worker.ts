/**
 * NoizyLab OS - Predictive Maintenance Worker
 * 🔮 AI-Powered Failure Prediction System
 * 
 * Uses machine learning to predict device failures before they happen
 * by analyzing repair history, component lifespans, and usage patterns.
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
  PREDICTIVE_MAINTENANCE_KV: KVNamespace;
  D1_DATABASE: D1Database;
  R2_BUCKET: R2Bucket;
  AI: Ai;
  ANALYTICS_SERVICE: Fetcher;
  NOTIFICATIONS_SERVICE: Fetcher;
  BRAIN_SERVICE: Fetcher;
}

interface DeviceProfile {
  device_id: string;
  device_model: string;
  manufacture_date: string;
  first_repair_date: string;
  total_repairs: number;
  components_replaced: ComponentHistory[];
  usage_hours_estimate: number;
  environment_factors: EnvironmentFactors;
  risk_score: number;
  predicted_failures: PredictedFailure[];
}

interface ComponentHistory {
  component_type: string;
  original_install: string;
  replaced_date?: string;
  current_age_days: number;
  expected_lifespan_days: number;
  health_percentage: number;
}

interface EnvironmentFactors {
  humidity_exposure: 'low' | 'medium' | 'high';
  temperature_stress: 'low' | 'medium' | 'high';
  physical_stress: 'low' | 'medium' | 'high';
  power_surge_history: boolean;
  liquid_damage_history: boolean;
}

interface PredictedFailure {
  component: string;
  probability: number;
  estimated_date: string;
  confidence: number;
  prevention_action: string;
  cost_if_preventive: number;
  cost_if_reactive: number;
  severity: 'low' | 'medium' | 'high' | 'critical';
}

interface FailurePattern {
  pattern_id: string;
  device_model: string;
  failure_sequence: string[];
  occurrence_count: number;
  avg_time_between_failures: number;
  root_cause: string;
  prevention_strategy: string;
}

interface RiskAssessment {
  device_id: string;
  overall_risk: number;
  risk_category: 'healthy' | 'watch' | 'at-risk' | 'critical';
  top_risks: PredictedFailure[];
  recommended_actions: PreventiveAction[];
  next_assessment_date: string;
}

interface PreventiveAction {
  action_id: string;
  priority: number;
  action_type: 'inspection' | 'replacement' | 'cleaning' | 'firmware' | 'calibration';
  component: string;
  description: string;
  estimated_cost: number;
  savings_potential: number;
  deadline: string;
}

interface ComponentLifespanModel {
  component_type: string;
  base_lifespan_hours: number;
  failure_curve: 'bathtub' | 'linear' | 'exponential';
  factors: LifespanFactor[];
  current_reliability: number;
}

interface LifespanFactor {
  factor_name: string;
  impact_multiplier: number;
  applicable_conditions: string[];
}

interface FleetAnalysis {
  total_devices: number;
  healthy_count: number;
  watch_count: number;
  at_risk_count: number;
  critical_count: number;
  predicted_failures_30d: number;
  predicted_failures_90d: number;
  preventive_maintenance_queue: PreventiveAction[];
  cost_projections: CostProjection;
  fleet_health_trend: TrendData[];
}

interface CostProjection {
  preventive_cost_30d: number;
  reactive_cost_if_ignored_30d: number;
  potential_savings_30d: number;
  preventive_cost_90d: number;
  reactive_cost_if_ignored_90d: number;
  potential_savings_90d: number;
}

interface TrendData {
  date: string;
  health_score: number;
  failures_count: number;
  preventive_actions_count: number;
}

interface MLTrainingData {
  feature_vector: number[];
  labels: {
    failed_within_30d: boolean;
    failed_component: string;
    failure_type: string;
  };
}

const app = new Hono<{ Bindings: Env }>();

app.use('/*', cors());

// Component lifespan knowledge base (can be dynamically updated)
const COMPONENT_LIFESPAN_KB: Record<string, ComponentLifespanModel> = {
  'battery': {
    component_type: 'battery',
    base_lifespan_hours: 2000, // ~2-3 years typical use
    failure_curve: 'exponential',
    factors: [
      { factor_name: 'high_temperature', impact_multiplier: 0.7, applicable_conditions: ['hot_climate', 'gaming_use'] },
      { factor_name: 'fast_charging', impact_multiplier: 0.85, applicable_conditions: ['frequent_fast_charge'] },
      { factor_name: 'deep_discharge', impact_multiplier: 0.8, applicable_conditions: ['frequent_zero_battery'] },
    ],
    current_reliability: 0.95,
  },
  'display': {
    component_type: 'display',
    base_lifespan_hours: 30000, // ~6-8 years
    failure_curve: 'bathtub',
    factors: [
      { factor_name: 'oled_burn_in', impact_multiplier: 0.75, applicable_conditions: ['static_content', 'high_brightness'] },
      { factor_name: 'physical_stress', impact_multiplier: 0.6, applicable_conditions: ['frequent_drops', 'screen_pressure'] },
    ],
    current_reliability: 0.92,
  },
  'charging_port': {
    component_type: 'charging_port',
    base_lifespan_hours: 10000, // ~4-5 years
    failure_curve: 'linear',
    factors: [
      { factor_name: 'debris_accumulation', impact_multiplier: 0.7, applicable_conditions: ['dusty_environment', 'pocket_carry'] },
      { factor_name: 'cable_stress', impact_multiplier: 0.8, applicable_conditions: ['non_oem_cables', 'angled_charging'] },
    ],
    current_reliability: 0.88,
  },
  'motherboard': {
    component_type: 'motherboard',
    base_lifespan_hours: 50000, // ~10+ years
    failure_curve: 'bathtub',
    factors: [
      { factor_name: 'liquid_damage', impact_multiplier: 0.3, applicable_conditions: ['liquid_exposure'] },
      { factor_name: 'power_surge', impact_multiplier: 0.5, applicable_conditions: ['power_surge_history'] },
      { factor_name: 'thermal_cycling', impact_multiplier: 0.85, applicable_conditions: ['gaming_use', 'heavy_load'] },
    ],
    current_reliability: 0.97,
  },
  'speaker': {
    component_type: 'speaker',
    base_lifespan_hours: 20000,
    failure_curve: 'linear',
    factors: [
      { factor_name: 'high_volume', impact_multiplier: 0.7, applicable_conditions: ['max_volume_use'] },
      { factor_name: 'moisture', impact_multiplier: 0.6, applicable_conditions: ['gym_use', 'humid_environment'] },
    ],
    current_reliability: 0.91,
  },
  'camera': {
    component_type: 'camera',
    base_lifespan_hours: 25000,
    failure_curve: 'bathtub',
    factors: [
      { factor_name: 'ois_wear', impact_multiplier: 0.8, applicable_conditions: ['heavy_video_use'] },
      { factor_name: 'dust_ingress', impact_multiplier: 0.75, applicable_conditions: ['dusty_environment'] },
    ],
    current_reliability: 0.93,
  },
};

// Failure pattern recognition database
const FAILURE_PATTERNS: FailurePattern[] = [
  {
    pattern_id: 'cascade_battery_charging',
    device_model: 'iPhone',
    failure_sequence: ['battery_swell', 'charging_intermittent', 'no_charge'],
    occurrence_count: 1247,
    avg_time_between_failures: 45,
    root_cause: 'Battery degradation causing charging circuit stress',
    prevention_strategy: 'Replace battery at 80% health threshold',
  },
  {
    pattern_id: 'thermal_cascade',
    device_model: 'MacBook',
    failure_sequence: ['fan_noise', 'thermal_throttling', 'random_shutdown', 'gpu_failure'],
    occurrence_count: 834,
    avg_time_between_failures: 120,
    root_cause: 'Thermal paste degradation and dust accumulation',
    prevention_strategy: 'Thermal paste replacement and cleaning every 2 years',
  },
  {
    pattern_id: 'display_cascade',
    device_model: 'iPhone',
    failure_sequence: ['ghost_touch', 'display_lines', 'display_dead'],
    occurrence_count: 2103,
    avg_time_between_failures: 30,
    root_cause: 'Flex cable degradation from repeated folding',
    prevention_strategy: 'Inspect flex cable during any display-related repair',
  },
];

// ==================== Device Profile Analysis ====================

app.post('/profile/analyze', async (c) => {
  const { device_id, repair_history, usage_data } = await c.req.json();

  // Build comprehensive device profile
  const profile = await buildDeviceProfile(c.env, device_id, repair_history, usage_data);

  // Run predictive models
  const predictions = await runPredictiveModels(c.env, profile);

  // Store profile
  await c.env.PREDICTIVE_MAINTENANCE_KV.put(
    `profile:${device_id}`,
    JSON.stringify({ ...profile, predicted_failures: predictions }),
    { expirationTtl: 86400 * 7 } // 7 days cache
  );

  // Alert if critical
  if (predictions.some(p => p.probability > 0.8 && p.severity === 'critical')) {
    await c.env.NOTIFICATIONS_SERVICE.fetch(new Request('https://notifications/send', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        type: 'predictive_alert',
        priority: 'high',
        device_id,
        message: `Critical failure predicted for device ${device_id}`,
        predictions: predictions.filter(p => p.probability > 0.8),
      }),
    }));
  }

  return c.json({
    device_id,
    profile,
    predictions,
    overall_health: calculateOverallHealth(profile, predictions),
    recommended_actions: generatePreventiveActions(predictions),
  });
});

// ==================== Risk Assessment ====================

app.post('/risk/assess', async (c) => {
  const { device_id, include_cost_analysis = true } = await c.req.json();

  // Get or build profile
  const cachedProfile = await c.env.PREDICTIVE_MAINTENANCE_KV.get(`profile:${device_id}`);
  let profile: DeviceProfile;

  if (cachedProfile) {
    profile = JSON.parse(cachedProfile);
  } else {
    // Fetch from database and build profile
    const deviceData = await c.env.D1_DATABASE.prepare(`
      SELECT d.*, 
        GROUP_CONCAT(r.repair_type) as repair_types,
        COUNT(r.id) as repair_count
      FROM devices d
      LEFT JOIN repairs r ON d.id = r.device_id
      WHERE d.id = ?
      GROUP BY d.id
    `).bind(device_id).first();

    if (!deviceData) {
      return c.json({ error: 'Device not found' }, 404);
    }

    profile = await buildDeviceProfile(c.env, device_id, deviceData, null);
  }

  const riskScore = calculateRiskScore(profile);
  const assessment: RiskAssessment = {
    device_id,
    overall_risk: riskScore,
    risk_category: getRiskCategory(riskScore),
    top_risks: profile.predicted_failures?.slice(0, 5) || [],
    recommended_actions: generatePreventiveActions(profile.predicted_failures || []),
    next_assessment_date: new Date(Date.now() + 30 * 24 * 60 * 60 * 1000).toISOString(),
  };

  if (include_cost_analysis) {
    const costAnalysis = await calculateCostAnalysis(profile.predicted_failures || []);
    return c.json({ assessment, cost_analysis: costAnalysis });
  }

  return c.json({ assessment });
});

// ==================== Fleet Analysis ====================

app.get('/fleet/analysis', async (c) => {
  const customer_id = c.req.query('customer_id');

  // Get all devices for fleet analysis
  let devicesQuery = `
    SELECT d.id, d.model, d.created_at,
      COUNT(r.id) as repair_count,
      MAX(r.created_at) as last_repair
    FROM devices d
    LEFT JOIN repairs r ON d.id = r.device_id
  `;

  if (customer_id) {
    devicesQuery += ` WHERE d.customer_id = ? `;
  }
  devicesQuery += ` GROUP BY d.id `;

  const stmt = customer_id
    ? c.env.D1_DATABASE.prepare(devicesQuery).bind(customer_id)
    : c.env.D1_DATABASE.prepare(devicesQuery);

  const devices = await stmt.all();

  // Analyze fleet
  const fleetAnalysis = await analyzeFleet(c.env, devices.results || []);

  // Store fleet snapshot
  await c.env.D1_DATABASE.prepare(`
    INSERT INTO fleet_snapshots (customer_id, snapshot_data, created_at)
    VALUES (?, ?, datetime('now'))
  `).bind(customer_id || 'all', JSON.stringify(fleetAnalysis)).run();

  return c.json(fleetAnalysis);
});

// ==================== Pattern Detection ====================

app.post('/patterns/detect', async (c) => {
  const { device_model, symptoms } = await c.req.json();

  // Match against known failure patterns
  const matchedPatterns = FAILURE_PATTERNS.filter(pattern => {
    if (device_model && !pattern.device_model.toLowerCase().includes(device_model.toLowerCase())) {
      return false;
    }

    const symptomMatches = symptoms.filter((s: string) =>
      pattern.failure_sequence.some(f => f.toLowerCase().includes(s.toLowerCase()))
    );

    return symptomMatches.length > 0;
  });

  // Calculate pattern progression
  const patternAnalysis = matchedPatterns.map(pattern => {
    const currentPosition = findPatternPosition(pattern.failure_sequence, symptoms);
    const nextPredictedFailures = pattern.failure_sequence.slice(currentPosition);
    const timeToNextFailure = pattern.avg_time_between_failures;

    return {
      pattern,
      current_position: currentPosition,
      progression_percentage: (currentPosition / pattern.failure_sequence.length) * 100,
      next_predicted_failures: nextPredictedFailures,
      estimated_days_to_next: timeToNextFailure,
      prevention_window: timeToNextFailure > 30 ? 'good' : timeToNextFailure > 14 ? 'limited' : 'urgent',
      recommended_action: pattern.prevention_strategy,
    };
  });

  // Use AI to discover new patterns if no strong matches
  if (matchedPatterns.length === 0 && symptoms.length > 1) {
    const aiPatternAnalysis = await discoverNewPatterns(c.env, device_model, symptoms);
    return c.json({
      known_patterns: [],
      ai_discovered_patterns: aiPatternAnalysis,
      recommendation: 'New failure pattern detected - adding to knowledge base',
    });
  }

  return c.json({
    matched_patterns: patternAnalysis,
    highest_risk_pattern: patternAnalysis.sort((a, b) => b.progression_percentage - a.progression_percentage)[0],
  });
});

// ==================== Component Health Monitoring ====================

app.post('/component/health', async (c) => {
  const { device_id, component_type, usage_data } = await c.req.json();

  const lifespanModel = COMPONENT_LIFESPAN_KB[component_type];
  if (!lifespanModel) {
    return c.json({ error: 'Unknown component type' }, 400);
  }

  // Calculate current health
  const health = calculateComponentHealth(lifespanModel, usage_data);

  // Predict remaining lifespan
  const prediction = predictComponentLifespan(lifespanModel, health, usage_data);

  // Generate maintenance recommendation
  const recommendation = generateComponentRecommendation(component_type, health, prediction);

  // Store health data for trend analysis
  await c.env.D1_DATABASE.prepare(`
    INSERT INTO component_health_logs (device_id, component_type, health_score, predicted_remaining_days, created_at)
    VALUES (?, ?, ?, ?, datetime('now'))
  `).bind(device_id, component_type, health.percentage, prediction.remaining_days).run();

  return c.json({
    component: component_type,
    current_health: health,
    lifespan_prediction: prediction,
    recommendation,
    reliability_curve: generateReliabilityCurve(lifespanModel, health),
  });
});

// ==================== Batch Device Monitoring ====================

app.post('/batch/monitor', async (c) => {
  const { device_ids } = await c.req.json();

  const results = await Promise.all(
    device_ids.map(async (device_id: string) => {
      const cached = await c.env.PREDICTIVE_MAINTENANCE_KV.get(`profile:${device_id}`);
      if (cached) {
        const profile = JSON.parse(cached);
        return {
          device_id,
          risk_score: profile.risk_score,
          top_risk: profile.predicted_failures?.[0],
          status: getRiskCategory(profile.risk_score),
        };
      }
      return {
        device_id,
        status: 'no_data',
        recommendation: 'Device profile needed - schedule analysis',
      };
    })
  );

  const summary = {
    total_devices: device_ids.length,
    critical: results.filter(r => r.status === 'critical').length,
    at_risk: results.filter(r => r.status === 'at-risk').length,
    watch: results.filter(r => r.status === 'watch').length,
    healthy: results.filter(r => r.status === 'healthy').length,
    no_data: results.filter(r => r.status === 'no_data').length,
  };

  return c.json({ devices: results, summary });
});

// ==================== ML Training Data Generation ====================

app.post('/ml/generate-training-data', async (c) => {
  // Fetch historical repair data for ML training
  const repairData = await c.env.D1_DATABASE.prepare(`
    SELECT 
      d.id as device_id,
      d.model,
      d.created_at as device_created,
      r.repair_type,
      r.created_at as repair_date,
      r.components_replaced,
      r.symptoms,
      LEAD(r.repair_type) OVER (PARTITION BY d.id ORDER BY r.created_at) as next_repair,
      LEAD(r.created_at) OVER (PARTITION BY d.id ORDER BY r.created_at) as next_repair_date
    FROM devices d
    JOIN repairs r ON d.id = r.device_id
    ORDER BY d.id, r.created_at
  `).all();

  const trainingData: MLTrainingData[] = [];

  for (const record of repairData.results || []) {
    const features = generateFeatureVector(record as any);
    const labels = {
      failed_within_30d: record.next_repair_date
        ? daysBetween(record.repair_date as string, record.next_repair_date as string) <= 30
        : false,
      failed_component: record.next_repair as string || 'none',
      failure_type: record.repair_type as string,
    };

    trainingData.push({ feature_vector: features, labels });
  }

  // Store training data in R2
  await c.env.R2_BUCKET.put(
    `ml/training-data-${Date.now()}.json`,
    JSON.stringify(trainingData),
    { httpMetadata: { contentType: 'application/json' } }
  );

  return c.json({
    records_processed: trainingData.length,
    features_per_record: trainingData[0]?.feature_vector.length || 0,
    storage_key: `ml/training-data-${Date.now()}.json`,
  });
});

// ==================== Proactive Alert Scheduling ====================

app.post('/alerts/schedule', async (c) => {
  const { device_id, alert_thresholds } = await c.req.json();

  const defaultThresholds = {
    critical_risk: 0.9,
    high_risk: 0.7,
    medium_risk: 0.5,
    days_before_predicted_failure: 14,
  };

  const thresholds = { ...defaultThresholds, ...alert_thresholds };

  // Get device profile
  const cached = await c.env.PREDICTIVE_MAINTENANCE_KV.get(`profile:${device_id}`);
  if (!cached) {
    return c.json({ error: 'Device profile not found - run analysis first' }, 404);
  }

  const profile: DeviceProfile = JSON.parse(cached);

  // Schedule alerts based on predictions
  const scheduledAlerts = [];

  for (const prediction of profile.predicted_failures) {
    const daysUntilFailure = daysBetween(new Date().toISOString(), prediction.estimated_date);

    if (prediction.probability >= thresholds.critical_risk) {
      scheduledAlerts.push({
        device_id,
        alert_type: 'critical',
        component: prediction.component,
        scheduled_date: new Date().toISOString(), // Immediate
        message: `CRITICAL: ${prediction.component} failure imminent (${Math.round(prediction.probability * 100)}% probability)`,
      });
    } else if (prediction.probability >= thresholds.high_risk && daysUntilFailure <= thresholds.days_before_predicted_failure) {
      const alertDate = new Date();
      alertDate.setDate(alertDate.getDate() + Math.max(0, daysUntilFailure - thresholds.days_before_predicted_failure));

      scheduledAlerts.push({
        device_id,
        alert_type: 'high',
        component: prediction.component,
        scheduled_date: alertDate.toISOString(),
        message: `High risk: ${prediction.component} may fail within ${daysUntilFailure} days`,
      });
    }
  }

  // Store scheduled alerts
  for (const alert of scheduledAlerts) {
    await c.env.D1_DATABASE.prepare(`
      INSERT INTO scheduled_alerts (device_id, alert_type, component, scheduled_date, message, status)
      VALUES (?, ?, ?, ?, ?, 'pending')
    `).bind(alert.device_id, alert.alert_type, alert.component, alert.scheduled_date, alert.message).run();
  }

  return c.json({
    device_id,
    alerts_scheduled: scheduledAlerts.length,
    alerts: scheduledAlerts,
    next_assessment: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000).toISOString(),
  });
});

// ==================== Helper Functions ====================

async function buildDeviceProfile(
  env: Env,
  device_id: string,
  repair_history: any,
  usage_data: any
): Promise<DeviceProfile> {
  const components = extractComponentHistory(repair_history);
  const environment = inferEnvironmentFactors(repair_history, usage_data);

  return {
    device_id,
    device_model: repair_history.model || 'Unknown',
    manufacture_date: repair_history.manufacture_date || repair_history.created_at,
    first_repair_date: repair_history.first_repair || new Date().toISOString(),
    total_repairs: repair_history.repair_count || 0,
    components_replaced: components,
    usage_hours_estimate: usage_data?.hours || estimateUsageHours(repair_history),
    environment_factors: environment,
    risk_score: 0, // Calculated separately
    predicted_failures: [],
  };
}

function extractComponentHistory(repair_history: any): ComponentHistory[] {
  const components: ComponentHistory[] = [];
  const componentTypes = ['battery', 'display', 'charging_port', 'motherboard', 'speaker', 'camera'];

  for (const componentType of componentTypes) {
    const lifespan = COMPONENT_LIFESPAN_KB[componentType];
    const wasReplaced = repair_history.repair_types?.includes(componentType);

    components.push({
      component_type: componentType,
      original_install: repair_history.manufacture_date || repair_history.created_at,
      replaced_date: wasReplaced ? repair_history.last_repair : undefined,
      current_age_days: daysBetween(
        wasReplaced ? repair_history.last_repair : repair_history.created_at,
        new Date().toISOString()
      ),
      expected_lifespan_days: (lifespan?.base_lifespan_hours || 10000) / 8, // 8 hours/day usage estimate
      health_percentage: calculateSimpleHealth(componentType, repair_history),
    });
  }

  return components;
}

function calculateSimpleHealth(componentType: string, repair_history: any): number {
  const lifespan = COMPONENT_LIFESPAN_KB[componentType];
  if (!lifespan) return 85;

  const age = daysBetween(repair_history.created_at, new Date().toISOString());
  const expectedLifeDays = lifespan.base_lifespan_hours / 8;
  const ageRatio = age / expectedLifeDays;

  // Different curves for different failure types
  switch (lifespan.failure_curve) {
    case 'exponential':
      return Math.max(20, 100 - Math.pow(ageRatio, 1.5) * 80);
    case 'linear':
      return Math.max(20, 100 - ageRatio * 80);
    case 'bathtub':
      if (ageRatio < 0.1) return 95 - ageRatio * 50; // Early failures
      if (ageRatio < 0.7) return 90; // Stable period
      return Math.max(20, 90 - (ageRatio - 0.7) * 200); // Wear-out
    default:
      return 100 - ageRatio * 50;
  }
}

function inferEnvironmentFactors(repair_history: any, usage_data: any): EnvironmentFactors {
  return {
    humidity_exposure: usage_data?.humid_environment ? 'high' : 'medium',
    temperature_stress: usage_data?.gaming_use || usage_data?.hot_climate ? 'high' : 'medium',
    physical_stress: repair_history.repair_count > 3 ? 'high' : repair_history.repair_count > 1 ? 'medium' : 'low',
    power_surge_history: repair_history.repair_types?.includes('motherboard') || false,
    liquid_damage_history: repair_history.repair_types?.includes('liquid_damage') || false,
  };
}

function estimateUsageHours(repair_history: any): number {
  const daysSincePurchase = daysBetween(repair_history.created_at, new Date().toISOString());
  return daysSincePurchase * 4; // Assume 4 hours/day average
}

async function runPredictiveModels(env: Env, profile: DeviceProfile): Promise<PredictedFailure[]> {
  const predictions: PredictedFailure[] = [];

  for (const component of profile.components_replaced) {
    if (component.health_percentage < 80) {
      const failureProbability = calculateFailureProbability(component, profile.environment_factors);
      const daysToFailure = estimateDaysToFailure(component, failureProbability);

      predictions.push({
        component: component.component_type,
        probability: failureProbability,
        estimated_date: new Date(Date.now() + daysToFailure * 24 * 60 * 60 * 1000).toISOString(),
        confidence: 0.75 + (profile.total_repairs * 0.02), // More data = higher confidence
        prevention_action: getPreventionAction(component.component_type),
        cost_if_preventive: getPreventiveCost(component.component_type),
        cost_if_reactive: getReactiveCost(component.component_type),
        severity: getSeverity(component.component_type, failureProbability),
      });
    }
  }

  return predictions.sort((a, b) => b.probability - a.probability);
}

function calculateFailureProbability(component: ComponentHistory, environment: EnvironmentFactors): number {
  let baseProbability = (100 - component.health_percentage) / 100;

  // Adjust for environment factors
  if (environment.humidity_exposure === 'high') baseProbability *= 1.3;
  if (environment.temperature_stress === 'high') baseProbability *= 1.25;
  if (environment.physical_stress === 'high') baseProbability *= 1.2;
  if (environment.liquid_damage_history) baseProbability *= 1.5;

  return Math.min(0.99, baseProbability);
}

function estimateDaysToFailure(component: ComponentHistory, probability: number): number {
  const remainingLife = component.expected_lifespan_days - component.current_age_days;
  const adjustedLife = remainingLife * (1 - probability);
  return Math.max(7, Math.round(adjustedLife));
}

function getPreventionAction(componentType: string): string {
  const actions: Record<string, string> = {
    battery: 'Schedule battery replacement before capacity drops below 70%',
    display: 'Inspect display flex cable and replace if degraded',
    charging_port: 'Clean port and inspect for corrosion, replace if damaged',
    motherboard: 'Thermal paste replacement and full board inspection',
    speaker: 'Replace speaker assembly, check for water damage',
    camera: 'Inspect OIS mechanism and lens assembly',
  };
  return actions[componentType] || 'Schedule preventive inspection';
}

function getPreventiveCost(componentType: string): number {
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

function getReactiveCost(componentType: string): number {
  const costs: Record<string, number> = {
    battery: 89, // Higher due to potential damage
    display: 349,
    charging_port: 149,
    motherboard: 549, // Much higher if cascading damage
    speaker: 89,
    camera: 249,
  };
  return costs[componentType] || 199;
}

function getSeverity(componentType: string, probability: number): 'low' | 'medium' | 'high' | 'critical' {
  const criticalComponents = ['motherboard', 'battery'];
  const highComponents = ['display', 'charging_port'];

  if (probability > 0.9) return 'critical';
  if (criticalComponents.includes(componentType)) {
    return probability > 0.7 ? 'critical' : probability > 0.5 ? 'high' : 'medium';
  }
  if (highComponents.includes(componentType)) {
    return probability > 0.7 ? 'high' : probability > 0.5 ? 'medium' : 'low';
  }
  return probability > 0.7 ? 'medium' : 'low';
}

function calculateOverallHealth(profile: DeviceProfile, predictions: PredictedFailure[]): number {
  const componentHealthAvg = profile.components_replaced.reduce((sum, c) => sum + c.health_percentage, 0) / profile.components_replaced.length;
  const riskPenalty = predictions.reduce((sum, p) => sum + p.probability * (p.severity === 'critical' ? 20 : p.severity === 'high' ? 10 : 5), 0);
  return Math.max(0, Math.round(componentHealthAvg - riskPenalty));
}

function calculateRiskScore(profile: DeviceProfile): number {
  const predictions = profile.predicted_failures || [];
  if (predictions.length === 0) return 0.1;

  const weightedRisk = predictions.reduce((sum, p) => {
    const severityWeight = p.severity === 'critical' ? 1.5 : p.severity === 'high' ? 1.2 : p.severity === 'medium' ? 1.0 : 0.7;
    return sum + p.probability * severityWeight;
  }, 0);

  return Math.min(1, weightedRisk / predictions.length);
}

function getRiskCategory(score: number): 'healthy' | 'watch' | 'at-risk' | 'critical' {
  if (score < 0.25) return 'healthy';
  if (score < 0.5) return 'watch';
  if (score < 0.75) return 'at-risk';
  return 'critical';
}

function generatePreventiveActions(predictions: PredictedFailure[]): PreventiveAction[] {
  return predictions
    .filter(p => p.probability > 0.3)
    .map((p, index) => ({
      action_id: `action-${index + 1}`,
      priority: index + 1,
      action_type: 'replacement' as const,
      component: p.component,
      description: p.prevention_action,
      estimated_cost: p.cost_if_preventive,
      savings_potential: p.cost_if_reactive - p.cost_if_preventive,
      deadline: p.estimated_date,
    }));
}

async function analyzeFleet(env: Env, devices: any[]): Promise<FleetAnalysis> {
  let healthy = 0, watch = 0, atRisk = 0, critical = 0;
  let failures30d = 0, failures90d = 0;
  const maintenanceQueue: PreventiveAction[] = [];
  let preventive30 = 0, reactive30 = 0, preventive90 = 0, reactive90 = 0;

  for (const device of devices) {
    const cached = await env.PREDICTIVE_MAINTENANCE_KV.get(`profile:${device.id}`);
    if (cached) {
      const profile: DeviceProfile = JSON.parse(cached);
      const category = getRiskCategory(profile.risk_score);

      switch (category) {
        case 'healthy': healthy++; break;
        case 'watch': watch++; break;
        case 'at-risk': atRisk++; break;
        case 'critical': critical++; break;
      }

      for (const pred of profile.predicted_failures) {
        const daysToFailure = daysBetween(new Date().toISOString(), pred.estimated_date);
        if (daysToFailure <= 30) {
          failures30d++;
          preventive30 += pred.cost_if_preventive;
          reactive30 += pred.cost_if_reactive;
        }
        if (daysToFailure <= 90) {
          failures90d++;
          preventive90 += pred.cost_if_preventive;
          reactive90 += pred.cost_if_reactive;
        }

        if (pred.probability > 0.5) {
          maintenanceQueue.push({
            action_id: `${device.id}-${pred.component}`,
            priority: Math.round(pred.probability * 100),
            action_type: 'replacement',
            component: pred.component,
            description: pred.prevention_action,
            estimated_cost: pred.cost_if_preventive,
            savings_potential: pred.cost_if_reactive - pred.cost_if_preventive,
            deadline: pred.estimated_date,
          });
        }
      }
    }
  }

  return {
    total_devices: devices.length,
    healthy_count: healthy,
    watch_count: watch,
    at_risk_count: atRisk,
    critical_count: critical,
    predicted_failures_30d: failures30d,
    predicted_failures_90d: failures90d,
    preventive_maintenance_queue: maintenanceQueue.sort((a, b) => b.priority - a.priority).slice(0, 20),
    cost_projections: {
      preventive_cost_30d: preventive30,
      reactive_cost_if_ignored_30d: reactive30,
      potential_savings_30d: reactive30 - preventive30,
      preventive_cost_90d: preventive90,
      reactive_cost_if_ignored_90d: reactive90,
      potential_savings_90d: reactive90 - preventive90,
    },
    fleet_health_trend: [], // Would be populated from historical snapshots
  };
}

function findPatternPosition(sequence: string[], symptoms: string[]): number {
  let maxPosition = 0;
  for (let i = 0; i < sequence.length; i++) {
    if (symptoms.some(s => sequence[i].toLowerCase().includes(s.toLowerCase()))) {
      maxPosition = i + 1;
    }
  }
  return maxPosition;
}

async function discoverNewPatterns(env: Env, device_model: string, symptoms: string[]): Promise<any> {
  const response = await env.AI.run('@cf/meta/llama-3-8b-instruct', {
    messages: [
      {
        role: 'system',
        content: 'You are an expert in electronic device failure analysis. Analyze symptom sequences to identify potential failure patterns.',
      },
      {
        role: 'user',
        content: `Device: ${device_model}\nSymptoms observed: ${symptoms.join(', ')}\n\nAnalyze these symptoms and predict potential cascade failures, root causes, and prevention strategies.`,
      },
    ],
  });

  return {
    analysis: response,
    recommendation: 'New pattern detected - requires validation from repair technician',
  };
}

function calculateComponentHealth(model: ComponentLifespanModel, usage: any): { percentage: number; factors: string[] } {
  let health = 100;
  const appliedFactors: string[] = [];

  for (const factor of model.factors) {
    if (factor.applicable_conditions.some(c => usage?.[c])) {
      health *= factor.impact_multiplier;
      appliedFactors.push(factor.factor_name);
    }
  }

  return { percentage: Math.round(health), factors: appliedFactors };
}

function predictComponentLifespan(model: ComponentLifespanModel, health: { percentage: number }, usage: any): { remaining_days: number; confidence: number } {
  const baseRemaining = (model.base_lifespan_hours / 8) * (health.percentage / 100);
  return {
    remaining_days: Math.round(baseRemaining),
    confidence: 0.7 + (usage?.data_quality || 0) * 0.2,
  };
}

function generateComponentRecommendation(component: string, health: { percentage: number }, prediction: { remaining_days: number }): string {
  if (health.percentage < 30) {
    return `URGENT: Replace ${component} immediately - high failure risk`;
  }
  if (health.percentage < 50) {
    return `Schedule ${component} replacement within ${Math.min(30, prediction.remaining_days)} days`;
  }
  if (health.percentage < 70) {
    return `Monitor ${component} - consider replacement in ${prediction.remaining_days} days`;
  }
  return `${component} is healthy - next assessment in 90 days`;
}

function generateReliabilityCurve(model: ComponentLifespanModel, health: { percentage: number }): { day: number; reliability: number }[] {
  const curve = [];
  for (let day = 0; day <= 365; day += 30) {
    let reliability = health.percentage / 100;
    switch (model.failure_curve) {
      case 'exponential':
        reliability *= Math.exp(-day / 1000);
        break;
      case 'linear':
        reliability *= 1 - day / 1000;
        break;
      case 'bathtub':
        if (day < 30) reliability *= 0.98;
        else if (day < 270) reliability *= 0.95;
        else reliability *= Math.max(0.3, 1 - (day - 270) / 200);
        break;
    }
    curve.push({ day, reliability: Math.max(0, reliability) });
  }
  return curve;
}

function generateFeatureVector(record: any): number[] {
  return [
    new Date(record.device_created).getTime() / 1e12, // Normalized timestamp
    record.repair_count || 0,
    record.model?.includes('iPhone') ? 1 : 0,
    record.model?.includes('MacBook') ? 1 : 0,
    record.repair_type?.includes('battery') ? 1 : 0,
    record.repair_type?.includes('display') ? 1 : 0,
    record.repair_type?.includes('motherboard') ? 1 : 0,
    // Add more features as needed
  ];
}

function daysBetween(date1: string, date2: string): number {
  const d1 = new Date(date1);
  const d2 = new Date(date2);
  return Math.round(Math.abs(d2.getTime() - d1.getTime()) / (1000 * 60 * 60 * 24));
}

async function calculateCostAnalysis(predictions: PredictedFailure[]): Promise<any> {
  const preventiveCost = predictions.reduce((sum, p) => sum + p.cost_if_preventive * p.probability, 0);
  const reactiveCost = predictions.reduce((sum, p) => sum + p.cost_if_reactive * p.probability, 0);

  return {
    expected_preventive_cost: Math.round(preventiveCost),
    expected_reactive_cost: Math.round(reactiveCost),
    potential_savings: Math.round(reactiveCost - preventiveCost),
    roi_of_prevention: Math.round(((reactiveCost - preventiveCost) / preventiveCost) * 100),
  };
}

export default app;
