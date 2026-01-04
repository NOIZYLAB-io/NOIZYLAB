/**
 * NOIZYLAB AI Copilot - Slack Bot
 * 
 * AI-powered disk repair & monitoring bot for MC96 Digi Universe
 * Integrates with TechTool Pro 21, DiskWarrior, and NOIZYLAB scripts
 * 
 * @author Gabriel Almeida
 * @version 1.0.0
 */

const { App } = require('@slack/bolt');
const { exec } = require('child_process');
const { promisify } = require('util');
const execAsync = promisify(exec);
require('dotenv').config();

// Initialize Slack app
const app = new App({
  token: process.env.SLACK_BOT_TOKEN,
  signingSecret: process.env.SLACK_SIGNING_SECRET,
  socketMode: true, // Use WebSocket mode (no public endpoint needed!)
  appToken: process.env.SLACK_APP_TOKEN,
  port: process.env.PORT || 3000
});

// Script paths from environment
const SCRIPTS = {
  ttp21: process.env.TTP21_SCRIPT || '~/NOIZYLAB/TTP21_HOT_ROD_GUIDE.sh',
  status: process.env.STATUS_SCRIPT || '~/NOIZYLAB/QUICK_STATUS.sh',
  cleanup: process.env.CLEANUP_SCRIPT || '~/NOIZYLAB/ULTRA_AGGRESSIVE.sh',
  diskwarrior: process.env.DISKWARRIOR_SCRIPT || '~/NOIZYLAB/DISKWARRIOR_EMERGENCY_GUIDE.sh'
};

// Security: Check if user is authorized
function isAuthorized(userId, requireAdmin = false) {
  const allowedUsers = process.env.ALLOWED_USERS?.split(',') || [];
  const adminUsers = process.env.ADMIN_USERS?.split(',') || [];
  
  if (requireAdmin) {
    return adminUsers.includes(userId);
  }
  
  return allowedUsers.includes(userId) || adminUsers.includes(userId);
}

// Execute shell script and return output
async function runScript(scriptPath, args = '') {
  try {
    const { stdout, stderr } = await execAsync(`bash ${scriptPath} ${args}`);
    return { success: true, output: stdout, error: stderr };
  } catch (error) {
    return { success: false, output: '', error: error.message };
  }
}

// Format output for Slack (truncate if too long)
function formatOutput(output, maxLength = 2000) {
  if (!output) return '_No output_';
  
  if (output.length > maxLength) {
    return output.substring(0, maxLength) + '\n\n_...output truncated..._';
  }
  
  return output;
}

// ===========================
// SLASH COMMANDS
// ===========================

/**
 * /disk-status
 * Quick health check of all drives
 */
app.command('/disk-status', async ({ command, ack, say, client }) => {
  await ack();
  
  if (!isAuthorized(command.user_id)) {
    await say('❌ Unauthorized. Contact admin for access.');
    return;
  }
  
  await say('📊 *Running disk status check...*\n⏱️ This may take a few seconds...');
  
  const result = await runScript(SCRIPTS.status);
  
  if (result.success) {
    await say({
      text: '✅ Disk Status Report',
      blocks: [
        {
          type: 'header',
          text: {
            type: 'plain_text',
            text: '📊 Disk Status Report'
          }
        },
        {
          type: 'section',
          text: {
            type: 'mrkdwn',
            text: `\`\`\`${formatOutput(result.output)}\`\`\``
          }
        }
      ]
    });
  } else {
    await say(`❌ *Status check failed:*\n\`\`\`${result.error}\`\`\``);
  }
});

/**
 * /noizylab-repair [volume]
 * Run TechTool Pro 21 hot rod repair on specified volume
 */
app.command('/noizylab-repair', async ({ command, ack, say }) => {
  await ack();
  
  if (!isAuthorized(command.user_id, true)) {
    await say('❌ Admin access required for repair operations.');
    return;
  }
  
  const volume = command.text.trim() || 'all';
  
  await say({
    text: '🔧 Starting disk repair...',
    blocks: [
      {
        type: 'header',
        text: {
          type: 'plain_text',
          text: '🔧 TechTool Pro 21 Hot Rod Repair'
        }
      },
      {
        type: 'section',
        text: {
          type: 'mrkdwn',
          text: `*Target:* \`${volume}\`\n*Status:* Running pre-flight optimization...\n⏱️ Estimated time: 1-3.5 hours (6-10x faster with hot rod mode)`
        }
      }
    ]
  });
  
  const result = await runScript(SCRIPTS.ttp21, volume);
  
  if (result.success) {
    await say({
      text: '✅ Repair Complete',
      blocks: [
        {
          type: 'header',
          text: {
            type: 'plain_text',
            text: '✅ Repair Complete!'
          }
        },
        {
          type: 'section',
          text: {
            type: 'mrkdwn',
            text: `*Volume:* \`${volume}\`\n*Result:*\n\`\`\`${formatOutput(result.output, 1500)}\`\`\``
          }
        }
      ]
    });
  } else {
    await say(`❌ *Repair failed:*\n\`\`\`${result.error}\`\`\`\n\n💡 *Try:* \`/diskwarrior-emergency\` for alternative repair algorithm`);
  }
});

/**
 * /cleanup-all
 * Run aggressive cleanup (empty folders, caches, etc.)
 */
app.command('/cleanup-all', async ({ command, ack, say }) => {
  await ack();
  
  if (!isAuthorized(command.user_id, true)) {
    await say('❌ Admin access required for cleanup operations.');
    return;
  }
  
  await say({
    text: '🧹 Starting aggressive cleanup...',
    blocks: [
      {
        type: 'header',
        text: {
          type: 'plain_text',
          text: '🧹 Ultra Aggressive Cleanup'
        }
      },
      {
        type: 'section',
        text: {
          type: 'mrkdwn',
          text: '⚠️ *Warning:* This will delete:\n• Empty folders\n• Duplicate archives\n• Cache files\n• Temporary data\n\n⏱️ Running cleanup scripts...'
        }
      }
    ]
  });
  
  const result = await runScript(SCRIPTS.cleanup);
  
  if (result.success) {
    await say({
      text: '✅ Cleanup Complete',
      blocks: [
        {
          type: 'header',
          text: {
            type: 'plain_text',
            text: '✅ Cleanup Complete!'
          }
        },
        {
          type: 'section',
          text: {
            type: 'mrkdwn',
            text: `*Results:*\n\`\`\`${formatOutput(result.output)}\`\`\``
          }
        }
      ]
    });
  } else {
    await say(`❌ *Cleanup failed:*\n\`\`\`${result.error}\`\`\``);
  }
});

/**
 * /diskwarrior-emergency
 * Run DiskWarrior emergency repair (when TTP21 fails)
 */
app.command('/diskwarrior-emergency', async ({ command, ack, say }) => {
  await ack();
  
  if (!isAuthorized(command.user_id, true)) {
    await say('❌ Admin access required for emergency repair.');
    return;
  }
  
  await say({
    text: '🚨 DiskWarrior Emergency Repair',
    blocks: [
      {
        type: 'header',
        text: {
          type: 'plain_text',
          text: '🚨 DiskWarrior Emergency Repair'
        }
      },
      {
        type: 'section',
        text: {
          type: 'mrkdwn',
          text: '⚠️ *This is the backup repair algorithm*\n\nUse when TechTool Pro 21 fails or for severe directory corruption.\n\n📋 Starting DiskWarrior emergency workflow...'
        }
      }
    ]
  });
  
  const result = await runScript(SCRIPTS.diskwarrior);
  
  if (result.success) {
    await say({
      text: '✅ Emergency Repair Guide',
      blocks: [
        {
          type: 'section',
          text: {
            type: 'mrkdwn',
            text: `\`\`\`${formatOutput(result.output)}\`\`\``
          }
        }
      ]
    });
  } else {
    await say(`❌ *Guide failed to load:*\n\`\`\`${result.error}\`\`\``);
  }
});

// ===========================
// NATURAL LANGUAGE INTERFACE
// ===========================

/**
 * @noizylab mentions - Natural language AI interface
 */
app.event('app_mention', async ({ event, say, client }) => {
  const text = event.text.toLowerCase();
  const userId = event.user;
  
  if (!isAuthorized(userId)) {
    await say('❌ Unauthorized. Contact admin for access.');
    return;
  }
  
  // Simple keyword matching (upgrade to GPT-4 later)
  if (text.includes('slow') || text.includes('frozen') || text.includes('stuck')) {
    await say({
      text: 'Disk performance issue detected',
      blocks: [
        {
          type: 'section',
          text: {
            type: 'mrkdwn',
            text: '🔍 *I detected a disk performance issue!*\n\nI recommend:\n1️⃣ Run `/disk-status` to diagnose\n2️⃣ Use `/noizylab-repair <volume>` for hot rod repair\n3️⃣ If TTP21 fails, try `/diskwarrior-emergency`'
          }
        }
      ]
    });
  } else if (text.includes('status') || text.includes('health') || text.includes('check')) {
    await say('📊 Running disk status check...');
    const result = await runScript(SCRIPTS.status);
    await say(`\`\`\`${formatOutput(result.output)}\`\`\``);
  } else if (text.includes('space') || text.includes('full') || text.includes('capacity')) {
    await say('💾 Checking storage capacity...');
    const result = await runScript(SCRIPTS.status);
    await say(`\`\`\`${formatOutput(result.output)}\`\`\``);
  } else if (text.includes('help')) {
    await say({
      text: 'NOIZYLAB AI Help',
      blocks: [
        {
          type: 'header',
          text: {
            type: 'plain_text',
            text: '🤖 NOIZYLAB AI Copilot - Commands'
          }
        },
        {
          type: 'section',
          text: {
            type: 'mrkdwn',
            text: '*Available Commands:*\n\n`/disk-status` - Quick health check\n`/noizylab-repair <volume>` - TTP21 hot rod repair\n`/cleanup-all` - Aggressive cleanup\n`/diskwarrior-emergency` - Backup repair algorithm\n\n*Natural Language:*\nJust mention `@noizylab` and describe your issue!'
          }
        }
      ]
    });
  } else {
    await say({
      text: 'Hello!',
      blocks: [
        {
          type: 'section',
          text: {
            type: 'mrkdwn',
            text: '👋 Hey! I\'m the NOIZYLAB AI Copilot.\n\nI can help with:\n• Disk repair & optimization\n• Storage health monitoring\n• System cleanup\n\nTry saying:\n• "My 12TB drive is frozen"\n• "Check disk status"\n• "How much space left?"\n\nOr use `/disk-status` for a quick check!'
          }
        }
      ]
    });
  }
});

// ===========================
// PROACTIVE MONITORING
// ===========================

/**
 * Daily health report (runs at 9am)
 */
async function sendDailyReport() {
  if (process.env.ENABLE_DAILY_REPORTS !== 'true') return;
  
  const channel = process.env.DAILY_REPORT_CHANNEL || '#disk-health';
  
  const result = await runScript(SCRIPTS.status);
  
  await app.client.chat.postMessage({
    channel: channel,
    text: 'Daily Disk Health Report',
    blocks: [
      {
        type: 'header',
        text: {
          type: 'plain_text',
          text: '📊 Daily Disk Health Report'
        }
      },
      {
        type: 'section',
        text: {
          type: 'mrkdwn',
          text: `*Date:* ${new Date().toLocaleDateString()}\n\n\`\`\`${formatOutput(result.output)}\`\`\``
        }
      }
    ]
  });
}

// Schedule daily reports (9am)
setInterval(() => {
  const now = new Date();
  if (now.getHours() === 9 && now.getMinutes() === 0) {
    sendDailyReport();
  }
}, 60000); // Check every minute

// ===========================
// START BOT
// ===========================

(async () => {
  try {
    await app.start();
    console.log('⚡️ NOIZYLAB AI Copilot is running!');
    console.log('🔧 TechTool Pro 21 integration: READY');
    console.log('💾 DiskWarrior emergency mode: READY');
    console.log('🧹 Cleanup automation: READY');
    console.log('📊 Health monitoring: ACTIVE');
    console.log('\n🎯 Meeting Phineas Potts Standard: MAGICAL! ✨');
  } catch (error) {
    console.error('❌ Failed to start bot:', error);
    process.exit(1);
  }
})();

// Graceful shutdown
process.on('SIGINT', async () => {
  console.log('\n👋 Shutting down NOIZYLAB AI Copilot...');
  await app.stop();
  process.exit(0);
});
