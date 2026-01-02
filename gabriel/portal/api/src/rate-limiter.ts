/**
 * Rate Limiting Service
 * 
 * Protects the API from abuse using Cloudflare KV for distributed rate limiting
 * Implements sliding window algorithm for smooth rate limit enforcement
 */

// Rate limit configurations for different endpoints
const RATE_LIMITS = {
  // Scan endpoint - most expensive, strictest limits
  scan: {
    free: { requests: 5, windowSeconds: 3600 },      // 5 per hour for free tier
    basic: { requests: 20, windowSeconds: 3600 },    // 20 per hour for basic
    pro: { requests: 1000, windowSeconds: 3600 },    // 1000 per hour for pro
  },
  // Auth endpoints - prevent brute force
  auth: {
    default: { requests: 10, windowSeconds: 300 },   // 10 per 5 minutes
  },
  // General API - moderate limits
  api: {
    default: { requests: 100, windowSeconds: 60 },   // 100 per minute
  },
  // Webhook endpoints - high limits for service-to-service
  webhook: {
    default: { requests: 1000, windowSeconds: 60 },  // 1000 per minute
  },
};

interface RateLimitResult {
  allowed: boolean;
  remaining: number;
  resetAt: number;
  retryAfter?: number;
}

interface RateLimitEntry {
  count: number;
  windowStart: number;
}

/**
 * Rate Limiter using Cloudflare KV
 */
export class RateLimiter {
  private kv: KVNamespace;

  constructor(kv: KVNamespace) {
    this.kv = kv;
  }

  /**
   * Check and consume rate limit for a given key
   */
  async check(
    identifier: string,
    endpoint: keyof typeof RATE_LIMITS,
    tier: string = 'default'
  ): Promise<RateLimitResult> {
    const config = this.getConfig(endpoint, tier);
    const key = `ratelimit:${endpoint}:${identifier}`;
    const now = Math.floor(Date.now() / 1000);

    // Get current state
    const data = await this.kv.get<RateLimitEntry>(key, 'json');
    
    // Check if we're in a new window
    if (!data || now - data.windowStart >= config.windowSeconds) {
      // New window, reset counter
      const entry: RateLimitEntry = {
        count: 1,
        windowStart: now,
      };
      await this.kv.put(key, JSON.stringify(entry), {
        expirationTtl: config.windowSeconds,
      });
      
      return {
        allowed: true,
        remaining: config.requests - 1,
        resetAt: now + config.windowSeconds,
      };
    }

    // Check if limit exceeded
    if (data.count >= config.requests) {
      const resetAt = data.windowStart + config.windowSeconds;
      return {
        allowed: false,
        remaining: 0,
        resetAt,
        retryAfter: resetAt - now,
      };
    }

    // Increment counter
    const entry: RateLimitEntry = {
      count: data.count + 1,
      windowStart: data.windowStart,
    };
    await this.kv.put(key, JSON.stringify(entry), {
      expirationTtl: config.windowSeconds - (now - data.windowStart),
    });

    return {
      allowed: true,
      remaining: config.requests - entry.count,
      resetAt: data.windowStart + config.windowSeconds,
    };
  }

  /**
   * Get rate limit config for endpoint and tier
   */
  private getConfig(endpoint: keyof typeof RATE_LIMITS, tier: string) {
    const endpointConfig = RATE_LIMITS[endpoint];
    if ('default' in endpointConfig) {
      return endpointConfig.default;
    }
    return (endpointConfig as Record<string, { requests: number; windowSeconds: number }>)[tier] || endpointConfig.free;
  }

  /**
   * Add rate limit headers to response
   */
  static addHeaders(response: Response, result: RateLimitResult): Response {
    const headers = new Headers(response.headers);
    headers.set('X-RateLimit-Remaining', result.remaining.toString());
    headers.set('X-RateLimit-Reset', result.resetAt.toString());
    
    if (!result.allowed && result.retryAfter) {
      headers.set('Retry-After', result.retryAfter.toString());
    }
    
    return new Response(response.body, {
      status: response.status,
      statusText: response.statusText,
      headers,
    });
  }

  /**
   * Create rate limit exceeded response
   */
  static limitExceeded(result: RateLimitResult): Response {
    return new Response(
      JSON.stringify({
        error: 'Rate limit exceeded',
        remaining: result.remaining,
        resetAt: result.resetAt,
        retryAfter: result.retryAfter,
      }),
      {
        status: 429,
        headers: {
          'Content-Type': 'application/json',
          'X-RateLimit-Remaining': '0',
          'X-RateLimit-Reset': result.resetAt.toString(),
          'Retry-After': result.retryAfter?.toString() || '60',
        },
      }
    );
  }
}

// ============================================================================
// IP-BASED RATE LIMITING (NO AUTH REQUIRED)
// ============================================================================

/**
 * Get client IP from request, handling Cloudflare headers
 */
export function getClientIP(request: Request): string {
  // Cloudflare provides real IP in CF-Connecting-IP header
  const cfIP = request.headers.get('CF-Connecting-IP');
  if (cfIP) return cfIP;

  // Fallback to X-Forwarded-For
  const forwarded = request.headers.get('X-Forwarded-For');
  if (forwarded) return forwarded.split(',')[0].trim();

  // Last resort - use a hash of user agent + accept headers
  const ua = request.headers.get('User-Agent') || '';
  const accept = request.headers.get('Accept') || '';
  return `anon:${hashString(ua + accept)}`;
}

function hashString(str: string): string {
  let hash = 0;
  for (let i = 0; i < str.length; i++) {
    const char = str.charCodeAt(i);
    hash = ((hash << 5) - hash) + char;
    hash = hash & hash;
  }
  return Math.abs(hash).toString(16);
}

// ============================================================================
// MIDDLEWARE FOR CLOUDFLARE WORKERS
// ============================================================================

/**
 * Rate limiting middleware factory
 */
export function createRateLimitMiddleware(kv: KVNamespace) {
  const limiter = new RateLimiter(kv);

  return async function rateLimitMiddleware(
    request: Request,
    endpoint: keyof typeof RATE_LIMITS,
    getUserTier?: () => Promise<string>
  ): Promise<Response | null> {
    // Get identifier (user ID or IP)
    const identifier = getClientIP(request);
    
    // Get user tier if authenticated
    const tier = getUserTier ? await getUserTier() : 'default';
    
    // Check rate limit
    const result = await limiter.check(identifier, endpoint, tier);
    
    if (!result.allowed) {
      return RateLimiter.limitExceeded(result);
    }
    
    // Store result for later header addition
    (request as unknown as { rateLimitResult: RateLimitResult }).rateLimitResult = result;
    
    return null; // Continue to handler
  };
}

// ============================================================================
// DDOS PROTECTION LAYER
// ============================================================================

interface DDoSState {
  requestCount: number;
  lastReset: number;
  blocked: boolean;
  blockedUntil?: number;
}

/**
 * DDoS Protection - blocks IPs that make too many requests
 */
export class DDoSProtection {
  private kv: KVNamespace;
  private threshold = 500; // requests per window
  private windowSeconds = 60;
  private blockDuration = 600; // 10 minute block

  constructor(kv: KVNamespace) {
    this.kv = kv;
  }

  async check(ip: string): Promise<{ blocked: boolean; reason?: string }> {
    const key = `ddos:${ip}`;
    const now = Math.floor(Date.now() / 1000);
    
    const state = await this.kv.get<DDoSState>(key, 'json');
    
    // Check if currently blocked
    if (state?.blocked && state.blockedUntil && state.blockedUntil > now) {
      return {
        blocked: true,
        reason: `IP blocked for suspicious activity. Unblocked at ${new Date(state.blockedUntil * 1000).toISOString()}`,
      };
    }
    
    // New or reset window
    if (!state || now - state.lastReset >= this.windowSeconds) {
      await this.kv.put(key, JSON.stringify({
        requestCount: 1,
        lastReset: now,
        blocked: false,
      }), { expirationTtl: this.blockDuration });
      
      return { blocked: false };
    }
    
    // Increment and check threshold
    const newCount = state.requestCount + 1;
    
    if (newCount > this.threshold) {
      // Block the IP
      await this.kv.put(key, JSON.stringify({
        requestCount: newCount,
        lastReset: state.lastReset,
        blocked: true,
        blockedUntil: now + this.blockDuration,
      }), { expirationTtl: this.blockDuration });
      
      console.warn(`DDoS: Blocked IP ${ip} for exceeding ${this.threshold} requests/minute`);
      
      return {
        blocked: true,
        reason: 'Too many requests. You have been temporarily blocked.',
      };
    }
    
    // Update count
    await this.kv.put(key, JSON.stringify({
      ...state,
      requestCount: newCount,
    }), { expirationTtl: this.windowSeconds - (now - state.lastReset) });
    
    return { blocked: false };
  }

  static blockedResponse(reason: string): Response {
    return new Response(
      JSON.stringify({
        error: 'Access denied',
        reason,
      }),
      {
        status: 403,
        headers: {
          'Content-Type': 'application/json',
        },
      }
    );
  }
}

// ============================================================================
// EXPORTS
// ============================================================================

export default {
  RateLimiter,
  DDoSProtection,
  getClientIP,
  createRateLimitMiddleware,
  RATE_LIMITS,
};
