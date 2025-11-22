// scripts/check-propagation.js
// Check DNS propagation across multiple nameservers

import { promises as dns } from "dns";
import { config } from "dotenv";

config();

const DOMAIN = process.env.DOMAIN || "noizylab.ca";
const MAIL_DOMAIN = `mail.${DOMAIN}`;

// Public DNS servers to check
const DNS_SERVERS = [
  { name: "Google", ip: "8.8.8.8" },
  { name: "Cloudflare", ip: "1.1.1.1" },
  { name: "Quad9", ip: "9.9.9.9" },
  { name: "OpenDNS", ip: "208.67.222.222" },
];

async function checkRecord(domain, type, server) {
  const resolver = new dns.Resolver();
  resolver.setServers([server.ip]);

  try {
    let records;
    switch (type) {
      case "A":
        records = await resolver.resolve4(domain);
        return records;
      case "MX":
        records = await resolver.resolveMx(domain);
        return records.map((r) => `${r.priority} ${r.exchange}`);
      case "TXT":
        records = await resolver.resolveTxt(domain);
        return records.map((r) => r.join(" "));
      default:
        return null;
    }
  } catch (error) {
    return null;
  }
}

async function checkPropagation() {
  console.log("\n=== DNS Propagation Checker ===\n");
  console.log(`Domain: ${DOMAIN}\n`);

  const checks = [
    { domain: DOMAIN, type: "MX", description: "MX Record" },
    { domain: MAIL_DOMAIN, type: "A", description: "Mail Server A Record" },
    { domain: DOMAIN, type: "TXT", description: "TXT Records (SPF/DMARC)" },
    {
      domain: `${process.env.DKIM_SELECTOR || "selector1"}._domainkey.${DOMAIN}`,
      type: "TXT",
      description: "DKIM Record",
    },
    { domain: `_dmarc.${DOMAIN}`, type: "TXT", description: "DMARC Record" },
  ];

  console.log("Checking DNS propagation across multiple servers...\n");

  for (const check of checks) {
    console.log(`\n${check.description} (${check.domain}):`);
    console.log("-".repeat(60));

    const results = await Promise.all(
      DNS_SERVERS.map(async (server) => {
        const records = await checkRecord(check.domain, check.type, server);
        return { server, records };
      })
    );

    let allMatch = true;
    const firstResult = results[0].records;

    results.forEach(({ server, records }) => {
      const status = records ? "✅" : "❌";
      const recordStr = records
        ? Array.isArray(records)
          ? records.join(", ")
          : records
        : "Not found";

      console.log(`${status} ${server.name.padEnd(15)} ${recordStr}`);

      if (JSON.stringify(records) !== JSON.stringify(firstResult)) {
        allMatch = false;
      }
    });

    if (allMatch && firstResult) {
      console.log("\n✅ Fully propagated across all nameservers");
    } else if (results.some((r) => r.records)) {
      console.log("\n⚠️  Partial propagation - wait for full propagation");
    } else {
      console.log("\n❌ Not propagated - record may not be configured");
    }
  }

  console.log("\n");
  console.log("=== Propagation Summary ===\n");
  console.log("DNS propagation can take 24-48 hours to complete globally.");
  console.log("If you see partial propagation, check again in a few hours.\n");
  console.log("Additional tools to check propagation:");
  console.log("  - https://dnschecker.org");
  console.log("  - https://mxtoolbox.com");
  console.log("  - https://whatsmydns.net\n");
}

checkPropagation().catch((error) => {
  console.error("\n❌ Error:", error.message);
  process.exit(1);
});
