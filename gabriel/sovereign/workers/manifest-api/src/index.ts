/**
 * NOIZYLAB SOVEREIGN MANIFEST API
 * ================================
 * Cloudflare Worker for Success Manifest operations.
 * Money while you sleep. GORUNFREE.
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';
import { bearerAuth } from 'hono/bearer-auth';

// Types
interface Env {
  DB: D1Database;
  MANIFESTS: R2Bucket;
  KV_CACHE: KVNamespace;
  STRIPE_SECRET: string;
  SENDGRID_API_KEY: string;
  JWT_SECRET: string;
}

interface ManifestData {
  caseId: string;
  ticketId: string;
  customerName: string;
  customerEmail: string;
  deviceType: string;
  deviceModel: string;
  serialNumber?: string;
  diagnosis: string;
  rootCause: string;
  componentsAffected: string[];
  repairTechnique: string;
  solderPoints: number;
  voltageReadings: Record<string, number>;
  biometrics: {
    avgStability: number;
    auraMatchScore: number;
    jitterCompensated: number;
    sessionDuration: number;
  };
  forensicImages: {
    preRepair: string;
    postRepair: string;
    componentId: string;
  }[];
  verificationHash: string;
  totalPrice: number;
  createdAt: string;
  completedAt: string;
}

interface InvoiceRequest {
  manifestId: string;
  customerEmail: string;
  amount: number;
  description: string;
}

// Initialize Hono app
const app = new Hono<{ Bindings: Env }>();

// Middleware
app.use('*', cors({
  origin: ['https://portal.noizylab.ca', 'https://noizylab.ca', 'http://localhost:3000'],
  credentials: true,
}));

// =============================================================================
// MANIFEST ENDPOINTS
// =============================================================================

/**
 * Create new manifest
 * POST /api/manifests
 */
app.post('/api/manifests', async (c) => {
  const env = c.env;
  const data: ManifestData = await c.req.json();

  // Validate required fields
  if (!data.caseId || !data.ticketId || !data.customerEmail) {
    return c.json({ error: 'Missing required fields' }, 400);
  }

  // Generate verification hash if not provided
  if (!data.verificationHash) {
    data.verificationHash = await generateVerificationHash(data);
  }

  const now = new Date().toISOString();
  data.createdAt = data.createdAt || now;
  data.completedAt = data.completedAt || now;

  // Store in D1 database
  await env.DB.prepare(`
    INSERT INTO manifests (
      case_id, ticket_id, customer_name, customer_email,
      device_type, device_model, serial_number,
      diagnosis, root_cause, components_affected,
      repair_technique, solder_points,
      voltage_readings, biometrics, forensic_images,
      verification_hash, total_price,
      created_at, completed_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
  `).bind(
    data.caseId,
    data.ticketId,
    data.customerName,
    data.customerEmail,
    data.deviceType,
    data.deviceModel,
    data.serialNumber || null,
    data.diagnosis,
    data.rootCause,
    JSON.stringify(data.componentsAffected),
    data.repairTechnique,
    data.solderPoints,
    JSON.stringify(data.voltageReadings),
    JSON.stringify(data.biometrics),
    JSON.stringify(data.forensicImages),
    data.verificationHash,
    data.totalPrice,
    data.createdAt,
    data.completedAt
  ).run();

  // Store JSON manifest in R2
  await env.MANIFESTS.put(
    `manifests/${data.caseId}/data.json`,
    JSON.stringify(data),
    { httpMetadata: { contentType: 'application/json' } }
  );

  // Cache in KV for fast retrieval
  await env.KV_CACHE.put(
    `manifest:${data.caseId}`,
    JSON.stringify(data),
    { expirationTtl: 86400 * 30 } // 30 days
  );

  return c.json({
    success: true,
    caseId: data.caseId,
    verificationHash: data.verificationHash,
    portalUrl: `https://portal.noizylab.ca/manifests/${data.caseId}`
  });
});

/**
 * Get manifest by case ID
 * GET /api/manifests/:caseId
 */
app.get('/api/manifests/:caseId', async (c) => {
  const env = c.env;
  const caseId = c.req.param('caseId');

  // Try KV cache first
  const cached = await env.KV_CACHE.get(`manifest:${caseId}`);
  if (cached) {
    return c.json(JSON.parse(cached));
  }

  // Fall back to R2
  const r2Object = await env.MANIFESTS.get(`manifests/${caseId}/data.json`);
  if (r2Object) {
    const data = await r2Object.text();
    // Refresh cache
    await env.KV_CACHE.put(`manifest:${caseId}`, data, { expirationTtl: 86400 * 30 });
    return c.json(JSON.parse(data));
  }

  return c.json({ error: 'Manifest not found' }, 404);
});

/**
 * Verify manifest authenticity
 * GET /api/manifests/:caseId/verify
 */
app.get('/api/manifests/:caseId/verify', async (c) => {
  const env = c.env;
  const caseId = c.req.param('caseId');
  const providedHash = c.req.query('hash');

  const result = await env.DB.prepare(
    'SELECT verification_hash, created_at, customer_name, device_type, device_model FROM manifests WHERE case_id = ?'
  ).bind(caseId).first();

  if (!result) {
    return c.json({ verified: false, error: 'Manifest not found' }, 404);
  }

  const verified = providedHash ? result.verification_hash === providedHash : true;

  return c.json({
    verified,
    caseId,
    createdAt: result.created_at,
    device: `${result.device_type} ${result.device_model}`,
    customer: result.customer_name,
    signature: 'M2_ULTRA_GOD_NODE'
  });
});

/**
 * Upload forensic image
 * POST /api/manifests/:caseId/images
 */
app.post('/api/manifests/:caseId/images', async (c) => {
  const env = c.env;
  const caseId = c.req.param('caseId');

  const formData = await c.req.formData();
  const image = formData.get('image') as File;
  const imageType = formData.get('type') as string; // 'pre' or 'post'
  const componentId = formData.get('componentId') as string;

  if (!image) {
    return c.json({ error: 'No image provided' }, 400);
  }

  const imageBuffer = await image.arrayBuffer();
  const imageName = `${imageType}_${componentId || 'board'}_${Date.now()}.jpg`;
  const imagePath = `manifests/${caseId}/images/${imageName}`;

  await env.MANIFESTS.put(imagePath, imageBuffer, {
    httpMetadata: { contentType: image.type || 'image/jpeg' }
  });

  const imageUrl = `https://r2.noizylab.ca/${imagePath}`;

  return c.json({
    success: true,
    imagePath,
    imageUrl
  });
});

/**
 * Generate PDF manifest
 * GET /api/manifests/:caseId/pdf
 */
app.get('/api/manifests/:caseId/pdf', async (c) => {
  const env = c.env;
  const caseId = c.req.param('caseId');

  // Check for pre-generated PDF
  const pdfObject = await env.MANIFESTS.get(`manifests/${caseId}/manifest.pdf`);

  if (pdfObject) {
    return new Response(pdfObject.body, {
      headers: {
        'Content-Type': 'application/pdf',
        'Content-Disposition': `attachment; filename="MANIFEST_${caseId}.pdf"`
      }
    });
  }

  // PDF not found - would trigger generation via external service
  return c.json({
    error: 'PDF not yet generated',
    generateUrl: `/api/manifests/${caseId}/generate-pdf`
  }, 404);
});

/**
 * List manifests with filters
 * GET /api/manifests
 */
app.get('/api/manifests', async (c) => {
  const env = c.env;
  const email = c.req.query('email');
  const limit = parseInt(c.req.query('limit') || '20');
  const offset = parseInt(c.req.query('offset') || '0');

  let query = 'SELECT * FROM manifests';
  const params: any[] = [];

  if (email) {
    query += ' WHERE customer_email = ?';
    params.push(email);
  }

  query += ' ORDER BY created_at DESC LIMIT ? OFFSET ?';
  params.push(limit, offset);

  const results = await env.DB.prepare(query).bind(...params).all();

  return c.json({
    manifests: results.results,
    count: results.results?.length || 0,
    limit,
    offset
  });
});

// =============================================================================
// BILLING ENDPOINTS
// =============================================================================

/**
 * Create Stripe invoice for manifest
 * POST /api/billing/invoice
 */
app.post('/api/billing/invoice', async (c) => {
  const env = c.env;
  const { manifestId, customerEmail, amount, description }: InvoiceRequest = await c.req.json();

  // Create Stripe invoice via their API
  const stripeResponse = await fetch('https://api.stripe.com/v1/invoices', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${env.STRIPE_SECRET}`,
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: new URLSearchParams({
      'customer_email': customerEmail,
      'collection_method': 'send_invoice',
      'days_until_due': '7',
      'metadata[manifest_id]': manifestId,
    }).toString()
  });

  if (!stripeResponse.ok) {
    const error = await stripeResponse.text();
    return c.json({ error: 'Failed to create invoice', details: error }, 500);
  }

  const invoice = await stripeResponse.json();

  // Add line item
  await fetch('https://api.stripe.com/v1/invoiceitems', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${env.STRIPE_SECRET}`,
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: new URLSearchParams({
      'invoice': invoice.id,
      'amount': Math.round(amount * 100).toString(), // Stripe uses cents
      'currency': 'cad',
      'description': description,
    }).toString()
  });

  // Finalize and send invoice
  await fetch(`https://api.stripe.com/v1/invoices/${invoice.id}/finalize`, {
    method: 'POST',
    headers: { 'Authorization': `Bearer ${env.STRIPE_SECRET}` }
  });

  await fetch(`https://api.stripe.com/v1/invoices/${invoice.id}/send`, {
    method: 'POST',
    headers: { 'Authorization': `Bearer ${env.STRIPE_SECRET}` }
  });

  // Update manifest with invoice ID
  await env.DB.prepare(
    'UPDATE manifests SET stripe_invoice_id = ? WHERE case_id = ?'
  ).bind(invoice.id, manifestId).run();

  return c.json({
    success: true,
    invoiceId: invoice.id,
    invoiceUrl: invoice.hosted_invoice_url
  });
});

/**
 * Stripe webhook handler
 * POST /api/billing/webhook
 */
app.post('/api/billing/webhook', async (c) => {
  const env = c.env;
  const payload = await c.req.text();
  const signature = c.req.header('stripe-signature');

  // In production: verify webhook signature

  const event = JSON.parse(payload);

  if (event.type === 'invoice.paid') {
    const invoice = event.data.object;
    const manifestId = invoice.metadata?.manifest_id;

    if (manifestId) {
      await env.DB.prepare(
        'UPDATE manifests SET paid = 1, paid_at = ? WHERE case_id = ?'
      ).bind(new Date().toISOString(), manifestId).run();

      // Trigger post-payment automation
      await sendPaymentConfirmation(env, manifestId);
    }
  }

  return c.json({ received: true });
});

// =============================================================================
// NOTIFICATION ENDPOINTS
// =============================================================================

/**
 * Send completion email with manifest
 * POST /api/notifications/completion
 */
app.post('/api/notifications/completion', async (c) => {
  const env = c.env;
  const { caseId, customerEmail, customerName } = await c.req.json();

  // Get manifest data
  const manifest = await env.KV_CACHE.get(`manifest:${caseId}`);
  if (!manifest) {
    return c.json({ error: 'Manifest not found' }, 404);
  }

  const data = JSON.parse(manifest);

  // Send via SendGrid
  const emailResponse = await fetch('https://api.sendgrid.com/v3/mail/send', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${env.SENDGRID_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      personalizations: [{
        to: [{ email: customerEmail, name: customerName }],
        dynamic_template_data: {
          customer_name: customerName,
          device: `${data.deviceType} ${data.deviceModel}`,
          ticket_id: data.ticketId,
          case_id: caseId,
          total_price: `$${data.totalPrice.toFixed(2)}`,
          portal_url: `https://portal.noizylab.ca/manifests/${caseId}`,
          invoice_url: `https://portal.noizylab.ca/pay/${caseId}`
        }
      }],
      from: { email: 'repairs@noizylab.ca', name: 'NOIZYLAB Sovereign Repairs' },
      template_id: 'd-sovereign-repair-complete' // Your SendGrid template
    })
  });

  if (!emailResponse.ok) {
    return c.json({ error: 'Failed to send email' }, 500);
  }

  return c.json({ success: true, sentTo: customerEmail });
});

// =============================================================================
// ANALYTICS ENDPOINTS
// =============================================================================

/**
 * Get repair statistics
 * GET /api/analytics/stats
 */
app.get('/api/analytics/stats', async (c) => {
  const env = c.env;
  const period = c.req.query('period') || '30'; // days

  const stats = await env.DB.prepare(`
    SELECT
      COUNT(*) as total_repairs,
      SUM(total_price) as total_revenue,
      AVG(total_price) as avg_repair_value,
      COUNT(CASE WHEN paid = 1 THEN 1 END) as paid_count,
      SUM(CASE WHEN paid = 1 THEN total_price ELSE 0 END) as collected_revenue
    FROM manifests
    WHERE created_at >= datetime('now', '-${period} days')
  `).first();

  const byDevice = await env.DB.prepare(`
    SELECT device_type, COUNT(*) as count, SUM(total_price) as revenue
    FROM manifests
    WHERE created_at >= datetime('now', '-${period} days')
    GROUP BY device_type
    ORDER BY count DESC
    LIMIT 10
  `).all();

  const byComponent = await env.DB.prepare(`
    SELECT json_each.value as component, COUNT(*) as count
    FROM manifests, json_each(components_affected)
    WHERE created_at >= datetime('now', '-${period} days')
    GROUP BY json_each.value
    ORDER BY count DESC
    LIMIT 10
  `).all();

  return c.json({
    period: `${period} days`,
    overview: stats,
    byDevice: byDevice.results,
    byComponent: byComponent.results,
    projectedMonthly: (stats?.total_revenue || 0) * (30 / parseInt(period)),
    projectedAnnual: (stats?.total_revenue || 0) * (365 / parseInt(period))
  });
});

// =============================================================================
// HELPER FUNCTIONS
// =============================================================================

async function generateVerificationHash(data: ManifestData): Promise<string> {
  const input = `${data.caseId}:${data.ticketId}:${data.serialNumber}:${data.completedAt}`;
  const encoder = new TextEncoder();
  const dataBuffer = encoder.encode(input);
  const hashBuffer = await crypto.subtle.digest('SHA-256', dataBuffer);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  return hashArray.map(b => b.toString(16).padStart(2, '0')).join('').slice(0, 32).toUpperCase();
}

async function sendPaymentConfirmation(env: Env, manifestId: string): Promise<void> {
  // Would trigger email confirmation for payment received
  console.log(`Payment confirmed for manifest: ${manifestId}`);
}

// =============================================================================
// HEALTH CHECK
// =============================================================================

app.get('/health', (c) => {
  return c.json({
    status: 'operational',
    service: 'NOIZYLAB Sovereign Manifest API',
    timestamp: new Date().toISOString(),
    signature: 'GORUNFREE'
  });
});

// 404 handler
app.notFound((c) => {
  return c.json({ error: 'Not found', path: c.req.path }, 404);
});

// Error handler
app.onError((err, c) => {
  console.error('API Error:', err);
  return c.json({ error: 'Internal server error', message: err.message }, 500);
});

export default app;
