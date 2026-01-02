/**
 * Error Tracking Service
 * 
 * Lightweight error tracking for NoizyLab GABRIEL
 * Sends errors to a webhook for aggregation (Slack, Discord, or custom)
 */

interface ErrorContext {
  userId?: string;
  scanId?: string;
  boardType?: string;
  route?: string;
  method?: string;
  userAgent?: string;
  ip?: string;
  extra?: Record<string, unknown>;
}

interface ErrorReport {
  id: string;
  timestamp: string;
  level: 'error' | 'warning' | 'info';
  message: string;
  stack?: string;
  context: ErrorContext;
  environment: string;
  version: string;
}

// ============================================================================
// ERROR TRACKER
// ============================================================================

export class ErrorTracker {
  private webhookUrl: string;
  private environment: string;
  private version: string;
  private buffer: ErrorReport[] = [];
  private flushInterval: number = 5000; // 5 seconds

  constructor(config: {
    webhookUrl: string;
    environment: string;
    version: string;
  }) {
    this.webhookUrl = config.webhookUrl;
    this.environment = config.environment;
    this.version = config.version;
  }

  /**
   * Generate unique error ID
   */
  private generateId(): string {
    return `err_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
  }

  /**
   * Capture an error
   */
  async captureError(
    error: Error | string,
    context: ErrorContext = {}
  ): Promise<string> {
    const report: ErrorReport = {
      id: this.generateId(),
      timestamp: new Date().toISOString(),
      level: 'error',
      message: error instanceof Error ? error.message : error,
      stack: error instanceof Error ? error.stack : undefined,
      context,
      environment: this.environment,
      version: this.version,
    };

    // Send immediately for errors
    await this.send(report);
    
    return report.id;
  }

  /**
   * Capture a warning
   */
  async captureWarning(
    message: string,
    context: ErrorContext = {}
  ): Promise<string> {
    const report: ErrorReport = {
      id: this.generateId(),
      timestamp: new Date().toISOString(),
      level: 'warning',
      message,
      context,
      environment: this.environment,
      version: this.version,
    };

    this.buffer.push(report);
    
    // Flush if buffer is getting large
    if (this.buffer.length >= 10) {
      await this.flush();
    }
    
    return report.id;
  }

  /**
   * Capture info/metric
   */
  captureInfo(message: string, context: ErrorContext = {}): void {
    const report: ErrorReport = {
      id: this.generateId(),
      timestamp: new Date().toISOString(),
      level: 'info',
      message,
      context,
      environment: this.environment,
      version: this.version,
    };

    this.buffer.push(report);
  }

  /**
   * Send error to webhook
   */
  private async send(report: ErrorReport): Promise<void> {
    try {
      // Format for Slack/Discord
      const payload = this.formatSlackPayload(report);
      
      await fetch(this.webhookUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });
    } catch (e) {
      // Don't let error tracking errors crash the app
      console.error('Failed to send error report:', e);
    }
  }

  /**
   * Flush buffered warnings/info
   */
  async flush(): Promise<void> {
    if (this.buffer.length === 0) return;
    
    const reports = this.buffer.splice(0, this.buffer.length);
    
    // Group by level
    const errors = reports.filter(r => r.level === 'error');
    const warnings = reports.filter(r => r.level === 'warning');
    const info = reports.filter(r => r.level === 'info');
    
    // Send summary
    const summary = {
      text: `📊 GABRIEL Error Summary (${this.environment})`,
      blocks: [
        {
          type: 'section',
          text: {
            type: 'mrkdwn',
            text: `*Error Summary* - ${new Date().toISOString()}\n\n` +
              `🔴 Errors: ${errors.length}\n` +
              `🟡 Warnings: ${warnings.length}\n` +
              `ℹ️ Info: ${info.length}`,
          },
        },
        ...errors.slice(0, 5).map(e => ({
          type: 'section',
          text: {
            type: 'mrkdwn',
            text: `\`${e.id}\` ${e.message.substring(0, 100)}`,
          },
        })),
      ],
    };
    
    try {
      await fetch(this.webhookUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(summary),
      });
    } catch (e) {
      console.error('Failed to flush error buffer:', e);
    }
  }

  /**
   * Format error for Slack webhook
   */
  private formatSlackPayload(report: ErrorReport) {
    const emoji = report.level === 'error' ? '🔴' : report.level === 'warning' ? '🟡' : 'ℹ️';
    const color = report.level === 'error' ? '#ef4444' : report.level === 'warning' ? '#f59e0b' : '#3b82f6';
    
    return {
      attachments: [
        {
          color,
          blocks: [
            {
              type: 'section',
              text: {
                type: 'mrkdwn',
                text: `${emoji} *${report.level.toUpperCase()}* in \`${this.environment}\`\n\n*${report.message}*`,
              },
            },
            {
              type: 'section',
              fields: [
                {
                  type: 'mrkdwn',
                  text: `*ID:*\n\`${report.id}\``,
                },
                {
                  type: 'mrkdwn',
                  text: `*Time:*\n${report.timestamp}`,
                },
                report.context.userId ? {
                  type: 'mrkdwn',
                  text: `*User:*\n${report.context.userId}`,
                } : null,
                report.context.route ? {
                  type: 'mrkdwn',
                  text: `*Route:*\n${report.context.method} ${report.context.route}`,
                } : null,
              ].filter(Boolean),
            },
            report.stack ? {
              type: 'section',
              text: {
                type: 'mrkdwn',
                text: `*Stack:*\n\`\`\`${report.stack.substring(0, 500)}\`\`\``,
              },
            } : null,
          ].filter(Boolean),
        },
      ],
    };
  }
}

// ============================================================================
// REQUEST ERROR HANDLER
// ============================================================================

/**
 * Wrap request handler with error tracking
 */
export function withErrorTracking(
  tracker: ErrorTracker,
  handler: (request: Request) => Promise<Response>
) {
  return async (request: Request): Promise<Response> => {
    const url = new URL(request.url);
    const context: ErrorContext = {
      route: url.pathname,
      method: request.method,
      userAgent: request.headers.get('User-Agent') || undefined,
      ip: request.headers.get('CF-Connecting-IP') || undefined,
    };

    try {
      const response = await handler(request);
      
      // Track 5xx errors
      if (response.status >= 500) {
        await tracker.captureError(
          `HTTP ${response.status}: ${response.statusText}`,
          context
        );
      }
      
      // Track 4xx as warnings
      if (response.status >= 400 && response.status < 500) {
        tracker.captureInfo(`HTTP ${response.status}: ${url.pathname}`, context);
      }
      
      return response;
    } catch (error) {
      // Capture unhandled errors
      const errorId = await tracker.captureError(
        error instanceof Error ? error : new Error(String(error)),
        context
      );
      
      return new Response(
        JSON.stringify({
          error: 'Internal server error',
          errorId,
          message: error instanceof Error ? error.message : 'Unknown error',
        }),
        {
          status: 500,
          headers: { 'Content-Type': 'application/json' },
        }
      );
    }
  };
}

// ============================================================================
// HEALTH METRICS
// ============================================================================

interface HealthMetrics {
  requestsTotal: number;
  requestsSuccess: number;
  requestsFailed: number;
  avgResponseTime: number;
  uptime: number;
  lastError?: ErrorReport;
}

export class HealthMonitor {
  private metrics: HealthMetrics = {
    requestsTotal: 0,
    requestsSuccess: 0,
    requestsFailed: 0,
    avgResponseTime: 0,
    uptime: Date.now(),
  };
  
  private responseTimes: number[] = [];
  private maxSamples = 100;

  recordRequest(duration: number, success: boolean) {
    this.metrics.requestsTotal++;
    
    if (success) {
      this.metrics.requestsSuccess++;
    } else {
      this.metrics.requestsFailed++;
    }
    
    // Update average response time
    this.responseTimes.push(duration);
    if (this.responseTimes.length > this.maxSamples) {
      this.responseTimes.shift();
    }
    this.metrics.avgResponseTime = 
      this.responseTimes.reduce((a, b) => a + b, 0) / this.responseTimes.length;
  }

  recordError(error: ErrorReport) {
    this.metrics.lastError = error;
  }

  getMetrics(): HealthMetrics & { successRate: number } {
    return {
      ...this.metrics,
      uptime: Date.now() - this.metrics.uptime,
      successRate: this.metrics.requestsTotal > 0
        ? (this.metrics.requestsSuccess / this.metrics.requestsTotal) * 100
        : 100,
    };
  }

  /**
   * Health check endpoint handler
   */
  healthCheck(): Response {
    const metrics = this.getMetrics();
    const healthy = metrics.successRate > 95 && metrics.avgResponseTime < 5000;
    
    return new Response(
      JSON.stringify({
        status: healthy ? 'healthy' : 'degraded',
        ...metrics,
        version: '1.0.0',
        timestamp: new Date().toISOString(),
      }),
      {
        status: healthy ? 200 : 503,
        headers: { 'Content-Type': 'application/json' },
      }
    );
  }
}

// ============================================================================
// EXPORTS
// ============================================================================

export default {
  ErrorTracker,
  HealthMonitor,
  withErrorTracking,
};
