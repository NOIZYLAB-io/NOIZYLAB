// Generated Cloudflare Worker bindings type definitions

interface Env {
  // Environment variables
  ENVIRONMENT: string;
  APP_NAME: string;
  DEFAULT_FROM_EMAIL: string;
  RATE_LIMIT_MAX_REQUESTS: string;
  RATE_LIMIT_WINDOW_SECONDS: string;

  // Secrets (set via wrangler secret put)
  MAILCHANNELS_API_KEY?: string;
  RESEND_API_KEY?: string;
  SENDGRID_API_KEY?: string;
  DKIM_PRIVATE_KEY?: string;
  DKIM_DOMAIN?: string;
  DKIM_SELECTOR?: string;

  // KV Namespace
  EMAIL_KV: KVNamespace;

  // D1 Database
  EMAIL_DB: D1Database;

  // Queue
  EMAIL_QUEUE: Queue<EmailQueueMessage>;
}

interface EmailQueueMessage {
  id: string;
  to: string | string[];
  from: string;
  subject: string;
  html?: string;
  text?: string;
  replyTo?: string;
  cc?: string[];
  bcc?: string[];
  headers?: Record<string, string>;
  attachments?: EmailAttachment[];
  templateId?: string;
  templateData?: Record<string, unknown>;
  priority?: 'high' | 'normal' | 'low';
  scheduledAt?: string;
  retryCount?: number;
  maxRetries?: number;
}

interface EmailAttachment {
  filename: string;
  content: string;
  contentType: string;
  encoding?: 'base64' | 'utf-8';
}
