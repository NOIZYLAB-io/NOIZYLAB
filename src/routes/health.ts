/**
 * NOIZYLAB Email System - Health Routes
 * Health check and status endpoints
 */

import { Hono } from 'hono';
import type { HealthCheckResponse, HealthCheckStatus } from '../types';
import { now } from '../utils';

/**
 * Application version
 */
const VERSION = '1.0.0';

/**
 * Context type with services
 */
interface HealthContext {
  Variables: {
    emailService: import('../services/email-service').EmailService;
    kv: KVNamespace;
    db: D1Database;
    requestId: string;
  };
}

const healthRoutes = new Hono<HealthContext>();

/**
 * GET /health - Simple health check
 */
healthRoutes.get('/', async (c) => {
  return c.json({
    status: 'healthy',
    version: VERSION,
    timestamp: now(),
  });
});

/**
 * GET /health/detailed - Detailed health check with component status
 */
healthRoutes.get('/detailed', async (c) => {
  const emailService = c.get('emailService');
  const kv = c.get('kv');
  const db = c.get('db');

  const checks: HealthCheckResponse['checks'] = {
    database: await checkDatabase(db),
    cache: await checkCache(kv),
    queue: { status: 'pass' }, // Queue health is implicit in Workers
    provider: { status: 'pass' },
  };

  // Check email providers
  const providerHealth = await emailService.healthCheck();
  const healthyProviders = Object.values(providerHealth).filter((h) => h.healthy).length;
  const totalProviders = Object.keys(providerHealth).length;

  if (healthyProviders === 0 && totalProviders > 0) {
    checks.provider = {
      status: 'fail',
      message: 'All email providers are unhealthy',
    };
  } else if (healthyProviders < totalProviders) {
    checks.provider = {
      status: 'warn',
      message: `${healthyProviders}/${totalProviders} providers healthy`,
    };
  }

  // Determine overall status
  const statuses = Object.values(checks).map((c) => c.status);
  let overallStatus: 'healthy' | 'degraded' | 'unhealthy' = 'healthy';

  if (statuses.includes('fail')) {
    overallStatus = 'unhealthy';
  } else if (statuses.includes('warn')) {
    overallStatus = 'degraded';
  }

  const response: HealthCheckResponse = {
    status: overallStatus,
    version: VERSION,
    timestamp: now(),
    checks,
  };

  const statusCode = overallStatus === 'healthy' ? 200 : overallStatus === 'degraded' ? 200 : 503;

  return c.json(response, statusCode);
});

/**
 * GET /health/ready - Readiness probe for Kubernetes-style deployments
 */
healthRoutes.get('/ready', async (c) => {
  const db = c.get('db');
  const kv = c.get('kv');

  const dbCheck = await checkDatabase(db);
  const cacheCheck = await checkCache(kv);

  const ready = dbCheck.status !== 'fail' && cacheCheck.status !== 'fail';

  return c.json(
    {
      ready,
      timestamp: now(),
    },
    ready ? 200 : 503
  );
});

/**
 * GET /health/live - Liveness probe
 */
healthRoutes.get('/live', async (c) => {
  return c.json({
    live: true,
    timestamp: now(),
  });
});

/**
 * Check database connectivity
 */
async function checkDatabase(db: D1Database): Promise<HealthCheckStatus> {
  const startTime = Date.now();

  try {
    await db.prepare('SELECT 1').first();

    return {
      status: 'pass',
      latencyMs: Date.now() - startTime,
    };
  } catch (error) {
    return {
      status: 'fail',
      latencyMs: Date.now() - startTime,
      message: error instanceof Error ? error.message : 'Database check failed',
    };
  }
}

/**
 * Check cache (KV) connectivity
 */
async function checkCache(kv: KVNamespace): Promise<HealthCheckStatus> {
  const startTime = Date.now();
  const testKey = '__health_check__';

  try {
    await kv.put(testKey, 'ok', { expirationTtl: 60 });
    const value = await kv.get(testKey);

    if (value !== 'ok') {
      return {
        status: 'warn',
        latencyMs: Date.now() - startTime,
        message: 'Cache read/write mismatch',
      };
    }

    return {
      status: 'pass',
      latencyMs: Date.now() - startTime,
    };
  } catch (error) {
    return {
      status: 'fail',
      latencyMs: Date.now() - startTime,
      message: error instanceof Error ? error.message : 'Cache check failed',
    };
  }
}

export { healthRoutes };
