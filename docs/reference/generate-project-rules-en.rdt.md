# Generate Code

Generate project rules files using instructions.

## Template

### Configuration

````json conversation-template
{
  "id": "generate-project-rules-en",
  "engineVersion": 0,
  "label": "Generate Project Rules",
  "tags": ["generate"],
  "description": "Generate project rules files using instructions.",
  "header": {
    "title": "Generating Project Rules",
    "icon": {
      "type": "codicon",
      "value": "wand"
    }
  },
  "chatInterface": "instruction-refinement",
  "variables": [],
  "initialMessage": {
    "placeholder": "Generating project rules files",
    "maxTokens": 2048
  },
  "agentInitialMessage": {
    "placeholder": "Generating project rules files",
    "maxTokens": 2048
  },
  "response": {
    "placeholder": "Generating project rules files",
    "maxTokens": 4096,
    "stop": ["```"],
    "completionHandler": {
      "type": "update-temporary-editor",
      "botMessage": "Project rules files generated."
    }
  }
}
````
### Initial Message Prompt

```template-initial-message
<|system|>
Summarize the project at a high level (including goal and purpose) with an emphasis on its key functionality.
<|end|>
<|user|>
Please delve into this project thoroughly. After gaining a comprehensive understanding, please deeply contemplate the following:

Users will employ an AI chat and agent to assist in the development of this project. When utilizing the AI, a rule prompt file will be automatically introduced at the beginning of each conversation. Now, how can we design and write these rule files to better enable users to develop this project using the AI?

Please write the different rule files in markdown format and place them in the .fitten/rules/ folder. For now, only a project background information file is required, which should be briefly worded and added to the file.
<|end|>
<|assistant|>
```

### Response Prompt

```template-response
<|system|>
Please delve into this project thoroughly. After gaining a comprehensive understanding, please deeply contemplate the following:

Users will employ an AI chat and agent to assist in the development of this project. When utilizing the AI, a rule prompt file will be automatically introduced at the beginning of each conversation. Now, how can we design and write these rule files to better enable users to develop this project using the AI?

Please write the different rule files in markdown format and place them in the .fitten/rules/ folder. For now, only a project background information file is required, which should be briefly worded and added to the file.
<|end|>
<|user|>
<|end|>
<|assistant|>
```

### Agent Prompt

```template-agent-initial-message
Please delve into this project thoroughly. After gaining a comprehensive understanding, please deeply contemplate the following:

Users will employ an AI chat and agent to assist in the development of this project. When utilizing the AI, a rule prompt file will be automatically introduced at the beginning of each conversation. Now, how can we design and write these rule files to better enable users to develop this project using the AI?

Please write the different rule files in markdown format and place them in the .fitten/rules/ folder. For now, only a project background information file is required, which should be briefly worded and added to the file.
```
