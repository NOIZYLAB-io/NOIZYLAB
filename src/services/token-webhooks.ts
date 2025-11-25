/**
 * NOIZYLAB Token Webhook Service
 * Webhook notifications for token events
 */

import type { Env } from '../types';

export type TokenEventType =
  | 'token.created'
  | 'token.revoked'
  | 'token.rotated'
  | 'token.expired'
  | 'token.rate_limited'
  | 'token.suspicious_activity'
  | 'token.first_use'
  | 'token.scope_violation';

export interface TokenWebhook {
  id: string;
  url: string;
  events: TokenEventType[];
  secret: string;
  isActive: boolean;
  createdAt: string;
  lastTriggeredAt?: string;
  failureCount: number;
  metadata?: Record<string, string>;
}

export interface TokenWebhookPayload {
  event: TokenEventType;
  timestamp: string;
  data: {
    tokenId: string;
    tokenName?: string;
    details?: Record<string, unknown>;
  };
}

export interface CreateWebhookInput {
  url: string;
  events: TokenEventType[];
  metadata?: Record<string, string>;
}

export class TokenWebhookService {
  private readonly kv: KVNamespace;
  private readonly prefix = 'webhook:token';
  private readonly maxRetries = 3;
  private readonly retryDelays = [1000, 5000, 30000]; // 1s, 5s, 30s

  constructor(kv: KVNamespace) {
    this.kv = kv;
  }

  /**
   * Create a new webhook
   */
  async createWebhook(input: CreateWebhookInput): Promise<TokenWebhook> {
    const id = this.generateId('whk');
    const secret = this.generateSecret();

    const webhook: TokenWebhook = {
      id,
      url: input.url,
      events: input.events,
      secret,
      isActive: true,
      createdAt: new Date().toISOString(),
      failureCount: 0,
      metadata: input.metadata,
    };

    await this.kv.put(`${this.prefix}:${id}`, JSON.stringify(webhook));

    // Index by event for efficient lookup
    for (const event of input.events) {
      await this.addWebhookToEvent(event, id);
    }

    return webhook;
  }

  /**
   * Get webhook by ID
   */
  async getWebhook(id: string): Promise<TokenWebhook | null> {
    const data = await this.kv.get(`${this.prefix}:${id}`);
    return data ? JSON.parse(data) : null;
  }

  /**
   * List all webhooks
   */
  async listWebhooks(): Promise<TokenWebhook[]> {
    const list = await this.kv.list({ prefix: `${this.prefix}:` });
    const webhooks: TokenWebhook[] = [];

    for (const key of list.keys) {
      if (!key.name.includes(':event:')) {
        const data = await this.kv.get(key.name);
        if (data) {
          webhooks.push(JSON.parse(data));
        }
      }
    }

    return webhooks;
  }

  /**
   * Update webhook
   */
  async updateWebhook(
    id: string,
    updates: Partial<Pick<TokenWebhook, 'url' | 'events' | 'isActive' | 'metadata'>>
  ): Promise<TokenWebhook | null> {
    const webhook = await this.getWebhook(id);
    if (!webhook) return null;

    // If events changed, update indexes
    if (updates.events) {
      // Remove from old event indexes
      for (const event of webhook.events) {
        await this.removeWebhookFromEvent(event, id);
      }
      // Add to new event indexes
      for (const event of updates.events) {
        await this.addWebhookToEvent(event, id);
      }
    }

    const updated: TokenWebhook = {
      ...webhook,
      ...updates,
    };

    await this.kv.put(`${this.prefix}:${id}`, JSON.stringify(updated));
    return updated;
  }

  /**
   * Delete webhook
   */
  async deleteWebhook(id: string): Promise<boolean> {
    const webhook = await this.getWebhook(id);
    if (!webhook) return false;

    // Remove from event indexes
    for (const event of webhook.events) {
      await this.removeWebhookFromEvent(event, id);
    }

    await this.kv.delete(`${this.prefix}:${id}`);
    return true;
  }

  /**
   * Trigger webhooks for an event
   */
  async triggerEvent(
    event: TokenEventType,
    tokenId: string,
    tokenName?: string,
    details?: Record<string, unknown>
  ): Promise<void> {
    const webhookIds = await this.getWebhooksForEvent(event);

    const payload: TokenWebhookPayload = {
      event,
      timestamp: new Date().toISOString(),
      data: {
        tokenId,
        tokenName,
        details,
      },
    };

    // Trigger all webhooks in parallel
    await Promise.all(
      webhookIds.map(id => this.sendWebhook(id, payload))
    );
  }

  /**
   * Send webhook with retry logic
   */
  private async sendWebhook(webhookId: string, payload: TokenWebhookPayload): Promise<void> {
    const webhook = await this.getWebhook(webhookId);
    if (!webhook || !webhook.isActive) return;

    const signature = await this.generateSignature(payload, webhook.secret);

    for (let attempt = 0; attempt <= this.maxRetries; attempt++) {
      try {
        const response = await fetch(webhook.url, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-Noizylab-Signature': signature,
            'X-Noizylab-Event': payload.event,
            'X-Noizylab-Delivery': this.generateId('dlv'),
            'User-Agent': 'NOIZYLAB-Webhooks/1.0',
          },
          body: JSON.stringify(payload),
        });

        if (response.ok) {
          // Success - reset failure count
          webhook.failureCount = 0;
          webhook.lastTriggeredAt = new Date().toISOString();
          await this.kv.put(`${this.prefix}:${webhookId}`, JSON.stringify(webhook));
          return;
        }

        // Non-retryable status codes
        if (response.status >= 400 && response.status < 500) {
          console.error(`Webhook ${webhookId} failed with status ${response.status}`);
          break;
        }
      } catch (error) {
        console.error(`Webhook ${webhookId} failed:`, error);
      }

      // Wait before retry
      if (attempt < this.maxRetries) {
        await this.delay(this.retryDelays[attempt]);
      }
    }

    // All retries failed
    webhook.failureCount++;
    webhook.lastTriggeredAt = new Date().toISOString();

    // Disable webhook after too many failures
    if (webhook.failureCount >= 10) {
      webhook.isActive = false;
      console.warn(`Webhook ${webhookId} disabled after ${webhook.failureCount} failures`);
    }

    await this.kv.put(`${this.prefix}:${webhookId}`, JSON.stringify(webhook));
  }

  /**
   * Test webhook
   */
  async testWebhook(id: string): Promise<{
    success: boolean;
    statusCode?: number;
    responseTime?: number;
    error?: string;
  }> {
    const webhook = await this.getWebhook(id);
    if (!webhook) {
      return { success: false, error: 'Webhook not found' };
    }

    const testPayload: TokenWebhookPayload = {
      event: 'token.created',
      timestamp: new Date().toISOString(),
      data: {
        tokenId: 'test_token_id',
        tokenName: 'Test Token',
        details: { test: true },
      },
    };

    const signature = await this.generateSignature(testPayload, webhook.secret);
    const startTime = Date.now();

    try {
      const response = await fetch(webhook.url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-Noizylab-Signature': signature,
          'X-Noizylab-Event': 'test',
          'X-Noizylab-Test': 'true',
          'User-Agent': 'NOIZYLAB-Webhooks/1.0',
        },
        body: JSON.stringify(testPayload),
      });

      const responseTime = Date.now() - startTime;

      return {
        success: response.ok,
        statusCode: response.status,
        responseTime,
      };
    } catch (error) {
      return {
        success: false,
        error: error instanceof Error ? error.message : 'Unknown error',
        responseTime: Date.now() - startTime,
      };
    }
  }

  /**
   * Get webhook delivery history
   */
  async getDeliveryHistory(webhookId: string, limit = 20): Promise<Array<{
    id: string;
    event: TokenEventType;
    timestamp: string;
    success: boolean;
    statusCode?: number;
    responseTime?: number;
  }>> {
    const list = await this.kv.list({
      prefix: `${this.prefix}:delivery:${webhookId}:`,
      limit,
    });

    const deliveries: Array<{
      id: string;
      event: TokenEventType;
      timestamp: string;
      success: boolean;
      statusCode?: number;
      responseTime?: number;
    }> = [];

    for (const key of list.keys) {
      const data = await this.kv.get(key.name);
      if (data) {
        deliveries.push(JSON.parse(data));
      }
    }

    return deliveries.sort((a, b) =>
      new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime()
    );
  }

  // Private helpers

  private async addWebhookToEvent(event: TokenEventType, webhookId: string): Promise<void> {
    const key = `${this.prefix}:event:${event}`;
    const existing = await this.kv.get(key);
    const ids: string[] = existing ? JSON.parse(existing) : [];

    if (!ids.includes(webhookId)) {
      ids.push(webhookId);
      await this.kv.put(key, JSON.stringify(ids));
    }
  }

  private async removeWebhookFromEvent(event: TokenEventType, webhookId: string): Promise<void> {
    const key = `${this.prefix}:event:${event}`;
    const existing = await this.kv.get(key);

    if (existing) {
      const ids: string[] = JSON.parse(existing);
      const filtered = ids.filter(id => id !== webhookId);
      await this.kv.put(key, JSON.stringify(filtered));
    }
  }

  private async getWebhooksForEvent(event: TokenEventType): Promise<string[]> {
    const key = `${this.prefix}:event:${event}`;
    const data = await this.kv.get(key);
    return data ? JSON.parse(data) : [];
  }

  private async generateSignature(payload: TokenWebhookPayload, secret: string): Promise<string> {
    const encoder = new TextEncoder();
    const data = encoder.encode(JSON.stringify(payload));
    const key = await crypto.subtle.importKey(
      'raw',
      encoder.encode(secret),
      { name: 'HMAC', hash: 'SHA-256' },
      false,
      ['sign']
    );
    const signature = await crypto.subtle.sign('HMAC', key, data);
    return `sha256=${Array.from(new Uint8Array(signature))
      .map(b => b.toString(16).padStart(2, '0'))
      .join('')}`;
  }

  private generateId(prefix: string): string {
    const timestamp = Date.now().toString(36);
    const random = Math.random().toString(36).substring(2, 10);
    return `${prefix}_${timestamp}${random}`;
  }

  private generateSecret(): string {
    const array = new Uint8Array(32);
    crypto.getRandomValues(array);
    return `whsec_${Array.from(array, b => b.toString(16).padStart(2, '0')).join('')}`;
  }

  private delay(ms: number): Promise<void> {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
}

/**
 * Create token webhook service from environment
 */
export function createTokenWebhookService(env: Env): TokenWebhookService {
  return new TokenWebhookService(env.EMAIL_KV);
}

/**
 * Verify webhook signature
 */
export async function verifyWebhookSignature(
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
    ['sign']
  );

  const expectedSignature = await crypto.subtle.sign('HMAC', key, encoder.encode(payload));
  const expected = `sha256=${Array.from(new Uint8Array(expectedSignature))
    .map(b => b.toString(16).padStart(2, '0'))
    .join('')}`;

  return signature === expected;
}
