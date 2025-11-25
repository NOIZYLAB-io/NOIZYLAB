// ═══════════════════════════════════════════════════════════════════════════════
// PROJECT BLUEPRINTS - PRE-BUILT PROJECT TEMPLATES
// One command to generate complete, production-ready projects
// ═══════════════════════════════════════════════════════════════════════════════

export const BLUEPRINTS = {
  // ─── CLOUDFLARE STACK ──────────────────────────────────────────────────────

  "cf-email-system": {
    name: "Cloudflare Email System",
    description: "AI-powered email processing with agent routing",
    category: "cloudflare",
    files: [
      "workers/email-worker.js",
      "workers/api.js",
      "wrangler.toml",
      "package.json",
      "README.md"
    ],
    features: ["Email routing", "AI analysis", "Spam detection", "Webhooks"],
    config: {
      kv: ["MAIL_LOGS", "AGENTS_STATE"],
      ai: true,
      email: true
    }
  },

  "cf-api": {
    name: "Cloudflare API",
    description: "REST API on Cloudflare Workers with KV storage",
    category: "cloudflare",
    files: [
      "workers/api.js",
      "wrangler.toml",
      "package.json",
      "README.md"
    ],
    features: ["CRUD operations", "KV storage", "Authentication", "Rate limiting"],
    config: {
      kv: ["DATA"],
      auth: true
    }
  },

  "cf-ai-agent": {
    name: "Cloudflare AI Agent",
    description: "AI-powered agent with Workers AI",
    category: "cloudflare",
    files: [
      "workers/agent.js",
      "wrangler.toml",
      "package.json",
      "README.md"
    ],
    features: ["AI chat", "Context memory", "Tool calling", "Streaming"],
    config: {
      ai: true,
      kv: ["MEMORY"]
    }
  },

  // ─── CLI TOOLS ─────────────────────────────────────────────────────────────

  "cli-tool": {
    name: "CLI Tool",
    description: "Full-featured command-line interface",
    category: "cli",
    files: [
      "cli.js",
      "lib/commands.js",
      "lib/utils.js",
      "package.json",
      "README.md"
    ],
    features: ["Colorful output", "Multiple commands", "Config management", "Interactive mode"]
  },

  "cli-ai": {
    name: "AI CLI Assistant",
    description: "CLI with AI capabilities",
    category: "cli",
    files: [
      "cli.js",
      "lib/ai.js",
      "lib/prompts.js",
      "package.json",
      "README.md"
    ],
    features: ["AI chat", "Code generation", "File analysis", "Natural language commands"]
  },

  // ─── FULL STACK ────────────────────────────────────────────────────────────

  "fullstack-app": {
    name: "Full Stack Application",
    description: "Complete web application with API and frontend",
    category: "fullstack",
    files: [
      "server/index.js",
      "server/routes/api.js",
      "server/middleware/auth.js",
      "client/index.html",
      "client/app.js",
      "client/style.css",
      "package.json",
      "README.md"
    ],
    features: ["Express server", "REST API", "Static frontend", "Authentication"]
  },

  "saas-starter": {
    name: "SaaS Starter Kit",
    description: "Complete SaaS boilerplate",
    category: "fullstack",
    files: [
      "server/index.js",
      "server/routes/auth.js",
      "server/routes/api.js",
      "server/routes/billing.js",
      "server/middleware/auth.js",
      "server/models/user.js",
      "client/index.html",
      "package.json",
      "README.md"
    ],
    features: ["User auth", "Subscription billing", "Dashboard", "API keys"]
  },

  // ─── BOTS & AUTOMATION ─────────────────────────────────────────────────────

  "discord-bot": {
    name: "Discord Bot",
    description: "Feature-rich Discord bot",
    category: "bot",
    files: [
      "bot.js",
      "commands/index.js",
      "events/index.js",
      "utils/embed.js",
      "package.json",
      "README.md"
    ],
    features: ["Slash commands", "Event handling", "Embed messages", "Database integration"]
  },

  "telegram-bot": {
    name: "Telegram Bot",
    description: "Telegram bot with inline keyboards",
    category: "bot",
    files: [
      "bot.js",
      "handlers/commands.js",
      "handlers/callbacks.js",
      "utils/keyboard.js",
      "package.json",
      "README.md"
    ],
    features: ["Commands", "Inline keyboards", "Callback queries", "Webhooks"]
  },

  "automation-suite": {
    name: "Automation Suite",
    description: "Task automation with scheduling",
    category: "automation",
    files: [
      "index.js",
      "tasks/index.js",
      "scheduler.js",
      "config.json",
      "package.json",
      "README.md"
    ],
    features: ["Cron jobs", "Task queue", "Retry logic", "Notifications"]
  },

  // ─── MICROSERVICES ─────────────────────────────────────────────────────────

  "microservice": {
    name: "Microservice",
    description: "Lightweight microservice template",
    category: "backend",
    files: [
      "service.js",
      "routes/health.js",
      "routes/api.js",
      "middleware/index.js",
      "Dockerfile",
      "docker-compose.yml",
      "package.json",
      "README.md"
    ],
    features: ["Health checks", "Docker ready", "Logging", "Metrics"]
  },

  "graphql-api": {
    name: "GraphQL API",
    description: "GraphQL server with subscriptions",
    category: "backend",
    files: [
      "server.js",
      "schema/index.js",
      "resolvers/index.js",
      "models/index.js",
      "package.json",
      "README.md"
    ],
    features: ["Queries", "Mutations", "Subscriptions", "Authentication"]
  },

  // ─── DATA & AI ─────────────────────────────────────────────────────────────

  "data-pipeline": {
    name: "Data Pipeline",
    description: "ETL data processing pipeline",
    category: "data",
    files: [
      "pipeline.js",
      "extractors/index.js",
      "transformers/index.js",
      "loaders/index.js",
      "package.json",
      "README.md"
    ],
    features: ["ETL", "Batch processing", "Error handling", "Logging"]
  },

  "ml-service": {
    name: "ML Service",
    description: "Machine learning inference service",
    category: "ai",
    files: [
      "service.js",
      "models/index.js",
      "inference/index.js",
      "utils/preprocess.js",
      "package.json",
      "README.md"
    ],
    features: ["Model serving", "Preprocessing", "Batch inference", "API"]
  }
};

// ─── BLUEPRINT GENERATOR ─────────────────────────────────────────────────────

export class BlueprintGenerator {
  constructor() {
    this.blueprints = BLUEPRINTS;
  }

  list(category = null) {
    const entries = Object.entries(this.blueprints);

    if (category) {
      return entries
        .filter(([_, bp]) => bp.category === category)
        .map(([id, bp]) => ({ id, ...bp }));
    }

    return entries.map(([id, bp]) => ({ id, ...bp }));
  }

  getCategories() {
    const categories = new Set();
    Object.values(this.blueprints).forEach(bp => categories.add(bp.category));
    return Array.from(categories);
  }

  get(id) {
    return this.blueprints[id];
  }

  async generate(id, options = {}) {
    const blueprint = this.blueprints[id];

    if (!blueprint) {
      throw new Error(`Blueprint not found: ${id}`);
    }

    const { name = blueprint.name.toLowerCase().replace(/\s+/g, "-"), outputDir = "." } = options;

    // Generate project structure
    const files = await this.generateFiles(blueprint, name, options);

    return {
      blueprint: id,
      name,
      outputDir,
      files,
      features: blueprint.features,
      config: blueprint.config
    };
  }

  async generateFiles(blueprint, name, options) {
    const files = [];

    // Generate each file based on the blueprint
    for (const filePath of blueprint.files) {
      const content = await this.generateFileContent(filePath, blueprint, name, options);
      files.push({ path: filePath, content });
    }

    return files;
  }

  async generateFileContent(filePath, blueprint, name, options) {
    const ext = filePath.split(".").pop();

    switch (ext) {
      case "json":
        if (filePath === "package.json") {
          return this.generatePackageJson(blueprint, name);
        }
        return "{}";

      case "md":
        if (filePath === "README.md") {
          return this.generateReadme(blueprint, name);
        }
        return "";

      case "toml":
        if (filePath === "wrangler.toml") {
          return this.generateWranglerToml(blueprint, name);
        }
        return "";

      case "js":
        return this.generateJsFile(filePath, blueprint, name);

      default:
        return `// ${filePath}\n// Generated by CODEMASTER`;
    }
  }

  generatePackageJson(blueprint, name) {
    return JSON.stringify({
      name,
      version: "1.0.0",
      description: blueprint.description,
      type: "module",
      scripts: {
        start: "node index.js",
        dev: "nodemon index.js",
        test: "node --test",
        build: "echo 'Build'"
      },
      keywords: blueprint.features.map(f => f.toLowerCase().replace(/\s+/g, "-")),
      author: "CODEMASTER",
      license: "MIT"
    }, null, 2);
  }

  generateReadme(blueprint, name) {
    return `# ${name}

${blueprint.description}

## Features

${blueprint.features.map(f => `- ${f}`).join("\n")}

## Getting Started

\`\`\`bash
npm install
npm run dev
\`\`\`

## Generated by CODEMASTER
`;
  }

  generateWranglerToml(blueprint, name) {
    let config = `name = "${name}"
main = "workers/index.js"
compatibility_date = "2024-12-01"
`;

    if (blueprint.config?.kv) {
      config += "\nkv_namespaces = [\n";
      blueprint.config.kv.forEach((ns, i) => {
        config += `  { binding = "${ns}", id = "YOUR_${ns}_ID" }${i < blueprint.config.kv.length - 1 ? "," : ""}\n`;
      });
      config += "]\n";
    }

    if (blueprint.config?.ai) {
      config += "\n[ai]\nbinding = \"AI\"\n";
    }

    return config;
  }

  generateJsFile(filePath, blueprint, name) {
    return `// ═══════════════════════════════════════════════════════════════════════════════
// ${name.toUpperCase()} - ${filePath}
// Generated by CODEMASTER
// ═══════════════════════════════════════════════════════════════════════════════

// TODO: Implement ${filePath}

export default {};
`;
  }
}

export default BlueprintGenerator;
