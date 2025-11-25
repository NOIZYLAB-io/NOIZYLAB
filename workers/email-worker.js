// ═══════════════════════════════════════════════════════════════════════════════
// NOIZYLAB EMAIL WORKER v2.0
// AI-Powered Email Processing with Multi-Agent Routing
// ═══════════════════════════════════════════════════════════════════════════════

// ─── AGENT DEFINITIONS ───────────────────────────────────────────────────────
const AGENTS = {
  LUCY: {
    name: "LUCY",
    role: "Creative Director",
    triggers: ["design", "brand", "logo", "creative", "visual", "art", "style", "aesthetic"],
    personality: "Creative, visionary, bold ideas",
    responseStyle: "enthusiastic and imaginative"
  },
  KEITH: {
    name: "KEITH",
    role: "Technical Lead",
    triggers: ["code", "bug", "error", "api", "server", "database", "technical", "deploy", "system"],
    personality: "Analytical, precise, solution-oriented",
    responseStyle: "methodical and detailed"
  },
  WARDY: {
    name: "WARDY",
    role: "Project Manager",
    triggers: ["deadline", "schedule", "meeting", "project", "task", "timeline", "plan", "status"],
    personality: "Organized, efficient, deadline-focused",
    responseStyle: "concise and action-oriented"
  },
  RED_ALERT: {
    name: "RED_ALERT",
    role: "Security & Urgency Handler",
    triggers: ["urgent", "emergency", "critical", "asap", "security", "breach", "hack", "down", "broken"],
    personality: "Vigilant, rapid response, no-nonsense",
    responseStyle: "direct and urgent"
  },
  NOVA: {
    name: "NOVA",
    role: "Research Analyst",
    triggers: ["research", "data", "analysis", "report", "study", "investigate", "insight", "metrics"],
    personality: "Curious, thorough, data-driven",
    responseStyle: "informative and evidence-based"
  },
  ECHO: {
    name: "ECHO",
    role: "Communications Lead",
    triggers: ["client", "customer", "feedback", "complaint", "review", "press", "media", "pr"],
    personality: "Diplomatic, clear, empathetic",
    responseStyle: "warm and professional"
  }
};

// ─── SPAM DETECTION PATTERNS ─────────────────────────────────────────────────
const SPAM_PATTERNS = [
  /\b(viagra|cialis|lottery|winner|prince|inheritance)\b/i,
  /\b(click here|act now|limited time|free money)\b/i,
  /\b(unsubscribe|opt-out).*(http|click)/i,
  /\b(bitcoin|crypto).*(investment|opportunity|profit)\b/i,
  /\$\d{1,3}(,\d{3})*\s*(million|billion|USD)/i,
  /(dear\s+(friend|customer|user|winner))/i,
  /\b(nigerian|foreign|overseas)\s+(prince|lottery|bank)\b/i,
];

const TRUSTED_DOMAINS = [
  "noizylab.ca",
  "gmail.com",
  "icloud.com",
  "apple.com",
  "github.com",
  "cloudflare.com"
];

// ─── MAIN EMAIL HANDLER ──────────────────────────────────────────────────────
export default {
  async email(message, env, ctx) {
    const startTime = Date.now();
    const emailId = `email-${startTime}-${Math.random().toString(36).substr(2, 9)}`;

    try {
      // Extract email data
      const from = message.from;
      const to = message.to;
      const subject = message.headers.get("subject") || "(No Subject)";
      const rawBody = await message.text();
      const body = rawBody.substring(0, 10000); // Limit body size

      // ─── RATE LIMITING ─────────────────────────────────────────────────────
      const rateLimitKey = `rate-${from.split("@")[1]}`;
      const currentCount = parseInt(await env.RATE_LIMITS?.get(rateLimitKey) || "0");
      const maxEmails = parseInt(env.MAX_EMAILS_PER_HOUR || "100");

      if (currentCount >= maxEmails) {
        await logEvent(env, emailId, "RATE_LIMITED", { from, subject });
        return; // Silently drop rate-limited emails
      }

      // Update rate limit counter (expires in 1 hour)
      await env.RATE_LIMITS?.put(rateLimitKey, String(currentCount + 1), { expirationTtl: 3600 });

      // ─── SPAM DETECTION ────────────────────────────────────────────────────
      const spamScore = calculateSpamScore(from, subject, body);
      const spamThreshold = parseInt(env.SPAM_THRESHOLD || "7");
      const isSpam = spamScore >= spamThreshold;

      if (isSpam) {
        await logEvent(env, emailId, "SPAM_DETECTED", { from, subject, spamScore });
        // Don't forward spam, but still log it
        return;
      }

      // ─── AI ANALYSIS ───────────────────────────────────────────────────────
      const analysis = await analyzeEmail(env, { from, to, subject, body });

      // ─── AGENT ROUTING ─────────────────────────────────────────────────────
      const assignedAgent = determineAgent(subject, body, analysis);
      const agentResponse = await callAgent(env, assignedAgent, { from, to, subject, body, analysis });

      // ─── LOGGING ───────────────────────────────────────────────────────────
      const logEntry = {
        id: emailId,
        timestamp: new Date().toISOString(),
        from,
        to,
        subject,
        bodyPreview: body.substring(0, 500),
        spamScore,
        analysis,
        agent: assignedAgent.name,
        agentResponse,
        processingTime: Date.now() - startTime
      };

      await env.MAIL_LOGS?.put(emailId, JSON.stringify(logEntry), { expirationTtl: 2592000 }); // 30 days

      // ─── WEBHOOK NOTIFICATION ──────────────────────────────────────────────
      if (env.WEBHOOK_ENABLED === "true" && env.WEBHOOK_URL) {
        ctx.waitUntil(sendWebhook(env, logEntry));
      }

      // ─── FORWARD EMAIL ─────────────────────────────────────────────────────
      const forwardTo = env.FORWARD_EMAIL || "rsplowman@icloud.com";
      await message.forward(forwardTo);

      // ─── AUTO-REPLY FOR URGENT/HIGH PRIORITY ───────────────────────────────
      if (analysis.urgency >= 8 || assignedAgent.name === "RED_ALERT") {
        const replyBody = generateAutoReply(assignedAgent, analysis);
        await message.reply({
          from: "noreply@noizylab.ca",
          subject: `RE: ${subject}`,
          text: replyBody
        });
      }

      // ─── UPDATE AGENT STATE ────────────────────────────────────────────────
      await updateAgentState(env, assignedAgent.name, emailId);

    } catch (error) {
      await logEvent(env, emailId, "ERROR", {
        message: error.message,
        stack: error.stack
      });

      // Still forward the email even if processing fails
      try {
        await message.forward(env.FORWARD_EMAIL || "rsplowman@icloud.com");
      } catch (forwardError) {
        // Last resort logging
        console.error("Forward failed:", forwardError);
      }
    }
  },

  // ─── HTTP HANDLER (for health checks) ──────────────────────────────────────
  async fetch(request, env) {
    return new Response(JSON.stringify({
      status: "ok",
      worker: "noizylab-email-worker",
      version: "2.0.0",
      timestamp: new Date().toISOString()
    }), {
      headers: { "Content-Type": "application/json" }
    });
  }
};

// ═══════════════════════════════════════════════════════════════════════════════
// HELPER FUNCTIONS
// ═══════════════════════════════════════════════════════════════════════════════

function calculateSpamScore(from, subject, body) {
  let score = 0;
  const content = `${subject} ${body}`.toLowerCase();
  const fromDomain = from.split("@")[1]?.toLowerCase() || "";

  // Check trusted domains
  if (TRUSTED_DOMAINS.some(d => fromDomain.includes(d))) {
    score -= 3;
  }

  // Check spam patterns
  SPAM_PATTERNS.forEach(pattern => {
    if (pattern.test(content)) {
      score += 2;
    }
  });

  // Check for excessive caps
  const capsRatio = (subject.match(/[A-Z]/g) || []).length / subject.length;
  if (capsRatio > 0.6 && subject.length > 10) {
    score += 2;
  }

  // Check for suspicious links
  const linkCount = (body.match(/https?:\/\//g) || []).length;
  if (linkCount > 5) {
    score += 1;
  }
  if (linkCount > 10) {
    score += 2;
  }

  // Check for common spam phrases
  const spamPhrases = ["click here", "act now", "limited time", "free", "winner", "congratulations"];
  spamPhrases.forEach(phrase => {
    if (content.includes(phrase)) {
      score += 1;
    }
  });

  return Math.max(0, score);
}

async function analyzeEmail(env, email) {
  try {
    const prompt = `Analyze this email and respond with ONLY valid JSON (no markdown, no extra text):

From: ${email.from}
To: ${email.to}
Subject: ${email.subject}
Body: ${email.body.substring(0, 2000)}

Required JSON format:
{
  "intent": "question|request|complaint|information|urgent|spam|other",
  "urgency": 0-10,
  "sentiment": "positive|negative|neutral",
  "summary": "brief 1-2 sentence summary",
  "keywords": ["keyword1", "keyword2"],
  "actionRequired": true/false,
  "suggestedAction": "what should be done"
}`;

    const response = await env.AI.run("@cf/mistral/mistral-7b-instruct-v0.1", {
      prompt,
      max_tokens: 500
    });

    // Extract JSON from response
    const jsonMatch = response.response?.match(/\{[\s\S]*\}/);
    if (jsonMatch) {
      return JSON.parse(jsonMatch[0]);
    }

    return {
      intent: "other",
      urgency: 5,
      sentiment: "neutral",
      summary: "Unable to analyze",
      keywords: [],
      actionRequired: false,
      suggestedAction: "Manual review required"
    };
  } catch (error) {
    return {
      intent: "error",
      urgency: 5,
      sentiment: "neutral",
      summary: "Analysis failed",
      keywords: [],
      actionRequired: true,
      suggestedAction: "Manual review required",
      error: error.message
    };
  }
}

function determineAgent(subject, body, analysis) {
  const content = `${subject} ${body}`.toLowerCase();

  // Check for urgent keywords first
  if (analysis.urgency >= 8 || /urgent|emergency|critical|asap|immediately/i.test(content)) {
    return AGENTS.RED_ALERT;
  }

  // Score each agent based on trigger matches
  let bestAgent = AGENTS.ECHO; // Default to communications
  let highestScore = 0;

  for (const [name, agent] of Object.entries(AGENTS)) {
    let score = 0;
    agent.triggers.forEach(trigger => {
      const regex = new RegExp(`\\b${trigger}\\b`, "gi");
      const matches = content.match(regex);
      if (matches) {
        score += matches.length;
      }
    });

    if (score > highestScore) {
      highestScore = score;
      bestAgent = agent;
    }
  }

  return bestAgent;
}

async function callAgent(env, agent, data) {
  try {
    const prompt = `You are ${agent.name}, the ${agent.role} at NoizyLab.
Your personality: ${agent.personality}
Your response style: ${agent.responseStyle}

Analyze this incoming email and provide your assessment:

From: ${data.from}
Subject: ${data.subject}
Summary: ${data.analysis.summary}
Urgency: ${data.analysis.urgency}/10
Sentiment: ${data.analysis.sentiment}

Respond with ONLY valid JSON:
{
  "agent": "${agent.name}",
  "assessment": "your professional assessment",
  "recommendedAction": "specific action to take",
  "priority": "low|medium|high|critical",
  "estimatedResponseTime": "time estimate",
  "notes": "any additional observations"
}`;

    const response = await env.AI.run("@cf/mistral/mistral-7b-instruct-v0.1", {
      prompt,
      max_tokens: 400
    });

    const jsonMatch = response.response?.match(/\{[\s\S]*\}/);
    if (jsonMatch) {
      return JSON.parse(jsonMatch[0]);
    }

    return {
      agent: agent.name,
      assessment: "Analysis completed",
      recommendedAction: "Review manually",
      priority: "medium",
      notes: "Automated response"
    };
  } catch (error) {
    return {
      agent: agent.name,
      error: error.message,
      priority: "medium"
    };
  }
}

function generateAutoReply(agent, analysis) {
  const templates = {
    RED_ALERT: `Thank you for your message. This has been flagged as URGENT and is being handled with the highest priority.

Our team has been immediately notified and will respond as soon as possible.

Summary of your request: ${analysis.summary}

– NoizyLab Emergency Response`,

    KEITH: `Thank you for your technical inquiry.

We've received your message and our technical team is reviewing it.

Summary: ${analysis.summary}

We'll get back to you with a detailed response shortly.

– NoizyLab Technical Team`,

    default: `Thank you for contacting NoizyLab.

We've received your message and it has been assigned to the appropriate team member.

Summary: ${analysis.summary}

Expected response time: Within 24 hours.

– NoizyLab Team`
  };

  return templates[agent.name] || templates.default;
}

async function sendWebhook(env, logEntry) {
  try {
    const agentEmojis = {
      LUCY: "🎨",
      KEITH: "⚙️",
      WARDY: "📋",
      RED_ALERT: "🚨",
      NOVA: "🔬",
      ECHO: "📢"
    };

    const priorityColors = {
      low: 0x2ECC71,
      medium: 0xF39C12,
      high: 0xE74C3C,
      critical: 0x9B59B6
    };

    const embed = {
      title: `📧 New Email: ${logEntry.subject.substring(0, 100)}`,
      description: logEntry.bodyPreview.substring(0, 300),
      color: priorityColors[logEntry.agentResponse?.priority] || 0x3498DB,
      fields: [
        { name: "From", value: logEntry.from, inline: true },
        { name: "Agent", value: `${agentEmojis[logEntry.agent] || "🤖"} ${logEntry.agent}`, inline: true },
        { name: "Urgency", value: `${logEntry.analysis?.urgency || "N/A"}/10`, inline: true },
        { name: "Intent", value: logEntry.analysis?.intent || "Unknown", inline: true },
        { name: "Priority", value: logEntry.agentResponse?.priority || "medium", inline: true },
        { name: "Spam Score", value: String(logEntry.spamScore), inline: true }
      ],
      footer: { text: `ID: ${logEntry.id} | Processed in ${logEntry.processingTime}ms` },
      timestamp: logEntry.timestamp
    };

    await fetch(env.WEBHOOK_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ embeds: [embed] })
    });
  } catch (error) {
    console.error("Webhook failed:", error);
  }
}

async function logEvent(env, id, type, data) {
  const entry = {
    id,
    type,
    timestamp: new Date().toISOString(),
    ...data
  };

  await env.MAIL_LOGS?.put(`${type}-${id}`, JSON.stringify(entry), { expirationTtl: 604800 }); // 7 days
}

async function updateAgentState(env, agentName, emailId) {
  const stateKey = `agent-${agentName}`;
  const currentState = JSON.parse(await env.AGENTS_STATE?.get(stateKey) || "{}");

  const newState = {
    ...currentState,
    lastActive: new Date().toISOString(),
    emailsProcessed: (currentState.emailsProcessed || 0) + 1,
    lastEmailId: emailId
  };

  await env.AGENTS_STATE?.put(stateKey, JSON.stringify(newState));
}
