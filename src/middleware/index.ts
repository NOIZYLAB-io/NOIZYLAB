/**
 * NOIZYLAB Email System - Middleware
 * Common middleware for request handling
 */

import { Hono, Context, Next } from 'hono';
import { cors } from 'hono/cors';
import { logger } from 'hono/logger';
import { secureHeaders } from 'hono/secure-headers';
import { timing, startTime, endTime } from 'hono/timing';
import { generateRequestId, now } from '../utils';
import { isNoizylabError, AuthenticationError, InternalError } from '../errors';

/**
 * Request ID middleware - adds unique ID to each request
 */
export function requestIdMiddleware() {
  return async (c: Context, next: Next): Promise<void> => {
    const requestId = c.req.header('X-Request-ID') ?? generateRequestId();
    c.set('requestId', requestId);
    c.header('X-Request-ID', requestId);
    await next();
  };
}

/**
 * API key authentication middleware
 */
export function authMiddleware(apiKeys: Set<string>) {
  return async (c: Context, next: Next): Promise<Response | void> => {
    // Skip auth for health endpoints
    if (c.req.path.startsWith('/health')) {
      await next();
      return;
    }

    const authHeader = c.req.header('Authorization');

    if (authHeader === undefined) {
      const error = new AuthenticationError('Missing Authorization header');
      return c.json(error.toJSON(), error.statusCode);
    }

    const [scheme, token] = authHeader.split(' ');

    if (scheme !== 'Bearer' || token === undefined) {
      const error = new AuthenticationError('Invalid Authorization header format');
      return c.json(error.toJSON(), error.statusCode);
    }

    if (!apiKeys.has(token)) {
      const error = new AuthenticationError('Invalid API key');
      return c.json(error.toJSON(), error.statusCode);
    }

    // Set client ID from API key (could be mapped to actual client)
    c.set('clientId', token.slice(0, 8));

    await next();
  };
}

/**
 * Error handling middleware
 */
export function errorMiddleware() {
  return async (c: Context, next: Next): Promise<Response | void> => {
    try {
      await next();
    } catch (error) {
      console.error('Unhandled error:', error);

      if (isNoizylabError(error)) {
        return c.json(error.toJSON(), error.statusCode);
      }

      const internalError = new InternalError(
        error instanceof Error ? error.message : 'An unexpected error occurred'
      );

      return c.json(internalError.toJSON(), internalError.statusCode);
    }
  };
}

/**
 * Request validation middleware - ensures JSON content type for POST/PUT/PATCH
 */
export function contentTypeMiddleware() {
  return async (c: Context, next: Next): Promise<Response | void> => {
    const method = c.req.method;
    const contentType = c.req.header('Content-Type');

    if (['POST', 'PUT', 'PATCH'].includes(method)) {
      if (contentType === undefined || !contentType.includes('application/json')) {
        return c.json(
          {
            success: false,
            error: {
              code: 'INVALID_CONTENT_TYPE',
              message: 'Content-Type must be application/json',
            },
            timestamp: now(),
          },
          415
        );
      }
    }

    await next();
  };
}

/**
 * Response time header middleware
 */
export function responseTimeMiddleware() {
  return async (c: Context, next: Next): Promise<void> => {
    const startTime = Date.now();
    await next();
    const duration = Date.now() - startTime;
    c.header('X-Response-Time', `${duration}ms`);
  };
}

/**
 * Not found handler
 */
export function notFoundHandler(c: Context): Response {
  return c.json(
    {
      success: false,
      error: {
        code: 'NOT_FOUND',
        message: `Route not found: ${c.req.method} ${c.req.path}`,
      },
      timestamp: now(),
    },
    404
  );
}

/**
 * Apply all middleware to a Hono app
 */
export function applyMiddleware(app: Hono, config: { apiKeys?: Set<string> } = {}): void {
  // Security headers
  app.use('*', secureHeaders());

  // CORS
  app.use(
    '*',
    cors({
      origin: '*',
      allowMethods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
      allowHeaders: ['Content-Type', 'Authorization', 'X-Request-ID', 'X-Idempotency-Key'],
      exposeHeaders: [
        'X-Request-ID',
        'X-Response-Time',
        'X-RateLimit-Limit',
        'X-RateLimit-Remaining',
        'X-RateLimit-Reset',
        'Retry-After',
      ],
      maxAge: 86400,
    })
  );

  // Request timing
  app.use('*', timing());

  // Response time
  app.use('*', responseTimeMiddleware());

  // Request ID
  app.use('*', requestIdMiddleware());

  // Error handling
  app.use('*', errorMiddleware());

  // Content type validation
  app.use('*', contentTypeMiddleware());

  // Authentication (if API keys provided)
  if (config.apiKeys !== undefined && config.apiKeys.size > 0) {
    app.use('*', authMiddleware(config.apiKeys));
  }

  // Not found handler
  app.notFound(notFoundHandler);
}
