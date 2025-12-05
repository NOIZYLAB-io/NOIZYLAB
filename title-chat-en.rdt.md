# AI Chat in English

This template lets you chat with fittencode in English.

## Template

### Configuration

```json conversation-template
{
  "id": "title-chat-en",
  "engineVersion": 0,
  "label": "Start chat",
  "description": "Start a basic chat with fittencode.",
  "header": {
    "title": "New Chat",
    "useFirstMessageAsTitle": true,
    "icon": {
      "type": "codicon",
      "value": "comment-discussion"
    }
  },
  "variables": [
    {
      "name": "filename",
      "time": "conversation-start",
      "type": "filename"
    },
    {
      "name": "rules",
      "time": "conversation-start",
      "type": "rules"
    },
    {
      "name": "language",
      "time": "conversation-start",
      "type": "language"
    },
    {
      "name": "titleSelectedText",
      "time": "conversation-start",
      "type": "title-selected-text"
    },
    {
      "name": "lastMessage",
      "time": "message",
      "type": "message",
      "property": "content",
      "index": -1
    }
  ],
  "response": {
    "maxTokens": 1024,
    "stop": ["Bot:", "Developer:"]
  }
}
```

### Response Prompt

```template-response
<|system|>
Reply English.
{{#if rules}}
{{rules}}
{{/if}}
<|end|>
{{#each promptMessages}}
{{#if (eq author "bot")}}
<|assistant|>
{{content}}
<|end|>
{{else}}
<|user|>
{{content}}
<|end|>
{{/if}}
{{/each}}
<|assistant|>
```
