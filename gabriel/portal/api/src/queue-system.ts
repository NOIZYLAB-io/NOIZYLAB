/**
 * Queue System for Background Jobs
 * 
 * Uses Cloudflare Queues for reliable background job processing
 * Handles: scan processing, email sending, webhook delivery, analytics aggregation
 */

// ============================================================================
// JOB TYPES
// ============================================================================

type JobType = 
  | 'process_scan'
  | 'send_email'
  | 'deliver_webhook'
  | 'aggregate_metrics'
  | 'cleanup_expired'
  | 'generate_report';

interface BaseJob {
  id: string;
  type: JobType;
  createdAt: string;
  attempts: number;
  maxAttempts: number;
  priority: 'high' | 'normal' | 'low';
}

interface ProcessScanJob extends BaseJob {
  type: 'process_scan';
  payload: {
    scanId: string;
    userId: string;
    imageUrl: string;
    boardType?: string;
  };
}

interface SendEmailJob extends BaseJob {
  type: 'send_email';
  payload: {
    template: string;
    to: string;
    data: Record<string, unknown>;
  };
}

interface DeliverWebhookJob extends BaseJob {
  type: 'deliver_webhook';
  payload: {
    url: string;
    event: string;
    data: Record<string, unknown>;
    secret?: string;
  };
}

interface AggregateMetricsJob extends BaseJob {
  type: 'aggregate_metrics';
  payload: {
    date: string;
    metrics: string[];
  };
}

interface CleanupExpiredJob extends BaseJob {
  type: 'cleanup_expired';
  payload: {
    prefix: string;
    maxAge: number;
  };
}

interface GenerateReportJob extends BaseJob {
  type: 'generate_report';
  payload: {
    userId: string;
    reportType: 'weekly' | 'monthly';
    dateRange: { start: string; end: string };
  };
}

type Job = 
  | ProcessScanJob 
  | SendEmailJob 
  | DeliverWebhookJob 
  | AggregateMetricsJob 
  | CleanupExpiredJob
  | GenerateReportJob;

// ============================================================================
// QUEUE PRODUCER
// ============================================================================

export class QueueProducer {
  private queue: Queue;

  constructor(queue: Queue) {
    this.queue = queue;
  }

  private generateId(): string {
    return `job_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
  }

  private createJob<T extends Job>(
    type: JobType,
    payload: T['payload'],
    options: { priority?: Job['priority']; maxAttempts?: number } = {}
  ): Omit<T, 'payload'> & { payload: T['payload'] } {
    return {
      id: this.generateId(),
      type,
      createdAt: new Date().toISOString(),
      attempts: 0,
      maxAttempts: options.maxAttempts || 3,
      priority: options.priority || 'normal',
      payload,
    } as unknown as Omit<T, 'payload'> & { payload: T['payload'] };
  }

  /**
   * Queue a scan for processing
   */
  async queueScan(payload: ProcessScanJob['payload']): Promise<string> {
    const job = this.createJob<ProcessScanJob>('process_scan', payload, {
      priority: 'high',
      maxAttempts: 3,
    });
    
    await this.queue.send(job);
    console.log(`Queued scan job: ${job.id}`);
    
    return job.id;
  }

  /**
   * Queue an email to send
   */
  async queueEmail(payload: SendEmailJob['payload']): Promise<string> {
    const job = this.createJob<SendEmailJob>('send_email', payload, {
      priority: 'normal',
      maxAttempts: 5,
    });
    
    await this.queue.send(job);
    
    return job.id;
  }

  /**
   * Queue a webhook delivery
   */
  async queueWebhook(payload: DeliverWebhookJob['payload']): Promise<string> {
    const job = this.createJob<DeliverWebhookJob>('deliver_webhook', payload, {
      priority: 'high',
      maxAttempts: 5,
    });
    
    await this.queue.send(job);
    
    return job.id;
  }

  /**
   * Queue metrics aggregation
   */
  async queueAggregation(payload: AggregateMetricsJob['payload']): Promise<string> {
    const job = this.createJob<AggregateMetricsJob>('aggregate_metrics', payload, {
      priority: 'low',
      maxAttempts: 3,
    });
    
    await this.queue.send(job);
    
    return job.id;
  }

  /**
   * Queue cleanup job
   */
  async queueCleanup(payload: CleanupExpiredJob['payload']): Promise<string> {
    const job = this.createJob<CleanupExpiredJob>('cleanup_expired', payload, {
      priority: 'low',
      maxAttempts: 1,
    });
    
    await this.queue.send(job);
    
    return job.id;
  }

  /**
   * Queue report generation
   */
  async queueReport(payload: GenerateReportJob['payload']): Promise<string> {
    const job = this.createJob<GenerateReportJob>('generate_report', payload, {
      priority: 'normal',
      maxAttempts: 3,
    });
    
    await this.queue.send(job);
    
    return job.id;
  }

  /**
   * Batch send multiple jobs
   */
  async sendBatch(jobs: Job[]): Promise<void> {
    const messages = jobs.map(job => ({ body: job }));
    await this.queue.sendBatch(messages);
    console.log(`Queued ${jobs.length} jobs in batch`);
  }
}

// ============================================================================
// QUEUE CONSUMER (Worker Handler)
// ============================================================================

interface ProcessorContext {
  kv: KVNamespace;
  r2: R2Bucket;
  ai: Ai;
  env: Record<string, string>;
}

type JobProcessor<T extends Job> = (job: T, ctx: ProcessorContext) => Promise<void>;

const processors: Record<JobType, JobProcessor<Job>> = {
  process_scan: async (job, ctx) => {
    const scanJob = job as ProcessScanJob;
    console.log(`Processing scan: ${scanJob.payload.scanId}`);
    
    // 1. Download image from R2
    const image = await ctx.r2.get(`scans/${scanJob.payload.scanId}/input.jpg`);
    if (!image) throw new Error('Image not found');
    
    // 2. Run AI analysis
    const analysis = await ctx.ai.run('@cf/meta/llama-3.2-11b-vision-instruct', {
      image: await image.arrayBuffer(),
      prompt: 'Analyze this circuit board for defects, damaged components, and potential issues.',
    });
    
    // 3. Store results
    await ctx.kv.put(
      `scan:${scanJob.payload.scanId}:result`,
      JSON.stringify({
        status: 'complete',
        analysis,
        completedAt: new Date().toISOString(),
      })
    );
    
    // 4. Update user metrics
    const userKey = `user:${scanJob.payload.userId}:stats`;
    const stats = await ctx.kv.get<{ scans: number }>(userKey, 'json') || { scans: 0 };
    stats.scans++;
    await ctx.kv.put(userKey, JSON.stringify(stats));
    
    console.log(`Scan ${scanJob.payload.scanId} completed`);
  },

  send_email: async (job, ctx) => {
    const emailJob = job as SendEmailJob;
    console.log(`Sending email to: ${emailJob.payload.to}`);
    
    const response = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${ctx.env.RESEND_API_KEY}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        from: 'GABRIEL <hello@noizylab.com>',
        to: [emailJob.payload.to],
        subject: emailJob.payload.data.subject,
        html: emailJob.payload.data.html,
      }),
    });
    
    if (!response.ok) {
      throw new Error(`Email failed: ${await response.text()}`);
    }
    
    console.log(`Email sent to ${emailJob.payload.to}`);
  },

  deliver_webhook: async (job, ctx) => {
    const webhookJob = job as DeliverWebhookJob;
    console.log(`Delivering webhook to: ${webhookJob.payload.url}`);
    
    const timestamp = Date.now().toString();
    const payload = JSON.stringify({
      event: webhookJob.payload.event,
      data: webhookJob.payload.data,
      timestamp,
    });
    
    // Generate signature if secret provided
    const headers: Record<string, string> = {
      'Content-Type': 'application/json',
      'X-Webhook-Timestamp': timestamp,
    };
    
    if (webhookJob.payload.secret) {
      const encoder = new TextEncoder();
      const key = await crypto.subtle.importKey(
        'raw',
        encoder.encode(webhookJob.payload.secret),
        { name: 'HMAC', hash: 'SHA-256' },
        false,
        ['sign']
      );
      const signature = await crypto.subtle.sign('HMAC', key, encoder.encode(payload));
      headers['X-Webhook-Signature'] = btoa(String.fromCharCode(...new Uint8Array(signature)));
    }
    
    const response = await fetch(webhookJob.payload.url, {
      method: 'POST',
      headers,
      body: payload,
    });
    
    if (!response.ok) {
      throw new Error(`Webhook failed: ${response.status} ${response.statusText}`);
    }
    
    console.log(`Webhook delivered to ${webhookJob.payload.url}`);
  },

  aggregate_metrics: async (job, ctx) => {
    const metricsJob = job as AggregateMetricsJob;
    console.log(`Aggregating metrics for: ${metricsJob.payload.date}`);
    
    // Aggregate daily metrics from hourly data
    const hourlyKeys = [];
    for (let h = 0; h < 24; h++) {
      hourlyKeys.push(`metrics:hourly:${metricsJob.payload.date}:${h.toString().padStart(2, '0')}`);
    }
    
    let totalScans = 0;
    let totalRevenue = 0;
    let totalUsers = new Set<string>();
    
    for (const key of hourlyKeys) {
      const data = await ctx.kv.get<{
        scans: number;
        revenue: number;
        users: string[];
      }>(key, 'json');
      
      if (data) {
        totalScans += data.scans;
        totalRevenue += data.revenue;
        data.users.forEach(u => totalUsers.add(u));
      }
    }
    
    // Store daily aggregate
    await ctx.kv.put(
      `metrics:daily:${metricsJob.payload.date}`,
      JSON.stringify({
        date: metricsJob.payload.date,
        scans: totalScans,
        revenue: totalRevenue,
        uniqueUsers: totalUsers.size,
        aggregatedAt: new Date().toISOString(),
      })
    );
    
    console.log(`Metrics aggregated for ${metricsJob.payload.date}`);
  },

  cleanup_expired: async (job, ctx) => {
    const cleanupJob = job as CleanupExpiredJob;
    console.log(`Cleaning up expired items with prefix: ${cleanupJob.payload.prefix}`);
    
    const now = Date.now();
    const maxAge = cleanupJob.payload.maxAge;
    let deleted = 0;
    
    // List and delete expired keys
    const list = await ctx.kv.list({ prefix: cleanupJob.payload.prefix });
    
    for (const key of list.keys) {
      if (key.metadata && typeof key.metadata === 'object' && 'createdAt' in key.metadata) {
        const createdAt = new Date(key.metadata.createdAt as string).getTime();
        if (now - createdAt > maxAge) {
          await ctx.kv.delete(key.name);
          deleted++;
        }
      }
    }
    
    console.log(`Cleanup complete: ${deleted} items deleted`);
  },

  generate_report: async (job, ctx) => {
    const reportJob = job as GenerateReportJob;
    console.log(`Generating ${reportJob.payload.reportType} report for user: ${reportJob.payload.userId}`);
    
    // Gather data for report
    const scans = await ctx.kv.list({
      prefix: `user:${reportJob.payload.userId}:scan:`,
    });
    
    // Generate report content
    const report = {
      userId: reportJob.payload.userId,
      type: reportJob.payload.reportType,
      dateRange: reportJob.payload.dateRange,
      generatedAt: new Date().toISOString(),
      summary: {
        totalScans: scans.keys.length,
        // Add more metrics...
      },
    };
    
    // Store report
    await ctx.r2.put(
      `reports/${reportJob.payload.userId}/${reportJob.payload.reportType}-${Date.now()}.json`,
      JSON.stringify(report)
    );
    
    console.log(`Report generated for user ${reportJob.payload.userId}`);
  },
};

/**
 * Queue consumer handler for Cloudflare Workers
 */
export async function handleQueue(
  batch: MessageBatch<Job>,
  ctx: ProcessorContext
): Promise<void> {
  for (const message of batch.messages) {
    const job = message.body;
    
    try {
      console.log(`Processing job ${job.id} (type: ${job.type}, attempt: ${job.attempts + 1}/${job.maxAttempts})`);
      
      const processor = processors[job.type];
      if (!processor) {
        console.error(`Unknown job type: ${job.type}`);
        message.ack();
        continue;
      }
      
      await processor(job, ctx);
      message.ack();
      
      console.log(`Job ${job.id} completed successfully`);
    } catch (error) {
      console.error(`Job ${job.id} failed:`, error);
      
      // Retry if under max attempts
      if (job.attempts + 1 < job.maxAttempts) {
        message.retry({
          delaySeconds: Math.pow(2, job.attempts) * 10, // Exponential backoff
        });
      } else {
        console.error(`Job ${job.id} exceeded max attempts, moving to DLQ`);
        message.ack(); // Or move to dead letter queue
      }
    }
  }
}

// ============================================================================
// SCHEDULED JOBS
// ============================================================================

/**
 * Handle scheduled cron triggers
 */
export async function handleScheduled(
  event: ScheduledEvent,
  producer: QueueProducer
): Promise<void> {
  const cron = event.cron;
  
  switch (cron) {
    // Daily at midnight: aggregate metrics
    case '0 0 * * *':
      const yesterday = new Date();
      yesterday.setDate(yesterday.getDate() - 1);
      await producer.queueAggregation({
        date: yesterday.toISOString().split('T')[0],
        metrics: ['scans', 'revenue', 'users'],
      });
      break;
    
    // Every 6 hours: cleanup expired data
    case '0 */6 * * *':
      await producer.queueCleanup({
        prefix: 'temp:',
        maxAge: 24 * 60 * 60 * 1000, // 24 hours
      });
      break;
    
    // Weekly on Monday: generate reports
    case '0 9 * * 1':
      // Queue weekly reports for active users
      // (In production, iterate through users)
      break;
  }
}

// ============================================================================
// EXPORTS
// ============================================================================

export default {
  QueueProducer,
  handleQueue,
  handleScheduled,
};
