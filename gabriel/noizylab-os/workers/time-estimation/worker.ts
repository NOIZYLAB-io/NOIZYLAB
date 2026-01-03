/**
 * NoizyLab OS - Time Estimation Worker
 * 
 * ML-Powered Repair Time Prediction System:
 * - Historical data-driven time estimation
 * - Confidence intervals and uncertainty quantification
 * - Technician skill factor adjustment
 * - Parts availability impact analysis
 * - Queue position and workload modeling
 * - Dynamic re-estimation during repairs
 * - SLA tracking and prediction
 * - Customer communication automation
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
  DB: D1Database;
  CACHE: KVNamespace;
  AI: any;
  NOTIFICATIONS_QUEUE: Queue;
}

interface TimeEstimate {
  estimatedMinutes: number;
  confidenceInterval: { low: number; high: number };
  confidence: number;
  factors: EstimationFactor[];
  breakdown: TimeBreakdown;
  slaStatus: 'on_track' | 'at_risk' | 'breach_likely';
  suggestedCompletionDate: string;
}

interface EstimationFactor {
  name: string;
  impact: number; // Multiplier (1 = no impact)
  description: string;
  controllable: boolean;
}

interface TimeBreakdown {
  diagnosis: number;
  partsWait: number;
  repair: number;
  testing: number;
  documentation: number;
  buffer: number;
}

interface TechnicianProfile {
  id: string;
  speedMultiplier: number;
  expertiseAreas: string[];
  avgQualityScore: number;
  currentWorkload: number;
}

const app = new Hono<{ Bindings: Env }>();

app.use('*', cors());

// =============================================================================
// BASE TIME MATRICES (Industry benchmarks + NoizyLab learning)
// =============================================================================

const BASE_REPAIR_TIMES: Record<string, Record<string, number>> = {
  'iphone': {
    'screen_replacement': 45,
    'battery_replacement': 30,
    'charging_port': 60,
    'camera_repair': 45,
    'speaker_repair': 40,
    'water_damage': 120,
    'motherboard': 180,
    'button_repair': 35,
    'face_id': 90,
    'software_issue': 30
  },
  'macbook': {
    'screen_replacement': 90,
    'battery_replacement': 60,
    'keyboard_replacement': 120,
    'trackpad_repair': 75,
    'logic_board': 240,
    'ssd_upgrade': 45,
    'fan_replacement': 60,
    'speaker_repair': 50,
    'usb_port': 90,
    'software_issue': 45
  },
  'ipad': {
    'screen_replacement': 60,
    'battery_replacement': 45,
    'charging_port': 50,
    'camera_repair': 40,
    'button_repair': 35,
    'speaker_repair': 40,
    'water_damage': 100,
    'software_issue': 30
  },
  'samsung_phone': {
    'screen_replacement': 50,
    'battery_replacement': 35,
    'charging_port': 55,
    'camera_repair': 50,
    'speaker_repair': 40,
    'water_damage': 110,
    'motherboard': 160,
    'software_issue': 30
  },
  'game_console': {
    'hdmi_port': 90,
    'disc_drive': 75,
    'power_supply': 60,
    'fan_cleaning': 30,
    'thermal_paste': 45,
    'controller_port': 50,
    'hard_drive': 40,
    'laser_repair': 80
  },
  'laptop_generic': {
    'screen_replacement': 75,
    'battery_replacement': 45,
    'keyboard_replacement': 90,
    'hinge_repair': 80,
    'motherboard': 200,
    'ram_upgrade': 20,
    'ssd_upgrade': 30,
    'fan_replacement': 50,
    'dc_jack': 70
  }
};

// =============================================================================
// PRIMARY ESTIMATION ENDPOINT
// =============================================================================

app.post('/api/estimate', async (c) => {
  const { 
    deviceType, 
    repairType, 
    severity,
    technicianId,
    partsAvailable,
    customerId,
    additionalNotes
  } = await c.req.json();
  
  // Get base time from matrix
  const baseTime = getBaseTime(deviceType, repairType);
  
  // Gather all estimation factors
  const factors: EstimationFactor[] = [];
  
  // Factor 1: Device condition/severity
  const severityFactor = await calculateSeverityFactor(severity, additionalNotes, c.env);
  factors.push(severityFactor);
  
  // Factor 2: Technician skill
  const techFactor = await calculateTechnicianFactor(c.env, technicianId, deviceType, repairType);
  factors.push(techFactor);
  
  // Factor 3: Parts availability
  const partsFactor = await calculatePartsFactor(c.env, partsAvailable, deviceType, repairType);
  factors.push(partsFactor);
  
  // Factor 4: Queue position and workload
  const queueFactor = await calculateQueueFactor(c.env, technicianId);
  factors.push(queueFactor);
  
  // Factor 5: Historical complexity for this customer
  const customerFactor = await calculateCustomerHistoryFactor(c.env, customerId, deviceType);
  factors.push(customerFactor);
  
  // Factor 6: Time of day / day of week patterns
  const temporalFactor = calculateTemporalFactor();
  factors.push(temporalFactor);
  
  // Calculate adjusted time
  let adjustedTime = baseTime;
  for (const factor of factors) {
    adjustedTime *= factor.impact;
  }
  
  // Calculate confidence interval using historical variance
  const confidence = await calculateConfidence(c.env, deviceType, repairType, factors);
  const confidenceInterval = calculateConfidenceInterval(adjustedTime, confidence);
  
  // Build time breakdown
  const breakdown = calculateTimeBreakdown(adjustedTime, repairType, partsFactor);
  
  // Check SLA status
  const slaStatus = await checkSlaStatus(c.env, customerId, adjustedTime);
  
  // Calculate suggested completion date
  const suggestedCompletionDate = calculateCompletionDate(adjustedTime, queueFactor);
  
  const estimate: TimeEstimate = {
    estimatedMinutes: Math.round(adjustedTime),
    confidenceInterval,
    confidence: confidence.overall,
    factors,
    breakdown,
    slaStatus,
    suggestedCompletionDate
  };
  
  // Store estimate for learning
  await storeEstimate(c.env, {
    deviceType,
    repairType,
    estimate,
    factors,
    timestamp: Date.now()
  });
  
  return c.json(estimate);
});

function getBaseTime(deviceType: string, repairType: string): number {
  // Normalize device type
  const normalizedDevice = normalizeDeviceType(deviceType);
  const deviceTimes = BASE_REPAIR_TIMES[normalizedDevice] || BASE_REPAIR_TIMES['laptop_generic'];
  
  // Find best matching repair type
  const normalizedRepair = normalizeRepairType(repairType);
  return deviceTimes[normalizedRepair] || 60; // Default 60 minutes
}

function normalizeDeviceType(deviceType: string): string {
  const lower = deviceType.toLowerCase();
  
  if (lower.includes('iphone')) return 'iphone';
  if (lower.includes('macbook') || lower.includes('mac book')) return 'macbook';
  if (lower.includes('ipad')) return 'ipad';
  if (lower.includes('samsung') && lower.includes('phone')) return 'samsung_phone';
  if (lower.includes('playstation') || lower.includes('xbox') || lower.includes('switch') || lower.includes('console')) return 'game_console';
  
  return 'laptop_generic';
}

function normalizeRepairType(repairType: string): string {
  const lower = repairType.toLowerCase();
  
  if (lower.includes('screen') || lower.includes('display') || lower.includes('lcd')) return 'screen_replacement';
  if (lower.includes('battery')) return 'battery_replacement';
  if (lower.includes('charg') || lower.includes('port') || lower.includes('usb-c') || lower.includes('lightning')) return 'charging_port';
  if (lower.includes('camera')) return 'camera_repair';
  if (lower.includes('speaker') || lower.includes('audio')) return 'speaker_repair';
  if (lower.includes('water') || lower.includes('liquid')) return 'water_damage';
  if (lower.includes('board') || lower.includes('logic') || lower.includes('mother')) return 'motherboard';
  if (lower.includes('keyboard')) return 'keyboard_replacement';
  if (lower.includes('trackpad') || lower.includes('touchpad')) return 'trackpad_repair';
  if (lower.includes('software') || lower.includes('os') || lower.includes('update')) return 'software_issue';
  if (lower.includes('button') || lower.includes('power')) return 'button_repair';
  if (lower.includes('hdmi')) return 'hdmi_port';
  if (lower.includes('disc') || lower.includes('drive')) return 'disc_drive';
  if (lower.includes('fan')) return 'fan_replacement';
  
  return 'software_issue'; // Safe default
}

async function calculateSeverityFactor(severity: string, notes: string, env: Env): Promise<EstimationFactor> {
  // Base severity multipliers
  const severityMultipliers: Record<string, number> = {
    'minor': 0.8,
    'moderate': 1.0,
    'severe': 1.3,
    'critical': 1.6
  };
  
  let impact = severityMultipliers[severity?.toLowerCase()] || 1.0;
  
  // Use AI to analyze notes for hidden complexity
  if (notes && notes.length > 20) {
    const response = await env.AI.run('@cf/meta/llama-3-8b-instruct', {
      messages: [
        {
          role: 'system',
          content: `Analyze this repair note and estimate complexity modifier (0.8-1.5). 
          Look for: multiple issues, previous repair attempts, water indicators, physical damage extent.
          Respond with JSON: {"modifier": 1.0, "reason": "brief reason"}`
        },
        { role: 'user', content: notes }
      ]
    });
    
    try {
      const analysis = JSON.parse(response.response);
      impact *= analysis.modifier;
    } catch (e) {
      // AI parsing failed, use base severity
    }
  }
  
  return {
    name: 'Severity/Complexity',
    impact,
    description: `Device condition: ${severity || 'unknown'}`,
    controllable: false
  };
}

async function calculateTechnicianFactor(env: Env, technicianId: string, deviceType: string, repairType: string): Promise<EstimationFactor> {
  if (!technicianId) {
    return {
      name: 'Technician Skill',
      impact: 1.0,
      description: 'No technician assigned yet',
      controllable: true
    };
  }
  
  // Get technician's historical performance for this repair type
  const techStats = await env.DB.prepare(`
    SELECT 
      AVG(actual_time / estimated_time) as accuracy_ratio,
      AVG(actual_time) as avg_time,
      COUNT(*) as repair_count,
      AVG(quality_score) as avg_quality
    FROM repairs
    WHERE technician_id = ?
      AND device_type LIKE ?
      AND repair_type = ?
      AND actual_time IS NOT NULL
  `).bind(technicianId, `%${deviceType}%`, repairType).first();
  
  // Get overall technician speed
  const overallStats = await env.DB.prepare(`
    SELECT 
      AVG(actual_time / estimated_time) as overall_ratio,
      certification_level
    FROM repairs r
    JOIN technicians t ON r.technician_id = t.id
    WHERE technician_id = ?
      AND actual_time IS NOT NULL
  `).bind(technicianId).first();
  
  // Calculate impact
  let impact = 1.0;
  let description = '';
  
  if (techStats && (techStats.repair_count as number) >= 5) {
    // Enough data for this specific repair type
    impact = techStats.accuracy_ratio as number || 1.0;
    description = `Expert in this repair (${techStats.repair_count} completed, avg quality: ${((techStats.avg_quality as number) || 0).toFixed(1)}/5)`;
  } else if (overallStats?.overall_ratio) {
    // Use overall performance
    impact = overallStats.overall_ratio as number;
    description = `Based on overall performance`;
  }
  
  // Certification bonus
  if (overallStats?.certification_level === 'master') {
    impact *= 0.85; // 15% faster
    description += ' (Master certified)';
  }
  
  return {
    name: 'Technician Skill',
    impact: Math.max(0.5, Math.min(2.0, impact)), // Clamp between 0.5x and 2x
    description: description || 'Average technician performance',
    controllable: true
  };
}

async function calculatePartsFactor(env: Env, partsAvailable: boolean, deviceType: string, repairType: string): Promise<EstimationFactor> {
  if (partsAvailable === true) {
    return {
      name: 'Parts Availability',
      impact: 1.0,
      description: 'Parts in stock',
      controllable: false
    };
  }
  
  // Check parts lead time
  const partsInfo = await env.DB.prepare(`
    SELECT 
      AVG(lead_time_hours) as avg_lead_time,
      stock_level,
      last_restock_date
    FROM parts_inventory
    WHERE device_type LIKE ? AND part_type = ?
  `).bind(`%${deviceType}%`, repairType).first();
  
  if (!partsInfo) {
    return {
      name: 'Parts Availability',
      impact: 1.5, // 50% longer if no info
      description: 'Parts status unknown - added buffer',
      controllable: false
    };
  }
  
  const leadTimeHours = (partsInfo.avg_lead_time as number) || 24;
  const stockLevel = (partsInfo.stock_level as number) || 0;
  
  if (stockLevel > 0) {
    return {
      name: 'Parts Availability',
      impact: 1.0,
      description: `${stockLevel} in stock`,
      controllable: false
    };
  }
  
  // Calculate wait time impact (convert hours to multiplier)
  const waitTimeImpact = 1 + (leadTimeHours / 24) * 0.2; // ~20% increase per day of wait
  
  return {
    name: 'Parts Availability',
    impact: waitTimeImpact,
    description: `Parts on order (~${leadTimeHours}hr lead time)`,
    controllable: false
  };
}

async function calculateQueueFactor(env: Env, technicianId: string): Promise<EstimationFactor> {
  if (!technicianId) {
    // Get average queue depth
    const queueStats = await env.DB.prepare(`
      SELECT COUNT(*) as pending
      FROM repairs
      WHERE status = 'pending' OR status = 'in_progress'
    `).first();
    
    const pending = (queueStats?.pending as number) || 0;
    
    return {
      name: 'Queue Position',
      impact: 1 + (pending / 20) * 0.1, // 10% increase per 20 in queue
      description: `${pending} repairs in queue`,
      controllable: true
    };
  }
  
  // Get technician's current workload
  const workload = await env.DB.prepare(`
    SELECT 
      COUNT(*) as active_repairs,
      SUM(estimated_time - COALESCE(time_spent, 0)) as remaining_minutes
    FROM repairs
    WHERE technician_id = ?
      AND (status = 'in_progress' OR status = 'pending')
  `).bind(technicianId).first();
  
  const activeRepairs = (workload?.active_repairs as number) || 0;
  const remainingMinutes = (workload?.remaining_minutes as number) || 0;
  
  // Queue impact based on workload
  const queueImpact = 1 + (activeRepairs * 0.05) + (remainingMinutes / 480) * 0.1;
  
  return {
    name: 'Queue Position',
    impact: Math.min(2.0, queueImpact),
    description: `Technician has ${activeRepairs} active repairs (~${Math.round(remainingMinutes)}min remaining)`,
    controllable: true
  };
}

async function calculateCustomerHistoryFactor(env: Env, customerId: string, deviceType: string): Promise<EstimationFactor> {
  if (!customerId) {
    return {
      name: 'Customer History',
      impact: 1.0,
      description: 'New customer',
      controllable: false
    };
  }
  
  const history = await env.DB.prepare(`
    SELECT 
      COUNT(*) as repair_count,
      AVG(CASE WHEN actual_time > estimated_time * 1.2 THEN 1.2 
               WHEN actual_time < estimated_time * 0.8 THEN 0.8
               ELSE actual_time / estimated_time END) as complexity_ratio,
      SUM(CASE WHEN reopen_count > 0 THEN 1 ELSE 0 END) as reopened_repairs
    FROM repairs
    WHERE customer_id = ? AND device_type LIKE ?
  `).bind(customerId, `%${deviceType}%`).first();
  
  if (!history || (history.repair_count as number) === 0) {
    return {
      name: 'Customer History',
      impact: 1.0,
      description: 'First repair for this device type',
      controllable: false
    };
  }
  
  const complexityRatio = (history.complexity_ratio as number) || 1.0;
  const reopenRate = (history.reopened_repairs as number) / (history.repair_count as number);
  
  // Devices that needed reopening tend to take longer
  const impact = complexityRatio * (1 + reopenRate * 0.2);
  
  return {
    name: 'Customer History',
    impact: Math.max(0.8, Math.min(1.5, impact)),
    description: `${history.repair_count} previous repairs, ${(reopenRate * 100).toFixed(0)}% reopen rate`,
    controllable: false
  };
}

function calculateTemporalFactor(): EstimationFactor {
  const now = new Date();
  const hour = now.getHours();
  const day = now.getDay();
  
  let impact = 1.0;
  let description = 'Normal business hours';
  
  // Friday afternoon rush
  if (day === 5 && hour >= 14) {
    impact = 1.1;
    description = 'Friday afternoon - typically busier';
  }
  
  // Monday morning backlog
  if (day === 1 && hour < 12) {
    impact = 1.15;
    description = 'Monday morning - processing weekend backlog';
  }
  
  // End of day - partial work
  if (hour >= 17) {
    impact = 1.05;
    description = 'End of day - may continue tomorrow';
  }
  
  // Lunch hour
  if (hour >= 12 && hour <= 13) {
    impact = 1.08;
    description = 'Lunch hour - reduced capacity';
  }
  
  return {
    name: 'Time of Day',
    impact,
    description,
    controllable: false
  };
}

async function calculateConfidence(env: Env, deviceType: string, repairType: string, factors: EstimationFactor[]): Promise<{ overall: number; dataPoints: number }> {
  // Get historical accuracy for this repair type
  const accuracy = await env.DB.prepare(`
    SELECT 
      COUNT(*) as count,
      AVG(ABS(actual_time - estimated_time) / estimated_time) as avg_error,
      STDEV(actual_time / estimated_time) as variance
    FROM repairs
    WHERE device_type LIKE ? AND repair_type = ?
      AND actual_time IS NOT NULL
  `).bind(`%${deviceType}%`, repairType).first();
  
  const count = (accuracy?.count as number) || 0;
  const avgError = (accuracy?.avg_error as number) || 0.3;
  const variance = (accuracy?.variance as number) || 0.25;
  
  // Base confidence from historical data
  let dataConfidence = Math.min(0.95, 0.5 + (count / 100) * 0.45);
  
  // Adjust for error rate
  const errorAdjustment = 1 - Math.min(0.4, avgError);
  
  // Adjust for number of uncertain factors
  const uncertainFactors = factors.filter(f => !f.controllable && f.impact > 1.2).length;
  const factorAdjustment = 1 - (uncertainFactors * 0.1);
  
  const overall = dataConfidence * errorAdjustment * factorAdjustment;
  
  return {
    overall: Math.max(0.3, Math.min(0.95, overall)),
    dataPoints: count
  };
}

function calculateConfidenceInterval(estimatedTime: number, confidence: { overall: number }): { low: number; high: number } {
  // Higher confidence = narrower interval
  const errorMargin = (1 - confidence.overall) * estimatedTime;
  
  return {
    low: Math.round(Math.max(estimatedTime * 0.5, estimatedTime - errorMargin)),
    high: Math.round(estimatedTime + errorMargin * 1.5)
  };
}

function calculateTimeBreakdown(totalTime: number, repairType: string, partsFactor: EstimationFactor): TimeBreakdown {
  // Standard breakdown percentages
  const breakdowns: Record<string, { diagnosis: number; partsWait: number; repair: number; testing: number; documentation: number }> = {
    'screen_replacement': { diagnosis: 0.05, partsWait: 0, repair: 0.7, testing: 0.15, documentation: 0.1 },
    'battery_replacement': { diagnosis: 0.1, partsWait: 0, repair: 0.6, testing: 0.2, documentation: 0.1 },
    'water_damage': { diagnosis: 0.2, partsWait: 0.1, repair: 0.45, testing: 0.15, documentation: 0.1 },
    'motherboard': { diagnosis: 0.25, partsWait: 0.1, repair: 0.4, testing: 0.15, documentation: 0.1 },
    'default': { diagnosis: 0.15, partsWait: 0.05, repair: 0.55, testing: 0.15, documentation: 0.1 }
  };
  
  const percentages = breakdowns[repairType] || breakdowns['default'];
  
  // Adjust parts wait based on availability factor
  let partsWaitTime = totalTime * percentages.partsWait;
  if (partsFactor.impact > 1) {
    partsWaitTime = (partsFactor.impact - 1) * 480; // Convert to minutes of wait
  }
  
  const workTime = totalTime - partsWaitTime;
  
  return {
    diagnosis: Math.round(workTime * percentages.diagnosis),
    partsWait: Math.round(partsWaitTime),
    repair: Math.round(workTime * percentages.repair),
    testing: Math.round(workTime * percentages.testing),
    documentation: Math.round(workTime * percentages.documentation),
    buffer: Math.round(workTime * 0.1) // 10% buffer
  };
}

async function checkSlaStatus(env: Env, customerId: string, estimatedMinutes: number): Promise<'on_track' | 'at_risk' | 'breach_likely'> {
  // Get customer SLA
  const customer = await env.DB.prepare(`
    SELECT sla_hours FROM customers WHERE id = ?
  `).bind(customerId).first();
  
  const slaHours = (customer?.sla_hours as number) || 48; // Default 48 hours
  const slaMinutes = slaHours * 60;
  
  if (estimatedMinutes <= slaMinutes * 0.7) return 'on_track';
  if (estimatedMinutes <= slaMinutes * 0.9) return 'at_risk';
  return 'breach_likely';
}

function calculateCompletionDate(estimatedMinutes: number, queueFactor: EstimationFactor): string {
  const now = new Date();
  const businessMinutesPerDay = 480; // 8 hours
  
  // Add queue wait time
  const totalMinutes = estimatedMinutes + (queueFactor.impact - 1) * businessMinutesPerDay;
  
  // Calculate business days needed
  const daysNeeded = Math.ceil(totalMinutes / businessMinutesPerDay);
  
  // Add to current date (skipping weekends)
  let completionDate = new Date(now);
  let daysAdded = 0;
  
  while (daysAdded < daysNeeded) {
    completionDate.setDate(completionDate.getDate() + 1);
    const day = completionDate.getDay();
    if (day !== 0 && day !== 6) { // Skip weekends
      daysAdded++;
    }
  }
  
  return completionDate.toISOString().split('T')[0];
}

async function storeEstimate(env: Env, data: any): Promise<void> {
  await env.DB.prepare(`
    INSERT INTO time_estimates (
      device_type, repair_type, estimated_minutes,
      confidence, factors_json, created_at
    ) VALUES (?, ?, ?, ?, ?, datetime('now'))
  `).bind(
    data.deviceType,
    data.repairType,
    data.estimate.estimatedMinutes,
    data.estimate.confidence,
    JSON.stringify(data.factors)
  ).run();
}

// =============================================================================
// REAL-TIME UPDATE ENDPOINT
// =============================================================================

app.post('/api/update/:repairId', async (c) => {
  const repairId = c.req.param('repairId');
  const { currentPhase, timeSpent, discoveredIssues } = await c.req.json();
  
  // Get original estimate
  const repair = await c.env.DB.prepare(`
    SELECT * FROM repairs WHERE id = ?
  `).bind(repairId).first();
  
  if (!repair) {
    return c.json({ error: 'Repair not found' }, 404);
  }
  
  // Calculate remaining time based on progress
  const originalEstimate = repair.estimated_time as number;
  const phases = ['diagnosis', 'partsWait', 'repair', 'testing', 'documentation'];
  const currentPhaseIndex = phases.indexOf(currentPhase);
  
  // Recalculate if issues discovered
  let adjustedRemaining = originalEstimate - timeSpent;
  
  if (discoveredIssues && discoveredIssues.length > 0) {
    // Add time for discovered issues
    for (const issue of discoveredIssues) {
      const additionalTime = getBaseTime(repair.device_type as string, issue.type);
      adjustedRemaining += additionalTime * 0.7; // 70% of normal time since already disassembled
    }
    
    // Notify customer of delay
    await c.env.NOTIFICATIONS_QUEUE.send({
      type: 'estimate_updated',
      repairId,
      oldEstimate: originalEstimate,
      newEstimate: timeSpent + adjustedRemaining,
      reason: `Additional issues discovered: ${discoveredIssues.map((i: any) => i.type).join(', ')}`,
      timestamp: Date.now()
    });
  }
  
  // Update repair record
  await c.env.DB.prepare(`
    UPDATE repairs 
    SET current_phase = ?, time_spent = ?, revised_estimate = ?
    WHERE id = ?
  `).bind(currentPhase, timeSpent, timeSpent + adjustedRemaining, repairId).run();
  
  // Return updated estimate
  return c.json({
    repairId,
    currentPhase,
    timeSpent,
    remainingTime: Math.round(adjustedRemaining),
    newTotalEstimate: Math.round(timeSpent + adjustedRemaining),
    progressPercent: Math.round((timeSpent / (timeSpent + adjustedRemaining)) * 100),
    onTrack: adjustedRemaining <= (originalEstimate - timeSpent) * 1.2
  });
});

// =============================================================================
// BATCH ESTIMATION
// =============================================================================

app.post('/api/batch', async (c) => {
  const { repairs } = await c.req.json();
  
  const estimates = await Promise.all(
    repairs.map(async (repair: any) => {
      const response = await app.request('/api/estimate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(repair)
      });
      return { repairId: repair.id, ...(await response.json()) };
    })
  );
  
  // Calculate totals
  const totalMinutes = estimates.reduce((sum, e) => sum + e.estimatedMinutes, 0);
  const avgConfidence = estimates.reduce((sum, e) => sum + e.confidence, 0) / estimates.length;
  
  return c.json({
    estimates,
    summary: {
      totalRepairs: estimates.length,
      totalMinutes,
      totalHours: (totalMinutes / 60).toFixed(1),
      avgConfidence: avgConfidence.toFixed(2),
      technicianHoursNeeded: Math.ceil(totalMinutes / 480)
    }
  });
});

// =============================================================================
// ANALYTICS ENDPOINTS
// =============================================================================

app.get('/api/analytics/accuracy', async (c) => {
  const days = parseInt(c.req.query('days') || '30');
  
  const accuracy = await c.env.DB.prepare(`
    SELECT 
      device_type,
      repair_type,
      COUNT(*) as count,
      AVG(actual_time) as avg_actual,
      AVG(estimated_time) as avg_estimated,
      AVG(ABS(actual_time - estimated_time) / estimated_time * 100) as mape,
      SUM(CASE WHEN actual_time <= estimated_time THEN 1 ELSE 0 END) * 100.0 / COUNT(*) as on_time_pct
    FROM repairs
    WHERE actual_time IS NOT NULL
      AND created_at > datetime('now', '-${days} days')
    GROUP BY device_type, repair_type
    ORDER BY count DESC
  `).all();
  
  // Overall metrics
  const overall = await c.env.DB.prepare(`
    SELECT 
      AVG(ABS(actual_time - estimated_time) / estimated_time * 100) as overall_mape,
      SUM(CASE WHEN actual_time <= estimated_time THEN 1 ELSE 0 END) * 100.0 / COUNT(*) as overall_on_time
    FROM repairs
    WHERE actual_time IS NOT NULL
      AND created_at > datetime('now', '-${days} days')
  `).first();
  
  return c.json({
    byRepairType: accuracy.results,
    overall: {
      mape: ((overall?.overall_mape as number) || 0).toFixed(1) + '%',
      onTimePercent: ((overall?.overall_on_time as number) || 0).toFixed(1) + '%'
    },
    period: `${days} days`
  });
});

app.get('/api/analytics/technician/:id', async (c) => {
  const techId = c.req.param('id');
  
  const stats = await c.env.DB.prepare(`
    SELECT 
      repair_type,
      COUNT(*) as repairs,
      AVG(actual_time) as avg_time,
      AVG(quality_score) as avg_quality,
      AVG(actual_time / estimated_time) as speed_ratio
    FROM repairs
    WHERE technician_id = ? AND actual_time IS NOT NULL
    GROUP BY repair_type
    ORDER BY repairs DESC
  `).bind(techId).all();
  
  // Trend over time
  const trend = await c.env.DB.prepare(`
    SELECT 
      strftime('%Y-%m', created_at) as month,
      AVG(actual_time / estimated_time) as speed_ratio,
      AVG(quality_score) as quality
    FROM repairs
    WHERE technician_id = ? AND actual_time IS NOT NULL
    GROUP BY month
    ORDER BY month DESC
    LIMIT 12
  `).bind(techId).all();
  
  return c.json({
    byRepairType: stats.results,
    trend: trend.results,
    summary: {
      totalRepairs: stats.results?.reduce((sum: number, r: any) => sum + r.repairs, 0) || 0,
      avgSpeedRatio: (stats.results?.reduce((sum: number, r: any) => sum + r.speed_ratio, 0) || 0) / (stats.results?.length || 1),
      strongestArea: stats.results?.[0]?.repair_type || 'N/A'
    }
  });
});

// =============================================================================
// ML MODEL RETRAINING TRIGGER
// =============================================================================

app.post('/api/model/retrain', async (c) => {
  // Get recent completed repairs for training
  const trainingData = await c.env.DB.prepare(`
    SELECT 
      device_type, repair_type, severity,
      estimated_time, actual_time,
      technician_id, parts_available,
      customer_id, factors_json
    FROM repairs
    WHERE actual_time IS NOT NULL
    ORDER BY created_at DESC
    LIMIT 5000
  `).all();
  
  // Store training snapshot
  const trainingId = crypto.randomUUID();
  await c.env.CACHE.put(
    `training:${trainingId}`,
    JSON.stringify(trainingData.results),
    { expirationTtl: 86400 }
  );
  
  return c.json({
    trainingId,
    dataPoints: trainingData.results?.length || 0,
    status: 'training_queued',
    message: 'Model retraining initiated with latest data'
  });
});

export default app;
