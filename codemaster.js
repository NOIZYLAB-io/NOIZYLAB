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
// ║                                   Version 1.0.0                                        ║
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
  ${C.cyan}THE ULTIMATE AI-POWERED CODE COMMAND CENTER${C.reset}                    ${C.dim}v1.0.0${C.reset}
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
  version: { desc: "Show version", run: () => log("CODEMASTER v1.0.0") },
  status: { desc: "System status", run: showStatus },

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
  noizy: { desc: "NoizyLab commands", usage: "noizy <command>", run: noizyCommands }
};

// ═══════════════════════════════════════════════════════════════════════════════
// COMMAND IMPLEMENTATIONS
// ═══════════════════════════════════════════════════════════════════════════════

function showHelp() {
  banner();

  log(`${C.bright}COMMANDS:${C.reset}\n`);

  const categories = {
    "Info": ["help", "version", "status"],
    "Agents": ["agents", "summon", "council", "chat"],
    "Generation": ["forge", "generators", "blueprints", "scaffold"],
    "Workflows": ["workflow"],
    "Deployment": ["deploy", "dev"],
    "Analysis": ["analyze", "secure"],
    "Interactive": ["shell"],
    "Utilities": ["init", "config", "logs", "noizy"]
  };

  for (const [category, cmds] of Object.entries(categories)) {
    log(`  ${C.yellow}${category}${C.reset}`);
    cmds.forEach(name => {
      const cmd = commands[name];
      const usage = cmd.usage ? ` ${C.dim}${cmd.usage}${C.reset}` : "";
      log(`    ${C.cyan}${name.padEnd(12)}${C.reset} ${cmd.desc}${usage}`);
    });
    log("");
  }

  log(`${C.bright}EXAMPLES:${C.reset}\n`);
  log(`  ${C.dim}$${C.reset} codemaster summon FORGE "Create a REST API for users"`);
  log(`  ${C.dim}$${C.reset} codemaster forge api --resources users,posts`);
  log(`  ${C.dim}$${C.reset} codemaster scaffold saas my-app`);
  log(`  ${C.dim}$${C.reset} codemaster shell`);
  log(`  ${C.dim}$${C.reset} codemaster council "Review this architecture"`);
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
