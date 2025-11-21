// godaddy-dns-manager.js
// Run with: node godaddy-dns-manager.js [--setup|--verify|--list]

import fetch from "node-fetch";
import { config } from "dotenv";

// Load environment variables
config();

// ----------------------------
// Configuration
// ----------------------------
const API_KEY = process.env.GODADDY_API_KEY || "YOUR_GODADDY_API_KEY";
const API_SECRET = process.env.GODADDY_API_SECRET || "YOUR_GODADDY_API_SECRET";
const DOMAIN = process.env.DOMAIN || "noizylab.ca";
const MAIL_SERVER_IP = process.env.MAIL_SERVER_IP || "YOUR_MAIL_SERVER_IP";
const DKIM_SELECTOR = process.env.DKIM_SELECTOR || "selector1";
const DKIM_PUBLIC_KEY = process.env.DKIM_PUBLIC_KEY || "DKIM_PLACEHOLDER_VALUE";

// ----------------------------
// Helper for GoDaddy API calls
// ----------------------------
async function api(path, method = "GET", body = null) {
  const url = `https://api.godaddy.com/v1/domains/${DOMAIN}${path}`;

  const headers = {
    Authorization: `sso-key ${API_KEY}:${API_SECRET}`,
    "Content-Type": "application/json",
  };

  const options = { method, headers };

  if (body) options.body = JSON.stringify(body);

  const response = await fetch(url, options);
  if (!response.ok) {
    console.error(`API Error: ${response.status} ${response.statusText}`);
    const details = await response.text();
    console.error(details);
    throw new Error("GoDaddy API failed.");
  }

  return response.json().catch(() => ({}));
}

// ----------------------------
// List all DNS records
// ----------------------------
async function listRecords() {
  console.log(`\nListing DNS records for ${DOMAIN}...\n`);
  const records = await api("/records");

  if (Array.isArray(records)) {
    console.log("Current DNS Records:");
    console.log("-".repeat(60));
    records.forEach((r) => {
      console.log(`${r.type.padEnd(6)} ${r.name.padEnd(30)} ${r.data}`);
    });
    console.log("-".repeat(60));
    console.log(`Total: ${records.length} records\n`);
  }

  return records;
}

// ----------------------------
// Set domain forwarding
// ----------------------------
async function setForwarding() {
  console.log("\nSetting forwarding for noizyfish.com -> noizylab.ca...");

  // Note: Domain forwarding is typically set on the source domain (noizyfish.com)
  // This creates a CNAME or redirect. Adjust endpoint as needed.
  const forwarding = {
    type: "REDIRECT_PERMANENT",
    url: "https://noizylab.ca",
  };

  // GoDaddy forwarding endpoint may vary - check API docs
  // This is a placeholder for the forwarding setup
  console.log("Note: Configure forwarding in GoDaddy dashboard or on source domain");
  return forwarding;
}

// ----------------------------
// Configure A record for mail server
// ----------------------------
async function setMailServerRecord() {
  console.log("\nAdding A record for mail server...");

  if (MAIL_SERVER_IP === "YOUR_MAIL_SERVER_IP") {
    console.log("Warning: MAIL_SERVER_IP not configured. Skipping A record.");
    return;
  }

  const record = [
    {
      type: "A",
      name: "mail",
      data: MAIL_SERVER_IP,
      ttl: 600,
    },
  ];

  await api("/records/A/mail", "PUT", record);
  console.log(`A record added: mail.${DOMAIN} -> ${MAIL_SERVER_IP}`);
}

// ----------------------------
// Configure MX record
// ----------------------------
async function setMXRecord() {
  console.log("\nAdding MX record...");

  const record = [
    {
      type: "MX",
      name: "@",
      data: `mail.${DOMAIN}`,
      priority: 10,
      ttl: 600,
    },
  ];

  await api("/records/MX/@", "PUT", record);
  console.log(`MX record added: ${DOMAIN} -> mail.${DOMAIN} (priority 10)`);
}

// ----------------------------
// Configure SPF record
// ----------------------------
async function setSPFRecord() {
  console.log("\nAdding SPF record...");

  const spfValue = `v=spf1 a mx ip4:${MAIL_SERVER_IP !== "YOUR_MAIL_SERVER_IP" ? MAIL_SERVER_IP : "YOUR_IP"} ~all`;

  const record = [
    {
      type: "TXT",
      name: "@",
      data: spfValue,
      ttl: 600,
    },
  ];

  await api("/records/TXT/@", "PUT", record);
  console.log(`SPF record added: ${spfValue}`);
}

// ----------------------------
// Configure DKIM record
// ----------------------------
async function setDKIMRecord() {
  console.log("\nAdding DKIM record...");

  if (DKIM_PUBLIC_KEY === "DKIM_PLACEHOLDER_VALUE") {
    console.log("Warning: DKIM_PUBLIC_KEY not configured. Using placeholder.");
  }

  const dkimName = `${DKIM_SELECTOR}._domainkey`;
  const dkimValue = `v=DKIM1; k=rsa; p=${DKIM_PUBLIC_KEY}`;

  const record = [
    {
      type: "TXT",
      name: dkimName,
      data: dkimValue,
      ttl: 600,
    },
  ];

  await api(`/records/TXT/${dkimName}`, "PUT", record);
  console.log(`DKIM record added: ${dkimName}.${DOMAIN}`);
}

// ----------------------------
// Configure DMARC record
// ----------------------------
async function setDMARCRecord() {
  console.log("\nAdding DMARC record...");

  const dmarcValue = `v=DMARC1; p=quarantine; rua=mailto:dmarc@${DOMAIN}; ruf=mailto:dmarc@${DOMAIN}; fo=1`;

  const record = [
    {
      type: "TXT",
      name: "_dmarc",
      data: dmarcValue,
      ttl: 600,
    },
  ];

  await api("/records/TXT/_dmarc", "PUT", record);
  console.log(`DMARC record added: _dmarc.${DOMAIN}`);
}

// ----------------------------
// Verify DNS configuration
// ----------------------------
async function verifyDNS() {
  console.log(`\nVerifying DNS configuration for ${DOMAIN}...\n`);

  const records = await api("/records");
  const checks = {
    mx: false,
    spf: false,
    dkim: false,
    dmarc: false,
    mailA: false,
  };

  records.forEach((r) => {
    if (r.type === "MX") checks.mx = true;
    if (r.type === "TXT" && r.data.includes("v=spf1")) checks.spf = true;
    if (r.type === "TXT" && r.name.includes("_domainkey")) checks.dkim = true;
    if (r.type === "TXT" && r.name === "_dmarc") checks.dmarc = true;
    if (r.type === "A" && r.name === "mail") checks.mailA = true;
  });

  console.log("DNS Verification Results:");
  console.log("-".repeat(40));
  console.log(`MX Record:      ${checks.mx ? "OK" : "MISSING"}`);
  console.log(`SPF Record:     ${checks.spf ? "OK" : "MISSING"}`);
  console.log(`DKIM Record:    ${checks.dkim ? "OK" : "MISSING"}`);
  console.log(`DMARC Record:   ${checks.dmarc ? "OK" : "MISSING"}`);
  console.log(`Mail A Record:  ${checks.mailA ? "OK" : "MISSING"}`);
  console.log("-".repeat(40));

  const allPassed = Object.values(checks).every((v) => v);
  if (allPassed) {
    console.log("\nAll DNS records configured correctly!\n");
  } else {
    console.log("\nSome records are missing. Run with --setup to configure.\n");
  }

  return checks;
}

// ----------------------------
// Full email DNS setup
// ----------------------------
async function setupEmailDNS() {
  console.log("\n=== Setting up Email DNS Records ===\n");

  await setMailServerRecord();
  await setMXRecord();
  await setSPFRecord();
  await setDKIMRecord();
  await setDMARCRecord();

  console.log("\n=== Email DNS Setup Complete ===\n");
}

// ----------------------------
// CLI Handler
// ----------------------------
function showHelp() {
  console.log(`
GoDaddy DNS Manager for ${DOMAIN}

Usage: node godaddy-dns-manager.js [command]

Commands:
  --setup    Configure all email DNS records (MX, SPF, DKIM, DMARC)
  --verify   Verify DNS configuration
  --list     List all current DNS records
  --help     Show this help message

Configuration:
  Copy .env.example to .env and fill in your credentials:
  - GODADDY_API_KEY
  - GODADDY_API_SECRET
  - MAIL_SERVER_IP
  - DKIM_PUBLIC_KEY
`);
}

// ----------------------------
// EXECUTE
// ----------------------------
async function run() {
  const args = process.argv.slice(2);
  const command = args[0] || "--help";

  // Validate credentials
  if (API_KEY === "YOUR_GODADDY_API_KEY" || API_SECRET === "YOUR_GODADDY_API_SECRET") {
    if (command !== "--help") {
      console.error("\nError: GoDaddy API credentials not configured.");
      console.error("Copy .env.example to .env and add your credentials.\n");
      process.exit(1);
    }
  }

  try {
    switch (command) {
      case "--setup":
        await setupEmailDNS();
        await verifyDNS();
        break;
      case "--verify":
        await verifyDNS();
        break;
      case "--list":
        await listRecords();
        break;
      case "--help":
      default:
        showHelp();
    }
  } catch (e) {
    console.error("\nError:", e.message);
    process.exit(1);
  }
}

run();
