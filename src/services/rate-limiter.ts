/**
 * NOIZYLAB Email System - Rate Limiter Service
 * Implements sliding window rate limiting using KV storage
 */

import type { RateLimitConfig, RateLimitResult } from '../types';
import { RateLimitError } from '../errors';
import { now } from '../utils';

/**
 * Rate limiter using sliding window algorithm with KV storage
 */
export class RateLimiter {
  private readonly kv: KVNamespace;
  private readonly config: RateLimitConfig;
  private readonly keyPrefix: string;

  constructor(kv: KVNamespace, config: RateLimitConfig, keyPrefix: string = 'ratelimit') {
    this.kv = kv;
    this.config = config;
    this.keyPrefix = keyPrefix;
  }

  /**
   * Check if a request is allowed under the rate limit
   */
  async check(identifier: string): Promise<RateLimitResult> {
    const key = this.buildKey(identifier);
    const currentTime = Math.floor(Date.now() / 1000);
    const windowStart = currentTime - this.config.windowSeconds;

    // Get current window data
    const data = await this.getWindowData(key);

    // Filter out expired entries and count requests in current window
    const validRequests = data.requests.filter((timestamp) => timestamp > windowStart);
    const requestCount = validRequests.length;

    const remaining = Math.max(0, this.config.maxRequests - requestCount);
    const resetAt = currentTime + this.config.windowSeconds;

    return {
      allowed: requestCount < this.config.maxRequests,
      remaining,
      resetAt,
      limit: this.config.maxRequests,
    };
  }

  /**
   * Record a request and check if it's allowed
   */
  async consume(identifier: string): Promise<RateLimitResult> {
    const key = this.buildKey(identifier);
    const currentTime = Math.floor(Date.now() / 1000);
    const windowStart = currentTime - this.config.windowSeconds;

    // Get current window data
    const data = await this.getWindowData(key);

    // Filter out expired entries
    const validRequests = data.requests.filter((timestamp) => timestamp > windowStart);
    const requestCount = validRequests.length;

    const resetAt = currentTime + this.config.windowSeconds;

    // Check if limit exceeded
    if (requestCount >= this.config.maxRequests) {
      const retryAfter = this.config.windowSeconds;
      throw new RateLimitError(
        `Rate limit exceeded. Maximum ${this.config.maxRequests} requests per ${this.config.windowSeconds} seconds.`,
        retryAfter,
        {
          identifier,
          limit: this.config.maxRequests,
          windowSeconds: this.config.windowSeconds,
          resetAt,
        }
      );
    }

    // Add current request
    validRequests.push(currentTime);

    // Store updated data
    await this.setWindowData(key, { requests: validRequests });

    const remaining = Math.max(0, this.config.maxRequests - validRequests.length);

    return {
      allowed: true,
      remaining,
      resetAt,
      limit: this.config.maxRequests,
    };
  }

  /**
   * Reset rate limit for an identifier
   */
  async reset(identifier: string): Promise<void> {
    const key = this.buildKey(identifier);
    await this.kv.delete(key);
  }

  /**
   * Get rate limit status without consuming
   */
  async getStatus(identifier: string): Promise<RateLimitResult> {
    return this.check(identifier);
  }

  private buildKey(identifier: string): string {
    return `${this.keyPrefix}:${identifier}`;
  }

  private async getWindowData(key: string): Promise<{ requests: number[] }> {
    const stored = await this.kv.get(key, 'json');
    if (stored === null || typeof stored !== 'object') {
      return { requests: [] };
    }
    const data = stored as { requests?: unknown };
    if (!Array.isArray(data.requests)) {
      return { requests: [] };
    }
    return { requests: data.requests.filter((r): r is number => typeof r === 'number') };
  }

  private async setWindowData(key: string, data: { requests: number[] }): Promise<void> {
    await this.kv.put(key, JSON.stringify(data), {
      expirationTtl: this.config.windowSeconds * 2,
    });
  }
}

/**
 * Create rate limiter from environment configuration
 */
export function createRateLimiter(kv: KVNamespace, env: Env): RateLimiter {
  const config: RateLimitConfig = {
    maxRequests: parseInt(env.RATE_LIMIT_MAX_REQUESTS, 10) || 100,
    windowSeconds: parseInt(env.RATE_LIMIT_WINDOW_SECONDS, 10) || 3600,
  };

  return new RateLimiter(kv, config);
}

/**
 * Rate limit middleware result type
 */
export interface RateLimitHeaders {
  'X-RateLimit-Limit': string;
  'X-RateLimit-Remaining': string;
  'X-RateLimit-Reset': string;
  'Retry-After'?: string;
}

/**
 * Generate rate limit headers from result
 */
export function getRateLimitHeaders(result: RateLimitResult): RateLimitHeaders {
  const headers: RateLimitHeaders = {
    'X-RateLimit-Limit': result.limit.toString(),
    'X-RateLimit-Remaining': result.remaining.toString(),
    'X-RateLimit-Reset': result.resetAt.toString(),
  };

  if (!result.allowed) {
    headers['Retry-After'] = (result.resetAt - Math.floor(Date.now() / 1000)).toString();
  }

  return headers;
}
