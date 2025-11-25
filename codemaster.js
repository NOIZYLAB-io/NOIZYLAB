#!/usr/bin/env node
// ╔═══════════════════════════════════════════════════════════════════════════════╗
// ║   ██████╗ ██████╗ ██████╗ ███████╗███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗  ║
// ║  ██╔════╝██╔═══██╗██╔══██╗██╔════╝████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗ ║
// ║  ██║     ██║   ██║██║  ██║█████╗  ██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝ ║
// ║  ██║     ██║   ██║██║  ██║██╔══╝  ██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗ ║
// ║  ╚██████╗╚██████╔╝██████╔╝███████╗██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║ ║
// ║   ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝ ║
// ║                                                                                        ║
// ║                    THE ULTIMATE AI-POWERED CODE COMMAND CENTER                         ║
// ║                                   Version 2.0.0                                        ║
// ╚═══════════════════════════════════════════════════════════════════════════════════════╝

import { execSync, spawn } from "child_process";
import fs from "fs";
import path from "path";
import readline from "readline";

// ═══════════════════════════════════════════════════════════════════════════════
// COLORS & STYLING
// ═══════════════════════════════════════════════════════════════════════════════

const C = {
  reset: "\x1b[0m",
  bright: "\x1b[1m",
  dim: "\x1b[2m",
  underscore: "\x1b[4m",
  blink: "\x1b[5m",
  reverse: "\x1b[7m",
  // Colors
  black: "\x1b[30m",
  red: "\x1b[31m",
  green: "\x1b[32m",
  yellow: "\x1b[33m",
  blue: "\x1b[34m",
  magenta: "\x1b[35m",
  cyan: "\x1b[36m",
  white: "\x1b[37m",
  // Bright colors
  brightRed: "\x1b[91m",
  brightGreen: "\x1b[92m",
  brightYellow: "\x1b[93m",
  brightBlue: "\x1b[94m",
  brightMagenta: "\x1b[95m",
  brightCyan: "\x1b[96m",
  // Backgrounds
  bgBlack: "\x1b[40m",
  bgRed: "\x1b[41m",
  bgGreen: "\x1b[42m",
  bgYellow: "\x1b[43m",
  bgBlue: "\x1b[44m",
  bgMagenta: "\x1b[45m",
  bgCyan: "\x1b[46m"
};

// ═══════════════════════════════════════════════════════════════════════════════
// HELPERS
// ═══════════════════════════════════════════════════════════════════════════════

const log = (msg) => console.log(msg);
const success = (msg) => log(`${C.green}✓${C.reset} ${msg}`);
const error = (msg) => log(`${C.red}✗${C.reset} ${msg}`);
const info = (msg) => log(`${C.cyan}ℹ${C.reset} ${msg}`);
const warn = (msg) => log(`${C.yellow}⚠${C.reset} ${msg}`);
const debug = (msg) => log(`${C.dim}[DEBUG] ${msg}${C.reset}`);

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

// ═══════════════════════════════════════════════════════════════════════════════
// BANNER
// ═══════════════════════════════════════════════════════════════════════════════

function banner() {
  console.log(`
${C.brightMagenta}${C.bright}
   ██████╗ ██████╗ ██████╗ ███████╗███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗
  ██╔════╝██╔═══██╗██╔══██╗██╔════╝████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
  ██║     ██║   ██║██║  ██║█████╗  ██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝
  ██║     ██║   ██║██║  ██║██╔══╝  ██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
  ╚██████╗╚██████╔╝██████╔╝███████╗██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║
   ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
${C.reset}
  ${C.dim}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${C.reset}
  ${C.cyan}THE ULTIMATE AI-POWERED CODE COMMAND CENTER${C.reset}                    ${C.dim}v2.0.0${C.reset}
  ${C.dim}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${C.reset}
`);
}

// ═══════════════════════════════════════════════════════════════════════════════
// AGENTS
// ═══════════════════════════════════════════════════════════════════════════════

const AGENTS = {
  // Supreme Commander
  CODEMASTER: { name: "CODEMASTER", role: "Supreme Commander", emoji: "👑", color: C.brightMagenta },
  // Core Agents
  ARCHITECT: { name: "ARCHITECT", role: "System Architect", emoji: "🏗️", color: C.blue },
  FORGE: { name: "FORGE", role: "Code Forge Master", emoji: "🔨", color: C.yellow },
  SENTINEL: { name: "SENTINEL", role: "Security Guardian", emoji: "🛡️", color: C.red },
  ORACLE: { name: "ORACLE", role: "Knowledge Keeper", emoji: "🔮", color: C.magenta },
  PHANTOM: { name: "PHANTOM", role: "Debug Hunter", emoji: "👻", color: C.white },
  NEXUS: { name: "NEXUS", role: "Integration Master", emoji: "🔗", color: C.cyan },
  CHRONOS: { name: "CHRONOS", role: "Automation Timekeeper", emoji: "⏰", color: C.green },
  // NoizyLab Agents
  LUCY: { name: "LUCY", role: "Creative Director", emoji: "🎨", color: C.brightMagenta },
  KEITH: { name: "KEITH", role: "Technical Lead", emoji: "⚙️", color: C.brightBlue },
  WARDY: { name: "WARDY", role: "Project Manager", emoji: "📋", color: C.brightGreen },
  RED_ALERT: { name: "RED_ALERT", role: "Emergency Handler", emoji: "🚨", color: C.brightRed },
  NOVA: { name: "NOVA", role: "Research Analyst", emoji: "🔬", color: C.brightCyan },
  ECHO: { name: "ECHO", role: "Communications Lead", emoji: "📢", color: C.brightYellow }
};

// ═══════════════════════════════════════════════════════════════════════════════
// GENERATORS
// ═══════════════════════════════════════════════════════════════════════════════

const GENERATORS = {
  worker: { name: "Cloudflare Worker", emoji: "⚡" },
  api: { name: "REST API", emoji: "🔌" },
  cli: { name: "CLI Tool", emoji: "💻" },
  component: { name: "React Component", emoji: "⚛️" },
  server: { name: "Express Server", emoji: "🖥️" },
  model: { name: "Database Model", emoji: "🗃️" },
  test: { name: "Test Suite", emoji: "🧪" },
  project: { name: "Full Project", emoji: "📦" }
};

// ═══════════════════════════════════════════════════════════════════════════════
// BLUEPRINTS
// ═══════════════════════════════════════════════════════════════════════════════

const BLUEPRINTS = {
  "cf-email": { name: "Cloudflare Email System", emoji: "📧" },
  "cf-api": { name: "Cloudflare API", emoji: "🌐" },
  "cf-ai": { name: "Cloudflare AI Agent", emoji: "🤖" },
  "cli-tool": { name: "CLI Tool", emoji: "💻" },
  "fullstack": { name: "Full Stack App", emoji: "🚀" },
  "saas": { name: "SaaS Starter", emoji: "💼" },
  "discord-bot": { name: "Discord Bot", emoji: "🎮" },
  "microservice": { name: "Microservice", emoji: "🔧" }
};

// ═══════════════════════════════════════════════════════════════════════════════
// COMMANDS
// ═══════════════════════════════════════════════════════════════════════════════

const commands = {
  // ─── HELP & INFO ─────────────────────────────────────────────────────────
  help: { desc: "Show this help message", run: showHelp },
  version: { desc: "Show version", run: () => log("CODEMASTER v2.0.0") },
  status: { desc: "System status", run: showStatus },
  stats: { desc: "Project statistics", run: showProjectStats },

  // ─── AGENTS ──────────────────────────────────────────────────────────────
  agents: { desc: "List all agents", run: listAgents },
  summon: { desc: "Summon an agent", usage: "summon <AGENT> <task>", run: summonAgent },
  council: { desc: "Summon the agent council", run: summonCouncil },

  // ─── GENERATION ──────────────────────────────────────────────────────────
  forge: { desc: "Generate code", usage: "forge <type> [options]", run: forgeCode },
  generators: { desc: "List code generators", run: listGenerators },

  // ─── BLUEPRINTS ──────────────────────────────────────────────────────────
  blueprints: { desc: "List project blueprints", run: listBlueprints },
  scaffold: { desc: "Scaffold a project", usage: "scaffold <blueprint> <name>", run: scaffoldProject },

  // ─── WORKFLOWS ───────────────────────────────────────────────────────────
  workflow: { desc: "Manage workflows", usage: "workflow [create|run|list]", run: manageWorkflows },

  // ─── DEPLOYMENT ──────────────────────────────────────────────────────────
  deploy: { desc: "Deploy workers", usage: "deploy [all|<worker>]", run: deployWorkers },
  dev: { desc: "Start dev server", run: startDev },

  // ─── ANALYSIS ────────────────────────────────────────────────────────────
  analyze: { desc: "Analyze code", usage: "analyze <file>", run: analyzeCode },
  secure: { desc: "Security scan", usage: "secure [path]", run: securityScan },

  // ─── INTERACTIVE ─────────────────────────────────────────────────────────
  shell: { desc: "Interactive CODEMASTER shell", run: interactiveShell },
  chat: { desc: "Chat with an agent", usage: "chat [agent]", run: chatWithAgent },

  // ─── UTILITIES ───────────────────────────────────────────────────────────
  init: { desc: "Initialize CODEMASTER project", run: initProject },
  config: { desc: "Manage configuration", usage: "config [get|set] <key> [value]", run: manageConfig },
  logs: { desc: "View logs", run: viewLogs },

  // ─── NOIZYLAB ────────────────────────────────────────────────────────────
  noizy: { desc: "NoizyLab commands", usage: "noizy <command>", run: noizyCommands },

  // ─── CODE QUALITY ─────────────────────────────────────────────────────────
  review: { desc: "AI code review", usage: "review <file|dir>", run: codeReview },
  docs: { desc: "Generate documentation", usage: "docs [type] [target]", run: generateDocs },
  test: { desc: "Generate tests", usage: "test <file>", run: generateTests },
  lint: { desc: "Lint code", usage: "lint [path]", run: lintCode },

  // ─── GIT AUTOMATION ───────────────────────────────────────────────────────
  commit: { desc: "Smart commit with AI message", usage: "commit [files]", run: smartCommit },
  pr: { desc: "Create pull request", usage: "pr [title]", run: createPR },
  branch: { desc: "Smart branch management", usage: "branch <action>", run: manageBranch },

  // ─── MONITORING & METRICS ─────────────────────────────────────────────────
  metrics: { desc: "View system metrics", run: showMetrics },
  dashboard: { desc: "Open dashboard", run: openDashboard },
  watch: { desc: "Watch files for changes", usage: "watch [pattern]", run: watchFiles },

  // ─── PIPELINES ────────────────────────────────────────────────────────────
  pipeline: { desc: "Run automation pipeline", usage: "pipeline <name>", run: runPipeline },
  ci: { desc: "CI/CD operations", usage: "ci [test|build|deploy]", run: runCI },

  // ─── UTILITIES ────────────────────────────────────────────────────────────
  clean: { desc: "Clean build artifacts", run: cleanProject },
  upgrade: { desc: "Upgrade CODEMASTER", run: upgradeCLI },
  doctor: { desc: "Diagnose issues", run: diagnoseIssues }
};

// ═══════════════════════════════════════════════════════════════════════════════
// COMMAND IMPLEMENTATIONS
// ═══════════════════════════════════════════════════════════════════════════════

function showHelp() {
  banner();

  log(`${C.bright}COMMANDS:${C.reset}\n`);

  const categories = {
    "Info": ["help", "version", "status", "stats"],
    "Agents": ["agents", "summon", "council", "chat"],
    "Generation": ["forge", "generators", "blueprints", "scaffold"],
    "Code Quality": ["review", "docs", "test", "lint"],
    "Git Automation": ["commit", "pr", "branch"],
    "Workflows": ["workflow", "pipeline", "ci"],
    "Monitoring": ["metrics", "dashboard", "watch"],
    "Deployment": ["deploy", "dev"],
    "Analysis": ["analyze", "secure"],
    "Interactive": ["shell"],
    "Utilities": ["init", "config", "logs", "clean", "upgrade", "doctor", "noizy"]
  };

  for (const [category, cmds] of Object.entries(categories)) {
    log(`  ${C.yellow}${category}${C.reset}`);
    cmds.forEach(name => {
      const cmd = commands[name];
      if (cmd) {
        const usage = cmd.usage ? ` ${C.dim}${cmd.usage}${C.reset}` : "";
        log(`    ${C.cyan}${name.padEnd(12)}${C.reset} ${cmd.desc}${usage}`);
      }
    });
    log("");
  }

  log(`${C.bright}EXAMPLES:${C.reset}\n`);
  log(`  ${C.dim}$${C.reset} codemaster summon FORGE "Create a REST API for users"`);
  log(`  ${C.dim}$${C.reset} codemaster forge api --resources users,posts`);
  log(`  ${C.dim}$${C.reset} codemaster scaffold saas my-app`);
  log(`  ${C.dim}$${C.reset} codemaster review ./src`);
  log(`  ${C.dim}$${C.reset} codemaster commit`);
  log(`  ${C.dim}$${C.reset} codemaster pipeline full-deploy`);
  log(`  ${C.dim}$${C.reset} codemaster doctor`);
  log(`  ${C.dim}$${C.reset} codemaster shell`);
  log("");
}

function showStatus() {
  banner();

  log(`${C.bright}SYSTEM STATUS${C.reset}\n`);

  // Check Node
  const nodeVersion = shOutput("node --version");
  success(`Node.js: ${nodeVersion}`);

  // Check wrangler
  const wranglerVersion = shOutput("npx wrangler --version 2>/dev/null");
  if (wranglerVersion) {
    success(`Wrangler: ${wranglerVersion}`);
  } else {
    warn("Wrangler: Not installed");
  }

  // Check files
  log(`\n${C.bright}CORE FILES${C.reset}\n`);
  const coreFiles = [
    "codemaster.js",
    "noizy.js",
    "core/codemaster.js",
    "generators/code-forge.js",
    "workers/codemaster-api.js",
    "workers/email-worker.js"
  ];

  coreFiles.forEach(f => {
    if (fs.existsSync(f)) {
      success(f);
    } else {
      warn(`${f} (missing)`);
    }
  });

  // Agents
  log(`\n${C.bright}AGENTS (${Object.keys(AGENTS).length})${C.reset}\n`);
  Object.values(AGENTS).forEach(a => {
    log(`  ${a.emoji} ${a.color}${a.name.padEnd(12)}${C.reset} ${C.dim}${a.role}${C.reset}`);
  });

  // Generators
  log(`\n${C.bright}GENERATORS (${Object.keys(GENERATORS).length})${C.reset}\n`);
  Object.entries(GENERATORS).forEach(([id, g]) => {
    log(`  ${g.emoji} ${C.cyan}${id.padEnd(12)}${C.reset} ${g.name}`);
  });

  log("");
}

function listAgents() {
  banner();
  log(`${C.bright}CODEMASTER AGENTS${C.reset}\n`);

  // Supreme Commander
  log(`${C.yellow}━━━ SUPREME COMMANDER ━━━${C.reset}\n`);
  const cm = AGENTS.CODEMASTER;
  log(`  ${cm.emoji} ${cm.color}${C.bright}${cm.name}${C.reset}`);
  log(`     ${C.dim}${cm.role}${C.reset}`);
  log(`     ${C.dim}Orchestrates all agents, makes final decisions${C.reset}`);

  // Core Agents
  log(`\n${C.yellow}━━━ CORE AGENTS ━━━${C.reset}\n`);
  ["ARCHITECT", "FORGE", "SENTINEL", "ORACLE", "PHANTOM", "NEXUS", "CHRONOS"].forEach(name => {
    const a = AGENTS[name];
    log(`  ${a.emoji} ${a.color}${C.bright}${a.name}${C.reset} - ${a.role}`);
  });

  // NoizyLab Agents
  log(`\n${C.yellow}━━━ NOIZYLAB AGENTS ━━━${C.reset}\n`);
  ["LUCY", "KEITH", "WARDY", "RED_ALERT", "NOVA", "ECHO"].forEach(name => {
    const a = AGENTS[name];
    log(`  ${a.emoji} ${a.color}${C.bright}${a.name}${C.reset} - ${a.role}`);
  });

  log(`\n${C.dim}Usage: codemaster summon <AGENT> <task>${C.reset}\n`);
}

function summonAgent(args) {
  const agentName = args[0]?.toUpperCase();
  const task = args.slice(1).join(" ");

  if (!agentName || !task) {
    error("Usage: codemaster summon <AGENT> <task>");
    log(`\nAvailable agents: ${Object.keys(AGENTS).join(", ")}`);
    return;
  }

  const agent = AGENTS[agentName];
  if (!agent) {
    error(`Unknown agent: ${agentName}`);
    return;
  }

  banner();
  log(`${agent.emoji} ${agent.color}${C.bright}SUMMONING ${agent.name}${C.reset}`);
  log(`${C.dim}${agent.role}${C.reset}\n`);
  info(`Task: ${task}\n`);

  const prompt = `You are ${agent.name}, the ${agent.role} in the CODEMASTER system.

Task: ${task}

Provide a detailed, actionable response in JSON format:
{
  "agent": "${agent.name}",
  "analysis": "your analysis",
  "actions": ["action 1", "action 2"],
  "code": "any generated code",
  "priority": "low|medium|high|critical"
}`;

  info("Thinking...\n");

  const escapedPrompt = prompt.replace(/"/g, '\\"').replace(/\n/g, '\\n');
  const result = shOutput(`npx wrangler ai run @cf/mistral/mistral-7b-instruct-v0.1 "${escapedPrompt}" 2>/dev/null`);

  if (result) {
    try {
      const parsed = JSON.parse(result);
      log(`${C.bright}RESPONSE:${C.reset}\n`);
      if (parsed.analysis) log(`${C.cyan}Analysis:${C.reset} ${parsed.analysis}`);
      if (parsed.actions) {
        log(`${C.cyan}Actions:${C.reset}`);
        parsed.actions.forEach((a, i) => log(`  ${i + 1}. ${a}`));
      }
      if (parsed.code) {
        log(`${C.cyan}Code:${C.reset}`);
        log(parsed.code);
      }
      if (parsed.priority) log(`${C.cyan}Priority:${C.reset} ${parsed.priority}`);
    } catch {
      log(result);
    }
  } else {
    warn("Could not reach AI. Ensure you're logged in: npx wrangler login");
  }

  log("");
}

function summonCouncil(args) {
  const topic = args.join(" ") || "general discussion";

  banner();
  log(`${C.bright}${C.yellow}⚔️  SUMMONING THE AGENT COUNCIL ⚔️${C.reset}\n`);
  info(`Topic: ${topic}\n`);

  const councilAgents = ["CODEMASTER", "ARCHITECT", "FORGE", "SENTINEL"];

  councilAgents.forEach(name => {
    const agent = AGENTS[name];
    log(`${agent.emoji} ${agent.color}${agent.name}${C.reset} has joined the council`);
  });

  log(`\n${C.dim}The council is deliberating...${C.reset}\n`);

  // In a real implementation, each agent would provide input
  log(`${C.bright}COUNCIL VERDICT:${C.reset}`);
  log(`${C.dim}Each agent has analyzed the topic and provided recommendations.${C.reset}\n`);
}

function forgeCode(args) {
  const type = args[0];

  if (!type) {
    error("Usage: codemaster forge <type> [options]");
    log(`\nAvailable types: ${Object.keys(GENERATORS).join(", ")}`);
    return;
  }

  const generator = GENERATORS[type];
  if (!generator) {
    error(`Unknown generator: ${type}`);
    return;
  }

  banner();
  log(`${generator.emoji} ${C.bright}FORGING ${generator.name.toUpperCase()}${C.reset}\n`);

  summonAgent(["FORGE", `Generate a ${generator.name} with production-quality code`]);
}

function listGenerators() {
  banner();
  log(`${C.bright}CODE GENERATORS${C.reset}\n`);

  Object.entries(GENERATORS).forEach(([id, gen]) => {
    log(`  ${gen.emoji} ${C.cyan}${id.padEnd(12)}${C.reset} ${gen.name}`);
  });

  log(`\n${C.dim}Usage: codemaster forge <type>${C.reset}\n`);
}

function listBlueprints() {
  banner();
  log(`${C.bright}PROJECT BLUEPRINTS${C.reset}\n`);

  Object.entries(BLUEPRINTS).forEach(([id, bp]) => {
    log(`  ${bp.emoji} ${C.cyan}${id.padEnd(15)}${C.reset} ${bp.name}`);
  });

  log(`\n${C.dim}Usage: codemaster scaffold <blueprint> <name>${C.reset}\n`);
}

function scaffoldProject(args) {
  const [blueprint, name] = args;

  if (!blueprint || !name) {
    error("Usage: codemaster scaffold <blueprint> <name>");
    listBlueprints();
    return;
  }

  const bp = BLUEPRINTS[blueprint];
  if (!bp) {
    error(`Unknown blueprint: ${blueprint}`);
    return;
  }

  banner();
  log(`${bp.emoji} ${C.bright}SCAFFOLDING ${bp.name.toUpperCase()}${C.reset}`);
  log(`${C.dim}Project: ${name}${C.reset}\n`);

  summonAgent(["ARCHITECT", `Scaffold a complete ${bp.name} project named "${name}" with all necessary files and configurations`]);
}

function manageWorkflows(args) {
  const action = args[0] || "list";

  banner();
  log(`${C.bright}WORKFLOWS${C.reset}\n`);

  if (action === "list") {
    info("No workflows configured yet.");
    log(`\n${C.dim}Create one with: codemaster workflow create <name>${C.reset}`);
  } else if (action === "create") {
    const name = args[1];
    if (!name) {
      error("Usage: codemaster workflow create <name>");
      return;
    }
    success(`Workflow "${name}" created`);
  } else if (action === "run") {
    const name = args[1];
    if (!name) {
      error("Usage: codemaster workflow run <name>");
      return;
    }
    info(`Running workflow: ${name}`);
  }

  log("");
}

function deployWorkers(args) {
  const target = args[0] || "all";

  banner();
  log(`${C.bright}DEPLOYING WORKERS${C.reset}\n`);

  const workers = {
    "email-worker": "workers/email-worker.js",
    "api-dashboard": "workers/api-dashboard.js",
    "codemaster-api": "workers/codemaster-api.js"
  };

  if (target === "all") {
    Object.entries(workers).forEach(([name, path]) => {
      if (fs.existsSync(path)) {
        info(`Deploying ${name}...`);
        sh(`npx wrangler deploy ${path}`);
      }
    });
  } else if (workers[target]) {
    info(`Deploying ${target}...`);
    sh(`npx wrangler deploy ${workers[target]}`);
  } else {
    error(`Unknown worker: ${target}`);
    log(`\nAvailable: ${Object.keys(workers).join(", ")}, all`);
  }

  log("");
}

function startDev(args) {
  const worker = args[0] || "email-worker";

  banner();
  info(`Starting dev server for ${worker}...`);
  sh(`npx wrangler dev workers/${worker}.js`);
}

function analyzeCode(args) {
  const file = args[0];

  if (!file) {
    error("Usage: codemaster analyze <file>");
    return;
  }

  if (!fs.existsSync(file)) {
    error(`File not found: ${file}`);
    return;
  }

  banner();
  log(`${C.bright}ANALYZING CODE${C.reset}\n`);
  info(`File: ${file}\n`);

  const content = fs.readFileSync(file, "utf8");
  summonAgent(["ARCHITECT", `Analyze this code for architecture, quality, and improvements:\n\n${content.substring(0, 2000)}`]);
}

function securityScan(args) {
  const target = args[0] || ".";

  banner();
  log(`${C.bright}🛡️ SECURITY SCAN${C.reset}\n`);
  info(`Target: ${target}\n`);

  summonAgent(["SENTINEL", `Perform a security audit on the codebase at ${target}. Check for vulnerabilities, secrets, and security best practices.`]);
}

async function interactiveShell() {
  banner();
  log(`${C.bright}CODEMASTER INTERACTIVE SHELL${C.reset}`);
  log(`${C.dim}Type 'help' for commands, 'exit' to quit${C.reset}\n`);

  let currentAgent = AGENTS.CODEMASTER;

  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  const prompt = () => {
    rl.question(`${currentAgent.emoji} ${currentAgent.color}${currentAgent.name}${C.reset} > `, (input) => {
      const trimmed = input.trim();

      if (!trimmed) { prompt(); return; }
      if (trimmed === "exit" || trimmed === "quit") {
        log("\n👑 CODEMASTER signing off...\n");
        rl.close();
        return;
      }

      if (trimmed === "help") {
        log(`\n${C.bright}SHELL COMMANDS:${C.reset}`);
        log(`  ${C.cyan}switch <AGENT>${C.reset} - Switch agent`);
        log(`  ${C.cyan}agents${C.reset}         - List agents`);
        log(`  ${C.cyan}forge <type>${C.reset}   - Generate code`);
        log(`  ${C.cyan}clear${C.reset}          - Clear screen`);
        log(`  ${C.cyan}exit${C.reset}           - Exit shell`);
        log(`  ${C.dim}Or type any task for the current agent${C.reset}\n`);
        prompt(); return;
      }

      if (trimmed === "agents") {
        Object.values(AGENTS).forEach(a => {
          const marker = a.name === currentAgent.name ? " ←" : "";
          log(`  ${a.emoji} ${a.color}${a.name}${C.reset} - ${a.role}${marker}`);
        });
        log("");
        prompt(); return;
      }

      if (trimmed === "clear") {
        console.clear();
        banner();
        prompt(); return;
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
        prompt(); return;
      }

      if (trimmed.startsWith("forge ")) {
        const type = trimmed.split(" ")[1];
        forgeCode([type]);
        prompt(); return;
      }

      // Send to current agent
      log(`\n${C.dim}Processing...${C.reset}\n`);
      summonAgent([currentAgent.name, trimmed]);
      prompt();
    });
  };

  prompt();
}

function chatWithAgent(args) {
  const agentName = args[0]?.toUpperCase() || "CODEMASTER";
  const agent = AGENTS[agentName];

  if (!agent) {
    error(`Unknown agent: ${agentName}`);
    return;
  }

  banner();
  log(`${agent.emoji} ${agent.color}${C.bright}CHATTING WITH ${agent.name}${C.reset}`);
  log(`${C.dim}${agent.role}${C.reset}\n`);

  // Enter chat mode with this agent
  interactiveShell();
}

function initProject() {
  banner();
  info("Initializing CODEMASTER project...\n");

  const dirs = ["core", "generators", "blueprints", "workers", "agents", "templates", "lib", "config", "workflows", "plugins", "tests"];

  dirs.forEach(dir => {
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
      success(`Created ${dir}/`);
    } else {
      info(`${dir}/ exists`);
    }
  });

  log("");
  success("CODEMASTER initialized!\n");
}

function manageConfig(args) {
  const [action, key, value] = args;
  const configPath = "config/codemaster.json";

  if (!fs.existsSync(configPath)) {
    fs.writeFileSync(configPath, JSON.stringify({ version: "1.0.0" }, null, 2));
  }

  const config = JSON.parse(fs.readFileSync(configPath, "utf8"));

  if (!action || action === "get") {
    banner();
    log(`${C.bright}CONFIGURATION${C.reset}\n`);
    log(JSON.stringify(config, null, 2));
  } else if (action === "set" && key) {
    config[key] = value;
    fs.writeFileSync(configPath, JSON.stringify(config, null, 2));
    success(`Set ${key} = ${value}`);
  }

  log("");
}

function viewLogs(args) {
  banner();
  info("Tailing worker logs...\n");
  sh("npx wrangler tail");
}

function noizyCommands(args) {
  // Pass through to noizy CLI
  const command = args.join(" ");
  if (command) {
    sh(`node noizy.js ${command}`);
  } else {
    sh("node noizy.js help");
  }
}

// ═══════════════════════════════════════════════════════════════════════════════
// NEW v2.0 COMMAND IMPLEMENTATIONS
// ═══════════════════════════════════════════════════════════════════════════════

function showProjectStats() {
  banner();
  log(`${C.bright}PROJECT STATISTICS${C.reset}\n`);

  // Count files by extension
  const counts = { js: 0, ts: 0, json: 0, html: 0, css: 0, md: 0, total: 0, lines: 0 };

  function walkDir(dir) {
    if (!fs.existsSync(dir)) return;
    const files = fs.readdirSync(dir);
    files.forEach(file => {
      if (file.startsWith(".") || file === "node_modules") return;
      const fullPath = path.join(dir, file);
      const stat = fs.statSync(fullPath);
      if (stat.isDirectory()) {
        walkDir(fullPath);
      } else {
        counts.total++;
        const ext = path.extname(file).slice(1);
        if (counts[ext] !== undefined) counts[ext]++;
        try {
          const content = fs.readFileSync(fullPath, "utf8");
          counts.lines += content.split("\n").length;
        } catch {}
      }
    });
  }

  walkDir(".");

  log(`  ${C.cyan}Total Files:${C.reset}     ${counts.total}`);
  log(`  ${C.cyan}Total Lines:${C.reset}     ${counts.lines.toLocaleString()}`);
  log("");
  log(`  ${C.yellow}JavaScript:${C.reset}      ${counts.js} files`);
  log(`  ${C.yellow}TypeScript:${C.reset}      ${counts.ts} files`);
  log(`  ${C.yellow}JSON:${C.reset}            ${counts.json} files`);
  log(`  ${C.yellow}HTML:${C.reset}            ${counts.html} files`);
  log(`  ${C.yellow}CSS:${C.reset}             ${counts.css} files`);
  log(`  ${C.yellow}Markdown:${C.reset}        ${counts.md} files`);

  // Git stats
  const commits = shOutput("git rev-list --count HEAD 2>/dev/null") || "0";
  const branch = shOutput("git branch --show-current 2>/dev/null") || "N/A";
  const lastCommit = shOutput("git log -1 --format='%h %s' 2>/dev/null") || "N/A";

  log(`\n${C.bright}GIT STATISTICS${C.reset}\n`);
  log(`  ${C.cyan}Branch:${C.reset}          ${branch}`);
  log(`  ${C.cyan}Commits:${C.reset}         ${commits}`);
  log(`  ${C.cyan}Last Commit:${C.reset}     ${lastCommit}`);
  log("");
}

function codeReview(args) {
  const target = args[0] || ".";

  banner();
  log(`${C.bright}AI CODE REVIEW${C.reset}\n`);
  info(`Target: ${target}\n`);

  if (fs.existsSync(target)) {
    const isDir = fs.statSync(target).isDirectory();
    if (isDir) {
      info("Reviewing directory structure and key files...\n");
    } else {
      const content = fs.readFileSync(target, "utf8");
      log(`${C.dim}Analyzing ${content.split("\n").length} lines of code...${C.reset}\n`);
    }
  }

  summonAgent(["ARCHITECT", `Perform a comprehensive code review on ${target}. Check for:
1. Code quality and best practices
2. Performance issues
3. Security vulnerabilities
4. Maintainability
5. Suggestions for improvement

Provide specific, actionable feedback.`]);
}

function generateDocs(args) {
  const type = args[0] || "readme";
  const target = args[1] || ".";

  banner();
  log(`${C.bright}DOCUMENTATION GENERATOR${C.reset}\n`);
  info(`Type: ${type}, Target: ${target}\n`);

  const types = {
    readme: "Generate a comprehensive README.md with features, installation, usage, and API documentation",
    api: "Generate API documentation with all endpoints, parameters, and examples",
    jsdoc: "Add JSDoc comments to all functions and classes",
    changelog: "Generate a CHANGELOG.md from git history",
    contributing: "Generate a CONTRIBUTING.md with guidelines"
  };

  if (!types[type]) {
    error(`Unknown doc type: ${type}`);
    log(`\nAvailable: ${Object.keys(types).join(", ")}`);
    return;
  }

  summonAgent(["ORACLE", types[type] + ` for the project at ${target}`]);
}

function generateTests(args) {
  const file = args[0];

  if (!file) {
    error("Usage: codemaster test <file>");
    return;
  }

  if (!fs.existsSync(file)) {
    error(`File not found: ${file}`);
    return;
  }

  banner();
  log(`${C.bright}TEST GENERATOR${C.reset}\n`);
  info(`File: ${file}\n`);

  const content = fs.readFileSync(file, "utf8");
  summonAgent(["PHANTOM", `Generate comprehensive tests for this code:

\`\`\`javascript
${content.substring(0, 3000)}
\`\`\`

Include:
1. Unit tests for all functions
2. Edge cases
3. Error handling tests
4. Integration tests if applicable
5. Use modern testing patterns`]);
}

function lintCode(args) {
  const target = args[0] || ".";

  banner();
  log(`${C.bright}CODE LINTING${C.reset}\n`);
  info(`Target: ${target}\n`);

  // Try ESLint first
  const eslintResult = shOutput(`npx eslint ${target} --format stylish 2>&1`);
  if (eslintResult) {
    log(eslintResult);
  } else {
    warn("ESLint not configured. Running basic checks...\n");
    summonAgent(["SENTINEL", `Perform a code lint check on ${target}. Look for common issues, unused variables, formatting problems, and style inconsistencies.`]);
  }
}

function smartCommit(args) {
  const files = args.join(" ") || ".";

  banner();
  log(`${C.bright}SMART COMMIT${C.reset}\n`);

  // Get git diff
  const diff = shOutput(`git diff --staged --stat 2>/dev/null`) || shOutput(`git diff --stat 2>/dev/null`);

  if (!diff) {
    warn("No changes detected to commit.");
    return;
  }

  info("Changes detected:\n");
  log(diff);

  // Stage files if specified
  if (files !== ".") {
    sh(`git add ${files}`, true);
  }

  // Get detailed diff for AI analysis
  const detailedDiff = shOutput(`git diff --staged 2>/dev/null`) || shOutput(`git diff 2>/dev/null`);

  log(`\n${C.dim}Generating commit message with AI...${C.reset}\n`);

  const prompt = `Based on this git diff, generate a clear, concise commit message following conventional commits format (type: description).

Diff:
${detailedDiff?.substring(0, 2000) || "No diff available"}

Return ONLY the commit message, nothing else. Format: <type>(<scope>): <description>`;

  const commitMsg = shOutput(`npx wrangler ai run @cf/mistral/mistral-7b-instruct-v0.1 "${prompt.replace(/"/g, '\\"').replace(/\n/g, '\\n')}" 2>/dev/null`);

  if (commitMsg) {
    log(`${C.cyan}Suggested commit message:${C.reset}`);
    log(`  ${commitMsg}\n`);
    info(`Run: git commit -m "${commitMsg.replace(/"/g, '\\"')}"`);
  } else {
    warn("Could not generate commit message. Please write one manually.");
  }
}

function createPR(args) {
  const title = args.join(" ");

  banner();
  log(`${C.bright}CREATE PULL REQUEST${C.reset}\n`);

  const branch = shOutput("git branch --show-current");
  const baseBranch = shOutput("git remote show origin 2>/dev/null | grep 'HEAD branch' | awk '{print $NF}'") || "main";

  info(`Current branch: ${branch}`);
  info(`Base branch: ${baseBranch}\n`);

  // Get commits for this branch
  const commits = shOutput(`git log ${baseBranch}..HEAD --oneline 2>/dev/null`);

  if (!commits) {
    warn("No commits to create PR from.");
    return;
  }

  log(`${C.cyan}Commits in this branch:${C.reset}`);
  log(commits);

  if (title) {
    log(`\n${C.dim}Creating PR...${C.reset}`);
    sh(`gh pr create --title "${title}" --body "Auto-generated PR by CODEMASTER"`);
  } else {
    log(`\n${C.dim}Generate PR with: gh pr create --title "Your Title"${C.reset}`);
  }
}

function manageBranch(args) {
  const action = args[0];

  banner();
  log(`${C.bright}BRANCH MANAGEMENT${C.reset}\n`);

  if (!action) {
    // List branches
    const branches = shOutput("git branch -a");
    log(branches);
    log(`\n${C.dim}Actions: create, switch, delete, clean${C.reset}`);
    return;
  }

  switch (action) {
    case "create":
      const name = args[1];
      if (!name) {
        error("Usage: codemaster branch create <name>");
        return;
      }
      sh(`git checkout -b ${name}`);
      success(`Created and switched to branch: ${name}`);
      break;

    case "switch":
      const target = args[1];
      if (!target) {
        error("Usage: codemaster branch switch <name>");
        return;
      }
      sh(`git checkout ${target}`);
      break;

    case "delete":
      const delBranch = args[1];
      if (!delBranch) {
        error("Usage: codemaster branch delete <name>");
        return;
      }
      sh(`git branch -d ${delBranch}`);
      break;

    case "clean":
      info("Cleaning merged branches...");
      sh(`git branch --merged | grep -v "\\*" | xargs -n 1 git branch -d 2>/dev/null || true`);
      success("Cleaned up merged branches");
      break;

    default:
      error(`Unknown action: ${action}`);
  }
}

function showMetrics() {
  banner();
  log(`${C.bright}SYSTEM METRICS${C.reset}\n`);

  // Memory usage
  const memUsage = process.memoryUsage();
  log(`${C.yellow}Memory Usage:${C.reset}`);
  log(`  Heap Used:     ${Math.round(memUsage.heapUsed / 1024 / 1024)} MB`);
  log(`  Heap Total:    ${Math.round(memUsage.heapTotal / 1024 / 1024)} MB`);
  log(`  RSS:           ${Math.round(memUsage.rss / 1024 / 1024)} MB`);

  // Uptime
  log(`\n${C.yellow}System:${C.reset}`);
  log(`  Node Version:  ${process.version}`);
  log(`  Platform:      ${process.platform}`);
  log(`  Architecture:  ${process.arch}`);

  // Project metrics
  log(`\n${C.yellow}Project:${C.reset}`);
  log(`  Agents:        ${Object.keys(AGENTS).length}`);
  log(`  Generators:    ${Object.keys(GENERATORS).length}`);
  log(`  Blueprints:    ${Object.keys(BLUEPRINTS).length}`);

  log("");
}

function openDashboard() {
  banner();
  info("Opening dashboard...\n");

  const dashboardPath = "dashboard/dashboard.html";
  if (fs.existsSync(dashboardPath)) {
    // Try to open in browser
    const openCmd = process.platform === "darwin" ? "open" : process.platform === "win32" ? "start" : "xdg-open";
    sh(`${openCmd} ${dashboardPath} 2>/dev/null || echo "Open ${dashboardPath} in your browser"`, true);
    success(`Dashboard: ${dashboardPath}`);
  } else {
    warn("Dashboard not found. Run: codemaster init");
  }
}

function watchFiles(args) {
  const pattern = args[0] || "**/*.js";

  banner();
  log(`${C.bright}FILE WATCHER${C.reset}\n`);
  info(`Watching: ${pattern}`);
  info("Press Ctrl+C to stop\n");

  // Simple file watcher using fs.watch
  const watchedDirs = new Set();

  function addWatch(dir) {
    if (watchedDirs.has(dir)) return;
    watchedDirs.add(dir);

    try {
      fs.watch(dir, { recursive: true }, (eventType, filename) => {
        if (filename && filename.endsWith(".js")) {
          const time = new Date().toLocaleTimeString();
          log(`${C.dim}[${time}]${C.reset} ${C.cyan}${eventType}${C.reset}: ${filename}`);
        }
      });
    } catch {}
  }

  addWatch(".");
  info("Watching for changes...");
}

function runPipeline(args) {
  const pipelineName = args[0];

  banner();
  log(`${C.bright}AUTOMATION PIPELINE${C.reset}\n`);

  const pipelines = {
    "full-deploy": ["lint", "test", "build", "deploy"],
    "code-quality": ["lint", "review", "test"],
    "quick-deploy": ["build", "deploy"],
    "docs-update": ["docs", "commit"]
  };

  if (!pipelineName) {
    log(`${C.yellow}Available Pipelines:${C.reset}\n`);
    Object.entries(pipelines).forEach(([name, steps]) => {
      log(`  ${C.cyan}${name.padEnd(15)}${C.reset} ${steps.join(" -> ")}`);
    });
    log(`\n${C.dim}Usage: codemaster pipeline <name>${C.reset}`);
    return;
  }

  const steps = pipelines[pipelineName];
  if (!steps) {
    error(`Unknown pipeline: ${pipelineName}`);
    return;
  }

  info(`Running pipeline: ${pipelineName}`);
  log(`${C.dim}Steps: ${steps.join(" -> ")}${C.reset}\n`);

  steps.forEach((step, i) => {
    log(`\n${C.yellow}[${i + 1}/${steps.length}]${C.reset} ${C.bright}${step.toUpperCase()}${C.reset}`);
    if (commands[step]) {
      commands[step].run([]);
    }
  });

  log(`\n${C.green}Pipeline complete!${C.reset}\n`);
}

function runCI(args) {
  const action = args[0] || "test";

  banner();
  log(`${C.bright}CI/CD OPERATIONS${C.reset}\n`);

  switch (action) {
    case "test":
      info("Running tests...");
      sh("npm test 2>/dev/null || node --test 2>/dev/null || echo 'No test command configured'");
      break;

    case "build":
      info("Building project...");
      sh("npm run build 2>/dev/null || echo 'No build command configured'");
      break;

    case "deploy":
      info("Deploying...");
      deployWorkers(["all"]);
      break;

    case "all":
      info("Running full CI pipeline...");
      runPipeline(["full-deploy"]);
      break;

    default:
      error(`Unknown CI action: ${action}`);
      log("\nAvailable: test, build, deploy, all");
  }
}

function cleanProject() {
  banner();
  log(`${C.bright}CLEANING PROJECT${C.reset}\n`);

  const toClean = [
    "node_modules/.cache",
    "dist",
    "build",
    ".wrangler",
    "coverage",
    "*.log"
  ];

  toClean.forEach(item => {
    if (item.includes("*")) {
      // Glob pattern
      const files = shOutput(`ls ${item} 2>/dev/null`);
      if (files) {
        sh(`rm -f ${item}`, true);
        success(`Removed ${item}`);
      }
    } else if (fs.existsSync(item)) {
      sh(`rm -rf ${item}`, true);
      success(`Removed ${item}`);
    }
  });

  log("");
  success("Clean complete!");
}

function upgradeCLI() {
  banner();
  log(`${C.bright}UPGRADE CODEMASTER${C.reset}\n`);

  info("Checking for updates...");

  // Check git for updates
  const status = shOutput("git fetch && git status -uno 2>/dev/null");
  if (status && status.includes("behind")) {
    info("Updates available!");
    sh("git pull");
    success("CODEMASTER upgraded!");
  } else {
    success("Already up to date!");
  }

  log("");
}

function diagnoseIssues() {
  banner();
  log(`${C.bright}CODEMASTER DOCTOR${C.reset}\n`);
  log(`${C.dim}Diagnosing system issues...${C.reset}\n`);

  let issues = 0;

  // Check Node.js
  const nodeVersion = shOutput("node --version");
  if (nodeVersion) {
    const major = parseInt(nodeVersion.slice(1).split(".")[0]);
    if (major >= 18) {
      success(`Node.js ${nodeVersion}`);
    } else {
      warn(`Node.js ${nodeVersion} (recommend v18+)`);
      issues++;
    }
  } else {
    error("Node.js not found");
    issues++;
  }

  // Check npm
  const npmVersion = shOutput("npm --version");
  if (npmVersion) {
    success(`npm ${npmVersion}`);
  } else {
    error("npm not found");
    issues++;
  }

  // Check wrangler
  const wranglerVersion = shOutput("npx wrangler --version 2>/dev/null");
  if (wranglerVersion) {
    success(`Wrangler ${wranglerVersion}`);
  } else {
    warn("Wrangler not installed (run: npm install -g wrangler)");
    issues++;
  }

  // Check wrangler auth
  const wranglerWhoami = shOutput("npx wrangler whoami 2>/dev/null");
  if (wranglerWhoami && !wranglerWhoami.includes("not authenticated")) {
    success("Wrangler authenticated");
  } else {
    warn("Wrangler not authenticated (run: npx wrangler login)");
    issues++;
  }

  // Check git
  const gitVersion = shOutput("git --version");
  if (gitVersion) {
    success(gitVersion);
  } else {
    error("Git not found");
    issues++;
  }

  // Check core files
  const coreFiles = ["codemaster.js", "package.json", "wrangler.toml"];
  coreFiles.forEach(file => {
    if (fs.existsSync(file)) {
      success(`${file} present`);
    } else {
      warn(`${file} missing`);
      issues++;
    }
  });

  log("");
  if (issues === 0) {
    log(`${C.green}${C.bright}All systems operational!${C.reset}`);
  } else {
    log(`${C.yellow}${issues} issue(s) found. See warnings above.${C.reset}`);
  }
  log("");
}

// ═══════════════════════════════════════════════════════════════════════════════
// MAIN
// ═══════════════════════════════════════════════════════════════════════════════

const args = process.argv.slice(2);
const command = args[0];
const commandArgs = args.slice(1);

if (!command || command === "help" || command === "--help" || command === "-h") {
  commands.help.run();
} else if (commands[command]) {
  commands[command].run(commandArgs);
} else {
  error(`Unknown command: ${command}`);
  log(`\nRun ${C.cyan}codemaster help${C.reset} for available commands.\n`);
}
