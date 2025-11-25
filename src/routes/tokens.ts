/**
 * NOIZYLAB Token Management API Routes
 * Complete API for managing API tokens with full CRUD operations
 */

import { Hono } from 'hono';
import { z } from 'zod';
import {
  APIKeyService,
  type APIKeyScope,
  type CreateAPIKeyInput,
  scopeDescriptions
} from '../services/api-key-service';
import { ValidationError, AuthenticationError, NotFoundError } from '../errors';
import type { Env, Variables } from '../types';

// Validation schemas
const CreateTokenSchema = z.object({
  name: z.string().min(1).max(100),
  scopes: z.array(z.enum([
    'email:send',
    'email:read',
    'email:delete',
    'templates:read',
    'templates:write',
    'templates:delete',
    'analytics:read',
    'webhooks:manage',
    'suppression:manage',
    'batch:send',
    'api-keys:manage',
    'admin:full'
  ])).min(1),
  expiresInDays: z.number().int().min(1).max(365).optional(),
  rateLimit: z.number().int().min(1).max(100000).optional(),
  allowedIPs: z.array(z.string().ip()).optional(),
  metadata: z.record(z.string()).optional(),
});

const UpdateTokenSchema = z.object({
  name: z.string().min(1).max(100).optional(),
  scopes: z.array(z.enum([
    'email:send',
    'email:read',
    'email:delete',
    'templates:read',
    'templates:write',
    'templates:delete',
    'analytics:read',
    'webhooks:manage',
    'suppression:manage',
    'batch:send',
    'api-keys:manage',
    'admin:full'
  ])).min(1).optional(),
  rateLimit: z.number().int().min(1).max(100000).optional(),
  allowedIPs: z.array(z.string().ip()).optional(),
  metadata: z.record(z.string()).optional(),
});

const ListTokensSchema = z.object({
  limit: z.coerce.number().int().min(1).max(100).default(20),
  cursor: z.string().optional(),
  includeInactive: z.coerce.boolean().default(false),
});

// Create router
const tokens = new Hono<{ Bindings: Env; Variables: Variables }>();

/**
 * GET /tokens
 * List all API tokens
 */
tokens.get('/', async (c) => {
  const apiKeyService = c.get('apiKeyService');
  const query = c.req.query();

  const parsed = ListTokensSchema.safeParse(query);
  if (!parsed.success) {
    throw new ValidationError('Invalid query parameters', parsed.error.flatten().fieldErrors);
  }

  const { limit, cursor, includeInactive } = parsed.data;

  const result = await apiKeyService.listKeys({ limit, cursor });

  // Filter inactive if needed
  const keys = includeInactive
    ? result.keys
    : result.keys.filter(k => k.isActive);

  // Mask sensitive data
  const safeKeys = keys.map(key => ({
    id: key.id,
    name: key.name,
    scopes: key.scopes,
    isActive: key.isActive,
    createdAt: key.createdAt,
    lastUsedAt: key.lastUsedAt,
    expiresAt: key.expiresAt,
    rateLimit: key.rateLimit,
    metadata: key.metadata,
    // Show masked prefix only
    keyPrefix: `nz_${key.id.substring(0, 8)}...`,
  }));

  return c.json({
    success: true,
    data: {
      tokens: safeKeys,
      cursor: result.cursor,
      total: safeKeys.length,
    },
    meta: {
      requestId: c.get('requestId'),
    },
  });
});

/**
 * GET /tokens/scopes
 * Get available scopes and descriptions
 */
tokens.get('/scopes', async (c) => {
  const scopes = Object.entries(scopeDescriptions).map(([scope, description]) => ({
    scope,
    description,
    category: scope.split(':')[0],
  }));

  return c.json({
    success: true,
    data: { scopes },
  });
});

/**
 * GET /tokens/:id
 * Get a specific token by ID
 */
tokens.get('/:id', async (c) => {
  const apiKeyService = c.get('apiKeyService');
  const { id } = c.req.param();

  const key = await apiKeyService.getKey(id);

  if (!key) {
    throw new NotFoundError('Token not found');
  }

  // Get usage stats
  const stats = await apiKeyService.getKeyStats(id);

  return c.json({
    success: true,
    data: {
      token: {
        id: key.id,
        name: key.name,
        scopes: key.scopes,
        isActive: key.isActive,
        createdAt: key.createdAt,
        lastUsedAt: key.lastUsedAt,
        expiresAt: key.expiresAt,
        rateLimit: key.rateLimit,
        metadata: key.metadata,
        keyPrefix: `nz_${key.id.substring(0, 8)}...`,
      },
      stats,
    },
  });
});

/**
 * POST /tokens
 * Create a new API token
 */
tokens.post('/', async (c) => {
  const apiKeyService = c.get('apiKeyService');
  const body = await c.req.json();

  const parsed = CreateTokenSchema.safeParse(body);
  if (!parsed.success) {
    throw new ValidationError('Invalid token data', parsed.error.flatten().fieldErrors);
  }

  const { name, scopes, expiresInDays, rateLimit, allowedIPs, metadata } = parsed.data;

  // Calculate expiration date
  let expiresAt: string | undefined;
  if (expiresInDays) {
    const expDate = new Date();
    expDate.setDate(expDate.getDate() + expiresInDays);
    expiresAt = expDate.toISOString();
  }

  const input: CreateAPIKeyInput = {
    name,
    scopes: scopes as APIKeyScope[],
    expiresAt,
    rateLimit,
    metadata: {
      ...metadata,
      allowedIPs: allowedIPs?.join(','),
    },
  };

  const result = await apiKeyService.createKey(input);

  // Log token creation
  await logTokenEvent(c.env, {
    event: 'token.created',
    tokenId: result.key.id,
    tokenName: name,
    scopes,
    createdBy: c.get('clientId') || 'system',
    ip: c.req.header('CF-Connecting-IP') || 'unknown',
  });

  return c.json({
    success: true,
    data: {
      token: {
        id: result.key.id,
        name: result.key.name,
        scopes: result.key.scopes,
        createdAt: result.key.createdAt,
        expiresAt: result.key.expiresAt,
      },
      // IMPORTANT: This is the only time the raw key is shown!
      rawKey: result.rawKey,
      warning: 'Save this token now! It will not be shown again.',
    },
    meta: {
      requestId: c.get('requestId'),
    },
  }, 201);
});

/**
 * PATCH /tokens/:id
 * Update a token
 */
tokens.patch('/:id', async (c) => {
  const apiKeyService = c.get('apiKeyService');
  const { id } = c.req.param();
  const body = await c.req.json();

  const parsed = UpdateTokenSchema.safeParse(body);
  if (!parsed.success) {
    throw new ValidationError('Invalid update data', parsed.error.flatten().fieldErrors);
  }

  const existing = await apiKeyService.getKey(id);
  if (!existing) {
    throw new NotFoundError('Token not found');
  }

  const { name, scopes, rateLimit, allowedIPs, metadata } = parsed.data;

  const updated = await apiKeyService.updateKey(id, {
    name,
    scopes: scopes as APIKeyScope[] | undefined,
    rateLimit,
    metadata: {
      ...existing.metadata,
      ...metadata,
      ...(allowedIPs && { allowedIPs: allowedIPs.join(',') }),
    },
  });

  if (!updated) {
    throw new NotFoundError('Token not found');
  }

  // Log update
  await logTokenEvent(c.env, {
    event: 'token.updated',
    tokenId: id,
    changes: parsed.data,
    updatedBy: c.get('clientId') || 'system',
    ip: c.req.header('CF-Connecting-IP') || 'unknown',
  });

  return c.json({
    success: true,
    data: {
      token: {
        id: updated.id,
        name: updated.name,
        scopes: updated.scopes,
        isActive: updated.isActive,
        updatedAt: new Date().toISOString(),
      },
    },
  });
});

/**
 * POST /tokens/:id/rotate
 * Rotate a token (create new, deactivate old)
 */
tokens.post('/:id/rotate', async (c) => {
  const apiKeyService = c.get('apiKeyService');
  const { id } = c.req.param();

  const result = await apiKeyService.rotateKey(id);

  if (!result) {
    throw new NotFoundError('Token not found');
  }

  // Log rotation
  await logTokenEvent(c.env, {
    event: 'token.rotated',
    oldTokenId: id,
    newTokenId: result.key.id,
    rotatedBy: c.get('clientId') || 'system',
    ip: c.req.header('CF-Connecting-IP') || 'unknown',
  });

  return c.json({
    success: true,
    data: {
      token: {
        id: result.key.id,
        name: result.key.name,
        scopes: result.key.scopes,
        createdAt: result.key.createdAt,
      },
      rawKey: result.rawKey,
      warning: 'Save this new token now! The old token has been deactivated.',
      oldTokenId: id,
    },
  });
});

/**
 * POST /tokens/:id/revoke
 * Revoke/deactivate a token
 */
tokens.post('/:id/revoke', async (c) => {
  const apiKeyService = c.get('apiKeyService');
  const { id } = c.req.param();

  const key = await apiKeyService.deactivateKey(id);

  if (!key) {
    throw new NotFoundError('Token not found');
  }

  // Log revocation
  await logTokenEvent(c.env, {
    event: 'token.revoked',
    tokenId: id,
    tokenName: key.name,
    revokedBy: c.get('clientId') || 'system',
    ip: c.req.header('CF-Connecting-IP') || 'unknown',
  });

  return c.json({
    success: true,
    data: {
      message: 'Token revoked successfully',
      tokenId: id,
      revokedAt: new Date().toISOString(),
    },
  });
});

/**
 * POST /tokens/:id/reactivate
 * Reactivate a previously revoked token
 */
tokens.post('/:id/reactivate', async (c) => {
  const apiKeyService = c.get('apiKeyService');
  const { id } = c.req.param();

  const key = await apiKeyService.reactivateKey(id);

  if (!key) {
    throw new NotFoundError('Token not found');
  }

  // Log reactivation
  await logTokenEvent(c.env, {
    event: 'token.reactivated',
    tokenId: id,
    tokenName: key.name,
    reactivatedBy: c.get('clientId') || 'system',
    ip: c.req.header('CF-Connecting-IP') || 'unknown',
  });

  return c.json({
    success: true,
    data: {
      message: 'Token reactivated successfully',
      token: {
        id: key.id,
        name: key.name,
        isActive: key.isActive,
      },
    },
  });
});

/**
 * DELETE /tokens/:id
 * Permanently delete a token
 */
tokens.delete('/:id', async (c) => {
  const apiKeyService = c.get('apiKeyService');
  const { id } = c.req.param();

  // Get token info before deletion for logging
  const key = await apiKeyService.getKey(id);

  const deleted = await apiKeyService.deleteKey(id);

  if (!deleted) {
    throw new NotFoundError('Token not found');
  }

  // Log deletion
  await logTokenEvent(c.env, {
    event: 'token.deleted',
    tokenId: id,
    tokenName: key?.name || 'unknown',
    deletedBy: c.get('clientId') || 'system',
    ip: c.req.header('CF-Connecting-IP') || 'unknown',
  });

  return c.json({
    success: true,
    data: {
      message: 'Token permanently deleted',
      tokenId: id,
      deletedAt: new Date().toISOString(),
    },
  });
});

/**
 * GET /tokens/:id/stats
 * Get detailed usage statistics for a token
 */
tokens.get('/:id/stats', async (c) => {
  const apiKeyService = c.get('apiKeyService');
  const { id } = c.req.param();

  const key = await apiKeyService.getKey(id);
  if (!key) {
    throw new NotFoundError('Token not found');
  }

  const stats = await apiKeyService.getKeyStats(id);

  // Get additional analytics from KV
  const analytics = await getTokenAnalytics(c.env, id);

  return c.json({
    success: true,
    data: {
      tokenId: id,
      tokenName: key.name,
      stats,
      analytics,
    },
  });
});

/**
 * POST /tokens/:id/test
 * Test a token's validity
 */
tokens.post('/:id/test', async (c) => {
  const apiKeyService = c.get('apiKeyService');
  const { id } = c.req.param();

  const key = await apiKeyService.getKey(id);

  if (!key) {
    return c.json({
      success: true,
      data: {
        valid: false,
        reason: 'Token not found',
      },
    });
  }

  if (!key.isActive) {
    return c.json({
      success: true,
      data: {
        valid: false,
        reason: 'Token is inactive/revoked',
      },
    });
  }

  if (key.expiresAt && new Date(key.expiresAt) < new Date()) {
    return c.json({
      success: true,
      data: {
        valid: false,
        reason: 'Token has expired',
        expiredAt: key.expiresAt,
      },
    });
  }

  return c.json({
    success: true,
    data: {
      valid: true,
      token: {
        id: key.id,
        name: key.name,
        scopes: key.scopes,
        expiresAt: key.expiresAt,
      },
    },
  });
});

/**
 * GET /tokens/audit
 * Get token audit log
 */
tokens.get('/audit/log', async (c) => {
  const limit = parseInt(c.req.query('limit') || '50');
  const tokenId = c.req.query('tokenId');

  const logs = await getTokenAuditLog(c.env, { limit, tokenId });

  return c.json({
    success: true,
    data: {
      logs,
      total: logs.length,
    },
  });
});

// Helper functions

async function logTokenEvent(env: Env, event: Record<string, unknown>): Promise<void> {
  try {
    const logKey = `token:audit:${Date.now()}:${Math.random().toString(36).substr(2, 9)}`;
    await env.EMAIL_KV.put(logKey, JSON.stringify({
      ...event,
      timestamp: new Date().toISOString(),
    }), {
      expirationTtl: 60 * 60 * 24 * 90, // 90 days
    });
  } catch (error) {
    console.error('Failed to log token event:', error);
  }
}

async function getTokenAnalytics(env: Env, tokenId: string): Promise<Record<string, unknown>> {
  try {
    const analyticsKey = `token:analytics:${tokenId}`;
    const data = await env.EMAIL_KV.get(analyticsKey);
    if (data) {
      return JSON.parse(data);
    }
  } catch (error) {
    console.error('Failed to get token analytics:', error);
  }

  return {
    totalRequests: 0,
    last24Hours: 0,
    last7Days: 0,
    last30Days: 0,
    topEndpoints: [],
    errorRate: 0,
  };
}

async function getTokenAuditLog(
  env: Env,
  options: { limit: number; tokenId?: string }
): Promise<Array<Record<string, unknown>>> {
  try {
    const prefix = options.tokenId
      ? `token:audit:`
      : 'token:audit:';

    const list = await env.EMAIL_KV.list({ prefix, limit: options.limit });

    const logs: Array<Record<string, unknown>> = [];

    for (const key of list.keys) {
      const data = await env.EMAIL_KV.get(key.name);
      if (data) {
        const log = JSON.parse(data);
        if (!options.tokenId || log.tokenId === options.tokenId) {
          logs.push(log);
        }
      }
    }

    return logs.sort((a, b) =>
      new Date(b.timestamp as string).getTime() - new Date(a.timestamp as string).getTime()
    );
  } catch (error) {
    console.error('Failed to get audit log:', error);
    return [];
  }
}

export default tokens;
