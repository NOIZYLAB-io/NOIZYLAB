/**
 * NOIZYLAB Email System - Email Routes
 * API endpoints for email operations
 */

import { Hono } from 'hono';
import type { EmailRequest } from '../types';
import {
  isNoizylabError,
  toNoizylabError,
  ValidationError,
} from '../errors';
import { getRateLimitHeaders } from '../services/rate-limiter';
import { generateRequestId, now } from '../utils';

/**
 * Context type with email service
 */
interface EmailContext {
  Variables: {
    emailService: import('../services/email-service').EmailService;
    clientId: string;
    requestId: string;
  };
}

const emailRoutes = new Hono<EmailContext>();

/**
 * POST /emails - Send an email
 */
emailRoutes.post('/', async (c) => {
  const requestId = c.get('requestId');
  const emailService = c.get('emailService');
  const clientId = c.get('clientId');

  try {
    const body = await c.req.json<EmailRequest>();

    const { response, rateLimit } = await emailService.send(body, clientId);

    // Set rate limit headers
    const rateLimitHeaders = getRateLimitHeaders(rateLimit);
    Object.entries(rateLimitHeaders).forEach(([key, value]) => {
      c.header(key, value);
    });

    return c.json(
      {
        success: true,
        data: response,
        meta: {
          requestId,
          timestamp: now(),
          rateLimit: {
            remaining: rateLimit.remaining,
            limit: rateLimit.limit,
            resetAt: rateLimit.resetAt,
          },
        },
      },
      201
    );
  } catch (error) {
    const noizylabError = toNoizylabError(error);

    return c.json(noizylabError.toJSON(), noizylabError.statusCode);
  }
});

/**
 * GET /emails/:messageId - Get email status
 */
emailRoutes.get('/:messageId', async (c) => {
  const requestId = c.get('requestId');
  const emailService = c.get('emailService');
  const messageId = c.req.param('messageId');

  try {
    const log = await emailService.getEmailLog(messageId);

    if (log === null) {
      return c.json(
        {
          success: false,
          error: {
            code: 'NOT_FOUND',
            message: `Email not found: ${messageId}`,
          },
          meta: { requestId, timestamp: now() },
        },
        404
      );
    }

    return c.json({
      success: true,
      data: {
        messageId: log.messageId,
        to: log.to,
        from: log.from,
        subject: log.subject,
        status: log.status,
        provider: log.provider,
        sentAt: log.sentAt,
        deliveredAt: log.deliveredAt,
        bouncedAt: log.bouncedAt,
        errorMessage: log.errorMessage,
        createdAt: log.createdAt,
      },
      meta: { requestId, timestamp: now() },
    });
  } catch (error) {
    const noizylabError = toNoizylabError(error);
    return c.json(noizylabError.toJSON(), noizylabError.statusCode);
  }
});

/**
 * GET /emails - List emails with pagination
 */
emailRoutes.get('/', async (c) => {
  const requestId = c.get('requestId');
  const emailService = c.get('emailService');

  const limit = parseInt(c.req.query('limit') ?? '50', 10);
  const offset = parseInt(c.req.query('offset') ?? '0', 10);
  const status = c.req.query('status') as import('../types').EmailStatus | undefined;
  const from = c.req.query('from');
  const to = c.req.query('to');

  try {
    const { logs, total } = await emailService.listEmailLogs({
      limit: Math.min(limit, 100),
      offset,
      status,
      from,
      to,
    });

    return c.json({
      success: true,
      data: logs.map((log) => ({
        messageId: log.messageId,
        to: log.to,
        from: log.from,
        subject: log.subject,
        status: log.status,
        sentAt: log.sentAt,
        createdAt: log.createdAt,
      })),
      meta: {
        requestId,
        timestamp: now(),
        pagination: {
          total,
          limit,
          offset,
          hasMore: offset + logs.length < total,
        },
      },
    });
  } catch (error) {
    const noizylabError = toNoizylabError(error);
    return c.json(noizylabError.toJSON(), noizylabError.statusCode);
  }
});

export { emailRoutes };
