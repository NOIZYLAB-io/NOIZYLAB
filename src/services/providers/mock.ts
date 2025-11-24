/**
 * NOIZYLAB Email System - Mock Provider
 * Mock email provider for testing purposes
 */

import type { EmailRequest } from '../../types';
import { ProviderError } from '../../errors';
import { generateMessageId, sleep } from '../../utils';
import { BaseEmailProvider, type SendOptions, type ProviderResponse } from './base';

/**
 * Sent email record for testing assertions
 */
export interface MockSentEmail {
  id: string;
  email: EmailRequest;
  timestamp: string;
  options?: SendOptions;
}

/**
 * Mock provider configuration
 */
export interface MockProviderConfig {
  /** Simulate network latency in ms */
  latencyMs?: number;
  /** Probability of failure (0-1) */
  failureRate?: number;
  /** Custom failure message */
  failureMessage?: string;
  /** Whether to store sent emails */
  recordEmails?: boolean;
}

/**
 * Mock email provider for testing
 */
export class MockProvider extends BaseEmailProvider {
  readonly name = 'mock' as const;
  readonly supportsAttachments = true;
  readonly supportsBcc = true;
  readonly maxRecipientsPerRequest = 1000;

  private readonly config: Required<MockProviderConfig>;
  private sentEmails: MockSentEmail[] = [];
  private sendCount = 0;
  private failCount = 0;

  constructor(config: MockProviderConfig = {}) {
    super();
    this.config = {
      latencyMs: config.latencyMs ?? 0,
      failureRate: config.failureRate ?? 0,
      failureMessage: config.failureMessage ?? 'Mock provider simulated failure',
      recordEmails: config.recordEmails ?? true,
    };
  }

  async send(email: EmailRequest, options?: SendOptions): Promise<ProviderResponse> {
    this.sendCount++;

    // Simulate latency
    if (this.config.latencyMs > 0) {
      await sleep(this.config.latencyMs);
    }

    // Simulate failure
    if (this.config.failureRate > 0 && Math.random() < this.config.failureRate) {
      this.failCount++;
      throw new ProviderError(this.name, this.config.failureMessage, {
        simulated: true,
        failureRate: this.config.failureRate,
      });
    }

    const messageId = generateMessageId();

    // Record email
    if (this.config.recordEmails) {
      this.sentEmails.push({
        id: messageId,
        email,
        timestamp: new Date().toISOString(),
        options,
      });
    }

    return {
      success: true,
      messageId,
      provider: this.name,
      rawResponse: {
        mock: true,
        sendCount: this.sendCount,
      },
    };
  }

  async healthCheck(): Promise<{ healthy: boolean; latencyMs: number; message?: string }> {
    const startTime = Date.now();

    if (this.config.latencyMs > 0) {
      await sleep(Math.min(this.config.latencyMs, 100));
    }

    return {
      healthy: true,
      latencyMs: Date.now() - startTime,
      message: 'Mock provider is always healthy',
    };
  }

  validateConfig(): { valid: boolean; errors: string[] } {
    const errors: string[] = [];

    if (this.config.failureRate < 0 || this.config.failureRate > 1) {
      errors.push('Failure rate must be between 0 and 1');
    }

    if (this.config.latencyMs < 0) {
      errors.push('Latency must be non-negative');
    }

    return {
      valid: errors.length === 0,
      errors,
    };
  }

  // Testing utilities

  /**
   * Get all sent emails
   */
  getSentEmails(): MockSentEmail[] {
    return [...this.sentEmails];
  }

  /**
   * Get last sent email
   */
  getLastEmail(): MockSentEmail | undefined {
    return this.sentEmails[this.sentEmails.length - 1];
  }

  /**
   * Find emails by recipient
   */
  findEmailsByRecipient(recipient: string): MockSentEmail[] {
    return this.sentEmails.filter((sent) => {
      const recipients = Array.isArray(sent.email.to) ? sent.email.to : [sent.email.to];
      return recipients.includes(recipient);
    });
  }

  /**
   * Find emails by subject (partial match)
   */
  findEmailsBySubject(subject: string): MockSentEmail[] {
    return this.sentEmails.filter((sent) =>
      sent.email.subject.toLowerCase().includes(subject.toLowerCase())
    );
  }

  /**
   * Get send count
   */
  getSendCount(): number {
    return this.sendCount;
  }

  /**
   * Get failure count
   */
  getFailCount(): number {
    return this.failCount;
  }

  /**
   * Clear all recorded emails
   */
  clear(): void {
    this.sentEmails = [];
    this.sendCount = 0;
    this.failCount = 0;
  }

  /**
   * Set failure rate dynamically
   */
  setFailureRate(rate: number): void {
    this.config.failureRate = Math.max(0, Math.min(1, rate));
  }

  /**
   * Set latency dynamically
   */
  setLatency(ms: number): void {
    this.config.latencyMs = Math.max(0, ms);
  }
}

/**
 * Create mock provider with default config
 */
export function createMockProvider(config?: MockProviderConfig): MockProvider {
  return new MockProvider(config);
}
