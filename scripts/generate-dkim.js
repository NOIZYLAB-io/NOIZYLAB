// scripts/generate-dkim.js
// DKIM Key Pair Generator

import { generateKeyPairSync } from "crypto";
import { writeFileSync, readFileSync, existsSync } from "fs";
import { config } from "dotenv";

config();

const DOMAIN = process.env.DOMAIN || "noizylab.ca";
const SELECTOR = process.env.DKIM_SELECTOR || "selector1";

console.log("\n=== DKIM Key Generator ===\n");
console.log(`Domain: ${DOMAIN}`);
console.log(`Selector: ${SELECTOR}\n`);

// Generate RSA key pair
console.log("Generating 2048-bit RSA key pair...");
const { publicKey, privateKey } = generateKeyPairSync("rsa", {
  modulusLength: 2048,
  publicKeyEncoding: {
    type: "spki",
    format: "pem",
  },
  privateKeyEncoding: {
    type: "pkcs8",
    format: "pem",
  },
});

// Extract public key without headers and newlines for DNS
const publicKeyDNS = publicKey
  .replace(/-----BEGIN PUBLIC KEY-----/, "")
  .replace(/-----END PUBLIC KEY-----/, "")
  .replace(/\n/g, "")
  .trim();

console.log("Keys generated successfully!\n");

// Save keys to files
const timestamp = new Date().toISOString().replace(/[:.]/g, "-");
const privateKeyFile = `./backups/dkim-private-${SELECTOR}-${timestamp}.pem`;
const publicKeyFile = `./backups/dkim-public-${SELECTOR}-${timestamp}.pem`;

writeFileSync(privateKeyFile, privateKey);
writeFileSync(publicKeyFile, publicKey);

console.log("Keys saved to:");
console.log(`  Private: ${privateKeyFile}`);
console.log(`  Public:  ${publicKeyFile}\n`);

// Update .env file
const envPath = "./.env";
let envContent = "";

if (existsSync(envPath)) {
  envContent = readFileSync(envPath, "utf-8");
} else if (existsSync("./.env.example")) {
  envContent = readFileSync("./.env.example", "utf-8");
}

// Update or add DKIM keys
const updateEnvVar = (content, key, value) => {
  const regex = new RegExp(`^${key}=.*$`, "m");
  if (regex.test(content)) {
    return content.replace(regex, `${key}=${value}`);
  } else {
    return content + `\n${key}=${value}`;
  }
};

envContent = updateEnvVar(envContent, "DKIM_PUBLIC_KEY", publicKeyDNS);
envContent = updateEnvVar(
  envContent,
  "DKIM_PRIVATE_KEY",
  privateKey.replace(/\n/g, "\\n")
);

writeFileSync(envPath, envContent);
console.log("Updated .env file with new DKIM keys\n");

// Display DNS record
console.log("=== DNS TXT Record ===\n");
console.log(`Name: ${SELECTOR}._domainkey.${DOMAIN}`);
console.log(`Type: TXT`);
console.log(`Value: v=DKIM1; k=rsa; p=${publicKeyDNS}\n`);

console.log("=== GoDaddy DNS Record Format ===\n");
console.log(`Name: ${SELECTOR}._domainkey`);
console.log(`Type: TXT`);
console.log(`Data: v=DKIM1; k=rsa; p=${publicKeyDNS}\n`);

console.log("=== Next Steps ===\n");
console.log("1. Run: npm run dns:setup");
console.log("2. Wait 24-48 hours for DNS propagation");
console.log("3. Verify: npm run dns:verify");
console.log("4. Test email: npm run test:email\n");

console.log("IMPORTANT: Keep the private key secure and never share it!\n");
