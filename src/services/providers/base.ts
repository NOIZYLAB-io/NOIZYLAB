/**
 * NOIZYLAB Email System - Base Email Provider
 * Abstract base class for email providers
 */

import type { EmailRequest, EmailResponse, EmailProvider, DKIMConfig } from '../../types';

/**
 * Email sending options
 */
export interface SendOptions {
  dkim?: DKIMConfig;
  timeout?: number;
}

/**
 * Provider-specific response
 */
export interface ProviderResponse {
  success: boolean;
  messageId?: string;
  provider: EmailProvider;
  rawResponse?: unknown;
  error?: {
    code: string;
    message: string;
  };
}

/**
 * Abstract base class for email providers
 */
export abstract class BaseEmailProvider {
  abstract readonly name: EmailProvider;
  abstract readonly supportsAttachments: boolean;
  abstract readonly supportsBcc: boolean;
  abstract readonly maxRecipientsPerRequest: number;

  /**
   * Send an email
   */
  abstract send(email: EmailRequest, options?: SendOptions): Promise<ProviderResponse>;

  /**
   * Check provider health/availability
   */
  abstract healthCheck(): Promise<{ healthy: boolean; latencyMs: number; message?: string }>;

  /**
   * Validate provider configuration
   */
  abstract validateConfig(): { valid: boolean; errors: string[] };

  /**
   * Build email headers including DKIM if configured
   */
  protected buildHeaders(
    email: EmailRequest,
    options?: SendOptions
  ): Record<string, string> {
    const headers: Record<string, string> = {
      ...email.headers,
    };

    if (email.priority === 'high') {
      headers['X-Priority'] = '1';
      headers['X-MSMail-Priority'] = 'High';
      headers['Importance'] = 'High';
    } else if (email.priority === 'low') {
      headers['X-Priority'] = '5';
      headers['X-MSMail-Priority'] = 'Low';
      headers['Importance'] = 'Low';
    }

    return headers;
  }

  /**
   * Normalize recipients to array
   */
  protected normalizeRecipients(recipients: string | string[]): string[] {
    return Array.isArray(recipients) ? recipients : [recipients];
  }

  /**
   * Format recipient for API calls
   */
  protected formatRecipient(email: string): { email: string } {
    return { email };
  }

  /**
   * Format recipients list
   */
  protected formatRecipients(recipients: string | string[]): Array<{ email: string }> {
    return this.normalizeRecipients(recipients).map(this.formatRecipient);
  }
}
