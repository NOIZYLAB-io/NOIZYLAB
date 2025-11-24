/**
 * NOIZYLAB Email System - Custom Error Classes
 * Provides structured error handling across the application
 */

import type { EmailErrorCode } from '../types';

/**
 * Base error class for all NOIZYLAB errors
 */
export abstract class NoizylabError extends Error {
  abstract readonly code: EmailErrorCode;
  abstract readonly statusCode: number;
  readonly details?: Record<string, unknown>;
  readonly timestamp: string;

  constructor(message: string, details?: Record<string, unknown>) {
    super(message);
    this.name = this.constructor.name;
    this.details = details;
    this.timestamp = new Date().toISOString();
    Error.captureStackTrace?.(this, this.constructor);
  }

  toJSON(): Record<string, unknown> {
    return {
      success: false,
      error: {
        code: this.code,
        message: this.message,
        details: this.details,
      },
      timestamp: this.timestamp,
    };
  }
}

/**
 * Validation error for invalid input data
 */
export class ValidationError extends NoizylabError {
  readonly code = 'VALIDATION_ERROR' as const;
  readonly statusCode = 400;

  constructor(message: string, details?: Record<string, unknown>) {
    super(message, details);
  }
}

/**
 * Rate limit exceeded error
 */
export class RateLimitError extends NoizylabError {
  readonly code = 'RATE_LIMIT_EXCEEDED' as const;
  readonly statusCode = 429;
  readonly retryAfter: number;

  constructor(message: string, retryAfter: number, details?: Record<string, unknown>) {
    super(message, { ...details, retryAfter });
    this.retryAfter = retryAfter;
  }
}

/**
 * Authentication error for invalid credentials
 */
export class AuthenticationError extends NoizylabError {
  readonly code = 'AUTHENTICATION_ERROR' as const;
  readonly statusCode = 401;

  constructor(message: string = 'Authentication failed', details?: Record<string, unknown>) {
    super(message, details);
  }
}

/**
 * Provider error for email service failures
 */
export class ProviderError extends NoizylabError {
  readonly code = 'PROVIDER_ERROR' as const;
  readonly statusCode = 502;
  readonly provider: string;

  constructor(provider: string, message: string, details?: Record<string, unknown>) {
    super(message, { ...details, provider });
    this.provider = provider;
  }
}

/**
 * Template not found error
 */
export class TemplateNotFoundError extends NoizylabError {
  readonly code = 'TEMPLATE_NOT_FOUND' as const;
  readonly statusCode = 404;
  readonly templateId: string;

  constructor(templateId: string) {
    super(`Template not found: ${templateId}`, { templateId });
    this.templateId = templateId;
  }
}

/**
 * Template render error
 */
export class TemplateRenderError extends NoizylabError {
  readonly code = 'TEMPLATE_RENDER_ERROR' as const;
  readonly statusCode = 400;
  readonly templateId: string;

  constructor(templateId: string, message: string, details?: Record<string, unknown>) {
    super(message, { ...details, templateId });
    this.templateId = templateId;
  }
}

/**
 * Attachment too large error
 */
export class AttachmentTooLargeError extends NoizylabError {
  readonly code = 'ATTACHMENT_TOO_LARGE' as const;
  readonly statusCode = 413;
  readonly maxSize: number;
  readonly actualSize: number;

  constructor(maxSize: number, actualSize: number) {
    super(`Attachment exceeds maximum size of ${maxSize} bytes`, {
      maxSize,
      actualSize,
    });
    this.maxSize = maxSize;
    this.actualSize = actualSize;
  }
}

/**
 * Recipient blocked error
 */
export class RecipientBlockedError extends NoizylabError {
  readonly code = 'RECIPIENT_BLOCKED' as const;
  readonly statusCode = 400;
  readonly recipient: string;
  readonly reason: string;

  constructor(recipient: string, reason: string) {
    super(`Recipient is blocked: ${recipient}`, { recipient, reason });
    this.recipient = recipient;
    this.reason = reason;
  }
}

/**
 * Internal server error
 */
export class InternalError extends NoizylabError {
  readonly code = 'INTERNAL_ERROR' as const;
  readonly statusCode = 500;

  constructor(message: string = 'Internal server error', details?: Record<string, unknown>) {
    super(message, details);
  }
}

/**
 * Idempotency conflict error
 */
export class IdempotencyConflictError extends NoizylabError {
  readonly code = 'IDEMPOTENCY_CONFLICT' as const;
  readonly statusCode = 409;
  readonly idempotencyKey: string;

  constructor(idempotencyKey: string, existingMessageId: string) {
    super(`Request with idempotency key already processed`, {
      idempotencyKey,
      existingMessageId,
    });
    this.idempotencyKey = idempotencyKey;
  }
}

/**
 * Type guard to check if an error is a NoizylabError
 */
export function isNoizylabError(error: unknown): error is NoizylabError {
  return error instanceof NoizylabError;
}

/**
 * Convert unknown error to NoizylabError
 */
export function toNoizylabError(error: unknown): NoizylabError {
  if (isNoizylabError(error)) {
    return error;
  }

  if (error instanceof Error) {
    return new InternalError(error.message, {
      originalError: error.name,
      stack: error.stack,
    });
  }

  return new InternalError('An unknown error occurred', {
    originalError: String(error),
  });
}
