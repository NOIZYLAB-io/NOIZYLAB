#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

console.log('🚀 Publishing to VS Code Marketplace...');

// Ensure we're in the vscode directory
process.chdir(path.join(__dirname, '..'));

try {
    // Check if we have a personal access token
    const token = process.env.VSCE_PAT;
    if (!token) {
        console.log('❌ VSCE_PAT environment variable not set');
        console.log('');
        console.log('To publish to VS Code Marketplace:');
        console.log('1. Create a Personal Access Token at:');
        console.log('   https://dev.azure.com/[your-org]/_usersSettings/tokens');
        console.log('2. Set environment variable: set VSCE_PAT=your-token');
        console.log('3. Run this script again');
        console.log('');
        console.log('Or publish manually:');
        console.log('1. Build: npm run package');
        console.log('2. Upload .vsix file to: https://marketplace.visualstudio.com/manage');
        process.exit(1);
    }

    // Build first
    console.log('🔨 Building extension...');
    execSync('node scripts/build-vscode.js', { stdio: 'inherit' });

    // Publish
    console.log('📤 Publishing to marketplace...');
    execSync('vsce publish', { stdio: 'inherit' });

    console.log('✅ Extension published successfully!');
    console.log('🎉 Your extension is now available on the VS Code Marketplace');

} catch (error) {
    console.error('❌ Publish failed:', error.message);
    console.log('');
    console.log('Manual publishing steps:');
    console.log('1. Visit: https://marketplace.visualstudio.com/manage');
    console.log('2. Sign in with your Microsoft account');
    console.log('3. Create a publisher if you don\'t have one');
    console.log('4. Upload your .vsix file');
    process.exit(1);
}