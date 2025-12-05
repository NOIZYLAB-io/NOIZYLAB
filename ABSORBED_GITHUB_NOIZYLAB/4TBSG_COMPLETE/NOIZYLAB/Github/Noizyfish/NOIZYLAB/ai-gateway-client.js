#!/usr/bin/env node
/**
 * NOIZYLAB AI Gateway Client
 * Automation script for interacting with Cloudflare AI Gateway
 * Usage: node ai-gateway-client.js
 */

const GATEWAY_URL = process.env.AI_GATEWAY_URL || 'https://noizylab-ai-gateway.your-subdomain.workers.dev';
const AUTH_TOKEN = process.env.INTERNAL_AUTH_TOKEN || 'your-secure-token-here';

/**
 * Call AI Gateway with authentication
 */
async function callAIGateway(prompt, model = 'claude', options = {}) {
  console.log(`\n🤖 Calling AI Gateway (${model})...`);
  
  const startTime = Date.now();
  
  try {
    const response = await fetch(GATEWAY_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${AUTH_TOKEN}`,
      },
      body: JSON.stringify({
        model_choice: model,
        prompt: prompt,
        max_tokens: options.max_tokens || 2048,
        temperature: options.temperature || 0.7,
      }),
    });

    if (!response.ok) {
      const errorText = await response.text();
      console.error(`❌ Gateway error (${response.status}):`, errorText);
      return null;
    }

    const data = await response.json();
    const duration = Date.now() - startTime;
    
    console.log(`✅ Response received in ${duration}ms`);
    console.log(`📊 Model: ${data.model}`);
    console.log(`📊 Usage:`, data.usage);
    
    return data;
  } catch (error) {
    console.error('❌ Request failed:', error.message);
    return null;
  }
}

/**
 * Generate email summary for domain reports
 */
async function generateDomainEmailSummary(domainData) {
  const prompt = `Analyze this domain and email configuration and provide a brief executive summary with recommendations:
  
${JSON.stringify(domainData, null, 2)}

Provide:
1. Overall health status
2. Critical issues (if any)
3. Top 3 recommendations
4. Security posture`;

  const response = await callAIGateway(prompt, 'claude');
  
  if (response) {
    console.log('\n📋 AI-Generated Summary:');
    console.log('─'.repeat(60));
    console.log(response.result);
    console.log('─'.repeat(60));
  }
  
  return response;
}

/**
 * Generate email content for notifications
 */
async function generateEmailContent(subject, context) {
  const prompt = `Write a professional email with the following:
Subject: ${subject}

Context: ${context}

Requirements:
- Professional tone
- Clear and concise
- Action items if applicable
- Appropriate greeting and signature for business email`;

  const response = await callAIGateway(prompt, 'claude');
  
  if (response) {
    console.log('\n📧 Generated Email:');
    console.log('─'.repeat(60));
    console.log(response.result);
    console.log('─'.repeat(60));
  }
  
  return response;
}

/**
 * Analyze monitoring alerts and suggest actions
 */
async function analyzeMonitoringAlerts(alerts) {
  const prompt = `Analyze these monitoring alerts and provide actionable recommendations:

${JSON.stringify(alerts, null, 2)}

Provide:
1. Severity assessment
2. Root cause analysis
3. Immediate actions needed
4. Prevention recommendations`;

  const response = await callAIGateway(prompt, 'claude');
  
  if (response) {
    console.log('\n🔍 Alert Analysis:');
    console.log('─'.repeat(60));
    console.log(response.result);
    console.log('─'.repeat(60));
  }
  
  return response;
}

/**
 * Generate code for automation tasks
 */
async function generateAutomationCode(task) {
  const prompt = `Generate Python code for the following automation task:

${task}

Requirements:
- Production-ready code
- Error handling
- Comments
- Follow best practices`;

  const response = await callAIGateway(prompt, 'claude');
  
  if (response) {
    console.log('\n💻 Generated Code:');
    console.log('─'.repeat(60));
    console.log(response.result);
    console.log('─'.repeat(60));
  }
  
  return response;
}

// ==================== EXAMPLE USAGE ====================

async function main() {
  console.log('========================================');
  console.log('🚀 NOIZYLAB AI GATEWAY - CLIENT DEMO');
  console.log('========================================');
  
  // Example 1: Domain summary
  const domainData = {
    domain: 'noizylab.ca',
    health_score: 85,
    issues: ['DKIM not configured', 'SSL expires in 45 days'],
    emails: ['rsp@noizylab.ca', 'help@noizylab.ca', 'hello@noizylab.ca']
  };
  
  console.log('\n📊 Example 1: Generate Domain Summary');
  await generateDomainEmailSummary(domainData);
  
  // Example 2: Email content generation
  console.log('\n\n📧 Example 2: Generate Email Content');
  await generateEmailContent(
    'Weekly Domain Health Report',
    'Our domain fishmusicinc.com had 99.8% uptime this week with no critical issues'
  );
  
  // Example 3: Alert analysis
  console.log('\n\n🚨 Example 3: Analyze Monitoring Alerts');
  const alerts = [
    { type: 'SSL', domain: 'fishmusicinc.com', message: 'Certificate expires in 25 days' },
    { type: 'DNS', domain: 'noizylab.ca', message: 'Slow DNS response (500ms)' }
  ];
  await analyzeMonitoringAlerts(alerts);
  
  console.log('\n========================================');
  console.log('✅ AI Gateway Demo Complete!');
  console.log('========================================');
}

// Run if executed directly
if (require.main === module) {
  main().catch(console.error);
}

// Export functions for use in other scripts
module.exports = {
  callAIGateway,
  generateDomainEmailSummary,
  generateEmailContent,
  analyzeMonitoringAlerts,
  generateAutomationCode
};

