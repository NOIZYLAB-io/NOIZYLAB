#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

console.log('🔨 Building VS Code Extension...');

// Ensure we're in the vscode directory
process.chdir(path.join(__dirname, '..'));

try {
    // Install dependencies
    console.log('📦 Installing dependencies...');
    execSync('npm install', { stdio: 'inherit' });

    // Compile TypeScript
    console.log('🔧 Compiling TypeScript...');
    execSync('npm run compile', { stdio: 'inherit' });

    // Install vsce if not present
    try {
        execSync('vsce --version', { stdio: 'pipe' });
    } catch {
        console.log('📦 Installing vsce...');
        execSync('npm install -g vsce', { stdio: 'inherit' });
    }

    // Package the extension
    console.log('📦 Packaging extension...');
    execSync('vsce package', { stdio: 'inherit' });

    // Find the generated .vsix file
    const files = fs.readdirSync('.');
    const vsixFile = files.find(file => file.endsWith('.vsix'));

    if (vsixFile) {
        console.log(`✅ Extension packaged successfully: ${vsixFile}`);
        console.log('');
        console.log('🚀 Next steps:');
        console.log('1. Test locally: code --install-extension ' + vsixFile);
        console.log('2. Publish: vsce publish');
        console.log('3. Or upload to VS Code Marketplace manually');
    } else {
        console.error('❌ No .vsix file found');
        process.exit(1);
    }

} catch (error) {
    console.error('❌ Build failed:', error.message);
    process.exit(1);
}