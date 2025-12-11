# API Documentation

## Email Sending API

### sendEmail(options)

Send an email using a template or custom HTML.

**Parameters:**

- `options` (Object):
  - `to` (String, required): Recipient email address
  - `subject` (String, required): Email subject line
  - `template` (String, optional): Template name (without .html extension)
  - `html` (String, optional): Custom HTML content (if not using template)
  - `variables` (Object, optional): Template variables for replacement
  - `from` (String, optional): Sender email (defaults to .env config)
  - `replyTo` (String, optional): Reply-to email (defaults to .env config)

**Returns:** Promise<Object>
- `success` (Boolean): Whether the email was sent
- `messageId` (String): Unique message identifier
- `sent` (Boolean): False if EMAIL_ENABLED=false

**Example:**

```javascript
const { sendEmail } = require('./index');

// Using a template
await sendEmail({
  to: 'user@example.com',
  subject: 'Welcome!',
  template: 'welcome',
  variables: {
    firstName: 'John',
    dashboardUrl: 'https://example.com/dashboard'
  }
});

// Using custom HTML
await sendEmail({
  to: 'user@example.com',
  subject: 'Custom Message',
  html: '<h1>Hello!</h1><p>Custom content</p>'
});
```

---

### loadTemplate(templateName, variables)

Load and compile an HTML email template.

**Parameters:**

- `templateName` (String, required): Template filename without extension
- `variables` (Object, optional): Variables to replace in template

**Returns:** String (compiled HTML)

**Example:**

```javascript
const { loadTemplate } = require('./index');

const html = loadTemplate('welcome', {
  firstName: 'John',
  dashboardUrl: 'https://example.com/dashboard'
});
```

---

### verifyConnection()

Test SMTP server connection.

**Returns:** Promise<Boolean>

**Example:**

```javascript
const { verifyConnection } = require('./index');

try {
  await verifyConnection();
  console.log('Connection successful');
} catch (error) {
  console.error('Connection failed:', error);
}
```

---

### createTransporter()

Create a Nodemailer transporter instance.

**Returns:** Transporter object

**Example:**

```javascript
const { createTransporter } = require('./index');

const transporter = createTransporter();
// Use transporter directly with Nodemailer API
```

---

### getSMTPConfig()

Get processed SMTP configuration for current provider.

**Returns:** Object (SMTP configuration)

**Example:**

```javascript
const { getSMTPConfig } = require('./index');

const config = getSMTPConfig();
console.log('Using SMTP host:', config.host);
```

---

## Template Variables

### welcome.html

```javascript
{
  firstName: 'John',
  dashboardUrl: 'https://example.com/dashboard',
  facebookUrl: 'https://facebook.com/yourpage',
  twitterUrl: 'https://twitter.com/yourpage',
  instagramUrl: 'https://instagram.com/yourpage',
  linkedinUrl: 'https://linkedin.com/company/yourcompany',
  unsubscribeUrl: 'https://example.com/unsubscribe',
  preferencesUrl: 'https://example.com/preferences',
  privacyUrl: 'https://example.com/privacy'
}
```

### order-confirmation.html

```javascript
{
  customerName: 'John Doe',
  orderNumber: 'ORD-12345',
  orderDate: 'November 22, 2025',
  subtotal: '99.99',
  shipping: '9.99',
  tax: '8.50',
  total: '118.48',
  items: [
    { name: 'Product 1', quantity: 2, price: '49.99' },
    { name: 'Product 2', quantity: 1, price: '49.99' }
  ],
  shippingName: 'John Doe',
  shippingAddress: '123 Main St',
  shippingCity: 'Los Angeles',
  shippingState: 'CA',
  shippingZip: '90001',
  shippingCountry: 'USA',
  trackingUrl: 'https://example.com/track/12345'
}
```

### support-response.html

```javascript
{
  customerName: 'John Doe',
  ticketNumber: 'TICK-12345',
  subject: 'Question about product',
  status: 'Open',
  priority: 'Medium',
  responseMessage: 'Thank you for contacting us...',
  originalMessage: 'I have a question about...',
  agentName: 'Sarah Johnson',
  helpCenterUrl: 'https://example.com/help',
  faqUrl: 'https://example.com/faq',
  communityUrl: 'https://example.com/community',
  statusUrl: 'https://status.example.com'
}
```

### password-reset.html

```javascript
{
  userName: 'John Doe',
  resetUrl: 'https://example.com/reset-password?token=abc123',
  resetCode: '123456',
  expirationTime: '24'  // hours
}
```

### newsletter.html

```javascript
{
  firstName: 'John',
  monthYear: 'November 2025',
  article1Image: 'https://example.com/images/article1.jpg',
  article1Title: 'New Album Release',
  article1Excerpt: 'Check out our latest album...',
  article1Url: 'https://example.com/articles/1',
  article2Image: 'https://example.com/images/article2.jpg',
  article2Title: 'Artist Interview',
  article2Excerpt: 'We sat down with...',
  article2Url: 'https://example.com/articles/2',
  article3Image: 'https://example.com/images/article3.jpg',
  article3Title: 'Concert Highlights',
  article3Excerpt: 'Recap of last weekend...',
  article3Url: 'https://example.com/articles/3',
  eventsUrl: 'https://example.com/events',
  topTracks: [
    { title: 'Song 1', artist: 'Artist 1' },
    { title: 'Song 2', artist: 'Artist 2' }
  ],
  facebookUrl: 'https://facebook.com/yourpage',
  twitterUrl: 'https://twitter.com/yourpage',
  instagramUrl: 'https://instagram.com/yourpage',
  spotifyUrl: 'https://open.spotify.com/user/yourprofile',
  unsubscribeUrl: 'https://example.com/unsubscribe',
  preferencesUrl: 'https://example.com/preferences'
}
```

---

## Error Handling

All async functions may throw errors. Always use try-catch:

```javascript
try {
  await sendEmail({
    to: 'user@example.com',
    subject: 'Test',
    template: 'welcome',
    variables: { firstName: 'John' }
  });
} catch (error) {
  console.error('Failed to send email:', error.message);
  // Handle error appropriately
}
```

Common errors:
- `Invalid email provider` - Check EMAIL_PROVIDER in .env
- `Template not found` - Template file doesn't exist
- `Authentication failed` - Invalid credentials
- `Connection timeout` - Network or firewall issue

---

## Rate Limiting

Configure in `.env`:

```env
EMAIL_RATE_LIMIT=10
EMAIL_RATE_WINDOW=60000
```

The SMTP configuration includes built-in connection pooling and rate limiting.

---

## Testing

Disable actual email sending for testing:

```env
EMAIL_ENABLED=false
```

When disabled, `sendEmail()` returns:

```javascript
{
  preview: { /* email details */ },
  sent: false
}
```
