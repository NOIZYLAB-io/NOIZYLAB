/**
 * NOIZYLAB Email System - SendGrid Provider
 * Email sending via SendGrid API
 */

import type { EmailRequest, EmailAttachment } from '../../types';
import { ProviderError, AuthenticationError } from '../../errors';
import { generateMessageId, timeout } from '../../utils';
import { BaseEmailProvider, type SendOptions, type ProviderResponse } from './base';

/**
 * SendGrid API endpoint
 */
const SENDGRID_API = 'https://api.sendgrid.com/v3/mail/send';

/**
 * SendGrid personalization
 */
interface SendGridPersonalization {
  to: Array<{ email: string }>;
  cc?: Array<{ email: string }>;
  bcc?: Array<{ email: string }>;
}

/**
 * SendGrid attachment format
 */
interface SendGridAttachment {
  content: string;
  filename: string;
  type: string;
  disposition: 'attachment' | 'inline';
}

/**
 * SendGrid request body
 */
interface SendGridRequest {
  personalizations: SendGridPersonalization[];
  from: { email: string };
  reply_to?: { email: string };
  subject: string;
  content: Array<{ type: string; value: string }>;
  attachments?: SendGridAttachment[];
  headers?: Record<string, string>;
  categories?: string[];
  mail_settings?: {
    sandbox_mode?: { enable: boolean };
  };
}

/**
 * SendGrid email provider
 */
export class SendGridProvider extends BaseEmailProvider {
  readonly name = 'sendgrid' as const;
  readonly supportsAttachments = true;
  readonly supportsBcc = true;
  readonly maxRecipientsPerRequest = 1000;

  private readonly apiKey: string;
  private readonly sandboxMode: boolean;

  constructor(apiKey: string, options: { sandboxMode?: boolean } = {}) {
    super();
    this.apiKey = apiKey;
    this.sandboxMode = options.sandboxMode ?? false;
  }

  async send(email: EmailRequest, options?: SendOptions): Promise<ProviderResponse> {
    const messageId = generateMessageId();
    const startTime = Date.now();

    try {
      const request = this.buildRequest(email, options);

      const response = await timeout(
        fetch(SENDGRID_API, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${this.apiKey}`,
          },
          body: JSON.stringify(request),
        }),
        options?.timeout ?? 30000,
        'SendGrid request timed out'
      );

      if (!response.ok) {
        if (response.status === 401 || response.status === 403) {
          throw new AuthenticationError('Invalid SendGrid API key');
        }

        const errorBody = await response.text();
        throw new ProviderError(
          this.name,
          `SendGrid API error: ${response.status} ${response.statusText}`,
          {
            statusCode: response.status,
            body: errorBody,
          }
        );
      }

      // SendGrid returns message ID in header
      const sgMessageId = response.headers.get('X-Message-Id');

      return {
        success: true,
        messageId: sgMessageId ?? messageId,
        provider: this.name,
        rawResponse: {
          status: response.status,
          messageId: sgMessageId,
          latencyMs: Date.now() - startTime,
        },
      };
    } catch (error) {
      if (error instanceof ProviderError || error instanceof AuthenticationError) {
        throw error;
      }

      throw new ProviderError(
        this.name,
        error instanceof Error ? error.message : 'Unknown SendGrid error',
        { originalError: String(error) }
      );
    }
  }

  async healthCheck(): Promise<{ healthy: boolean; latencyMs: number; message?: string }> {
    const startTime = Date.now();

    try {
      // Check API key by getting user profile
      const response = await timeout(
        fetch('https://api.sendgrid.com/v3/user/profile', {
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
      errors.push('SendGrid API key is required');
    } else if (!this.apiKey.startsWith('SG.')) {
      errors.push('Invalid SendGrid API key format (should start with "SG.")');
    }

    return {
      valid: errors.length === 0,
      errors,
    };
  }

  private buildRequest(email: EmailRequest, options?: SendOptions): SendGridRequest {
    const from = email.from ?? 'noreply@example.com';
    const headers = this.buildHeaders(email, options);

    const personalization: SendGridPersonalization = {
      to: this.formatRecipients(email.to),
    };

    if (email.cc !== undefined && email.cc.length > 0) {
      personalization.cc = this.formatRecipients(email.cc);
    }

    if (email.bcc !== undefined && email.bcc.length > 0) {
      personalization.bcc = this.formatRecipients(email.bcc);
    }

    const content: Array<{ type: string; value: string }> = [];

    if (email.text !== undefined) {
      content.push({ type: 'text/plain', value: email.text });
    }

    if (email.html !== undefined) {
      content.push({ type: 'text/html', value: email.html });
    }

    const request: SendGridRequest = {
      personalizations: [personalization],
      from: { email: from },
      subject: email.subject,
      content,
    };

    if (email.replyTo !== undefined) {
      request.reply_to = { email: email.replyTo };
    }

    if (Object.keys(headers).length > 0) {
      request.headers = headers;
    }

    if (email.attachments !== undefined && email.attachments.length > 0) {
      request.attachments = email.attachments.map((att) => ({
        content: att.content,
        filename: att.filename,
        type: att.contentType,
        disposition: 'attachment' as const,
      }));
    }

    if (email.tags !== undefined && email.tags.length > 0) {
      request.categories = email.tags;
    }

    if (this.sandboxMode) {
      request.mail_settings = {
        sandbox_mode: { enable: true },
      };
    }

    return request;
  }
}

/**
 * Create SendGrid provider from environment
 */
export function createSendGridProvider(
  env: Env,
  options: { sandboxMode?: boolean } = {}
): SendGridProvider | null {
  if (env.SENDGRID_API_KEY === undefined || env.SENDGRID_API_KEY === '') {
    return null;
  }
  return new SendGridProvider(env.SENDGRID_API_KEY, options);
}
