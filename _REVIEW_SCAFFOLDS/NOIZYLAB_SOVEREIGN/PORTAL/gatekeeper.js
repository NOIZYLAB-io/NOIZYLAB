#!/usr/bin/env node
// Gatekeeper stub: reads manifest and prints revenue mode.
const fs = require("fs");
const path = require("path");

const manifestPath = path.join(__dirname, "..", "MANIFESTS", "noizylab_manifest.json");
let revenueMode = "AUTO";

const args = process.argv.slice(2);
for (let i = 0; i < args.length; i++) {
  if (args[i] === "--revenue-mode" && args[i + 1]) {
    revenueMode = args[i + 1];
    i++;
  }
}

function loadManifest() {
  try {
    const raw = fs.readFileSync(manifestPath, "utf8");
    return JSON.parse(raw);
  } catch (err) {
    console.error("Failed to load manifest:", err.message);
    return null;
  }
}

function main() {
  const manifest = loadManifest();
  if (!manifest) {
    console.log("Gatekeeper: manifest unavailable.");
    return;
  }
  console.log(`💰 Gatekeeper revenue mode: ${revenueMode}`);
  console.log(`Services loaded: ${(manifest.service_definitions || []).length}`);
}

main();
