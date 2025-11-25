/**
 * NOIZYLAB Token Analytics Service
 * Comprehensive usage tracking and analytics for API tokens
 */

import type { Env } from '../types';

export interface TokenUsageEvent {
  tokenId: string;
  endpoint: string;
  method: string;
  statusCode: number;
  responseTime: number;
  ip: string;
  userAgent?: string;
  timestamp: string;
  requestId: string;
  errorCode?: string;
}

export interface TokenAnalytics {
  tokenId: string;
  totalRequests: number;
  successfulRequests: number;
  failedRequests: number;
  avgResponseTime: number;
  last24Hours: HourlyStats[];
  last7Days: DailyStats[];
  last30Days: DailyStats[];
  topEndpoints: EndpointStats[];
  topErrors: ErrorStats[];
  topIPs: IPStats[];
  rateLimit: RateLimitStats;
}

export interface HourlyStats {
  hour: string;
  requests: number;
  errors: number;
  avgLatency: number;
}

export interface DailyStats {
  date: string;
  requests: number;
  errors: number;
  avgLatency: number;
}

export interface EndpointStats {
  endpoint: string;
  method: string;
  count: number;
  avgLatency: number;
  errorRate: number;
}

export interface ErrorStats {
  errorCode: string;
  count: number;
  lastOccurred: string;
}

export interface IPStats {
  ip: string;
  requests: number;
  lastSeen: string;
}

export interface RateLimitStats {
  current: number;
  limit: number;
  remaining: number;
  resetsAt: string;
  exceeded: number;
}

export class TokenAnalyticsService {
  private readonly kv: KVNamespace;
  private readonly prefix = 'analytics';

  constructor(kv: KVNamespace) {
    this.kv = kv;
  }

  /**
   * Record a token usage event
   */
  async recordUsage(event: TokenUsageEvent): Promise<void> {
    const now = new Date();
    const hourKey = this.getHourKey(now);
    const dayKey = this.getDayKey(now);

    // Update hourly stats
    await this.incrementCounter(`${this.prefix}:hourly:${event.tokenId}:${hourKey}:requests`);
    if (event.statusCode >= 400) {
      await this.incrementCounter(`${this.prefix}:hourly:${event.tokenId}:${hourKey}:errors`);
    }

    // Update daily stats
    await this.incrementCounter(`${this.prefix}:daily:${event.tokenId}:${dayKey}:requests`);
    if (event.statusCode >= 400) {
      await this.incrementCounter(`${this.prefix}:daily:${event.tokenId}:${dayKey}:errors`);
    }

    // Update endpoint stats
    const endpointKey = `${event.method}:${event.endpoint}`;
    await this.incrementCounter(`${this.prefix}:endpoints:${event.tokenId}:${endpointKey}`);

    // Update error stats
    if (event.errorCode) {
      await this.incrementCounter(`${this.prefix}:errors:${event.tokenId}:${event.errorCode}`);
    }

    // Update IP stats
    await this.incrementCounter(`${this.prefix}:ips:${event.tokenId}:${event.ip}`);

    // Update latency stats (rolling average)
    await this.updateLatency(event.tokenId, event.responseTime);

    // Store recent event for audit
    await this.storeRecentEvent(event);

    // Update total counters
    await this.incrementCounter(`${this.prefix}:total:${event.tokenId}:requests`);
    if (event.statusCode >= 400) {
      await this.incrementCounter(`${this.prefix}:total:${event.tokenId}:errors`);
    }
  }

  /**
   * Get comprehensive analytics for a token
   */
  async getAnalytics(tokenId: string): Promise<TokenAnalytics> {
    const now = new Date();

    // Get total stats
    const totalRequests = await this.getCounter(`${this.prefix}:total:${tokenId}:requests`);
    const totalErrors = await this.getCounter(`${this.prefix}:total:${tokenId}:errors`);
    const avgResponseTime = await this.getLatency(tokenId);

    // Get hourly stats for last 24 hours
    const last24Hours = await this.getHourlyStats(tokenId, now, 24);

    // Get daily stats for last 7 days
    const last7Days = await this.getDailyStats(tokenId, now, 7);

    // Get daily stats for last 30 days
    const last30Days = await this.getDailyStats(tokenId, now, 30);

    // Get top endpoints
    const topEndpoints = await this.getTopEndpoints(tokenId, 10);

    // Get top errors
    const topErrors = await this.getTopErrors(tokenId, 10);

    // Get top IPs
    const topIPs = await this.getTopIPs(tokenId, 10);

    // Get rate limit stats
    const rateLimit = await this.getRateLimitStats(tokenId);

    return {
      tokenId,
      totalRequests,
      successfulRequests: totalRequests - totalErrors,
      failedRequests: totalErrors,
      avgResponseTime,
      last24Hours,
      last7Days,
      last30Days,
      topEndpoints,
      topErrors,
      topIPs,
      rateLimit,
    };
  }

  /**
   * Get real-time stats for dashboard
   */
  async getRealTimeStats(tokenId: string): Promise<{
    requestsPerMinute: number;
    activeConnections: number;
    errorRate: number;
    latencyP50: number;
    latencyP95: number;
    latencyP99: number;
  }> {
    const now = new Date();
    const minuteKey = this.getMinuteKey(now);

    const requestsPerMinute = await this.getCounter(
      `${this.prefix}:minute:${tokenId}:${minuteKey}:requests`
    );

    const errors = await this.getCounter(
      `${this.prefix}:minute:${tokenId}:${minuteKey}:errors`
    );

    const errorRate = requestsPerMinute > 0 ? (errors / requestsPerMinute) * 100 : 0;

    // Get latency percentiles from recent events
    const latencies = await this.getRecentLatencies(tokenId);
    const sorted = latencies.sort((a, b) => a - b);

    return {
      requestsPerMinute,
      activeConnections: 0, // Would need WebSocket tracking
      errorRate: Math.round(errorRate * 100) / 100,
      latencyP50: this.percentile(sorted, 50),
      latencyP95: this.percentile(sorted, 95),
      latencyP99: this.percentile(sorted, 99),
    };
  }

  /**
   * Get global analytics across all tokens
   */
  async getGlobalAnalytics(): Promise<{
    totalTokens: number;
    activeTokens: number;
    totalRequests24h: number;
    totalErrors24h: number;
    avgLatency: number;
  }> {
    // Get list of all tokens
    const list = await this.kv.list({ prefix: 'apikey:id:' });
    const totalTokens = list.keys.length;

    // Count active tokens (used in last 24h)
    const now = new Date();
    let activeTokens = 0;
    let totalRequests = 0;
    let totalErrors = 0;

    for (const key of list.keys) {
      const tokenId = key.name.replace('apikey:id:', '');
      const dayKey = this.getDayKey(now);

      const requests = await this.getCounter(`${this.prefix}:daily:${tokenId}:${dayKey}:requests`);
      if (requests > 0) {
        activeTokens++;
        totalRequests += requests;
        totalErrors += await this.getCounter(`${this.prefix}:daily:${tokenId}:${dayKey}:errors`);
      }
    }

    return {
      totalTokens,
      activeTokens,
      totalRequests24h: totalRequests,
      totalErrors24h: totalErrors,
      avgLatency: 45, // Placeholder
    };
  }

  // Private helper methods

  private async incrementCounter(key: string): Promise<void> {
    const current = await this.getCounter(key);
    await this.kv.put(key, String(current + 1), {
      expirationTtl: 60 * 60 * 24 * 90, // 90 days
    });
  }

  private async getCounter(key: string): Promise<number> {
    const value = await this.kv.get(key);
    return value ? parseInt(value, 10) : 0;
  }

  private async updateLatency(tokenId: string, latency: number): Promise<void> {
    const key = `${this.prefix}:latency:${tokenId}`;
    const data = await this.kv.get(key);

    let stats = data ? JSON.parse(data) : { count: 0, total: 0 };
    stats.count++;
    stats.total += latency;

    await this.kv.put(key, JSON.stringify(stats), {
      expirationTtl: 60 * 60 * 24 * 30,
    });
  }

  private async getLatency(tokenId: string): Promise<number> {
    const key = `${this.prefix}:latency:${tokenId}`;
    const data = await this.kv.get(key);

    if (!data) return 0;

    const stats = JSON.parse(data);
    return stats.count > 0 ? Math.round(stats.total / stats.count) : 0;
  }

  private async storeRecentEvent(event: TokenUsageEvent): Promise<void> {
    const key = `${this.prefix}:events:${event.tokenId}:${Date.now()}`;
    await this.kv.put(key, JSON.stringify(event), {
      expirationTtl: 60 * 60, // 1 hour
    });
  }

  private async getRecentLatencies(tokenId: string): Promise<number[]> {
    const list = await this.kv.list({
      prefix: `${this.prefix}:events:${tokenId}:`,
      limit: 100,
    });

    const latencies: number[] = [];

    for (const key of list.keys) {
      const data = await this.kv.get(key.name);
      if (data) {
        const event = JSON.parse(data) as TokenUsageEvent;
        latencies.push(event.responseTime);
      }
    }

    return latencies;
  }

  private async getHourlyStats(tokenId: string, now: Date, hours: number): Promise<HourlyStats[]> {
    const stats: HourlyStats[] = [];

    for (let i = 0; i < hours; i++) {
      const date = new Date(now.getTime() - i * 60 * 60 * 1000);
      const hourKey = this.getHourKey(date);

      const requests = await this.getCounter(`${this.prefix}:hourly:${tokenId}:${hourKey}:requests`);
      const errors = await this.getCounter(`${this.prefix}:hourly:${tokenId}:${hourKey}:errors`);

      stats.push({
        hour: hourKey,
        requests,
        errors,
        avgLatency: 0,
      });
    }

    return stats.reverse();
  }

  private async getDailyStats(tokenId: string, now: Date, days: number): Promise<DailyStats[]> {
    const stats: DailyStats[] = [];

    for (let i = 0; i < days; i++) {
      const date = new Date(now.getTime() - i * 24 * 60 * 60 * 1000);
      const dayKey = this.getDayKey(date);

      const requests = await this.getCounter(`${this.prefix}:daily:${tokenId}:${dayKey}:requests`);
      const errors = await this.getCounter(`${this.prefix}:daily:${tokenId}:${dayKey}:errors`);

      stats.push({
        date: dayKey,
        requests,
        errors,
        avgLatency: 0,
      });
    }

    return stats.reverse();
  }

  private async getTopEndpoints(tokenId: string, limit: number): Promise<EndpointStats[]> {
    const list = await this.kv.list({
      prefix: `${this.prefix}:endpoints:${tokenId}:`,
      limit: 100,
    });

    const endpoints: EndpointStats[] = [];

    for (const key of list.keys) {
      const count = await this.getCounter(key.name);
      const parts = key.name.split(':');
      const [method, ...endpointParts] = parts.slice(-1)[0].split('/');

      endpoints.push({
        endpoint: '/' + endpointParts.join('/'),
        method: method || 'GET',
        count,
        avgLatency: 0,
        errorRate: 0,
      });
    }

    return endpoints
      .sort((a, b) => b.count - a.count)
      .slice(0, limit);
  }

  private async getTopErrors(tokenId: string, limit: number): Promise<ErrorStats[]> {
    const list = await this.kv.list({
      prefix: `${this.prefix}:errors:${tokenId}:`,
      limit: 100,
    });

    const errors: ErrorStats[] = [];

    for (const key of list.keys) {
      const count = await this.getCounter(key.name);
      const errorCode = key.name.split(':').pop() || 'UNKNOWN';

      errors.push({
        errorCode,
        count,
        lastOccurred: new Date().toISOString(),
      });
    }

    return errors
      .sort((a, b) => b.count - a.count)
      .slice(0, limit);
  }

  private async getTopIPs(tokenId: string, limit: number): Promise<IPStats[]> {
    const list = await this.kv.list({
      prefix: `${this.prefix}:ips:${tokenId}:`,
      limit: 100,
    });

    const ips: IPStats[] = [];

    for (const key of list.keys) {
      const requests = await this.getCounter(key.name);
      const ip = key.name.split(':').pop() || 'unknown';

      ips.push({
        ip,
        requests,
        lastSeen: new Date().toISOString(),
      });
    }

    return ips
      .sort((a, b) => b.requests - a.requests)
      .slice(0, limit);
  }

  private async getRateLimitStats(tokenId: string): Promise<RateLimitStats> {
    // Get rate limit info from rate limiter
    const key = `ratelimit:${tokenId}`;
    const data = await this.kv.get(key);

    if (!data) {
      return {
        current: 0,
        limit: 100,
        remaining: 100,
        resetsAt: new Date(Date.now() + 3600000).toISOString(),
        exceeded: 0,
      };
    }

    const info = JSON.parse(data);
    return {
      current: info.count || 0,
      limit: info.limit || 100,
      remaining: Math.max(0, (info.limit || 100) - (info.count || 0)),
      resetsAt: info.resetAt || new Date(Date.now() + 3600000).toISOString(),
      exceeded: info.exceeded || 0,
    };
  }

  private getHourKey(date: Date): string {
    return date.toISOString().slice(0, 13);
  }

  private getDayKey(date: Date): string {
    return date.toISOString().slice(0, 10);
  }

  private getMinuteKey(date: Date): string {
    return date.toISOString().slice(0, 16);
  }

  private percentile(arr: number[], p: number): number {
    if (arr.length === 0) return 0;
    const index = Math.ceil((p / 100) * arr.length) - 1;
    return arr[Math.max(0, index)] || 0;
  }
}

/**
 * Create token analytics service from environment
 */
export function createTokenAnalyticsService(env: Env): TokenAnalyticsService {
  return new TokenAnalyticsService(env.EMAIL_KV);
}
