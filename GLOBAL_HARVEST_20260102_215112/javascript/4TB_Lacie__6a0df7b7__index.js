require('dotenv').config();
const nodemailer = require('nodemailer');
const fs = require('fs');
const path = require('path');
const Handlebars = require('handlebars');

// Load SMTP configuration
const smtpConfig = require('./config/smtp.json');

/**
 * Get SMTP configuration based on selected provider
 */
function getSMTPConfig() {
  const provider = process.env.EMAIL_PROVIDER || 'gmail';
  const config = smtpConfig.providers[provider];
  
  if (!config) {
    throw new Error(`Invalid email provider: ${provider}`);
  }
  
  // Replace environment variables in config
  const processedConfig = JSON.parse(
    JSON.stringify(config).replace(/\$\{(\w+)\}/g, (match, varName) => {
      return process.env[varName] || match;
    })
  );
  
  return processedConfig;
}

/**
 * Create nodemailer transporter
 */
function createTransporter() {
  const config = getSMTPConfig();
  return nodemailer.createTransport(config);
}

/**
 * Load and compile email template
 * @param {string} templateName - Name of the template file (without extension)
 * @param {object} variables - Template variables
 */
function loadTemplate(templateName, variables = {}) {
  const templatePath = path.join(__dirname, 'templates', `${templateName}.html`);
  
  if (!fs.existsSync(templatePath)) {
    throw new Error(`Template not found: ${templateName}`);
  }
  
  const templateContent = fs.readFileSync(templatePath, 'utf8');
  const template = Handlebars.compile(templateContent);
  
  return template(variables);
}

/**
 * Send email
 * @param {object} options - Email options
 * @param {string} options.to - Recipient email address
 * @param {string} options.subject - Email subject
 * @param {string} options.html - HTML content or template name
 * @param {object} options.variables - Template variables (if using template)
 * @param {string} options.from - Sender email (optional)
 * @param {string} options.replyTo - Reply-to email (optional)
 */
async function sendEmail(options) {
  if (!process.env.EMAIL_ENABLED || process.env.EMAIL_ENABLED === 'false') {
    console.log('Email sending is disabled. Set EMAIL_ENABLED=true in .env');
    return { preview: options, sent: false };
  }
  
  const transporter = createTransporter();
  
  // Load template if template name provided
  let html = options.html;
  if (options.template) {
    html = loadTemplate(options.template, options.variables || {});
  }
  
  const mailOptions = {
    from: options.from || `${process.env.EMAIL_FROM_NAME} <${process.env.EMAIL_FROM_ADDRESS}>`,
    to: options.to,
    subject: options.subject,
    html: html,
    replyTo: options.replyTo || process.env.EMAIL_REPLY_TO
  };
  
  try {
    const info = await transporter.sendMail(mailOptions);
    console.log('Email sent successfully:', info.messageId);
    return { success: true, messageId: info.messageId };
  } catch (error) {
    console.error('Error sending email:', error);
    throw error;
  }
}

/**
 * Verify SMTP connection
 */
async function verifyConnection() {
  const transporter = createTransporter();
  
  try {
    await transporter.verify();
    console.log('✓ SMTP connection verified successfully');
    return true;
  } catch (error) {
    console.error('✗ SMTP connection failed:', error.message);
    throw error;
  }
}

module.exports = {
  createTransporter,
  loadTemplate,
  sendEmail,
  verifyConnection,
  getSMTPConfig
};
