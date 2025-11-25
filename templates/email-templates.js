// ═══════════════════════════════════════════════════════════════════════════════
// NOIZYLAB EMAIL TEMPLATES v2.0
// Professional Email Response Templates
// ═══════════════════════════════════════════════════════════════════════════════

export const TEMPLATES = {
  // ─── AUTO-REPLY TEMPLATES ──────────────────────────────────────────────────

  urgent: {
    subject: "RE: {original_subject}",
    body: `Thank you for your urgent message.

This has been flagged as HIGH PRIORITY and our team has been immediately notified.

📋 Summary: {summary}
🎯 Assigned to: {agent}
⏱️  Expected response: Within 2 hours

If this is a critical emergency, please also reach out directly at:
📞 Emergency Line: +1 (xxx) xxx-xxxx

We're on it!

– NoizyLab Emergency Response Team
🚨 RED_ALERT Protocol Activated`
  },

  acknowledgment: {
    subject: "RE: {original_subject}",
    body: `Thank you for contacting NoizyLab!

We've received your message and it's being processed by our AI-powered system.

📋 Summary: {summary}
🤖 Assigned Agent: {agent}
📊 Priority: {priority}
⏱️  Expected response: {response_time}

Track your request at: https://status.noizylab.ca/track/{ticket_id}

Best regards,
– NoizyLab Team`
  },

  technical: {
    subject: "RE: {original_subject} - Technical Support",
    body: `Thank you for your technical inquiry.

Our Technical Lead (KEITH) has received your request and is analyzing it.

🔧 Issue Summary: {summary}
📊 Urgency Level: {urgency}/10
🏷️  Category: Technical Support

What happens next:
1. Our team will review your technical details
2. We may reach out for additional information if needed
3. You'll receive a detailed response with solutions

For urgent technical issues, include [URGENT] in your subject line.

– NoizyLab Technical Support
⚙️ Powered by KEITH`
  },

  creative: {
    subject: "RE: {original_subject} - Creative Request",
    body: `Thank you for your creative request!

Our Creative Director (LUCY) is excited to review your project.

🎨 Request Summary: {summary}
✨ Estimated timeline: We'll provide a quote within 24-48 hours

Please feel free to share any additional materials:
- Brand guidelines
- Reference images
- Mood boards
- Specific requirements

We love bringing creative visions to life!

– NoizyLab Creative Team
🎨 Powered by LUCY`
  },

  project: {
    subject: "RE: {original_subject} - Project Inquiry",
    body: `Thank you for reaching out about your project!

Our Project Manager (WARDY) has received your inquiry.

📋 Summary: {summary}
📅 Next steps: We'll schedule a discovery call within 48 hours

To help us prepare, please share:
- Project timeline expectations
- Budget range (if available)
- Key stakeholders

We're looking forward to collaborating with you!

– NoizyLab Project Management
📋 Powered by WARDY`
  },

  // ─── NOTIFICATION TEMPLATES ────────────────────────────────────────────────

  webhook_discord: {
    content: "📧 **New Email Received**",
    embeds: [{
      title: "{subject}",
      description: "{body_preview}",
      color: "{priority_color}",
      fields: [
        { name: "From", value: "{from}", inline: true },
        { name: "Agent", value: "{agent}", inline: true },
        { name: "Urgency", value: "{urgency}/10", inline: true },
        { name: "Intent", value: "{intent}", inline: true },
        { name: "Priority", value: "{priority}", inline: true },
        { name: "Spam Score", value: "{spam_score}", inline: true }
      ],
      footer: { text: "ID: {email_id} | {processing_time}ms" },
      timestamp: "{timestamp}"
    }]
  },

  webhook_slack: {
    text: "📧 New Email: {subject}",
    blocks: [
      {
        type: "header",
        text: { type: "plain_text", text: "📧 New Email Received" }
      },
      {
        type: "section",
        fields: [
          { type: "mrkdwn", text: "*From:*\\n{from}" },
          { type: "mrkdwn", text: "*Agent:*\\n{agent}" },
          { type: "mrkdwn", text: "*Subject:*\\n{subject}" },
          { type: "mrkdwn", text: "*Priority:*\\n{priority}" }
        ]
      },
      {
        type: "section",
        text: { type: "mrkdwn", text: "*Summary:*\\n{summary}" }
      }
    ]
  },

  // ─── DIGEST TEMPLATES ──────────────────────────────────────────────────────

  daily_digest: {
    subject: "📊 NoizyLab Daily Digest - {date}",
    body: `Good morning! Here's your daily email digest.

═══════════════════════════════════════════════════
📧 EMAIL STATISTICS
═══════════════════════════════════════════════════

📬 Received: {total_emails}
🚫 Spam Blocked: {spam_blocked}
⚡ Urgent: {urgent_count}
✅ Processed: {processed_count}

═══════════════════════════════════════════════════
🤖 AGENT ACTIVITY
═══════════════════════════════════════════════════

🎨 LUCY (Creative): {lucy_count} emails
⚙️ KEITH (Technical): {keith_count} emails
📋 WARDY (Projects): {wardy_count} emails
🚨 RED_ALERT (Urgent): {red_alert_count} emails
🔬 NOVA (Research): {nova_count} emails
📢 ECHO (Communications): {echo_count} emails

═══════════════════════════════════════════════════
📌 TOP PRIORITIES
═══════════════════════════════════════════════════

{priority_list}

─────────────────────────────────────────────────
View full dashboard: https://api.noizylab.ca/dashboard

– NoizyLab AI System`
  },

  // ─── ERROR TEMPLATES ───────────────────────────────────────────────────────

  error_notification: {
    subject: "⚠️ NoizyLab System Alert",
    body: `A system error has occurred.

🚨 Error Type: {error_type}
📝 Message: {error_message}
⏰ Time: {timestamp}
📧 Related Email: {email_id}

Our team has been automatically notified.

– NoizyLab System Monitor`
  },

  rate_limit_warning: {
    subject: "⚠️ Rate Limit Warning",
    body: `High email volume detected from your domain.

📧 Domain: {domain}
📊 Emails received: {count}/{limit} per hour
⏰ Reset time: {reset_time}

If this is expected behavior, no action is needed.
If not, please check for potential email loops or misconfigurations.

– NoizyLab Security`
  }
};

// ─── TEMPLATE RENDERER ───────────────────────────────────────────────────────

export function renderTemplate(templateName, data) {
  const template = TEMPLATES[templateName];
  if (!template) {
    throw new Error(`Template not found: ${templateName}`);
  }

  let rendered = JSON.stringify(template);

  // Replace all placeholders
  for (const [key, value] of Object.entries(data)) {
    const placeholder = new RegExp(`\\{${key}\\}`, "g");
    rendered = rendered.replace(placeholder, String(value || ""));
  }

  return JSON.parse(rendered);
}

// ─── PRIORITY COLOR MAPPING ──────────────────────────────────────────────────

export const PRIORITY_COLORS = {
  low: 0x2ECC71,      // Green
  medium: 0xF39C12,   // Orange
  high: 0xE74C3C,     // Red
  critical: 0x9B59B6  // Purple
};

export function getPriorityColor(priority) {
  return PRIORITY_COLORS[priority] || PRIORITY_COLORS.medium;
}

// ─── AGENT RESPONSE STYLES ───────────────────────────────────────────────────

export const AGENT_SIGNATURES = {
  LUCY: "🎨 Creative vibes,\n– LUCY",
  KEITH: "⚙️ Code on,\n– KEITH",
  WARDY: "📋 Stay organized,\n– WARDY",
  RED_ALERT: "🚨 Stay vigilant,\n– RED_ALERT",
  NOVA: "🔬 Data drives decisions,\n– NOVA",
  ECHO: "📢 Communication is key,\n– ECHO"
};

export default {
  TEMPLATES,
  renderTemplate,
  PRIORITY_COLORS,
  getPriorityColor,
  AGENT_SIGNATURES
};
