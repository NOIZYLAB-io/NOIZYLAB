/**
 * NOIZYLAB Email System - Resend Provider
 * Email sending via Resend API (modern email API)
 */

import type { EmailRequest, EmailAttachment } from '../../types';
import { ProviderError, AuthenticationError } from '../../errors';
import { generateMessageId, timeout } from '../../utils';
import { BaseEmailProvider, type SendOptions, type ProviderResponse } from './base';

/**
 * Resend API endpoint
 */
const RESEND_API = 'https://api.resend.com/emails';

/**
 * Resend attachment format
 */
interface ResendAttachment {
  filename: string;
  content: string;
}

/**
 * Resend request body
 */
interface ResendRequest {
  from: string;
  to: string | string[];
  subject: string;
  html?: string;
  text?: string;
  cc?: string[];
  bcc?: string[];
  reply_to?: string;
  headers?: Record<string, string>;
  attachments?: ResendAttachment[];
  tags?: Array<{ name: string; value: string }>;
}

/**
 * Resend API response
 */
interface ResendResponse {
  id?: string;
  error?: {
    message: string;
    name: string;
  };
}

/**
 * Resend email provider
 */
export class ResendProvider extends BaseEmailProvider {
  readonly name = 'resend' as const;
  readonly supportsAttachments = true;
  readonly supportsBcc = true;
  readonly maxRecipientsPerRequest = 50;

  private readonly apiKey: string;

  constructor(apiKey: string) {
    super();
    this.apiKey = apiKey;
  }

  async send(email: EmailRequest, options?: SendOptions): Promise<ProviderResponse> {
    const startTime = Date.now();

    try {
      const request = this.buildRequest(email);

      const response = await timeout(
        fetch(RESEND_API, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${this.apiKey}`,
          },
          body: JSON.stringify(request),
        }),
        options?.timeout ?? 30000,
        'Resend request timed out'
      );

      const data = (await response.json()) as ResendResponse;

      if (!response.ok) {
        if (response.status === 401 || response.status === 403) {
          throw new AuthenticationError('Invalid Resend API key');
        }

        throw new ProviderError(
          this.name,
          data.error?.message ?? `Resend API error: ${response.status}`,
          {
            statusCode: response.status,
            errorName: data.error?.name,
          }
        );
      }

      return {
        success: true,
        messageId: data.id ?? generateMessageId(),
        provider: this.name,
        rawResponse: {
          id: data.id,
          latencyMs: Date.now() - startTime,
        },
      };
    } catch (error) {
      if (error instanceof ProviderError || error instanceof AuthenticationError) {
        throw error;
      }

      throw new ProviderError(
        this.name,
        error instanceof Error ? error.message : 'Unknown Resend error',
        { originalError: String(error) }
      );
    }
  }

  async healthCheck(): Promise<{ healthy: boolean; latencyMs: number; message?: string }> {
    const startTime = Date.now();

    try {
      // Check API key validity by listing emails (minimal data)
      const response = await timeout(
        fetch('https://api.resend.com/emails?limit=1', {
          method: 'GET',
          headers: {
            Authorization: `Bearer ${this.apiKey}`,
          },
        }),
        5000,
        'Health check timed out'
      );

      return {
        healthy: response.ok,
        latencyMs: Date.now() - startTime,
        message: response.ok ? undefined : `API returned ${response.status}`,
      };
    } catch (error) {
      return {
        healthy: false,
        latencyMs: Date.now() - startTime,
        message: error instanceof Error ? error.message : 'Unknown error',
      };
    }
  }

  validateConfig(): { valid: boolean; errors: string[] } {
    const errors: string[] = [];

    if (this.apiKey === '' || this.apiKey === undefined) {
      errors.push('Resend API key is required');
    } else if (!this.apiKey.startsWith('re_')) {
      errors.push('Invalid Resend API key format (should start with "re_")');
    }

    return {
      valid: errors.length === 0,
      errors,
    };
  }

  private buildRequest(email: EmailRequest): ResendRequest {
    const from = email.from ?? 'noreply@example.com';

    const request: ResendRequest = {
      from,
      to: email.to,
      subject: email.subject,
    };

    if (email.html !== undefined) {
      request.html = email.html;
    }

    if (email.text !== undefined) {
      request.text = email.text;
    }

    if (email.cc !== undefined && email.cc.length > 0) {
      request.cc = email.cc;
    }

    if (email.bcc !== undefined && email.bcc.length > 0) {
      request.bcc = email.bcc;
    }

    if (email.replyTo !== undefined) {
      request.reply_to = email.replyTo;
    }

    if (email.headers !== undefined && Object.keys(email.headers).length > 0) {
      request.headers = email.headers;
    }

    if (email.attachments !== undefined && email.attachments.length > 0) {
      request.attachments = email.attachments.map((att) => ({
        filename: att.filename,
        content: att.content,
      }));
    }

    if (email.tags !== undefined && email.tags.length > 0) {
      request.tags = email.tags.map((tag) => ({ name: tag, value: 'true' }));
    }

    return request;
  }
}

/**
 * Create Resend provider from environment
 */
export function createResendProvider(env: Env): ResendProvider | null {
  if (env.RESEND_API_KEY === undefined || env.RESEND_API_KEY === '') {
    return null;
  }
  return new ResendProvider(env.RESEND_API_KEY);
}
