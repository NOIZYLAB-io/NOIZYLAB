/**
 * NOIZYLAB Email System - Email Service
 * Main service orchestrating email sending, templates, and logging
 */

import type {
  EmailRequest,
  EmailResponse,
  EmailLog,
  EmailStatus,
  EmailProvider,
  RateLimitResult,
} from '../types';
import { EmailRequestSchema } from '../types';
import {
  ValidationError,
  IdempotencyConflictError,
  InternalError,
  isNoizylabError,
  toNoizylabError,
} from '../errors';
import {
  generateMessageId,
  generateRequestId,
  normalizeEmailList,
  now,
  retryWithBackoff,
} from '../utils';
import { RateLimiter } from './rate-limiter';
import { TemplateEngine } from './template-engine';
import {
  type BaseEmailProvider,
  type ProviderRegistry,
  type ProviderResponse,
  getDefaultProvider,
  getProvider,
} from './providers';

/**
 * Email service configuration
 */
export interface EmailServiceConfig {
  defaultFromEmail: string;
  maxRetries: number;
  retryDelayMs: number;
  idempotencyTtlSeconds: number;
}

/**
 * Email service options for sending
 */
export interface SendEmailOptions {
  provider?: EmailProvider;
  skipRateLimit?: boolean;
  skipIdempotency?: boolean;
}

/**
 * Main email service class
 */
export class EmailService {
  private readonly providers: ProviderRegistry;
  private readonly rateLimiter: RateLimiter;
  private readonly templateEngine: TemplateEngine;
  private readonly kv: KVNamespace;
  private readonly db: D1Database;
  private readonly config: EmailServiceConfig;

  constructor(
    providers: ProviderRegistry,
    rateLimiter: RateLimiter,
    templateEngine: TemplateEngine,
    kv: KVNamespace,
    db: D1Database,
    config: EmailServiceConfig
  ) {
    this.providers = providers;
    this.rateLimiter = rateLimiter;
    this.templateEngine = templateEngine;
    this.kv = kv;
    this.db = db;
    this.config = config;
  }

  /**
   * Send an email
   */
  async send(
    request: EmailRequest,
    clientId: string,
    options: SendEmailOptions = {}
  ): Promise<{ response: EmailResponse; rateLimit: RateLimitResult }> {
    const messageId = generateMessageId();
    const timestamp = now();

    // Validate request
    const validation = EmailRequestSchema.safeParse(request);
    if (!validation.success) {
      throw new ValidationError('Invalid email request', {
        errors: validation.error.errors.map((e) => ({
          path: e.path.join('.'),
          message: e.message,
        })),
      });
    }

    const email = validation.data;

    // Check idempotency
    if (email.idempotencyKey !== undefined && options.skipIdempotency !== true) {
      const existingMessageId = await this.checkIdempotency(email.idempotencyKey);
      if (existingMessageId !== null) {
        throw new IdempotencyConflictError(email.idempotencyKey, existingMessageId);
      }
    }

    // Check rate limit
    let rateLimitResult: RateLimitResult;
    if (options.skipRateLimit !== true) {
      rateLimitResult = await this.rateLimiter.consume(clientId);
    } else {
      rateLimitResult = await this.rateLimiter.check(clientId);
    }

    // Process template if specified
    let processedEmail = email;
    if (email.templateId !== undefined) {
      const rendered = await this.templateEngine.renderById(
        email.templateId,
        email.templateData ?? {}
      );
      processedEmail = {
        ...email,
        subject: rendered.subject,
        html: rendered.html,
        text: rendered.text,
      };
    }

    // Set default from address
    if (processedEmail.from === undefined) {
      processedEmail = {
        ...processedEmail,
        from: this.config.defaultFromEmail,
      };
    }

    // Get provider
    const provider = options.provider !== undefined
      ? getProvider(this.providers, options.provider)
      : getDefaultProvider(this.providers);

    if (provider === undefined) {
      throw new InternalError(`Provider not available: ${options.provider}`);
    }

    // Handle scheduled emails
    if (email.scheduledAt !== undefined) {
      const scheduledDate = new Date(email.scheduledAt);
      if (scheduledDate > new Date()) {
        await this.scheduleEmail(messageId, processedEmail, scheduledDate);

        const response: EmailResponse = {
          success: true,
          messageId,
          status: 'scheduled',
          timestamp,
        };

        return { response, rateLimit: rateLimitResult };
      }
    }

    // Send email with retry
    let providerResponse: ProviderResponse;
    try {
      providerResponse = await retryWithBackoff(
        () => provider.send(processedEmail),
        {
          maxRetries: this.config.maxRetries,
          baseDelayMs: this.config.retryDelayMs,
        }
      );
    } catch (error) {
      // Log failed email
      await this.logEmail({
        id: generateRequestId(),
        messageId,
        to: normalizeEmailList(processedEmail.to),
        from: processedEmail.from ?? this.config.defaultFromEmail,
        subject: processedEmail.subject,
        status: 'failed',
        provider: provider.name,
        templateId: email.templateId,
        tags: email.tags,
        errorMessage: error instanceof Error ? error.message : String(error),
        createdAt: timestamp,
        updatedAt: timestamp,
      });

      throw toNoizylabError(error);
    }

    // Store idempotency key
    if (email.idempotencyKey !== undefined) {
      await this.storeIdempotencyKey(email.idempotencyKey, providerResponse.messageId ?? messageId);
    }

    // Log successful email
    await this.logEmail({
      id: generateRequestId(),
      messageId: providerResponse.messageId ?? messageId,
      to: normalizeEmailList(processedEmail.to),
      from: processedEmail.from ?? this.config.defaultFromEmail,
      subject: processedEmail.subject,
      status: 'sent',
      provider: provider.name,
      templateId: email.templateId,
      tags: email.tags,
      sentAt: timestamp,
      createdAt: timestamp,
      updatedAt: timestamp,
    });

    const response: EmailResponse = {
      success: true,
      messageId: providerResponse.messageId ?? messageId,
      status: 'sent',
      timestamp,
    };

    return { response, rateLimit: rateLimitResult };
  }

  /**
   * Get email log by message ID
   */
  async getEmailLog(messageId: string): Promise<EmailLog | null> {
    try {
      const result = await this.db
        .prepare('SELECT * FROM email_logs WHERE message_id = ?')
        .bind(messageId)
        .first();

      if (result === null) {
        return null;
      }

      return this.parseEmailLog(result);
    } catch {
      return null;
    }
  }

  /**
   * List email logs with pagination
   */
  async listEmailLogs(options: {
    limit?: number;
    offset?: number;
    status?: EmailStatus;
    from?: string;
    to?: string;
  } = {}): Promise<{ logs: EmailLog[]; total: number }> {
    const { limit = 50, offset = 0, status, from, to } = options;

    let query = 'SELECT * FROM email_logs WHERE 1=1';
    const params: unknown[] = [];

    if (status !== undefined) {
      query += ' AND status = ?';
      params.push(status);
    }

    if (from !== undefined) {
      query += ' AND from_address = ?';
      params.push(from);
    }

    if (to !== undefined) {
      query += ' AND to_addresses LIKE ?';
      params.push(`%${to}%`);
    }

    query += ' ORDER BY created_at DESC LIMIT ? OFFSET ?';
    params.push(limit, offset);

    try {
      const results = await this.db
        .prepare(query)
        .bind(...params)
        .all();

      const countResult = await this.db
        .prepare('SELECT COUNT(*) as count FROM email_logs')
        .first<{ count: number }>();

      const logs = (results.results ?? []).map((row) => this.parseEmailLog(row));

      return {
        logs,
        total: countResult?.count ?? 0,
      };
    } catch {
      return { logs: [], total: 0 };
    }
  }

  /**
   * Update email status (for webhooks)
   */
  async updateEmailStatus(
    messageId: string,
    status: EmailStatus,
    metadata?: Record<string, unknown>
  ): Promise<void> {
    const timestamp = now();
    const statusField = status === 'delivered' ? 'delivered_at' : status === 'bounced' ? 'bounced_at' : null;

    let query = 'UPDATE email_logs SET status = ?, updated_at = ?';
    const params: unknown[] = [status, timestamp];

    if (statusField !== null) {
      query += `, ${statusField} = ?`;
      params.push(timestamp);
    }

    if (metadata !== undefined) {
      query += ', metadata = ?';
      params.push(JSON.stringify(metadata));
    }

    query += ' WHERE message_id = ?';
    params.push(messageId);

    await this.db.prepare(query).bind(...params).run();
  }

  /**
   * Check rate limit status for a client
   */
  async getRateLimitStatus(clientId: string): Promise<RateLimitResult> {
    return this.rateLimiter.getStatus(clientId);
  }

  /**
   * Health check for all providers
   */
  async healthCheck(): Promise<Record<string, { healthy: boolean; latencyMs: number; message?: string }>> {
    const results: Record<string, { healthy: boolean; latencyMs: number; message?: string }> = {};

    for (const [name, provider] of Object.entries(this.providers)) {
      if (provider !== undefined) {
        results[name] = await provider.healthCheck();
      }
    }

    return results;
  }

  private async checkIdempotency(key: string): Promise<string | null> {
    const stored = await this.kv.get(`idempotency:${key}`);
    return stored;
  }

  private async storeIdempotencyKey(key: string, messageId: string): Promise<void> {
    await this.kv.put(`idempotency:${key}`, messageId, {
      expirationTtl: this.config.idempotencyTtlSeconds,
    });
  }

  private async scheduleEmail(messageId: string, email: EmailRequest, scheduledAt: Date): Promise<void> {
    await this.kv.put(
      `scheduled:${messageId}`,
      JSON.stringify({ email, scheduledAt: scheduledAt.toISOString() }),
      {
        expirationTtl: Math.ceil((scheduledAt.getTime() - Date.now()) / 1000) + 86400,
      }
    );
  }

  private async logEmail(log: EmailLog): Promise<void> {
    try {
      await this.db
        .prepare(
          `INSERT INTO email_logs (
            id, message_id, to_addresses, from_address, subject, status,
            provider, template_id, tags, metadata, error_message,
            sent_at, delivered_at, bounced_at, created_at, updated_at
          ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`
        )
        .bind(
          log.id,
          log.messageId,
          JSON.stringify(log.to),
          log.from,
          log.subject,
          log.status,
          log.provider,
          log.templateId ?? null,
          log.tags !== undefined ? JSON.stringify(log.tags) : null,
          log.metadata !== undefined ? JSON.stringify(log.metadata) : null,
          log.errorMessage ?? null,
          log.sentAt ?? null,
          log.deliveredAt ?? null,
          log.bouncedAt ?? null,
          log.createdAt,
          log.updatedAt
        )
        .run();
    } catch (error) {
      // Log error but don't fail the request
      console.error('Failed to log email:', error);
    }
  }

  private parseEmailLog(row: Record<string, unknown>): EmailLog {
    return {
      id: String(row['id']),
      messageId: String(row['message_id']),
      to: JSON.parse(String(row['to_addresses'])) as string[],
      from: String(row['from_address']),
      subject: String(row['subject']),
      status: String(row['status']) as EmailStatus,
      provider: String(row['provider']) as EmailProvider,
      templateId: row['template_id'] !== null ? String(row['template_id']) : undefined,
      tags: row['tags'] !== null ? JSON.parse(String(row['tags'])) as string[] : undefined,
      metadata: row['metadata'] !== null ? JSON.parse(String(row['metadata'])) as Record<string, unknown> : undefined,
      errorMessage: row['error_message'] !== null ? String(row['error_message']) : undefined,
      sentAt: row['sent_at'] !== null ? String(row['sent_at']) : undefined,
      deliveredAt: row['delivered_at'] !== null ? String(row['delivered_at']) : undefined,
      bouncedAt: row['bounced_at'] !== null ? String(row['bounced_at']) : undefined,
      createdAt: String(row['created_at']),
      updatedAt: String(row['updated_at']),
    };
  }
}

/**
 * Create email service from environment
 */
export function createEmailService(
  providers: ProviderRegistry,
  rateLimiter: RateLimiter,
  templateEngine: TemplateEngine,
  env: Env
): EmailService {
  const config: EmailServiceConfig = {
    defaultFromEmail: env.DEFAULT_FROM_EMAIL,
    maxRetries: 3,
    retryDelayMs: 1000,
    idempotencyTtlSeconds: 86400, // 24 hours
  };

  return new EmailService(
    providers,
    rateLimiter,
    templateEngine,
    env.EMAIL_KV,
    env.EMAIL_DB,
    config
  );
}
