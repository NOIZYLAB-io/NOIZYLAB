#!/usr/bin/env node

/**
 * 🟣 GABRIEL OS CLI — Local-First Command Interface
 * 
 * All operations run locally in /Users/m2ultra/NOIZYLAB
 */

import { Gabriel } from './gabriel/index.js';
import fs from 'fs';
import path from 'path';

const ROOT = '/Users/m2ultra/NOIZYLAB';

const help = `
🟣 GABRIEL OS v1.0 CLI — Local Operations

Usage: node gabriel-cli.mjs <command> [options]

Commands:
  scan [path]              Scan directory for files
  heal [path]              Auto-fix codebase issues
  organize [path]          Organize files by type
  workflow                 Run complete workflow (scan → heal → organize)
  daemon [interval]        Start daemon mode
  status                   Show system status
  cleanup                  Delete empty folders
  cleanup:find             Find empty folders (dry run)

Examples:
  node gabriel-cli.mjs scan
  node gabriel-cli.mjs scan "/Volumes/4TB Blue Fish"
  node gabriel-cli.mjs heal
  node gabriel-cli.mjs workflow
  node gabriel-cli.mjs daemon 60000

Default path: ${ROOT}
`;

const args = process.argv.slice(2);
const cmd = args[0];
const pathArg = args[1] || ROOT;

async function main() {
  if (!cmd) {
    console.log(help);
    process.exit(0);
  }

  try {
    switch (cmd) {
      case 'scan':
        await handleScan(pathArg);
        break;
      
      case 'heal':
        await handleHeal(pathArg);
        break;
      
      case 'organize':
        await handleOrganize(pathArg);
        break;
      
      case 'workflow':
        await handleWorkflow(pathArg);
        break;
      
      case 'daemon':
        await handleDaemon(pathArg, parseInt(args[1] || 60000));
        break;
      
      case 'status':
        await handleStatus(pathArg);
        break;
      
      case 'cleanup':
        await handleCleanup(pathArg, false);
        break;
      
      case 'cleanup:find':
        await handleCleanup(pathArg, true);
        break;
      
      default:
        console.log(help);
        process.exit(1);
    }
  } catch (error) {
    console.error('❌ Error:', error.message);
    process.exit(1);
  }
}

async function handleScan(dirPath) {
  console.log('🟣 GABRIEL SCANNER');
  console.log('='.repeat(60));
  console.log(`📂 Scanning: ${dirPath}\n`);

  if (!fs.existsSync(dirPath)) {
    console.error(`❌ Path not found: ${dirPath}`);
    process.exit(1);
  }

  const gabriel = new Gabriel(dirPath);
  const startTime = Date.now();

  const files = await gabriel.scan();
  const duration = Date.now() - startTime;
  const stats = gabriel.getScanStats();

  console.log('✅ Scan Complete!');
  console.log('='.repeat(60));
  console.log(`📊 Statistics:`);
  console.log(`   Files: ${stats.files.toLocaleString()}`);
  console.log(`   Directories: ${stats.directories.toLocaleString()}`);
  console.log(`   Total indexed: ${stats.indexed.toLocaleString()}`);
  console.log(`   Duration: ${(duration / 1000).toFixed(2)}s`);

  if (stats.byClassification) {
    console.log('\n📁 Files by Classification:');
    Object.entries(stats.byClassification)
      .sort((a, b) => b[1] - a[1])
      .forEach(([type, count]) => {
        console.log(`   ${type.padEnd(15)}: ${count.toLocaleString()}`);
      });
  }

  // Save results
  const outputPath = path.join(ROOT, `scan-${Date.now()}.json`);
  fs.writeFileSync(outputPath, JSON.stringify({
    path: dirPath,
    timestamp: new Date().toISOString(),
    stats,
    files: files.slice(0, 1000) // Limit to first 1000 for file size
  }, null, 2));
  console.log(`\n💾 Results saved: ${outputPath}`);
}

async function handleHeal(dirPath) {
  console.log('🟣 GABRIEL HEALER');
  console.log('='.repeat(60));
  console.log(`🔧 Healing: ${dirPath}\n`);

  if (!fs.existsSync(dirPath)) {
    console.error(`❌ Path not found: ${dirPath}`);
    process.exit(1);
  }

  const gabriel = new Gabriel(dirPath, {
    healer: {
      autoFix: true,
      backup: true
    }
  });

  const report = await gabriel.heal();
  const summary = report.summary || {};

  console.log('✅ Healing Complete!');
  console.log('='.repeat(60));
  console.log(`📊 Results:`);
  console.log(`   Issues found: ${summary.totalIssues || 0}`);
  console.log(`   Fixed: ${summary.fixed || 0}`);
  console.log(`   Errors: ${summary.errors || 0}`);
  console.log(`   Backups: ${summary.backups || 0}`);
  console.log(`   Duration: ${report.duration || 0}ms`);

  if (summary.byType) {
    console.log('\n🔧 Fixed by Type:');
    Object.entries(summary.byType).forEach(([type, count]) => {
      console.log(`   ${type.padEnd(20)}: ${count}`);
    });
  }
}

async function handleOrganize(dirPath) {
  console.log('🟣 GABRIEL ORGANIZER');
  console.log('='.repeat(60));
  console.log(`📁 Organizing: ${dirPath}\n`);

  if (!fs.existsSync(dirPath)) {
    console.error(`❌ Path not found: ${dirPath}`);
    process.exit(1);
  }

  const gabriel = new Gabriel(dirPath);
  
  // Scan first
  console.log('📂 Scanning files...');
  const files = await gabriel.scan();
  console.log(`   Found ${files.length} files`);

  // Organize
  console.log('\n📁 Organizing...');
  const results = gabriel.organize(files);
  const report = gabriel.getOrgReport();

  console.log('✅ Organization Complete!');
  console.log('='.repeat(60));
  console.log(`📊 Results:`);
  console.log(`   Organized: ${report.summary?.organized || 0}`);
  console.log(`   Skipped: ${report.summary?.skipped || 0}`);
  console.log(`   Errors: ${report.summary?.errors || 0}`);
}

async function handleWorkflow(dirPath) {
  console.log('🟣 GABRIEL OS - Complete Workflow');
  console.log('='.repeat(60));
  console.log(`📂 Working on: ${dirPath}\n`);

  if (!fs.existsSync(dirPath)) {
    console.error(`❌ Path not found: ${dirPath}`);
    process.exit(1);
  }

  const gabriel = new Gabriel(dirPath);
  const results = await gabriel.workflow();

  console.log('\n✅ Workflow Complete!');
  console.log('='.repeat(60));
  console.log(`📊 Summary:`);
  console.log(`   Files scanned: ${results.scan?.length || 0}`);
  console.log(`   Issues fixed: ${results.heal?.fixed || 0}`);
  console.log(`   Files organized: ${results.organize?.filter(r => r.success).length || 0}`);
}

async function handleDaemon(dirPath, interval) {
  console.log('🟣 GABRIEL DAEMON - Starting...');
  console.log('='.repeat(60));
  console.log(`📂 Root: ${dirPath}`);
  console.log(`⏰ Interval: ${interval}ms (${interval / 1000}s)\n`);

  if (!fs.existsSync(dirPath)) {
    console.error(`❌ Path not found: ${dirPath}`);
    process.exit(1);
  }

  const gabriel = new Gabriel(dirPath);

  // Handle graceful shutdown
  process.on('SIGINT', () => {
    console.log('\n\n🛑 Shutting down daemon...');
    gabriel.stop();
    process.exit(0);
  });

  process.on('SIGTERM', () => {
    console.log('\n\n🛑 Shutting down daemon...');
    gabriel.stop();
    process.exit(0);
  });

  gabriel.start(interval);
}

async function handleStatus(dirPath) {
  const gabriel = new Gabriel(dirPath);
  const status = gabriel.getSystemStatus();

  console.log('🟣 GABRIEL OS - System Status');
  console.log('='.repeat(60));
  console.log(`📂 Root: ${status.root}`);
  console.log(`⏰ Timestamp: ${new Date(status.timestamp).toLocaleString()}`);
  
  if (status.daemon) {
    console.log(`\n🔄 Daemon:`);
    console.log(`   Running: ${status.daemon.running ? 'Yes' : 'No'}`);
    console.log(`   Cycles: ${status.daemon.cycleCount || 0}`);
    if (status.daemon.stats?.uptime) {
      console.log(`   Uptime: ${Math.floor(status.daemon.stats.uptime / 1000)}s`);
    }
  }

  if (status.pipeline) {
    console.log(`\n🧩 Pipeline:`);
    console.log(`   Total events: ${status.pipeline.total || 0}`);
    console.log(`   Success rate: ${(status.pipeline.successRate * 100).toFixed(1)}%`);
  }
}

async function handleCleanup(dirPath, dryRun = false) {
  const { GabrielCleanup } = await import('./gabriel/cleanup/index.js');
  
  const cleanup = new GabrielCleanup(dirPath, {
    dryRun,
    excludePatterns: [
      'node_modules',
      '.git',
      '.DS_Store',
      'dist',
      'build',
      '.gabriel'
    ]
  });

  const report = await cleanup.deleteEmptyFolders();

  if (dryRun) {
    console.log(`\n🔍 Found ${report.empty.length} empty folders (DRY RUN)`);
    if (report.empty.length > 0) {
      console.log('\nEmpty folders:');
      report.empty.slice(0, 20).forEach(folder => {
        console.log(`   ${folder}`);
      });
      if (report.empty.length > 20) {
        console.log(`   ... and ${report.empty.length - 20} more`);
      }
      console.log(`\nTo delete them, run: node gabriel-cli.mjs cleanup`);
    }
  }
}

main().catch(console.error);

