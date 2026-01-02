/**
 * Email Notification Service
 * 
 * Handles all email notifications for NoizyLab GABRIEL
 * Uses Resend API for transactional emails
 */

interface EmailConfig {
  RESEND_API_KEY: string;
  FROM_EMAIL: string;
  REPLY_TO: string;
}

interface ScanResult {
  id: string;
  boardType: string;
  issuesCount: number;
  confidence: number;
  issues: Array<{
    component: string;
    type: string;
    severity: string;
    description: string;
  }>;
}

interface User {
  email: string;
  name: string;
  credits: number;
}

// ============================================================================
// EMAIL TEMPLATES
// ============================================================================

const templates = {
  // Welcome email for new users
  welcome: (user: User) => ({
    subject: '🔬 Welcome to NoizyLab GABRIEL - Your AI Board Inspector',
    html: `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #0a0a0a; color: #ffffff; margin: 0; padding: 40px 20px; }
    .container { max-width: 600px; margin: 0 auto; }
    .header { text-align: center; margin-bottom: 40px; }
    .logo { font-size: 32px; font-weight: bold; color: #22c55e; }
    .content { background: #111; border-radius: 16px; padding: 32px; border: 1px solid #222; }
    h1 { color: #22c55e; margin: 0 0 16px 0; }
    p { line-height: 1.6; color: #888; margin: 16px 0; }
    .button { display: inline-block; background: #22c55e; color: #000; padding: 14px 28px; border-radius: 8px; text-decoration: none; font-weight: 600; margin: 24px 0; }
    .features { background: #1a1a1a; border-radius: 12px; padding: 24px; margin: 24px 0; }
    .feature { display: flex; align-items: flex-start; margin: 16px 0; }
    .feature-icon { font-size: 24px; margin-right: 16px; }
    .feature-text h3 { color: #fff; margin: 0 0 4px 0; font-size: 16px; }
    .feature-text p { margin: 0; font-size: 14px; }
    .footer { text-align: center; margin-top: 40px; color: #666; font-size: 12px; }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <div class="logo">🔬 NoizyLab GABRIEL</div>
    </div>
    <div class="content">
      <h1>Welcome, ${user.name}!</h1>
      <p>You've just unlocked AI-powered board inspection. GABRIEL uses advanced computer vision to help you diagnose and repair electronics with precision.</p>
      
      <div class="features">
        <div class="feature">
          <span class="feature-icon">📸</span>
          <div class="feature-text">
            <h3>Instant Analysis</h3>
            <p>Snap a photo and get component-level diagnostics in seconds</p>
          </div>
        </div>
        <div class="feature">
          <span class="feature-icon">🎯</span>
          <div class="feature-text">
            <h3>AR Overlay</h3>
            <p>See exactly where issues are with augmented reality highlighting</p>
          </div>
        </div>
        <div class="feature">
          <span class="feature-icon">🎤</span>
          <div class="feature-text">
            <h3>Voice Guidance</h3>
            <p>Hands-free repair instructions while you work</p>
          </div>
        </div>
      </div>
      
      <p>You have <strong style="color: #22c55e;">${user.credits} free credits</strong> to get started!</p>
      
      <a href="https://gabriel.noizylab.com/dashboard" class="button">Start Your First Scan →</a>
      
      <p style="font-size: 14px;">Questions? Reply to this email or check our <a href="https://gabriel.noizylab.com/docs" style="color: #22c55e;">documentation</a>.</p>
    </div>
    <div class="footer">
      <p>NoizyLab Inc. • Anaheim, California</p>
      <p>You're receiving this because you signed up at gabriel.noizylab.com</p>
    </div>
  </div>
</body>
</html>
    `,
  }),

  // Scan complete notification
  scanComplete: (user: User, scan: ScanResult) => ({
    subject: `✅ Scan Complete: ${scan.issuesCount} issues found on ${scan.boardType}`,
    html: `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #0a0a0a; color: #ffffff; margin: 0; padding: 40px 20px; }
    .container { max-width: 600px; margin: 0 auto; }
    .header { text-align: center; margin-bottom: 40px; }
    .logo { font-size: 24px; font-weight: bold; color: #22c55e; }
    .content { background: #111; border-radius: 16px; padding: 32px; border: 1px solid #222; }
    h1 { color: #fff; margin: 0 0 8px 0; font-size: 24px; }
    .subtitle { color: #888; margin: 0 0 24px 0; }
    .stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin: 24px 0; }
    .stat { background: #1a1a1a; border-radius: 12px; padding: 16px; text-align: center; }
    .stat-value { font-size: 28px; font-weight: bold; color: #22c55e; }
    .stat-label { font-size: 12px; color: #666; margin-top: 4px; }
    .issues { margin: 24px 0; }
    .issue { background: #1a1a1a; border-radius: 8px; padding: 16px; margin: 12px 0; border-left: 4px solid; }
    .issue.critical { border-color: #ef4444; }
    .issue.warning { border-color: #f59e0b; }
    .issue.info { border-color: #3b82f6; }
    .issue-header { display: flex; justify-content: space-between; margin-bottom: 8px; }
    .issue-component { font-weight: 600; color: #fff; }
    .issue-type { font-size: 12px; color: #888; }
    .issue-desc { color: #888; font-size: 14px; }
    .button { display: inline-block; background: #22c55e; color: #000; padding: 14px 28px; border-radius: 8px; text-decoration: none; font-weight: 600; margin: 24px 0; }
    .footer { text-align: center; margin-top: 40px; color: #666; font-size: 12px; }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <div class="logo">🔬 NoizyLab GABRIEL</div>
    </div>
    <div class="content">
      <h1>Scan Complete!</h1>
      <p class="subtitle">${scan.boardType} • Scan ID: ${scan.id}</p>
      
      <div class="stats">
        <div class="stat">
          <div class="stat-value">${scan.issuesCount}</div>
          <div class="stat-label">Issues Found</div>
        </div>
        <div class="stat">
          <div class="stat-value">${scan.confidence}%</div>
          <div class="stat-label">Confidence</div>
        </div>
        <div class="stat">
          <div class="stat-value">${user.credits}</div>
          <div class="stat-label">Credits Left</div>
        </div>
      </div>
      
      <div class="issues">
        <h3 style="color: #888; font-size: 14px; text-transform: uppercase;">Issues Detected</h3>
        ${scan.issues.slice(0, 5).map(issue => `
          <div class="issue ${issue.severity}">
            <div class="issue-header">
              <span class="issue-component">${issue.component}</span>
              <span class="issue-type">${issue.type}</span>
            </div>
            <p class="issue-desc">${issue.description}</p>
          </div>
        `).join('')}
        ${scan.issues.length > 5 ? `<p style="color: #888; text-align: center;">+ ${scan.issues.length - 5} more issues</p>` : ''}
      </div>
      
      <a href="https://gabriel.noizylab.com/scan/${scan.id}" class="button">View Full Report →</a>
    </div>
    <div class="footer">
      <p>NoizyLab Inc. • Anaheim, California</p>
    </div>
  </div>
</body>
</html>
    `,
  }),

  // Low credits warning
  lowCredits: (user: User) => ({
    subject: `⚠️ Low Credits: Only ${user.credits} scans remaining`,
    html: `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #0a0a0a; color: #ffffff; margin: 0; padding: 40px 20px; }
    .container { max-width: 600px; margin: 0 auto; }
    .header { text-align: center; margin-bottom: 40px; }
    .logo { font-size: 24px; font-weight: bold; color: #22c55e; }
    .content { background: #111; border-radius: 16px; padding: 32px; border: 1px solid #f59e0b; }
    h1 { color: #f59e0b; margin: 0 0 16px 0; }
    p { line-height: 1.6; color: #888; margin: 16px 0; }
    .credits-display { background: #1a1a1a; border-radius: 12px; padding: 24px; text-align: center; margin: 24px 0; }
    .credits-value { font-size: 48px; font-weight: bold; color: #f59e0b; }
    .credits-label { color: #888; margin-top: 8px; }
    .plans { display: grid; gap: 16px; margin: 24px 0; }
    .plan { background: #1a1a1a; border-radius: 12px; padding: 20px; display: flex; justify-content: space-between; align-items: center; }
    .plan-name { font-weight: 600; }
    .plan-price { color: #22c55e; font-weight: bold; }
    .button { display: inline-block; background: #22c55e; color: #000; padding: 14px 28px; border-radius: 8px; text-decoration: none; font-weight: 600; margin: 24px 0; }
    .footer { text-align: center; margin-top: 40px; color: #666; font-size: 12px; }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <div class="logo">🔬 NoizyLab GABRIEL</div>
    </div>
    <div class="content">
      <h1>⚠️ Running Low on Credits</h1>
      <p>Hey ${user.name}, you're running low on scan credits. Top up to keep diagnosing boards without interruption.</p>
      
      <div class="credits-display">
        <div class="credits-value">${user.credits}</div>
        <div class="credits-label">Credits Remaining</div>
      </div>
      
      <div class="plans">
        <div class="plan">
          <span class="plan-name">Golden Audit (1 scan)</span>
          <span class="plan-price">$4.99</span>
        </div>
        <div class="plan">
          <span class="plan-name">Legacy Kit (10 scans)</span>
          <span class="plan-price">$29</span>
        </div>
        <div class="plan">
          <span class="plan-name">Pro Unlimited</span>
          <span class="plan-price">$99/mo</span>
        </div>
      </div>
      
      <a href="https://gabriel.noizylab.com/pricing" class="button">Get More Credits →</a>
    </div>
    <div class="footer">
      <p>NoizyLab Inc. • Anaheim, California</p>
    </div>
  </div>
</body>
</html>
    `,
  }),

  // Payment receipt
  paymentReceipt: (user: User, payment: { amount: number; product: string; credits: number; date: string }) => ({
    subject: `🧾 Receipt: ${payment.product} - $${(payment.amount / 100).toFixed(2)}`,
    html: `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #0a0a0a; color: #ffffff; margin: 0; padding: 40px 20px; }
    .container { max-width: 600px; margin: 0 auto; }
    .header { text-align: center; margin-bottom: 40px; }
    .logo { font-size: 24px; font-weight: bold; color: #22c55e; }
    .content { background: #111; border-radius: 16px; padding: 32px; border: 1px solid #222; }
    h1 { color: #22c55e; margin: 0 0 8px 0; }
    .subtitle { color: #888; margin: 0 0 24px 0; }
    .receipt { background: #1a1a1a; border-radius: 12px; padding: 24px; margin: 24px 0; }
    .receipt-row { display: flex; justify-content: space-between; padding: 12px 0; border-bottom: 1px solid #333; }
    .receipt-row:last-child { border-bottom: none; }
    .receipt-label { color: #888; }
    .receipt-value { font-weight: 600; }
    .total { font-size: 24px; color: #22c55e; }
    p { line-height: 1.6; color: #888; margin: 16px 0; }
    .button { display: inline-block; background: #22c55e; color: #000; padding: 14px 28px; border-radius: 8px; text-decoration: none; font-weight: 600; margin: 24px 0; }
    .footer { text-align: center; margin-top: 40px; color: #666; font-size: 12px; }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <div class="logo">🔬 NoizyLab GABRIEL</div>
    </div>
    <div class="content">
      <h1>Payment Received ✓</h1>
      <p class="subtitle">Thank you for your purchase, ${user.name}!</p>
      
      <div class="receipt">
        <div class="receipt-row">
          <span class="receipt-label">Product</span>
          <span class="receipt-value">${payment.product}</span>
        </div>
        <div class="receipt-row">
          <span class="receipt-label">Credits Added</span>
          <span class="receipt-value">+${payment.credits}</span>
        </div>
        <div class="receipt-row">
          <span class="receipt-label">Date</span>
          <span class="receipt-value">${payment.date}</span>
        </div>
        <div class="receipt-row">
          <span class="receipt-label">Amount Paid</span>
          <span class="receipt-value total">$${(payment.amount / 100).toFixed(2)}</span>
        </div>
      </div>
      
      <p>Your new credit balance: <strong style="color: #22c55e;">${user.credits} credits</strong></p>
      
      <a href="https://gabriel.noizylab.com/dashboard" class="button">Go to Dashboard →</a>
      
      <p style="font-size: 12px; color: #666;">This receipt is for your records. For billing questions, reply to this email.</p>
    </div>
    <div class="footer">
      <p>NoizyLab Inc. • Anaheim, California</p>
      <p>Tax ID: XX-XXXXXXX</p>
    </div>
  </div>
</body>
</html>
    `,
  }),

  // Weekly digest
  weeklyDigest: (user: User, stats: { scans: number; issuesFound: number; boardsFixed: number }) => ({
    subject: `📊 Your Weekly GABRIEL Report: ${stats.scans} scans, ${stats.issuesFound} issues found`,
    html: `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #0a0a0a; color: #ffffff; margin: 0; padding: 40px 20px; }
    .container { max-width: 600px; margin: 0 auto; }
    .header { text-align: center; margin-bottom: 40px; }
    .logo { font-size: 24px; font-weight: bold; color: #22c55e; }
    .content { background: #111; border-radius: 16px; padding: 32px; border: 1px solid #222; }
    h1 { color: #fff; margin: 0 0 8px 0; }
    .subtitle { color: #888; margin: 0 0 24px 0; }
    .stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin: 24px 0; }
    .stat { background: #1a1a1a; border-radius: 12px; padding: 20px; text-align: center; }
    .stat-value { font-size: 32px; font-weight: bold; color: #22c55e; }
    .stat-label { font-size: 12px; color: #666; margin-top: 8px; }
    p { line-height: 1.6; color: #888; margin: 16px 0; }
    .tip { background: linear-gradient(135deg, #22c55e20, #3b82f620); border-radius: 12px; padding: 20px; margin: 24px 0; }
    .tip h3 { color: #22c55e; margin: 0 0 8px 0; font-size: 14px; }
    .tip p { margin: 0; font-size: 14px; }
    .button { display: inline-block; background: #22c55e; color: #000; padding: 14px 28px; border-radius: 8px; text-decoration: none; font-weight: 600; margin: 24px 0; }
    .footer { text-align: center; margin-top: 40px; color: #666; font-size: 12px; }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <div class="logo">🔬 NoizyLab GABRIEL</div>
    </div>
    <div class="content">
      <h1>Your Week in Review</h1>
      <p class="subtitle">Hey ${user.name}, here's what you accomplished this week!</p>
      
      <div class="stats">
        <div class="stat">
          <div class="stat-value">${stats.scans}</div>
          <div class="stat-label">Boards Scanned</div>
        </div>
        <div class="stat">
          <div class="stat-value">${stats.issuesFound}</div>
          <div class="stat-label">Issues Found</div>
        </div>
        <div class="stat">
          <div class="stat-value">${stats.boardsFixed}</div>
          <div class="stat-label">Boards Fixed</div>
        </div>
      </div>
      
      <div class="tip">
        <h3>💡 Pro Tip</h3>
        <p>Use the AR overlay feature to highlight component locations in real-time while you work. It's like having X-ray vision for your boards!</p>
      </div>
      
      <p>You have <strong style="color: #22c55e;">${user.credits} credits</strong> remaining.</p>
      
      <a href="https://gabriel.noizylab.com/dashboard" class="button">View Full Stats →</a>
    </div>
    <div class="footer">
      <p>NoizyLab Inc. • Anaheim, California</p>
      <p><a href="https://gabriel.noizylab.com/settings" style="color: #666;">Manage email preferences</a></p>
    </div>
  </div>
</body>
</html>
    `,
  }),
};

// ============================================================================
// EMAIL SERVICE
// ============================================================================

export class EmailService {
  private config: EmailConfig;

  constructor(config: EmailConfig) {
    this.config = config;
  }

  private async send(to: string, template: { subject: string; html: string }) {
    const response = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${this.config.RESEND_API_KEY}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        from: this.config.FROM_EMAIL,
        reply_to: this.config.REPLY_TO,
        to: [to],
        subject: template.subject,
        html: template.html,
      }),
    });

    if (!response.ok) {
      const error = await response.text();
      throw new Error(`Failed to send email: ${error}`);
    }

    return response.json();
  }

  async sendWelcome(user: User) {
    return this.send(user.email, templates.welcome(user));
  }

  async sendScanComplete(user: User, scan: ScanResult) {
    return this.send(user.email, templates.scanComplete(user, scan));
  }

  async sendLowCredits(user: User) {
    return this.send(user.email, templates.lowCredits(user));
  }

  async sendPaymentReceipt(user: User, payment: { amount: number; product: string; credits: number; date: string }) {
    return this.send(user.email, templates.paymentReceipt(user, payment));
  }

  async sendWeeklyDigest(user: User, stats: { scans: number; issuesFound: number; boardsFixed: number }) {
    return this.send(user.email, templates.weeklyDigest(user, stats));
  }
}

// ============================================================================
// CLOUDFLARE WORKER INTEGRATION
// ============================================================================

export function createEmailRoutes(emailService: EmailService) {
  return {
    // Send welcome email when user registers
    async handleWelcome(user: User) {
      try {
        await emailService.sendWelcome(user);
        console.log(`Welcome email sent to ${user.email}`);
      } catch (error) {
        console.error('Failed to send welcome email:', error);
      }
    },

    // Send scan completion notification
    async handleScanComplete(user: User, scan: ScanResult) {
      try {
        await emailService.sendScanComplete(user, scan);
        
        // Check if low credits
        if (user.credits <= 2) {
          await emailService.sendLowCredits(user);
        }
      } catch (error) {
        console.error('Failed to send scan notification:', error);
      }
    },

    // Send payment receipt
    async handlePayment(user: User, payment: { amount: number; product: string; credits: number }) {
      try {
        await emailService.sendPaymentReceipt(user, {
          ...payment,
          date: new Date().toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'long',
            day: 'numeric',
          }),
        });
      } catch (error) {
        console.error('Failed to send payment receipt:', error);
      }
    },
  };
}

export default {
  EmailService,
  createEmailRoutes,
  templates,
};
