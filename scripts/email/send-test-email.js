#!/usr/bin/env node

require('dotenv').config();
const { sendEmail } = require('../index');

const testEmail = process.argv[2] || process.env.GMAIL_USER || process.env.OFFICE365_USER;

if (!testEmail) {
  console.error('Please provide a test email address:');
  console.error('  npm run test:send your-email@example.com');
  process.exit(1);
}

console.log('Sending test email...\n');
console.log(`To: ${testEmail}`);
console.log('Template: welcome\n');

const testData = {
  to: testEmail,
  template: 'welcome',
  subject: 'Test Email - Welcome to Fish Music Inc! 🎵',
  variables: {
    firstName: 'Test User',
    dashboardUrl: 'https://fishmusicinc.com/dashboard',
    facebookUrl: 'https://facebook.com/fishmusicinc',
    twitterUrl: 'https://twitter.com/fishmusicinc',
    instagramUrl: 'https://instagram.com/fishmusicinc',
    linkedinUrl: 'https://linkedin.com/company/fishmusicinc',
    unsubscribeUrl: 'https://fishmusicinc.com/unsubscribe',
    preferencesUrl: 'https://fishmusicinc.com/preferences',
    privacyUrl: 'https://fishmusicinc.com/privacy'
  }
};

sendEmail(testData)
  .then((result) => {
    if (result.sent === false) {
      console.log('✓ Test email prepared (not sent - EMAIL_ENABLED=false)');
      console.log('\nPreview:', JSON.stringify(result.preview, null, 2));
    } else {
      console.log('✓ Test email sent successfully!');
      console.log(`Message ID: ${result.messageId}`);
      console.log('\nCheck your inbox for the test email.');
    }
    process.exit(0);
  })
  .catch((error) => {
    console.error('✗ Failed to send test email!');
    console.error('Error:', error.message);
    process.exit(1);
  });
