/**
 * API Key Authentication System
 * 
 * Manages API keys for programmatic access to GABRIEL
 * Supports scoped permissions and usage tracking
 */

interface APIKey {
  id: string;
  userId: string;
  name: string;
  keyHash: string;
  prefix: string;  // First 8 chars for identification
  permissions: Permission[];
  rateLimit: number;  // Requests per minute
  createdAt: string;
  lastUsed?: string;
  expiresAt?: string;
  active: boolean;
}

type Permission = 
  | 'scan:read'
  | 'scan:write'
  | 'reference:read'
  | 'reference:write'
  | 'webhook:manage'
  | 'analytics:read'
  | 'admin:all';

interface APIKeyUsage {
  keyId: string;
  date: string;
  requests: number;
  scans: number;
  errors: number;
}

// ============================================================================
// API KEY MANAGER
// ============================================================================

export class APIKeyManager {
  private kv: KVNamespace;

  constructor(kv: KVNamespace) {
    this.kv = kv;
  }

  /**
   * Generate a new API key
   */
  async createKey(
    userId: string,
    name: string,
    permissions: Permission[],
    options: { rateLimit?: number; expiresIn?: number } = {}
  ): Promise<{ key: string; apiKey: APIKey }> {
    // Generate key: gab_live_xxxxxxxxxxxxxxxxxxxx
    const rawKey = this.generateRawKey();
    const key = `gab_live_${rawKey}`;
    const prefix = key.substring(0, 12);
    const keyHash = await this.hashKey(key);

    const apiKey: APIKey = {
      id: `key_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`,
      userId,
      name,
      keyHash,
      prefix,
      permissions,
      rateLimit: options.rateLimit || 60,
      createdAt: new Date().toISOString(),
      expiresAt: options.expiresIn 
        ? new Date(Date.now() + options.expiresIn).toISOString()
        : undefined,
      active: true,
    };

    // Store by hash for lookup
    await this.kv.put(`apikey:hash:${keyHash}`, JSON.stringify(apiKey));
    
    // Store by ID for management
    await this.kv.put(`apikey:id:${apiKey.id}`, JSON.stringify(apiKey));

    // Index by user
    const userKeys = await this.getUserKeys(userId);
    userKeys.push(apiKey.id);
    await this.kv.put(`user:${userId}:apikeys`, JSON.stringify(userKeys));

    // Return key only once - never stored in plain text
    return { key, apiKey: { ...apiKey, keyHash: '***' } };
  }

  /**
   * Validate an API key and return its config
   */
  async validateKey(key: string): Promise<APIKey | null> {
    if (!key.startsWith('gab_live_')) return null;

    const keyHash = await this.hashKey(key);
    const apiKey = await this.kv.get<APIKey>(`apikey:hash:${keyHash}`, 'json');
    
    if (!apiKey) return null;
    if (!apiKey.active) return null;
    if (apiKey.expiresAt && new Date(apiKey.expiresAt) < new Date()) {
      return null;
    }

    // Update last used
    apiKey.lastUsed = new Date().toISOString();
    await this.kv.put(`apikey:hash:${keyHash}`, JSON.stringify(apiKey));
    await this.kv.put(`apikey:id:${apiKey.id}`, JSON.stringify(apiKey));

    // Track usage
    await this.trackUsage(apiKey.id);

    return apiKey;
  }

  /**
   * Check if key has permission
   */
  hasPermission(apiKey: APIKey, permission: Permission): boolean {
    if (apiKey.permissions.includes('admin:all')) return true;
    return apiKey.permissions.includes(permission);
  }

  /**
   * Get all keys for a user
   */
  async getUserKeys(userId: string): Promise<string[]> {
    const data = await this.kv.get(`user:${userId}:apikeys`, 'json');
    return (data as string[]) || [];
  }

  /**
   * Get key by ID
   */
  async getKeyById(keyId: string): Promise<APIKey | null> {
    return this.kv.get(`apikey:id:${keyId}`, 'json');
  }

  /**
   * List all keys for a user (safe version without hashes)
   */
  async listKeys(userId: string): Promise<Omit<APIKey, 'keyHash'>[]> {
    const keyIds = await this.getUserKeys(userId);
    const keys = await Promise.all(
      keyIds.map(id => this.getKeyById(id))
    );
    
    return keys
      .filter((k): k is APIKey => k !== null)
      .map(k => ({ ...k, keyHash: '***' }));
  }

  /**
   * Revoke an API key
   */
  async revokeKey(keyId: string, userId: string): Promise<boolean> {
    const apiKey = await this.getKeyById(keyId);
    if (!apiKey || apiKey.userId !== userId) return false;

    // Soft delete - mark as inactive
    apiKey.active = false;
    await this.kv.put(`apikey:hash:${apiKey.keyHash}`, JSON.stringify(apiKey));
    await this.kv.put(`apikey:id:${keyId}`, JSON.stringify(apiKey));

    return true;
  }

  /**
   * Delete an API key permanently
   */
  async deleteKey(keyId: string, userId: string): Promise<boolean> {
    const apiKey = await this.getKeyById(keyId);
    if (!apiKey || apiKey.userId !== userId) return false;

    await this.kv.delete(`apikey:hash:${apiKey.keyHash}`);
    await this.kv.delete(`apikey:id:${keyId}`);

    // Remove from user index
    const userKeys = await this.getUserKeys(userId);
    const filtered = userKeys.filter(id => id !== keyId);
    await this.kv.put(`user:${userId}:apikeys`, JSON.stringify(filtered));

    return true;
  }

  /**
   * Track usage statistics
   */
  private async trackUsage(keyId: string, isError = false, isScan = false): Promise<void> {
    const date = new Date().toISOString().split('T')[0];
    const key = `apikey:usage:${keyId}:${date}`;
    
    const usage = await this.kv.get<APIKeyUsage>(key, 'json') || {
      keyId,
      date,
      requests: 0,
      scans: 0,
      errors: 0,
    };

    usage.requests++;
    if (isError) usage.errors++;
    if (isScan) usage.scans++;

    await this.kv.put(key, JSON.stringify(usage), {
      expirationTtl: 90 * 24 * 60 * 60, // 90 days
    });
  }

  /**
   * Get usage statistics for a key
   */
  async getUsage(keyId: string, days = 30): Promise<APIKeyUsage[]> {
    const usage: APIKeyUsage[] = [];
    const now = new Date();

    for (let i = 0; i < days; i++) {
      const date = new Date(now);
      date.setDate(date.getDate() - i);
      const dateStr = date.toISOString().split('T')[0];
      
      const dayUsage = await this.kv.get<APIKeyUsage>(
        `apikey:usage:${keyId}:${dateStr}`,
        'json'
      );
      
      if (dayUsage) usage.push(dayUsage);
    }

    return usage;
  }

  /**
   * Generate raw key bytes
   */
  private generateRawKey(): string {
    const array = new Uint8Array(24);
    crypto.getRandomValues(array);
    return Array.from(array, b => b.toString(16).padStart(2, '0')).join('');
  }

  /**
   * Hash key for storage
   */
  private async hashKey(key: string): Promise<string> {
    const encoder = new TextEncoder();
    const data = encoder.encode(key);
    const hashBuffer = await crypto.subtle.digest('SHA-256', data);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
  }
}

// ============================================================================
// AUTH MIDDLEWARE
// ============================================================================

export function createAuthMiddleware(keyManager: APIKeyManager) {
  return async function authMiddleware(
    request: Request
  ): Promise<{ apiKey: APIKey } | Response> {
    // Check Authorization header
    const authHeader = request.headers.get('Authorization');
    const apiKeyHeader = request.headers.get('X-API-Key');
    
    let key: string | null = null;
    
    if (authHeader?.startsWith('Bearer ')) {
      key = authHeader.substring(7);
    } else if (apiKeyHeader) {
      key = apiKeyHeader;
    }

    if (!key) {
      return new Response(JSON.stringify({
        error: 'Unauthorized',
        message: 'API key required. Use Authorization: Bearer <key> or X-API-Key header.',
      }), {
        status: 401,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    const apiKey = await keyManager.validateKey(key);
    
    if (!apiKey) {
      return new Response(JSON.stringify({
        error: 'Unauthorized',
        message: 'Invalid or expired API key.',
      }), {
        status: 401,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    return { apiKey };
  };
}

/**
 * Check permission middleware
 */
export function requirePermission(apiKey: APIKey, permission: Permission): Response | null {
  const keyManager = new APIKeyManager({} as KVNamespace);
  
  if (!keyManager.hasPermission(apiKey, permission)) {
    return new Response(JSON.stringify({
      error: 'Forbidden',
      message: `This API key does not have the '${permission}' permission.`,
      required: permission,
      granted: apiKey.permissions,
    }), {
      status: 403,
      headers: { 'Content-Type': 'application/json' },
    });
  }
  
  return null;
}

// ============================================================================
// API ROUTES
// ============================================================================

export function createAPIKeyRoutes(manager: APIKeyManager) {
  return {
    // List keys
    async list(userId: string): Promise<Response> {
      const keys = await manager.listKeys(userId);
      return new Response(JSON.stringify({ keys }), {
        headers: { 'Content-Type': 'application/json' },
      });
    },

    // Create key
    async create(userId: string, request: Request): Promise<Response> {
      const body = await request.json() as {
        name: string;
        permissions: Permission[];
        rateLimit?: number;
        expiresIn?: number;
      };

      if (!body.name || !body.permissions?.length) {
        return new Response(JSON.stringify({
          error: 'Name and permissions required',
        }), {
          status: 400,
          headers: { 'Content-Type': 'application/json' },
        });
      }

      const result = await manager.createKey(
        userId,
        body.name,
        body.permissions,
        {
          rateLimit: body.rateLimit,
          expiresIn: body.expiresIn,
        }
      );

      return new Response(JSON.stringify({
        key: result.key,
        apiKey: result.apiKey,
        warning: 'Store this key securely. It will not be shown again.',
      }), {
        status: 201,
        headers: { 'Content-Type': 'application/json' },
      });
    },

    // Revoke key
    async revoke(userId: string, keyId: string): Promise<Response> {
      const revoked = await manager.revokeKey(keyId, userId);
      
      if (!revoked) {
        return new Response(JSON.stringify({ error: 'Key not found' }), {
          status: 404,
          headers: { 'Content-Type': 'application/json' },
        });
      }

      return new Response(JSON.stringify({ success: true }), {
        headers: { 'Content-Type': 'application/json' },
      });
    },

    // Get usage
    async usage(userId: string, keyId: string): Promise<Response> {
      const key = await manager.getKeyById(keyId);
      
      if (!key || key.userId !== userId) {
        return new Response(JSON.stringify({ error: 'Key not found' }), {
          status: 404,
          headers: { 'Content-Type': 'application/json' },
        });
      }

      const usage = await manager.getUsage(keyId);
      
      return new Response(JSON.stringify({ usage }), {
        headers: { 'Content-Type': 'application/json' },
      });
    },
  };
}

export default {
  APIKeyManager,
  createAuthMiddleware,
  requirePermission,
  createAPIKeyRoutes,
};
