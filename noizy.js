#!/usr/bin/env node
// ═══════════════════════════════════════════════════════════════════════════════
// NOIZYLAB CLI v2.0 - AI-POWERED COMMAND CENTER
// ═══════════════════════════════════════════════════════════════════════════════

import { execSync, spawn } from "child_process";
import fs from "fs";
import path from "path";
import readline from "readline";

// ─── COLORS ──────────────────────────────────────────────────────────────────
const C = {
  reset: "\x1b[0m",
  bright: "\x1b[1m",
  dim: "\x1b[2m",
  red: "\x1b[31m",
  green: "\x1b[32m",
  yellow: "\x1b[33m",
  blue: "\x1b[34m",
  magenta: "\x1b[35m",
  cyan: "\x1b[36m",
  white: "\x1b[37m",
  bgRed: "\x1b[41m",
  bgGreen: "\x1b[42m",
  bgYellow: "\x1b[43m",
  bgBlue: "\x1b[44m",
  bgMagenta: "\x1b[45m",
  bgCyan: "\x1b[46m",
};

// ─── HELPERS ─────────────────────────────────────────────────────────────────
const log = (msg) => console.log(msg);
const success = (msg) => log(`${C.green}✓${C.reset} ${msg}`);
const error = (msg) => log(`${C.red}✗${C.reset} ${msg}`);
const info = (msg) => log(`${C.cyan}ℹ${C.reset} ${msg}`);
const warn = (msg) => log(`${C.yellow}⚠${C.reset} ${msg}`);

function sh(cmd, silent = false) {
  try {
    return execSync(cmd, { encoding: "utf8", stdio: silent ? "pipe" : "inherit" });
  } catch (e) {
    if (!silent) error(`Command failed: ${cmd}`);
    return null;
  }
}

function shOutput(cmd) {
  try {
    return execSync(cmd, { encoding: "utf8" }).trim();
  } catch {
    return null;
  }
}

// ─── BANNER ──────────────────────────────────────────────────────────────────
function banner() {
  console.log(`
${C.magenta}${C.bright}
    ╔═╗╔═╗╔═╗╔═╗╔═╗  ╦  ╔═╗╔╗   ${C.reset}${C.cyan}v2.0${C.reset}
${C.magenta}${C.bright}    ║║║║ ║║╔╝╚═╗╠═╝  ║  ╠═╣╠╩╗  ${C.reset}${C.dim}AI Command Center${C.reset}
${C.magenta}${C.bright}    ╝╚╝╚═╝╚╝ ╚═╝╩    ╩═╝╩ ╩╚═╝  ${C.reset}${C.dim}━━━━━━━━━━━━━━━━━${C.reset}
`);
}

// ─── AGENTS ──────────────────────────────────────────────────────────────────
const AGENTS = {
  LUCY: {
    name: "LUCY",
    role: "Creative Director",
    emoji: "🎨",
    color: C.magenta,
    description: "Creative strategy, branding, visual concepts",
    personality: "Creative, visionary, bold ideas"
  },
  KEITH: {
    name: "KEITH",
    role: "Technical Lead",
    emoji: "⚙️",
    color: C.blue,
    description: "Code review, architecture, technical decisions",
    personality: "Analytical, precise, solution-oriented"
  },
  WARDY: {
    name: "WARDY",
    role: "Project Manager",
    emoji: "📋",
    color: C.green,
    description: "Task management, scheduling, coordination",
    personality: "Organized, efficient, deadline-focused"
  },
  RED_ALERT: {
    name: "RED_ALERT",
    role: "Security & Urgency Handler",
    emoji: "🚨",
    color: C.red,
    description: "Emergency response, security issues, critical alerts",
    personality: "Vigilant, rapid response, no-nonsense"
  },
  NOVA: {
    name: "NOVA",
    role: "Research Analyst",
    emoji: "🔬",
    color: C.cyan,
    description: "Data analysis, market research, insights",
    personality: "Curious, thorough, data-driven"
  },
  ECHO: {
    name: "ECHO",
    role: "Communications Lead",
    emoji: "📢",
    color: C.yellow,
    description: "Client communications, messaging, PR",
    personality: "Diplomatic, clear, empathetic"
  }
};

// ─── COMMANDS ────────────────────────────────────────────────────────────────
const commands = {
  help: {
    desc: "Show this help message",
    usage: "noizy help",
    run: showHelp
  },
  init: {
    desc: "Initialize NoizyLab project",
    usage: "noizy init",
    run: initProject
  },
  status: {
    desc: "Show system status and stats",
    usage: "noizy status",
    run: showStatus
  },
  deploy: {
    desc: "Deploy workers to Cloudflare",
    usage: "noizy deploy [email|api|all]",
    run: deployWorkers
  },
  agent: {
    desc: "Summon an AI agent",
    usage: "noizy agent <NAME> <TASK>",
    run: summonAgent
  },
  agents: {
    desc: "List all available agents",
    usage: "noizy agents",
    run: listAgents
  },
  logs: {
    desc: "View email/agent logs",
    usage: "noizy logs [--tail] [--filter=<term>]",
    run: viewLogs
  },
  config: {
    desc: "Manage configuration",
    usage: "noizy config [get|set] <key> [value]",
    run: manageConfig
  },
  test: {
    desc: "Test email worker locally",
    usage: "noizy test <email-json-file>",
    run: testWorker
  },
  shell: {
    desc: "Interactive agent shell",
    usage: "noizy shell",
    run: interactiveShell
  },
  webhook: {
    desc: "Test webhook notifications",
    usage: "noizy webhook <message>",
    run: testWebhook
  },
  kv: {
    desc: "Manage KV store",
    usage: "noizy kv [list|get|delete] <key>",
    run: manageKV
  }
};

// ─── COMMAND IMPLEMENTATIONS ─────────────────────────────────────────────────

function showHelp() {
  banner();
  log(`${C.bright}COMMANDS:${C.reset}\n`);

  for (const [name, cmd] of Object.entries(commands)) {
    log(`  ${C.cyan}${name.padEnd(12)}${C.reset} ${cmd.desc}`);
    log(`  ${C.dim}${cmd.usage}${C.reset}\n`);
  }

  log(`${C.bright}EXAMPLES:${C.reset}\n`);
  log(`  ${C.dim}$${C.reset} noizy agent LUCY "Design a new logo concept"`);
  log(`  ${C.dim}$${C.reset} noizy deploy all`);
  log(`  ${C.dim}$${C.reset} noizy shell`);
  log(`  ${C.dim}$${C.reset} noizy logs --tail\n`);
}

function initProject() {
  banner();
  info("Initializing NoizyLab project...\n");

  const dirs = ["workers", "agents", "templates", "lib", "config", "tests"];
  dirs.forEach(dir => {
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
      success(`Created ${dir}/`);
    } else {
      info(`${dir}/ already exists`);
    }
  });

  // Create default config
  const configPath = "config/noizylab.json";
  if (!fs.existsSync(configPath)) {
    const defaultConfig = {
      version: "2.0.0",
      forwardEmail: "rsplowman@icloud.com",
      webhookEnabled: true,
      spamThreshold: 7,
      maxEmailsPerHour: 100,
      agents: Object.keys(AGENTS),
      createdAt: new Date().toISOString()
    };
    fs.writeFileSync(configPath, JSON.stringify(defaultConfig, null, 2));
    success(`Created ${configPath}`);
  }

  log("");
  success("Project initialized!\n");
  info("Next steps:");
  log(`  1. Update KV namespace IDs in ${C.cyan}wrangler.toml${C.reset}`);
  log(`  2. Run ${C.cyan}npm install${C.reset}`);
  log(`  3. Run ${C.cyan}noizy deploy all${C.reset}`);
  log("");
}

function showStatus() {
  banner();
  log(`${C.bright}SYSTEM STATUS${C.reset}\n`);

  // Check wrangler
  const wranglerVersion = shOutput("npx wrangler --version");
  if (wranglerVersion) {
    success(`Wrangler: ${wranglerVersion}`);
  } else {
    error("Wrangler: Not installed");
  }

  // Check Node
  const nodeVersion = shOutput("node --version");
  success(`Node.js: ${nodeVersion}`);

  // Check files
  const files = [
    "package.json",
    "wrangler.toml",
    "workers/email-worker.js",
    "workers/api-dashboard.js",
    "config/noizylab.json"
  ];

  log(`\n${C.bright}FILES${C.reset}\n`);
  files.forEach(f => {
    if (fs.existsSync(f)) {
      success(f);
    } else {
      warn(`${f} (missing)`);
    }
  });

  // Show agents
  log(`\n${C.bright}AGENTS${C.reset}\n`);
  Object.values(AGENTS).forEach(a => {
    log(`  ${a.emoji} ${a.color}${a.name}${C.reset} - ${a.role}`);
  });

  log("");
}

function deployWorkers(args) {
  banner();
  const target = args[0] || "all";

  if (target === "email" || target === "all") {
    info("Deploying email worker...");
    sh("npx wrangler deploy workers/email-worker.js");
    success("Email worker deployed!");
  }

  if (target === "api" || target === "all") {
    info("Deploying API dashboard worker...");
    sh("npx wrangler deploy workers/api-dashboard.js");
    success("API dashboard deployed!");
  }

  log("");
  success("Deployment complete!");
}

function summonAgent(args) {
  const agentName = args[0]?.toUpperCase();
  const task = args.slice(1).join(" ");

  if (!agentName || !task) {
    error("Usage: noizy agent <NAME> <TASK>");
    log(`\nAvailable agents: ${Object.keys(AGENTS).join(", ")}`);
    return;
  }

  const agent = AGENTS[agentName];
  if (!agent) {
    error(`Unknown agent: ${agentName}`);
    log(`\nAvailable agents: ${Object.keys(AGENTS).join(", ")}`);
    return;
  }

  banner();
  log(`${agent.emoji} ${agent.color}${C.bright}SUMMONING ${agent.name}${C.reset}`);
  log(`${C.dim}${agent.role} - ${agent.description}${C.reset}\n`);
  info(`Task: ${task}\n`);

  const prompt = `You are ${agent.name}, the ${agent.role} at NoizyLab.
Personality: ${agent.personality}
Specialization: ${agent.description}

Task: ${task}

Respond in JSON format:
{
  "agent": "${agent.name}",
  "analysis": "your analysis of the task",
  "action": "recommended action",
  "steps": ["step 1", "step 2", ...],
  "priority": "low|medium|high|critical",
  "notes": "additional notes"
}`;

  info("Thinking...\n");

  // Use wrangler AI
  const escapedPrompt = prompt.replace(/"/g, '\\"').replace(/\n/g, '\\n');
  const result = shOutput(`npx wrangler ai run @cf/mistral/mistral-7b-instruct-v0.1 "${escapedPrompt}" 2>/dev/null`);

  if (result) {
    try {
      const parsed = JSON.parse(result);
      log(`${C.bright}RESPONSE:${C.reset}\n`);
      log(`${C.cyan}Analysis:${C.reset} ${parsed.analysis || "N/A"}`);
      log(`${C.cyan}Action:${C.reset} ${parsed.action || "N/A"}`);
      log(`${C.cyan}Priority:${C.reset} ${parsed.priority || "N/A"}`);
      if (parsed.steps) {
        log(`${C.cyan}Steps:${C.reset}`);
        parsed.steps.forEach((s, i) => log(`  ${i + 1}. ${s}`));
      }
      if (parsed.notes) {
        log(`${C.cyan}Notes:${C.reset} ${parsed.notes}`);
      }
    } catch {
      log(result);
    }
  } else {
    warn("Could not reach AI. Make sure you're logged in: npx wrangler login");
  }

  log("");
}

function listAgents() {
  banner();
  log(`${C.bright}NOIZYLAB AGENTS${C.reset}\n`);

  Object.values(AGENTS).forEach(agent => {
    log(`${agent.emoji} ${agent.color}${C.bright}${agent.name}${C.reset}`);
    log(`   ${C.dim}Role:${C.reset} ${agent.role}`);
    log(`   ${C.dim}Specialty:${C.reset} ${agent.description}`);
    log(`   ${C.dim}Personality:${C.reset} ${agent.personality}`);
    log("");
  });

  log(`${C.dim}Usage: noizy agent <NAME> <TASK>${C.reset}\n`);
}

function viewLogs(args) {
  banner();
  const tail = args.includes("--tail");
  const filterArg = args.find(a => a.startsWith("--filter="));
  const filter = filterArg ? filterArg.split("=")[1] : null;

  if (tail) {
    info("Tailing logs (Ctrl+C to exit)...\n");
    sh("npx wrangler tail");
  } else {
    info("Fetching KV logs...\n");
    const cmd = filter
      ? `npx wrangler kv:key list --namespace-id YOUR_MAIL_LOGS_KV_ID | grep "${filter}"`
      : "npx wrangler kv:key list --namespace-id YOUR_MAIL_LOGS_KV_ID";
    sh(cmd);
  }
}

function manageConfig(args) {
  const action = args[0];
  const key = args[1];
  const value = args[2];
  const configPath = "config/noizylab.json";

  if (!fs.existsSync(configPath)) {
    error("Config not found. Run 'noizy init' first.");
    return;
  }

  const config = JSON.parse(fs.readFileSync(configPath, "utf8"));

  if (!action || action === "get") {
    banner();
    log(`${C.bright}CONFIGURATION${C.reset}\n`);
    if (key) {
      log(`${C.cyan}${key}:${C.reset} ${JSON.stringify(config[key], null, 2)}`);
    } else {
      log(JSON.stringify(config, null, 2));
    }
  } else if (action === "set" && key && value !== undefined) {
    // Try to parse as JSON, otherwise use as string
    try {
      config[key] = JSON.parse(value);
    } catch {
      config[key] = value;
    }
    config.updatedAt = new Date().toISOString();
    fs.writeFileSync(configPath, JSON.stringify(config, null, 2));
    success(`Set ${key} = ${value}`);
  } else {
    error("Usage: noizy config [get|set] <key> [value]");
  }

  log("");
}

function testWorker(args) {
  const file = args[0];

  if (!file) {
    error("Usage: noizy test <email-json-file>");
    log("\nExample email.json:");
    log(JSON.stringify({
      from: "sender@example.com",
      to: "inbox@noizylab.ca",
      subject: "Test Email",
      body: "This is a test message"
    }, null, 2));
    return;
  }

  if (!fs.existsSync(file)) {
    error(`File not found: ${file}`);
    return;
  }

  banner();
  info(`Testing with ${file}...\n`);

  const email = JSON.parse(fs.readFileSync(file, "utf8"));
  log(`${C.cyan}From:${C.reset} ${email.from}`);
  log(`${C.cyan}To:${C.reset} ${email.to}`);
  log(`${C.cyan}Subject:${C.reset} ${email.subject}`);
  log(`${C.cyan}Body:${C.reset} ${email.body?.substring(0, 100)}...`);
  log("");

  info("Starting local dev server...");
  sh("npx wrangler dev workers/email-worker.js --local");
}

async function interactiveShell() {
  banner();
  log(`${C.bright}INTERACTIVE AGENT SHELL${C.reset}`);
  log(`${C.dim}Type 'help' for commands, 'exit' to quit${C.reset}\n`);

  let currentAgent = AGENTS.KEITH;

  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  const prompt = () => {
    rl.question(`${currentAgent.emoji} ${currentAgent.color}${currentAgent.name}${C.reset} > `, async (input) => {
      const trimmed = input.trim();

      if (!trimmed) {
        prompt();
        return;
      }

      if (trimmed === "exit" || trimmed === "quit") {
        log("\nGoodbye! 👋\n");
        rl.close();
        return;
      }

      if (trimmed === "help") {
        log(`\n${C.bright}SHELL COMMANDS:${C.reset}`);
        log(`  ${C.cyan}switch <AGENT>${C.reset} - Switch to different agent`);
        log(`  ${C.cyan}agents${C.reset}         - List all agents`);
        log(`  ${C.cyan}clear${C.reset}          - Clear screen`);
        log(`  ${C.cyan}exit${C.reset}           - Exit shell`);
        log(`  ${C.dim}Or type any task for the current agent${C.reset}\n`);
        prompt();
        return;
      }

      if (trimmed === "agents") {
        Object.values(AGENTS).forEach(a => {
          const marker = a.name === currentAgent.name ? " ←" : "";
          log(`  ${a.emoji} ${a.color}${a.name}${C.reset} - ${a.role}${marker}`);
        });
        log("");
        prompt();
        return;
      }

      if (trimmed === "clear") {
        console.clear();
        banner();
        prompt();
        return;
      }

      if (trimmed.startsWith("switch ")) {
        const name = trimmed.split(" ")[1]?.toUpperCase();
        if (AGENTS[name]) {
          currentAgent = AGENTS[name];
          success(`Switched to ${currentAgent.name}`);
        } else {
          error(`Unknown agent: ${name}`);
        }
        log("");
        prompt();
        return;
      }

      // Send to agent
      log(`\n${C.dim}Thinking...${C.reset}\n`);
      summonAgent([currentAgent.name, trimmed]);
      prompt();
    });
  };

  prompt();
}

function testWebhook(args) {
  const message = args.join(" ") || "Test webhook notification from NoizyLab CLI";

  banner();
  info("Sending test webhook...\n");

  const payload = {
    content: `🔔 **NoizyLab Alert**\n${message}`,
    embeds: [{
      title: "CLI Test",
      description: message,
      color: 0x9B59B6,
      timestamp: new Date().toISOString()
    }]
  };

  log(`${C.dim}Payload:${C.reset}`);
  log(JSON.stringify(payload, null, 2));
  log("");
  warn("Set WEBHOOK_URL secret first: npx wrangler secret put WEBHOOK_URL");
}

function manageKV(args) {
  const action = args[0] || "list";
  const key = args[1];

  banner();

  if (action === "list") {
    info("Listing KV keys...\n");
    sh("npx wrangler kv:key list --namespace-id YOUR_MAIL_LOGS_KV_ID");
  } else if (action === "get" && key) {
    info(`Getting ${key}...\n`);
    sh(`npx wrangler kv:key get "${key}" --namespace-id YOUR_MAIL_LOGS_KV_ID`);
  } else if (action === "delete" && key) {
    warn(`Deleting ${key}...`);
    sh(`npx wrangler kv:key delete "${key}" --namespace-id YOUR_MAIL_LOGS_KV_ID`);
    success("Deleted!");
  } else {
    error("Usage: noizy kv [list|get|delete] <key>");
  }

  log("");
}

// ─── MAIN ────────────────────────────────────────────────────────────────────
const args = process.argv.slice(2);
const command = args[0];
const commandArgs = args.slice(1);

if (!command || command === "help" || command === "--help" || command === "-h") {
  commands.help.run();
} else if (commands[command]) {
  commands[command].run(commandArgs);
} else {
  error(`Unknown command: ${command}`);
  log(`\nRun ${C.cyan}noizy help${C.reset} for available commands.\n`);
}
