/**
 * NOIZYLAB IP Allowlist Service
 * IP-based access control for API tokens
 */

import type { Env } from '../types';

export interface IPAllowlistEntry {
  ip: string;
  type: 'single' | 'range' | 'cidr';
  description?: string;
  createdAt: string;
  createdBy?: string;
}

export interface IPAllowlistConfig {
  tokenId: string;
  enabled: boolean;
  mode: 'allowlist' | 'blocklist';
  entries: IPAllowlistEntry[];
  defaultAction: 'allow' | 'deny';
  logDenied: boolean;
  notifyOnDeny: boolean;
  createdAt: string;
  updatedAt: string;
}

export interface IPCheckResult {
  allowed: boolean;
  ip: string;
  matchedEntry?: IPAllowlistEntry;
  reason?: string;
}

export class IPAllowlistService {
  private readonly kv: KVNamespace;
  private readonly prefix = 'ipallow';

  constructor(kv: KVNamespace) {
    this.kv = kv;
  }

  /**
   * Configure IP allowlist for a token
   */
  async configureAllowlist(
    tokenId: string,
    config: Partial<Omit<IPAllowlistConfig, 'tokenId' | 'createdAt' | 'updatedAt'>>
  ): Promise<IPAllowlistConfig> {
    const existing = await this.getConfig(tokenId);

    const now = new Date().toISOString();
    const updated: IPAllowlistConfig = {
      tokenId,
      enabled: config.enabled ?? existing?.enabled ?? false,
      mode: config.mode ?? existing?.mode ?? 'allowlist',
      entries: config.entries ?? existing?.entries ?? [],
      defaultAction: config.defaultAction ?? existing?.defaultAction ?? 'deny',
      logDenied: config.logDenied ?? existing?.logDenied ?? true,
      notifyOnDeny: config.notifyOnDeny ?? existing?.notifyOnDeny ?? false,
      createdAt: existing?.createdAt ?? now,
      updatedAt: now,
    };

    await this.kv.put(`${this.prefix}:${tokenId}`, JSON.stringify(updated));
    return updated;
  }

  /**
   * Get IP allowlist configuration for a token
   */
  async getConfig(tokenId: string): Promise<IPAllowlistConfig | null> {
    const data = await this.kv.get(`${this.prefix}:${tokenId}`);
    return data ? JSON.parse(data) : null;
  }

  /**
   * Add IP to allowlist
   */
  async addIP(
    tokenId: string,
    ip: string,
    options: { description?: string; createdBy?: string } = {}
  ): Promise<IPAllowlistConfig | null> {
    const config = await this.getConfig(tokenId);
    if (!config) {
      // Create new config
      return this.configureAllowlist(tokenId, {
        enabled: true,
        entries: [{
          ip,
          type: this.detectIPType(ip),
          description: options.description,
          createdAt: new Date().toISOString(),
          createdBy: options.createdBy,
        }],
      });
    }

    // Check if IP already exists
    if (config.entries.some(e => e.ip === ip)) {
      return config;
    }

    config.entries.push({
      ip,
      type: this.detectIPType(ip),
      description: options.description,
      createdAt: new Date().toISOString(),
      createdBy: options.createdBy,
    });

    return this.configureAllowlist(tokenId, { entries: config.entries });
  }

  /**
   * Remove IP from allowlist
   */
  async removeIP(tokenId: string, ip: string): Promise<IPAllowlistConfig | null> {
    const config = await this.getConfig(tokenId);
    if (!config) return null;

    config.entries = config.entries.filter(e => e.ip !== ip);
    return this.configureAllowlist(tokenId, { entries: config.entries });
  }

  /**
   * Check if an IP is allowed
   */
  async checkIP(tokenId: string, ip: string): Promise<IPCheckResult> {
    const config = await this.getConfig(tokenId);

    // No config or disabled = allow all
    if (!config || !config.enabled) {
      return { allowed: true, ip };
    }

    // Check against entries
    for (const entry of config.entries) {
      if (this.matchIP(ip, entry)) {
        const isAllowlist = config.mode === 'allowlist';
        return {
          allowed: isAllowlist,
          ip,
          matchedEntry: entry,
          reason: isAllowlist ? 'IP in allowlist' : 'IP in blocklist',
        };
      }
    }

    // No match - use default action
    const allowed = config.defaultAction === 'allow';
    return {
      allowed,
      ip,
      reason: allowed ? 'Default action: allow' : 'IP not in allowlist',
    };
  }

  /**
   * Bulk check IPs
   */
  async checkIPs(tokenId: string, ips: string[]): Promise<Map<string, IPCheckResult>> {
    const results = new Map<string, IPCheckResult>();

    for (const ip of ips) {
      results.set(ip, await this.checkIP(tokenId, ip));
    }

    return results;
  }

  /**
   * Log denied access attempt
   */
  async logDeniedAccess(
    tokenId: string,
    ip: string,
    details: {
      endpoint?: string;
      userAgent?: string;
      requestId?: string;
    }
  ): Promise<void> {
    const key = `${this.prefix}:denied:${tokenId}:${Date.now()}`;
    await this.kv.put(key, JSON.stringify({
      ip,
      tokenId,
      timestamp: new Date().toISOString(),
      ...details,
    }), {
      expirationTtl: 60 * 60 * 24 * 30, // 30 days
    });
  }

  /**
   * Get denied access attempts
   */
  async getDeniedAttempts(
    tokenId: string,
    limit = 50
  ): Promise<Array<{
    ip: string;
    timestamp: string;
    endpoint?: string;
    userAgent?: string;
    requestId?: string;
  }>> {
    const list = await this.kv.list({
      prefix: `${this.prefix}:denied:${tokenId}:`,
      limit,
    });

    const attempts: Array<{
      ip: string;
      timestamp: string;
      endpoint?: string;
      userAgent?: string;
      requestId?: string;
    }> = [];

    for (const key of list.keys) {
      const data = await this.kv.get(key.name);
      if (data) {
        attempts.push(JSON.parse(data));
      }
    }

    return attempts.sort((a, b) =>
      new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime()
    );
  }

  /**
   * Enable allowlist for token
   */
  async enable(tokenId: string): Promise<IPAllowlistConfig | null> {
    return this.configureAllowlist(tokenId, { enabled: true });
  }

  /**
   * Disable allowlist for token
   */
  async disable(tokenId: string): Promise<IPAllowlistConfig | null> {
    return this.configureAllowlist(tokenId, { enabled: false });
  }

  /**
   * Delete allowlist configuration
   */
  async deleteConfig(tokenId: string): Promise<boolean> {
    await this.kv.delete(`${this.prefix}:${tokenId}`);
    return true;
  }

  // Private helpers

  private detectIPType(ip: string): 'single' | 'range' | 'cidr' {
    if (ip.includes('/')) return 'cidr';
    if (ip.includes('-')) return 'range';
    return 'single';
  }

  private matchIP(ip: string, entry: IPAllowlistEntry): boolean {
    switch (entry.type) {
      case 'single':
        return ip === entry.ip;
      case 'range':
        return this.isIPInRange(ip, entry.ip);
      case 'cidr':
        return this.isIPInCIDR(ip, entry.ip);
      default:
        return false;
    }
  }

  private isIPInRange(ip: string, range: string): boolean {
    const [start, end] = range.split('-').map(s => s.trim());
    const ipNum = this.ipToNumber(ip);
    const startNum = this.ipToNumber(start);
    const endNum = this.ipToNumber(end);
    return ipNum >= startNum && ipNum <= endNum;
  }

  private isIPInCIDR(ip: string, cidr: string): boolean {
    const [network, prefixStr] = cidr.split('/');
    const prefix = parseInt(prefixStr, 10);

    const ipNum = this.ipToNumber(ip);
    const networkNum = this.ipToNumber(network);

    // Create mask
    const mask = ~((1 << (32 - prefix)) - 1) >>> 0;

    return (ipNum & mask) === (networkNum & mask);
  }

  private ipToNumber(ip: string): number {
    return ip.split('.').reduce((acc, octet) => (acc << 8) + parseInt(octet, 10), 0) >>> 0;
  }
}

/**
 * Create IP allowlist service from environment
 */
export function createIPAllowlistService(env: Env): IPAllowlistService {
  return new IPAllowlistService(env.EMAIL_KV);
}

/**
 * IP allowlist middleware
 */
export function ipAllowlistMiddleware(allowlistService: IPAllowlistService) {
  return async (c: any, next: () => Promise<void>) => {
    const tokenId = c.get('tokenId');
    if (!tokenId) {
      await next();
      return;
    }

    const ip = c.req.header('CF-Connecting-IP') ||
               c.req.header('X-Forwarded-For')?.split(',')[0]?.trim() ||
               'unknown';

    const result = await allowlistService.checkIP(tokenId, ip);

    if (!result.allowed) {
      // Log the denied attempt
      await allowlistService.logDeniedAccess(tokenId, ip, {
        endpoint: c.req.path,
        userAgent: c.req.header('User-Agent'),
        requestId: c.get('requestId'),
      });

      return c.json({
        success: false,
        error: {
          code: 'IP_NOT_ALLOWED',
          message: 'Access denied: IP address not in allowlist',
        },
      }, 403);
    }

    await next();
  };
}
