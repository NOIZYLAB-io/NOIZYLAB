// ╔═══════════════════════════════════════════════════════════════════════════════╗
// ║   ██████╗ ██████╗ ██████╗ ███████╗███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗    ║
// ║  ██╔════╝██╔═══██╗██╔══██╗██╔════╝████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗   ║
// ║  ██║     ██║   ██║██║  ██║█████╗  ██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝   ║
// ║  ██║     ██║   ██║██║  ██║██╔══╝  ██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗   ║
// ║  ╚██████╗╚██████╔╝██████╔╝███████╗██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║   ║
// ║   ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝   ║
// ║                                                                                          ║
// ║                         MASTER API - THE UNIFIED CONTROL CENTER                          ║
// ╚═══════════════════════════════════════════════════════════════════════════════════════════╝

// ─── CONFIGURATION ───────────────────────────────────────────────────────────

const VERSION = "1.0.0";

const CORS_HEADERS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type, Authorization, X-API-Key",
  "Content-Type": "application/json"
};

// ─── AGENTS REGISTRY ─────────────────────────────────────────────────────────

const AGENTS = {
  CODEMASTER: { name: "CODEMASTER", role: "Supreme Commander", emoji: "👑", priority: 0 },
  ARCHITECT: { name: "ARCHITECT", role: "System Architect", emoji: "🏗️", priority: 1 },
  FORGE: { name: "FORGE", role: "Code Forge Master", emoji: "🔨", priority: 1 },
  SENTINEL: { name: "SENTINEL", role: "Security Guardian", emoji: "🛡️", priority: 1 },
  ORACLE: { name: "ORACLE", role: "Knowledge Keeper", emoji: "🔮", priority: 2 },
  PHANTOM: { name: "PHANTOM", role: "Debug Hunter", emoji: "👻", priority: 1 },
  NEXUS: { name: "NEXUS", role: "Integration Master", emoji: "🔗", priority: 2 },
  CHRONOS: { name: "CHRONOS", role: "Automation Timekeeper", emoji: "⏰", priority: 2 },
  // Original NoizyLab agents
  LUCY: { name: "LUCY", role: "Creative Director", emoji: "🎨", priority: 2 },
  KEITH: { name: "KEITH", role: "Technical Lead", emoji: "⚙️", priority: 2 },
  WARDY: { name: "WARDY", role: "Project Manager", emoji: "📋", priority: 2 },
  RED_ALERT: { name: "RED_ALERT", role: "Emergency Handler", emoji: "🚨", priority: 1 },
  NOVA: { name: "NOVA", role: "Research Analyst", emoji: "🔬", priority: 2 },
  ECHO: { name: "ECHO", role: "Communications Lead", emoji: "📢", priority: 2 }
};

// ─── GENERATORS ──────────────────────────────────────────────────────────────

const GENERATORS = [
  { id: "worker", name: "Cloudflare Worker", description: "Edge computing worker" },
  { id: "api", name: "REST API", description: "Full REST API with CRUD" },
  { id: "cli", name: "CLI Tool", description: "Command-line interface" },
  { id: "component", name: "React Component", description: "React functional component" },
  { id: "server", name: "Express Server", description: "Node.js server" },
  { id: "model", name: "Database Model", description: "Database schema" },
  { id: "test", name: "Test Suite", description: "Comprehensive tests" },
  { id: "project", name: "Full Project", description: "Complete scaffold" }
];

// ─── BLUEPRINTS ──────────────────────────────────────────────────────────────

const BLUEPRINTS = [
  { id: "cf-email-system", name: "Cloudflare Email System", category: "cloudflare" },
  { id: "cf-api", name: "Cloudflare API", category: "cloudflare" },
  { id: "cf-ai-agent", name: "Cloudflare AI Agent", category: "cloudflare" },
  { id: "cli-tool", name: "CLI Tool", category: "cli" },
  { id: "cli-ai", name: "AI CLI Assistant", category: "cli" },
  { id: "fullstack-app", name: "Full Stack Application", category: "fullstack" },
  { id: "saas-starter", name: "SaaS Starter Kit", category: "fullstack" },
  { id: "discord-bot", name: "Discord Bot", category: "bot" },
  { id: "microservice", name: "Microservice", category: "backend" },
  { id: "graphql-api", name: "GraphQL API", category: "backend" }
];

// ═══════════════════════════════════════════════════════════════════════════════
// MAIN HANDLER
// ═══════════════════════════════════════════════════════════════════════════════

export default {
  async fetch(request, env, ctx) {
    // Handle CORS preflight
    if (request.method === "OPTIONS") {
      return new Response(null, { headers: CORS_HEADERS });
    }

    const url = new URL(request.url);
    const path = url.pathname;
    const method = request.method;

    // Optional authentication
    const apiKey = request.headers.get("X-API-Key");
    if (env.REQUIRE_AUTH === "true" && apiKey !== env.ADMIN_API_KEY) {
      return json({ error: "Unauthorized" }, 401);
    }

    try {
      // ─── HEALTH & INFO ─────────────────────────────────────────────────────

      if (path === "/" || path === "/health") {
        return json({
          name: "CODEMASTER API",
          version: VERSION,
          status: "operational",
          timestamp: new Date().toISOString(),
          endpoints: getEndpoints()
        });
      }

      if (path === "/status") {
        return json(await getSystemStatus(env));
      }

      // ─── AGENTS ────────────────────────────────────────────────────────────

      if (path === "/agents" && method === "GET") {
        return json({
          count: Object.keys(AGENTS).length,
          agents: Object.values(AGENTS).map(a => ({
            ...a,
            available: true
          }))
        });
      }

      if (path.match(/^\/agents\/\w+$/) && method === "GET") {
        const name = path.split("/")[2].toUpperCase();
        const agent = AGENTS[name];
        if (!agent) return json({ error: "Agent not found" }, 404);

        const state = await env.CODEMASTER_STATE?.get(`agent-${name}`, "json") || {};
        return json({ ...agent, state });
      }

      if (path.match(/^\/agents\/\w+\/execute$/) && method === "POST") {
        const name = path.split("/")[2].toUpperCase();
        const body = await request.json();
        return json(await executeAgent(env, name, body));
      }

      // ─── GENERATORS ────────────────────────────────────────────────────────

      if (path === "/generators" && method === "GET") {
        return json({ generators: GENERATORS });
      }

      if (path === "/generate" && method === "POST") {
        const body = await request.json();
        return json(await generateCode(env, body));
      }

      // ─── BLUEPRINTS ────────────────────────────────────────────────────────

      if (path === "/blueprints" && method === "GET") {
        const category = url.searchParams.get("category");
        let blueprints = BLUEPRINTS;
        if (category) {
          blueprints = blueprints.filter(b => b.category === category);
        }
        return json({ blueprints });
      }

      if (path === "/blueprints/scaffold" && method === "POST") {
        const body = await request.json();
        return json(await scaffoldProject(env, body));
      }

      // ─── WORKFLOWS ─────────────────────────────────────────────────────────

      if (path === "/workflows" && method === "GET") {
        const workflows = await env.CODEMASTER_STATE?.get("workflows", "json") || [];
        return json({ workflows });
      }

      if (path === "/workflows" && method === "POST") {
        const body = await request.json();
        return json(await createWorkflow(env, body));
      }

      if (path.match(/^\/workflows\/[\w-]+\/run$/) && method === "POST") {
        const id = path.split("/")[2];
        const body = await request.json();
        return json(await runWorkflow(env, id, body));
      }

      // ─── TASKS ─────────────────────────────────────────────────────────────

      if (path === "/tasks" && method === "GET") {
        const tasks = await env.CODEMASTER_STATE?.get("tasks", "json") || [];
        return json({ tasks: tasks.slice(-100) });
      }

      if (path === "/tasks" && method === "POST") {
        const body = await request.json();
        return json(await createTask(env, body));
      }

      // ─── AI CHAT ───────────────────────────────────────────────────────────

      if (path === "/chat" && method === "POST") {
        const body = await request.json();
        return json(await aiChat(env, body));
      }

      // ─── ORCHESTRATE ───────────────────────────────────────────────────────

      if (path === "/orchestrate" && method === "POST") {
        const body = await request.json();
        return json(await orchestrate(env, body));
      }

      // ─── ANALYZE ───────────────────────────────────────────────────────────

      if (path === "/analyze" && method === "POST") {
        const body = await request.json();
        return json(await analyzeCode(env, body));
      }

      // ─── METRICS ───────────────────────────────────────────────────────────

      if (path === "/metrics" && method === "GET") {
        return json(await getMetrics(env));
      }

      // 404 Not Found
      return json({ error: "Not Found", path, availableEndpoints: getEndpoints() }, 404);

    } catch (error) {
      console.error("API Error:", error);
      return json({ error: error.message, stack: error.stack }, 500);
    }
  }
};

// ═══════════════════════════════════════════════════════════════════════════════
// API HANDLERS
// ═══════════════════════════════════════════════════════════════════════════════

async function getSystemStatus(env) {
  const metrics = await env.CODEMASTER_STATE?.get("metrics", "json") || {
    tasksCompleted: 0,
    agentCalls: 0,
    codeGenerated: 0
  };

  return {
    name: "CODEMASTER",
    version: VERSION,
    status: "operational",
    uptime: "99.9%",
    agents: {
      total: Object.keys(AGENTS).length,
      active: Object.keys(AGENTS).length
    },
    generators: GENERATORS.length,
    blueprints: BLUEPRINTS.length,
    metrics,
    timestamp: new Date().toISOString()
  };
}

async function executeAgent(env, agentName, params) {
  const agent = AGENTS[agentName];
  if (!agent) {
    throw new Error(`Agent not found: ${agentName}`);
  }

  const { task, context = {} } = params;
  const taskId = `task-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;

  // Build AI prompt
  const prompt = `You are ${agent.name}, the ${agent.role} in the CODEMASTER system.
Your emoji: ${agent.emoji}

Task: ${task}
Context: ${JSON.stringify(context)}

Provide a detailed, actionable response. If generating code, use proper formatting.
Respond in JSON format:
{
  "agent": "${agent.name}",
  "response": "your detailed response",
  "actions": ["action 1", "action 2"],
  "code": "any generated code (optional)",
  "recommendations": ["recommendation 1"]
}`;

  try {
    const aiResponse = await env.AI.run("@cf/mistral/mistral-7b-instruct-v0.1", {
      prompt,
      max_tokens: 2000
    });

    // Parse response
    let result;
    try {
      const jsonMatch = aiResponse.response?.match(/\{[\s\S]*\}/);
      result = jsonMatch ? JSON.parse(jsonMatch[0]) : { response: aiResponse.response };
    } catch {
      result = { response: aiResponse.response };
    }

    // Update metrics
    await updateMetrics(env, "agentCalls", 1);

    // Log task
    await logTask(env, {
      id: taskId,
      agent: agentName,
      task,
      result,
      timestamp: new Date().toISOString()
    });

    return {
      taskId,
      agent: agent.name,
      emoji: agent.emoji,
      ...result
    };

  } catch (error) {
    return {
      taskId,
      agent: agent.name,
      error: error.message
    };
  }
}

async function generateCode(env, params) {
  const { type, spec = {}, options = {} } = params;

  const generator = GENERATORS.find(g => g.id === type);
  if (!generator) {
    throw new Error(`Unknown generator: ${type}`);
  }

  // Use FORGE agent for generation
  const result = await executeAgent(env, "FORGE", {
    task: `Generate a ${generator.name} with the following specification: ${JSON.stringify(spec)}`,
    context: { generatorType: type, options }
  });

  await updateMetrics(env, "codeGenerated", 1);

  return {
    generator: type,
    ...result
  };
}

async function scaffoldProject(env, params) {
  const { blueprint, name, options = {} } = params;

  const bp = BLUEPRINTS.find(b => b.id === blueprint);
  if (!bp) {
    throw new Error(`Blueprint not found: ${blueprint}`);
  }

  // Use ARCHITECT agent for scaffolding
  const result = await executeAgent(env, "ARCHITECT", {
    task: `Scaffold a new project using the "${bp.name}" blueprint named "${name}"`,
    context: { blueprint: bp, options }
  });

  return {
    blueprint: bp.id,
    projectName: name,
    ...result
  };
}

async function createWorkflow(env, params) {
  const { name, steps, triggers = [] } = params;

  const workflow = {
    id: `wf-${Date.now()}`,
    name,
    steps,
    triggers,
    createdAt: new Date().toISOString(),
    status: "active"
  };

  const workflows = await env.CODEMASTER_STATE?.get("workflows", "json") || [];
  workflows.push(workflow);
  await env.CODEMASTER_STATE?.put("workflows", JSON.stringify(workflows));

  return workflow;
}

async function runWorkflow(env, id, params) {
  const workflows = await env.CODEMASTER_STATE?.get("workflows", "json") || [];
  const workflow = workflows.find(w => w.id === id);

  if (!workflow) {
    throw new Error(`Workflow not found: ${id}`);
  }

  // Execute with CHRONOS agent
  return executeAgent(env, "CHRONOS", {
    task: `Execute workflow "${workflow.name}"`,
    context: { workflow, input: params.input }
  });
}

async function createTask(env, params) {
  const { command, agent = "CODEMASTER", priority = "medium" } = params;

  const task = {
    id: `task-${Date.now()}`,
    command,
    agent,
    priority,
    status: "pending",
    createdAt: new Date().toISOString()
  };

  // Execute immediately or queue based on priority
  if (priority === "critical" || priority === "high") {
    const result = await executeAgent(env, agent, { task: command });
    task.status = "completed";
    task.result = result;
  }

  await logTask(env, task);
  return task;
}

async function aiChat(env, params) {
  const { message, agent = "CODEMASTER", context = {} } = params;

  return executeAgent(env, agent.toUpperCase(), {
    task: message,
    context
  });
}

async function orchestrate(env, params) {
  const { workflow, steps } = params;

  const results = [];

  for (const step of steps) {
    const { agent, task, dependsOn } = step;

    // Check dependencies
    if (dependsOn) {
      const depResult = results.find(r => r.step === dependsOn);
      if (!depResult || !depResult.success) {
        results.push({ step: step.name, skipped: true, reason: `Dependency ${dependsOn} not met` });
        continue;
      }
    }

    const result = await executeAgent(env, agent || "CODEMASTER", { task });
    results.push({
      step: step.name,
      agent,
      success: !result.error,
      result
    });
  }

  return {
    workflow,
    completed: results.filter(r => r.success).length,
    total: steps.length,
    results
  };
}

async function analyzeCode(env, params) {
  const { code, language = "javascript", aspects = ["security", "performance", "quality"] } = params;

  const analyses = await Promise.all(
    aspects.map(aspect => {
      const agentMap = {
        security: "SENTINEL",
        performance: "FORGE",
        quality: "ARCHITECT",
        documentation: "ORACLE",
        bugs: "PHANTOM"
      };

      return executeAgent(env, agentMap[aspect] || "CODEMASTER", {
        task: `Analyze the following ${language} code for ${aspect}:\n\n${code}`,
        context: { aspect }
      });
    })
  );

  return {
    language,
    aspects,
    analyses
  };
}

async function getMetrics(env) {
  return await env.CODEMASTER_STATE?.get("metrics", "json") || {
    tasksCompleted: 0,
    agentCalls: 0,
    codeGenerated: 0,
    workflowsRun: 0,
    errors: 0,
    lastUpdated: null
  };
}

// ═══════════════════════════════════════════════════════════════════════════════
// HELPERS
// ═══════════════════════════════════════════════════════════════════════════════

function json(data, status = 200) {
  return new Response(JSON.stringify(data, null, 2), {
    status,
    headers: CORS_HEADERS
  });
}

function getEndpoints() {
  return [
    "GET  /                    - API info",
    "GET  /status              - System status",
    "GET  /agents              - List all agents",
    "GET  /agents/:name        - Get agent details",
    "POST /agents/:name/execute - Execute agent task",
    "GET  /generators          - List code generators",
    "POST /generate            - Generate code",
    "GET  /blueprints          - List project blueprints",
    "POST /blueprints/scaffold - Scaffold project",
    "GET  /workflows           - List workflows",
    "POST /workflows           - Create workflow",
    "POST /workflows/:id/run   - Run workflow",
    "GET  /tasks               - List tasks",
    "POST /tasks               - Create task",
    "POST /chat                - AI chat",
    "POST /orchestrate         - Orchestrate multi-agent workflow",
    "POST /analyze             - Analyze code",
    "GET  /metrics             - Get metrics"
  ];
}

async function updateMetrics(env, key, increment = 1) {
  const metrics = await env.CODEMASTER_STATE?.get("metrics", "json") || {
    tasksCompleted: 0,
    agentCalls: 0,
    codeGenerated: 0,
    workflowsRun: 0,
    errors: 0
  };

  metrics[key] = (metrics[key] || 0) + increment;
  metrics.lastUpdated = new Date().toISOString();

  await env.CODEMASTER_STATE?.put("metrics", JSON.stringify(metrics));
}

async function logTask(env, task) {
  const tasks = await env.CODEMASTER_STATE?.get("tasks", "json") || [];
  tasks.push(task);

  // Keep only last 1000 tasks
  if (tasks.length > 1000) {
    tasks.splice(0, tasks.length - 1000);
  }

  await env.CODEMASTER_STATE?.put("tasks", JSON.stringify(tasks));
  await updateMetrics(env, "tasksCompleted", 1);
}
