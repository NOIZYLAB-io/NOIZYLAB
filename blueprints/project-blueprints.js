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
  },

  "rag-system": {
    name: "RAG AI System",
    description: "Retrieval-Augmented Generation with vector search",
    category: "ai",
    files: [
      "index.js",
      "lib/embeddings.js",
      "lib/vector-store.js",
      "lib/retriever.js",
      "lib/generator.js",
      "api/routes.js",
      "package.json",
      "README.md"
    ],
    features: ["Vector embeddings", "Semantic search", "Context injection", "Streaming responses"],
    config: { ai: true, kv: ["VECTORS", "DOCUMENTS"] }
  },

  // ─── BROWSER EXTENSIONS ──────────────────────────────────────────────────────

  "chrome-extension": {
    name: "Chrome Extension",
    description: "Modern Chrome extension with popup and background script",
    category: "extension",
    files: [
      "manifest.json",
      "popup/popup.html",
      "popup/popup.js",
      "popup/popup.css",
      "background/service-worker.js",
      "content/content.js",
      "lib/storage.js",
      "README.md"
    ],
    features: ["Manifest V3", "Popup UI", "Background service worker", "Content scripts", "Storage API"]
  },

  "firefox-addon": {
    name: "Firefox Add-on",
    description: "Firefox browser add-on with WebExtension API",
    category: "extension",
    files: [
      "manifest.json",
      "popup/popup.html",
      "popup/popup.js",
      "background/background.js",
      "content/content.js",
      "README.md"
    ],
    features: ["WebExtension API", "Cross-browser compatible", "Popup", "Background scripts"]
  },

  // ─── PLATFORMS & APPS ────────────────────────────────────────────────────────

  "slack-app": {
    name: "Slack App",
    description: "Slack bot with slash commands and interactive messages",
    category: "bot",
    files: [
      "app.js",
      "handlers/commands.js",
      "handlers/events.js",
      "handlers/interactions.js",
      "lib/blocks.js",
      "lib/slack-api.js",
      "package.json",
      "README.md"
    ],
    features: ["Slash commands", "Event subscriptions", "Interactive messages", "Block Kit UI"]
  },

  "webhook-processor": {
    name: "Webhook Processor",
    description: "Multi-source webhook ingestion and processing",
    category: "backend",
    files: [
      "workers/webhook-handler.js",
      "processors/github.js",
      "processors/stripe.js",
      "processors/generic.js",
      "lib/signature.js",
      "lib/queue.js",
      "wrangler.toml",
      "package.json",
      "README.md"
    ],
    features: ["Signature verification", "Multi-source support", "Queue processing", "Retry logic"],
    config: { kv: ["WEBHOOK_LOGS", "QUEUE"], ai: false }
  },

  "realtime-dashboard": {
    name: "Real-time Dashboard",
    description: "Live analytics dashboard with WebSocket updates",
    category: "fullstack",
    files: [
      "server/index.js",
      "server/websocket.js",
      "server/routes/api.js",
      "client/index.html",
      "client/js/app.js",
      "client/js/charts.js",
      "client/js/websocket.js",
      "client/css/dashboard.css",
      "package.json",
      "README.md"
    ],
    features: ["WebSocket", "Real-time charts", "Live metrics", "Responsive design"]
  },

  "ecommerce-api": {
    name: "E-commerce API",
    description: "Complete e-commerce backend with products, cart, and checkout",
    category: "backend",
    files: [
      "server/index.js",
      "routes/products.js",
      "routes/cart.js",
      "routes/orders.js",
      "routes/payments.js",
      "middleware/auth.js",
      "models/product.js",
      "models/order.js",
      "models/user.js",
      "lib/stripe.js",
      "package.json",
      "README.md"
    ],
    features: ["Product catalog", "Shopping cart", "Order management", "Stripe payments", "Inventory"]
  },

  "blog-platform": {
    name: "Blog Platform",
    description: "Full-featured blog with markdown support and admin",
    category: "fullstack",
    files: [
      "server/index.js",
      "routes/posts.js",
      "routes/auth.js",
      "routes/admin.js",
      "lib/markdown.js",
      "lib/seo.js",
      "client/index.html",
      "client/admin.html",
      "client/css/blog.css",
      "package.json",
      "README.md"
    ],
    features: ["Markdown support", "SEO optimization", "Admin panel", "RSS feed", "Comments"]
  },

  // ─── INFRASTRUCTURE ──────────────────────────────────────────────────────────

  "api-gateway": {
    name: "API Gateway",
    description: "Edge API gateway with routing, auth, and rate limiting",
    category: "cloudflare",
    files: [
      "workers/gateway.js",
      "lib/router.js",
      "lib/auth.js",
      "lib/rate-limiter.js",
      "lib/transformer.js",
      "config/routes.js",
      "wrangler.toml",
      "package.json",
      "README.md"
    ],
    features: ["Request routing", "JWT auth", "Rate limiting", "Request transformation", "Caching"],
    config: { kv: ["RATE_LIMITS", "CACHE"], ai: false }
  },

  "cron-worker": {
    name: "Cron Worker",
    description: "Scheduled tasks on Cloudflare Workers",
    category: "cloudflare",
    files: [
      "workers/cron.js",
      "tasks/cleanup.js",
      "tasks/reports.js",
      "tasks/sync.js",
      "lib/notifications.js",
      "wrangler.toml",
      "package.json",
      "README.md"
    ],
    features: ["Scheduled triggers", "Multiple tasks", "Error handling", "Notifications"],
    config: { kv: ["TASK_LOGS"], triggers: ["0 * * * *", "0 0 * * *"] }
  },

  "auth-service": {
    name: "Authentication Service",
    description: "Complete auth system with JWT, OAuth, and MFA",
    category: "backend",
    files: [
      "server/index.js",
      "routes/auth.js",
      "routes/oauth.js",
      "routes/mfa.js",
      "middleware/jwt.js",
      "lib/password.js",
      "lib/totp.js",
      "lib/oauth-providers.js",
      "models/user.js",
      "models/session.js",
      "package.json",
      "README.md"
    ],
    features: ["JWT tokens", "OAuth2 (Google, GitHub)", "MFA/2FA", "Password hashing", "Session management"]
  },

  // ─── DEVELOPMENT TOOLS ───────────────────────────────────────────────────────

  "dev-proxy": {
    name: "Development Proxy",
    description: "Local dev proxy with request logging and mocking",
    category: "dev-tools",
    files: [
      "proxy.js",
      "lib/logger.js",
      "lib/mocker.js",
      "lib/transformer.js",
      "config/routes.json",
      "mocks/index.js",
      "package.json",
      "README.md"
    ],
    features: ["Request logging", "Response mocking", "Request rewriting", "CORS handling"]
  },

  "test-harness": {
    name: "Test Harness",
    description: "Complete testing setup with unit, integration, and e2e",
    category: "dev-tools",
    files: [
      "tests/unit/example.test.js",
      "tests/integration/api.test.js",
      "tests/e2e/flow.test.js",
      "tests/fixtures/index.js",
      "tests/helpers/index.js",
      "tests/mocks/index.js",
      "jest.config.js",
      "package.json",
      "README.md"
    ],
    features: ["Unit tests", "Integration tests", "E2E tests", "Fixtures", "Mocking"]
  },

  "monorepo-starter": {
    name: "Monorepo Starter",
    description: "Monorepo setup with workspaces and shared packages",
    category: "dev-tools",
    files: [
      "package.json",
      "packages/shared/package.json",
      "packages/shared/index.js",
      "packages/api/package.json",
      "packages/api/index.js",
      "packages/web/package.json",
      "packages/web/index.html",
      "turbo.json",
      "README.md"
    ],
    features: ["NPM workspaces", "Shared packages", "Turborepo", "Unified scripts"]
  },

  // ─── SPECIALIZED ─────────────────────────────────────────────────────────────

  "notification-service": {
    name: "Notification Service",
    description: "Multi-channel notification system (email, SMS, push)",
    category: "backend",
    files: [
      "server/index.js",
      "providers/email.js",
      "providers/sms.js",
      "providers/push.js",
      "providers/slack.js",
      "lib/template.js",
      "lib/queue.js",
      "routes/api.js",
      "package.json",
      "README.md"
    ],
    features: ["Email", "SMS", "Push notifications", "Slack", "Templates", "Queue"]
  },

  "file-processor": {
    name: "File Processor",
    description: "File upload, processing, and storage system",
    category: "backend",
    files: [
      "workers/upload.js",
      "processors/image.js",
      "processors/document.js",
      "processors/video.js",
      "lib/storage.js",
      "lib/queue.js",
      "wrangler.toml",
      "package.json",
      "README.md"
    ],
    features: ["Multi-file upload", "Image processing", "R2 storage", "Progress tracking"],
    config: { r2: ["FILES"], kv: ["METADATA"] }
  },

  "search-service": {
    name: "Search Service",
    description: "Full-text search with indexing and autocomplete",
    category: "backend",
    files: [
      "server/index.js",
      "lib/indexer.js",
      "lib/search.js",
      "lib/autocomplete.js",
      "lib/ranking.js",
      "routes/api.js",
      "package.json",
      "README.md"
    ],
    features: ["Full-text search", "Autocomplete", "Fuzzy matching", "Ranking", "Faceted search"]
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
