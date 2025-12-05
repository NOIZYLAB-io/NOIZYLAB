#!/usr/bin/env node

import { GabrielScanner } from './gabriel/scanner/index.js';
import fs from 'fs';
import path from 'path';

const DRIVE_PATH = '/Volumes/4TB Blue Fish';

console.log('🟣 GABRIEL SCANNER - 4TB Blue Fish Drive');
console.log('='.repeat(60));
console.log(`📂 Scanning: ${DRIVE_PATH}\n`);

// Check if drive is mounted
if (!fs.existsSync(DRIVE_PATH)) {
  console.error(`❌ Drive not found at: ${DRIVE_PATH}`);
  console.log('\nAvailable volumes:');
  const volumes = fs.readdirSync('/Volumes');
  volumes.forEach(vol => {
    if (vol.includes('Fish') || vol.includes('4TB')) {
      console.log(`  • /Volumes/${vol}`);
    }
  });
  process.exit(1);
}

// Create scanner with options for large drive
const scanner = new GabrielScanner(DRIVE_PATH, {
  includeHidden: false,
  excludePatterns: [
    '.DS_Store',
    '.Spotlight-V100',
    '.Trashes',
    '.fseventsd',
    '.TemporaryItems'
  ]
});

console.log('🔍 Starting scan...');
const startTime = Date.now();

try {
  const index = await scanner.scan();
  const duration = Date.now() - startTime;

  // Get statistics
  const stats = scanner.getStats();
  
  console.log('\n✅ Scan Complete!');
  console.log('='.repeat(60));
  console.log(`📊 Statistics:`);
  console.log(`   Files scanned: ${stats.indexed}`);
  console.log(`   Directories: ${stats.byType.directory || 0}`);
  console.log(`   Files: ${stats.byType.file || 0}`);
  console.log(`   Duration: ${(duration / 1000).toFixed(2)}s`);
  console.log(`   Errors: ${stats.errors || 0}`);

  console.log('\n📁 Files by Classification:');
  const byClassification = stats.byClassification || {};
  Object.entries(byClassification)
    .sort((a, b) => b[1] - a[1])
    .forEach(([type, count]) => {
      console.log(`   ${type.padEnd(15)}: ${count.toLocaleString()}`);
    });

  // Save scan results
  const outputPath = path.join(process.cwd(), '4tb-blue-fish-scan.json');
  fs.writeFileSync(outputPath, scanner.toJSON(), 'utf8');
  console.log(`\n💾 Results saved to: ${outputPath}`);

  // Summary by file type
  console.log('\n📋 Top File Extensions:');
  const extensions = {};
  index.filter(item => item.type === 'file' && item.extension).forEach(item => {
    extensions[item.extension] = (extensions[item.extension] || 0) + 1;
  });
  
  Object.entries(extensions)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 10)
    .forEach(([ext, count]) => {
      console.log(`   ${ext.padEnd(10)}: ${count.toLocaleString()}`);
    });

} catch (error) {
  console.error('\n❌ Scan Error:', error.message);
  process.exit(1);
}

