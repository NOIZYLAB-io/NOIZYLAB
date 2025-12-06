#!/usr/bin/env node

require('dotenv').config();
const { verifyConnection } = require('../index');

console.log('Testing SMTP connection...\n');

verifyConnection()
  .then(() => {
    console.log('\n✓ SMTP connection test passed!');
    process.exit(0);
  })
  .catch((error) => {
    console.error('\n✗ SMTP connection test failed!');
    console.error('Error:', error.message);
    process.exit(1);
  });
