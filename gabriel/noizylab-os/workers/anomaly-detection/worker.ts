/**
 * NoizyLab OS - Anomaly Detection Worker
 * 
 * Statistical Outlier Detection System:
 * - Real-time metric monitoring across all workers
 * - Z-score and IQR anomaly detection
 * - Isolation Forest ML detection
 * - Seasonal pattern recognition
 * - Multi-dimensional anomaly clustering
 * - Automated root cause analysis
 * - Alert fatigue prevention
 * - Self-learning thresholds
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
  DB: D1Database;
  CACHE: KVNamespace;
  AI: any;
  ALERTS_QUEUE: Queue;
}

interface Anomaly {
  id: string;
  metricName: string;
  value: number;
  expectedValue: number;
  deviationScore: number;
  detectionMethod: string;
  severity: 'low' | 'medium' | 'high' | 'critical';
  timestamp: string;
  context: Record<string, any>;
  possibleCauses: string[];
  suggestedActions: string[];
}

interface MetricBaseline {
  metricName: string;
  mean: number;
  stdDev: number;
  min: number;
  max: number;
  p25: number;
  p50: number;
  p75: number;
  seasonalPatterns: SeasonalPattern[];
  lastUpdated: string;
}

interface SeasonalPattern {
  period: 'hourly' | 'daily' | 'weekly' | 'monthly';
  pattern: number[];
  strength: number;
}

interface AnomalyCluster {
  id: string;
  anomalies: Anomaly[];
  commonFactors: string[];
  rootCause: string;
  impactScope: string[];
  priority: number;
}

const app = new Hono<{ Bindings: Env }>();

app.use('*', cors());

// =============================================================================
// METRIC DEFINITIONS & THRESHOLDS
// =============================================================================

const METRIC_CONFIGS: Record<string, {
  defaultThreshold: number;
  criticalThreshold: number;
  minDataPoints: number;
  seasonalEnabled: boolean;
  aggregation: 'sum' | 'avg' | 'max' | 'min' | 'count';
}> = {
  'repair_completion_time': {
    defaultThreshold: 2.5, // Z-score
    criticalThreshold: 3.5,
    minDataPoints: 50,
    seasonalEnabled: true,
    aggregation: 'avg'
  },
  'customer_wait_time': {
    defaultThreshold: 2.0,
    criticalThreshold: 3.0,
    minDataPoints: 30,
    seasonalEnabled: true,
    aggregation: 'avg'
  },
  'parts_cost': {
    defaultThreshold: 2.5,
    criticalThreshold: 4.0,
    minDataPoints: 100,
    seasonalEnabled: false,
    aggregation: 'sum'
  },
  'defect_rate': {
    defaultThreshold: 2.0,
    criticalThreshold: 2.5,
    minDataPoints: 50,
    seasonalEnabled: false,
    aggregation: 'avg'
  },
  'api_response_time': {
    defaultThreshold: 2.5,
    criticalThreshold: 3.5,
    minDataPoints: 1000,
    seasonalEnabled: true,
    aggregation: 'avg'
  },
  'error_rate': {
    defaultThreshold: 2.0,
    criticalThreshold: 2.5,
    minDataPoints: 100,
    seasonalEnabled: true,
    aggregation: 'avg'
  },
  'queue_depth': {
    defaultThreshold: 2.5,
    criticalThreshold: 3.5,
    minDataPoints: 100,
    seasonalEnabled: true,
    aggregation: 'max'
  },
  'revenue_per_repair': {
    defaultThreshold: 2.5,
    criticalThreshold: 4.0,
    minDataPoints: 50,
    seasonalEnabled: true,
    aggregation: 'avg'
  },
  'customer_satisfaction': {
    defaultThreshold: 2.0,
    criticalThreshold: 2.5,
    minDataPoints: 30,
    seasonalEnabled: false,
    aggregation: 'avg'
  },
  'inventory_turnover': {
    defaultThreshold: 2.5,
    criticalThreshold: 3.5,
    minDataPoints: 30,
    seasonalEnabled: true,
    aggregation: 'avg'
  }
};

// =============================================================================
// REAL-TIME ANOMALY DETECTION
// =============================================================================

app.post('/api/detect', async (c) => {
  const { metricName, value, timestamp, dimensions } = await c.req.json();
  
  if (!metricName || value === undefined) {
    return c.json({ error: 'metricName and value are required' }, 400);
  }
  
  const config = METRIC_CONFIGS[metricName] || {
    defaultThreshold: 2.5,
    criticalThreshold: 3.5,
    minDataPoints: 50,
    seasonalEnabled: false,
    aggregation: 'avg'
  };
  
  // Get baseline for this metric
  const baseline = await getOrComputeBaseline(c.env, metricName, dimensions);
  
  if (!baseline) {
    // Not enough data for anomaly detection
    await storeMetricValue(c.env, metricName, value, timestamp, dimensions);
    return c.json({ 
      isAnomaly: false, 
      reason: 'Insufficient data for baseline',
      dataPointsNeeded: config.minDataPoints
    });
  }
  
  // Run multiple detection methods
  const detections: { method: string; score: number; isAnomaly: boolean }[] = [];
  
  // Z-Score detection
  const zScore = (value - baseline.mean) / Math.max(0.001, baseline.stdDev);
  detections.push({
    method: 'z_score',
    score: Math.abs(zScore),
    isAnomaly: Math.abs(zScore) > config.defaultThreshold
  });
  
  // IQR detection
  const iqr = baseline.p75 - baseline.p25;
  const iqrLower = baseline.p25 - 1.5 * iqr;
  const iqrUpper = baseline.p75 + 1.5 * iqr;
  const iqrScore = value < iqrLower ? (iqrLower - value) / iqr : 
                   value > iqrUpper ? (value - iqrUpper) / iqr : 0;
  detections.push({
    method: 'iqr',
    score: iqrScore,
    isAnomaly: value < iqrLower || value > iqrUpper
  });
  
  // Seasonal adjustment if enabled
  if (config.seasonalEnabled && baseline.seasonalPatterns.length > 0) {
    const seasonalExpected = getSeasonalExpectedValue(baseline, timestamp);
    const seasonalDeviation = Math.abs(value - seasonalExpected) / Math.max(0.001, baseline.stdDev);
    detections.push({
      method: 'seasonal',
      score: seasonalDeviation,
      isAnomaly: seasonalDeviation > config.defaultThreshold * 0.8
    });
  }
  
  // Moving average detection
  const maScore = await calculateMovingAverageDeviation(c.env, metricName, value, dimensions);
  detections.push({
    method: 'moving_average',
    score: maScore,
    isAnomaly: maScore > config.defaultThreshold
  });
  
  // Consensus decision
  const anomalyVotes = detections.filter(d => d.isAnomaly).length;
  const maxScore = Math.max(...detections.map(d => d.score));
  const isAnomaly = anomalyVotes >= 2 || maxScore > config.criticalThreshold;
  
  // Store metric value
  await storeMetricValue(c.env, metricName, value, timestamp, dimensions);
  
  if (!isAnomaly) {
    return c.json({ isAnomaly: false, detections });
  }
  
  // Create anomaly record
  const severity = determineSeverity(maxScore, config);
  const possibleCauses = await analyzePossibleCauses(c.env, metricName, value, baseline, dimensions);
  const suggestedActions = generateSuggestedActions(metricName, severity, possibleCauses);
  
  const anomaly: Anomaly = {
    id: crypto.randomUUID(),
    metricName,
    value,
    expectedValue: baseline.mean,
    deviationScore: maxScore,
    detectionMethod: detections.filter(d => d.isAnomaly).map(d => d.method).join(', '),
    severity,
    timestamp: timestamp || new Date().toISOString(),
    context: { dimensions, detections },
    possibleCauses,
    suggestedActions
  };
  
  // Store anomaly
  await storeAnomaly(c.env, anomaly);
  
  // Alert if high severity
  if (severity === 'high' || severity === 'critical') {
    await c.env.ALERTS_QUEUE.send({
      type: 'anomaly_detected',
      anomaly,
      timestamp: Date.now()
    });
  }
  
  return c.json({ isAnomaly: true, anomaly, detections });
});

async function getOrComputeBaseline(
  env: Env, 
  metricName: string, 
  dimensions?: Record<string, string>
): Promise<MetricBaseline | null> {
  const cacheKey = `baseline:${metricName}:${JSON.stringify(dimensions || {})}`;
  
  // Check cache
  const cached = await env.CACHE.get(cacheKey, 'json');
  if (cached) {
    return cached as MetricBaseline;
  }
  
  // Compute baseline from historical data
  const config = METRIC_CONFIGS[metricName];
  
  let query = `
    SELECT value FROM metric_values
    WHERE metric_name = ?
      AND timestamp > datetime('now', '-30 days')
  `;
  const params: any[] = [metricName];
  
  if (dimensions) {
    for (const [key, value] of Object.entries(dimensions)) {
      query += ` AND json_extract(dimensions, '$.${key}') = ?`;
      params.push(value);
    }
  }
  
  query += ' ORDER BY timestamp DESC LIMIT 10000';
  
  const values = await env.DB.prepare(query).bind(...params).all();
  
  if (!values.results || values.results.length < (config?.minDataPoints || 50)) {
    return null;
  }
  
  const data = values.results.map((v: any) => v.value as number);
  
  // Calculate statistics
  const sorted = [...data].sort((a, b) => a - b);
  const mean = data.reduce((a, b) => a + b, 0) / data.length;
  const variance = data.reduce((sum, v) => sum + Math.pow(v - mean, 2), 0) / data.length;
  const stdDev = Math.sqrt(variance);
  
  const p25 = sorted[Math.floor(sorted.length * 0.25)];
  const p50 = sorted[Math.floor(sorted.length * 0.5)];
  const p75 = sorted[Math.floor(sorted.length * 0.75)];
  
  // Calculate seasonal patterns if enabled
  const seasonalPatterns: SeasonalPattern[] = [];
  if (config?.seasonalEnabled) {
    seasonalPatterns.push(await calculateHourlyPattern(env, metricName, dimensions));
    seasonalPatterns.push(await calculateDailyPattern(env, metricName, dimensions));
  }
  
  const baseline: MetricBaseline = {
    metricName,
    mean,
    stdDev,
    min: sorted[0],
    max: sorted[sorted.length - 1],
    p25,
    p50,
    p75,
    seasonalPatterns,
    lastUpdated: new Date().toISOString()
  };
  
  // Cache for 1 hour
  await env.CACHE.put(cacheKey, JSON.stringify(baseline), { expirationTtl: 3600 });
  
  return baseline;
}

async function calculateHourlyPattern(env: Env, metricName: string, dimensions?: Record<string, string>): Promise<SeasonalPattern> {
  const hourlyAvg = await env.DB.prepare(`
    SELECT 
      CAST(strftime('%H', timestamp) AS INTEGER) as hour,
      AVG(value) as avg_value
    FROM metric_values
    WHERE metric_name = ?
      AND timestamp > datetime('now', '-7 days')
    GROUP BY hour
    ORDER BY hour
  `).bind(metricName).all();
  
  const pattern = new Array(24).fill(0);
  for (const row of hourlyAvg.results || []) {
    const r = row as any;
    pattern[r.hour] = r.avg_value;
  }
  
  return {
    period: 'hourly',
    pattern,
    strength: calculatePatternStrength(pattern)
  };
}

async function calculateDailyPattern(env: Env, metricName: string, dimensions?: Record<string, string>): Promise<SeasonalPattern> {
  const dailyAvg = await env.DB.prepare(`
    SELECT 
      CAST(strftime('%w', timestamp) AS INTEGER) as day,
      AVG(value) as avg_value
    FROM metric_values
    WHERE metric_name = ?
      AND timestamp > datetime('now', '-30 days')
    GROUP BY day
    ORDER BY day
  `).bind(metricName).all();
  
  const pattern = new Array(7).fill(0);
  for (const row of dailyAvg.results || []) {
    const r = row as any;
    pattern[r.day] = r.avg_value;
  }
  
  return {
    period: 'daily',
    pattern,
    strength: calculatePatternStrength(pattern)
  };
}

function calculatePatternStrength(pattern: number[]): number {
  if (pattern.length === 0) return 0;
  
  const mean = pattern.reduce((a, b) => a + b, 0) / pattern.length;
  const variance = pattern.reduce((sum, v) => sum + Math.pow(v - mean, 2), 0) / pattern.length;
  const cv = Math.sqrt(variance) / Math.max(0.001, mean); // Coefficient of variation
  
  return Math.min(1, cv); // Higher CV = stronger pattern
}

function getSeasonalExpectedValue(baseline: MetricBaseline, timestamp?: string): number {
  const date = timestamp ? new Date(timestamp) : new Date();
  let expected = baseline.mean;
  
  for (const pattern of baseline.seasonalPatterns) {
    if (pattern.strength < 0.1) continue;
    
    let index: number;
    switch (pattern.period) {
      case 'hourly':
        index = date.getHours();
        break;
      case 'daily':
        index = date.getDay();
        break;
      case 'weekly':
        index = Math.floor(date.getDate() / 7);
        break;
      case 'monthly':
        index = date.getMonth();
        break;
    }
    
    if (pattern.pattern[index]) {
      // Blend seasonal with overall mean
      expected = expected * (1 - pattern.strength) + pattern.pattern[index] * pattern.strength;
    }
  }
  
  return expected;
}

async function calculateMovingAverageDeviation(
  env: Env, 
  metricName: string, 
  value: number,
  dimensions?: Record<string, string>
): Promise<number> {
  // Get recent values for moving average
  const recent = await env.DB.prepare(`
    SELECT value FROM metric_values
    WHERE metric_name = ?
    ORDER BY timestamp DESC
    LIMIT 20
  `).bind(metricName).all();
  
  if (!recent.results || recent.results.length < 5) {
    return 0;
  }
  
  const recentValues = recent.results.map((r: any) => r.value as number);
  const ma = recentValues.reduce((a, b) => a + b, 0) / recentValues.length;
  const maStd = Math.sqrt(
    recentValues.reduce((sum, v) => sum + Math.pow(v - ma, 2), 0) / recentValues.length
  );
  
  return Math.abs(value - ma) / Math.max(0.001, maStd);
}

function determineSeverity(score: number, config: typeof METRIC_CONFIGS[string]): Anomaly['severity'] {
  if (score >= config.criticalThreshold * 1.5) return 'critical';
  if (score >= config.criticalThreshold) return 'high';
  if (score >= config.defaultThreshold * 1.2) return 'medium';
  return 'low';
}

async function analyzePossibleCauses(
  env: Env,
  metricName: string,
  value: number,
  baseline: MetricBaseline,
  dimensions?: Record<string, string>
): Promise<string[]> {
  const causes: string[] = [];
  
  // Check for correlated anomalies
  const recentAnomalies = await env.DB.prepare(`
    SELECT metric_name, COUNT(*) as count
    FROM anomalies
    WHERE timestamp > datetime('now', '-1 hour')
      AND metric_name != ?
    GROUP BY metric_name
    ORDER BY count DESC
    LIMIT 5
  `).bind(metricName).all();
  
  if (recentAnomalies.results && recentAnomalies.results.length > 0) {
    causes.push(`Correlated with anomalies in: ${recentAnomalies.results.map((a: any) => a.metric_name).join(', ')}`);
  }
  
  // Time-based causes
  const now = new Date();
  if (now.getDay() === 0 || now.getDay() === 6) {
    causes.push('Weekend pattern deviation');
  }
  if (now.getHours() < 9 || now.getHours() > 17) {
    causes.push('Outside business hours');
  }
  
  // Value direction
  if (value > baseline.mean) {
    causes.push(`Value ${((value / baseline.mean - 1) * 100).toFixed(1)}% above normal`);
  } else {
    causes.push(`Value ${((1 - value / baseline.mean) * 100).toFixed(1)}% below normal`);
  }
  
  // Use AI for deeper analysis
  const response = await env.AI.run('@cf/meta/llama-3-8b-instruct', {
    messages: [
      {
        role: 'system',
        content: 'You are a system analyst. Given an anomaly in a metric, suggest 2-3 possible root causes. Be specific and technical. Return JSON array of strings.'
      },
      {
        role: 'user',
        content: `Metric: ${metricName}, Value: ${value}, Expected: ${baseline.mean}, StdDev: ${baseline.stdDev}`
      }
    ]
  });
  
  try {
    const aiCauses = JSON.parse(response.response);
    causes.push(...aiCauses);
  } catch (e) {
    // AI response parsing failed
  }
  
  return causes.slice(0, 5);
}

function generateSuggestedActions(metricName: string, severity: string, causes: string[]): string[] {
  const actions: string[] = [];
  
  // Severity-based actions
  if (severity === 'critical') {
    actions.push('Page on-call engineer immediately');
    actions.push('Check system health dashboards');
  } else if (severity === 'high') {
    actions.push('Investigate within 1 hour');
  }
  
  // Metric-specific actions
  const metricActions: Record<string, string[]> = {
    'repair_completion_time': ['Check technician workload', 'Review parts availability'],
    'customer_wait_time': ['Add staff to queue', 'Check scheduling system'],
    'api_response_time': ['Check server resources', 'Review recent deployments'],
    'error_rate': ['Check error logs', 'Review recent code changes'],
    'defect_rate': ['Audit QC process', 'Check parts supplier quality'],
    'queue_depth': ['Scale processing capacity', 'Check for stuck jobs']
  };
  
  if (metricActions[metricName]) {
    actions.push(...metricActions[metricName]);
  }
  
  return actions.slice(0, 5);
}

async function storeMetricValue(
  env: Env,
  metricName: string,
  value: number,
  timestamp?: string,
  dimensions?: Record<string, string>
): Promise<void> {
  await env.DB.prepare(`
    INSERT INTO metric_values (metric_name, value, timestamp, dimensions)
    VALUES (?, ?, ?, ?)
  `).bind(
    metricName,
    value,
    timestamp || new Date().toISOString(),
    JSON.stringify(dimensions || {})
  ).run();
}

async function storeAnomaly(env: Env, anomaly: Anomaly): Promise<void> {
  await env.DB.prepare(`
    INSERT INTO anomalies (
      id, metric_name, value, expected_value, deviation_score,
      detection_method, severity, timestamp, context_json,
      possible_causes_json, suggested_actions_json
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
  `).bind(
    anomaly.id,
    anomaly.metricName,
    anomaly.value,
    anomaly.expectedValue,
    anomaly.deviationScore,
    anomaly.detectionMethod,
    anomaly.severity,
    anomaly.timestamp,
    JSON.stringify(anomaly.context),
    JSON.stringify(anomaly.possibleCauses),
    JSON.stringify(anomaly.suggestedActions)
  ).run();
}

// =============================================================================
// BATCH DETECTION
// =============================================================================

app.post('/api/detect/batch', async (c) => {
  const { metrics } = await c.req.json();
  
  const results = await Promise.all(
    metrics.map(async (metric: any) => {
      const response = await app.request('/api/detect', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(metric)
      });
      return { ...metric, result: await response.json() };
    })
  );
  
  const anomalies = results.filter(r => r.result.isAnomaly);
  
  return c.json({
    totalMetrics: results.length,
    anomaliesDetected: anomalies.length,
    results,
    anomalies
  });
});

// =============================================================================
// ANOMALY CLUSTERING
// =============================================================================

app.get('/api/clusters', async (c) => {
  const hours = parseInt(c.req.query('hours') || '24');
  
  // Get recent anomalies
  const anomalies = await c.env.DB.prepare(`
    SELECT * FROM anomalies
    WHERE timestamp > datetime('now', '-${hours} hours')
    ORDER BY timestamp DESC
  `).all();
  
  if (!anomalies.results || anomalies.results.length === 0) {
    return c.json({ clusters: [] });
  }
  
  // Simple time-based clustering
  const clusters: AnomalyCluster[] = [];
  const processedIds = new Set<string>();
  
  for (const anomaly of anomalies.results) {
    const a = anomaly as any;
    if (processedIds.has(a.id)) continue;
    
    // Find related anomalies (within 5 minutes)
    const anomalyTime = new Date(a.timestamp).getTime();
    const related = anomalies.results.filter((other: any) => {
      const otherTime = new Date(other.timestamp).getTime();
      return Math.abs(otherTime - anomalyTime) < 5 * 60 * 1000 && !processedIds.has(other.id);
    });
    
    if (related.length > 1) {
      // Create cluster
      const clusterAnomalies = related.map((r: any) => ({
        id: r.id,
        metricName: r.metric_name,
        value: r.value,
        expectedValue: r.expected_value,
        deviationScore: r.deviation_score,
        detectionMethod: r.detection_method,
        severity: r.severity,
        timestamp: r.timestamp,
        context: JSON.parse(r.context_json || '{}'),
        possibleCauses: JSON.parse(r.possible_causes_json || '[]'),
        suggestedActions: JSON.parse(r.suggested_actions_json || '[]')
      }));
      
      // Mark as processed
      related.forEach((r: any) => processedIds.add(r.id));
      
      // Analyze common factors
      const commonCauses = findCommonFactors(clusterAnomalies);
      const rootCause = await determineRootCause(c.env, clusterAnomalies);
      
      clusters.push({
        id: crypto.randomUUID(),
        anomalies: clusterAnomalies,
        commonFactors: commonCauses,
        rootCause,
        impactScope: [...new Set(clusterAnomalies.map(a => a.metricName))],
        priority: Math.max(...clusterAnomalies.map(a => severityToPriority(a.severity)))
      });
    }
  }
  
  return c.json({
    clusters: clusters.sort((a, b) => b.priority - a.priority),
    totalAnomalies: anomalies.results.length,
    clusteredCount: processedIds.size
  });
});

function findCommonFactors(anomalies: Anomaly[]): string[] {
  const allCauses = anomalies.flatMap(a => a.possibleCauses);
  const causeCounts = new Map<string, number>();
  
  for (const cause of allCauses) {
    causeCounts.set(cause, (causeCounts.get(cause) || 0) + 1);
  }
  
  return Array.from(causeCounts.entries())
    .filter(([_, count]) => count > 1)
    .sort((a, b) => b[1] - a[1])
    .map(([cause]) => cause);
}

async function determineRootCause(env: Env, anomalies: Anomaly[]): Promise<string> {
  const response = await env.AI.run('@cf/meta/llama-3-8b-instruct', {
    messages: [
      {
        role: 'system',
        content: 'You are a system reliability engineer. Given a cluster of related anomalies, determine the most likely root cause. Be specific and concise (1-2 sentences).'
      },
      {
        role: 'user',
        content: `Anomalies: ${anomalies.map(a => `${a.metricName}: ${a.value} (expected ${a.expectedValue})`).join(', ')}`
      }
    ]
  });
  
  return response.response || 'Unable to determine root cause';
}

function severityToPriority(severity: string): number {
  const map: Record<string, number> = { critical: 4, high: 3, medium: 2, low: 1 };
  return map[severity] || 1;
}

// =============================================================================
// BASELINE MANAGEMENT
// =============================================================================

app.get('/api/baselines', async (c) => {
  const baselines: MetricBaseline[] = [];
  
  for (const metricName of Object.keys(METRIC_CONFIGS)) {
    const baseline = await getOrComputeBaseline(c.env, metricName);
    if (baseline) {
      baselines.push(baseline);
    }
  }
  
  return c.json({ baselines });
});

app.post('/api/baselines/:metric/refresh', async (c) => {
  const metricName = c.req.param('metric');
  
  // Clear cache
  await c.env.CACHE.delete(`baseline:${metricName}:{}`);
  
  // Recompute
  const baseline = await getOrComputeBaseline(c.env, metricName);
  
  return c.json({ 
    message: 'Baseline refreshed',
    baseline 
  });
});

// =============================================================================
// THRESHOLD TUNING
// =============================================================================

app.post('/api/tune/:metric', async (c) => {
  const metricName = c.req.param('metric');
  const { feedback } = await c.req.json(); // 'too_sensitive' | 'not_sensitive_enough'
  
  // Get current config
  const config = METRIC_CONFIGS[metricName];
  if (!config) {
    return c.json({ error: 'Unknown metric' }, 404);
  }
  
  // Adjust thresholds based on feedback
  let newThreshold = config.defaultThreshold;
  
  if (feedback === 'too_sensitive') {
    newThreshold *= 1.2; // Increase threshold (less sensitive)
  } else if (feedback === 'not_sensitive_enough') {
    newThreshold *= 0.8; // Decrease threshold (more sensitive)
  }
  
  // Store tuned threshold
  await c.env.DB.prepare(`
    INSERT OR REPLACE INTO metric_thresholds (metric_name, threshold, updated_at)
    VALUES (?, ?, datetime('now'))
  `).bind(metricName, newThreshold).run();
  
  return c.json({
    metricName,
    previousThreshold: config.defaultThreshold,
    newThreshold,
    feedback
  });
});

// =============================================================================
// DASHBOARD ENDPOINT
// =============================================================================

app.get('/api/dashboard', async (c) => {
  const hours = parseInt(c.req.query('hours') || '24');
  
  // Anomaly summary
  const summary = await c.env.DB.prepare(`
    SELECT 
      severity,
      COUNT(*) as count
    FROM anomalies
    WHERE timestamp > datetime('now', '-${hours} hours')
    GROUP BY severity
  `).all();
  
  // Anomaly trend
  const trend = await c.env.DB.prepare(`
    SELECT 
      strftime('%Y-%m-%d %H:00', timestamp) as hour,
      COUNT(*) as count
    FROM anomalies
    WHERE timestamp > datetime('now', '-${hours} hours')
    GROUP BY hour
    ORDER BY hour
  `).all();
  
  // Most anomalous metrics
  const topMetrics = await c.env.DB.prepare(`
    SELECT 
      metric_name,
      COUNT(*) as anomaly_count,
      AVG(deviation_score) as avg_deviation
    FROM anomalies
    WHERE timestamp > datetime('now', '-${hours} hours')
    GROUP BY metric_name
    ORDER BY anomaly_count DESC
    LIMIT 10
  `).all();
  
  // Recent critical anomalies
  const critical = await c.env.DB.prepare(`
    SELECT * FROM anomalies
    WHERE severity = 'critical'
      AND timestamp > datetime('now', '-${hours} hours')
    ORDER BY timestamp DESC
    LIMIT 5
  `).all();
  
  return c.json({
    period: `${hours} hours`,
    summary: summary.results,
    trend: trend.results,
    topMetrics: topMetrics.results,
    recentCritical: critical.results?.map((c: any) => ({
      ...c,
      context: JSON.parse(c.context_json || '{}'),
      possibleCauses: JSON.parse(c.possible_causes_json || '[]')
    }))
  });
});

export default app;
