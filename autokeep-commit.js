#!/usr/bin/env node

import { execSync } from "child_process";

function changed() {
  return execSync("git status --porcelain").toString().trim() !== "";
}

if (!changed()) process.exit(0);

try {
  // Generate commit message using Cursor's internal model
  const msg = execSync(
    `cursor --summarize-diff`,
    { encoding: "utf8" }
  ).trim();

  execSync("git add -A");
  execSync(`git commit -m "${msg || "AutoKeep: update"}"`);

  console.log("✓ AutoKeep committed changes.");
} catch (err) {
  console.error("AutoKeep commit failed:", err.message);
}
