# Cloudflare AI Super-Code Guide

## 🚀 Features

- **7 AI Models** - Llama, Mistral, Gemma, Qwen, DeepSeek
- **Streaming Support** - Real-time responses
- **Smart Caching** - 24-hour cache with KV
- **Usage Tracking** - Database logging
- **Error Handling** - Production-ready
- **CORS Enabled** - Frontend ready

## 📋 Endpoints

### 1. Chat (Standard)
```bash
POST /api/ai/chat
Content-Type: application/json

{
  "prompt": "Your question here",
  "model": "llama-3.1-8b",
  "temperature": 0.7,
  "max_tokens": 2048,
  "system": "You are a helpful assistant"
}
```

### 2. Streaming
```bash
POST /api/ai/stream
Content-Type: application/json

{
  "prompt": "Your question here",
  "model": "llama-3.1-70b",
  "stream": true
}
```

### 3. List Models
```bash
GET /api/ai/models
```

### 4. Stats
```bash
GET /api/ai/stats
```

## 🤖 Available Models

- `llama-3.1-8b` - Fast, efficient (default)
- `llama-3.1-70b` - More powerful
- `mistral-7b` - Mistral AI
- `gemma-7b` - Google Gemma
- `qwen-14b` - Alibaba Qwen
- `deepseek-7b` - Math-focused

## 💡 Usage Examples

### JavaScript/TypeScript
```typescript
const response = await fetch('https://ai.noizylab.ca/api/ai/chat', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    prompt: 'Explain quantum computing',
    model: 'llama-3.1-70b',
    temperature: 0.8
  })
});

const data = await response.json();
console.log(data.response);
```

### Streaming
```typescript
const response = await fetch('https://ai.noizylab.ca/api/ai/stream', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    prompt: 'Write a story',
    stream: true
  })
});

const reader = response.body?.getReader();
const decoder = new TextDecoder();

while (true) {
  const { done, value } = await reader!.read();
  if (done) break;
  
  const chunk = decoder.decode(value);
  console.log(chunk);
}
```

## ⚙️ Configuration

Edit `wrangler.toml`:
- Add D1 database ID
- Add KV namespace ID
- Add R2 bucket name
- Configure routes

## 📊 Database Schema

```sql
CREATE TABLE IF NOT EXISTS ai_interactions (
  id TEXT PRIMARY KEY,
  model TEXT NOT NULL,
  prompt TEXT,
  tokens INTEGER,
  latency INTEGER,
  created_at INTEGER
);
```

## 🚀 Deploy

```bash
cd workers/ai-super-worker
wrangler deploy
```

## 🎯 Performance

- **Caching**: 24-hour TTL
- **Latency**: Tracked per request
- **Tokens**: Estimated and logged
- **Stats**: 24-hour rolling window

