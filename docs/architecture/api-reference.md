# NoizyLab API Reference

## Email Intelligence API

### Base URL
```
http://localhost:8000
```

### Endpoints

#### GET `/`
Health check endpoint.

**Response:**
```json
{
  "status": "running",
  "version": "3.0"
}
```

#### POST `/validate`
Validate an email address.

**Request:**
```json
{
  "email": "user@example.com"
}
```

**Response:**
```json
{
  "email": "user@example.com",
  "valid": true,
  "category": "professional",
  "quality_score": 0.95
}
```

#### GET `/analytics`
Get all email analytics data.

**Response:**
```json
{
  "emails": [
    {
      "id": 1,
      "email": "user@example.com",
      "category": "professional",
      "quality_score": 0.95
    }
  ]
}
```

#### GET `/stream`
WebSocket endpoint for real-time data streaming.

**Connection:**
```javascript
const ws = new WebSocket('ws://localhost:8000/stream');
ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log(data);
};
```

## Universal Blocker API

### Endpoints

#### POST `/block`
Add domain to blocklist.

**Request:**
```json
{
  "domain": "spam.com"
}
```

#### GET `/blocklist`
Get current blocklist.

## iMessage Spam Filter API

### Endpoints

#### POST `/filter`
Run spam filter on iMessage database.

**Request:**
```json
{
  "pattern": "Bounce-21",
  "auto_delete": false
}
```

## Authentication

All endpoints require API key in header:
```
X-API-Key: your-api-key
```

