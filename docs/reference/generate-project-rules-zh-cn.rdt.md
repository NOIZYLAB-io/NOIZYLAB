# Generate Code

Generate project rules files using instructions.

## Template

### Configuration

````json conversation-template
{
  "id": "generate-project-rules-zh-cn",
  "engineVersion": 0,
  "label": "Generate Project Rules",
  "tags": ["generate"],
  "description": "Generate project rules files using instructions.",
  "header": {
    "title": "生成项目级规则文件",
    "icon": {
      "type": "codicon",
      "value": "wand"
    }
  },
  "chatInterface": "instruction-refinement",
  "variables": [],
  "initialMessage": {
    "placeholder": "生成项目级规则文件中",
    "maxTokens": 2048
  },
  "agentInitialMessage": {
    "placeholder": "生成项目级规则文件中",
    "maxTokens": 2048
  },
  "response": {
    "placeholder": "正在生成项目级规则文件",
    "maxTokens": 4096,
    "stop": ["```"],
    "completionHandler": {
      "type": "update-temporary-editor",
      "botMessage": "已生成项目级规则文件。"
    }
  }
}
````

### Initial Message Prompt

```template-initial-message
<|system|>
Summarize the project at a high level (including goal and purpose) with an emphasis on its key functionality.
请完全使用中文回答。
<|end|>
<|user|>
请深入了解这个项目，在了解完毕后。请深入思考：
用户将会使用AI对话和智能体辅助开发此项目，在使用AI时都会在对话的开始自动引入规则提示文件。
现在，如何设计和编写这些规则文件才能更好的让用户使用AI开发此项目？
请将不同的规则文件以markdown的形式写入在.fitten/rules/文件夹下
目前只需要你生成一个项目背景信息文件，以简短的文字表述并添加到文件中。
<|end|>
<|assistant|>
```

### Response Prompt

```template-response
<|system|>
请深入了解这个项目，在了解完毕后。请深入思考：
用户将会使用AI对话和智能体辅助开发此项目，在使用AI时都会在对话的开始自动引入规则提示文件。
现在，如何设计和编写这些规则文件才能更好的让用户使用AI开发此项目？
请将不同的规则文件以markdown的形式写入在.fitten/rules/文件夹下
目前只需要你生成一个项目背景信息文件，以简短的文字表述并添加到文件中。
<|end|>
<|user|>
<|end|>
<|assistant|>
```

### Agent Prompt

```template-agent-initial-message
请深入了解这个项目，在了解完毕后。请深入思考：
用户将会使用AI对话和智能体辅助开发此项目，在使用AI时都会在对话的开始自动引入规则提示文件。
现在，如何设计和编写这些规则文件才能更好的让用户使用AI开发此项目？
请将不同的规则文件以markdown的形式写入在.fitten/rules/文件夹下
目前只需要你生成一个项目背景信息文件，以简短的文字表述并添加到文件中。
```
