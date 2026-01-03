/**
 * NoizyLab OS - Component Lifecycle Worker
 * 
 * Component Lifecycle Intelligence System:
 * - Battery health degradation tracking
 * - Component wear prediction curves
 * - Optimal replacement timing recommendations
 * - Failure probability scoring over time
 * - Environmental factor impact analysis
 * - Cost-benefit replacement analysis
 * - Proactive maintenance scheduling
 * - Fleet-wide component analytics
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
  DB: D1Database;
  CACHE: KVNamespace;
  AI: any;
  ALERTS_QUEUE: Queue;
}

interface ComponentHealth {
  componentId: string;
  componentType: string;
  currentHealth: number; // 0-100
  degradationRate: number; // % per month
  estimatedEOL: string;
  cycleCount?: number;
  maxCycles?: number;
  recommendations: HealthRecommendation[];
  riskLevel: 'healthy' | 'monitor' | 'warning' | 'critical';
}

interface HealthRecommendation {
  action: string;
  urgency: 'low' | 'medium' | 'high' | 'immediate';
  reason: string;
  estimatedCost: number;
  costIfIgnored: number;
  optimalWindow: { start: string; end: string };
}

interface DegradationCurve {
  componentType: string;
  model: string;
  dataPoints: { age: number; health: number }[];
  formula: string;
  r2Score: number;
  environmentalFactors: Record<string, number>;
}

interface LifecyclePrediction {
  deviceId: string;
  component: string;
  predictions: {
    months: number;
    health: number;
    failureProbability: number;
  }[];
  optimalReplacementDate: string;
  costAnalysis: CostAnalysis;
}

interface CostAnalysis {
  replaceNow: number;
  replaceOptimal: number;
  waitForFailure: number;
  recommendation: string;
}

const app = new Hono<{ Bindings: Env }>();

app.use('*', cors());

// =============================================================================
// COMPONENT DEGRADATION MODELS
// =============================================================================

const DEGRADATION_MODELS: Record<string, {
  baseLifespan: number; // months
  degradationCurve: 'linear' | 'exponential' | 'bathtub' | 'logarithmic';
  maxCycles?: number;
  environmentalSensitivity: Record<string, number>;
  criticalThreshold: number;
  warningThreshold: number;
}> = {
  'battery_lithium': {
    baseLifespan: 36, // 3 years
    degradationCurve: 'exponential',
    maxCycles: 1000,
    environmentalSensitivity: {
      temperature_high: 1.5,
      temperature_low: 1.2,
      humidity: 1.1,
      charge_frequency: 0.8
    },
    criticalThreshold: 60,
    warningThreshold: 75
  },
  'screen_lcd': {
    baseLifespan: 60,
    degradationCurve: 'linear',
    environmentalSensitivity: {
      brightness_usage: 1.3,
      burn_in_risk: 1.2,
      impact_history: 2.0
    },
    criticalThreshold: 70,
    warningThreshold: 80
  },
  'screen_oled': {
    baseLifespan: 48,
    degradationCurve: 'logarithmic',
    environmentalSensitivity: {
      brightness_usage: 1.5,
      burn_in_risk: 1.8,
      impact_history: 2.0
    },
    criticalThreshold: 65,
    warningThreshold: 78
  },
  'keyboard_mechanical': {
    baseLifespan: 84, // 7 years
    degradationCurve: 'bathtub',
    maxCycles: 50000000,
    environmentalSensitivity: {
      dust_exposure: 1.3,
      liquid_exposure: 3.0,
      heavy_usage: 1.2
    },
    criticalThreshold: 50,
    warningThreshold: 70
  },
  'keyboard_membrane': {
    baseLifespan: 48,
    degradationCurve: 'linear',
    maxCycles: 5000000,
    environmentalSensitivity: {
      dust_exposure: 1.4,
      liquid_exposure: 2.5,
      heavy_usage: 1.4
    },
    criticalThreshold: 40,
    warningThreshold: 60
  },
  'hdd_mechanical': {
    baseLifespan: 60,
    degradationCurve: 'bathtub',
    environmentalSensitivity: {
      shock_events: 2.5,
      temperature_high: 1.4,
      power_cycles: 1.2,
      operating_hours: 1.1
    },
    criticalThreshold: 70,
    warningThreshold: 85
  },
  'ssd_nand': {
    baseLifespan: 84,
    degradationCurve: 'linear',
    maxCycles: 3000, // TBW equivalent
    environmentalSensitivity: {
      write_intensity: 1.5,
      temperature_high: 1.3
    },
    criticalThreshold: 75,
    warningThreshold: 85
  },
  'fan_cooling': {
    baseLifespan: 48,
    degradationCurve: 'exponential',
    environmentalSensitivity: {
      dust_exposure: 2.0,
      continuous_operation: 1.3,
      temperature_high: 1.2
    },
    criticalThreshold: 50,
    warningThreshold: 70
  },
  'charging_port': {
    baseLifespan: 36,
    degradationCurve: 'logarithmic',
    maxCycles: 10000,
    environmentalSensitivity: {
      insertion_frequency: 1.5,
      debris_exposure: 1.8,
      cable_quality: 1.3
    },
    criticalThreshold: 60,
    warningThreshold: 75
  },
  'speaker': {
    baseLifespan: 72,
    degradationCurve: 'linear',
    environmentalSensitivity: {
      volume_level: 1.6,
      moisture_exposure: 2.0,
      debris_exposure: 1.4
    },
    criticalThreshold: 65,
    warningThreshold: 80
  }
};

// =============================================================================
// COMPONENT HEALTH CHECK
// =============================================================================

app.post('/api/health/check', async (c) => {
  const { deviceId, componentType, metrics } = await c.req.json();
  
  // Get component record
  const component = await c.env.DB.prepare(`
    SELECT * FROM device_components
    WHERE device_id = ? AND component_type = ?
  `).bind(deviceId, componentType).first();
  
  // Get degradation model
  const model = DEGRADATION_MODELS[normalizeComponentType(componentType)];
  if (!model) {
    return c.json({ error: 'Unknown component type' }, 400);
  }
  
  // Calculate current health
  const installDate = component?.install_date 
    ? new Date(component.install_date as string)
    : new Date();
  const ageMonths = (Date.now() - installDate.getTime()) / (1000 * 60 * 60 * 24 * 30);
  
  // Get environmental factors
  const environmentalImpact = await calculateEnvironmentalImpact(
    c.env, deviceId, componentType, model.environmentalSensitivity
  );
  
  // Calculate health based on degradation curve
  const baseHealth = calculateHealthFromCurve(
    model.degradationCurve,
    ageMonths,
    model.baseLifespan,
    environmentalImpact
  );
  
  // Adjust for cycle count if applicable
  let cycleAdjustedHealth = baseHealth;
  if (model.maxCycles && metrics?.cycleCount) {
    const cycleHealth = 100 - (metrics.cycleCount / model.maxCycles * 100);
    cycleAdjustedHealth = Math.min(baseHealth, cycleHealth);
  }
  
  // Adjust for current metrics (e.g., battery diagnostics)
  const metricsAdjustedHealth = adjustForMetrics(cycleAdjustedHealth, metrics, componentType);
  
  // Determine risk level
  let riskLevel: 'healthy' | 'monitor' | 'warning' | 'critical' = 'healthy';
  if (metricsAdjustedHealth <= model.criticalThreshold) riskLevel = 'critical';
  else if (metricsAdjustedHealth <= model.warningThreshold) riskLevel = 'warning';
  else if (metricsAdjustedHealth <= model.warningThreshold + 10) riskLevel = 'monitor';
  
  // Generate recommendations
  const recommendations = generateRecommendations(
    componentType,
    metricsAdjustedHealth,
    riskLevel,
    ageMonths,
    model
  );
  
  // Calculate degradation rate
  const degradationRate = calculateDegradationRate(c.env, deviceId, componentType, ageMonths);
  
  // Estimate EOL
  const monthsToEOL = (metricsAdjustedHealth - model.criticalThreshold) / (degradationRate / 30);
  const estimatedEOL = new Date(Date.now() + monthsToEOL * 30 * 24 * 60 * 60 * 1000);
  
  const health: ComponentHealth = {
    componentId: component?.id as string || crypto.randomUUID(),
    componentType,
    currentHealth: Math.round(metricsAdjustedHealth * 10) / 10,
    degradationRate,
    estimatedEOL: estimatedEOL.toISOString().split('T')[0],
    cycleCount: metrics?.cycleCount,
    maxCycles: model.maxCycles,
    recommendations,
    riskLevel
  };
  
  // Store health check
  await storeHealthCheck(c.env, deviceId, health);
  
  // Alert if critical
  if (riskLevel === 'critical') {
    await c.env.ALERTS_QUEUE.send({
      type: 'component_critical',
      deviceId,
      componentType,
      health: metricsAdjustedHealth,
      estimatedEOL: health.estimatedEOL,
      timestamp: Date.now()
    });
  }
  
  return c.json(health);
});

function normalizeComponentType(type: string): string {
  const lower = type.toLowerCase();
  
  if (lower.includes('battery')) return 'battery_lithium';
  if (lower.includes('oled')) return 'screen_oled';
  if (lower.includes('lcd') || lower.includes('screen') || lower.includes('display')) return 'screen_lcd';
  if (lower.includes('mechanical') && lower.includes('keyboard')) return 'keyboard_mechanical';
  if (lower.includes('keyboard')) return 'keyboard_membrane';
  if (lower.includes('hdd') || lower.includes('hard drive')) return 'hdd_mechanical';
  if (lower.includes('ssd') || lower.includes('flash')) return 'ssd_nand';
  if (lower.includes('fan') || lower.includes('cooling')) return 'fan_cooling';
  if (lower.includes('charging') || lower.includes('port') || lower.includes('usb')) return 'charging_port';
  if (lower.includes('speaker') || lower.includes('audio')) return 'speaker';
  
  return 'battery_lithium'; // Safe default
}

function calculateHealthFromCurve(
  curve: string,
  ageMonths: number,
  baseLifespan: number,
  environmentalImpact: number
): number {
  const adjustedLifespan = baseLifespan / environmentalImpact;
  const ageRatio = ageMonths / adjustedLifespan;
  
  switch (curve) {
    case 'linear':
      return Math.max(0, 100 - (ageRatio * 100));
    
    case 'exponential':
      // Faster degradation over time
      return Math.max(0, 100 * Math.exp(-2 * ageRatio));
    
    case 'logarithmic':
      // Fast initial degradation, then slows
      return Math.max(0, 100 - 30 * Math.log(1 + ageRatio * 3));
    
    case 'bathtub':
      // High failure early, stable middle, high failure late
      if (ageRatio < 0.1) {
        return 100 - (0.1 - ageRatio) * 50; // Infant mortality
      } else if (ageRatio < 0.8) {
        return 100 - ageRatio * 20; // Stable period
      } else {
        return Math.max(0, 100 - ageRatio * 80); // Wear-out
      }
    
    default:
      return Math.max(0, 100 - (ageRatio * 100));
  }
}

async function calculateEnvironmentalImpact(
  env: Env,
  deviceId: string,
  componentType: string,
  sensitivity: Record<string, number>
): Promise<number> {
  // Get environmental history for device
  const envHistory = await env.DB.prepare(`
    SELECT 
      AVG(temperature) as avg_temp,
      MAX(temperature) as max_temp,
      AVG(humidity) as avg_humidity,
      SUM(impact_events) as total_impacts,
      SUM(usage_hours) as total_hours
    FROM device_environment_logs
    WHERE device_id = ?
  `).bind(deviceId).first();
  
  let impact = 1.0;
  
  if (envHistory) {
    // Temperature impact
    if ((envHistory.max_temp as number) > 45) {
      impact *= sensitivity.temperature_high || 1.0;
    }
    if ((envHistory.avg_temp as number) < 10) {
      impact *= sensitivity.temperature_low || 1.0;
    }
    
    // Humidity impact
    if ((envHistory.avg_humidity as number) > 70) {
      impact *= sensitivity.humidity || 1.0;
    }
    
    // Impact/shock events
    if ((envHistory.total_impacts as number) > 5) {
      impact *= sensitivity.impact_history || sensitivity.shock_events || 1.0;
    }
    
    // Heavy usage
    if ((envHistory.total_hours as number) > 3000) {
      impact *= sensitivity.heavy_usage || sensitivity.continuous_operation || 1.0;
    }
  }
  
  return impact;
}

function adjustForMetrics(health: number, metrics: any, componentType: string): number {
  if (!metrics) return health;
  
  // Battery-specific adjustments
  if (componentType.includes('battery')) {
    if (metrics.maxCapacity) {
      // Apple-style max capacity reporting
      health = Math.min(health, metrics.maxCapacity);
    }
    if (metrics.peakPerformance === false) {
      health *= 0.9; // Performance throttling active
    }
  }
  
  // Storage-specific adjustments
  if (componentType.includes('ssd') || componentType.includes('hdd')) {
    if (metrics.reallocatedSectors > 0) {
      health -= metrics.reallocatedSectors * 2;
    }
    if (metrics.pendingSectors > 0) {
      health -= metrics.pendingSectors * 5;
    }
    if (metrics.smartWarning) {
      health *= 0.7;
    }
  }
  
  // Screen-specific adjustments
  if (componentType.includes('screen')) {
    if (metrics.deadPixels > 0) {
      health -= metrics.deadPixels * 3;
    }
    if (metrics.burnIn) {
      health *= 0.8;
    }
  }
  
  return Math.max(0, Math.min(100, health));
}

function generateRecommendations(
  componentType: string,
  health: number,
  riskLevel: string,
  ageMonths: number,
  model: any
): HealthRecommendation[] {
  const recommendations: HealthRecommendation[] = [];
  const now = new Date();
  
  // Get replacement cost estimates
  const costs = getReplacementCosts(componentType);
  
  if (riskLevel === 'critical') {
    recommendations.push({
      action: 'Replace immediately',
      urgency: 'immediate',
      reason: `Component health (${health.toFixed(0)}%) below critical threshold (${model.criticalThreshold}%)`,
      estimatedCost: costs.replacement,
      costIfIgnored: costs.replacement * 2 + costs.collateralDamage,
      optimalWindow: {
        start: now.toISOString().split('T')[0],
        end: new Date(now.getTime() + 14 * 24 * 60 * 60 * 1000).toISOString().split('T')[0]
      }
    });
  } else if (riskLevel === 'warning') {
    recommendations.push({
      action: 'Schedule replacement',
      urgency: 'high',
      reason: `Component health (${health.toFixed(0)}%) approaching critical levels`,
      estimatedCost: costs.replacement,
      costIfIgnored: costs.replacement * 1.5,
      optimalWindow: {
        start: new Date(now.getTime() + 14 * 24 * 60 * 60 * 1000).toISOString().split('T')[0],
        end: new Date(now.getTime() + 60 * 24 * 60 * 60 * 1000).toISOString().split('T')[0]
      }
    });
    
    // Add preventive maintenance
    recommendations.push({
      action: 'Perform preventive maintenance',
      urgency: 'medium',
      reason: 'May extend component life by 10-20%',
      estimatedCost: costs.maintenance,
      costIfIgnored: costs.replacement * 0.3,
      optimalWindow: {
        start: now.toISOString().split('T')[0],
        end: new Date(now.getTime() + 30 * 24 * 60 * 60 * 1000).toISOString().split('T')[0]
      }
    });
  } else if (riskLevel === 'monitor') {
    recommendations.push({
      action: 'Monitor closely',
      urgency: 'low',
      reason: 'Component showing early signs of wear',
      estimatedCost: 0,
      costIfIgnored: costs.replacement * 0.1,
      optimalWindow: {
        start: now.toISOString().split('T')[0],
        end: new Date(now.getTime() + 90 * 24 * 60 * 60 * 1000).toISOString().split('T')[0]
      }
    });
  }
  
  // Component-specific recommendations
  if (componentType.includes('battery') && health < 85) {
    recommendations.push({
      action: 'Calibrate battery',
      urgency: 'low',
      reason: 'Battery calibration can improve accuracy of health readings',
      estimatedCost: 0,
      costIfIgnored: costs.maintenance * 0.5,
      optimalWindow: {
        start: now.toISOString().split('T')[0],
        end: new Date(now.getTime() + 30 * 24 * 60 * 60 * 1000).toISOString().split('T')[0]
      }
    });
  }
  
  if (componentType.includes('fan') && health < 80) {
    recommendations.push({
      action: 'Clean and lubricate',
      urgency: 'medium',
      reason: 'Fan cleaning can significantly extend lifespan',
      estimatedCost: costs.maintenance,
      costIfIgnored: costs.replacement,
      optimalWindow: {
        start: now.toISOString().split('T')[0],
        end: new Date(now.getTime() + 14 * 24 * 60 * 60 * 1000).toISOString().split('T')[0]
      }
    });
  }
  
  return recommendations;
}

function getReplacementCosts(componentType: string): { replacement: number; maintenance: number; collateralDamage: number } {
  const costs: Record<string, { replacement: number; maintenance: number; collateralDamage: number }> = {
    'battery_lithium': { replacement: 80, maintenance: 20, collateralDamage: 200 },
    'screen_lcd': { replacement: 150, maintenance: 30, collateralDamage: 100 },
    'screen_oled': { replacement: 250, maintenance: 40, collateralDamage: 150 },
    'keyboard_mechanical': { replacement: 120, maintenance: 25, collateralDamage: 50 },
    'keyboard_membrane': { replacement: 80, maintenance: 15, collateralDamage: 30 },
    'hdd_mechanical': { replacement: 100, maintenance: 20, collateralDamage: 500 }, // Data loss risk
    'ssd_nand': { replacement: 150, maintenance: 0, collateralDamage: 500 },
    'fan_cooling': { replacement: 50, maintenance: 15, collateralDamage: 300 }, // Thermal damage
    'charging_port': { replacement: 60, maintenance: 15, collateralDamage: 100 },
    'speaker': { replacement: 40, maintenance: 10, collateralDamage: 20 }
  };
  
  return costs[componentType] || { replacement: 100, maintenance: 20, collateralDamage: 100 };
}

function calculateDegradationRate(env: Env, deviceId: string, componentType: string, ageMonths: number): number {
  // Simple degradation rate calculation
  // In production, this would use historical health check data
  const model = DEGRADATION_MODELS[normalizeComponentType(componentType)];
  if (!model) return 2.5; // Default 2.5% per month
  
  // Base rate from lifespan
  const baseRate = 100 / model.baseLifespan;
  
  // Adjust for curve type
  switch (model.degradationCurve) {
    case 'exponential':
      return baseRate * (1 + ageMonths / model.baseLifespan);
    case 'logarithmic':
      return baseRate / (1 + ageMonths / 12);
    case 'bathtub':
      if (ageMonths < model.baseLifespan * 0.1 || ageMonths > model.baseLifespan * 0.8) {
        return baseRate * 2;
      }
      return baseRate * 0.5;
    default:
      return baseRate;
  }
}

async function storeHealthCheck(env: Env, deviceId: string, health: ComponentHealth): Promise<void> {
  await env.DB.prepare(`
    INSERT INTO component_health_history (
      device_id, component_type, health_score, risk_level,
      degradation_rate, estimated_eol, created_at
    ) VALUES (?, ?, ?, ?, ?, ?, datetime('now'))
  `).bind(
    deviceId,
    health.componentType,
    health.currentHealth,
    health.riskLevel,
    health.degradationRate,
    health.estimatedEOL
  ).run();
}

// =============================================================================
// LIFECYCLE PREDICTION
// =============================================================================

app.get('/api/predict/:deviceId/:component', async (c) => {
  const deviceId = c.req.param('deviceId');
  const component = c.req.param('component');
  
  // Get current health
  const currentHealth = await c.env.DB.prepare(`
    SELECT * FROM component_health_history
    WHERE device_id = ? AND component_type = ?
    ORDER BY created_at DESC LIMIT 1
  `).bind(deviceId, component).first();
  
  if (!currentHealth) {
    return c.json({ error: 'No health data available' }, 404);
  }
  
  const model = DEGRADATION_MODELS[normalizeComponentType(component)];
  const health = currentHealth.health_score as number;
  const degradationRate = currentHealth.degradation_rate as number;
  
  // Generate predictions for next 24 months
  const predictions: { months: number; health: number; failureProbability: number }[] = [];
  
  for (let months = 1; months <= 24; months++) {
    const predictedHealth = Math.max(0, health - (degradationRate * months));
    const failureProbability = calculateFailureProbability(
      predictedHealth,
      model?.criticalThreshold || 60
    );
    
    predictions.push({
      months,
      health: Math.round(predictedHealth * 10) / 10,
      failureProbability: Math.round(failureProbability * 1000) / 1000
    });
  }
  
  // Find optimal replacement date
  const optimalMonth = findOptimalReplacementMonth(predictions, model);
  const optimalDate = new Date();
  optimalDate.setMonth(optimalDate.getMonth() + optimalMonth);
  
  // Cost analysis
  const costs = getReplacementCosts(normalizeComponentType(component));
  const costAnalysis = calculateCostAnalysis(predictions, costs, optimalMonth);
  
  const prediction: LifecyclePrediction = {
    deviceId,
    component,
    predictions,
    optimalReplacementDate: optimalDate.toISOString().split('T')[0],
    costAnalysis
  };
  
  return c.json(prediction);
});

function calculateFailureProbability(health: number, criticalThreshold: number): number {
  if (health <= criticalThreshold) {
    return 0.9 + (criticalThreshold - health) * 0.01;
  }
  
  // Sigmoid function centered at critical threshold
  const x = (criticalThreshold - health) / 10;
  return 1 / (1 + Math.exp(-x));
}

function findOptimalReplacementMonth(
  predictions: { months: number; health: number; failureProbability: number }[],
  model: any
): number {
  const criticalThreshold = model?.criticalThreshold || 60;
  const warningThreshold = model?.warningThreshold || 75;
  
  // Find month where health crosses warning threshold
  for (const p of predictions) {
    if (p.health <= warningThreshold) {
      return Math.max(1, p.months - 1); // Replace month before warning
    }
  }
  
  return 12; // Default to 12 months if no critical point found
}

function calculateCostAnalysis(
  predictions: { months: number; health: number; failureProbability: number }[],
  costs: { replacement: number; maintenance: number; collateralDamage: number },
  optimalMonth: number
): CostAnalysis {
  // Cost if replaced now
  const replaceNow = costs.replacement;
  
  // Cost if replaced at optimal time (may have maintenance costs)
  const replaceOptimal = costs.replacement + costs.maintenance;
  
  // Expected cost if waiting for failure
  const failureProb = predictions[Math.min(optimalMonth + 6, predictions.length - 1)]?.failureProbability || 0.5;
  const waitForFailure = costs.replacement * 1.3 + // Emergency premium
                          costs.collateralDamage * failureProb +
                          costs.maintenance * 3; // Multiple maintenance attempts
  
  let recommendation = '';
  if (replaceNow <= replaceOptimal * 0.9) {
    recommendation = 'Replace now for best value';
  } else if (replaceOptimal < waitForFailure * 0.7) {
    recommendation = `Schedule replacement in ${optimalMonth} months for optimal cost`;
  } else {
    recommendation = 'Monitor and reassess in 3 months';
  }
  
  return {
    replaceNow: Math.round(replaceNow),
    replaceOptimal: Math.round(replaceOptimal),
    waitForFailure: Math.round(waitForFailure),
    recommendation
  };
}

// =============================================================================
// FLEET ANALYTICS
// =============================================================================

app.get('/api/fleet/health', async (c) => {
  const componentType = c.req.query('type');
  
  let query = `
    SELECT 
      component_type,
      COUNT(*) as total_devices,
      AVG(health_score) as avg_health,
      SUM(CASE WHEN risk_level = 'critical' THEN 1 ELSE 0 END) as critical_count,
      SUM(CASE WHEN risk_level = 'warning' THEN 1 ELSE 0 END) as warning_count,
      SUM(CASE WHEN risk_level = 'monitor' THEN 1 ELSE 0 END) as monitor_count,
      SUM(CASE WHEN risk_level = 'healthy' THEN 1 ELSE 0 END) as healthy_count,
      AVG(degradation_rate) as avg_degradation_rate
    FROM (
      SELECT DISTINCT ON (device_id, component_type) *
      FROM component_health_history
      ORDER BY device_id, component_type, created_at DESC
    ) latest_health
  `;
  
  if (componentType) {
    query += ` WHERE component_type = '${componentType}'`;
  }
  
  query += ` GROUP BY component_type ORDER BY critical_count DESC`;
  
  const fleetHealth = await c.env.DB.prepare(query).all();
  
  // Calculate fleet-wide metrics
  const totalDevices = fleetHealth.results?.reduce((sum: number, r: any) => sum + r.total_devices, 0) || 0;
  const criticalTotal = fleetHealth.results?.reduce((sum: number, r: any) => sum + r.critical_count, 0) || 0;
  
  // Predict upcoming failures
  const upcomingFailures = await c.env.DB.prepare(`
    SELECT device_id, component_type, health_score, estimated_eol
    FROM component_health_history
    WHERE estimated_eol < date('now', '+30 days')
      AND health_score < 75
    ORDER BY estimated_eol ASC
    LIMIT 20
  `).all();
  
  return c.json({
    byComponent: fleetHealth.results,
    summary: {
      totalDevicesMonitored: totalDevices,
      criticalComponents: criticalTotal,
      fleetHealthScore: fleetHealth.results?.[0]?.avg_health || 0
    },
    upcomingFailures: upcomingFailures.results,
    maintenanceSchedule: generateMaintenanceSchedule(fleetHealth.results || [])
  });
});

function generateMaintenanceSchedule(fleetData: any[]): any[] {
  const schedule = [];
  const now = new Date();
  
  for (const component of fleetData) {
    if (component.critical_count > 0) {
      schedule.push({
        componentType: component.component_type,
        priority: 'immediate',
        deviceCount: component.critical_count,
        suggestedDate: now.toISOString().split('T')[0],
        estimatedHours: component.critical_count * 0.5
      });
    }
    
    if (component.warning_count > 0) {
      const warningDate = new Date(now.getTime() + 14 * 24 * 60 * 60 * 1000);
      schedule.push({
        componentType: component.component_type,
        priority: 'scheduled',
        deviceCount: component.warning_count,
        suggestedDate: warningDate.toISOString().split('T')[0],
        estimatedHours: component.warning_count * 0.5
      });
    }
  }
  
  return schedule.sort((a, b) => {
    const priorityOrder = { immediate: 0, scheduled: 1, preventive: 2 };
    return priorityOrder[a.priority as keyof typeof priorityOrder] - priorityOrder[b.priority as keyof typeof priorityOrder];
  });
}

// =============================================================================
// DEGRADATION CURVE LEARNING
// =============================================================================

app.post('/api/learn/curve', async (c) => {
  const { componentType } = await c.req.json();
  
  // Get historical health data for this component type
  const historicalData = await c.env.DB.prepare(`
    SELECT 
      device_id,
      health_score,
      julianday(created_at) - julianday(
        (SELECT MIN(created_at) FROM component_health_history h2 
         WHERE h2.device_id = component_health_history.device_id 
         AND h2.component_type = component_health_history.component_type)
      ) as days_since_install
    FROM component_health_history
    WHERE component_type = ?
    ORDER BY device_id, created_at
  `).bind(componentType).all();
  
  if (!historicalData.results || historicalData.results.length < 50) {
    return c.json({ error: 'Insufficient data for curve learning' }, 400);
  }
  
  // Convert to data points
  const dataPoints = historicalData.results.map((r: any) => ({
    age: r.days_since_install / 30, // Convert to months
    health: r.health_score
  }));
  
  // Use AI to fit best curve
  const response = await c.env.AI.run('@cf/meta/llama-3-8b-instruct', {
    messages: [
      {
        role: 'system',
        content: `You are a data scientist analyzing component degradation patterns.
        Given health data points (age in months, health score 0-100), determine the best fitting degradation curve.
        
        Respond with JSON:
        {
          "curveType": "linear|exponential|logarithmic|bathtub",
          "formula": "health = ...",
          "r2Score": 0.XX,
          "baseLifespan": XX,
          "insights": "brief insight about degradation pattern"
        }`
      },
      {
        role: 'user',
        content: `Analyze these degradation data points for ${componentType}: ${JSON.stringify(dataPoints.slice(0, 100))}`
      }
    ]
  });
  
  try {
    const analysis = JSON.parse(response.response);
    
    // Store learned curve
    await c.env.DB.prepare(`
      INSERT OR REPLACE INTO learned_degradation_curves (
        component_type, curve_type, formula, r2_score, base_lifespan, data_points, updated_at
      ) VALUES (?, ?, ?, ?, ?, ?, datetime('now'))
    `).bind(
      componentType,
      analysis.curveType,
      analysis.formula,
      analysis.r2Score,
      analysis.baseLifespan,
      dataPoints.length
    ).run();
    
    return c.json({
      componentType,
      learnedCurve: analysis,
      dataPointsUsed: dataPoints.length,
      status: 'curve_updated'
    });
  } catch (e) {
    return c.json({ error: 'Failed to analyze degradation pattern' }, 500);
  }
});

export default app;
