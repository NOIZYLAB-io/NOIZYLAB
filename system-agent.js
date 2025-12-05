/**
 * NoizyLab System Agent
 * Handles agent-based tasks using Claude API
 */

import { readFileSync, existsSync, statSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import { execSync } from 'child_process';
import os, { homedir } from 'os';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const AGENTS = {
  LUCY: {
    name: 'LUCY',
    description: 'System Health & Analysis Agent',
    model: 'claude-3-5-sonnet-20241022',
    capabilities: [
      'system_health',
      'file_analysis',
      'workspace_status',
      'performance_metrics',
      'diagnostics'
    ]
  },
  // Add more agents here
};

export class SystemAgent {
  constructor(agentName, apiKey) {
    this.agentName = agentName.toUpperCase();
    this.agent = AGENTS[this.agentName];
    this.apiKey = apiKey;
    
    if (!this.agent) {
      throw new Error(`Unknown agent: ${agentName}. Available: ${Object.keys(AGENTS).join(', ')}`);
    }
  }

  async execute(task) {
    console.log(`\n🤖 Agent ${this.agent.name} executing: "${task}"\n`);

    // Route to appropriate handler
    if (task.toLowerCase().includes('system health') || task.toLowerCase().includes('analyze system')) {
      return await this.analyzeSystemHealth();
    } else if (task.toLowerCase().includes('workspace') || task.toLowerCase().includes('status')) {
      return await this.analyzeWorkspace();
    } else {
      // Generic task - use Claude API
      return await this.handleGenericTask(task);
    }
  }

  async analyzeSystemHealth() {
    console.log('📊 Collecting system health data...\n');

    const healthData = {
      timestamp: new Date().toISOString(),
      system: {
        platform: os.platform(),
        arch: os.arch(),
        hostname: os.hostname(),
        uptime: os.uptime(),
        loadavg: os.loadavg(),
        totalmem: os.totalmem(),
        freemem: os.freemem(),
        cpus: os.cpus().length,
      },
      noizylab: {
        workspace: this.getNoizyLabWorkspace(),
        config: this.getNoizyLabConfig(),
        directories: this.checkNoizyLabDirectories(),
        pythonScripts: this.checkPythonScripts(),
      },
      disk: {
        workspace: this.getDiskUsage(process.cwd()),
        noizylab: this.getDiskUsage(this.getNoizyLabPath()),
      }
    };

    // Display health report
    this.displayHealthReport(healthData);

    // If API key available, get AI analysis
    if (this.apiKey) {
      return await this.getAIAnalysis(healthData, 'system health analysis');
    }

    return healthData;
  }

  getNoizyLabWorkspace() {
    const workspacePath = join(homedir(), 'NOIZYLAB');
    return {
      path: workspacePath,
      exists: existsSync(workspacePath),
      configExists: existsSync(join(workspacePath, '.noizylabrc')),
      apiKeyExists: existsSync(join(workspacePath, '.noizylab_api_key')),
    };
  }

  getNoizyLabConfig() {
    try {
      const configPath = join(homedir(), 'NOIZYLAB', '.config', 'noizylab_config.json');
      if (existsSync(configPath)) {
        return JSON.parse(readFileSync(configPath, 'utf8'));
      }
    } catch (e) {
      // Ignore
    }
    return null;
  }

  checkNoizyLabDirectories() {
    const basePath = join(homedir(), 'NOIZYLAB');
    const dirs = ['Audio', 'Files', 'Projects', 'Media', '.config', '.data'];
    const status = {};

    dirs.forEach(dir => {
      const dirPath = join(basePath, dir);
      status[dir] = {
        exists: existsSync(dirPath),
        path: dirPath,
      };
      if (existsSync(dirPath)) {
        try {
          const stats = statSync(dirPath);
          status[dir].isDirectory = stats.isDirectory();
        } catch (e) {
          // Ignore
        }
      }
    });

    return status;
  }

  checkPythonScripts() {
    const scripts = [
      'master_control.py',
      'ai_enhanced_organizer.py',
      'disk_scanner.py',
      'downloads_scanner.py',
      'unified_config.py',
      'setup_noizylab_api.py',
    ];

    const status = {};
    scripts.forEach(script => {
      const scriptPath = join(process.cwd(), script);
      status[script] = {
        exists: existsSync(scriptPath),
        path: scriptPath,
      };
    });

    return status;
  }

  getDiskUsage(path) {
    try {
      if (!existsSync(path)) {
        return { exists: false };
      }
      const stats = statSync(path);
      return {
        exists: true,
        isDirectory: stats.isDirectory(),
        size: stats.size,
        modified: stats.mtime,
      };
    } catch (e) {
      return { error: e.message };
    }
  }

  getNoizyLabPath() {
    return join(homedir(), 'NOIZYLAB');
  }

  displayHealthReport(data) {
    console.log('═══════════════════════════════════════════════════════════');
    console.log('  SYSTEM HEALTH REPORT');
    console.log('═══════════════════════════════════════════════════════════\n');

    // System Info
    console.log('🖥️  SYSTEM INFORMATION');
    console.log(`   Platform: ${data.system.platform} (${data.system.arch})`);
    console.log(`   Hostname: ${data.system.hostname}`);
    console.log(`   CPUs: ${data.system.cpus}`);
    console.log(`   Memory: ${(data.system.totalmem / 1024 / 1024 / 1024).toFixed(2)} GB total, ${(data.system.freemem / 1024 / 1024 / 1024).toFixed(2)} GB free`);
    console.log(`   Uptime: ${(data.system.uptime / 3600).toFixed(2)} hours`);
    console.log(`   Load Average: ${data.system.loadavg.map(l => l.toFixed(2)).join(', ')}\n`);

    // NoizyLab Status
    console.log('📁 NOIZYLAB WORKSPACE');
    const workspace = data.noizylab.workspace;
    console.log(`   Path: ${workspace.path}`);
    console.log(`   Exists: ${workspace.exists ? '✅' : '❌'}`);
    console.log(`   Config: ${workspace.configExists ? '✅' : '❌'}`);
    console.log(`   API Key: ${workspace.apiKeyExists ? '✅' : '❌'}\n`);

    // Directories
    console.log('📂 NOIZYLAB DIRECTORIES');
    Object.entries(data.noizylab.directories).forEach(([name, info]) => {
      const status = info.exists ? '✅' : '❌';
      console.log(`   ${status} ${name}`);
    });
    console.log('');

    // Python Scripts
    console.log('🐍 PYTHON SCRIPTS');
    const scripts = data.noizylab.pythonScripts;
    const existing = Object.entries(scripts).filter(([_, info]) => info.exists);
    const missing = Object.entries(scripts).filter(([_, info]) => !info.exists);
    
    existing.forEach(([name, _]) => {
      console.log(`   ✅ ${name}`);
    });
    if (missing.length > 0) {
      missing.forEach(([name, _]) => {
        console.log(`   ❌ ${name}`);
      });
    }
    console.log('');

    // Health Score
    const healthScore = this.calculateHealthScore(data);
    console.log('═══════════════════════════════════════════════════════════');
    console.log(`   HEALTH SCORE: ${healthScore.score}/100 ${healthScore.emoji}`);
    console.log('═══════════════════════════════════════════════════════════\n');
  }

  calculateHealthScore(data) {
    let score = 0;
    let maxScore = 0;

    // Workspace exists (20 points)
    maxScore += 20;
    if (data.noizylab.workspace.exists) score += 20;

    // Config exists (15 points)
    maxScore += 15;
    if (data.noizylab.workspace.configExists) score += 15;

    // API Key exists (15 points)
    maxScore += 15;
    if (data.noizylab.workspace.apiKeyExists) score += 15;

    // Directories exist (30 points)
    maxScore += 30;
    const dirCount = Object.values(data.noizylab.directories).filter(d => d.exists).length;
    score += (dirCount / Object.keys(data.noizylab.directories).length) * 30;

    // Python scripts exist (20 points)
    maxScore += 20;
    const scriptCount = Object.values(data.noizylab.pythonScripts).filter(s => s.exists).length;
    score += (scriptCount / Object.keys(data.noizylab.pythonScripts).length) * 20;

    const percentage = Math.round((score / maxScore) * 100);
    let emoji = '🔴';
    if (percentage >= 80) emoji = '🟢';
    else if (percentage >= 60) emoji = '🟡';
    else if (percentage >= 40) emoji = '🟠';

    return { score: percentage, emoji };
  }

  async getAIAnalysis(data, task) {
    if (!this.apiKey) {
      return { error: 'API key not available for AI analysis' };
    }

    try {
      console.log('🤖 Getting AI analysis from Claude...\n');
      
      const prompt = `You are ${this.agent.name}, a system health analysis agent for NoizyLab.

Task: ${task}

System Health Data:
${JSON.stringify(data, null, 2)}

Please provide:
1. A summary of the system health status
2. Any issues or concerns identified
3. Recommendations for improvement
4. Priority actions if needed

Format your response clearly with sections.`;

      // Call Claude API
      const response = await this.callClaudeAPI(prompt);
      
      console.log('═══════════════════════════════════════════════════════════');
      console.log('  AI ANALYSIS');
      console.log('═══════════════════════════════════════════════════════════\n');
      console.log(response);
      console.log('\n═══════════════════════════════════════════════════════════\n');

      return { data, analysis: response };
    } catch (error) {
      console.error(`❌ Error getting AI analysis: ${error.message}`);
      return { data, error: error.message };
    }
  }

  async callClaudeAPI(prompt) {
    // Use Python script to call Claude API (since we have Python integration)
    try {
      const pythonScript = `
import sys
import json
import os
from pathlib import Path

sys.path.insert(0, str(Path.home() / 'NOIZYLAB'))
try:
    from claude_integration import get_api_key
    api_key = get_api_key()
except:
    api_key = os.environ.get('ANTHROPIC_API_KEY') or os.environ.get('NOIZYLAB_API_KEY')

if not api_key:
    print(json.dumps({"error": "No API key found"}))
    sys.exit(1)

try:
    import anthropic
    client = anthropic.Anthropic(api_key=api_key)
    
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=2000,
        messages=[{
            "role": "user",
            "content": ${JSON.stringify(prompt)}
        }]
    )
    
    print(message.content[0].text)
except Exception as e:
    print(json.dumps({"error": str(e)}))
`;

      const result = execSync(`python3 -c ${JSON.stringify(pythonScript)}`, {
        encoding: 'utf8',
        maxBuffer: 10 * 1024 * 1024,
      });

      return result.trim();
    } catch (error) {
      // Fallback: return error message
      return `Error calling Claude API: ${error.message}. Make sure anthropic package is installed: pip install anthropic`;
    }
  }

  async analyzeWorkspace() {
    // Similar to system health but focused on workspace
    return await this.analyzeSystemHealth();
  }

  async handleGenericTask(task) {
    console.log(`🤖 Processing task with ${this.agent.name}...\n`);
    
    if (this.apiKey) {
      return await this.getAIAnalysis({ task }, task);
    } else {
      console.log('⚠️  API key not available. Install and configure:');
      console.log('   python3 setup_noizylab_api.py\n');
      return { task, error: 'API key not configured' };
    }
  }
}

