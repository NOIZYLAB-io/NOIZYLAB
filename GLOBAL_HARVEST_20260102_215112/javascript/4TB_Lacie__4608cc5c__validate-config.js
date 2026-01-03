#!/usr/bin/env node

require('dotenv').config();
const fs = require('fs');
const path = require('path');

console.log('Validating email configuration...\n');

let hasErrors = false;

// Check required environment variables
const requiredVars = [
  'EMAIL_PROVIDER',
  'EMAIL_FROM_NAME',
  'EMAIL_FROM_ADDRESS'
];

const providerVars = {
  gmail: ['GMAIL_USER', 'GMAIL_APP_PASSWORD'],
  office365: ['OFFICE365_USER', 'OFFICE365_PASSWORD'],
  custom: ['SMTP_HOST', 'SMTP_PORT', 'SMTP_USER', 'SMTP_PASSWORD']
};

console.log('Checking environment variables...');

requiredVars.forEach(varName => {
  if (!process.env[varName]) {
    console.error(`✗ Missing required variable: ${varName}`);
    hasErrors = true;
  } else {
    console.log(`✓ ${varName}`);
  }
});

const provider = process.env.EMAIL_PROVIDER || 'gmail';
if (providerVars[provider]) {
  console.log(`\nChecking ${provider} specific variables...`);
  providerVars[provider].forEach(varName => {
    if (!process.env[varName]) {
      console.error(`✗ Missing ${provider} variable: ${varName}`);
      hasErrors = true;
    } else {
      console.log(`✓ ${varName}`);
    }
  });
}

// Check config files
console.log('\nChecking configuration files...');

const configFiles = [
  'config/smtp.json',
  'config/imap.json',
  'config/email-rules.json'
];

configFiles.forEach(file => {
  const filePath = path.join(__dirname, '..', file);
  if (!fs.existsSync(filePath)) {
    console.error(`✗ Missing config file: ${file}`);
    hasErrors = true;
  } else {
    try {
      JSON.parse(fs.readFileSync(filePath, 'utf8'));
      console.log(`✓ ${file}`);
    } catch (error) {
      console.error(`✗ Invalid JSON in ${file}: ${error.message}`);
      hasErrors = true;
    }
  }
});

// Check templates
console.log('\nChecking email templates...');

const templates = [
  'welcome.html',
  'order-confirmation.html',
  'support-response.html',
  'password-reset.html',
  'newsletter.html'
];

templates.forEach(template => {
  const templatePath = path.join(__dirname, '..', 'templates', template);
  if (!fs.existsSync(templatePath)) {
    console.error(`✗ Missing template: ${template}`);
    hasErrors = true;
  } else {
    console.log(`✓ ${template}`);
  }
});

console.log('\n' + '='.repeat(50));

if (hasErrors) {
  console.error('\n✗ Configuration validation failed!');
  console.error('Please fix the errors above before proceeding.\n');
  process.exit(1);
} else {
  console.log('\n✓ Configuration validation passed!');
  console.log('All required files and settings are in place.\n');
  process.exit(0);
}
