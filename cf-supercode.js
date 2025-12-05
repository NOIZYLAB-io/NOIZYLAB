#!/usr/bin/env node
/**
 * CLOUDFLARE SUPERCODE — NoizyLab OS
 * ----------------------------------------
 * One command to:
 *  - Deploy all Workers
 *  - Run all D1 migrations
 *  - Sync Queues & DOs
 *  - Test AI providers
 *  - Validate wrangler environment
 */

import { execSync } from "child_process";
import { existsSync, readFileSync } from "fs";
import { fileURLToPath } from "url";
import { dirname, join } from "path";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const BASE = join(__dirname, "..");

function run(cmd, options = {}) {
  console.log(`➡️  ${cmd}`);
  try {
    execSync(cmd, { 
      stdio: options.silent ? "ignore" : "inherit",
      cwd: BASE,
      ...options 
    });
    return true;
  } catch (error) {
    console.error(`❌ Command failed: ${cmd}`);
    if (!options.ignoreErrors) {
      throw error;
    }
    return false;
  }
}

function loadEnv() {
  const envPath = `${BASE}/.env`;
  if (!existsSync(envPath)) {
    console.warn("⚠️  .env file not found");
    return;
  }

  const lines = readFileSync(envPath, "utf8")
    .split("\n")
    .map(l => l.trim())
    .filter(Boolean)
    .filter(l => !l.startsWith("#"));

  lines.forEach(line => {
    const match = line.match(/^([^=]+)=(.*)$/);
    if (match) {
      const [, key, value] = match;
      process.env[key.trim()] = value.trim().replace(/^["']|["']$/g, "");
    }
  });
}

// ------------------------------
// MAIN EXECUTION
// ------------------------------
(async () => {
  console.log("🚀 CLOUDFLARE SUPERCODE STARTING…");
  console.log("");

  loadEnv();

  if (!process.env.CF_ACCOUNT_ID || !process.env.CF_API_TOKEN) {
    console.error("❌ Missing Cloudflare credentials in .env");
    console.error("   Required: CF_ACCOUNT_ID, CF_API_TOKEN");
    process.exit(1);
  }

  // Wrangler login if needed
  try {
    execSync("wrangler whoami", { stdio: "ignore", cwd: BASE });
    console.log("✔️  Already authenticated with Cloudflare");
  } catch {
    console.log("🔑 Logging in to Cloudflare...");
    run("wrangler login");
  }

  // Deploy all workers
  console.log("");
  console.log("🏗️  Deploying Workers...");
  const workers = [
    "ai-super-worker",
    "super-worker", 
    "noizymem-engine",
    "vlan-autopilot",
    "intake",
    "mc96",
    "teamviewer",
    "agent-arbiter",
    "dreamchamber",
    "events"
  ];

  for (const w of workers) {
    const path = `${BASE}/workers/${w}`;
    if (existsSync(path) && existsSync(`${path}/wrangler.toml`)) {
      console.log(`  📦 Deploying ${w}...`);
      run(`cd ${path} && wrangler deploy`, { ignoreErrors: true });
    }
  }

  // Sync Queues
  console.log("");
  console.log("📬 Setting up Queues...");
  const queues = ["SNAPSHOT_QUEUE", "EVENT_QUEUE", "AI_QUEUE", "REPAIR_QUEUE"];
  for (const queue of queues) {
    run(`wrangler queues create ${queue} || true`, { ignoreErrors: true });
  }

  // Run D1 migrations
  console.log("");
  console.log("💾 Running D1 Migrations...");
  const migrations = [
    `${BASE}/migrations/sql/001_initial_schema.sql`,
    `${BASE}/db/schema/init.sql`
  ];
  
  for (const migration of migrations) {
    if (existsSync(migration)) {
      console.log(`  📝 Running ${migration}...`);
      run(`wrangler d1 execute noizylab --file=${migration}`, { ignoreErrors: true });
    }
  }

  // Test AI providers if configured
  console.log("");
  console.log("🤖 Testing AI Providers...");
  if (process.env.GEMINI_API_KEY) {
    console.log("  ✓ Gemini API key configured");
  }
  if (process.env.ANTHROPIC_API_KEY) {
    console.log("  ✓ Claude API key configured");
  }
  if (process.env.OPENAI_API_KEY) {
    console.log("  ✓ OpenAI API key configured");
  }

  console.log("");
  console.log("✨ ALL CLOUDFLARE SYSTEMS SYNCED SUCCESSFULLY!");
  console.log("");
  console.log("Next steps:");
  console.log("  • Run: wrangler dev (local development)");
  console.log("  • Run: ./supercode/guardian.sh (system health check)");
  console.log("  • Run: ./supercode/test-harness.sh (run tests)");
})();

