// ═══════════════════════════════════════════════════════════════════════════════
// AI MODEL ROUTER - INTELLIGENT MULTI-MODEL ORCHESTRATION
// Routes requests to the optimal AI model based on task type
// ═══════════════════════════════════════════════════════════════════════════════

export class AIRouter {
  constructor(env) {
    this.env = env;
    this.models = this.initializeModels();
    this.stats = {
      calls: {},
      latency: {},
      errors: {}
    };
  }

  // ─── MODEL DEFINITIONS ─────────────────────────────────────────────────────

  initializeModels() {
    return {
      // Fast, general purpose
      mistral: {
        id: "@cf/mistral/mistral-7b-instruct-v0.1",
        name: "Mistral 7B",
        strengths: ["general", "fast", "code", "chat"],
        maxTokens: 4096,
        speed: "fast",
        cost: "low"
      },
      // Code specialized
      codellama: {
        id: "@cf/meta/codellama-7b-instruct",
        name: "Code Llama 7B",
        strengths: ["code", "debugging", "refactoring"],
        maxTokens: 4096,
        speed: "fast",
        cost: "low"
      },
      // Larger, more capable
      llama2: {
        id: "@cf/meta/llama-2-7b-chat-int8",
        name: "Llama 2 7B",
        strengths: ["reasoning", "analysis", "creative"],
        maxTokens: 4096,
        speed: "medium",
        cost: "low"
      },
      // SQL specialized
      sqlcoder: {
        id: "@cf/defog/sqlcoder-7b-2",
        name: "SQLCoder 7B",
        strengths: ["sql", "database", "queries"],
        maxTokens: 2048,
        speed: "fast",
        cost: "low"
      },
      // Embeddings
      bge: {
        id: "@cf/baai/bge-base-en-v1.5",
        name: "BGE Embeddings",
        strengths: ["embeddings", "similarity", "search"],
        maxTokens: 512,
        speed: "fast",
        cost: "low"
      },
      // Image generation
      sdxl: {
        id: "@cf/stabilityai/stable-diffusion-xl-base-1.0",
        name: "Stable Diffusion XL",
        strengths: ["images", "art", "design"],
        maxTokens: null,
        speed: "slow",
        cost: "medium"
      }
    };
  }

  // ─── INTELLIGENT ROUTING ───────────────────────────────────────────────────

  selectModel(task) {
    const taskLower = task.toLowerCase();

    // Code-related tasks
    if (this.matchesAny(taskLower, ["code", "function", "class", "debug", "fix", "refactor", "implement", "programming"])) {
      return "codellama";
    }

    // SQL/Database tasks
    if (this.matchesAny(taskLower, ["sql", "query", "database", "table", "select", "insert", "schema"])) {
      return "sqlcoder";
    }

    // Image generation
    if (this.matchesAny(taskLower, ["image", "picture", "draw", "design", "logo", "art", "illustration"])) {
      return "sdxl";
    }

    // Embeddings/Search
    if (this.matchesAny(taskLower, ["embed", "similarity", "search", "vector", "semantic"])) {
      return "bge";
    }

    // Complex reasoning
    if (this.matchesAny(taskLower, ["analyze", "reason", "explain", "compare", "evaluate", "strategy"])) {
      return "llama2";
    }

    // Default to Mistral for general tasks
    return "mistral";
  }

  matchesAny(text, keywords) {
    return keywords.some(kw => text.includes(kw));
  }

  // ─── EXECUTE REQUEST ───────────────────────────────────────────────────────

  async run(task, options = {}) {
    const {
      model: forcedModel,
      maxTokens = 2000,
      temperature = 0.7,
      systemPrompt = null,
      format = "text" // text, json, code
    } = options;

    // Select model
    const modelKey = forcedModel || this.selectModel(task);
    const model = this.models[modelKey];

    if (!model) {
      throw new Error(`Unknown model: ${modelKey}`);
    }

    const startTime = Date.now();

    try {
      // Build prompt based on format
      let prompt = task;

      if (systemPrompt) {
        prompt = `${systemPrompt}\n\n${task}`;
      }

      if (format === "json") {
        prompt += "\n\nRespond with valid JSON only, no markdown or explanation.";
      } else if (format === "code") {
        prompt += "\n\nRespond with code only, no explanation or markdown code blocks.";
      }

      // Execute
      const response = await this.env.AI.run(model.id, {
        prompt,
        max_tokens: Math.min(maxTokens, model.maxTokens || maxTokens),
        temperature
      });

      // Track stats
      this.trackStats(modelKey, Date.now() - startTime, true);

      // Parse response
      let result = response.response || response;

      if (format === "json") {
        try {
          const jsonMatch = result.match(/\{[\s\S]*\}/);
          if (jsonMatch) {
            result = JSON.parse(jsonMatch[0]);
          }
        } catch {
          // Return as-is if JSON parsing fails
        }
      }

      return {
        model: modelKey,
        modelName: model.name,
        response: result,
        latency: Date.now() - startTime,
        tokens: this.estimateTokens(prompt, result)
      };

    } catch (error) {
      this.trackStats(modelKey, Date.now() - startTime, false);
      throw error;
    }
  }

  // ─── SPECIALIZED METHODS ───────────────────────────────────────────────────

  async generateCode(spec, language = "javascript") {
    const prompt = `Generate ${language} code for the following specification:

${spec}

Requirements:
- Production-quality code
- Include error handling
- Add comments for complex logic
- Follow best practices for ${language}

Return only the code, no explanations.`;

    return this.run(prompt, { model: "codellama", format: "code" });
  }

  async analyzeCode(code, aspects = ["quality", "security", "performance"]) {
    const prompt = `Analyze this code for: ${aspects.join(", ")}

\`\`\`
${code}
\`\`\`

Return JSON with:
{
  "quality": { "score": 0-100, "issues": [], "suggestions": [] },
  "security": { "score": 0-100, "vulnerabilities": [], "fixes": [] },
  "performance": { "score": 0-100, "bottlenecks": [], "optimizations": [] },
  "overall": { "score": 0-100, "summary": "" }
}`;

    return this.run(prompt, { model: "codellama", format: "json" });
  }

  async generateSQL(description, schema = null) {
    let prompt = `Generate SQL query for: ${description}`;

    if (schema) {
      prompt += `\n\nDatabase schema:\n${schema}`;
    }

    prompt += "\n\nReturn only the SQL query.";

    return this.run(prompt, { model: "sqlcoder", format: "code" });
  }

  async generateImage(description, options = {}) {
    const { width = 1024, height = 1024, style = "photorealistic" } = options;

    const prompt = `${description}, ${style}, high quality, detailed`;

    const response = await this.env.AI.run(this.models.sdxl.id, {
      prompt,
      width,
      height
    });

    return {
      model: "sdxl",
      image: response,
      prompt: description
    };
  }

  async getEmbeddings(texts) {
    const textsArray = Array.isArray(texts) ? texts : [texts];

    const response = await this.env.AI.run(this.models.bge.id, {
      text: textsArray
    });

    return {
      model: "bge",
      embeddings: response.data,
      dimensions: response.data[0]?.length || 0
    };
  }

  async chat(messages, options = {}) {
    const { model = "mistral", systemPrompt } = options;

    // Build conversation
    let prompt = "";

    if (systemPrompt) {
      prompt += `System: ${systemPrompt}\n\n`;
    }

    messages.forEach(msg => {
      prompt += `${msg.role === "user" ? "Human" : "Assistant"}: ${msg.content}\n`;
    });

    prompt += "Assistant:";

    return this.run(prompt, { model });
  }

  // ─── MULTI-MODEL PIPELINE ──────────────────────────────────────────────────

  async pipeline(stages) {
    const results = [];
    let context = {};

    for (const stage of stages) {
      const { name, model, prompt, transform } = stage;

      // Interpolate context into prompt
      let finalPrompt = prompt;
      Object.entries(context).forEach(([key, value]) => {
        finalPrompt = finalPrompt.replace(`{${key}}`, JSON.stringify(value));
      });

      const result = await this.run(finalPrompt, { model });

      // Transform result if needed
      const output = transform ? transform(result.response) : result.response;

      results.push({ stage: name, output, model: result.model });
      context[name] = output;
    }

    return { stages: results, context };
  }

  // ─── STATS & MONITORING ────────────────────────────────────────────────────

  trackStats(model, latency, success) {
    if (!this.stats.calls[model]) {
      this.stats.calls[model] = 0;
      this.stats.latency[model] = [];
      this.stats.errors[model] = 0;
    }

    this.stats.calls[model]++;
    this.stats.latency[model].push(latency);

    if (!success) {
      this.stats.errors[model]++;
    }

    // Keep only last 100 latencies
    if (this.stats.latency[model].length > 100) {
      this.stats.latency[model].shift();
    }
  }

  getStats() {
    const stats = {};

    Object.keys(this.models).forEach(model => {
      const latencies = this.stats.latency[model] || [];
      const avgLatency = latencies.length > 0
        ? latencies.reduce((a, b) => a + b, 0) / latencies.length
        : 0;

      stats[model] = {
        calls: this.stats.calls[model] || 0,
        errors: this.stats.errors[model] || 0,
        avgLatency: Math.round(avgLatency),
        successRate: this.stats.calls[model]
          ? ((this.stats.calls[model] - (this.stats.errors[model] || 0)) / this.stats.calls[model] * 100).toFixed(1) + "%"
          : "N/A"
      };
    });

    return stats;
  }

  estimateTokens(prompt, response) {
    // Rough estimation: ~4 chars per token
    const promptTokens = Math.ceil(prompt.length / 4);
    const responseTokens = Math.ceil((response?.length || 0) / 4);
    return { prompt: promptTokens, response: responseTokens, total: promptTokens + responseTokens };
  }

  // ─── MODEL INFO ────────────────────────────────────────────────────────────

  listModels() {
    return Object.entries(this.models).map(([key, model]) => ({
      key,
      ...model
    }));
  }

  getModel(key) {
    return this.models[key];
  }
}

export default AIRouter;
