#!/usr/bin/env node
/**
 * 🧊 NOIZY SUPER CLI
 * 
 * Cursor will autocomplete EVERY Cloudflare call after this.
 */

import { nukeDNS, upsertDNS } from "../cf/dns.js";
import { createRoute } from "../cf/email.js";

console.log("⚡ NOIZYLAB: CLOUDFLARE CONTROL MODE ⚡");

const cmd = process.argv[2];
const zoneId = process.env.CF_ZONE;

if (!zoneId) {
  console.error("❌ CF_ZONE environment variable required");
  process.exit(1);
}

switch (cmd) {
  case "reset":
    await nukeDNS(zoneId);
    console.log("🔥 DNS nuked!");
    break;

  case "fix-email":
    await createRoute(zoneId, "help@noizylab.ca", "rsplowman@icloud.com");
    await createRoute(zoneId, "rsp@noizylab.ca", "rsplowman@icloud.com");
    console.log("📨 Email routing restored!");
    break;

  case "dominate":
    console.log("🌩 Activating Overlord Mode...");
    await nukeDNS(zoneId);
    await upsertDNS(zoneId, {
      type: "A",
      name: "noizylab.ca",
      content: "1.1.1.1",
      proxied: true,
    });
    console.log("👑 Cloudflare now obeys.");
    break;

  default:
    console.log("Commands: reset | fix-email | dominate");
}

