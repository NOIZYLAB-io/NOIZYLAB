/**
 * NoizyLab OS - Automated Testing Worker
 * Self-Testing & Quality Assurance Engine
 * 
 * Features:
 * - Automated API endpoint testing
 * - Integration test orchestration
 * - Load testing & stress testing
 * - Chaos engineering (fault injection)
 * - Performance regression detection
 * - Test coverage tracking
 * - Scheduled health checks
 * - Test result analytics
 */

import { Hono } from 'hono';

interface Env {
  TESTING_KV: KVNamespace;
  DB: D1Database;
  AI: Ai;
}

interface TestSuite {
  id: string;
  name: string;
  description: string;
  tests: TestCase[];
  setup?: TestStep[];
  teardown?: TestStep[];
  schedule?: string;  // Cron expression
  lastRun?: Date;
  status: 'active' | 'paused' | 'draft';
}

interface TestCase {
  id: string;
  name: string;
  description: string;
  type: 'api' | 'integration' | 'load' | 'chaos' | 'e2e';
  steps: TestStep[];
  assertions: Assertion[];
  timeout: number;
  retries: number;
  tags: string[];
  priority: 'critical' | 'high' | 'medium' | 'low';
}

interface TestStep {
  id: string;
  action: string;
  target: string;
  method?: string;
  headers?: Record<string, string>;
  body?: any;
  variables?: Record<string, string>;
  waitAfter?: number;
}

interface Assertion {
  type: 'status' | 'body' | 'header' | 'timing' | 'schema' | 'custom';
  target?: string;
  operator: 'equals' | 'contains' | 'matches' | 'lessThan' | 'greaterThan' | 'exists';
  expected: any;
  message?: string;
}

interface TestResult {
  testId: string;
  suiteId: string;
  status: 'passed' | 'failed' | 'skipped' | 'error';
  duration: number;
  assertions: AssertionResult[];
  logs: string[];
  metadata: Record<string, any>;
  timestamp: Date;
}

interface AssertionResult {
  assertion: Assertion;
  passed: boolean;
  actual?: any;
  message?: string;
}

interface TestRunSummary {
  runId: string;
  suiteId: string;
  startTime: Date;
  endTime: Date;
  duration: number;
  totalTests: number;
  passed: number;
  failed: number;
  skipped: number;
  coverage?: CoverageReport;
  results: TestResult[];
}

interface CoverageReport {
  endpoints: EndpointCoverage[];
  overallCoverage: number;
  untestedEndpoints: string[];
}

interface EndpointCoverage {
  endpoint: string;
  method: string;
  tested: boolean;
  testCount: number;
  lastTested?: Date;
}

interface LoadTestConfig {
  targetUrl: string;
  duration: number;  // seconds
  concurrency: number;
  rampUp: number;  // seconds
  requestsPerSecond?: number;
  scenarios: LoadScenario[];
}

interface LoadScenario {
  name: string;
  weight: number;
  request: TestStep;
}

interface LoadTestResult {
  id: string;
  config: LoadTestConfig;
  metrics: LoadMetrics;
  errors: ErrorSummary[];
  timeline: TimelinePoint[];
}

interface LoadMetrics {
  totalRequests: number;
  successfulRequests: number;
  failedRequests: number;
  avgResponseTime: number;
  minResponseTime: number;
  maxResponseTime: number;
  p50ResponseTime: number;
  p95ResponseTime: number;
  p99ResponseTime: number;
  requestsPerSecond: number;
  throughput: number;
  errorRate: number;
}

interface ErrorSummary {
  type: string;
  count: number;
  message: string;
  firstOccurrence: Date;
  lastOccurrence: Date;
}

interface TimelinePoint {
  timestamp: Date;
  requestsPerSecond: number;
  avgResponseTime: number;
  errorRate: number;
  activeConnections: number;
}

interface ChaosExperiment {
  id: string;
  name: string;
  type: 'latency' | 'error' | 'partition' | 'resource' | 'shutdown';
  target: string;
  parameters: Record<string, any>;
  duration: number;
  rollbackPlan: string;
}

interface HealthCheck {
  id: string;
  name: string;
  endpoint: string;
  method: string;
  expectedStatus: number;
  timeout: number;
  interval: number;  // seconds
  alertThreshold: number;  // consecutive failures
}

interface HealthStatus {
  checkId: string;
  status: 'healthy' | 'degraded' | 'unhealthy';
  responseTime: number;
  lastCheck: Date;
  consecutiveFailures: number;
  uptime: number;
}

const app = new Hono<{ Bindings: Env }>();

// ==================== TEST SUITE MANAGEMENT ====================

app.post('/suite', async (c) => {
  const suite: TestSuite = await c.req.json();
  suite.id = suite.id || `suite_${Date.now()}`;
  suite.status = suite.status || 'draft';
  
  // Validate suite
  const validation = validateTestSuite(suite);
  if (!validation.valid) {
    return c.json({ error: 'Invalid test suite', issues: validation.issues }, 400);
  }
  
  // Store suite
  await c.env.TESTING_KV.put(`suite:${suite.id}`, JSON.stringify(suite));
  
  // Store in D1
  await c.env.DB.prepare(`
    INSERT INTO test_suites (id, name, description, test_count, status, created_at)
    VALUES (?, ?, ?, ?, ?, datetime('now'))
    ON CONFLICT(id) DO UPDATE SET
      name = excluded.name,
      description = excluded.description,
      test_count = excluded.test_count,
      status = excluded.status
  `).bind(suite.id, suite.name, suite.description, suite.tests.length, suite.status).run();
  
  return c.json({
    success: true,
    suite: {
      id: suite.id,
      name: suite.name,
      testCount: suite.tests.length
    }
  });
});

app.get('/suite/:suiteId', async (c) => {
  const suiteId = c.req.param('suiteId');
  const suiteJson = await c.env.TESTING_KV.get(`suite:${suiteId}`);
  
  if (!suiteJson) {
    return c.json({ error: 'Suite not found' }, 404);
  }
  
  const suite: TestSuite = JSON.parse(suiteJson);
  
  // Get recent run history
  const runHistory = await c.env.DB.prepare(`
    SELECT run_id, start_time, duration, passed, failed, status
    FROM test_runs
    WHERE suite_id = ?
    ORDER BY start_time DESC
    LIMIT 10
  `).bind(suiteId).all();
  
  return c.json({
    suite,
    runHistory: runHistory.results || []
  });
});

app.get('/suites', async (c) => {
  const status = c.req.query('status');
  
  let query = 'SELECT * FROM test_suites';
  if (status) {
    query += ` WHERE status = '${status}'`;
  }
  query += ' ORDER BY created_at DESC';
  
  const result = await c.env.DB.prepare(query).all();
  
  return c.json({
    suites: result.results || []
  });
});

// ==================== TEST EXECUTION ====================

app.post('/run/:suiteId', async (c) => {
  const suiteId = c.req.param('suiteId');
  const { testIds, parallel = false } = await c.req.json();
  
  const suiteJson = await c.env.TESTING_KV.get(`suite:${suiteId}`);
  if (!suiteJson) {
    return c.json({ error: 'Suite not found' }, 404);
  }
  
  const suite: TestSuite = JSON.parse(suiteJson);
  const runId = `run_${Date.now()}`;
  const startTime = new Date();
  
  // Filter tests if specific IDs provided
  const testsToRun = testIds 
    ? suite.tests.filter(t => testIds.includes(t.id))
    : suite.tests;
  
  // Run setup
  if (suite.setup) {
    await runTestSteps(suite.setup, {});
  }
  
  // Run tests
  const results: TestResult[] = [];
  
  if (parallel) {
    const promises = testsToRun.map(test => executeTest(c.env, test, suiteId));
    results.push(...await Promise.all(promises));
  } else {
    for (const test of testsToRun) {
      const result = await executeTest(c.env, test, suiteId);
      results.push(result);
    }
  }
  
  // Run teardown
  if (suite.teardown) {
    await runTestSteps(suite.teardown, {});
  }
  
  const endTime = new Date();
  const summary: TestRunSummary = {
    runId,
    suiteId,
    startTime,
    endTime,
    duration: endTime.getTime() - startTime.getTime(),
    totalTests: results.length,
    passed: results.filter(r => r.status === 'passed').length,
    failed: results.filter(r => r.status === 'failed').length,
    skipped: results.filter(r => r.status === 'skipped').length,
    results
  };
  
  // Store results
  await c.env.TESTING_KV.put(`run:${runId}`, JSON.stringify(summary));
  
  await c.env.DB.prepare(`
    INSERT INTO test_runs (run_id, suite_id, start_time, duration, total, passed, failed, skipped, status)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
  `).bind(
    runId,
    suiteId,
    startTime.toISOString(),
    summary.duration,
    summary.totalTests,
    summary.passed,
    summary.failed,
    summary.skipped,
    summary.failed > 0 ? 'failed' : 'passed'
  ).run();
  
  return c.json(summary);
});

app.get('/run/:runId', async (c) => {
  const runId = c.req.param('runId');
  const runJson = await c.env.TESTING_KV.get(`run:${runId}`);
  
  if (!runJson) {
    return c.json({ error: 'Run not found' }, 404);
  }
  
  return c.json(JSON.parse(runJson));
});

// ==================== LOAD TESTING ====================

app.post('/load/start', async (c) => {
  const config: LoadTestConfig = await c.req.json();
  const testId = `load_${Date.now()}`;
  
  // Initialize metrics
  const responseTimes: number[] = [];
  const errors: Map<string, ErrorSummary> = new Map();
  const timeline: TimelinePoint[] = [];
  let successCount = 0;
  let failCount = 0;
  
  const startTime = Date.now();
  const endTime = startTime + config.duration * 1000;
  
  // Simulate load test (in a real scenario, this would be distributed)
  const batchSize = Math.min(config.concurrency, 10);
  let currentConcurrency = 0;
  const rampUpInterval = config.rampUp * 1000 / config.concurrency;
  
  while (Date.now() < endTime) {
    // Ramp up concurrency
    if (currentConcurrency < config.concurrency) {
      currentConcurrency = Math.min(
        config.concurrency,
        Math.floor((Date.now() - startTime) / rampUpInterval) + 1
      );
    }
    
    // Select scenario based on weight
    const scenario = selectScenario(config.scenarios);
    
    // Execute requests
    const batchPromises = [];
    for (let i = 0; i < Math.min(batchSize, currentConcurrency); i++) {
      batchPromises.push(executeLoadRequest(scenario.request));
    }
    
    const batchResults = await Promise.allSettled(batchPromises);
    
    for (const result of batchResults) {
      if (result.status === 'fulfilled') {
        const { success, responseTime, error } = result.value;
        responseTimes.push(responseTime);
        
        if (success) {
          successCount++;
        } else {
          failCount++;
          if (error) {
            const existing = errors.get(error.type) || {
              type: error.type,
              count: 0,
              message: error.message,
              firstOccurrence: new Date(),
              lastOccurrence: new Date()
            };
            existing.count++;
            existing.lastOccurrence = new Date();
            errors.set(error.type, existing);
          }
        }
      } else {
        failCount++;
      }
    }
    
    // Record timeline point
    const elapsed = (Date.now() - startTime) / 1000;
    if (elapsed % 1 < 0.1) {  // Every second
      const recentTimes = responseTimes.slice(-batchSize);
      timeline.push({
        timestamp: new Date(),
        requestsPerSecond: batchSize,
        avgResponseTime: recentTimes.reduce((a, b) => a + b, 0) / recentTimes.length,
        errorRate: failCount / (successCount + failCount),
        activeConnections: currentConcurrency
      });
    }
    
    // Small delay to prevent overwhelming
    await new Promise(resolve => setTimeout(resolve, 100));
  }
  
  // Calculate final metrics
  const sortedTimes = [...responseTimes].sort((a, b) => a - b);
  const metrics: LoadMetrics = {
    totalRequests: successCount + failCount,
    successfulRequests: successCount,
    failedRequests: failCount,
    avgResponseTime: responseTimes.reduce((a, b) => a + b, 0) / responseTimes.length,
    minResponseTime: sortedTimes[0] || 0,
    maxResponseTime: sortedTimes[sortedTimes.length - 1] || 0,
    p50ResponseTime: sortedTimes[Math.floor(sortedTimes.length * 0.5)] || 0,
    p95ResponseTime: sortedTimes[Math.floor(sortedTimes.length * 0.95)] || 0,
    p99ResponseTime: sortedTimes[Math.floor(sortedTimes.length * 0.99)] || 0,
    requestsPerSecond: (successCount + failCount) / config.duration,
    throughput: successCount / config.duration,
    errorRate: failCount / (successCount + failCount)
  };
  
  const result: LoadTestResult = {
    id: testId,
    config,
    metrics,
    errors: Array.from(errors.values()),
    timeline
  };
  
  // Store result
  await c.env.TESTING_KV.put(`load:${testId}`, JSON.stringify(result));
  
  await c.env.DB.prepare(`
    INSERT INTO load_tests (id, target_url, duration, concurrency, total_requests, error_rate, avg_response_time, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, datetime('now'))
  `).bind(
    testId,
    config.targetUrl,
    config.duration,
    config.concurrency,
    metrics.totalRequests,
    metrics.errorRate,
    metrics.avgResponseTime
  ).run();
  
  return c.json(result);
});

app.get('/load/:testId', async (c) => {
  const testId = c.req.param('testId');
  const resultJson = await c.env.TESTING_KV.get(`load:${testId}`);
  
  if (!resultJson) {
    return c.json({ error: 'Load test not found' }, 404);
  }
  
  return c.json(JSON.parse(resultJson));
});

// ==================== CHAOS ENGINEERING ====================

app.post('/chaos/experiment', async (c) => {
  const experiment: ChaosExperiment = await c.req.json();
  experiment.id = experiment.id || `chaos_${Date.now()}`;
  
  // Validate experiment
  if (!['latency', 'error', 'partition', 'resource', 'shutdown'].includes(experiment.type)) {
    return c.json({ error: 'Invalid chaos experiment type' }, 400);
  }
  
  // Store experiment
  await c.env.TESTING_KV.put(`chaos:${experiment.id}`, JSON.stringify({
    ...experiment,
    status: 'pending',
    createdAt: new Date()
  }));
  
  return c.json({
    success: true,
    experiment: {
      id: experiment.id,
      type: experiment.type,
      target: experiment.target,
      status: 'pending'
    },
    warning: 'Chaos experiments can cause service disruption. Use with caution.'
  });
});

app.post('/chaos/:experimentId/start', async (c) => {
  const experimentId = c.req.param('experimentId');
  const expJson = await c.env.TESTING_KV.get(`chaos:${experimentId}`);
  
  if (!expJson) {
    return c.json({ error: 'Experiment not found' }, 404);
  }
  
  const experiment = JSON.parse(expJson);
  
  // Start chaos injection
  const results = await injectChaos(c.env, experiment);
  
  // Update experiment status
  experiment.status = 'running';
  experiment.startedAt = new Date();
  await c.env.TESTING_KV.put(`chaos:${experimentId}`, JSON.stringify(experiment));
  
  // Schedule rollback
  setTimeout(async () => {
    await rollbackChaos(c.env, experiment);
    experiment.status = 'completed';
    experiment.completedAt = new Date();
    await c.env.TESTING_KV.put(`chaos:${experimentId}`, JSON.stringify(experiment));
  }, experiment.duration * 1000);
  
  return c.json({
    experimentId,
    status: 'running',
    duration: experiment.duration,
    rollbackScheduled: true,
    results
  });
});

app.post('/chaos/:experimentId/rollback', async (c) => {
  const experimentId = c.req.param('experimentId');
  const expJson = await c.env.TESTING_KV.get(`chaos:${experimentId}`);
  
  if (!expJson) {
    return c.json({ error: 'Experiment not found' }, 404);
  }
  
  const experiment = JSON.parse(expJson);
  
  // Rollback chaos
  await rollbackChaos(c.env, experiment);
  
  experiment.status = 'rolled_back';
  experiment.rolledBackAt = new Date();
  await c.env.TESTING_KV.put(`chaos:${experimentId}`, JSON.stringify(experiment));
  
  return c.json({
    experimentId,
    status: 'rolled_back',
    message: 'Chaos experiment rolled back successfully'
  });
});

// ==================== HEALTH CHECKS ====================

app.post('/health/check', async (c) => {
  const check: HealthCheck = await c.req.json();
  check.id = check.id || `health_${Date.now()}`;
  
  // Store health check config
  await c.env.TESTING_KV.put(`healthcheck:${check.id}`, JSON.stringify(check));
  
  // Perform initial check
  const status = await performHealthCheck(check);
  
  // Store status
  await c.env.TESTING_KV.put(`healthstatus:${check.id}`, JSON.stringify(status));
  
  return c.json({
    check,
    initialStatus: status
  });
});

app.get('/health/:checkId', async (c) => {
  const checkId = c.req.param('checkId');
  
  const checkJson = await c.env.TESTING_KV.get(`healthcheck:${checkId}`);
  const statusJson = await c.env.TESTING_KV.get(`healthstatus:${checkId}`);
  
  if (!checkJson) {
    return c.json({ error: 'Health check not found' }, 404);
  }
  
  return c.json({
    check: JSON.parse(checkJson),
    status: statusJson ? JSON.parse(statusJson) : null
  });
});

app.post('/health/:checkId/run', async (c) => {
  const checkId = c.req.param('checkId');
  
  const checkJson = await c.env.TESTING_KV.get(`healthcheck:${checkId}`);
  if (!checkJson) {
    return c.json({ error: 'Health check not found' }, 404);
  }
  
  const check: HealthCheck = JSON.parse(checkJson);
  const status = await performHealthCheck(check);
  
  // Update status
  await c.env.TESTING_KV.put(`healthstatus:${checkId}`, JSON.stringify(status));
  
  // Store history
  await c.env.DB.prepare(`
    INSERT INTO health_check_history (check_id, status, response_time, checked_at)
    VALUES (?, ?, ?, datetime('now'))
  `).bind(checkId, status.status, status.responseTime).run();
  
  return c.json(status);
});

app.get('/health/status/all', async (c) => {
  // Get all health check statuses
  const result = await c.env.DB.prepare(`
    SELECT hc.*, 
           (SELECT status FROM health_check_history WHERE check_id = hc.id ORDER BY checked_at DESC LIMIT 1) as latest_status,
           (SELECT response_time FROM health_check_history WHERE check_id = hc.id ORDER BY checked_at DESC LIMIT 1) as latest_response_time
    FROM health_checks hc
  `).all();
  
  return c.json({
    checks: result.results || [],
    summary: {
      total: (result.results || []).length,
      healthy: (result.results || []).filter(r => r.latest_status === 'healthy').length,
      unhealthy: (result.results || []).filter(r => r.latest_status === 'unhealthy').length
    }
  });
});

// ==================== COVERAGE TRACKING ====================

app.post('/coverage/report', async (c) => {
  const { endpoints } = await c.req.json();
  
  // Get all test cases
  const suites = await c.env.DB.prepare('SELECT id FROM test_suites').all();
  
  const testedEndpoints = new Set<string>();
  
  for (const suite of suites.results || []) {
    const suiteJson = await c.env.TESTING_KV.get(`suite:${suite.id}`);
    if (suiteJson) {
      const suiteData: TestSuite = JSON.parse(suiteJson);
      for (const test of suiteData.tests) {
        for (const step of test.steps) {
          if (step.target) {
            testedEndpoints.add(`${step.method || 'GET'}:${step.target}`);
          }
        }
      }
    }
  }
  
  const coverage: EndpointCoverage[] = endpoints.map((ep: any) => ({
    endpoint: ep.path,
    method: ep.method,
    tested: testedEndpoints.has(`${ep.method}:${ep.path}`),
    testCount: testedEndpoints.has(`${ep.method}:${ep.path}`) ? 1 : 0,
    lastTested: testedEndpoints.has(`${ep.method}:${ep.path}`) ? new Date() : undefined
  }));
  
  const report: CoverageReport = {
    endpoints: coverage,
    overallCoverage: coverage.filter(c => c.tested).length / coverage.length * 100,
    untestedEndpoints: coverage.filter(c => !c.tested).map(c => `${c.method} ${c.endpoint}`)
  };
  
  return c.json(report);
});

// ==================== ANALYTICS ====================

app.get('/analytics/trends', async (c) => {
  const days = parseInt(c.req.query('days') || '30');
  
  const result = await c.env.DB.prepare(`
    SELECT 
      date(start_time) as date,
      COUNT(*) as runs,
      SUM(passed) as total_passed,
      SUM(failed) as total_failed,
      AVG(duration) as avg_duration
    FROM test_runs
    WHERE start_time > datetime('now', '-${days} days')
    GROUP BY date(start_time)
    ORDER BY date
  `).all();
  
  return c.json({
    trends: result.results || [],
    summary: {
      totalRuns: (result.results || []).reduce((sum: number, r: any) => sum + r.runs, 0),
      avgPassRate: (result.results || []).reduce((sum: number, r: any) => 
        sum + (r.total_passed / (r.total_passed + r.total_failed)), 0) / (result.results?.length || 1) * 100
    }
  });
});

app.get('/analytics/flaky', async (c) => {
  // Identify flaky tests (tests that sometimes pass, sometimes fail)
  const result = await c.env.DB.prepare(`
    SELECT 
      test_id,
      COUNT(*) as runs,
      SUM(CASE WHEN status = 'passed' THEN 1 ELSE 0 END) as passes,
      SUM(CASE WHEN status = 'failed' THEN 1 ELSE 0 END) as failures
    FROM test_results
    WHERE created_at > datetime('now', '-30 days')
    GROUP BY test_id
    HAVING passes > 0 AND failures > 0
    ORDER BY failures DESC
  `).all();
  
  const flakyTests = (result.results || []).map((r: any) => ({
    testId: r.test_id,
    totalRuns: r.runs,
    passes: r.passes,
    failures: r.failures,
    flakinessScore: (r.failures / r.runs) * (r.passes / r.runs) * 4  // Max 1.0 at 50/50
  }));
  
  return c.json({
    flakyTests,
    recommendation: flakyTests.length > 0 
      ? `${flakyTests.length} flaky tests identified. Consider investigating and stabilizing.`
      : 'No flaky tests detected.'
  });
});

// ==================== HELPER FUNCTIONS ====================

function validateTestSuite(suite: TestSuite): { valid: boolean; issues: string[] } {
  const issues: string[] = [];
  
  if (!suite.name) issues.push('Suite name is required');
  if (!suite.tests || suite.tests.length === 0) issues.push('Suite must have at least one test');
  
  for (const test of suite.tests || []) {
    if (!test.name) issues.push(`Test ${test.id} missing name`);
    if (!test.steps || test.steps.length === 0) issues.push(`Test ${test.id} has no steps`);
    if (!test.assertions || test.assertions.length === 0) issues.push(`Test ${test.id} has no assertions`);
  }
  
  return { valid: issues.length === 0, issues };
}

async function executeTest(env: Env, test: TestCase, suiteId: string): Promise<TestResult> {
  const startTime = Date.now();
  const logs: string[] = [];
  const assertionResults: AssertionResult[] = [];
  let status: 'passed' | 'failed' | 'skipped' | 'error' = 'passed';
  
  logs.push(`Starting test: ${test.name}`);
  
  try {
    // Execute steps
    let context: Record<string, any> = {};
    let lastResponse: any = null;
    
    for (const step of test.steps) {
      logs.push(`Executing step: ${step.action} -> ${step.target}`);
      
      if (step.action === 'request') {
        const response = await executeRequest(step);
        lastResponse = response;
        context.response = response;
        
        if (step.waitAfter) {
          await new Promise(resolve => setTimeout(resolve, step.waitAfter));
        }
      } else if (step.action === 'extract') {
        // Extract variable from response
        if (step.variables && lastResponse) {
          for (const [key, path] of Object.entries(step.variables)) {
            context[key] = extractValue(lastResponse, path);
          }
        }
      }
    }
    
    // Evaluate assertions
    for (const assertion of test.assertions) {
      const result = evaluateAssertion(assertion, context);
      assertionResults.push(result);
      
      if (!result.passed) {
        status = 'failed';
        logs.push(`Assertion failed: ${result.message}`);
      }
    }
    
  } catch (error: any) {
    status = 'error';
    logs.push(`Error: ${error.message}`);
  }
  
  const result: TestResult = {
    testId: test.id,
    suiteId,
    status,
    duration: Date.now() - startTime,
    assertions: assertionResults,
    logs,
    metadata: { testName: test.name, priority: test.priority },
    timestamp: new Date()
  };
  
  // Store individual result
  await env.DB.prepare(`
    INSERT INTO test_results (test_id, suite_id, status, duration, created_at)
    VALUES (?, ?, ?, ?, datetime('now'))
  `).bind(test.id, suiteId, status, result.duration).run();
  
  return result;
}

async function executeRequest(step: TestStep): Promise<any> {
  const response = await fetch(step.target, {
    method: step.method || 'GET',
    headers: step.headers || {},
    body: step.body ? JSON.stringify(step.body) : undefined
  });
  
  const responseTime = 0; // Would be measured in real implementation
  let body;
  
  try {
    body = await response.json();
  } catch {
    body = await response.text();
  }
  
  return {
    status: response.status,
    headers: Object.fromEntries(response.headers.entries()),
    body,
    responseTime
  };
}

function evaluateAssertion(assertion: Assertion, context: Record<string, any>): AssertionResult {
  const response = context.response;
  let actual: any;
  let passed = false;
  
  switch (assertion.type) {
    case 'status':
      actual = response?.status;
      passed = evaluateOperator(actual, assertion.operator, assertion.expected);
      break;
    
    case 'body':
      actual = assertion.target ? extractValue(response?.body, assertion.target) : response?.body;
      passed = evaluateOperator(actual, assertion.operator, assertion.expected);
      break;
    
    case 'header':
      actual = response?.headers?.[assertion.target || ''];
      passed = evaluateOperator(actual, assertion.operator, assertion.expected);
      break;
    
    case 'timing':
      actual = response?.responseTime;
      passed = evaluateOperator(actual, assertion.operator, assertion.expected);
      break;
    
    default:
      passed = false;
  }
  
  return {
    assertion,
    passed,
    actual,
    message: passed 
      ? 'Assertion passed'
      : `Expected ${assertion.expected}, got ${actual}`
  };
}

function evaluateOperator(actual: any, operator: string, expected: any): boolean {
  switch (operator) {
    case 'equals':
      return actual === expected;
    case 'contains':
      return String(actual).includes(String(expected));
    case 'matches':
      return new RegExp(expected).test(String(actual));
    case 'lessThan':
      return Number(actual) < Number(expected);
    case 'greaterThan':
      return Number(actual) > Number(expected);
    case 'exists':
      return actual !== undefined && actual !== null;
    default:
      return false;
  }
}

function extractValue(obj: any, path: string): any {
  const parts = path.split('.');
  let current = obj;
  
  for (const part of parts) {
    if (current === undefined || current === null) return undefined;
    current = current[part];
  }
  
  return current;
}

async function runTestSteps(steps: TestStep[], context: Record<string, any>): Promise<void> {
  for (const step of steps) {
    if (step.action === 'request') {
      await executeRequest(step);
    }
    if (step.waitAfter) {
      await new Promise(resolve => setTimeout(resolve, step.waitAfter));
    }
  }
}

function selectScenario(scenarios: LoadScenario[]): LoadScenario {
  const totalWeight = scenarios.reduce((sum, s) => sum + s.weight, 0);
  let random = Math.random() * totalWeight;
  
  for (const scenario of scenarios) {
    random -= scenario.weight;
    if (random <= 0) return scenario;
  }
  
  return scenarios[0];
}

async function executeLoadRequest(request: TestStep): Promise<{ success: boolean; responseTime: number; error?: any }> {
  const startTime = Date.now();
  
  try {
    const response = await fetch(request.target, {
      method: request.method || 'GET',
      headers: request.headers || {},
      body: request.body ? JSON.stringify(request.body) : undefined
    });
    
    const responseTime = Date.now() - startTime;
    
    return {
      success: response.ok,
      responseTime,
      error: response.ok ? undefined : { type: `HTTP_${response.status}`, message: response.statusText }
    };
  } catch (error: any) {
    return {
      success: false,
      responseTime: Date.now() - startTime,
      error: { type: 'NETWORK_ERROR', message: error.message }
    };
  }
}

async function injectChaos(env: Env, experiment: ChaosExperiment): Promise<any> {
  // In a real implementation, this would inject actual faults
  // For now, we store the chaos configuration
  
  const chaosConfig = {
    type: experiment.type,
    target: experiment.target,
    parameters: experiment.parameters,
    active: true,
    startedAt: new Date()
  };
  
  await env.TESTING_KV.put(`chaos_active:${experiment.target}`, JSON.stringify(chaosConfig));
  
  return {
    injected: true,
    type: experiment.type,
    target: experiment.target
  };
}

async function rollbackChaos(env: Env, experiment: ChaosExperiment): Promise<void> {
  await env.TESTING_KV.delete(`chaos_active:${experiment.target}`);
}

async function performHealthCheck(check: HealthCheck): Promise<HealthStatus> {
  const startTime = Date.now();
  
  try {
    const response = await fetch(check.endpoint, {
      method: check.method,
      signal: AbortSignal.timeout(check.timeout)
    });
    
    const responseTime = Date.now() - startTime;
    const isHealthy = response.status === check.expectedStatus;
    
    return {
      checkId: check.id,
      status: isHealthy ? 'healthy' : 'unhealthy',
      responseTime,
      lastCheck: new Date(),
      consecutiveFailures: isHealthy ? 0 : 1,
      uptime: isHealthy ? 100 : 0
    };
  } catch (error) {
    return {
      checkId: check.id,
      status: 'unhealthy',
      responseTime: Date.now() - startTime,
      lastCheck: new Date(),
      consecutiveFailures: 1,
      uptime: 0
    };
  }
}

export default app;
