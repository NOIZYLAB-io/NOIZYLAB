/**
 * NOIZYLAB Email System - Email Providers Unit Tests
 */

import { describe, it, expect, beforeEach, vi } from 'vitest';
import { MockProvider, createMockProvider } from '../../src/services/providers/mock';
import { MailChannelsProvider } from '../../src/services/providers/mailchannels';
import { ResendProvider } from '../../src/services/providers/resend';
import { SendGridProvider } from '../../src/services/providers/sendgrid';
import { ProviderError, AuthenticationError } from '../../src/errors';
import type { EmailRequest } from '../../src/types';

describe('MockProvider', () => {
  let provider: MockProvider;

  beforeEach(() => {
    provider = new MockProvider({ recordEmails: true });
  });

  describe('send', () => {
    it('should send email successfully', async () => {
      const email: EmailRequest = {
        to: 'test@example.com',
        subject: 'Test Subject',
        text: 'Test body',
      };

      const result = await provider.send(email);

      expect(result.success).toBe(true);
      expect(result.messageId).toBeDefined();
      expect(result.provider).toBe('mock');
    });

    it('should record sent emails', async () => {
      const email: EmailRequest = {
        to: 'test@example.com',
        subject: 'Test Subject',
        text: 'Test body',
      };

      await provider.send(email);

      const sentEmails = provider.getSentEmails();
      expect(sentEmails).toHaveLength(1);
      expect(sentEmails[0]?.email.to).toBe('test@example.com');
    });

    it('should simulate latency', async () => {
      const slowProvider = new MockProvider({ latencyMs: 100 });

      const start = Date.now();
      await slowProvider.send({
        to: 'test@example.com',
        subject: 'Test',
        text: 'Test',
      });
      const duration = Date.now() - start;

      expect(duration).toBeGreaterThanOrEqual(90);
    });

    it('should simulate failures', async () => {
      const failingProvider = new MockProvider({ failureRate: 1.0 });

      await expect(
        failingProvider.send({
          to: 'test@example.com',
          subject: 'Test',
          text: 'Test',
        })
      ).rejects.toThrow(ProviderError);
    });
  });

  describe('getSentEmails', () => {
    it('should return all sent emails', async () => {
      await provider.send({ to: 'a@test.com', subject: 'A', text: 'A' });
      await provider.send({ to: 'b@test.com', subject: 'B', text: 'B' });
      await provider.send({ to: 'c@test.com', subject: 'C', text: 'C' });

      expect(provider.getSentEmails()).toHaveLength(3);
    });
  });

  describe('getLastEmail', () => {
    it('should return the last sent email', async () => {
      await provider.send({ to: 'first@test.com', subject: 'First', text: '' });
      await provider.send({ to: 'last@test.com', subject: 'Last', text: '' });

      const last = provider.getLastEmail();
      expect(last?.email.to).toBe('last@test.com');
    });

    it('should return undefined when no emails sent', () => {
      expect(provider.getLastEmail()).toBeUndefined();
    });
  });

  describe('findEmailsByRecipient', () => {
    it('should find emails by recipient', async () => {
      await provider.send({ to: 'alice@test.com', subject: 'For Alice', text: '' });
      await provider.send({ to: 'bob@test.com', subject: 'For Bob', text: '' });
      await provider.send({ to: 'alice@test.com', subject: 'Also for Alice', text: '' });

      const aliceEmails = provider.findEmailsByRecipient('alice@test.com');
      expect(aliceEmails).toHaveLength(2);
    });

    it('should handle array recipients', async () => {
      await provider.send({
        to: ['alice@test.com', 'bob@test.com'],
        subject: 'Group',
        text: '',
      });

      const aliceEmails = provider.findEmailsByRecipient('alice@test.com');
      expect(aliceEmails).toHaveLength(1);
    });
  });

  describe('findEmailsBySubject', () => {
    it('should find emails by subject (case insensitive)', async () => {
      await provider.send({ to: 'test@test.com', subject: 'Welcome Email', text: '' });
      await provider.send({ to: 'test@test.com', subject: 'Password Reset', text: '' });
      await provider.send({ to: 'test@test.com', subject: 'Welcome Back', text: '' });

      const welcomeEmails = provider.findEmailsBySubject('welcome');
      expect(welcomeEmails).toHaveLength(2);
    });
  });

  describe('getSendCount and getFailCount', () => {
    it('should track send and fail counts', async () => {
      const mixedProvider = new MockProvider({ failureRate: 0.5 });

      let sends = 0;
      let fails = 0;

      for (let i = 0; i < 20; i++) {
        try {
          await mixedProvider.send({ to: 'test@test.com', subject: 'Test', text: '' });
          sends++;
        } catch {
          fails++;
        }
      }

      expect(mixedProvider.getSendCount()).toBe(20);
      expect(mixedProvider.getFailCount()).toBe(fails);
    });
  });

  describe('clear', () => {
    it('should clear all recorded data', async () => {
      await provider.send({ to: 'test@test.com', subject: 'Test', text: '' });
      await provider.send({ to: 'test@test.com', subject: 'Test', text: '' });

      expect(provider.getSentEmails()).toHaveLength(2);
      expect(provider.getSendCount()).toBe(2);

      provider.clear();

      expect(provider.getSentEmails()).toHaveLength(0);
      expect(provider.getSendCount()).toBe(0);
      expect(provider.getFailCount()).toBe(0);
    });
  });

  describe('setFailureRate and setLatency', () => {
    it('should allow dynamic configuration', async () => {
      provider.setFailureRate(0);
      await provider.send({ to: 'test@test.com', subject: 'Test', text: '' });

      provider.setFailureRate(1);
      await expect(
        provider.send({ to: 'test@test.com', subject: 'Test', text: '' })
      ).rejects.toThrow(ProviderError);
    });
  });

  describe('healthCheck', () => {
    it('should always report healthy', async () => {
      const health = await provider.healthCheck();
      expect(health.healthy).toBe(true);
    });
  });

  describe('validateConfig', () => {
    it('should validate failure rate range', () => {
      const invalidProvider = new MockProvider({ failureRate: 1.5 });
      const result = invalidProvider.validateConfig();
      expect(result.valid).toBe(false);
      expect(result.errors[0]).toContain('Failure rate');
    });

    it('should validate latency is non-negative', () => {
      const invalidProvider = new MockProvider({ latencyMs: -100 });
      const result = invalidProvider.validateConfig();
      expect(result.valid).toBe(false);
      expect(result.errors[0]).toContain('Latency');
    });
  });
});

describe('MailChannelsProvider', () => {
  let provider: MailChannelsProvider;

  beforeEach(() => {
    provider = new MailChannelsProvider();
  });

  describe('properties', () => {
    it('should have correct name', () => {
      expect(provider.name).toBe('mailchannels');
    });

    it('should not support attachments', () => {
      expect(provider.supportsAttachments).toBe(false);
    });

    it('should support BCC', () => {
      expect(provider.supportsBcc).toBe(true);
    });
  });

  describe('validateConfig', () => {
    it('should be valid without DKIM', () => {
      const result = provider.validateConfig();
      expect(result.valid).toBe(true);
    });

    it('should require domain and selector with DKIM key', () => {
      const providerWithKey = new MailChannelsProvider({
        dkimPrivateKey: 'test-key',
      });
      const result = providerWithKey.validateConfig();
      expect(result.valid).toBe(false);
      expect(result.errors).toContain('DKIM domain is required when DKIM private key is provided');
      expect(result.errors).toContain('DKIM selector is required when DKIM private key is provided');
    });

    it('should be valid with complete DKIM config', () => {
      const providerWithDkim = new MailChannelsProvider({
        dkimPrivateKey: 'test-key',
        dkimDomain: 'example.com',
        dkimSelector: 'selector1',
      });
      const result = providerWithDkim.validateConfig();
      expect(result.valid).toBe(true);
    });
  });
});

describe('ResendProvider', () => {
  describe('validateConfig', () => {
    it('should require API key', () => {
      const provider = new ResendProvider('');
      const result = provider.validateConfig();
      expect(result.valid).toBe(false);
      expect(result.errors[0]).toContain('API key is required');
    });

    it('should validate API key format', () => {
      const provider = new ResendProvider('invalid_key');
      const result = provider.validateConfig();
      expect(result.valid).toBe(false);
      expect(result.errors[0]).toContain('should start with "re_"');
    });

    it('should accept valid API key', () => {
      const provider = new ResendProvider('re_test_key_123');
      const result = provider.validateConfig();
      expect(result.valid).toBe(true);
    });
  });

  describe('properties', () => {
    it('should have correct name', () => {
      const provider = new ResendProvider('re_test');
      expect(provider.name).toBe('resend');
    });

    it('should support attachments', () => {
      const provider = new ResendProvider('re_test');
      expect(provider.supportsAttachments).toBe(true);
    });
  });
});

describe('SendGridProvider', () => {
  describe('validateConfig', () => {
    it('should require API key', () => {
      const provider = new SendGridProvider('');
      const result = provider.validateConfig();
      expect(result.valid).toBe(false);
      expect(result.errors[0]).toContain('API key is required');
    });

    it('should validate API key format', () => {
      const provider = new SendGridProvider('invalid_key');
      const result = provider.validateConfig();
      expect(result.valid).toBe(false);
      expect(result.errors[0]).toContain('should start with "SG."');
    });

    it('should accept valid API key', () => {
      const provider = new SendGridProvider('SG.test_key_123');
      const result = provider.validateConfig();
      expect(result.valid).toBe(true);
    });
  });

  describe('properties', () => {
    it('should have correct name', () => {
      const provider = new SendGridProvider('SG.test');
      expect(provider.name).toBe('sendgrid');
    });

    it('should support attachments', () => {
      const provider = new SendGridProvider('SG.test');
      expect(provider.supportsAttachments).toBe(true);
    });

    it('should support sandbox mode', () => {
      const provider = new SendGridProvider('SG.test', { sandboxMode: true });
      expect(provider.name).toBe('sendgrid');
    });
  });
});

describe('createMockProvider', () => {
  it('should create provider with default config', () => {
    const provider = createMockProvider();
    expect(provider).toBeInstanceOf(MockProvider);
  });

  it('should create provider with custom config', () => {
    const provider = createMockProvider({ latencyMs: 500, failureRate: 0.1 });
    expect(provider).toBeInstanceOf(MockProvider);
  });
});
