/**
 * NoizyLab OS - AI Supervisor Worker
 * 🤖 Meta-AI System Orchestrator & Health Monitor
 * 
 * The "brain of brains" - monitors all other workers,
 * optimizes performance, handles failures, and makes
 * system-wide intelligent decisions.
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
  AI_SUPERVISOR_KV: KVNamespace;
  D1_DATABASE: D1Database;
  R2_BUCKET: R2Bucket;
  AI: Ai;
  ANALYTICS_QUEUE: Queue;
  
  // All worker services to supervise
  BRAIN_SERVICE: Fetcher;
  VOICE_SERVICE: Fetcher;
  VISION_SERVICE: Fetcher;
  PRICING_SERVICE: Fetcher;
  EBAY_SERVICE: Fetcher;
  INVENTORY_SERVICE: Fetcher;
  ANALYTICS_SERVICE: Fetcher;
  AR_GUIDE_SERVICE: Fetcher;
  TRAINING_SERVICE: Fetcher;
  CHAT_AGENT_SERVICE: Fetcher;
  NOTIFICATIONS_SERVICE: Fetcher;
  QC_INSPECTOR_SERVICE: Fetcher;
  CUSTOMER_PORTAL_SERVICE: Fetcher;
  SCHEMATIC_SERVICE: Fetcher;
  WORKFLOW_SERVICE: Fetcher;
  PREDICTIVE_SERVICE: Fetcher;
  PARTS_MATCHING_SERVICE: Fetcher;
  REPAIR_DNA_SERVICE: Fetcher;
  KNOWLEDGE_GRAPH_SERVICE: Fetcher;
  COLLABORATION_SERVICE: Fetcher;
}

interface WorkerHealth {
  worker_name: string;
  status: 'healthy' | 'degraded' | 'unhealthy' | 'unknown';
  response_time_ms: number;
  last_check: string;
  error_rate_1h: number;
  requests_1h: number;
  avg_response_time_1h: number;
  memory_usage?: number;
  cpu_usage?: number;
  last_error?: string;
}

interface SystemHealth {
  overall_status: 'healthy' | 'degraded' | 'critical';
  workers: WorkerHealth[];
  total_workers: number;
  healthy_count: number;
  degraded_count: number;
  unhealthy_count: number;
  system_load: number;
  recommendations: SystemRecommendation[];
  last_updated: string;
}

interface SystemRecommendation {
  priority: 'low' | 'medium' | 'high' | 'critical';
  category: string;
  recommendation: string;
  affected_workers: string[];
  action_type: 'manual' | 'automatic' | 'scheduled';
  estimated_impact: string;
}

interface WorkerMetrics {
  worker_name: string;
  timestamp: string;
  metrics: {
    requests: number;
    errors: number;
    avg_latency: number;
    p95_latency: number;
    p99_latency: number;
    success_rate: number;
  };
}

interface IncidentReport {
  id: string;
  severity: 'low' | 'medium' | 'high' | 'critical';
  affected_workers: string[];
  description: string;
  root_cause?: string;
  resolution?: string;
  started_at: string;
  resolved_at?: string;
  status: 'active' | 'investigating' | 'mitigated' | 'resolved';
  ai_analysis?: string;
  actions_taken: string[];
}

interface AutoHealingAction {
  action_id: string;
  worker_name: string;
  action_type: 'restart' | 'scale' | 'failover' | 'circuit_break' | 'rate_limit' | 'cache_clear';
  trigger: string;
  timestamp: string;
  result: 'success' | 'failed' | 'pending';
  details: string;
}

interface LoadBalancingDecision {
  decision_id: string;
  timestamp: string;
  current_load: Record<string, number>;
  rebalance_actions: {
    from_worker: string;
    to_worker: string;
    traffic_percentage: number;
  }[];
  reason: string;
}

interface PerformanceInsight {
  insight_type: string;
  worker_name: string;
  description: string;
  data: any;
  recommendation: string;
  potential_improvement: string;
}

const app = new Hono<{ Bindings: Env }>();

app.use('/*', cors());

// Worker registry with health endpoints
const WORKERS: Record<string, { service: keyof Env; healthEndpoint: string }> = {
  'brain': { service: 'BRAIN_SERVICE', healthEndpoint: '/health' },
  'voice': { service: 'VOICE_SERVICE', healthEndpoint: '/health' },
  'vision': { service: 'VISION_SERVICE', healthEndpoint: '/health' },
  'pricing': { service: 'PRICING_SERVICE', healthEndpoint: '/health' },
  'ebay-sniper': { service: 'EBAY_SERVICE', healthEndpoint: '/health' },
  'inventory': { service: 'INVENTORY_SERVICE', healthEndpoint: '/health' },
  'analytics': { service: 'ANALYTICS_SERVICE', healthEndpoint: '/health' },
  'ar-guide': { service: 'AR_GUIDE_SERVICE', healthEndpoint: '/health' },
  'training': { service: 'TRAINING_SERVICE', healthEndpoint: '/health' },
  'chat-agent': { service: 'CHAT_AGENT_SERVICE', healthEndpoint: '/health' },
  'notifications': { service: 'NOTIFICATIONS_SERVICE', healthEndpoint: '/health' },
  'qc-inspector': { service: 'QC_INSPECTOR_SERVICE', healthEndpoint: '/health' },
  'customer-portal': { service: 'CUSTOMER_PORTAL_SERVICE', healthEndpoint: '/health' },
  'schematic-analyzer': { service: 'SCHEMATIC_SERVICE', healthEndpoint: '/health' },
  'workflow-orchestrator': { service: 'WORKFLOW_SERVICE', healthEndpoint: '/health' },
  'predictive-maintenance': { service: 'PREDICTIVE_SERVICE', healthEndpoint: '/health' },
  'parts-matching': { service: 'PARTS_MATCHING_SERVICE', healthEndpoint: '/health' },
  'repair-dna': { service: 'REPAIR_DNA_SERVICE', healthEndpoint: '/health' },
  'knowledge-graph': { service: 'KNOWLEDGE_GRAPH_SERVICE', healthEndpoint: '/health' },
  'collaboration-hub': { service: 'COLLABORATION_SERVICE', healthEndpoint: '/health' },
};

// Thresholds for health determination
const HEALTH_THRESHOLDS = {
  response_time_healthy: 200, // ms
  response_time_degraded: 1000, // ms
  error_rate_healthy: 0.01, // 1%
  error_rate_degraded: 0.05, // 5%
  error_rate_critical: 0.10, // 10%
};

// ==================== System Health Dashboard ====================

app.get('/health', async (c) => {
  const systemHealth = await checkSystemHealth(c.env);
  return c.json(systemHealth);
});

app.get('/health/:worker', async (c) => {
  const workerName = c.req.param('worker');
  const health = await checkWorkerHealth(c.env, workerName);
  return c.json(health);
});

// ==================== Worker Metrics ====================

app.post('/metrics/report', async (c) => {
  const metrics: WorkerMetrics = await c.req.json();

  // Store metrics
  await c.env.D1_DATABASE.prepare(`
    INSERT INTO worker_metrics (
      worker_name, timestamp, requests, errors, avg_latency, p95_latency, p99_latency, success_rate
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
  `).bind(
    metrics.worker_name,
    metrics.timestamp,
    metrics.metrics.requests,
    metrics.metrics.errors,
    metrics.metrics.avg_latency,
    metrics.metrics.p95_latency,
    metrics.metrics.p99_latency,
    metrics.metrics.success_rate
  ).run();

  // Check for anomalies
  const anomalies = await detectAnomalies(c.env, metrics);

  if (anomalies.length > 0) {
    // Trigger auto-healing if needed
    for (const anomaly of anomalies) {
      await handleAnomaly(c.env, metrics.worker_name, anomaly);
    }
  }

  return c.json({ success: true, anomalies_detected: anomalies.length });
});

app.get('/metrics/:worker', async (c) => {
  const workerName = c.req.param('worker');
  const hours = parseInt(c.req.query('hours') || '24');

  const metrics = await c.env.D1_DATABASE.prepare(`
    SELECT * FROM worker_metrics
    WHERE worker_name = ? AND timestamp > datetime('now', '-${hours} hours')
    ORDER BY timestamp DESC
  `).bind(workerName).all();

  return c.json({
    worker: workerName,
    period_hours: hours,
    metrics: metrics.results || [],
    summary: calculateMetricsSummary(metrics.results || []),
  });
});

app.get('/metrics/aggregate', async (c) => {
  const hours = parseInt(c.req.query('hours') || '24');

  const aggregated = await c.env.D1_DATABASE.prepare(`
    SELECT 
      worker_name,
      SUM(requests) as total_requests,
      SUM(errors) as total_errors,
      AVG(avg_latency) as avg_latency,
      AVG(p95_latency) as avg_p95,
      AVG(success_rate) as avg_success_rate
    FROM worker_metrics
    WHERE timestamp > datetime('now', '-${hours} hours')
    GROUP BY worker_name
  `).all();

  return c.json({
    period_hours: hours,
    workers: aggregated.results || [],
    system_totals: calculateSystemTotals(aggregated.results || []),
  });
});

// ==================== Incident Management ====================

app.get('/incidents', async (c) => {
  const status = c.req.query('status');
  const limit = parseInt(c.req.query('limit') || '50');

  let query = 'SELECT * FROM incidents';
  const params: any[] = [];

  if (status) {
    query += ' WHERE status = ?';
    params.push(status);
  }

  query += ' ORDER BY started_at DESC LIMIT ?';
  params.push(limit);

  const incidents = await c.env.D1_DATABASE.prepare(query).bind(...params).all();

  return c.json({
    incidents: (incidents.results || []).map(parseIncident),
    total: incidents.results?.length || 0,
  });
});

app.post('/incidents', async (c) => {
  const { severity, affected_workers, description, trigger_source } = await c.req.json();

  const incidentId = `INC-${Date.now()}`;

  const incident: IncidentReport = {
    id: incidentId,
    severity,
    affected_workers,
    description,
    started_at: new Date().toISOString(),
    status: 'active',
    actions_taken: [],
  };

  // Perform AI analysis
  incident.ai_analysis = await analyzeIncident(c.env, incident);

  // Store incident
  await c.env.D1_DATABASE.prepare(`
    INSERT INTO incidents (
      id, severity, affected_workers, description, ai_analysis, status, started_at
    ) VALUES (?, ?, ?, ?, ?, 'active', datetime('now'))
  `).bind(incidentId, severity, JSON.stringify(affected_workers), description, incident.ai_analysis).run();

  // Notify relevant parties
  await c.env.NOTIFICATIONS_SERVICE.fetch(new Request('https://notifications/send', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      type: 'incident_alert',
      priority: severity === 'critical' ? 'urgent' : 'high',
      title: `System Incident: ${description}`,
      message: incident.ai_analysis,
      metadata: { incident_id: incidentId, affected_workers },
    }),
  }));

  // Attempt auto-remediation for known patterns
  const remediation = await attemptAutoRemediation(c.env, incident);

  return c.json({
    incident,
    auto_remediation: remediation,
  });
});

app.put('/incidents/:id', async (c) => {
  const incidentId = c.req.param('id');
  const updates = await c.req.json();

  await c.env.D1_DATABASE.prepare(`
    UPDATE incidents SET 
      status = COALESCE(?, status),
      root_cause = COALESCE(?, root_cause),
      resolution = COALESCE(?, resolution),
      resolved_at = CASE WHEN ? = 'resolved' THEN datetime('now') ELSE resolved_at END
    WHERE id = ?
  `).bind(updates.status, updates.root_cause, updates.resolution, updates.status, incidentId).run();

  return c.json({ success: true });
});

// ==================== Auto-Healing ====================

app.get('/auto-healing/actions', async (c) => {
  const hours = parseInt(c.req.query('hours') || '24');

  const actions = await c.env.D1_DATABASE.prepare(`
    SELECT * FROM auto_healing_actions
    WHERE timestamp > datetime('now', '-${hours} hours')
    ORDER BY timestamp DESC
  `).all();

  return c.json({
    actions: actions.results || [],
    summary: {
      total: actions.results?.length || 0,
      successful: (actions.results || []).filter((a: any) => a.result === 'success').length,
      failed: (actions.results || []).filter((a: any) => a.result === 'failed').length,
    },
  });
});

app.post('/auto-healing/trigger', async (c) => {
  const { worker_name, action_type, reason } = await c.req.json();

  const action = await executeAutoHealingAction(c.env, worker_name, action_type, reason);

  return c.json(action);
});

app.post('/auto-healing/circuit-breaker/:worker', async (c) => {
  const workerName = c.req.param('worker');
  const { enabled, threshold = 5, window_seconds = 60, cooldown_seconds = 300 } = await c.req.json();

  // Store circuit breaker config
  await c.env.AI_SUPERVISOR_KV.put(
    `circuit-breaker:${workerName}`,
    JSON.stringify({ enabled, threshold, window_seconds, cooldown_seconds, trips: 0, state: 'closed' }),
    { expirationTtl: 86400 }
  );

  return c.json({
    success: true,
    circuit_breaker: { worker: workerName, enabled, threshold, window_seconds, cooldown_seconds },
  });
});

// ==================== Performance Optimization ====================

app.get('/optimize/recommendations', async (c) => {
  const recommendations = await generateOptimizationRecommendations(c.env);
  return c.json({ recommendations });
});

app.post('/optimize/analyze', async (c) => {
  const { focus_areas = ['latency', 'errors', 'throughput'] } = await c.req.json();

  const insights: PerformanceInsight[] = [];

  for (const area of focus_areas) {
    const areaInsights = await analyzePerformanceArea(c.env, area);
    insights.push(...areaInsights);
  }

  // Use AI to prioritize and suggest actions
  const aiPrioritization = await prioritizeInsightsWithAI(c.env, insights);

  return c.json({
    insights,
    ai_prioritization: aiPrioritization,
    immediate_actions: insights.filter(i => i.insight_type === 'critical'),
  });
});

// ==================== Load Balancing ====================

app.get('/load-balancing/status', async (c) => {
  const currentLoad = await getCurrentLoad(c.env);
  return c.json(currentLoad);
});

app.post('/load-balancing/rebalance', async (c) => {
  const decision = await makeLoadBalancingDecision(c.env);

  if (decision.rebalance_actions.length > 0) {
    // Apply rebalancing
    await applyLoadBalancing(c.env, decision);

    // Store decision
    await c.env.D1_DATABASE.prepare(`
      INSERT INTO load_balancing_decisions (
        decision_id, timestamp, current_load, rebalance_actions, reason
      ) VALUES (?, datetime('now'), ?, ?, ?)
    `).bind(
      decision.decision_id,
      JSON.stringify(decision.current_load),
      JSON.stringify(decision.rebalance_actions),
      decision.reason
    ).run();
  }

  return c.json(decision);
});

// ==================== AI-Powered Diagnostics ====================

app.post('/diagnose', async (c) => {
  const { symptoms, affected_workers, time_range } = await c.req.json();

  // Gather relevant data
  const diagnosticData = await gatherDiagnosticData(c.env, affected_workers, time_range);

  // AI analysis
  const diagnosis = await performAIDiagnosis(c.env, symptoms, diagnosticData);

  return c.json(diagnosis);
});

app.post('/predict/issues', async (c) => {
  const { prediction_window_hours = 24 } = await c.req.json();

  const predictions = await predictUpcomingIssues(c.env, prediction_window_hours);

  return c.json({
    prediction_window_hours,
    predictions,
    recommended_preventive_actions: predictions.filter(p => p.probability > 0.7).map(p => p.preventive_action),
  });
});

// ==================== System Configuration ====================

app.get('/config', async (c) => {
  const configs: Record<string, any> = {};

  for (const [name] of Object.entries(WORKERS)) {
    const config = await c.env.AI_SUPERVISOR_KV.get(`config:${name}`);
    configs[name] = config ? JSON.parse(config) : { default: true };
  }

  return c.json({
    workers: configs,
    global: {
      auto_healing_enabled: true,
      alert_thresholds: HEALTH_THRESHOLDS,
      monitoring_interval_ms: 30000,
    },
  });
});

app.put('/config/:worker', async (c) => {
  const workerName = c.req.param('worker');
  const config = await c.req.json();

  await c.env.AI_SUPERVISOR_KV.put(`config:${workerName}`, JSON.stringify(config), { expirationTtl: 86400 * 30 });

  return c.json({ success: true, worker: workerName, config });
});

// ==================== Scheduled Health Check ====================

app.post('/cron/health-check', async (c) => {
  // This would be triggered by a Cron trigger
  const systemHealth = await checkSystemHealth(c.env);

  // Store health snapshot
  await c.env.D1_DATABASE.prepare(`
    INSERT INTO health_snapshots (timestamp, overall_status, healthy_count, degraded_count, unhealthy_count, data)
    VALUES (datetime('now'), ?, ?, ?, ?, ?)
  `).bind(
    systemHealth.overall_status,
    systemHealth.healthy_count,
    systemHealth.degraded_count,
    systemHealth.unhealthy_count,
    JSON.stringify(systemHealth)
  ).run();

  // Handle any issues
  for (const worker of systemHealth.workers) {
    if (worker.status === 'unhealthy') {
      await handleUnhealthyWorker(c.env, worker);
    } else if (worker.status === 'degraded') {
      await handleDegradedWorker(c.env, worker);
    }
  }

  return c.json({
    success: true,
    timestamp: new Date().toISOString(),
    system_status: systemHealth.overall_status,
    actions_taken: systemHealth.workers.filter(w => w.status !== 'healthy').length,
  });
});

// ==================== Helper Functions ====================

async function checkSystemHealth(env: Env): Promise<SystemHealth> {
  const workerHealthChecks = await Promise.all(
    Object.entries(WORKERS).map(([name]) => checkWorkerHealth(env, name))
  );

  const healthyCount = workerHealthChecks.filter(w => w.status === 'healthy').length;
  const degradedCount = workerHealthChecks.filter(w => w.status === 'degraded').length;
  const unhealthyCount = workerHealthChecks.filter(w => w.status === 'unhealthy').length;

  let overallStatus: 'healthy' | 'degraded' | 'critical';
  if (unhealthyCount > 2 || (unhealthyCount / workerHealthChecks.length) > 0.2) {
    overallStatus = 'critical';
  } else if (unhealthyCount > 0 || degradedCount > 3) {
    overallStatus = 'degraded';
  } else {
    overallStatus = 'healthy';
  }

  const recommendations = await generateSystemRecommendations(env, workerHealthChecks);

  return {
    overall_status: overallStatus,
    workers: workerHealthChecks,
    total_workers: workerHealthChecks.length,
    healthy_count: healthyCount,
    degraded_count: degradedCount,
    unhealthy_count: unhealthyCount,
    system_load: calculateSystemLoad(workerHealthChecks),
    recommendations,
    last_updated: new Date().toISOString(),
  };
}

async function checkWorkerHealth(env: Env, workerName: string): Promise<WorkerHealth> {
  const workerConfig = WORKERS[workerName];
  if (!workerConfig) {
    return {
      worker_name: workerName,
      status: 'unknown',
      response_time_ms: 0,
      last_check: new Date().toISOString(),
      error_rate_1h: 0,
      requests_1h: 0,
      avg_response_time_1h: 0,
      last_error: 'Worker not configured',
    };
  }

  const startTime = Date.now();
  let status: WorkerHealth['status'] = 'healthy';
  let lastError: string | undefined;

  try {
    const service = env[workerConfig.service] as Fetcher;
    const response = await service.fetch(new Request(`https://internal${workerConfig.healthEndpoint}`, {
      method: 'GET',
    }));

    const responseTime = Date.now() - startTime;

    if (!response.ok) {
      status = 'unhealthy';
      lastError = `HTTP ${response.status}`;
    } else if (responseTime > HEALTH_THRESHOLDS.response_time_degraded) {
      status = 'degraded';
    } else if (responseTime > HEALTH_THRESHOLDS.response_time_healthy) {
      status = 'degraded';
    }

    // Get historical metrics
    const metrics = await env.D1_DATABASE.prepare(`
      SELECT 
        SUM(requests) as total_requests,
        SUM(errors) as total_errors,
        AVG(avg_latency) as avg_latency
      FROM worker_metrics
      WHERE worker_name = ? AND timestamp > datetime('now', '-1 hour')
    `).bind(workerName).first();

    const errorRate = metrics && (metrics.total_requests as number) > 0
      ? (metrics.total_errors as number) / (metrics.total_requests as number)
      : 0;

    if (errorRate > HEALTH_THRESHOLDS.error_rate_critical) {
      status = 'unhealthy';
    } else if (errorRate > HEALTH_THRESHOLDS.error_rate_degraded) {
      status = 'degraded';
    }

    return {
      worker_name: workerName,
      status,
      response_time_ms: responseTime,
      last_check: new Date().toISOString(),
      error_rate_1h: errorRate,
      requests_1h: (metrics?.total_requests as number) || 0,
      avg_response_time_1h: (metrics?.avg_latency as number) || 0,
      last_error: lastError,
    };
  } catch (error) {
    return {
      worker_name: workerName,
      status: 'unhealthy',
      response_time_ms: Date.now() - startTime,
      last_check: new Date().toISOString(),
      error_rate_1h: 1,
      requests_1h: 0,
      avg_response_time_1h: 0,
      last_error: String(error),
    };
  }
}

async function detectAnomalies(env: Env, metrics: WorkerMetrics): Promise<string[]> {
  const anomalies: string[] = [];

  // Get baseline metrics
  const baseline = await env.D1_DATABASE.prepare(`
    SELECT 
      AVG(avg_latency) as baseline_latency,
      AVG(success_rate) as baseline_success,
      AVG(requests) as baseline_requests
    FROM worker_metrics
    WHERE worker_name = ? AND timestamp > datetime('now', '-7 days')
  `).bind(metrics.worker_name).first();

  if (baseline) {
    // Latency spike detection
    if (metrics.metrics.avg_latency > (baseline.baseline_latency as number) * 2) {
      anomalies.push('latency_spike');
    }

    // Success rate drop
    if (metrics.metrics.success_rate < (baseline.baseline_success as number) * 0.9) {
      anomalies.push('success_rate_drop');
    }

    // Traffic spike (might need scaling)
    if (metrics.metrics.requests > (baseline.baseline_requests as number) * 3) {
      anomalies.push('traffic_spike');
    }
  }

  return anomalies;
}

async function handleAnomaly(env: Env, workerName: string, anomaly: string): Promise<void> {
  // Check circuit breaker
  const cbState = await env.AI_SUPERVISOR_KV.get(`circuit-breaker:${workerName}`);
  if (cbState) {
    const cb = JSON.parse(cbState);
    if (cb.state === 'open') {
      // Circuit is open, don't take action
      return;
    }
  }

  // Take appropriate action based on anomaly type
  switch (anomaly) {
    case 'latency_spike':
      await executeAutoHealingAction(env, workerName, 'cache_clear', 'Latency spike detected');
      break;
    case 'success_rate_drop':
      await executeAutoHealingAction(env, workerName, 'circuit_break', 'Success rate drop detected');
      break;
    case 'traffic_spike':
      await executeAutoHealingAction(env, workerName, 'rate_limit', 'Traffic spike detected');
      break;
  }
}

async function executeAutoHealingAction(
  env: Env,
  workerName: string,
  actionType: AutoHealingAction['action_type'],
  trigger: string
): Promise<AutoHealingAction> {
  const actionId = `AH-${Date.now()}`;

  const action: AutoHealingAction = {
    action_id: actionId,
    worker_name: workerName,
    action_type: actionType,
    trigger,
    timestamp: new Date().toISOString(),
    result: 'pending',
    details: '',
  };

  try {
    switch (actionType) {
      case 'circuit_break':
        // Open circuit breaker
        const cbState = await env.AI_SUPERVISOR_KV.get(`circuit-breaker:${workerName}`);
        const cb = cbState ? JSON.parse(cbState) : { enabled: true, threshold: 5, window_seconds: 60, cooldown_seconds: 300, trips: 0 };
        cb.state = 'open';
        cb.opened_at = Date.now();
        await env.AI_SUPERVISOR_KV.put(`circuit-breaker:${workerName}`, JSON.stringify(cb), { expirationTtl: cb.cooldown_seconds });
        action.details = `Circuit breaker opened for ${cb.cooldown_seconds} seconds`;
        break;

      case 'rate_limit':
        // Apply rate limiting
        await env.AI_SUPERVISOR_KV.put(`rate-limit:${workerName}`, JSON.stringify({
          enabled: true,
          requests_per_second: 100,
          applied_at: Date.now(),
        }), { expirationTtl: 3600 });
        action.details = 'Rate limiting applied: 100 req/s';
        break;

      case 'cache_clear':
        // Signal cache clear (would need implementation in worker)
        await env.AI_SUPERVISOR_KV.put(`cache-clear:${workerName}`, JSON.stringify({
          requested_at: Date.now(),
        }), { expirationTtl: 60 });
        action.details = 'Cache clear signal sent';
        break;

      default:
        action.details = `Action type ${actionType} not implemented`;
    }

    action.result = 'success';
  } catch (error) {
    action.result = 'failed';
    action.details = String(error);
  }

  // Store action
  await env.D1_DATABASE.prepare(`
    INSERT INTO auto_healing_actions (
      action_id, worker_name, action_type, trigger, timestamp, result, details
    ) VALUES (?, ?, ?, ?, datetime('now'), ?, ?)
  `).bind(actionId, workerName, actionType, trigger, action.result, action.details).run();

  return action;
}

async function analyzeIncident(env: Env, incident: IncidentReport): Promise<string> {
  const response = await env.AI.run('@cf/meta/llama-3-8b-instruct', {
    messages: [
      {
        role: 'system',
        content: 'You are an expert SRE analyzing system incidents. Provide concise root cause analysis and recommended actions.',
      },
      {
        role: 'user',
        content: `Analyze this incident:
Severity: ${incident.severity}
Affected Workers: ${incident.affected_workers.join(', ')}
Description: ${incident.description}

Provide: 1) Likely root cause, 2) Immediate actions, 3) Long-term fixes`,
      },
    ],
  });

  return (response as any).response || 'Unable to analyze incident';
}

async function attemptAutoRemediation(env: Env, incident: IncidentReport): Promise<any> {
  const actions: string[] = [];

  // Known remediation patterns
  if (incident.description.includes('high latency')) {
    for (const worker of incident.affected_workers) {
      await executeAutoHealingAction(env, worker, 'cache_clear', `Incident ${incident.id}`);
      actions.push(`Cache clear on ${worker}`);
    }
  }

  if (incident.description.includes('error spike')) {
    for (const worker of incident.affected_workers) {
      await executeAutoHealingAction(env, worker, 'circuit_break', `Incident ${incident.id}`);
      actions.push(`Circuit breaker on ${worker}`);
    }
  }

  return {
    attempted: actions.length > 0,
    actions,
  };
}

async function generateSystemRecommendations(env: Env, workers: WorkerHealth[]): Promise<SystemRecommendation[]> {
  const recommendations: SystemRecommendation[] = [];

  // Unhealthy workers
  const unhealthy = workers.filter(w => w.status === 'unhealthy');
  if (unhealthy.length > 0) {
    recommendations.push({
      priority: 'critical',
      category: 'availability',
      recommendation: `Investigate and restore ${unhealthy.length} unhealthy workers`,
      affected_workers: unhealthy.map(w => w.worker_name),
      action_type: 'manual',
      estimated_impact: 'Service disruption',
    });
  }

  // High error rates
  const highError = workers.filter(w => w.error_rate_1h > HEALTH_THRESHOLDS.error_rate_degraded);
  if (highError.length > 0) {
    recommendations.push({
      priority: 'high',
      category: 'reliability',
      recommendation: `Review error logs for workers with high error rates`,
      affected_workers: highError.map(w => w.worker_name),
      action_type: 'manual',
      estimated_impact: 'User experience degradation',
    });
  }

  // Slow response times
  const slow = workers.filter(w => w.avg_response_time_1h > HEALTH_THRESHOLDS.response_time_degraded);
  if (slow.length > 0) {
    recommendations.push({
      priority: 'medium',
      category: 'performance',
      recommendation: `Optimize slow workers or consider caching`,
      affected_workers: slow.map(w => w.worker_name),
      action_type: 'scheduled',
      estimated_impact: 'Improved user experience',
    });
  }

  return recommendations;
}

async function generateOptimizationRecommendations(env: Env): Promise<SystemRecommendation[]> {
  // Get recent metrics
  const metrics = await env.D1_DATABASE.prepare(`
    SELECT 
      worker_name,
      AVG(avg_latency) as avg_latency,
      AVG(p95_latency) as p95_latency,
      SUM(errors) as total_errors,
      SUM(requests) as total_requests
    FROM worker_metrics
    WHERE timestamp > datetime('now', '-24 hours')
    GROUP BY worker_name
  `).all();

  const recommendations: SystemRecommendation[] = [];

  for (const row of metrics.results || []) {
    const m = row as any;

    // High P95 latency (tail latency issue)
    if (m.p95_latency > m.avg_latency * 3) {
      recommendations.push({
        priority: 'medium',
        category: 'performance',
        recommendation: `${m.worker_name} has high tail latency - investigate outlier requests`,
        affected_workers: [m.worker_name],
        action_type: 'manual',
        estimated_impact: '~30% latency improvement for slow requests',
      });
    }

    // Low traffic - could potentially consolidate
    if (m.total_requests < 100) {
      recommendations.push({
        priority: 'low',
        category: 'cost',
        recommendation: `${m.worker_name} has low traffic - consider consolidation or on-demand scaling`,
        affected_workers: [m.worker_name],
        action_type: 'scheduled',
        estimated_impact: 'Cost reduction',
      });
    }
  }

  return recommendations;
}

async function analyzePerformanceArea(env: Env, area: string): Promise<PerformanceInsight[]> {
  const insights: PerformanceInsight[] = [];

  switch (area) {
    case 'latency':
      const slowest = await env.D1_DATABASE.prepare(`
        SELECT worker_name, AVG(avg_latency) as avg_lat
        FROM worker_metrics
        WHERE timestamp > datetime('now', '-24 hours')
        GROUP BY worker_name
        ORDER BY avg_lat DESC
        LIMIT 5
      `).all();

      for (const row of slowest.results || []) {
        const r = row as any;
        insights.push({
          insight_type: 'latency',
          worker_name: r.worker_name,
          description: `Average latency of ${Math.round(r.avg_lat)}ms`,
          data: { avg_latency: r.avg_lat },
          recommendation: 'Consider caching, query optimization, or async processing',
          potential_improvement: '30-50% latency reduction',
        });
      }
      break;

    case 'errors':
      const errorProne = await env.D1_DATABASE.prepare(`
        SELECT worker_name, SUM(errors) as total_errors, SUM(requests) as total_requests
        FROM worker_metrics
        WHERE timestamp > datetime('now', '-24 hours')
        GROUP BY worker_name
        HAVING total_errors > 0
        ORDER BY total_errors DESC
      `).all();

      for (const row of errorProne.results || []) {
        const r = row as any;
        const errorRate = r.total_errors / r.total_requests;
        insights.push({
          insight_type: errorRate > 0.05 ? 'critical' : 'warning',
          worker_name: r.worker_name,
          description: `${r.total_errors} errors (${(errorRate * 100).toFixed(2)}% error rate)`,
          data: { errors: r.total_errors, error_rate: errorRate },
          recommendation: 'Review error logs and implement better error handling',
          potential_improvement: 'Improved reliability and user experience',
        });
      }
      break;
  }

  return insights;
}

async function prioritizeInsightsWithAI(env: Env, insights: PerformanceInsight[]): Promise<any> {
  if (insights.length === 0) return { prioritized: [] };

  const response = await env.AI.run('@cf/meta/llama-3-8b-instruct', {
    messages: [
      {
        role: 'system',
        content: 'You are an expert SRE. Prioritize performance insights and suggest action order.',
      },
      {
        role: 'user',
        content: `Prioritize these insights: ${JSON.stringify(insights.slice(0, 10))}`,
      },
    ],
  });

  return {
    ai_recommendation: (response as any).response,
    insights_count: insights.length,
  };
}

async function getCurrentLoad(env: Env): Promise<any> {
  const load = await env.D1_DATABASE.prepare(`
    SELECT worker_name, SUM(requests) as load
    FROM worker_metrics
    WHERE timestamp > datetime('now', '-5 minutes')
    GROUP BY worker_name
  `).all();

  const loadMap: Record<string, number> = {};
  for (const row of load.results || []) {
    const r = row as any;
    loadMap[r.worker_name] = r.load;
  }

  return {
    current_load: loadMap,
    timestamp: new Date().toISOString(),
    total_load: Object.values(loadMap).reduce((a, b) => a + b, 0),
  };
}

async function makeLoadBalancingDecision(env: Env): Promise<LoadBalancingDecision> {
  const currentLoad = await getCurrentLoad(env);

  const decision: LoadBalancingDecision = {
    decision_id: `LB-${Date.now()}`,
    timestamp: new Date().toISOString(),
    current_load: currentLoad.current_load,
    rebalance_actions: [],
    reason: 'Regular load balancing check',
  };

  // Simple load balancing logic - in production would be more sophisticated
  const loads = Object.entries(currentLoad.current_load as Record<string, number>);
  const avgLoad = currentLoad.total_load / loads.length;

  for (const [worker, load] of loads) {
    if (load > avgLoad * 2) {
      decision.rebalance_actions.push({
        from_worker: worker,
        to_worker: 'overflow',
        traffic_percentage: 20,
      });
      decision.reason = `${worker} is experiencing high load`;
    }
  }

  return decision;
}

async function applyLoadBalancing(env: Env, decision: LoadBalancingDecision): Promise<void> {
  for (const action of decision.rebalance_actions) {
    await env.AI_SUPERVISOR_KV.put(
      `load-balance:${action.from_worker}`,
      JSON.stringify({
        redirect_percentage: action.traffic_percentage,
        to_worker: action.to_worker,
        applied_at: Date.now(),
      }),
      { expirationTtl: 3600 }
    );
  }
}

async function gatherDiagnosticData(env: Env, affectedWorkers: string[], timeRange: string): Promise<any> {
  const data: Record<string, any> = {};

  for (const worker of affectedWorkers) {
    const metrics = await env.D1_DATABASE.prepare(`
      SELECT * FROM worker_metrics
      WHERE worker_name = ? AND timestamp > datetime('now', '-${timeRange || '1 hour'}')
      ORDER BY timestamp DESC
    `).bind(worker).all();

    data[worker] = {
      metrics: metrics.results,
      recent_errors: metrics.results?.filter((m: any) => m.errors > 0),
    };
  }

  return data;
}

async function performAIDiagnosis(env: Env, symptoms: string[], diagnosticData: any): Promise<any> {
  const response = await env.AI.run('@cf/meta/llama-3-8b-instruct', {
    messages: [
      {
        role: 'system',
        content: 'You are an expert systems diagnostician. Analyze symptoms and data to diagnose issues.',
      },
      {
        role: 'user',
        content: `Symptoms: ${symptoms.join(', ')}\nData: ${JSON.stringify(diagnosticData).slice(0, 2000)}\n\nProvide diagnosis with: 1) Root cause, 2) Affected components, 3) Recommended fix, 4) Prevention`,
      },
    ],
  });

  return {
    diagnosis: (response as any).response,
    symptoms,
    timestamp: new Date().toISOString(),
  };
}

async function predictUpcomingIssues(env: Env, windowHours: number): Promise<any[]> {
  // Get trend data
  const trends = await env.D1_DATABASE.prepare(`
    SELECT 
      worker_name,
      AVG(CASE WHEN timestamp > datetime('now', '-${windowHours} hours') THEN errors ELSE NULL END) as recent_errors,
      AVG(CASE WHEN timestamp < datetime('now', '-${windowHours} hours') THEN errors ELSE NULL END) as historical_errors,
      AVG(CASE WHEN timestamp > datetime('now', '-${windowHours} hours') THEN avg_latency ELSE NULL END) as recent_latency,
      AVG(CASE WHEN timestamp < datetime('now', '-${windowHours} hours') THEN avg_latency ELSE NULL END) as historical_latency
    FROM worker_metrics
    WHERE timestamp > datetime('now', '-${windowHours * 2} hours')
    GROUP BY worker_name
  `).all();

  const predictions: any[] = [];

  for (const row of trends.results || []) {
    const t = row as any;

    // Error rate increasing
    if (t.recent_errors > t.historical_errors * 1.5 && t.historical_errors > 0) {
      predictions.push({
        worker: t.worker_name,
        issue: 'error_spike',
        probability: Math.min(0.9, t.recent_errors / t.historical_errors - 1),
        timeframe: `Next ${windowHours} hours`,
        preventive_action: 'Review recent changes and enable enhanced monitoring',
      });
    }

    // Latency degradation
    if (t.recent_latency > t.historical_latency * 1.5 && t.historical_latency > 0) {
      predictions.push({
        worker: t.worker_name,
        issue: 'performance_degradation',
        probability: Math.min(0.8, t.recent_latency / t.historical_latency - 1),
        timeframe: `Next ${windowHours} hours`,
        preventive_action: 'Investigate resource usage and consider scaling',
      });
    }
  }

  return predictions;
}

async function handleUnhealthyWorker(env: Env, worker: WorkerHealth): Promise<void> {
  // Create incident
  await env.D1_DATABASE.prepare(`
    INSERT INTO incidents (
      id, severity, affected_workers, description, status, started_at
    ) VALUES (?, 'high', ?, ?, 'active', datetime('now'))
  `).bind(
    `INC-AUTO-${Date.now()}`,
    JSON.stringify([worker.worker_name]),
    `Worker ${worker.worker_name} is unhealthy: ${worker.last_error || 'Unknown error'}`
  ).run();

  // Attempt auto-healing
  await executeAutoHealingAction(env, worker.worker_name, 'circuit_break', 'Unhealthy status detected');
}

async function handleDegradedWorker(env: Env, worker: WorkerHealth): Promise<void> {
  // Just log and potentially rate limit
  if (worker.error_rate_1h > HEALTH_THRESHOLDS.error_rate_degraded) {
    await executeAutoHealingAction(env, worker.worker_name, 'rate_limit', 'Degraded status with high error rate');
  }
}

function calculateSystemLoad(workers: WorkerHealth[]): number {
  const totalRequests = workers.reduce((sum, w) => sum + w.requests_1h, 0);
  const expectedCapacity = workers.length * 10000; // Assumed capacity per worker
  return Math.min(1, totalRequests / expectedCapacity);
}

function calculateMetricsSummary(metrics: any[]): any {
  if (metrics.length === 0) return {};

  return {
    total_requests: metrics.reduce((sum, m) => sum + m.requests, 0),
    total_errors: metrics.reduce((sum, m) => sum + m.errors, 0),
    avg_latency: metrics.reduce((sum, m) => sum + m.avg_latency, 0) / metrics.length,
    avg_success_rate: metrics.reduce((sum, m) => sum + m.success_rate, 0) / metrics.length,
  };
}

function calculateSystemTotals(aggregated: any[]): any {
  return {
    total_requests: aggregated.reduce((sum, w) => sum + (w.total_requests || 0), 0),
    total_errors: aggregated.reduce((sum, w) => sum + (w.total_errors || 0), 0),
    avg_system_latency: aggregated.reduce((sum, w) => sum + (w.avg_latency || 0), 0) / aggregated.length,
    workers_reported: aggregated.length,
  };
}

function parseIncident(row: any): IncidentReport {
  return {
    id: row.id,
    severity: row.severity,
    affected_workers: JSON.parse(row.affected_workers || '[]'),
    description: row.description,
    root_cause: row.root_cause,
    resolution: row.resolution,
    started_at: row.started_at,
    resolved_at: row.resolved_at,
    status: row.status,
    ai_analysis: row.ai_analysis,
    actions_taken: JSON.parse(row.actions_taken || '[]'),
  };
}

export default app;
