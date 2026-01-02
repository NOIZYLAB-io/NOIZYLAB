/**
 *  █████╗ ██████╗ ██╗     ██████╗  █████╗ ████████╗███████╗██╗    ██╗ █████╗ ██╗   ██╗
 * ██╔══██╗██╔══██╗██║    ██╔════╝ ██╔══██╗╚══██╔══╝██╔════╝██║    ██║██╔══██╗╚██╗ ██╔╝
 * ███████║██████╔╝██║    ██║  ███╗███████║   ██║   █████╗  ██║ █╗ ██║███████║ ╚████╔╝ 
 * ██╔══██║██╔═══╝ ██║    ██║   ██║██╔══██║   ██║   ██╔══╝  ██║███╗██║██╔══██║  ╚██╔╝  
 * ██║  ██║██║     ██║    ╚██████╔╝██║  ██║   ██║   ███████╗╚███╔███╔╝██║  ██║   ██║   
 * ╚═╝  ╚═╝╚═╝     ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝   
 * 
 * NoizyLab OS - API Gateway
 * Unified API Gateway with auth, rate limiting, and intelligent routing
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';
import { jwt } from 'hono/jwt';

// ═══════════════════════════════════════════════════════════════════════════
// TYPES
// ═══════════════════════════════════════════════════════════════════════════

interface Env {
  NOIZYLAB_KV: KVNamespace;
  NOIZYLAB_DB: D1Database;
  JWT_SECRET: string;
  API_KEY_SALT: string;

  // Service bindings
  MAIN: Fetcher;
  BRAIN: Fetcher;
  VISION: Fetcher;
  VOICE: Fetcher;
  PRICING: Fetcher;
  INVENTORY: Fetcher;
  ANALYTICS: Fetcher;
  NOTIFICATIONS: Fetcher;
  QC_INSPECTOR: Fetcher;
  CUSTOMER_PORTAL: Fetcher;
  SCHEMATIC_ANALYZER: Fetcher;
  AR_GUIDE: Fetcher;
  TRAINING: Fetcher;
  EBAY_SNIPER: Fetcher;
  CHAT_AGENT: Fetcher;
  WORKFLOW_ORCHESTRATOR: Fetcher;
}

interface RateLimitConfig {
  requests: number;
  window: number; // seconds
}

interface ApiKey {
  id: string;
  key: string;
  name: string;
  workspaceId: string;
  scopes: string[];
  rateLimit: RateLimitConfig;
  enabled: boolean;
  lastUsed?: string;
  createdAt: string;
}

interface ServiceRoute {
  path: string;
  service: keyof Env;
  auth: 'none' | 'api_key' | 'jwt' | 'both';
  scopes?: string[];
  rateLimit?: RateLimitConfig;
}

// ═══════════════════════════════════════════════════════════════════════════
// ROUTE CONFIGURATION
// ═══════════════════════════════════════════════════════════════════════════

const ROUTES: ServiceRoute[] = [
  // Main API
  { path: '/api/tickets', service: 'MAIN', auth: 'both', scopes: ['tickets:read', 'tickets:write'] },
  { path: '/api/workspaces', service: 'MAIN', auth: 'jwt', scopes: ['admin'] },
  
  // AI Services
  { path: '/api/brain', service: 'BRAIN', auth: 'api_key', scopes: ['ai:diagnose'] },
  { path: '/api/vision', service: 'VISION', auth: 'api_key', scopes: ['ai:vision'] },
  { path: '/api/voice', service: 'VOICE', auth: 'api_key', scopes: ['ai:voice'] },
  
  // Business Operations
  { path: '/api/pricing', service: 'PRICING', auth: 'both', scopes: ['pricing:read', 'pricing:write'] },
  { path: '/api/inventory', service: 'INVENTORY', auth: 'both', scopes: ['inventory:read', 'inventory:write'] },
  { path: '/api/analytics', service: 'ANALYTICS', auth: 'jwt', scopes: ['analytics:read'] },
  
  // Customer Services
  { path: '/api/customers', service: 'CUSTOMER_PORTAL', auth: 'jwt', scopes: ['customers:read'] },
  { path: '/api/portal', service: 'CUSTOMER_PORTAL', auth: 'none' }, // Customer self-service
  
  // Technical Services
  { path: '/api/schematics', service: 'SCHEMATIC_ANALYZER', auth: 'api_key', scopes: ['schematics:read'] },
  { path: '/api/qc', service: 'QC_INSPECTOR', auth: 'both', scopes: ['qc:read', 'qc:write'] },
  { path: '/api/ar', service: 'AR_GUIDE', auth: 'api_key', scopes: ['ar:access'] },
  { path: '/api/training', service: 'TRAINING', auth: 'jwt', scopes: ['training:access'] },
  
  // Automation
  { path: '/api/workflows', service: 'WORKFLOW_ORCHESTRATOR', auth: 'jwt', scopes: ['workflows:manage'] },
  { path: '/api/notifications', service: 'NOTIFICATIONS', auth: 'both', scopes: ['notifications:send'] },
  { path: '/api/ebay', service: 'EBAY_SNIPER', auth: 'api_key', scopes: ['ebay:search', 'ebay:buy'] },
  
  // Real-time
  { path: '/api/chat', service: 'CHAT_AGENT', auth: 'both', scopes: ['chat:access'] }
];

// ═══════════════════════════════════════════════════════════════════════════
// RATE LIMITER
// ═══════════════════════════════════════════════════════════════════════════

class RateLimiter {
  private kv: KVNamespace;

  constructor(kv: KVNamespace) {
    this.kv = kv;
  }

  async check(key: string, config: RateLimitConfig): Promise<{ allowed: boolean; remaining: number; resetAt: number }> {
    const now = Math.floor(Date.now() / 1000);
    const windowKey = `ratelimit:${key}:${Math.floor(now / config.window)}`;

    const current = await this.kv.get(windowKey);
    const count = current ? parseInt(current) : 0;

    if (count >= config.requests) {
      return {
        allowed: false,
        remaining: 0,
        resetAt: (Math.floor(now / config.window) + 1) * config.window
      };
    }

    await this.kv.put(windowKey, (count + 1).toString(), { expirationTtl: config.window * 2 });

    return {
      allowed: true,
      remaining: config.requests - count - 1,
      resetAt: (Math.floor(now / config.window) + 1) * config.window
    };
  }
}

// ═══════════════════════════════════════════════════════════════════════════
// API KEY VALIDATOR
// ═══════════════════════════════════════════════════════════════════════════

class ApiKeyValidator {
  private db: D1Database;
  private kv: KVNamespace;

  constructor(db: D1Database, kv: KVNamespace) {
    this.db = db;
    this.kv = kv;
  }

  async validate(apiKey: string): Promise<ApiKey | null> {
    // Check cache first
    const cached = await this.kv.get(`apikey:${apiKey}`);
    if (cached) {
      return JSON.parse(cached);
    }

    // Hash the key for lookup
    const encoder = new TextEncoder();
    const data = encoder.encode(apiKey);
    const hashBuffer = await crypto.subtle.digest('SHA-256', data);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    const keyHash = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');

    const row = await this.db.prepare(
      'SELECT * FROM api_keys WHERE key_hash = ? AND enabled = 1'
    ).bind(keyHash).first();

    if (!row) {
      return null;
    }

    const key: ApiKey = {
      id: row.id as string,
      key: apiKey,
      name: row.name as string,
      workspaceId: row.workspace_id as string,
      scopes: JSON.parse(row.scopes as string),
      rateLimit: JSON.parse(row.rate_limit as string),
      enabled: true,
      createdAt: row.created_at as string
    };

    // Cache for 5 minutes
    await this.kv.put(`apikey:${apiKey}`, JSON.stringify(key), { expirationTtl: 300 });

    // Update last used
    await this.db.prepare(
      'UPDATE api_keys SET last_used_at = ? WHERE id = ?'
    ).bind(new Date().toISOString(), key.id).run();

    return key;
  }

  hasScope(key: ApiKey, requiredScopes: string[]): boolean {
    if (key.scopes.includes('*')) return true;
    return requiredScopes.some(scope => 
      key.scopes.includes(scope) || key.scopes.includes(scope.split(':')[0] + ':*')
    );
  }
}

// ═══════════════════════════════════════════════════════════════════════════
// HONO APP
// ═══════════════════════════════════════════════════════════════════════════

const app = new Hono<{ Bindings: Env }>();

app.use('*', cors({
  origin: ['https://noizylab.io', 'https://app.noizylab.io', 'http://localhost:3000'],
  credentials: true
}));

// Health check
app.get('/health', async (c) => {
  const services = [
    'MAIN', 'BRAIN', 'VISION', 'VOICE', 'PRICING', 'INVENTORY',
    'ANALYTICS', 'NOTIFICATIONS', 'QC_INSPECTOR', 'CUSTOMER_PORTAL',
    'SCHEMATIC_ANALYZER', 'AR_GUIDE', 'TRAINING', 'EBAY_SNIPER',
    'CHAT_AGENT', 'WORKFLOW_ORCHESTRATOR'
  ];

  const healthChecks = await Promise.all(
    services.map(async (service) => {
      try {
        const fetcher = c.env[service as keyof Env] as Fetcher;
        const response = await fetcher.fetch('https://internal/health', { method: 'GET' });
        return { service, status: response.ok ? 'healthy' : 'unhealthy', code: response.status };
      } catch (error) {
        return { service, status: 'error', error: String(error) };
      }
    })
  );

  const allHealthy = healthChecks.every(h => h.status === 'healthy');

  return c.json({
    status: allHealthy ? 'healthy' : 'degraded',
    gateway: 'healthy',
    services: healthChecks,
    timestamp: new Date().toISOString()
  }, allHealthy ? 200 : 503);
});

// System status dashboard
app.get('/status', async (c) => {
  return c.json({
    system: 'NoizyLab OS',
    version: '1.0.0',
    environment: 'production',
    workers: {
      total: 16,
      services: [
        { name: 'Main API', worker: 'noizylab-main', description: 'Core ticket and workspace management' },
        { name: 'Brain AI', worker: 'noizylab-brain', description: 'Claude-powered diagnostic engine' },
        { name: 'Vision AI', worker: 'noizylab-vision', description: 'PCB analysis and golden reference comparison' },
        { name: 'Voice AI', worker: 'noizylab-voice', description: 'ElevenLabs text-to-speech' },
        { name: 'Pricing Engine', worker: 'noizylab-pricing', description: 'Smart quote generation' },
        { name: 'Inventory', worker: 'noizylab-inventory', description: 'Parts tracking with ML predictions' },
        { name: 'Analytics', worker: 'noizylab-analytics', description: 'Business intelligence dashboard' },
        { name: 'Notifications', worker: 'noizylab-notifications', description: 'Multi-channel notification hub' },
        { name: 'QC Inspector', worker: 'noizylab-qc-inspector', description: 'Automated quality control' },
        { name: 'Customer Portal', worker: 'noizylab-customer-portal', description: 'Customer self-service' },
        { name: 'Schematic Analyzer', worker: 'noizylab-schematic-analyzer', description: 'Circuit analysis and fault diagnosis' },
        { name: 'AR Guide', worker: 'noizylab-ar-guide', description: 'Augmented reality repair guides' },
        { name: 'Training', worker: 'noizylab-training', description: 'Gamified technician training' },
        { name: 'eBay Sniper', worker: 'noizylab-ebay-sniper', description: 'Parts deal hunting' },
        { name: 'Chat Agent', worker: 'noizylab-chat-agent', description: 'Real-time AI assistant' },
        { name: 'Workflow Orchestrator', worker: 'noizylab-workflow-orchestrator', description: 'Automation engine' }
      ]
    },
    infrastructure: {
      database: 'Cloudflare D1',
      storage: 'Cloudflare R2',
      cache: 'Cloudflare KV',
      queue: 'Cloudflare Queues',
      ai: 'Claude 3.5 Opus + Workers AI'
    },
    capabilities: [
      'AI-powered diagnostics with extended thinking',
      'Computer vision PCB analysis',
      'Real-time voice synthesis',
      'Predictive inventory management',
      'Automated parts sourcing',
      'Multi-channel notifications',
      'Augmented reality repair guides',
      'Gamified training system',
      'Customer self-service portal',
      'Schematic analysis and circuit tracing',
      'Quality control automation',
      'Workflow orchestration'
    ]
  });
});

// API documentation
app.get('/docs', (c) => {
  return c.json({
    openapi: '3.0.0',
    info: {
      title: 'NoizyLab OS API',
      version: '1.0.0',
      description: 'Omni-Sovereign AI-Powered Hardware Restoration Platform'
    },
    servers: [
      { url: 'https://api.noizylab.io', description: 'Production' },
      { url: 'https://api-staging.noizylab.io', description: 'Staging' }
    ],
    paths: Object.fromEntries(
      ROUTES.map(route => [
        route.path,
        {
          get: {
            summary: `Access ${route.service} service`,
            security: route.auth !== 'none' ? [
              route.auth === 'api_key' ? { apiKey: [] } :
              route.auth === 'jwt' ? { bearerAuth: [] } :
              [{ apiKey: [] }, { bearerAuth: [] }]
            ] : undefined,
            responses: {
              200: { description: 'Success' },
              401: { description: 'Unauthorized' },
              429: { description: 'Rate limit exceeded' }
            }
          }
        }
      ])
    ),
    components: {
      securitySchemes: {
        apiKey: {
          type: 'apiKey',
          in: 'header',
          name: 'X-API-Key'
        },
        bearerAuth: {
          type: 'http',
          scheme: 'bearer',
          bearerFormat: 'JWT'
        }
      }
    }
  });
});

// Request logging middleware
app.use('*', async (c, next) => {
  const start = Date.now();
  const requestId = crypto.randomUUID();
  c.header('X-Request-ID', requestId);

  await next();

  const duration = Date.now() - start;
  
  // Log request (would send to analytics in production)
  console.log(JSON.stringify({
    requestId,
    method: c.req.method,
    path: c.req.path,
    status: c.res.status,
    duration,
    timestamp: new Date().toISOString()
  }));
});

// Rate limiting and auth middleware
app.use('/api/*', async (c, next) => {
  const path = c.req.path;
  const route = ROUTES.find(r => path.startsWith(r.path));

  if (!route) {
    return c.json({ error: 'Route not found' }, 404);
  }

  const rateLimiter = new RateLimiter(c.env.NOIZYLAB_KV);
  const apiKeyValidator = new ApiKeyValidator(c.env.NOIZYLAB_DB, c.env.NOIZYLAB_KV);

  // Check authentication
  if (route.auth !== 'none') {
    const apiKeyHeader = c.req.header('X-API-Key');
    const authHeader = c.req.header('Authorization');

    let authenticated = false;
    let rateLimitKey = '';
    let rateLimitConfig: RateLimitConfig = route.rateLimit || { requests: 100, window: 60 };

    // API Key auth
    if (apiKeyHeader && (route.auth === 'api_key' || route.auth === 'both')) {
      const apiKey = await apiKeyValidator.validate(apiKeyHeader);
      if (apiKey) {
        if (route.scopes && !apiKeyValidator.hasScope(apiKey, route.scopes)) {
          return c.json({ error: 'Insufficient permissions' }, 403);
        }
        authenticated = true;
        rateLimitKey = `key:${apiKey.id}`;
        rateLimitConfig = apiKey.rateLimit;
        c.set('apiKey', apiKey);
      }
    }

    // JWT auth
    if (authHeader?.startsWith('Bearer ') && (route.auth === 'jwt' || route.auth === 'both')) {
      try {
        const token = authHeader.replace('Bearer ', '');
        const { verify } = await import('hono/jwt');
        const payload = await verify(token, c.env.JWT_SECRET);
        authenticated = true;
        rateLimitKey = `user:${payload.sub}`;
        c.set('user', payload);
      } catch {
        // JWT invalid
      }
    }

    if (!authenticated) {
      return c.json({ error: 'Unauthorized' }, 401);
    }

    // Rate limiting
    const rateCheck = await rateLimiter.check(rateLimitKey, rateLimitConfig);
    c.header('X-RateLimit-Limit', rateLimitConfig.requests.toString());
    c.header('X-RateLimit-Remaining', rateCheck.remaining.toString());
    c.header('X-RateLimit-Reset', rateCheck.resetAt.toString());

    if (!rateCheck.allowed) {
      return c.json({ error: 'Rate limit exceeded' }, 429);
    }
  }

  await next();
});

// Route to services
app.all('/api/*', async (c) => {
  const path = c.req.path;
  const route = ROUTES.find(r => path.startsWith(r.path));

  if (!route) {
    return c.json({ error: 'Route not found' }, 404);
  }

  const service = c.env[route.service] as Fetcher;
  const subPath = path.replace(route.path, '') || '/';

  // Forward request to service
  const url = new URL(c.req.url);
  const targetUrl = `https://internal${subPath}${url.search}`;

  const headers = new Headers(c.req.raw.headers);
  headers.delete('host');
  
  // Add context headers
  const user = c.get('user');
  const apiKey = c.get('apiKey');
  if (user) headers.set('X-User-ID', user.sub);
  if (apiKey) headers.set('X-Workspace-ID', apiKey.workspaceId);

  try {
    const response = await service.fetch(targetUrl, {
      method: c.req.method,
      headers,
      body: c.req.method !== 'GET' && c.req.method !== 'HEAD' ? c.req.raw.body : undefined
    });

    // Forward response
    const responseHeaders = new Headers(response.headers);
    return new Response(response.body, {
      status: response.status,
      headers: responseHeaders
    });

  } catch (error) {
    console.error(`Service error (${route.service}):`, error);
    return c.json({ error: 'Service unavailable' }, 503);
  }
});

// API Key management
app.post('/keys', async (c) => {
  // This would be protected by admin auth
  const { name, workspaceId, scopes, rateLimit } = await c.req.json();

  const apiKey = `nlab_${crypto.randomUUID().replace(/-/g, '')}`;
  
  // Hash for storage
  const encoder = new TextEncoder();
  const data = encoder.encode(apiKey);
  const hashBuffer = await crypto.subtle.digest('SHA-256', data);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  const keyHash = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');

  const keyId = `key_${Date.now()}_${Math.random().toString(36).substring(7)}`;

  await c.env.NOIZYLAB_DB.prepare(`
    INSERT INTO api_keys (id, key_hash, name, workspace_id, scopes, rate_limit, enabled, created_at)
    VALUES (?, ?, ?, ?, ?, ?, 1, ?)
  `).bind(
    keyId,
    keyHash,
    name,
    workspaceId,
    JSON.stringify(scopes || ['*']),
    JSON.stringify(rateLimit || { requests: 1000, window: 60 }),
    new Date().toISOString()
  ).run();

  // Only return the key once
  return c.json({
    id: keyId,
    key: apiKey, // Only shown once!
    name,
    scopes: scopes || ['*'],
    rateLimit: rateLimit || { requests: 1000, window: 60 },
    message: 'Store this key securely - it will not be shown again'
  }, 201);
});

// Webhooks endpoint
app.post('/webhooks/:source', async (c) => {
  const source = c.req.param('source');
  const body = await c.req.text();
  const signature = c.req.header('X-Signature') || c.req.header('Stripe-Signature') || '';

  // Route to appropriate handler
  switch (source) {
    case 'stripe':
      return c.env.CUSTOMER_PORTAL.fetch('https://internal/webhooks/stripe', {
        method: 'POST',
        headers: { 'Stripe-Signature': signature, 'Content-Type': 'application/json' },
        body
      });

    case 'ebay':
      return c.env.EBAY_SNIPER.fetch('https://internal/webhooks/ebay', {
        method: 'POST',
        body
      });

    default:
      // Forward to workflow orchestrator for custom webhooks
      return c.env.WORKFLOW_ORCHESTRATOR.fetch('https://internal/webhooks', {
        method: 'POST',
        headers: { 'X-Webhook-Source': source },
        body
      });
  }
});

export default app;
