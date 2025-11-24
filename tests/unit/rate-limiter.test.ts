/**
 * NOIZYLAB Email System - Rate Limiter Unit Tests
 */

import { describe, it, expect, beforeEach, vi } from 'vitest';
import { env } from 'cloudflare:test';
import { RateLimiter, getRateLimitHeaders } from '../../src/services/rate-limiter';
import { RateLimitError } from '../../src/errors';

describe('RateLimiter', () => {
  let rateLimiter: RateLimiter;
  let mockKV: KVNamespace;

  beforeEach(() => {
    mockKV = env.EMAIL_KV;
    rateLimiter = new RateLimiter(mockKV, {
      maxRequests: 5,
      windowSeconds: 60,
    });
  });

  describe('check', () => {
    it('should allow requests within limit', async () => {
      const result = await rateLimiter.check('client-1');

      expect(result.allowed).toBe(true);
      expect(result.remaining).toBe(5);
      expect(result.limit).toBe(5);
    });

    it('should not consume quota when checking', async () => {
      await rateLimiter.check('client-2');
      await rateLimiter.check('client-2');
      await rateLimiter.check('client-2');

      const result = await rateLimiter.check('client-2');
      expect(result.remaining).toBe(5);
    });
  });

  describe('consume', () => {
    it('should decrement remaining count', async () => {
      const first = await rateLimiter.consume('client-3');
      expect(first.remaining).toBe(4);

      const second = await rateLimiter.consume('client-3');
      expect(second.remaining).toBe(3);
    });

    it('should throw RateLimitError when limit exceeded', async () => {
      // Consume all available requests
      for (let i = 0; i < 5; i++) {
        await rateLimiter.consume('client-4');
      }

      // Next request should fail
      await expect(rateLimiter.consume('client-4')).rejects.toThrow(RateLimitError);
    });

    it('should include retry info in error', async () => {
      for (let i = 0; i < 5; i++) {
        await rateLimiter.consume('client-5');
      }

      try {
        await rateLimiter.consume('client-5');
      } catch (error) {
        expect(error).toBeInstanceOf(RateLimitError);
        const rateLimitError = error as RateLimitError;
        expect(rateLimitError.retryAfter).toBe(60);
        expect(rateLimitError.statusCode).toBe(429);
      }
    });

    it('should track different clients separately', async () => {
      // Exhaust client-6
      for (let i = 0; i < 5; i++) {
        await rateLimiter.consume('client-6');
      }

      // client-7 should still work
      const result = await rateLimiter.consume('client-7');
      expect(result.allowed).toBe(true);
      expect(result.remaining).toBe(4);
    });
  });

  describe('reset', () => {
    it('should reset rate limit for client', async () => {
      // Use some quota
      await rateLimiter.consume('client-8');
      await rateLimiter.consume('client-8');

      const before = await rateLimiter.check('client-8');
      expect(before.remaining).toBe(3);

      // Reset
      await rateLimiter.reset('client-8');

      const after = await rateLimiter.check('client-8');
      expect(after.remaining).toBe(5);
    });
  });

  describe('getStatus', () => {
    it('should return current status without consuming', async () => {
      await rateLimiter.consume('client-9');
      await rateLimiter.consume('client-9');

      const status = await rateLimiter.getStatus('client-9');
      expect(status.remaining).toBe(3);
      expect(status.allowed).toBe(true);

      // Verify it didn't consume
      const statusAgain = await rateLimiter.getStatus('client-9');
      expect(statusAgain.remaining).toBe(3);
    });
  });

  describe('sliding window behavior', () => {
    it('should calculate reset time correctly', async () => {
      const beforeConsume = Math.floor(Date.now() / 1000);
      const result = await rateLimiter.consume('client-10');
      const afterConsume = Math.floor(Date.now() / 1000);

      // Reset should be within window
      expect(result.resetAt).toBeGreaterThanOrEqual(beforeConsume + 60);
      expect(result.resetAt).toBeLessThanOrEqual(afterConsume + 60);
    });
  });
});

describe('getRateLimitHeaders', () => {
  it('should generate correct headers for allowed request', () => {
    const result = {
      allowed: true,
      remaining: 95,
      resetAt: 1700000000,
      limit: 100,
    };

    const headers = getRateLimitHeaders(result);

    expect(headers['X-RateLimit-Limit']).toBe('100');
    expect(headers['X-RateLimit-Remaining']).toBe('95');
    expect(headers['X-RateLimit-Reset']).toBe('1700000000');
    expect(headers['Retry-After']).toBeUndefined();
  });

  it('should include Retry-After for denied request', () => {
    const now = Math.floor(Date.now() / 1000);
    const result = {
      allowed: false,
      remaining: 0,
      resetAt: now + 60,
      limit: 100,
    };

    const headers = getRateLimitHeaders(result);

    expect(headers['Retry-After']).toBeDefined();
    const retryAfter = parseInt(headers['Retry-After'] ?? '0', 10);
    expect(retryAfter).toBeGreaterThan(0);
    expect(retryAfter).toBeLessThanOrEqual(60);
  });
});
