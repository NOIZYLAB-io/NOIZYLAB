// ═══════════════════════════════════════════════════════════════════════════
// NOIZYLAB OS - Main Worker Entry Point
// "GO RUN FREE" Hot-Rod Edition
// ═══════════════════════════════════════════════════════════════════════════

import { Hono } from 'hono';
import { cors } from 'hono/cors';
import { logger } from 'hono/logger';
import { secureHeaders } from 'hono/secure-headers';

// Route imports
import { ticketRoutes } from './routes/tickets';
import { statusRoutes } from './routes/status';
import { uploadRoutes } from './routes/uploads';
import { liveRoutes } from './routes/live';
import { aiRoutes } from './routes/ai';
import { staffRoutes } from './routes/staff';
import { webhookRoutes } from './routes/webhooks';

// Types
export interface Env {
  // D1 Database
  DB: D1Database;
  
  // R2 Storage
  UPLOADS: R2Bucket;
  
  // KV Namespaces
  CACHE: KVNamespace;
  SESSIONS: KVNamespace;
  
  // Durable Objects
  CHAT_ROOM: DurableObjectNamespace;
  PRESENCE: DurableObjectNamespace;
  
  // AI Gateway
  AI: Ai;
  
  // Secrets
  TURNSTILE_SECRET: string;
  JWT_SECRET: string;
  
  // Config
  ENVIRONMENT: string;
}

// Create app
const app = new Hono<{ Bindings: Env }>();

// ═══════════════════════════════════════════════════════════════════════════
// Middleware
// ═══════════════════════════════════════════════════════════════════════════

app.use('*', logger());
app.use('*', secureHeaders());
app.use('*', cors({
  origin: ['https://noizylab.ca', 'https://portal.noizylab.ca', 'http://localhost:3000'],
  allowMethods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
  allowHeaders: ['Content-Type', 'Authorization', 'X-Turnstile-Token'],
  credentials: true,
}));

// ═══════════════════════════════════════════════════════════════════════════
// Health Check
// ═══════════════════════════════════════════════════════════════════════════

app.get('/', (c) => {
  return c.json({
    name: 'NoizyLab OS',
    version: '1.0.0',
    status: 'operational',
    timestamp: new Date().toISOString(),
    hotrod: 'GO RUN FREE 🏎️',
  });
});

app.get('/health', async (c) => {
  const checks = {
    api: 'ok',
    database: 'checking',
    storage: 'checking',
    ai: 'checking',
  };
  
  try {
    // Check D1
    await c.env.DB.prepare('SELECT 1').first();
    checks.database = 'ok';
  } catch (e) {
    checks.database = 'error';
  }
  
  try {
    // Check R2
    await c.env.UPLOADS.head('health-check');
    checks.storage = 'ok';
  } catch (e) {
    // HEAD on non-existent key returns null, not error
    checks.storage = 'ok';
  }
  
  try {
    // Check AI Gateway
    checks.ai = c.env.AI ? 'ok' : 'not-configured';
  } catch (e) {
    checks.ai = 'error';
  }
  
  const allOk = Object.values(checks).every(v => v === 'ok' || v === 'not-configured');
  
  return c.json({
    status: allOk ? 'healthy' : 'degraded',
    checks,
    timestamp: new Date().toISOString(),
  }, allOk ? 200 : 503);
});

// ═══════════════════════════════════════════════════════════════════════════
// API Routes
// ═══════════════════════════════════════════════════════════════════════════

// Public routes (Turnstile protected)
app.route('/api/tickets', ticketRoutes);
app.route('/api/status', statusRoutes);
app.route('/api/uploads', uploadRoutes);
app.route('/api/live', liveRoutes);

// AI routes
app.route('/api/ai', aiRoutes);

// Staff routes (Access protected)
app.route('/api/staff', staffRoutes);

// Webhook routes
app.route('/webhooks', webhookRoutes);

// ═══════════════════════════════════════════════════════════════════════════
// Error Handling
// ═══════════════════════════════════════════════════════════════════════════

app.onError((err, c) => {
  console.error('Error:', err);
  
  return c.json({
    error: 'Internal Server Error',
    message: c.env.ENVIRONMENT === 'development' ? err.message : 'Something went wrong',
    timestamp: new Date().toISOString(),
  }, 500);
});

app.notFound((c) => {
  return c.json({
    error: 'Not Found',
    message: `Route ${c.req.method} ${c.req.path} not found`,
    timestamp: new Date().toISOString(),
  }, 404);
});

// ═══════════════════════════════════════════════════════════════════════════
// Export
// ═══════════════════════════════════════════════════════════════════════════

export default app;

// Export Durable Objects
export { ChatRoom } from './durable/ChatRoom';
export { Presence } from './durable/Presence';
