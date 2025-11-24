/**
 * NOIZYLAB Email System - Type Definitions
 * Core type definitions for the email system
 */

import { z } from 'zod';

// =============================================================================
// Email Address Validation
// =============================================================================

const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

export const EmailAddressSchema = z.string().regex(emailRegex, 'Invalid email address format');

export const EmailAddressListSchema = z.union([
  EmailAddressSchema,
  z.array(EmailAddressSchema).min(1).max(50),
]);

// =============================================================================
// Email Attachment Schema
// =============================================================================

export const EmailAttachmentSchema = z.object({
  filename: z.string().min(1).max(255),
  content: z.string().min(1),
  contentType: z.string().min(1).max(255),
  encoding: z.enum(['base64', 'utf-8']).optional().default('base64'),
});

export type EmailAttachment = z.infer<typeof EmailAttachmentSchema>;

// =============================================================================
// Email Request Schema
// =============================================================================

export const EmailRequestSchema = z.object({
  to: EmailAddressListSchema,
  from: EmailAddressSchema.optional(),
  subject: z.string().min(1).max(998),
  html: z.string().max(10_000_000).optional(),
  text: z.string().max(10_000_000).optional(),
  replyTo: EmailAddressSchema.optional(),
  cc: z.array(EmailAddressSchema).max(50).optional(),
  bcc: z.array(EmailAddressSchema).max(50).optional(),
  headers: z.record(z.string()).optional(),
  attachments: z.array(EmailAttachmentSchema).max(10).optional(),
  templateId: z.string().min(1).max(100).optional(),
  templateData: z.record(z.unknown()).optional(),
  priority: z.enum(['high', 'normal', 'low']).optional().default('normal'),
  scheduledAt: z.string().datetime().optional(),
  idempotencyKey: z.string().min(1).max(100).optional(),
  tags: z.array(z.string().max(50)).max(10).optional(),
}).refine(
  (data) => data.html !== undefined || data.text !== undefined || data.templateId !== undefined,
  { message: 'Either html, text, or templateId must be provided' }
);

export type EmailRequest = z.infer<typeof EmailRequestSchema>;

// =============================================================================
// Email Response Types
// =============================================================================

export interface EmailResponse {
  success: boolean;
  messageId: string;
  status: EmailStatus;
  timestamp: string;
}

export interface EmailErrorResponse {
  success: false;
  error: {
    code: EmailErrorCode;
    message: string;
    details?: Record<string, unknown>;
  };
  timestamp: string;
}

export type EmailStatus =
  | 'queued'
  | 'sending'
  | 'sent'
  | 'delivered'
  | 'bounced'
  | 'failed'
  | 'scheduled';

export type EmailErrorCode =
  | 'VALIDATION_ERROR'
  | 'RATE_LIMIT_EXCEEDED'
  | 'AUTHENTICATION_ERROR'
  | 'PROVIDER_ERROR'
  | 'TEMPLATE_NOT_FOUND'
  | 'TEMPLATE_RENDER_ERROR'
  | 'ATTACHMENT_TOO_LARGE'
  | 'RECIPIENT_BLOCKED'
  | 'INTERNAL_ERROR'
  | 'IDEMPOTENCY_CONFLICT';

// =============================================================================
// Email Log Types
// =============================================================================

export interface EmailLog {
  id: string;
  messageId: string;
  to: string[];
  from: string;
  subject: string;
  status: EmailStatus;
  provider: EmailProvider;
  templateId?: string;
  tags?: string[];
  metadata?: Record<string, unknown>;
  errorMessage?: string;
  sentAt?: string;
  deliveredAt?: string;
  bouncedAt?: string;
  createdAt: string;
  updatedAt: string;
}

// =============================================================================
// Email Provider Types
// =============================================================================

export type EmailProvider = 'mailchannels' | 'resend' | 'sendgrid' | 'mock';

export interface EmailProviderConfig {
  provider: EmailProvider;
  apiKey?: string;
  endpoint?: string;
  dkim?: DKIMConfig;
}

export interface DKIMConfig {
  privateKey: string;
  domain: string;
  selector: string;
}

// =============================================================================
// Email Template Types
// =============================================================================

export const EmailTemplateSchema = z.object({
  id: z.string().min(1).max(100),
  name: z.string().min(1).max(255),
  subject: z.string().min(1).max(998),
  html: z.string().max(10_000_000).optional(),
  text: z.string().max(10_000_000).optional(),
  variables: z.array(z.string()).optional(),
  createdAt: z.string().datetime(),
  updatedAt: z.string().datetime(),
});

export type EmailTemplate = z.infer<typeof EmailTemplateSchema>;

// =============================================================================
// Rate Limiting Types
// =============================================================================

export interface RateLimitConfig {
  maxRequests: number;
  windowSeconds: number;
}

export interface RateLimitResult {
  allowed: boolean;
  remaining: number;
  resetAt: number;
  limit: number;
}

// =============================================================================
// Queue Types
// =============================================================================

export interface QueueMessage {
  id: string;
  email: EmailRequest;
  attempt: number;
  maxAttempts: number;
  createdAt: string;
  scheduledAt?: string;
}

// =============================================================================
// API Response Types
// =============================================================================

export interface APIResponse<T> {
  success: boolean;
  data?: T;
  error?: {
    code: string;
    message: string;
    details?: Record<string, unknown>;
  };
  meta?: {
    requestId: string;
    timestamp: string;
    rateLimit?: RateLimitResult;
  };
}

// =============================================================================
// Health Check Types
// =============================================================================

export interface HealthCheckResponse {
  status: 'healthy' | 'degraded' | 'unhealthy';
  version: string;
  timestamp: string;
  checks: {
    database: HealthCheckStatus;
    cache: HealthCheckStatus;
    queue: HealthCheckStatus;
    provider: HealthCheckStatus;
  };
}

export interface HealthCheckStatus {
  status: 'pass' | 'warn' | 'fail';
  latencyMs?: number;
  message?: string;
}

// =============================================================================
// Webhook Types
// =============================================================================

export type WebhookEventType =
  | 'email.sent'
  | 'email.delivered'
  | 'email.bounced'
  | 'email.complained'
  | 'email.failed';

export interface WebhookPayload {
  event: WebhookEventType;
  messageId: string;
  timestamp: string;
  data: Record<string, unknown>;
}
