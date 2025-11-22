// scripts/backup-dns.js
// Backup current DNS configuration

import fetch from "node-fetch";
import { writeFileSync } from "fs";
import { config } from "dotenv";

config();

const API_KEY = process.env.GODADDY_API_KEY;
const API_SECRET = process.env.GODADDY_API_SECRET;
const DOMAIN = process.env.DOMAIN || "noizylab.ca";

async function backupDNS() {
  console.log("\n=== DNS Backup Utility ===\n");

  if (!API_KEY || !API_SECRET) {
    console.error("❌ Error: GoDaddy API credentials not configured.");
    console.error("Run: npm run setup:wizard\n");
    process.exit(1);
  }

  console.log(`Domain: ${DOMAIN}`);
  console.log("Fetching current DNS records...\n");

  try {
    const url = `https://api.godaddy.com/v1/domains/${DOMAIN}/records`;
    const headers = {
      Authorization: `sso-key ${API_KEY}:${API_SECRET}`,
      "Content-Type": "application/json",
    };

    const response = await fetch(url, { headers });

    if (!response.ok) {
      const error = await response.text();
      throw new Error(`API Error ${response.status}: ${error}`);
    }

    const records = await response.json();
    console.log(`Retrieved ${records.length} DNS records\n`);

    // Create backup filename with timestamp
    const timestamp = new Date().toISOString().replace(/[:.]/g, "-");
    const filename = `./backups/dns-backup-${DOMAIN}-${timestamp}.json`;

    // Save backup
    const backup = {
      domain: DOMAIN,
      timestamp: new Date().toISOString(),
      recordCount: records.length,
      records: records,
    };

    writeFileSync(filename, JSON.stringify(backup, null, 2));

    console.log("✅ Backup created successfully!");
    console.log(`   File: ${filename}`);
    console.log(`   Records: ${records.length}`);
    console.log(`   Time: ${new Date().toLocaleString()}\n`);

    // Show summary
    const summary = records.reduce((acc, record) => {
      acc[record.type] = (acc[record.type] || 0) + 1;
      return acc;
    }, {});

    console.log("Record Summary:");
    console.log("-".repeat(30));
    Object.entries(summary).forEach(([type, count]) => {
      console.log(`${type.padEnd(10)} : ${count}`);
    });
    console.log("-".repeat(30));
    console.log();

    // Also create a latest backup symlink reference
    writeFileSync("./backups/latest-backup.json", JSON.stringify(backup, null, 2));
    console.log("💾 Latest backup reference updated\n");

    return backup;
  } catch (error) {
    console.error("\n❌ Backup failed:", error.message);
    process.exit(1);
  }
}

backupDNS();
