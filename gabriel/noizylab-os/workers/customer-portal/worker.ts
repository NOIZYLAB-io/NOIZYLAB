/**
 *  ██████╗██╗   ██╗███████╗████████╗ ██████╗ ███╗   ███╗███████╗██████╗ 
 * ██╔════╝██║   ██║██╔════╝╚══██╔══╝██╔═══██╗████╗ ████║██╔════╝██╔══██╗
 * ██║     ██║   ██║███████╗   ██║   ██║   ██║██╔████╔██║█████╗  ██████╔╝
 * ██║     ██║   ██║╚════██║   ██║   ██║   ██║██║╚██╔╝██║██╔══╝  ██╔══██╗
 * ╚██████╗╚██████╔╝███████║   ██║   ╚██████╔╝██║ ╚═╝ ██║███████╗██║  ██║
 *  ╚═════╝ ╚═════╝ ╚══════╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
 *              ██████╗  ██████╗ ██████╗ ████████╗ █████╗ ██╗     
 *              ██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔══██╗██║     
 *              ██████╔╝██║   ██║██████╔╝   ██║   ███████║██║     
 *              ██╔═══╝ ██║   ██║██╔══██╗   ██║   ██╔══██║██║     
 *              ██║     ╚██████╔╝██║  ██║   ██║   ██║  ██║███████╗
 *              ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝
 * 
 * NoizyLab OS - Customer Portal Worker
 * Self-service customer portal with AI assistant, repair tracking, and payments
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';
import { jwt, sign } from 'hono/jwt';

// ═══════════════════════════════════════════════════════════════════════════
// TYPES & INTERFACES
// ═══════════════════════════════════════════════════════════════════════════

interface Env {
  NOIZYLAB_KV: KVNamespace;
  NOIZYLAB_DB: D1Database;
  NOIZYLAB_UPLOADS: R2Bucket;
  NOIZYLAB_QUEUE: Queue;
  AI: Ai;
  JWT_SECRET: string;
  STRIPE_SECRET_KEY: string;
  ANTHROPIC_API_KEY: string;
  SENDGRID_API_KEY: string;
}

interface Customer {
  id: string;
  email: string;
  phone?: string;
  firstName: string;
  lastName: string;
  passwordHash: string;
  verified: boolean;
  avatar?: string;
  preferredContact: 'email' | 'phone' | 'sms';
  notificationPreferences: NotificationPrefs;
  loyaltyPoints: number;
  loyaltyTier: 'bronze' | 'silver' | 'gold' | 'platinum';
  totalSpent: number;
  repairCount: number;
  createdAt: string;
  lastLoginAt?: string;
}

interface NotificationPrefs {
  statusUpdates: boolean;
  marketingEmails: boolean;
  smsAlerts: boolean;
  pushNotifications: boolean;
}

interface CustomerTicket {
  id: string;
  customerId: string;
  status: 'submitted' | 'received' | 'diagnosing' | 'awaiting_approval' | 'in_repair' | 'qc' | 'ready' | 'completed' | 'cancelled';
  deviceType: string;
  deviceModel: string;
  serialNumber?: string;
  issueDescription: string;
  images: string[];
  quote?: Quote;
  timeline: TimelineEvent[];
  tracking?: ShippingTracking;
  invoice?: Invoice;
  createdAt: string;
  updatedAt: string;
  estimatedCompletion?: string;
  actualCompletion?: string;
  satisfactionRating?: number;
  feedback?: string;
}

interface Quote {
  id: string;
  laborCost: number;
  partsCost: number;
  diagnosticFee: number;
  tax: number;
  discount: number;
  total: number;
  validUntil: string;
  status: 'pending' | 'approved' | 'declined' | 'expired';
  items: QuoteItem[];
  notes?: string;
  approvedAt?: string;
}

interface QuoteItem {
  description: string;
  quantity: number;
  unitPrice: number;
  total: number;
  category: 'labor' | 'parts' | 'service';
}

interface TimelineEvent {
  timestamp: string;
  status: string;
  title: string;
  description: string;
  public: boolean;
  images?: string[];
}

interface ShippingTracking {
  carrier: string;
  trackingNumber: string;
  status: 'label_created' | 'in_transit' | 'out_for_delivery' | 'delivered';
  estimatedDelivery?: string;
  events: TrackingEvent[];
}

interface TrackingEvent {
  timestamp: string;
  location: string;
  description: string;
}

interface Invoice {
  id: string;
  amount: number;
  paid: boolean;
  paidAt?: string;
  paymentMethod?: string;
  stripePaymentIntentId?: string;
  pdfUrl?: string;
}

interface ConversationMessage {
  id: string;
  role: 'customer' | 'assistant' | 'technician';
  content: string;
  timestamp: string;
  attachments?: string[];
}

interface SupportConversation {
  id: string;
  customerId: string;
  ticketId?: string;
  status: 'active' | 'waiting' | 'resolved';
  messages: ConversationMessage[];
  createdAt: string;
  updatedAt: string;
}

// ═══════════════════════════════════════════════════════════════════════════
// AI CUSTOMER ASSISTANT
// ═══════════════════════════════════════════════════════════════════════════

class CustomerAssistant {
  private env: Env;

  constructor(env: Env) {
    this.env = env;
  }

  async chat(
    customerId: string,
    message: string,
    context: {
      tickets?: CustomerTicket[];
      conversation?: ConversationMessage[];
    }
  ): Promise<{ response: string; suggestedActions?: string[]; escalate?: boolean }> {
    
    const systemPrompt = `You are NoizyBot, the friendly AI customer service assistant for NoizyLab, a premium electronics repair shop.

Your personality:
- Warm, professional, and helpful
- Tech-savvy but explain things simply
- Proactive about offering solutions
- Empathetic about device issues

You can help customers with:
- Checking repair status
- Understanding quotes and pricing
- Scheduling appointments
- Tracking shipments
- Answering repair questions
- Providing troubleshooting tips
- Processing payments (tell them to click the payment link)

Customer's active tickets:
${context.tickets?.map(t => `
Ticket #${t.id}:
- Device: ${t.deviceModel}
- Status: ${t.status}
- Issue: ${t.issueDescription}
${t.quote ? `- Quote: $${t.quote.total} (${t.quote.status})` : ''}
${t.estimatedCompletion ? `- Est. Completion: ${t.estimatedCompletion}` : ''}
`).join('\n') || 'No active tickets'}

Previous conversation:
${context.conversation?.slice(-5).map(m => `${m.role}: ${m.content}`).join('\n') || 'New conversation'}

Respond naturally. If the customer needs human help or is upset, set escalate to true.
Provide response in JSON format:
{
  "response": "your message",
  "suggestedActions": ["action1", "action2"],
  "escalate": false
}`;

    try {
      const response = await fetch('https://api.anthropic.com/v1/messages', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'x-api-key': this.env.ANTHROPIC_API_KEY,
          'anthropic-version': '2023-06-01'
        },
        body: JSON.stringify({
          model: 'claude-sonnet-4-20250514',
          max_tokens: 1024,
          system: systemPrompt,
          messages: [{ role: 'user', content: message }]
        })
      });

      const data = await response.json() as any;
      const content = data.content[0].text;

      // Parse JSON response
      const jsonMatch = content.match(/\{[\s\S]*\}/);
      if (jsonMatch) {
        return JSON.parse(jsonMatch[0]);
      }

      return { response: content };
    } catch (error) {
      console.error('AI chat error:', error);
      return {
        response: "I'm having a moment! Let me connect you with our team for the best help.",
        escalate: true
      };
    }
  }

  async generateTicketSummary(ticket: CustomerTicket): Promise<string> {
    const prompt = `Create a friendly, easy-to-understand summary of this repair ticket for the customer:

Device: ${ticket.deviceModel}
Issue: ${ticket.issueDescription}
Current Status: ${ticket.status}
Timeline:
${ticket.timeline.filter(e => e.public).map(e => `- ${e.timestamp}: ${e.title}`).join('\n')}

${ticket.quote ? `Quote: $${ticket.quote.total}` : ''}

Write 2-3 sentences that are informative and reassuring.`;

    const response = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': this.env.ANTHROPIC_API_KEY,
        'anthropic-version': '2023-06-01'
      },
      body: JSON.stringify({
        model: 'claude-sonnet-4-20250514',
        max_tokens: 256,
        messages: [{ role: 'user', content: prompt }]
      })
    });

    const data = await response.json() as any;
    return data.content[0].text;
  }

  async diagnoseSelfHelp(issueDescription: string, deviceType: string): Promise<{
    possibleIssues: string[];
    selfFixSteps?: string[];
    needsProfessional: boolean;
    urgency: 'low' | 'medium' | 'high';
  }> {
    const prompt = `A customer describes their ${deviceType} issue:
"${issueDescription}"

Analyze and provide:
1. Possible causes (list 2-3)
2. Self-help steps they can try (if safe and appropriate)
3. Whether professional repair is recommended
4. Urgency level

Return JSON:
{
  "possibleIssues": ["issue1", "issue2"],
  "selfFixSteps": ["step1", "step2"],
  "needsProfessional": true/false,
  "urgency": "low|medium|high"
}`;

    const response = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': this.env.ANTHROPIC_API_KEY,
        'anthropic-version': '2023-06-01'
      },
      body: JSON.stringify({
        model: 'claude-sonnet-4-20250514',
        max_tokens: 512,
        messages: [{ role: 'user', content: prompt }]
      })
    });

    const data = await response.json() as any;
    const content = data.content[0].text;

    const jsonMatch = content.match(/\{[\s\S]*\}/);
    if (jsonMatch) {
      return JSON.parse(jsonMatch[0]);
    }

    return {
      possibleIssues: ['Unable to diagnose remotely'],
      needsProfessional: true,
      urgency: 'medium'
    };
  }
}

// ═══════════════════════════════════════════════════════════════════════════
// PAYMENT PROCESSOR
// ═══════════════════════════════════════════════════════════════════════════

class PaymentProcessor {
  private env: Env;

  constructor(env: Env) {
    this.env = env;
  }

  async createPaymentIntent(invoice: Invoice, customerId: string): Promise<{
    clientSecret: string;
    paymentIntentId: string;
  }> {
    const response = await fetch('https://api.stripe.com/v1/payment_intents', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${this.env.STRIPE_SECRET_KEY}`,
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: new URLSearchParams({
        amount: Math.round(invoice.amount * 100).toString(),
        currency: 'usd',
        'metadata[invoice_id]': invoice.id,
        'metadata[customer_id]': customerId,
        automatic_payment_methods: JSON.stringify({ enabled: true })
      } as Record<string, string>)
    });

    const data = await response.json() as any;

    if (data.error) {
      throw new Error(data.error.message);
    }

    return {
      clientSecret: data.client_secret,
      paymentIntentId: data.id
    };
  }

  async handleWebhook(body: string, signature: string): Promise<{ event: string; data: any }> {
    // In production, verify webhook signature with Stripe
    const payload = JSON.parse(body);
    return {
      event: payload.type,
      data: payload.data.object
    };
  }
}

// ═══════════════════════════════════════════════════════════════════════════
// LOYALTY SYSTEM
// ═══════════════════════════════════════════════════════════════════════════

class LoyaltyProgram {
  private static POINTS_PER_DOLLAR = 10;
  private static TIER_THRESHOLDS = {
    bronze: 0,
    silver: 1000,
    gold: 5000,
    platinum: 15000
  };
  private static TIER_DISCOUNTS = {
    bronze: 0,
    silver: 0.05,
    gold: 0.10,
    platinum: 0.15
  };

  static calculatePoints(amount: number): number {
    return Math.floor(amount * this.POINTS_PER_DOLLAR);
  }

  static getTier(totalPoints: number): 'bronze' | 'silver' | 'gold' | 'platinum' {
    if (totalPoints >= this.TIER_THRESHOLDS.platinum) return 'platinum';
    if (totalPoints >= this.TIER_THRESHOLDS.gold) return 'gold';
    if (totalPoints >= this.TIER_THRESHOLDS.silver) return 'silver';
    return 'bronze';
  }

  static getDiscount(tier: 'bronze' | 'silver' | 'gold' | 'platinum'): number {
    return this.TIER_DISCOUNTS[tier];
  }

  static getNextTierProgress(points: number): { nextTier: string; pointsNeeded: number; progress: number } {
    const tier = this.getTier(points);
    const tierList = ['bronze', 'silver', 'gold', 'platinum'] as const;
    const currentIndex = tierList.indexOf(tier);

    if (currentIndex === tierList.length - 1) {
      return { nextTier: 'max', pointsNeeded: 0, progress: 100 };
    }

    const nextTier = tierList[currentIndex + 1];
    const currentThreshold = this.TIER_THRESHOLDS[tier];
    const nextThreshold = this.TIER_THRESHOLDS[nextTier];
    const pointsNeeded = nextThreshold - points;
    const progress = ((points - currentThreshold) / (nextThreshold - currentThreshold)) * 100;

    return { nextTier, pointsNeeded, progress };
  }

  static getRewards(): Array<{ id: string; name: string; pointsCost: number; description: string }> {
    return [
      { id: 'free-diagnostic', name: 'Free Diagnostic', pointsCost: 500, description: 'Free diagnostic fee on your next repair' },
      { id: 'priority-service', name: 'Priority Service', pointsCost: 1000, description: 'Jump to the front of the queue' },
      { id: '10-off', name: '$10 Off', pointsCost: 1000, description: '$10 off any repair' },
      { id: '25-off', name: '$25 Off', pointsCost: 2500, description: '$25 off any repair' },
      { id: 'free-screen-protector', name: 'Free Screen Protector', pointsCost: 500, description: 'Free screen protector with repair' },
      { id: 'extended-warranty', name: '6-Month Extended Warranty', pointsCost: 3000, description: 'Extend your repair warranty by 6 months' }
    ];
  }
}

// ═══════════════════════════════════════════════════════════════════════════
// HONO APP
// ═══════════════════════════════════════════════════════════════════════════

const app = new Hono<{ Bindings: Env; Variables: { customer?: Customer } }>();

app.use('*', cors());

// Health check
app.get('/health', (c) => c.json({ 
  status: 'healthy', 
  service: 'customer-portal',
  version: '1.0.0'
}));

// ═══════════════════════════════════════════════════════════════════════════
// AUTH ROUTES
// ═══════════════════════════════════════════════════════════════════════════

app.post('/auth/register', async (c) => {
  const { email, password, firstName, lastName, phone } = await c.req.json();

  // Check if email exists
  const existing = await c.env.NOIZYLAB_DB.prepare(
    'SELECT id FROM customers WHERE email = ?'
  ).bind(email.toLowerCase()).first();

  if (existing) {
    return c.json({ error: 'Email already registered' }, 400);
  }

  // Hash password (using Web Crypto API)
  const encoder = new TextEncoder();
  const data = encoder.encode(password);
  const hashBuffer = await crypto.subtle.digest('SHA-256', data);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  const passwordHash = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');

  const customerId = `cust_${Date.now()}_${Math.random().toString(36).substring(7)}`;

  const customer: Customer = {
    id: customerId,
    email: email.toLowerCase(),
    phone,
    firstName,
    lastName,
    passwordHash,
    verified: false,
    preferredContact: 'email',
    notificationPreferences: {
      statusUpdates: true,
      marketingEmails: false,
      smsAlerts: false,
      pushNotifications: false
    },
    loyaltyPoints: 0,
    loyaltyTier: 'bronze',
    totalSpent: 0,
    repairCount: 0,
    createdAt: new Date().toISOString()
  };

  await c.env.NOIZYLAB_DB.prepare(`
    INSERT INTO customers (id, email, phone, first_name, last_name, password_hash, verified, 
      notification_prefs, loyalty_points, loyalty_tier, total_spent, repair_count, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
  `).bind(
    customerId, customer.email, customer.phone || null, firstName, lastName,
    passwordHash, 0, JSON.stringify(customer.notificationPreferences),
    0, 'bronze', 0, 0, customer.createdAt
  ).run();

  // Generate verification token
  const verificationToken = crypto.randomUUID();
  await c.env.NOIZYLAB_KV.put(`verify:${verificationToken}`, customerId, { expirationTtl: 86400 });

  // Queue verification email
  await c.env.NOIZYLAB_QUEUE.send({
    type: 'send_email',
    template: 'verification',
    to: email,
    data: {
      firstName,
      verificationLink: `https://portal.noizylab.io/verify?token=${verificationToken}`
    }
  });

  // Generate JWT
  const token = await sign(
    { sub: customerId, email: customer.email, exp: Math.floor(Date.now() / 1000) + 86400 * 7 },
    c.env.JWT_SECRET
  );

  return c.json({
    customer: {
      id: customerId,
      email: customer.email,
      firstName,
      lastName,
      loyaltyTier: 'bronze'
    },
    token
  }, 201);
});

app.post('/auth/login', async (c) => {
  const { email, password } = await c.req.json();

  const row = await c.env.NOIZYLAB_DB.prepare(
    'SELECT * FROM customers WHERE email = ?'
  ).bind(email.toLowerCase()).first();

  if (!row) {
    return c.json({ error: 'Invalid email or password' }, 401);
  }

  // Verify password
  const encoder = new TextEncoder();
  const data = encoder.encode(password);
  const hashBuffer = await crypto.subtle.digest('SHA-256', data);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  const passwordHash = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');

  if (passwordHash !== row.password_hash) {
    return c.json({ error: 'Invalid email or password' }, 401);
  }

  // Update last login
  await c.env.NOIZYLAB_DB.prepare(
    'UPDATE customers SET last_login_at = ? WHERE id = ?'
  ).bind(new Date().toISOString(), row.id).run();

  // Generate JWT
  const token = await sign(
    { sub: row.id, email: row.email, exp: Math.floor(Date.now() / 1000) + 86400 * 7 },
    c.env.JWT_SECRET
  );

  return c.json({
    customer: {
      id: row.id,
      email: row.email,
      firstName: row.first_name,
      lastName: row.last_name,
      loyaltyTier: row.loyalty_tier,
      loyaltyPoints: row.loyalty_points
    },
    token
  });
});

app.post('/auth/forgot-password', async (c) => {
  const { email } = await c.req.json();

  const customer = await c.env.NOIZYLAB_DB.prepare(
    'SELECT id, first_name FROM customers WHERE email = ?'
  ).bind(email.toLowerCase()).first();

  if (customer) {
    const resetToken = crypto.randomUUID();
    await c.env.NOIZYLAB_KV.put(`reset:${resetToken}`, customer.id as string, { expirationTtl: 3600 });

    await c.env.NOIZYLAB_QUEUE.send({
      type: 'send_email',
      template: 'password_reset',
      to: email,
      data: {
        firstName: customer.first_name,
        resetLink: `https://portal.noizylab.io/reset-password?token=${resetToken}`
      }
    });
  }

  return c.json({ message: 'If that email exists, a reset link has been sent' });
});

// ═══════════════════════════════════════════════════════════════════════════
// PROTECTED ROUTES (JWT Required)
// ═══════════════════════════════════════════════════════════════════════════

const protected_routes = new Hono<{ Bindings: Env; Variables: { customer: Customer } }>();

protected_routes.use('*', async (c, next) => {
  const authHeader = c.req.header('Authorization');
  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return c.json({ error: 'Unauthorized' }, 401);
  }

  try {
    const token = authHeader.replace('Bearer ', '');
    const payload = await import('hono/jwt').then(m => m.verify(token, c.env.JWT_SECRET));
    
    const customer = await c.env.NOIZYLAB_DB.prepare(
      'SELECT * FROM customers WHERE id = ?'
    ).bind(payload.sub).first();

    if (!customer) {
      return c.json({ error: 'Customer not found' }, 401);
    }

    c.set('customer', customer as unknown as Customer);
    await next();
  } catch (error) {
    return c.json({ error: 'Invalid token' }, 401);
  }
});

// Get profile
protected_routes.get('/profile', async (c) => {
  const customer = c.get('customer');
  
  const loyaltyProgress = LoyaltyProgram.getNextTierProgress(customer.loyaltyPoints);
  const discount = LoyaltyProgram.getDiscount(customer.loyaltyTier);

  return c.json({
    customer: {
      id: customer.id,
      email: customer.email,
      firstName: customer.firstName,
      lastName: customer.lastName,
      phone: customer.phone,
      preferredContact: customer.preferredContact,
      notificationPreferences: customer.notificationPreferences,
      verified: customer.verified
    },
    loyalty: {
      points: customer.loyaltyPoints,
      tier: customer.loyaltyTier,
      discount: `${discount * 100}%`,
      nextTier: loyaltyProgress.nextTier,
      pointsToNextTier: loyaltyProgress.pointsNeeded,
      progress: loyaltyProgress.progress
    },
    stats: {
      totalSpent: customer.totalSpent,
      repairCount: customer.repairCount,
      memberSince: customer.createdAt
    }
  });
});

// Update profile
protected_routes.put('/profile', async (c) => {
  const customer = c.get('customer');
  const updates = await c.req.json();

  const allowedFields = ['firstName', 'lastName', 'phone', 'preferredContact', 'notificationPreferences'];
  const filteredUpdates: Record<string, any> = {};

  for (const field of allowedFields) {
    if (updates[field] !== undefined) {
      filteredUpdates[field] = updates[field];
    }
  }

  if (Object.keys(filteredUpdates).length > 0) {
    const setClause = Object.entries(filteredUpdates).map(([key]) => {
      const dbKey = key.replace(/([A-Z])/g, '_$1').toLowerCase();
      return `${dbKey} = ?`;
    }).join(', ');

    await c.env.NOIZYLAB_DB.prepare(
      `UPDATE customers SET ${setClause}, updated_at = ? WHERE id = ?`
    ).bind(
      ...Object.values(filteredUpdates).map(v => typeof v === 'object' ? JSON.stringify(v) : v),
      new Date().toISOString(),
      customer.id
    ).run();
  }

  return c.json({ message: 'Profile updated' });
});

// ═══════════════════════════════════════════════════════════════════════════
// TICKETS
// ═══════════════════════════════════════════════════════════════════════════

protected_routes.get('/tickets', async (c) => {
  const customer = c.get('customer');
  const status = c.req.query('status');

  let query = 'SELECT * FROM tickets WHERE customer_id = ?';
  const params: any[] = [customer.id];

  if (status) {
    query += ' AND status = ?';
    params.push(status);
  }

  query += ' ORDER BY created_at DESC';

  const { results } = await c.env.NOIZYLAB_DB.prepare(query).bind(...params).all();

  return c.json({
    tickets: results.map(row => ({
      id: row.id,
      status: row.status,
      deviceType: row.device_type,
      deviceModel: row.device_model,
      issueDescription: row.issue_description,
      quote: row.quote_data ? JSON.parse(row.quote_data as string) : null,
      createdAt: row.created_at,
      estimatedCompletion: row.estimated_completion
    }))
  });
});

protected_routes.get('/tickets/:id', async (c) => {
  const customer = c.get('customer');
  const ticketId = c.req.param('id');

  const ticket = await c.env.NOIZYLAB_DB.prepare(
    'SELECT * FROM tickets WHERE id = ? AND customer_id = ?'
  ).bind(ticketId, customer.id).first();

  if (!ticket) {
    return c.json({ error: 'Ticket not found' }, 404);
  }

  const assistant = new CustomerAssistant(c.env);
  const summary = await assistant.generateTicketSummary(ticket as unknown as CustomerTicket);

  return c.json({
    ticket: {
      id: ticket.id,
      status: ticket.status,
      deviceType: ticket.device_type,
      deviceModel: ticket.device_model,
      serialNumber: ticket.serial_number,
      issueDescription: ticket.issue_description,
      images: ticket.images ? JSON.parse(ticket.images as string) : [],
      quote: ticket.quote_data ? JSON.parse(ticket.quote_data as string) : null,
      timeline: ticket.timeline ? JSON.parse(ticket.timeline as string).filter((e: TimelineEvent) => e.public) : [],
      tracking: ticket.tracking_data ? JSON.parse(ticket.tracking_data as string) : null,
      invoice: ticket.invoice_data ? JSON.parse(ticket.invoice_data as string) : null,
      createdAt: ticket.created_at,
      estimatedCompletion: ticket.estimated_completion
    },
    aiSummary: summary
  });
});

protected_routes.post('/tickets', async (c) => {
  const customer = c.get('customer');
  const { deviceType, deviceModel, serialNumber, issueDescription, images } = await c.req.json();

  const ticketId = `TKT-${Date.now().toString(36).toUpperCase()}`;

  const timeline: TimelineEvent[] = [{
    timestamp: new Date().toISOString(),
    status: 'submitted',
    title: 'Repair Request Submitted',
    description: 'Your repair request has been received. We\'ll contact you shortly.',
    public: true
  }];

  await c.env.NOIZYLAB_DB.prepare(`
    INSERT INTO tickets (id, customer_id, status, device_type, device_model, serial_number,
      issue_description, images, timeline, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
  `).bind(
    ticketId, customer.id, 'submitted', deviceType, deviceModel, serialNumber || null,
    issueDescription, JSON.stringify(images || []), JSON.stringify(timeline),
    new Date().toISOString()
  ).run();

  // Queue notification
  await c.env.NOIZYLAB_QUEUE.send({
    type: 'send_email',
    template: 'ticket_created',
    to: customer.email,
    data: {
      firstName: customer.firstName,
      ticketId,
      deviceModel,
      issueDescription
    }
  });

  return c.json({ ticketId, status: 'submitted' }, 201);
});

// Approve quote
protected_routes.post('/tickets/:id/approve-quote', async (c) => {
  const customer = c.get('customer');
  const ticketId = c.req.param('id');

  const ticket = await c.env.NOIZYLAB_DB.prepare(
    'SELECT * FROM tickets WHERE id = ? AND customer_id = ? AND status = ?'
  ).bind(ticketId, customer.id, 'awaiting_approval').first();

  if (!ticket) {
    return c.json({ error: 'Ticket not found or not awaiting approval' }, 404);
  }

  const quote = JSON.parse(ticket.quote_data as string) as Quote;
  quote.status = 'approved';
  quote.approvedAt = new Date().toISOString();

  const timeline = JSON.parse(ticket.timeline as string) as TimelineEvent[];
  timeline.push({
    timestamp: new Date().toISOString(),
    status: 'approved',
    title: 'Quote Approved',
    description: 'You approved the repair quote. We\'re starting work on your device!',
    public: true
  });

  await c.env.NOIZYLAB_DB.prepare(`
    UPDATE tickets SET status = ?, quote_data = ?, timeline = ?, updated_at = ?
    WHERE id = ?
  `).bind(
    'in_repair',
    JSON.stringify(quote),
    JSON.stringify(timeline),
    new Date().toISOString(),
    ticketId
  ).run();

  return c.json({ message: 'Quote approved', status: 'in_repair' });
});

// Decline quote
protected_routes.post('/tickets/:id/decline-quote', async (c) => {
  const customer = c.get('customer');
  const ticketId = c.req.param('id');
  const { reason } = await c.req.json();

  const ticket = await c.env.NOIZYLAB_DB.prepare(
    'SELECT * FROM tickets WHERE id = ? AND customer_id = ? AND status = ?'
  ).bind(ticketId, customer.id, 'awaiting_approval').first();

  if (!ticket) {
    return c.json({ error: 'Ticket not found or not awaiting approval' }, 404);
  }

  const quote = JSON.parse(ticket.quote_data as string) as Quote;
  quote.status = 'declined';

  const timeline = JSON.parse(ticket.timeline as string) as TimelineEvent[];
  timeline.push({
    timestamp: new Date().toISOString(),
    status: 'declined',
    title: 'Quote Declined',
    description: 'You declined the repair quote.',
    public: true
  });

  await c.env.NOIZYLAB_DB.prepare(`
    UPDATE tickets SET status = ?, quote_data = ?, timeline = ?, updated_at = ?
    WHERE id = ?
  `).bind(
    'cancelled',
    JSON.stringify(quote),
    JSON.stringify(timeline),
    new Date().toISOString(),
    ticketId
  ).run();

  return c.json({ message: 'Quote declined', status: 'cancelled' });
});

// ═══════════════════════════════════════════════════════════════════════════
// PAYMENTS
// ═══════════════════════════════════════════════════════════════════════════

protected_routes.post('/tickets/:id/pay', async (c) => {
  const customer = c.get('customer');
  const ticketId = c.req.param('id');

  const ticket = await c.env.NOIZYLAB_DB.prepare(
    'SELECT * FROM tickets WHERE id = ? AND customer_id = ?'
  ).bind(ticketId, customer.id).first();

  if (!ticket) {
    return c.json({ error: 'Ticket not found' }, 404);
  }

  const invoice = ticket.invoice_data ? JSON.parse(ticket.invoice_data as string) as Invoice : null;
  if (!invoice || invoice.paid) {
    return c.json({ error: 'No payment required or already paid' }, 400);
  }

  const payments = new PaymentProcessor(c.env);
  const { clientSecret, paymentIntentId } = await payments.createPaymentIntent(invoice, customer.id);

  // Store payment intent
  invoice.stripePaymentIntentId = paymentIntentId;
  await c.env.NOIZYLAB_DB.prepare(
    'UPDATE tickets SET invoice_data = ? WHERE id = ?'
  ).bind(JSON.stringify(invoice), ticketId).run();

  return c.json({ clientSecret });
});

// ═══════════════════════════════════════════════════════════════════════════
// AI CHAT
// ═══════════════════════════════════════════════════════════════════════════

protected_routes.post('/chat', async (c) => {
  const customer = c.get('customer');
  const { message, conversationId, ticketId } = await c.req.json();

  const assistant = new CustomerAssistant(c.env);

  // Get active tickets for context
  const { results: tickets } = await c.env.NOIZYLAB_DB.prepare(
    'SELECT * FROM tickets WHERE customer_id = ? AND status NOT IN (?, ?)'
  ).bind(customer.id, 'completed', 'cancelled').all();

  // Get conversation history
  let conversation: ConversationMessage[] = [];
  if (conversationId) {
    const cached = await c.env.NOIZYLAB_KV.get(`chat:${conversationId}`);
    if (cached) {
      conversation = JSON.parse(cached);
    }
  }

  // Generate response
  const result = await assistant.chat(customer.id, message, {
    tickets: tickets as unknown as CustomerTicket[],
    conversation
  });

  // Add messages to conversation
  const newMessages: ConversationMessage[] = [
    {
      id: crypto.randomUUID(),
      role: 'customer',
      content: message,
      timestamp: new Date().toISOString()
    },
    {
      id: crypto.randomUUID(),
      role: 'assistant',
      content: result.response,
      timestamp: new Date().toISOString()
    }
  ];

  conversation = [...conversation, ...newMessages];
  const convId = conversationId || crypto.randomUUID();

  await c.env.NOIZYLAB_KV.put(`chat:${convId}`, JSON.stringify(conversation), { expirationTtl: 86400 });

  // If escalate, create support conversation
  if (result.escalate) {
    await c.env.NOIZYLAB_DB.prepare(`
      INSERT INTO support_conversations (id, customer_id, ticket_id, status, messages, created_at)
      VALUES (?, ?, ?, ?, ?, ?)
    `).bind(
      convId, customer.id, ticketId || null, 'waiting',
      JSON.stringify(conversation), new Date().toISOString()
    ).run();

    await c.env.NOIZYLAB_QUEUE.send({
      type: 'support_escalation',
      conversationId: convId,
      customerId: customer.id,
      customerName: `${customer.firstName} ${customer.lastName}`
    });
  }

  return c.json({
    conversationId: convId,
    response: result.response,
    suggestedActions: result.suggestedActions,
    escalated: result.escalate
  });
});

protected_routes.get('/chat/:conversationId/history', async (c) => {
  const customer = c.get('customer');
  const conversationId = c.req.param('conversationId');

  const cached = await c.env.NOIZYLAB_KV.get(`chat:${conversationId}`);
  if (!cached) {
    return c.json({ messages: [] });
  }

  return c.json({ messages: JSON.parse(cached) });
});

// ═══════════════════════════════════════════════════════════════════════════
// SELF-HELP DIAGNOSIS
// ═══════════════════════════════════════════════════════════════════════════

protected_routes.post('/diagnose', async (c) => {
  const { issueDescription, deviceType } = await c.req.json();

  const assistant = new CustomerAssistant(c.env);
  const diagnosis = await assistant.diagnoseSelfHelp(issueDescription, deviceType);

  return c.json({ diagnosis });
});

// ═══════════════════════════════════════════════════════════════════════════
// LOYALTY & REWARDS
// ═══════════════════════════════════════════════════════════════════════════

protected_routes.get('/loyalty', async (c) => {
  const customer = c.get('customer');

  const progress = LoyaltyProgram.getNextTierProgress(customer.loyaltyPoints);
  const rewards = LoyaltyProgram.getRewards();

  return c.json({
    points: customer.loyaltyPoints,
    tier: customer.loyaltyTier,
    discount: `${LoyaltyProgram.getDiscount(customer.loyaltyTier) * 100}%`,
    progress,
    rewards,
    history: [] // Would fetch from DB
  });
});

protected_routes.post('/loyalty/redeem', async (c) => {
  const customer = c.get('customer');
  const { rewardId } = await c.req.json();

  const rewards = LoyaltyProgram.getRewards();
  const reward = rewards.find(r => r.id === rewardId);

  if (!reward) {
    return c.json({ error: 'Reward not found' }, 404);
  }

  if (customer.loyaltyPoints < reward.pointsCost) {
    return c.json({ error: 'Insufficient points' }, 400);
  }

  const newPoints = customer.loyaltyPoints - reward.pointsCost;
  const newTier = LoyaltyProgram.getTier(newPoints);

  await c.env.NOIZYLAB_DB.prepare(`
    UPDATE customers SET loyalty_points = ?, loyalty_tier = ?, updated_at = ?
    WHERE id = ?
  `).bind(newPoints, newTier, new Date().toISOString(), customer.id).run();

  // Generate reward code
  const rewardCode = `${rewardId.toUpperCase()}-${crypto.randomUUID().substring(0, 8).toUpperCase()}`;
  await c.env.NOIZYLAB_KV.put(`reward:${rewardCode}`, JSON.stringify({
    customerId: customer.id,
    rewardId,
    rewardName: reward.name,
    createdAt: new Date().toISOString(),
    expiresAt: new Date(Date.now() + 90 * 24 * 60 * 60 * 1000).toISOString()
  }), { expirationTtl: 90 * 24 * 60 * 60 });

  return c.json({
    message: 'Reward redeemed!',
    rewardCode,
    remainingPoints: newPoints,
    tier: newTier
  });
});

// ═══════════════════════════════════════════════════════════════════════════
// APPOINTMENTS
// ═══════════════════════════════════════════════════════════════════════════

protected_routes.get('/appointments/slots', async (c) => {
  const date = c.req.query('date') || new Date().toISOString().split('T')[0];
  const deviceType = c.req.query('deviceType');

  // Generate available time slots
  const slots = [];
  const baseDate = new Date(date);
  const dayOfWeek = baseDate.getDay();

  // Skip Sunday
  if (dayOfWeek === 0) {
    return c.json({ slots: [], message: 'Closed on Sundays' });
  }

  const startHour = dayOfWeek === 6 ? 10 : 9; // Saturday 10am, weekdays 9am
  const endHour = dayOfWeek === 6 ? 16 : 18; // Saturday 4pm, weekdays 6pm

  for (let hour = startHour; hour < endHour; hour++) {
    for (const minute of [0, 30]) {
      const slotTime = new Date(baseDate);
      slotTime.setHours(hour, minute, 0, 0);

      // Check availability (would query DB for booked slots)
      const available = Math.random() > 0.3; // Simulated availability

      slots.push({
        time: slotTime.toISOString(),
        available,
        duration: 30
      });
    }
  }

  return c.json({ date, slots });
});

protected_routes.post('/appointments', async (c) => {
  const customer = c.get('customer');
  const { slotTime, deviceType, deviceModel, issueDescription, ticketId } = await c.req.json();

  const appointmentId = `APT-${Date.now().toString(36).toUpperCase()}`;

  await c.env.NOIZYLAB_DB.prepare(`
    INSERT INTO appointments (id, customer_id, ticket_id, scheduled_time, device_type, 
      device_model, issue_description, status, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
  `).bind(
    appointmentId, customer.id, ticketId || null, slotTime, deviceType,
    deviceModel, issueDescription, 'scheduled', new Date().toISOString()
  ).run();

  // Queue confirmation email
  await c.env.NOIZYLAB_QUEUE.send({
    type: 'send_email',
    template: 'appointment_confirmation',
    to: customer.email,
    data: {
      firstName: customer.firstName,
      appointmentId,
      scheduledTime: slotTime,
      deviceModel
    }
  });

  return c.json({ appointmentId, scheduledTime: slotTime }, 201);
});

// Mount protected routes
app.route('/api', protected_routes);

// ═══════════════════════════════════════════════════════════════════════════
// PUBLIC ROUTES
// ═══════════════════════════════════════════════════════════════════════════

// Track ticket without login (by ticket ID + email)
app.post('/track', async (c) => {
  const { ticketId, email } = await c.req.json();

  const ticket = await c.env.NOIZYLAB_DB.prepare(`
    SELECT t.*, c.email FROM tickets t
    JOIN customers c ON t.customer_id = c.id
    WHERE t.id = ? AND c.email = ?
  `).bind(ticketId, email.toLowerCase()).first();

  if (!ticket) {
    return c.json({ error: 'Ticket not found' }, 404);
  }

  const timeline = JSON.parse(ticket.timeline as string).filter((e: TimelineEvent) => e.public);

  return c.json({
    ticket: {
      id: ticket.id,
      status: ticket.status,
      deviceModel: ticket.device_model,
      timeline,
      estimatedCompletion: ticket.estimated_completion
    }
  });
});

// Stripe webhook
app.post('/webhooks/stripe', async (c) => {
  const signature = c.req.header('Stripe-Signature') || '';
  const body = await c.req.text();

  const payments = new PaymentProcessor(c.env);
  const { event, data } = await payments.handleWebhook(body, signature);

  if (event === 'payment_intent.succeeded') {
    const invoiceId = data.metadata?.invoice_id;
    const customerId = data.metadata?.customer_id;

    if (invoiceId) {
      // Update invoice as paid
      const ticket = await c.env.NOIZYLAB_DB.prepare(
        'SELECT * FROM tickets WHERE invoice_data LIKE ?'
      ).bind(`%"id":"${invoiceId}"%`).first();

      if (ticket) {
        const invoice = JSON.parse(ticket.invoice_data as string) as Invoice;
        invoice.paid = true;
        invoice.paidAt = new Date().toISOString();
        invoice.paymentMethod = data.payment_method_types?.[0];

        await c.env.NOIZYLAB_DB.prepare(
          'UPDATE tickets SET invoice_data = ? WHERE id = ?'
        ).bind(JSON.stringify(invoice), ticket.id).run();

        // Update customer loyalty points
        const points = LoyaltyProgram.calculatePoints(invoice.amount);
        await c.env.NOIZYLAB_DB.prepare(`
          UPDATE customers 
          SET loyalty_points = loyalty_points + ?, total_spent = total_spent + ?
          WHERE id = ?
        `).bind(points, invoice.amount, customerId).run();
      }
    }
  }

  return c.json({ received: true });
});

export default app;
