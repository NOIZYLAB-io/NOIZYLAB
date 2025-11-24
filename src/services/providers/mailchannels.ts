/**
 * NOIZYLAB Email System - MailChannels Provider
 * Free email sending for Cloudflare Workers via MailChannels API
 */

import type { EmailRequest, EmailAttachment } from '../../types';
import { ProviderError } from '../../errors';
import { generateMessageId, timeout } from '../../utils';
import { BaseEmailProvider, type SendOptions, type ProviderResponse } from './base';

/**
 * MailChannels API endpoint
 */
const MAILCHANNELS_API = 'https://api.mailchannels.net/tx/v1/send';

/**
 * MailChannels email personalization
 */
interface MailChannelsPersonalization {
  to: Array<{ email: string; name?: string }>;
  cc?: Array<{ email: string; name?: string }>;
  bcc?: Array<{ email: string; name?: string }>;
  dkim_domain?: string;
  dkim_selector?: string;
  dkim_private_key?: string;
}

/**
 * MailChannels request body
 */
interface MailChannelsRequest {
  personalizations: MailChannelsPersonalization[];
  from: { email: string; name?: string };
  reply_to?: { email: string; name?: string };
  subject: string;
  content: Array<{ type: string; value: string }>;
  headers?: Record<string, string>;
}

/**
 * MailChannels email provider
 */
export class MailChannelsProvider extends BaseEmailProvider {
  readonly name = 'mailchannels' as const;
  readonly supportsAttachments = false; // MailChannels free tier doesn't support attachments
  readonly supportsBcc = true;
  readonly maxRecipientsPerRequest = 1000;

  private readonly defaultDomain?: string;
  private readonly dkimPrivateKey?: string;
  private readonly dkimSelector?: string;
  private readonly dkimDomain?: string;

  constructor(config: {
    dkimPrivateKey?: string;
    dkimSelector?: string;
    dkimDomain?: string;
  } = {}) {
    super();
    this.dkimPrivateKey = config.dkimPrivateKey;
    this.dkimSelector = config.dkimSelector;
    this.dkimDomain = config.dkimDomain;
  }

  async send(email: EmailRequest, options?: SendOptions): Promise<ProviderResponse> {
    const messageId = generateMessageId();
    const startTime = Date.now();

    try {
      const request = this.buildRequest(email, options);

      const response = await timeout(
        fetch(MAILCHANNELS_API, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(request),
        }),
        options?.timeout ?? 30000,
        'MailChannels request timed out'
      );

      if (!response.ok) {
        const errorBody = await response.text();
        throw new ProviderError(
          this.name,
          `MailChannels API error: ${response.status} ${response.statusText}`,
          {
            statusCode: response.status,
            body: errorBody,
          }
        );
      }

      return {
        success: true,
        messageId,
        provider: this.name,
        rawResponse: {
          status: response.status,
          latencyMs: Date.now() - startTime,
        },
      };
    } catch (error) {
      if (error instanceof ProviderError) {
        throw error;
      }

      throw new ProviderError(
        this.name,
        error instanceof Error ? error.message : 'Unknown MailChannels error',
        { originalError: String(error) }
      );
    }
  }

  async healthCheck(): Promise<{ healthy: boolean; latencyMs: number; message?: string }> {
    const startTime = Date.now();

    try {
      // MailChannels doesn't have a dedicated health endpoint
      // We'll do a simple connectivity check
      const response = await timeout(
        fetch(MAILCHANNELS_API, {
          method: 'OPTIONS',
        }),
        5000,
        'Health check timed out'
      );

      return {
        healthy: response.status < 500,
        latencyMs: Date.now() - startTime,
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

    // DKIM is optional but recommended
    if (this.dkimPrivateKey !== undefined && this.dkimPrivateKey !== '') {
      if (this.dkimDomain === undefined || this.dkimDomain === '') {
        errors.push('DKIM domain is required when DKIM private key is provided');
      }
      if (this.dkimSelector === undefined || this.dkimSelector === '') {
        errors.push('DKIM selector is required when DKIM private key is provided');
      }
    }

    return {
      valid: errors.length === 0,
      errors,
    };
  }

  private buildRequest(email: EmailRequest, options?: SendOptions): MailChannelsRequest {
    const from = email.from ?? 'noreply@example.com';
    const headers = this.buildHeaders(email, options);

    const personalization: MailChannelsPersonalization = {
      to: this.formatRecipients(email.to),
    };

    if (email.cc !== undefined && email.cc.length > 0) {
      personalization.cc = this.formatRecipients(email.cc);
    }

    if (email.bcc !== undefined && email.bcc.length > 0) {
      personalization.bcc = this.formatRecipients(email.bcc);
    }

    // Add DKIM configuration
    const dkim = options?.dkim;
    if (dkim !== undefined) {
      personalization.dkim_domain = dkim.domain;
      personalization.dkim_selector = dkim.selector;
      personalization.dkim_private_key = dkim.privateKey;
    } else if (this.dkimPrivateKey !== undefined) {
      personalization.dkim_domain = this.dkimDomain;
      personalization.dkim_selector = this.dkimSelector;
      personalization.dkim_private_key = this.dkimPrivateKey;
    }

    const content: Array<{ type: string; value: string }> = [];

    if (email.text !== undefined) {
      content.push({ type: 'text/plain', value: email.text });
    }

    if (email.html !== undefined) {
      content.push({ type: 'text/html', value: email.html });
    }

    const request: MailChannelsRequest = {
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

    return request;
  }
}

/**
 * Create MailChannels provider from environment
 */
export function createMailChannelsProvider(env: Env): MailChannelsProvider {
  return new MailChannelsProvider({
    dkimPrivateKey: env.DKIM_PRIVATE_KEY,
    dkimSelector: env.DKIM_SELECTOR,
    dkimDomain: env.DKIM_DOMAIN,
  });
}
