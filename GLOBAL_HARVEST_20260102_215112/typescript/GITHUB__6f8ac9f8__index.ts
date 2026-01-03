/**
 * ═══════════════════════════════════════════════════════════════════════════════
 * MC96-NETWORK - Network Orchestrator
 * Service discovery, health monitoring, and cross-worker communication
 * ═══════════════════════════════════════════════════════════════════════════════
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
  KV: KVNamespace;
  ANTIGRAVITY_URL?: string;
  GORUNFREE_URL?: string;
  NOIZYLAB_URL?: string;
}

interface ServiceInfo {
  name: string;
  url: string;
  status: 'healthy' | 'unhealthy' | 'unknown';
  latency?: number;
  lastCheck?: string;
}

// ═══════════════════════════════════════════════════════════════════════════════
// SERVICE REGISTRY
// ═══════════════════════════════════════════════════════════════════════════════

const DEFAULT_SERVICES = {
  antigravity: {
    name: 'ANTIGRAVITY',
    description: 'Command Hub + Circle of 8',
    endpoints: ['/', '/health', '/circle', '/daze', '/ai/chat', '/dashboard']
  },
  gorunfree: {
    name: 'GORUNFREE',
    description: 'Voice Command Processor',
    endpoints: ['/', '/health', '/transcribe', '/process', '/speak']
  },
  noizylab: {
    name: 'NOIZYLAB',
    description: 'Full Repair Service System',
    endpoints: ['/', '/health', '/equipment', '/workorders', '/stats']
  },
  'mc96-network': {
    name: 'MC96-NETWORK',
    description: 'Network Orchestrator',
    endpoints: ['/', '/health', '/services', '/discover', '/relay']
  }
};

// ═══════════════════════════════════════════════════════════════════════════════
// APP SETUP
// ═══════════════════════════════════════════════════════════════════════════════

const app = new Hono<{ Bindings: Env }>();

app.use('*', cors({
  origin: '*',
  allowMethods: ['GET', 'POST', 'OPTIONS'],
  allowHeaders: ['Content-Type', 'Authorization', 'X-MC96-Key']
}));

// ═══════════════════════════════════════════════════════════════════════════════
// ROUTES
// ═══════════════════════════════════════════════════════════════════════════════

app.get('/', (c) => {
  return c.json({
    name: 'MC96-NETWORK',
    version: '1.0.0',
    status: 'operational',
    mission: 'Network Orchestrator - MC96ECOUNIVERSE',
    services: Object.keys(DEFAULT_SERVICES),
    endpoints: [
      '/health',
      '/services',
      '/services/:name',
      '/discover',
      '/relay',
      '/broadcast'
    ]
  });
});

app.get('/health', async (c) => {
  return c.json({
    worker: 'ok',
    timestamp: new Date().toISOString(),
    configured_services: {
      antigravity: !!c.env.ANTIGRAVITY_URL,
      gorunfree: !!c.env.GORUNFREE_URL,
      noizylab: !!c.env.NOIZYLAB_URL
    }
  });
});

// ═══════════════════════════════════════════════════════════════════════════════
// SERVICE DISCOVERY
// ═══════════════════════════════════════════════════════════════════════════════

app.get('/services', async (c) => {
  const services: Record<string, ServiceInfo> = {};

  const serviceUrls: Record<string, string | undefined> = {
    antigravity: c.env.ANTIGRAVITY_URL,
    gorunfree: c.env.GORUNFREE_URL,
    noizylab: c.env.NOIZYLAB_URL
  };

  for (const [key, meta] of Object.entries(DEFAULT_SERVICES)) {
    const url = serviceUrls[key];
    
    if (url) {
      try {
        const start = Date.now();
        const response = await fetch(`${url}/health`, { 
          method: 'GET',
          headers: { 'User-Agent': 'MC96-Network/1.0' }
        });
        const latency = Date.now() - start;

        services[key] = {
          name: meta.name,
          url,
          status: response.ok ? 'healthy' : 'unhealthy',
          latency,
          lastCheck: new Date().toISOString()
        };
      } catch {
        services[key] = {
          name: meta.name,
          url,
          status: 'unhealthy',
          lastCheck: new Date().toISOString()
        };
      }
    } else {
      services[key] = {
        name: meta.name,
        url: 'not_configured',
        status: 'unknown'
      };
    }
  }

  // Cache results
  await c.env.KV.put('services:status', JSON.stringify(services), { expirationTtl: 60 });

  return c.json({
    services,
    total: Object.keys(services).length,
    healthy: Object.values(services).filter(s => s.status === 'healthy').length
  });
});

app.get('/services/:name', async (c) => {
  const name = c.req.param('name').toLowerCase();
  const meta = DEFAULT_SERVICES[name as keyof typeof DEFAULT_SERVICES];

  if (!meta) {
    return c.json({ 
      error: 'Service not found', 
      available: Object.keys(DEFAULT_SERVICES) 
    }, 404);
  }

  const serviceUrls: Record<string, string | undefined> = {
    antigravity: c.env.ANTIGRAVITY_URL,
    gorunfree: c.env.GORUNFREE_URL,
    noizylab: c.env.NOIZYLAB_URL,
    'mc96-network': 'self'
  };

  const url = serviceUrls[name];
  let status: ServiceInfo['status'] = 'unknown';
  let latency: number | undefined;
  let healthData: any = null;

  if (url && url !== 'self') {
    try {
      const start = Date.now();
      const response = await fetch(`${url}/health`);
      latency = Date.now() - start;
      status = response.ok ? 'healthy' : 'unhealthy';
      healthData = await response.json();
    } catch {
      status = 'unhealthy';
    }
  } else if (url === 'self') {
    status = 'healthy';
    latency = 0;
  }

  return c.json({
    ...meta,
    url: url || 'not_configured',
    status,
    latency,
    healthData
  });
});

// ═══════════════════════════════════════════════════════════════════════════════
// DISCOVERY ENDPOINT (for self-registration)
// ═══════════════════════════════════════════════════════════════════════════════

app.post('/discover', async (c) => {
  const body = await c.req.json<{
    name: string;
    url: string;
    endpoints?: string[];
    version?: string;
  }>();

  if (!body.name || !body.url) {
    return c.json({ error: 'name and url required' }, 400);
  }

  const registration = {
    name: body.name,
    url: body.url,
    endpoints: body.endpoints || [],
    version: body.version || '1.0.0',
    registered_at: new Date().toISOString()
  };

  await c.env.KV.put(
    `discovery:${body.name.toLowerCase()}`,
    JSON.stringify(registration),
    { expirationTtl: 3600 } // 1 hour
  );

  return c.json({ success: true, registration });
});

app.get('/discover', async (c) => {
  const list = await c.env.KV.list({ prefix: 'discovery:' });
  const registrations: any[] = [];

  for (const key of list.keys) {
    const data = await c.env.KV.get(key.name);
    if (data) {
      registrations.push(JSON.parse(data));
    }
  }

  return c.json({
    registrations,
    total: registrations.length
  });
});

// ═══════════════════════════════════════════════════════════════════════════════
// RELAY - Proxy requests to other services
// ═══════════════════════════════════════════════════════════════════════════════

app.post('/relay', async (c) => {
  const body = await c.req.json<{
    service: string;
    path: string;
    method?: string;
    body?: any;
    headers?: Record<string, string>;
  }>();

  if (!body.service || !body.path) {
    return c.json({ error: 'service and path required' }, 400);
  }

  const serviceUrls: Record<string, string | undefined> = {
    antigravity: c.env.ANTIGRAVITY_URL,
    gorunfree: c.env.GORUNFREE_URL,
    noizylab: c.env.NOIZYLAB_URL
  };

  const baseUrl = serviceUrls[body.service.toLowerCase()];
  
  if (!baseUrl) {
    return c.json({ 
      error: 'Service not configured',
      available: Object.keys(serviceUrls).filter(k => serviceUrls[k])
    }, 404);
  }

  try {
    const url = `${baseUrl}${body.path}`;
    const response = await fetch(url, {
      method: body.method || 'GET',
      headers: {
        'Content-Type': 'application/json',
        'X-Relayed-By': 'MC96-Network',
        ...body.headers
      },
      body: body.body ? JSON.stringify(body.body) : undefined
    });

    const data = await response.json();

    return c.json({
      relayed: true,
      service: body.service,
      path: body.path,
      status: response.status,
      data
    });
  } catch (error) {
    return c.json({ 
      error: 'Relay failed',
      details: error instanceof Error ? error.message : 'Unknown error'
    }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════════
// BROADCAST - Send message to all services
// ═══════════════════════════════════════════════════════════════════════════════

app.post('/broadcast', async (c) => {
  const body = await c.req.json<{
    message: string;
    type?: string;
    data?: any;
  }>();

  if (!body.message) {
    return c.json({ error: 'message required' }, 400);
  }

  const serviceUrls: Record<string, string | undefined> = {
    antigravity: c.env.ANTIGRAVITY_URL,
    gorunfree: c.env.GORUNFREE_URL,
    noizylab: c.env.NOIZYLAB_URL
  };

  const results: Record<string, any> = {};

  for (const [name, url] of Object.entries(serviceUrls)) {
    if (!url) {
      results[name] = { status: 'skipped', reason: 'not_configured' };
      continue;
    }

    try {
      // Try to POST to a /webhook or /broadcast endpoint if it exists
      const response = await fetch(`${url}/`, {
        method: 'GET',
        headers: { 
          'X-MC96-Broadcast': 'true',
          'X-MC96-Message': body.message
        }
      });

      results[name] = { 
        status: response.ok ? 'delivered' : 'failed',
        httpStatus: response.status
      };
    } catch (error) {
      results[name] = { status: 'failed', error: 'unreachable' };
    }
  }

  // Log broadcast
  const broadcastLog = {
    id: `broadcast-${Date.now()}`,
    message: body.message,
    type: body.type || 'general',
    results,
    timestamp: new Date().toISOString()
  };

  await c.env.KV.put(
    `broadcast:${broadcastLog.id}`,
    JSON.stringify(broadcastLog),
    { expirationTtl: 86400 * 7 } // 7 days
  );

  return c.json(broadcastLog);
});

export default app;
