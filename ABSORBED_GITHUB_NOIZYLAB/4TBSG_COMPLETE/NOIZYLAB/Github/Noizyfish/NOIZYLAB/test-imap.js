#!/usr/bin/env node

require('dotenv').config();
const Imap = require('imap');
const imapConfig = require('../config/imap.json');

console.log('Testing IMAP connection...\n');

const provider = process.env.EMAIL_PROVIDER || 'gmail';
const config = imapConfig.providers[provider];

if (!config) {
  console.error(`✗ Invalid email provider: ${provider}`);
  process.exit(1);
}

// Replace environment variables
const processedConfig = JSON.parse(
  JSON.stringify(config).replace(/\$\{(\w+)\}/g, (match, varName) => {
    return process.env[varName] || match;
  })
);

const imap = new Imap({
  user: processedConfig.auth.user,
  password: processedConfig.auth.pass,
  host: processedConfig.host,
  port: processedConfig.port,
  tls: processedConfig.secure,
  tlsOptions: { rejectUnauthorized: true }
});

imap.once('ready', () => {
  console.log('✓ IMAP connection established successfully!');
  
  imap.openBox('INBOX', true, (err, box) => {
    if (err) {
      console.error('✗ Error opening inbox:', err.message);
      imap.end();
      process.exit(1);
    }
    
    console.log(`✓ Inbox opened successfully`);
    console.log(`  Total messages: ${box.messages.total}`);
    console.log(`  Unread messages: ${box.messages.new}`);
    
    imap.end();
  });
});

imap.once('error', (err) => {
  console.error('✗ IMAP connection failed!');
  console.error('Error:', err.message);
  process.exit(1);
});

imap.once('end', () => {
  console.log('\n✓ IMAP connection test completed!');
  process.exit(0);
});

console.log('Connecting to IMAP server...');
imap.connect();
