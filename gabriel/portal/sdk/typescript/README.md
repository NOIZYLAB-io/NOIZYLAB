# GABRIEL TypeScript SDK

Official TypeScript/JavaScript SDK for the GABRIEL board inspection API.

## Installation

```bash
npm install @gabriel/sdk
# or
yarn add @gabriel/sdk
# or
pnpm add @gabriel/sdk
```

## Quick Start

```typescript
import GabrielClient from '@gabriel/sdk';

const gabriel = new GabrielClient({
  apiKey: 'gab_live_your_api_key_here'
});

// Upload and scan an image
const image = await fs.readFile('./pcb-image.jpg');
const { scanId } = await gabriel.scan.create(image, {
  boardType: 'iphone-15-pro-logic-board'
});

// Wait for results
const result = await gabriel.scan.waitForCompletion(scanId);

console.log(`Found ${result.issues?.length || 0} issues:`);
for (const issue of result.issues || []) {
  console.log(`- ${issue.component}: ${issue.description} (${issue.severity})`);
}
```

## API Reference

### Initialization

```typescript
import GabrielClient from '@gabriel/sdk';

const gabriel = new GabrielClient({
  apiKey: 'gab_live_xxx',      // Required: Your API key
  baseUrl: 'https://...',       // Optional: Custom API URL
  timeout: 30000,               // Optional: Request timeout (ms)
});
```

### Scans

#### Create a scan

```typescript
const { scanId } = await gabriel.scan.create(imageBuffer, {
  boardType: 'iphone-15-pro-logic-board',  // Optional: Specific board type
  userId: 'user_123',                       // Optional: Associate with user
  webhookUrl: 'https://...',                // Optional: Callback URL
  priority: 'high'                          // Optional: Processing priority
});
```

#### Get scan result

```typescript
const result = await gabriel.scan.get('scan_abc123');
```

#### Wait for completion

```typescript
const result = await gabriel.scan.waitForCompletion('scan_abc123', {
  maxWait: 60000,      // Maximum wait time (ms)
  pollInterval: 2000   // Polling interval (ms)
});
```

#### List scans

```typescript
const { data, total, hasMore } = await gabriel.scan.list({
  page: 1,
  perPage: 20,
  status: 'complete'
});
```

### Golden References

#### Upload a reference

```typescript
const reference = await gabriel.reference.upload(imageBuffer, {
  boardType: 'custom-board-v2',
  name: 'Production Unit #1'
});
```

#### List references

```typescript
const references = await gabriel.reference.list();
```

### Webhooks

#### Create a webhook

```typescript
const { webhook, secret } = await gabriel.webhook.create({
  url: 'https://your-server.com/webhook',
  events: ['scan.complete', 'scan.failed']
});

// Store the secret securely for signature verification
```

#### Verify webhook signature

```typescript
import { WebhookAPI } from '@gabriel/sdk';

const isValid = await WebhookAPI.verify(
  payload,    // Raw request body string
  signature,  // X-Gabriel-Signature header
  secret      // Your webhook secret
);
```

### Board Database

#### Search boards

```typescript
const boards = await gabriel.board.search('iPhone 15');
```

#### Get board details

```typescript
const board = await gabriel.board.get('iphone-15-pro-logic-board');
```

#### Get common issues

```typescript
const issues = await gabriel.board.getIssues('iphone-15-pro-logic-board');
```

## Error Handling

```typescript
import { 
  GabrielError, 
  AuthenticationError, 
  RateLimitError 
} from '@gabriel/sdk';

try {
  const result = await gabriel.scan.get('scan_123');
} catch (error) {
  if (error instanceof AuthenticationError) {
    console.error('Invalid API key');
  } else if (error instanceof RateLimitError) {
    console.error(`Rate limited. Retry in ${error.retryAfter}s`);
  } else if (error instanceof GabrielError) {
    console.error(`API Error: ${error.message} (${error.code})`);
  }
}
```

## TypeScript Types

Full TypeScript support with exported types:

```typescript
import type {
  ScanResult,
  Issue,
  GoldenReference,
  Webhook,
  ScanOptions,
  PaginatedResponse
} from '@gabriel/sdk';
```

## Examples

### Batch Processing

```typescript
const images = await Promise.all(
  files.map(f => fs.readFile(f))
);

// Start all scans in parallel
const scans = await Promise.all(
  images.map(img => gabriel.scan.create(img))
);

// Wait for all to complete
const results = await Promise.all(
  scans.map(s => gabriel.scan.waitForCompletion(s.scanId))
);
```

### Webhook Server (Express)

```typescript
import express from 'express';
import { WebhookAPI } from '@gabriel/sdk';

const app = express();

app.post('/webhook', express.raw({ type: 'application/json' }), async (req, res) => {
  const signature = req.headers['x-gabriel-signature'] as string;
  const isValid = await WebhookAPI.verify(
    req.body.toString(),
    signature,
    process.env.WEBHOOK_SECRET!
  );

  if (!isValid) {
    return res.status(401).send('Invalid signature');
  }

  const event = JSON.parse(req.body.toString());
  
  switch (event.type) {
    case 'scan.complete':
      console.log('Scan completed:', event.data.scanId);
      break;
    case 'scan.failed':
      console.log('Scan failed:', event.data.error);
      break;
  }

  res.send('OK');
});
```

## Support

- 📚 [Documentation](https://gabriel.noizylab.com/docs)
- 🐛 [Issues](https://github.com/Noizyfish/GABRIEL/issues)
- 💬 [Discord](https://discord.gg/noizylab)

## License

MIT © NOIZYLAB
