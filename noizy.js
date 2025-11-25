#!/usr/bin/env node
import { execSync } from "child_process";
import fs from "fs";

const args = process.argv.slice(2);
const command = args[0];

function sh(cmd) {
  return execSync(cmd, { encoding: "utf8" });
}

const help = `
🔥 NoizyLab CLI Commands

noizy init                Initialize project
noizy deploy-worker       Deploy Cloudflare Worker
noizy agent <NAME> <TASK> Call AI Agent
noizy logs                Read KV logs
`;

if (!command) {
  console.log(help);
  process.exit(0);
}

if (command === "init") {
  console.log("⚙ Initializing NoizyLab Project...");

  fs.mkdirSync("workers", { recursive: true });
  fs.writeFileSync("workers/email-worker.js", "// worker will be overwritten");

  console.log("Done.");
  process.exit(0);
}

if (command === "deploy-worker") {
  console.log("🚀 Deploying worker...");
  console.log(sh("npx wrangler deploy workers/email-worker.js"));
  process.exit(0);
}

if (command === "agent") {
  const agentName = args[1];
  const task = args.slice(2).join(" ");

  const prompt = `
  You are agent ${agentName}.
  Task: ${task}.
  Return JSON: { agent, action, notes, priority }
  `;

  console.log(sh(`npx wrangler ai "@cf/mistral/mistral-7b-instruct-v0.1" "${prompt}"`));
  process.exit(0);
}

if (command === "logs") {
  console.log(sh("npx wrangler kv:key list --namespace MAIL_LOGS"));
  process.exit(0);
}

console.log(help);
