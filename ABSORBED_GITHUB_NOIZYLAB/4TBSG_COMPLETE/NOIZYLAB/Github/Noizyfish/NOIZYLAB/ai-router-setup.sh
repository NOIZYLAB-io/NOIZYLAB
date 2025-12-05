#!/bin/bash
# MULTI-AI ROUTER SETUP SCRIPT
# Sets up the AI router for multiple providers

set -e

ROUTER_DIR="ai/router"
mkdir -p "$ROUTER_DIR/src"

cat > "$ROUTER_DIR/src/index.ts" << 'EOF'
// MULTI-AI ROUTER
// Routes requests to appropriate AI provider

export interface AIRequest {
  prompt: string;
  provider?: 'openai' | 'anthropic' | 'google' | 'auto';
  model?: string;
  temperature?: number;
}

export interface AIResponse {
  provider: string;
  model: string;
  response: string;
  tokens?: number;
  latency: number;
}

export class AIRouter {
  private openaiKey: string;
  private anthropicKey: string;
  private googleKey: string;

  constructor(env: { OPENAI_KEY: string; ANTHROPIC_KEY: string; GOOGLE_KEY: string }) {
    this.openaiKey = env.OPENAI_KEY;
    this.anthropicKey = env.ANTHROPIC_KEY;
    this.googleKey = env.GOOGLE_KEY;
  }

  async route(request: AIRequest): Promise<AIResponse> {
    const provider = request.provider || 'auto';
    const startTime = Date.now();

    let response: AIResponse;

    switch (provider) {
      case 'openai':
        response = await this.callOpenAI(request);
        break;
      case 'anthropic':
        response = await this.callAnthropic(request);
        break;
      case 'google':
        response = await this.callGoogle(request);
        break;
      case 'auto':
      default:
        response = await this.autoRoute(request);
        break;
    }

    response.latency = Date.now() - startTime;
    return response;
  }

  private async callOpenAI(request: AIRequest): Promise<AIResponse> {
    const model = request.model || 'gpt-4-turbo-preview';
    const response = await fetch('https://api.openai.com/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${this.openaiKey}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model,
        messages: [{ role: 'user', content: request.prompt }],
        temperature: request.temperature || 0.7,
      }),
    });

    const data = await response.json();
    return {
      provider: 'openai',
      model,
      response: data.choices[0].message.content,
      tokens: data.usage?.total_tokens,
      latency: 0,
    };
  }

  private async callAnthropic(request: AIRequest): Promise<AIResponse> {
    const model = request.model || 'claude-3-opus-20240229';
    const response = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'x-api-key': this.anthropicKey,
        'anthropic-version': '2023-06-01',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model,
        max_tokens: 4096,
        messages: [{ role: 'user', content: request.prompt }],
      }),
    });

    const data = await response.json();
    return {
      provider: 'anthropic',
      model,
      response: data.content[0].text,
      tokens: data.usage?.input_tokens + data.usage?.output_tokens,
      latency: 0,
    };
  }

  private async callGoogle(request: AIRequest): Promise<AIResponse> {
    const model = request.model || 'gemini-pro';
    const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${this.googleKey}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        contents: [{ parts: [{ text: request.prompt }] }],
      }),
    });

    const data = await response.json();
    return {
      provider: 'google',
      model,
      response: data.candidates[0].content.parts[0].text,
      latency: 0,
    };
  }

  private async autoRoute(request: AIRequest): Promise<AIResponse> {
    // Auto-select best provider based on prompt characteristics
    // For now, default to OpenAI
    return this.callOpenAI(request);
  }
}

export default AIRouter;
EOF

cat > "$ROUTER_DIR/package.json" << 'EOF'
{
  "name": "@noizylab/ai-router",
  "version": "1.0.0",
  "main": "src/index.ts",
  "type": "module"
}
EOF

echo "✅ AI Router setup complete!"
echo "📁 Router created in: $ROUTER_DIR"
echo ""
echo "🔑 Add API keys to wrangler.toml:"
echo "   OPENAI_KEY = \"your-key\""
echo "   ANTHROPIC_KEY = \"your-key\""
echo "   GOOGLE_KEY = \"your-key\""

