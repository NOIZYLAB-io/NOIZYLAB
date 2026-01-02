/**
 * Webhook System for B2B Integrations
 * 
 * Allows enterprise customers to receive real-time notifications
 * about scan completions, issues detected, and account events
 */

interface WebhookConfig {
  id: string;
  userId: string;
  url: string;
  secret: string;
  events: WebhookEvent[];
  active: boolean;
  createdAt: string;
  lastTriggered?: string;
  failureCount: number;
}

type WebhookEvent = 
  | 'scan.started'
  | 'scan.completed'
  | 'scan.failed'
  | 'issue.critical'
  | 'credits.low'
  | 'subscription.created'
  | 'subscription.cancelled';

interface WebhookPayload {
  event: WebhookEvent;
  timestamp: string;
  data: Record<string, unknown>;
}

// ============================================================================
// WEBHOOK MANAGER
// ============================================================================

export class WebhookManager {
  private kv: KVNamespace;

  constructor(kv: KVNamespace) {
    this.kv = kv;
  }

  /**
   * Register a new webhook endpoint
   */
  async register(
    userId: string,
    url: string,
    events: WebhookEvent[]
  ): Promise<WebhookConfig> {
    // Generate secret for signature verification
    const secret = this.generateSecret();
    
    const webhook: WebhookConfig = {
      id: `wh_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`,
      userId,
      url,
      secret,
      events,
      active: true,
      createdAt: new Date().toISOString(),
      failureCount: 0,
    };

    // Store webhook
    await this.kv.put(
      `webhook:${webhook.id}`,
      JSON.stringify(webhook)
    );

    // Index by user
    const userWebhooks = await this.getUserWebhooks(userId);
    userWebhooks.push(webhook.id);
    await this.kv.put(`user:${userId}:webhooks`, JSON.stringify(userWebhooks));

    return webhook;
  }

  /**
   * Get all webhooks for a user
   */
  async getUserWebhooks(userId: string): Promise<string[]> {
    const data = await this.kv.get(`user:${userId}:webhooks`, 'json');
    return (data as string[]) || [];
  }

  /**
   * Get webhook by ID
   */
  async getWebhook(webhookId: string): Promise<WebhookConfig | null> {
    return this.kv.get(`webhook:${webhookId}`, 'json');
  }

  /**
   * Update webhook configuration
   */
  async updateWebhook(
    webhookId: string,
    updates: Partial<Pick<WebhookConfig, 'url' | 'events' | 'active'>>
  ): Promise<WebhookConfig | null> {
    const webhook = await this.getWebhook(webhookId);
    if (!webhook) return null;

    const updated = { ...webhook, ...updates };
    await this.kv.put(`webhook:${webhookId}`, JSON.stringify(updated));
    
    return updated;
  }

  /**
   * Delete a webhook
   */
  async deleteWebhook(webhookId: string, userId: string): Promise<boolean> {
    const webhook = await this.getWebhook(webhookId);
    if (!webhook || webhook.userId !== userId) return false;

    await this.kv.delete(`webhook:${webhookId}`);

    // Remove from user index
    const userWebhooks = await this.getUserWebhooks(userId);
    const filtered = userWebhooks.filter(id => id !== webhookId);
    await this.kv.put(`user:${userId}:webhooks`, JSON.stringify(filtered));

    return true;
  }

  /**
   * Trigger webhooks for an event
   */
  async trigger(
    userId: string,
    event: WebhookEvent,
    data: Record<string, unknown>
  ): Promise<void> {
    const webhookIds = await this.getUserWebhooks(userId);
    
    for (const webhookId of webhookIds) {
      const webhook = await this.getWebhook(webhookId);
      if (!webhook || !webhook.active) continue;
      if (!webhook.events.includes(event)) continue;

      // Queue webhook delivery (don't await - fire and forget)
      this.deliver(webhook, event, data).catch(console.error);
    }
  }

  /**
   * Deliver webhook payload
   */
  private async deliver(
    webhook: WebhookConfig,
    event: WebhookEvent,
    data: Record<string, unknown>
  ): Promise<void> {
    const payload: WebhookPayload = {
      event,
      timestamp: new Date().toISOString(),
      data,
    };

    const body = JSON.stringify(payload);
    const signature = await this.sign(body, webhook.secret);

    try {
      const response = await fetch(webhook.url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-Webhook-ID': webhook.id,
          'X-Webhook-Event': event,
          'X-Webhook-Signature': signature,
          'X-Webhook-Timestamp': payload.timestamp,
        },
        body,
      });

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }

      // Success - reset failure count
      await this.updateWebhook(webhook.id, {});
      webhook.failureCount = 0;
      webhook.lastTriggered = payload.timestamp;
      await this.kv.put(`webhook:${webhook.id}`, JSON.stringify(webhook));

    } catch (error) {
      console.error(`Webhook ${webhook.id} failed:`, error);
      
      // Increment failure count
      webhook.failureCount++;
      
      // Disable after 5 consecutive failures
      if (webhook.failureCount >= 5) {
        webhook.active = false;
        console.warn(`Webhook ${webhook.id} disabled after 5 failures`);
      }
      
      await this.kv.put(`webhook:${webhook.id}`, JSON.stringify(webhook));
    }
  }

  /**
   * Generate HMAC signature
   */
  private async sign(payload: string, secret: string): Promise<string> {
    const encoder = new TextEncoder();
    const key = await crypto.subtle.importKey(
      'raw',
      encoder.encode(secret),
      { name: 'HMAC', hash: 'SHA-256' },
      false,
      ['sign']
    );
    
    const signature = await crypto.subtle.sign(
      'HMAC',
      key,
      encoder.encode(payload)
    );
    
    return btoa(String.fromCharCode(...new Uint8Array(signature)));
  }

  /**
   * Generate random secret
   */
  private generateSecret(): string {
    const array = new Uint8Array(32);
    crypto.getRandomValues(array);
    return Array.from(array, b => b.toString(16).padStart(2, '0')).join('');
  }

  /**
   * Verify incoming webhook (for customers to implement)
   */
  static async verify(
    payload: string,
    signature: string,
    secret: string
  ): Promise<boolean> {
    const encoder = new TextEncoder();
    const key = await crypto.subtle.importKey(
      'raw',
      encoder.encode(secret),
      { name: 'HMAC', hash: 'SHA-256' },
      false,
      ['verify']
    );

    const sigBytes = Uint8Array.from(atob(signature), c => c.charCodeAt(0));
    
    return crypto.subtle.verify(
      'HMAC',
      key,
      sigBytes,
      encoder.encode(payload)
    );
  }
}

// ============================================================================
// API ROUTES FOR WEBHOOK MANAGEMENT
// ============================================================================

export function createWebhookRoutes(manager: WebhookManager) {
  return {
    // List webhooks
    async list(userId: string): Promise<Response> {
      const webhookIds = await manager.getUserWebhooks(userId);
      const webhooks = await Promise.all(
        webhookIds.map(id => manager.getWebhook(id))
      );
      
      // Don't expose secrets
      const safe = webhooks
        .filter(Boolean)
        .map(w => ({ ...w, secret: '***' }));
      
      return new Response(JSON.stringify({ webhooks: safe }), {
        headers: { 'Content-Type': 'application/json' },
      });
    },

    // Create webhook
    async create(userId: string, request: Request): Promise<Response> {
      const body = await request.json() as { url: string; events: WebhookEvent[] };
      
      if (!body.url || !body.events?.length) {
        return new Response(JSON.stringify({ error: 'URL and events required' }), {
          status: 400,
          headers: { 'Content-Type': 'application/json' },
        });
      }

      const webhook = await manager.register(userId, body.url, body.events);
      
      return new Response(JSON.stringify({ webhook }), {
        status: 201,
        headers: { 'Content-Type': 'application/json' },
      });
    },

    // Update webhook
    async update(userId: string, webhookId: string, request: Request): Promise<Response> {
      const webhook = await manager.getWebhook(webhookId);
      
      if (!webhook || webhook.userId !== userId) {
        return new Response(JSON.stringify({ error: 'Not found' }), {
          status: 404,
          headers: { 'Content-Type': 'application/json' },
        });
      }

      const body = await request.json() as Partial<WebhookConfig>;
      const updated = await manager.updateWebhook(webhookId, {
        url: body.url,
        events: body.events,
        active: body.active,
      });
      
      return new Response(JSON.stringify({ webhook: { ...updated, secret: '***' } }), {
        headers: { 'Content-Type': 'application/json' },
      });
    },

    // Delete webhook
    async delete(userId: string, webhookId: string): Promise<Response> {
      const deleted = await manager.deleteWebhook(webhookId, userId);
      
      if (!deleted) {
        return new Response(JSON.stringify({ error: 'Not found' }), {
          status: 404,
          headers: { 'Content-Type': 'application/json' },
        });
      }
      
      return new Response(JSON.stringify({ success: true }), {
        headers: { 'Content-Type': 'application/json' },
      });
    },

    // Test webhook
    async test(userId: string, webhookId: string): Promise<Response> {
      const webhook = await manager.getWebhook(webhookId);
      
      if (!webhook || webhook.userId !== userId) {
        return new Response(JSON.stringify({ error: 'Not found' }), {
          status: 404,
          headers: { 'Content-Type': 'application/json' },
        });
      }

      await manager.trigger(userId, 'scan.completed', {
        test: true,
        message: 'This is a test webhook delivery',
        scanId: 'test_123',
        timestamp: new Date().toISOString(),
      });
      
      return new Response(JSON.stringify({ success: true, message: 'Test webhook sent' }), {
        headers: { 'Content-Type': 'application/json' },
      });
    },
  };
}

export default {
  WebhookManager,
  createWebhookRoutes,
};
