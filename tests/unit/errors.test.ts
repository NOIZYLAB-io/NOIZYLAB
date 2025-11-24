/**
 * NOIZYLAB Email System - Errors Unit Tests
 */

import { describe, it, expect } from 'vitest';
import {
  NoizylabError,
  ValidationError,
  RateLimitError,
  AuthenticationError,
  ProviderError,
  TemplateNotFoundError,
  TemplateRenderError,
  AttachmentTooLargeError,
  RecipientBlockedError,
  InternalError,
  IdempotencyConflictError,
  isNoizylabError,
  toNoizylabError,
} from '../../src/errors';

describe('Custom Errors', () => {
  describe('ValidationError', () => {
    it('should have correct properties', () => {
      const error = new ValidationError('Invalid input', { field: 'email' });

      expect(error.message).toBe('Invalid input');
      expect(error.code).toBe('VALIDATION_ERROR');
      expect(error.statusCode).toBe(400);
      expect(error.details).toEqual({ field: 'email' });
      expect(error.name).toBe('ValidationError');
    });

    it('should serialize to JSON correctly', () => {
      const error = new ValidationError('Invalid input');
      const json = error.toJSON();

      expect(json).toMatchObject({
        success: false,
        error: {
          code: 'VALIDATION_ERROR',
          message: 'Invalid input',
        },
      });
      expect(json['timestamp']).toBeDefined();
    });
  });

  describe('RateLimitError', () => {
    it('should have correct properties', () => {
      const error = new RateLimitError('Too many requests', 3600);

      expect(error.message).toBe('Too many requests');
      expect(error.code).toBe('RATE_LIMIT_EXCEEDED');
      expect(error.statusCode).toBe(429);
      expect(error.retryAfter).toBe(3600);
      expect(error.details?.['retryAfter']).toBe(3600);
    });

    it('should include retry info in JSON', () => {
      const error = new RateLimitError('Too many requests', 60, { limit: 100 });
      const json = error.toJSON();

      expect((json['error'] as Record<string, unknown>)['details']).toMatchObject({
        retryAfter: 60,
        limit: 100,
      });
    });
  });

  describe('AuthenticationError', () => {
    it('should have default message', () => {
      const error = new AuthenticationError();
      expect(error.message).toBe('Authentication failed');
      expect(error.code).toBe('AUTHENTICATION_ERROR');
      expect(error.statusCode).toBe(401);
    });

    it('should accept custom message', () => {
      const error = new AuthenticationError('Invalid API key');
      expect(error.message).toBe('Invalid API key');
    });
  });

  describe('ProviderError', () => {
    it('should include provider name', () => {
      const error = new ProviderError('resend', 'API rate limited');

      expect(error.message).toBe('API rate limited');
      expect(error.code).toBe('PROVIDER_ERROR');
      expect(error.statusCode).toBe(502);
      expect(error.provider).toBe('resend');
      expect(error.details?.['provider']).toBe('resend');
    });
  });

  describe('TemplateNotFoundError', () => {
    it('should include template ID', () => {
      const error = new TemplateNotFoundError('welcome-email');

      expect(error.message).toBe('Template not found: welcome-email');
      expect(error.code).toBe('TEMPLATE_NOT_FOUND');
      expect(error.statusCode).toBe(404);
      expect(error.templateId).toBe('welcome-email');
    });
  });

  describe('TemplateRenderError', () => {
    it('should include template ID and message', () => {
      const error = new TemplateRenderError('welcome-email', 'Missing variable: name');

      expect(error.message).toBe('Missing variable: name');
      expect(error.code).toBe('TEMPLATE_RENDER_ERROR');
      expect(error.statusCode).toBe(400);
      expect(error.templateId).toBe('welcome-email');
    });
  });

  describe('AttachmentTooLargeError', () => {
    it('should include size information', () => {
      const error = new AttachmentTooLargeError(10000000, 15000000);

      expect(error.message).toBe('Attachment exceeds maximum size of 10000000 bytes');
      expect(error.code).toBe('ATTACHMENT_TOO_LARGE');
      expect(error.statusCode).toBe(413);
      expect(error.maxSize).toBe(10000000);
      expect(error.actualSize).toBe(15000000);
    });
  });

  describe('RecipientBlockedError', () => {
    it('should include recipient and reason', () => {
      const error = new RecipientBlockedError('test@example.com', 'Previous bounce');

      expect(error.message).toBe('Recipient is blocked: test@example.com');
      expect(error.code).toBe('RECIPIENT_BLOCKED');
      expect(error.statusCode).toBe(400);
      expect(error.recipient).toBe('test@example.com');
      expect(error.reason).toBe('Previous bounce');
    });
  });

  describe('InternalError', () => {
    it('should have default message', () => {
      const error = new InternalError();
      expect(error.message).toBe('Internal server error');
      expect(error.code).toBe('INTERNAL_ERROR');
      expect(error.statusCode).toBe(500);
    });

    it('should accept custom message and details', () => {
      const error = new InternalError('Database connection failed', { db: 'primary' });
      expect(error.message).toBe('Database connection failed');
      expect(error.details).toEqual({ db: 'primary' });
    });
  });

  describe('IdempotencyConflictError', () => {
    it('should include key and existing message ID', () => {
      const error = new IdempotencyConflictError('unique-key-123', 'msg_abc123');

      expect(error.message).toBe('Request with idempotency key already processed');
      expect(error.code).toBe('IDEMPOTENCY_CONFLICT');
      expect(error.statusCode).toBe(409);
      expect(error.idempotencyKey).toBe('unique-key-123');
      expect(error.details?.['existingMessageId']).toBe('msg_abc123');
    });
  });

  describe('isNoizylabError', () => {
    it('should return true for NoizylabError instances', () => {
      expect(isNoizylabError(new ValidationError('test'))).toBe(true);
      expect(isNoizylabError(new RateLimitError('test', 60))).toBe(true);
      expect(isNoizylabError(new InternalError())).toBe(true);
    });

    it('should return false for other errors', () => {
      expect(isNoizylabError(new Error('test'))).toBe(false);
      expect(isNoizylabError(new TypeError('test'))).toBe(false);
      expect(isNoizylabError('string error')).toBe(false);
      expect(isNoizylabError(null)).toBe(false);
      expect(isNoizylabError(undefined)).toBe(false);
    });
  });

  describe('toNoizylabError', () => {
    it('should return NoizylabError as-is', () => {
      const original = new ValidationError('test');
      const result = toNoizylabError(original);
      expect(result).toBe(original);
    });

    it('should convert Error to InternalError', () => {
      const original = new Error('Something went wrong');
      const result = toNoizylabError(original);

      expect(result).toBeInstanceOf(InternalError);
      expect(result.message).toBe('Something went wrong');
      expect(result.details?.['originalError']).toBe('Error');
    });

    it('should convert unknown values to InternalError', () => {
      const result = toNoizylabError('string error');

      expect(result).toBeInstanceOf(InternalError);
      expect(result.message).toBe('An unknown error occurred');
      expect(result.details?.['originalError']).toBe('string error');
    });

    it('should handle null/undefined', () => {
      expect(toNoizylabError(null)).toBeInstanceOf(InternalError);
      expect(toNoizylabError(undefined)).toBeInstanceOf(InternalError);
    });
  });
});
