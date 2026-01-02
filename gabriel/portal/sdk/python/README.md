# GABRIEL Python SDK

Official Python SDK for the GABRIEL board inspection API.

## Installation

```bash
pip install gabriel-sdk
```

For better performance with connection pooling:

```bash
pip install gabriel-sdk[httpx]
```

## Quick Start

```python
from gabriel import GabrielClient

client = GabrielClient(api_key='gab_live_your_api_key_here')

# Upload and scan an image
with open('pcb-image.jpg', 'rb') as f:
    scan = client.scan.create(f, board_type='iphone-15-pro-logic-board')

# Wait for results
result = client.scan.wait_for_completion(scan['scanId'])

print(f'Found {len(result.issues or [])} issues:')
for issue in result.issues or []:
    print(f'- {issue.component}: {issue.description} ({issue.severity.value})')
```

## Quick Scan Function

For simple one-off scans:

```python
from gabriel import quick_scan

result = quick_scan('gab_live_xxx', 'board.jpg')
for issue in result.issues or []:
    print(f'{issue.component}: {issue.description}')
```

## Context Manager

Use as a context manager for automatic cleanup:

```python
from gabriel import GabrielClient

with GabrielClient(api_key='gab_live_xxx') as client:
    scan = client.scan.create(open('board.jpg', 'rb'))
    result = client.scan.wait_for_completion(scan['scanId'])
```

## API Reference

### Initialization

```python
from gabriel import GabrielClient

client = GabrielClient(
    api_key='gab_live_xxx',           # Required: Your API key
    base_url='https://...',            # Optional: Custom API URL
    timeout=30,                         # Optional: Request timeout (seconds)
)
```

### Scans

#### Create a scan

```python
scan = client.scan.create(
    image_file,                        # Required: File-like object or bytes
    board_type='iphone-15-pro',        # Optional: Specific board type
    user_id='user_123',                # Optional: Associate with user
    webhook_url='https://...',         # Optional: Callback URL
    priority='high'                    # Optional: 'normal' or 'high'
)
```

#### Get scan result

```python
result = client.scan.get('scan_abc123')
```

#### Wait for completion

```python
result = client.scan.wait_for_completion(
    'scan_abc123',
    max_wait=60,       # Maximum wait time (seconds)
    poll_interval=2    # Polling interval (seconds)
)
```

#### List scans

```python
response = client.scan.list(
    page=1,
    per_page=20,
    status='complete'
)
```

### Golden References

#### Upload a reference

```python
reference = client.reference.upload(
    image_file,
    board_type='custom-board-v2',
    name='Production Unit #1'
)
```

#### List references

```python
references = client.reference.list()
```

### Webhooks

#### Create a webhook

```python
result = client.webhook.create(
    url='https://your-server.com/webhook',
    events=['scan.complete', 'scan.failed']
)
# Store result['secret'] securely
```

#### Verify webhook signature

```python
from gabriel import WebhookAPI

is_valid = WebhookAPI.verify(
    payload,    # Raw request body string
    signature,  # X-Gabriel-Signature header
    secret      # Your webhook secret
)
```

### Board Database

```python
# Search boards
boards = client.board.search('iPhone 15')

# Get board details
board = client.board.get('iphone-15-pro-logic-board')

# Get common issues
issues = client.board.get_issues('iphone-15-pro-logic-board')
```

## Error Handling

```python
from gabriel import (
    GabrielError,
    AuthenticationError,
    RateLimitError,
    ScanTimeoutError
)

try:
    result = client.scan.get('scan_123')
except AuthenticationError:
    print('Invalid API key')
except RateLimitError as e:
    print(f'Rate limited. Retry in {e.retry_after}s')
except ScanTimeoutError as e:
    print(f'Scan {e.scan_id} timed out')
except GabrielError as e:
    print(f'API Error: {e.message} ({e.code})')
```

## Data Classes

The SDK uses Python dataclasses for structured responses:

```python
from gabriel import ScanResult, Issue, Severity, IssueType

# ScanResult fields
result.scan_id       # str
result.status        # 'processing' | 'complete' | 'failed'
result.board_type    # Optional[str]
result.confidence    # Optional[float]
result.issues        # Optional[List[Issue]]
result.metadata      # Optional[Dict]
result.created_at    # Optional[str]
result.completed_at  # Optional[str]

# Issue fields
issue.id             # str
issue.component      # str
issue.type           # IssueType enum
issue.severity       # Severity enum
issue.description    # str
issue.confidence     # float
issue.location       # Dict with x, y, width, height
issue.repair_guide   # Optional[str]

# Enums
Severity.CRITICAL
Severity.WARNING
Severity.INFO

IssueType.DAMAGED
IssueType.MISSING
IssueType.MISALIGNED
IssueType.COLD_SOLDER
IssueType.BRIDGED
```

## Examples

### Batch Processing

```python
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

def process_image(path: Path) -> ScanResult:
    with GabrielClient(api_key='gab_live_xxx') as client:
        with open(path, 'rb') as f:
            scan = client.scan.create(f)
        return client.scan.wait_for_completion(scan['scanId'])

images = list(Path('boards/').glob('*.jpg'))

with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(process_image, images))

for path, result in zip(images, results):
    print(f'{path}: {len(result.issues or [])} issues')
```

### Flask Webhook Server

```python
from flask import Flask, request
from gabriel import WebhookAPI
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    signature = request.headers.get('X-Gabriel-Signature', '')
    
    if not WebhookAPI.verify(
        request.data.decode(),
        signature,
        os.environ['WEBHOOK_SECRET']
    ):
        return 'Invalid signature', 401
    
    event = request.json
    
    if event['type'] == 'scan.complete':
        print(f"Scan completed: {event['data']['scanId']}")
    elif event['type'] == 'scan.failed':
        print(f"Scan failed: {event['data']['error']}")
    
    return 'OK'
```

## Requirements

- Python 3.8+
- Optional: `httpx` for better performance

## Support

- 📚 [Documentation](https://gabriel.noizylab.com/docs)
- 🐛 [Issues](https://github.com/Noizyfish/GABRIEL/issues)
- 💬 [Discord](https://discord.gg/noizylab)

## License

MIT © NOIZYLAB
