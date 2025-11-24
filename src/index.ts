/**
 * NOIZYLAB Email System - Main Entry Point
 * Cloudflare Workers entry point using Hono framework
 */

import { Hono } from 'hono';
import { emailRoutes, templateRoutes, healthRoutes } from './routes';
import { applyMiddleware } from './middleware';
import {
  createProviders,
  createRateLimiter,
  createTemplateEngine,
  createEmailService,
} from './services';
import { generateRequestId } from './utils';

/**
 * Application type with bindings
 */
type AppBindings = {
  Bindings: Env;
  Variables: {
    emailService: ReturnType<typeof createEmailService>;
    templateEngine: ReturnType<typeof createTemplateEngine>;
    kv: KVNamespace;
    db: D1Database;
    clientId: string;
    requestId: string;
  };
};

/**
 * Create the Hono application
 */
function createApp(): Hono<AppBindings> {
  const app = new Hono<AppBindings>();

  // Apply middleware
  applyMiddleware(app);

  // Initialize services middleware
  app.use('*', async (c, next) => {
    const env = c.env;

    // Create services
    const providers = createProviders(env);
    const rateLimiter = createRateLimiter(env.EMAIL_KV, env);
    const templateEngine = createTemplateEngine(env.EMAIL_KV);
    const emailService = createEmailService(providers, rateLimiter, templateEngine, env);

    // Set context variables
    c.set('emailService', emailService);
    c.set('templateEngine', templateEngine);
    c.set('kv', env.EMAIL_KV);
    c.set('db', env.EMAIL_DB);

    // Set default client ID if not set by auth middleware
    if (c.get('clientId') === undefined) {
      c.set('clientId', 'anonymous');
    }

    // Set request ID if not set
    if (c.get('requestId') === undefined) {
      c.set('requestId', generateRequestId());
    }

    await next();
  });

  // Mount routes
  app.route('/emails', emailRoutes);
  app.route('/templates', templateRoutes);
  app.route('/health', healthRoutes);

  // Root endpoint
  app.get('/', (c) => {
    return c.json({
      name: 'NOIZYLAB Email System',
      version: '1.0.0',
      documentation: '/docs',
      endpoints: {
        emails: '/emails',
        templates: '/templates',
        health: '/health',
      },
    });
  });

  return app;
}

// Create app instance
const app = createApp();

/**
 * Queue handler for async email processing
 */
async function handleQueue(
  batch: MessageBatch<EmailQueueMessage>,
  env: Env,
  _ctx: ExecutionContext
): Promise<void> {
  const providers = createProviders(env);
  const rateLimiter = createRateLimiter(env.EMAIL_KV, env);
  const templateEngine = createTemplateEngine(env.EMAIL_KV);
  const emailService = createEmailService(providers, rateLimiter, templateEngine, env);

  for (const message of batch.messages) {
    try {
      const queueMessage = message.body;

      // Convert queue message to email request
      const emailRequest = {
        to: queueMessage.to,
        from: queueMessage.from,
        subject: queueMessage.subject,
        html: queueMessage.html,
        text: queueMessage.text,
        replyTo: queueMessage.replyTo,
        cc: queueMessage.cc,
        bcc: queueMessage.bcc,
        headers: queueMessage.headers,
        attachments: queueMessage.attachments,
        templateId: queueMessage.templateId,
        templateData: queueMessage.templateData,
        priority: queueMessage.priority,
      };

      await emailService.send(emailRequest, `queue:${queueMessage.id}`, {
        skipRateLimit: true,
        skipIdempotency: true,
      });

      message.ack();
    } catch (error) {
      console.error('Queue processing error:', error);

      // Retry logic
      const retryCount = (message.body.retryCount ?? 0) + 1;
      const maxRetries = message.body.maxRetries ?? 3;

      if (retryCount < maxRetries) {
        message.retry({
          delaySeconds: Math.pow(2, retryCount) * 60, // Exponential backoff
        });
      } else {
        // Max retries exceeded, acknowledge and log failure
        console.error(`Max retries exceeded for message ${message.body.id}`);
        message.ack();
      }
    }
  }
}

/**
 * Scheduled handler for cron jobs
 */
async function handleScheduled(
  event: ScheduledEvent,
  env: Env,
  ctx: ExecutionContext
): Promise<void> {
  // Process scheduled emails
  const cursor = await env.EMAIL_KV.list({ prefix: 'scheduled:' });

  for (const key of cursor.keys) {
    const data = await env.EMAIL_KV.get(key.name, 'json');

    if (data !== null) {
      const { email, scheduledAt } = data as {
        email: import('./types').EmailRequest;
        scheduledAt: string;
      };

      if (new Date(scheduledAt) <= new Date()) {
        // Queue the email for sending
        await env.EMAIL_QUEUE.send({
          id: key.name.replace('scheduled:', ''),
          ...email,
        } as EmailQueueMessage);

        // Remove from scheduled
        await env.EMAIL_KV.delete(key.name);
      }
    }
  }
}

// Export handlers
export default {
  fetch: app.fetch,
  queue: handleQueue,
  scheduled: handleScheduled,
};

// Export app for testing
export { app, createApp };
