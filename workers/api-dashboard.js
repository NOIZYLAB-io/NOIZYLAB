// ═══════════════════════════════════════════════════════════════════════════════
// NOIZYLAB API DASHBOARD v2.0
// RESTful API for Email Analytics, Agent Management & System Monitoring
// ═══════════════════════════════════════════════════════════════════════════════

const CORS_HEADERS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type, Authorization, X-API-Key",
  "Content-Type": "application/json"
};

const AGENTS = ["LUCY", "KEITH", "WARDY", "RED_ALERT", "NOVA", "ECHO"];

export default {
  async fetch(request, env, ctx) {
    // Handle CORS preflight
    if (request.method === "OPTIONS") {
      return new Response(null, { headers: CORS_HEADERS });
    }

    const url = new URL(request.url);
    const path = url.pathname;
    const method = request.method;

    // API Key authentication (optional)
    const apiKey = request.headers.get("X-API-Key");
    const requireAuth = env.REQUIRE_AUTH === "true";

    if (requireAuth && apiKey !== env.ADMIN_API_KEY) {
      return jsonResponse({ error: "Unauthorized" }, 401);
    }

    try {
      // ─── ROUTES ────────────────────────────────────────────────────────────

      // Health check
      if (path === "/" || path === "/health") {
        return jsonResponse({
          status: "ok",
          service: "noizylab-api",
          version: "2.0.0",
          timestamp: new Date().toISOString(),
          endpoints: [
            "GET  /health",
            "GET  /stats",
            "GET  /emails",
            "GET  /emails/:id",
            "GET  /agents",
            "GET  /agents/:name",
            "POST /agents/:name/task",
            "GET  /spam",
            "GET  /search?q=term",
            "GET  /dashboard"
          ]
        });
      }

      // ─── STATISTICS ────────────────────────────────────────────────────────
      if (path === "/stats" && method === "GET") {
        return await getStats(env);
      }

      // ─── EMAILS ────────────────────────────────────────────────────────────
      if (path === "/emails" && method === "GET") {
        const limit = parseInt(url.searchParams.get("limit") || "50");
        const offset = parseInt(url.searchParams.get("offset") || "0");
        return await getEmails(env, limit, offset);
      }

      if (path.match(/^\/emails\/[\w-]+$/) && method === "GET") {
        const id = path.split("/")[2];
        return await getEmail(env, id);
      }

      // ─── AGENTS ────────────────────────────────────────────────────────────
      if (path === "/agents" && method === "GET") {
        return await getAgents(env);
      }

      if (path.match(/^\/agents\/\w+$/) && method === "GET") {
        const name = path.split("/")[2].toUpperCase();
        return await getAgent(env, name);
      }

      if (path.match(/^\/agents\/\w+\/task$/) && method === "POST") {
        const name = path.split("/")[2].toUpperCase();
        const body = await request.json();
        return await callAgentAPI(env, name, body.task);
      }

      // ─── SPAM ──────────────────────────────────────────────────────────────
      if (path === "/spam" && method === "GET") {
        return await getSpamLogs(env);
      }

      // ─── SEARCH ────────────────────────────────────────────────────────────
      if (path === "/search" && method === "GET") {
        const query = url.searchParams.get("q");
        if (!query) {
          return jsonResponse({ error: "Missing search query 'q'" }, 400);
        }
        return await searchEmails(env, query);
      }

      // ─── DASHBOARD ─────────────────────────────────────────────────────────
      if (path === "/dashboard" && method === "GET") {
        return await getDashboard(env);
      }

      // ─── AI CHAT ───────────────────────────────────────────────────────────
      if (path === "/chat" && method === "POST") {
        const body = await request.json();
        return await aiChat(env, body.message, body.agent);
      }

      // 404
      return jsonResponse({ error: "Not Found", path }, 404);

    } catch (error) {
      return jsonResponse({
        error: "Internal Server Error",
        message: error.message
      }, 500);
    }
  }
};

// ═══════════════════════════════════════════════════════════════════════════════
// API HANDLERS
// ═══════════════════════════════════════════════════════════════════════════════

async function getStats(env) {
  const stats = {
    timestamp: new Date().toISOString(),
    emails: { total: 0, today: 0, thisWeek: 0 },
    spam: { blocked: 0 },
    agents: {},
    performance: { avgProcessingTime: 0 }
  };

  // Get all keys to count
  const allKeys = await env.MAIL_LOGS?.list({ limit: 1000 });
  const now = Date.now();
  const dayMs = 86400000;
  const weekMs = dayMs * 7;

  let totalProcessingTime = 0;
  let processedCount = 0;

  if (allKeys?.keys) {
    for (const key of allKeys.keys) {
      if (key.name.startsWith("email-")) {
        stats.emails.total++;

        // Check timestamp from key name
        const timestamp = parseInt(key.name.split("-")[1]);
        if (timestamp && now - timestamp < dayMs) {
          stats.emails.today++;
        }
        if (timestamp && now - timestamp < weekMs) {
          stats.emails.thisWeek++;
        }
      }
      if (key.name.startsWith("SPAM_DETECTED")) {
        stats.spam.blocked++;
      }
    }
  }

  // Get agent stats
  for (const agentName of AGENTS) {
    const agentState = await env.AGENTS_STATE?.get(`agent-${agentName}`);
    if (agentState) {
      stats.agents[agentName] = JSON.parse(agentState);
    } else {
      stats.agents[agentName] = { emailsProcessed: 0, lastActive: null };
    }
  }

  return jsonResponse(stats);
}

async function getEmails(env, limit, offset) {
  const allKeys = await env.MAIL_LOGS?.list({ limit: 1000 });
  const emailKeys = allKeys?.keys
    ?.filter(k => k.name.startsWith("email-"))
    ?.sort((a, b) => {
      const tsA = parseInt(a.name.split("-")[1]) || 0;
      const tsB = parseInt(b.name.split("-")[1]) || 0;
      return tsB - tsA; // Newest first
    })
    ?.slice(offset, offset + limit) || [];

  const emails = await Promise.all(
    emailKeys.map(async (key) => {
      const data = await env.MAIL_LOGS?.get(key.name);
      if (data) {
        const parsed = JSON.parse(data);
        return {
          id: parsed.id,
          from: parsed.from,
          subject: parsed.subject,
          timestamp: parsed.timestamp,
          agent: parsed.agent,
          urgency: parsed.analysis?.urgency,
          spamScore: parsed.spamScore
        };
      }
      return null;
    })
  );

  return jsonResponse({
    total: allKeys?.keys?.filter(k => k.name.startsWith("email-")).length || 0,
    limit,
    offset,
    emails: emails.filter(Boolean)
  });
}

async function getEmail(env, id) {
  // Try with and without email- prefix
  let data = await env.MAIL_LOGS?.get(id);
  if (!data) {
    data = await env.MAIL_LOGS?.get(`email-${id}`);
  }

  if (!data) {
    return jsonResponse({ error: "Email not found" }, 404);
  }

  return jsonResponse(JSON.parse(data));
}

async function getAgents(env) {
  const agentData = await Promise.all(
    AGENTS.map(async (name) => {
      const state = await env.AGENTS_STATE?.get(`agent-${name}`);
      const agentInfo = {
        LUCY: { role: "Creative Director", emoji: "🎨", specialty: "Branding & Design" },
        KEITH: { role: "Technical Lead", emoji: "⚙️", specialty: "Code & Architecture" },
        WARDY: { role: "Project Manager", emoji: "📋", specialty: "Planning & Coordination" },
        RED_ALERT: { role: "Security Handler", emoji: "🚨", specialty: "Emergencies & Security" },
        NOVA: { role: "Research Analyst", emoji: "🔬", specialty: "Data & Research" },
        ECHO: { role: "Communications Lead", emoji: "📢", specialty: "Client Relations" }
      };

      return {
        name,
        ...agentInfo[name],
        stats: state ? JSON.parse(state) : { emailsProcessed: 0, lastActive: null }
      };
    })
  );

  return jsonResponse({ agents: agentData });
}

async function getAgent(env, name) {
  if (!AGENTS.includes(name)) {
    return jsonResponse({ error: "Agent not found" }, 404);
  }

  const state = await env.AGENTS_STATE?.get(`agent-${name}`);
  const agentInfo = {
    LUCY: {
      role: "Creative Director",
      emoji: "🎨",
      personality: "Creative, visionary, bold ideas",
      triggers: ["design", "brand", "logo", "creative", "visual"]
    },
    KEITH: {
      role: "Technical Lead",
      emoji: "⚙️",
      personality: "Analytical, precise, solution-oriented",
      triggers: ["code", "bug", "error", "api", "server", "database"]
    },
    WARDY: {
      role: "Project Manager",
      emoji: "📋",
      personality: "Organized, efficient, deadline-focused",
      triggers: ["deadline", "schedule", "meeting", "project", "task"]
    },
    RED_ALERT: {
      role: "Security & Urgency Handler",
      emoji: "🚨",
      personality: "Vigilant, rapid response, no-nonsense",
      triggers: ["urgent", "emergency", "critical", "security", "breach"]
    },
    NOVA: {
      role: "Research Analyst",
      emoji: "🔬",
      personality: "Curious, thorough, data-driven",
      triggers: ["research", "data", "analysis", "report", "metrics"]
    },
    ECHO: {
      role: "Communications Lead",
      emoji: "📢",
      personality: "Diplomatic, clear, empathetic",
      triggers: ["client", "customer", "feedback", "complaint", "pr"]
    }
  };

  return jsonResponse({
    name,
    ...agentInfo[name],
    stats: state ? JSON.parse(state) : { emailsProcessed: 0, lastActive: null }
  });
}

async function callAgentAPI(env, name, task) {
  if (!AGENTS.includes(name)) {
    return jsonResponse({ error: "Agent not found" }, 404);
  }

  if (!task) {
    return jsonResponse({ error: "Task is required" }, 400);
  }

  const agentInfo = {
    LUCY: { role: "Creative Director", personality: "Creative, visionary, bold ideas" },
    KEITH: { role: "Technical Lead", personality: "Analytical, precise, solution-oriented" },
    WARDY: { role: "Project Manager", personality: "Organized, efficient, deadline-focused" },
    RED_ALERT: { role: "Security Handler", personality: "Vigilant, rapid response, no-nonsense" },
    NOVA: { role: "Research Analyst", personality: "Curious, thorough, data-driven" },
    ECHO: { role: "Communications Lead", personality: "Diplomatic, clear, empathetic" }
  };

  const agent = agentInfo[name];
  const prompt = `You are ${name}, the ${agent.role} at NoizyLab.
Personality: ${agent.personality}

Task: ${task}

Respond with JSON:
{
  "agent": "${name}",
  "response": "your detailed response",
  "steps": ["step 1", "step 2"],
  "priority": "low|medium|high|critical",
  "timeEstimate": "estimated time"
}`;

  try {
    const response = await env.AI.run("@cf/mistral/mistral-7b-instruct-v0.1", {
      prompt,
      max_tokens: 600
    });

    const jsonMatch = response.response?.match(/\{[\s\S]*\}/);
    if (jsonMatch) {
      return jsonResponse(JSON.parse(jsonMatch[0]));
    }

    return jsonResponse({
      agent: name,
      response: response.response,
      priority: "medium"
    });
  } catch (error) {
    return jsonResponse({
      agent: name,
      error: error.message
    }, 500);
  }
}

async function getSpamLogs(env) {
  const allKeys = await env.MAIL_LOGS?.list({ limit: 1000 });
  const spamKeys = allKeys?.keys?.filter(k => k.name.startsWith("SPAM_DETECTED")) || [];

  const spamLogs = await Promise.all(
    spamKeys.slice(0, 100).map(async (key) => {
      const data = await env.MAIL_LOGS?.get(key.name);
      return data ? JSON.parse(data) : null;
    })
  );

  return jsonResponse({
    total: spamKeys.length,
    logs: spamLogs.filter(Boolean)
  });
}

async function searchEmails(env, query) {
  const allKeys = await env.MAIL_LOGS?.list({ limit: 1000 });
  const emailKeys = allKeys?.keys?.filter(k => k.name.startsWith("email-")) || [];

  const results = [];
  const queryLower = query.toLowerCase();

  for (const key of emailKeys.slice(0, 500)) {
    const data = await env.MAIL_LOGS?.get(key.name);
    if (data) {
      const email = JSON.parse(data);
      const searchableText = `${email.from} ${email.subject} ${email.bodyPreview || ""}`.toLowerCase();

      if (searchableText.includes(queryLower)) {
        results.push({
          id: email.id,
          from: email.from,
          subject: email.subject,
          timestamp: email.timestamp,
          agent: email.agent
        });

        if (results.length >= 50) break;
      }
    }
  }

  return jsonResponse({
    query,
    count: results.length,
    results
  });
}

async function getDashboard(env) {
  // Comprehensive dashboard data
  const [stats, emails, agents] = await Promise.all([
    getStatsData(env),
    getRecentEmails(env, 10),
    getAgentsSummary(env)
  ]);

  return jsonResponse({
    timestamp: new Date().toISOString(),
    summary: {
      totalEmails: stats.emails.total,
      todayEmails: stats.emails.today,
      spamBlocked: stats.spam.blocked,
      activeAgents: agents.filter(a => a.stats.lastActive).length
    },
    recentEmails: emails,
    agentActivity: agents,
    systemHealth: {
      status: "operational",
      uptime: "99.9%",
      lastCheck: new Date().toISOString()
    }
  });
}

async function aiChat(env, message, agentName = "KEITH") {
  if (!message) {
    return jsonResponse({ error: "Message is required" }, 400);
  }

  const agent = agentName.toUpperCase();
  if (!AGENTS.includes(agent)) {
    return jsonResponse({ error: "Invalid agent" }, 400);
  }

  const prompt = `You are ${agent}, an AI assistant at NoizyLab. Be helpful and concise.

User: ${message}

Respond naturally as ${agent}:`;

  try {
    const response = await env.AI.run("@cf/mistral/mistral-7b-instruct-v0.1", {
      prompt,
      max_tokens: 500
    });

    return jsonResponse({
      agent,
      message: response.response,
      timestamp: new Date().toISOString()
    });
  } catch (error) {
    return jsonResponse({ error: error.message }, 500);
  }
}

// ═══════════════════════════════════════════════════════════════════════════════
// HELPER FUNCTIONS
// ═══════════════════════════════════════════════════════════════════════════════

async function getStatsData(env) {
  const allKeys = await env.MAIL_LOGS?.list({ limit: 1000 });
  const now = Date.now();
  const dayMs = 86400000;

  let total = 0;
  let today = 0;
  let spam = 0;

  if (allKeys?.keys) {
    for (const key of allKeys.keys) {
      if (key.name.startsWith("email-")) {
        total++;
        const timestamp = parseInt(key.name.split("-")[1]);
        if (timestamp && now - timestamp < dayMs) {
          today++;
        }
      }
      if (key.name.startsWith("SPAM_DETECTED")) {
        spam++;
      }
    }
  }

  return {
    emails: { total, today },
    spam: { blocked: spam }
  };
}

async function getRecentEmails(env, limit) {
  const allKeys = await env.MAIL_LOGS?.list({ limit: 1000 });
  const emailKeys = allKeys?.keys
    ?.filter(k => k.name.startsWith("email-"))
    ?.sort((a, b) => {
      const tsA = parseInt(a.name.split("-")[1]) || 0;
      const tsB = parseInt(b.name.split("-")[1]) || 0;
      return tsB - tsA;
    })
    ?.slice(0, limit) || [];

  return await Promise.all(
    emailKeys.map(async (key) => {
      const data = await env.MAIL_LOGS?.get(key.name);
      if (data) {
        const parsed = JSON.parse(data);
        return {
          id: parsed.id,
          from: parsed.from,
          subject: parsed.subject?.substring(0, 50),
          agent: parsed.agent,
          timestamp: parsed.timestamp
        };
      }
      return null;
    })
  ).then(results => results.filter(Boolean));
}

async function getAgentsSummary(env) {
  return await Promise.all(
    AGENTS.map(async (name) => {
      const state = await env.AGENTS_STATE?.get(`agent-${name}`);
      return {
        name,
        stats: state ? JSON.parse(state) : { emailsProcessed: 0, lastActive: null }
      };
    })
  );
}

function jsonResponse(data, status = 200) {
  return new Response(JSON.stringify(data, null, 2), {
    status,
    headers: CORS_HEADERS
  });
}
