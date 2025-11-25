// ═══════════════════════════════════════════════════════════════════════════════
// WEBHOOK & NOTIFICATION SYSTEM
// Send notifications to Discord, Slack, Email, and custom endpoints
// ═══════════════════════════════════════════════════════════════════════════════

export class WebhookManager {
  constructor(config = {}) {
    this.webhooks = new Map();
    this.templates = this.initTemplates();
    this.queue = [];
    this.history = [];
    this.config = {
      retryAttempts: 3,
      retryDelay: 1000,
      batchSize: 10,
      ...config
    };
  }

  // ─── WEBHOOK REGISTRATION ──────────────────────────────────────────────────

  register(id, config) {
    const webhook = {
      id,
      type: config.type || "custom", // discord, slack, email, custom
      url: config.url,
      secret: config.secret || null,
      events: config.events || ["*"],
      enabled: config.enabled !== false,
      headers: config.headers || {},
      createdAt: new Date().toISOString()
    };

    this.webhooks.set(id, webhook);
    return webhook;
  }

  unregister(id) {
    this.webhooks.delete(id);
  }

  list() {
    return Array.from(this.webhooks.values());
  }

  // ─── SEND NOTIFICATIONS ────────────────────────────────────────────────────

  async send(event, data, options = {}) {
    const { webhookIds = null, priority = "normal" } = options;

    // Get matching webhooks
    let targets = Array.from(this.webhooks.values())
      .filter(w => w.enabled)
      .filter(w => w.events.includes("*") || w.events.includes(event));

    if (webhookIds) {
      targets = targets.filter(w => webhookIds.includes(w.id));
    }

    if (targets.length === 0) {
      return { sent: 0, message: "No matching webhooks" };
    }

    // Send to all targets
    const results = await Promise.allSettled(
      targets.map(webhook => this.sendToWebhook(webhook, event, data))
    );

    const successful = results.filter(r => r.status === "fulfilled").length;
    const failed = results.filter(r => r.status === "rejected");

    // Log results
    this.history.push({
      event,
      timestamp: new Date().toISOString(),
      targets: targets.length,
      successful,
      failed: failed.length
    });

    return {
      sent: successful,
      failed: failed.length,
      results: results.map((r, i) => ({
        webhook: targets[i].id,
        success: r.status === "fulfilled",
        error: r.reason?.message
      }))
    };
  }

  async sendToWebhook(webhook, event, data) {
    const payload = this.formatPayload(webhook.type, event, data);

    for (let attempt = 0; attempt < this.config.retryAttempts; attempt++) {
      try {
        const response = await fetch(webhook.url, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            ...webhook.headers,
            ...(webhook.secret ? { "X-Webhook-Secret": webhook.secret } : {})
          },
          body: JSON.stringify(payload)
        });

        if (!response.ok) {
          throw new Error(`HTTP ${response.status}`);
        }

        return { success: true };

      } catch (error) {
        if (attempt < this.config.retryAttempts - 1) {
          await this.delay(this.config.retryDelay * (attempt + 1));
        } else {
          throw error;
        }
      }
    }
  }

  // ─── PAYLOAD FORMATTING ────────────────────────────────────────────────────

  formatPayload(type, event, data) {
    switch (type) {
      case "discord":
        return this.formatDiscord(event, data);
      case "slack":
        return this.formatSlack(event, data);
      case "email":
        return this.formatEmail(event, data);
      default:
        return this.formatCustom(event, data);
    }
  }

  formatDiscord(event, data) {
    const colors = {
      success: 0x2ECC71,
      error: 0xE74C3C,
      warning: 0xF39C12,
      info: 0x3498DB,
      default: 0x9B59B6
    };

    const color = colors[data.severity] || colors[data.type] || colors.default;

    return {
      content: data.mention || null,
      embeds: [{
        title: `${this.getEmoji(event)} ${event.replace(/_/g, " ").toUpperCase()}`,
        description: data.message || data.summary,
        color,
        fields: this.buildFields(data),
        footer: {
          text: `CODEMASTER • ${new Date().toISOString()}`
        },
        timestamp: new Date().toISOString()
      }]
    };
  }

  formatSlack(event, data) {
    const colors = {
      success: "good",
      error: "danger",
      warning: "warning",
      info: "#3498DB"
    };

    return {
      text: `${this.getEmoji(event)} *${event.replace(/_/g, " ").toUpperCase()}*`,
      attachments: [{
        color: colors[data.severity] || colors[data.type] || "#9B59B6",
        text: data.message || data.summary,
        fields: this.buildSlackFields(data),
        footer: "CODEMASTER",
        ts: Math.floor(Date.now() / 1000)
      }]
    };
  }

  formatEmail(event, data) {
    return {
      subject: `[CODEMASTER] ${event.replace(/_/g, " ")}`,
      body: data.message || data.summary,
      html: this.buildEmailHtml(event, data),
      priority: data.severity === "critical" ? "high" : "normal"
    };
  }

  formatCustom(event, data) {
    return {
      event,
      timestamp: new Date().toISOString(),
      source: "codemaster",
      data
    };
  }

  buildFields(data) {
    const fields = [];

    if (data.agent) {
      fields.push({ name: "Agent", value: data.agent, inline: true });
    }
    if (data.status) {
      fields.push({ name: "Status", value: data.status, inline: true });
    }
    if (data.duration) {
      fields.push({ name: "Duration", value: `${data.duration}ms`, inline: true });
    }
    if (data.details) {
      fields.push({ name: "Details", value: data.details.substring(0, 1024), inline: false });
    }

    return fields;
  }

  buildSlackFields(data) {
    const fields = [];

    if (data.agent) {
      fields.push({ title: "Agent", value: data.agent, short: true });
    }
    if (data.status) {
      fields.push({ title: "Status", value: data.status, short: true });
    }

    return fields;
  }

  buildEmailHtml(event, data) {
    return `
<!DOCTYPE html>
<html>
<head>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    .container { max-width: 600px; margin: 0 auto; padding: 20px; }
    .header { background: linear-gradient(135deg, #9B59B6, #3498DB); color: white; padding: 20px; border-radius: 8px 8px 0 0; }
    .content { background: #f5f5f5; padding: 20px; border-radius: 0 0 8px 8px; }
    .footer { text-align: center; color: #666; margin-top: 20px; font-size: 12px; }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h2>${this.getEmoji(event)} ${event.replace(/_/g, " ").toUpperCase()}</h2>
    </div>
    <div class="content">
      <p>${data.message || data.summary}</p>
      ${data.details ? `<p><strong>Details:</strong> ${data.details}</p>` : ""}
    </div>
    <div class="footer">
      CODEMASTER • ${new Date().toISOString()}
    </div>
  </div>
</body>
</html>`;
  }

  getEmoji(event) {
    const emojis = {
      task_complete: "✅",
      task_failed: "❌",
      agent_called: "🤖",
      code_generated: "🔨",
      review_complete: "📝",
      deploy_success: "🚀",
      deploy_failed: "💥",
      security_alert: "🛡️",
      error: "⚠️",
      info: "ℹ️"
    };
    return emojis[event] || "📢";
  }

  // ─── TEMPLATES ─────────────────────────────────────────────────────────────

  initTemplates() {
    return {
      task_complete: {
        title: "Task Completed",
        fields: ["agent", "task", "duration"]
      },
      code_generated: {
        title: "Code Generated",
        fields: ["type", "files", "lines"]
      },
      deploy_success: {
        title: "Deployment Successful",
        fields: ["environment", "version", "url"]
      },
      error: {
        title: "Error Occurred",
        fields: ["type", "message", "stack"]
      }
    };
  }

  // ─── EVENT HELPERS ─────────────────────────────────────────────────────────

  async notifyTaskComplete(task) {
    return this.send("task_complete", {
      agent: task.agent,
      message: `Task "${task.name}" completed successfully`,
      duration: task.duration,
      type: "success"
    });
  }

  async notifyError(error) {
    return this.send("error", {
      message: error.message,
      stack: error.stack,
      severity: "error",
      type: "error"
    });
  }

  async notifyDeployment(deployment) {
    const event = deployment.success ? "deploy_success" : "deploy_failed";
    return this.send(event, {
      environment: deployment.environment,
      version: deployment.version,
      url: deployment.url,
      message: deployment.success
        ? `Deployed v${deployment.version} to ${deployment.environment}`
        : `Deployment to ${deployment.environment} failed`,
      severity: deployment.success ? "success" : "error"
    });
  }

  async notifySecurityAlert(alert) {
    return this.send("security_alert", {
      message: alert.message,
      severity: alert.severity || "critical",
      details: alert.details,
      mention: "@here" // Discord mention for urgent alerts
    });
  }

  // ─── UTILITIES ─────────────────────────────────────────────────────────────

  delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

  getHistory(limit = 50) {
    return this.history.slice(-limit);
  }

  getStats() {
    const total = this.history.length;
    const successful = this.history.reduce((sum, h) => sum + h.successful, 0);
    const failed = this.history.reduce((sum, h) => sum + h.failed, 0);

    return {
      totalNotifications: total,
      successRate: total > 0 ? ((successful / (successful + failed)) * 100).toFixed(1) + "%" : "N/A",
      webhooksRegistered: this.webhooks.size,
      webhooksEnabled: Array.from(this.webhooks.values()).filter(w => w.enabled).length
    };
  }
}

export default WebhookManager;
