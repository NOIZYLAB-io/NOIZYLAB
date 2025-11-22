// scripts/restore-dns.js
// Restore DNS configuration from backup

import fetch from "node-fetch";
import { readFileSync, readdirSync } from "fs";
import { config } from "dotenv";
import { createInterface } from "readline";

config();

const API_KEY = process.env.GODADDY_API_KEY;
const API_SECRET = process.env.GODADDY_API_SECRET;
const DOMAIN = process.env.DOMAIN || "noizylab.ca";

const rl = createInterface({
  input: process.stdin,
  output: process.stdout,
});

const question = (prompt) => {
  return new Promise((resolve) => {
    rl.question(prompt, resolve);
  });
};

async function restoreDNS() {
  console.log("\n=== DNS Restore Utility ===\n");

  if (!API_KEY || !API_SECRET) {
    console.error("❌ Error: GoDaddy API credentials not configured.");
    console.error("Run: npm run setup:wizard\n");
    rl.close();
    process.exit(1);
  }

  try {
    // List available backups
    const backupFiles = readdirSync("./backups")
      .filter((f) => f.startsWith("dns-backup-") && f.endsWith(".json"))
      .sort()
      .reverse();

    if (backupFiles.length === 0) {
      console.log("❌ No backup files found in ./backups/");
      console.log("Create a backup first: npm run dns:backup\n");
      rl.close();
      process.exit(1);
    }

    console.log("Available backups:\n");
    backupFiles.forEach((file, index) => {
      const backup = JSON.parse(readFileSync(`./backups/${file}`, "utf-8"));
      console.log(`${index + 1}. ${file}`);
      console.log(`   Date: ${new Date(backup.timestamp).toLocaleString()}`);
      console.log(`   Records: ${backup.recordCount}`);
      console.log();
    });

    const selection = await question(
      "Select backup to restore (number) or 'latest' [latest]: "
    );
    rl.close();

    let backupFile;
    if (!selection || selection.toLowerCase() === "latest") {
      backupFile = backupFiles[0];
    } else {
      const index = parseInt(selection) - 1;
      if (index < 0 || index >= backupFiles.length) {
        console.log("❌ Invalid selection\n");
        process.exit(1);
      }
      backupFile = backupFiles[index];
    }

    console.log(`\nRestoring from: ${backupFile}\n`);

    // Load backup
    const backup = JSON.parse(readFileSync(`./backups/${backupFile}`, "utf-8"));

    console.log(`Domain: ${backup.domain}`);
    console.log(`Backup Date: ${new Date(backup.timestamp).toLocaleString()}`);
    console.log(`Records to restore: ${backup.recordCount}\n`);

    // Restore DNS records
    console.log("⚠️  WARNING: This will replace ALL current DNS records!");
    console.log("Make sure you have a current backup before proceeding.\n");

    const url = `https://api.godaddy.com/v1/domains/${DOMAIN}/records`;
    const headers = {
      Authorization: `sso-key ${API_KEY}:${API_SECRET}`,
      "Content-Type": "application/json",
    };

    const response = await fetch(url, {
      method: "PUT",
      headers,
      body: JSON.stringify(backup.records),
    });

    if (!response.ok) {
      const error = await response.text();
      throw new Error(`API Error ${response.status}: ${error}`);
    }

    console.log("✅ DNS records restored successfully!");
    console.log(`   Restored ${backup.recordCount} records`);
    console.log(`   Domain: ${backup.domain}`);
    console.log();
    console.log("⏰ DNS propagation may take 24-48 hours");
    console.log("   Check status: npm run dns:check-propagation\n");
  } catch (error) {
    console.error("\n❌ Restore failed:", error.message);
    rl.close();
    process.exit(1);
  }
}

restoreDNS();
