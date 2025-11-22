// scripts/test-email.js
// Test email sending with DKIM signing

import nodemailer from "nodemailer";
import { config } from "dotenv";

config();

const DOMAIN = process.env.DOMAIN || "noizylab.ca";
const SMTP_HOST = process.env.SMTP_HOST;
const SMTP_PORT = process.env.SMTP_PORT || 587;
const SMTP_USER = process.env.SMTP_USER;
const SMTP_PASS = process.env.SMTP_PASS;
const TEST_EMAIL_TO = process.env.TEST_EMAIL_TO;
const DKIM_PRIVATE_KEY = process.env.DKIM_PRIVATE_KEY
  ? process.env.DKIM_PRIVATE_KEY.replace(/\\n/g, "\n")
  : null;
const DKIM_SELECTOR = process.env.DKIM_SELECTOR || "selector1";

async function testEmail() {
  console.log("\n=== Email Test Utility ===\n");

  // Validate configuration
  if (!SMTP_HOST || !SMTP_USER || !SMTP_PASS || !TEST_EMAIL_TO) {
    console.error("❌ Error: Email configuration incomplete.");
    console.error("\nRequired environment variables:");
    console.error("  - SMTP_HOST");
    console.error("  - SMTP_USER");
    console.error("  - SMTP_PASS");
    console.error("  - TEST_EMAIL_TO");
    console.error("\nRun: npm run setup:wizard\n");
    process.exit(1);
  }

  console.log(`Domain: ${DOMAIN}`);
  console.log(`SMTP Host: ${SMTP_HOST}:${SMTP_PORT}`);
  console.log(`From: ${SMTP_USER}`);
  console.log(`To: ${TEST_EMAIL_TO}`);
  console.log(`DKIM: ${DKIM_PRIVATE_KEY ? "Enabled" : "Disabled"}\n`);

  // Create transporter
  const transportOptions = {
    host: SMTP_HOST,
    port: parseInt(SMTP_PORT),
    secure: parseInt(SMTP_PORT) === 465,
    auth: {
      user: SMTP_USER,
      pass: SMTP_PASS,
    },
  };

  // Add DKIM if configured
  if (DKIM_PRIVATE_KEY) {
    transportOptions.dkim = {
      domainName: DOMAIN,
      keySelector: DKIM_SELECTOR,
      privateKey: DKIM_PRIVATE_KEY,
    };
  }

  const transporter = nodemailer.createTransport(transportOptions);

  // Test connection
  console.log("Testing SMTP connection...");
  try {
    await transporter.verify();
    console.log("✅ SMTP connection successful\n");
  } catch (error) {
    console.error("❌ SMTP connection failed:", error.message);
    console.error("\nCheck your SMTP credentials and try again.\n");
    process.exit(1);
  }

  // Send test email
  const timestamp = new Date().toISOString();
  const mailOptions = {
    from: `NOIZYLAB Test <${SMTP_USER}>`,
    to: TEST_EMAIL_TO,
    subject: `NOIZYLAB Email Test - ${timestamp}`,
    text: `This is a test email from NOIZYLAB DNS & Email Management System.

Domain: ${DOMAIN}
Timestamp: ${timestamp}
DKIM Signing: ${DKIM_PRIVATE_KEY ? "Enabled" : "Disabled"}
DKIM Selector: ${DKIM_SELECTOR}

If you receive this email, your email configuration is working correctly!

To verify email authentication:
1. Check email headers for DKIM signature
2. Use tools like:
   - https://www.mail-tester.com
   - https://mxtoolbox.com/dkim.aspx

---
NOIZYLAB Email System
${DOMAIN}
`,
    html: `
<!DOCTYPE html>
<html>
<head>
  <style>
    body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
    .container { max-width: 600px; margin: 0 auto; padding: 20px; }
    .header { background: #007bff; color: white; padding: 20px; text-align: center; }
    .content { background: #f8f9fa; padding: 20px; margin: 20px 0; }
    .footer { text-align: center; color: #666; font-size: 12px; }
    .success { color: #28a745; }
    .info { background: #e7f3ff; border-left: 4px solid #007bff; padding: 10px; margin: 10px 0; }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h1>NOIZYLAB Email Test</h1>
    </div>
    <div class="content">
      <h2 class="success">✅ Test Email Received!</h2>
      <p>Your NOIZYLAB email system is configured correctly.</p>

      <div class="info">
        <strong>Configuration Details:</strong><br>
        <strong>Domain:</strong> ${DOMAIN}<br>
        <strong>Timestamp:</strong> ${timestamp}<br>
        <strong>DKIM Signing:</strong> ${DKIM_PRIVATE_KEY ? "Enabled ✅" : "Disabled ❌"}<br>
        <strong>DKIM Selector:</strong> ${DKIM_SELECTOR}
      </div>

      <h3>Verify Email Authentication:</h3>
      <ol>
        <li>Check email headers for DKIM signature</li>
        <li>Use verification tools:
          <ul>
            <li><a href="https://www.mail-tester.com">Mail Tester</a></li>
            <li><a href="https://mxtoolbox.com/dkim.aspx">MXToolbox DKIM</a></li>
          </ul>
        </li>
      </ol>
    </div>
    <div class="footer">
      <p>NOIZYLAB Email System<br>${DOMAIN}</p>
    </div>
  </div>
</body>
</html>
`,
  };

  console.log("Sending test email...");
  try {
    const info = await transporter.sendMail(mailOptions);
    console.log("\n✅ Email sent successfully!");
    console.log(`   Message ID: ${info.messageId}`);
    console.log(`   Recipient: ${TEST_EMAIL_TO}`);
    console.log();
    console.log("Check your inbox and verify:");
    console.log("  1. Email was received");
    console.log("  2. Email headers show DKIM signature (if enabled)");
    console.log("  3. Email passed SPF/DKIM/DMARC checks");
    console.log();
    console.log("Use mail-tester.com for detailed analysis:");
    console.log("  1. Send an email to the address provided by mail-tester.com");
    console.log("  2. Check your spam score and authentication results\n");
  } catch (error) {
    console.error("\n❌ Email sending failed:", error.message);
    console.error("\nTroubleshooting:");
    console.error("  - Verify SMTP credentials");
    console.error("  - Check DNS records are propagated");
    console.error("  - Ensure mail server is configured correctly");
    console.error("  - Check firewall/security settings\n");
    process.exit(1);
  }
}

testEmail();
