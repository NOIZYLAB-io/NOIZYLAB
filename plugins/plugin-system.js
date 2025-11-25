// ═══════════════════════════════════════════════════════════════════════════════
// PLUGIN SYSTEM - EXTENSIBLE ARCHITECTURE
// Extend CODEMASTER with custom agents, generators, and capabilities
// ═══════════════════════════════════════════════════════════════════════════════

import { EventEmitter } from 'events';
import fs from 'fs';
import path from 'path';

export class PluginSystem extends EventEmitter {
  constructor(codemaster) {
    super();
    this.codemaster = codemaster;
    this.plugins = new Map();
    this.hooks = new Map();
    this.extensions = new Map();

    this.registerCoreHooks();
  }

  // ─── CORE HOOKS ────────────────────────────────────────────────────────────

  registerCoreHooks() {
    // Define hook points
    const hooks = [
      "beforeAgentCall",
      "afterAgentCall",
      "beforeGenerate",
      "afterGenerate",
      "beforeWorkflow",
      "afterWorkflow",
      "onError",
      "onTaskComplete",
      "onStartup",
      "onShutdown"
    ];

    hooks.forEach(hook => {
      this.hooks.set(hook, []);
    });
  }

  // ─── PLUGIN MANAGEMENT ─────────────────────────────────────────────────────

  async register(plugin) {
    const { id, name, version, description, init, hooks = {}, extensions = {} } = plugin;

    if (this.plugins.has(id)) {
      throw new Error(`Plugin already registered: ${id}`);
    }

    const pluginInstance = {
      id,
      name,
      version,
      description,
      status: "registered",
      registeredAt: new Date().toISOString()
    };

    // Register hooks
    Object.entries(hooks).forEach(([hookName, handler]) => {
      this.addHook(hookName, handler, id);
    });

    // Register extensions
    Object.entries(extensions).forEach(([type, items]) => {
      this.addExtensions(type, items, id);
    });

    // Initialize plugin
    if (typeof init === "function") {
      try {
        await init(this.codemaster, this);
        pluginInstance.status = "active";
      } catch (error) {
        pluginInstance.status = "error";
        pluginInstance.error = error.message;
      }
    } else {
      pluginInstance.status = "active";
    }

    this.plugins.set(id, pluginInstance);
    this.emit("pluginRegistered", pluginInstance);

    return pluginInstance;
  }

  unregister(pluginId) {
    const plugin = this.plugins.get(pluginId);

    if (!plugin) {
      throw new Error(`Plugin not found: ${pluginId}`);
    }

    // Remove hooks
    this.hooks.forEach((handlers, hookName) => {
      this.hooks.set(hookName, handlers.filter(h => h.pluginId !== pluginId));
    });

    // Remove extensions
    this.extensions.forEach((items, type) => {
      this.extensions.set(type, items.filter(i => i.pluginId !== pluginId));
    });

    this.plugins.delete(pluginId);
    this.emit("pluginUnregistered", { id: pluginId });
  }

  get(pluginId) {
    return this.plugins.get(pluginId);
  }

  list() {
    return Array.from(this.plugins.values());
  }

  // ─── HOOKS ─────────────────────────────────────────────────────────────────

  addHook(hookName, handler, pluginId = "core") {
    if (!this.hooks.has(hookName)) {
      this.hooks.set(hookName, []);
    }

    this.hooks.get(hookName).push({
      handler,
      pluginId,
      addedAt: new Date().toISOString()
    });
  }

  async runHooks(hookName, context = {}) {
    const handlers = this.hooks.get(hookName) || [];
    const results = [];

    for (const { handler, pluginId } of handlers) {
      try {
        const result = await handler(context, this.codemaster);
        results.push({ pluginId, success: true, result });
      } catch (error) {
        results.push({ pluginId, success: false, error: error.message });
        this.emit("hookError", { hookName, pluginId, error });
      }
    }

    return results;
  }

  // ─── EXTENSIONS ────────────────────────────────────────────────────────────

  addExtensions(type, items, pluginId) {
    if (!this.extensions.has(type)) {
      this.extensions.set(type, []);
    }

    const extensions = Array.isArray(items) ? items : [items];

    extensions.forEach(item => {
      this.extensions.get(type).push({
        ...item,
        pluginId,
        addedAt: new Date().toISOString()
      });
    });
  }

  getExtensions(type) {
    return this.extensions.get(type) || [];
  }

  // ─── PLUGIN LOADING ────────────────────────────────────────────────────────

  async loadFromDirectory(dir) {
    if (!fs.existsSync(dir)) {
      return [];
    }

    const loaded = [];
    const files = fs.readdirSync(dir);

    for (const file of files) {
      if (file.endsWith(".js") || file.endsWith(".mjs")) {
        try {
          const pluginPath = path.join(dir, file);
          const plugin = await import(pluginPath);

          if (plugin.default && plugin.default.id) {
            await this.register(plugin.default);
            loaded.push(plugin.default.id);
          }
        } catch (error) {
          this.emit("loadError", { file, error: error.message });
        }
      }
    }

    return loaded;
  }
}

// ─── PLUGIN TEMPLATE ─────────────────────────────────────────────────────────

export function createPlugin(config) {
  return {
    id: config.id,
    name: config.name || config.id,
    version: config.version || "1.0.0",
    description: config.description || "",

    // Hooks
    hooks: config.hooks || {},

    // Extensions (agents, generators, commands)
    extensions: config.extensions || {},

    // Initialization function
    init: config.init || null
  };
}

// ─── EXAMPLE PLUGINS ─────────────────────────────────────────────────────────

export const ExamplePlugins = {
  // Logger plugin
  logger: createPlugin({
    id: "logger",
    name: "Activity Logger",
    description: "Logs all CODEMASTER activity",
    hooks: {
      afterAgentCall: (ctx) => {
        console.log(`[LOG] Agent ${ctx.agent} called: ${ctx.task}`);
      },
      onError: (ctx) => {
        console.error(`[ERROR] ${ctx.error}`);
      }
    }
  }),

  // Metrics plugin
  metrics: createPlugin({
    id: "metrics",
    name: "Metrics Collector",
    description: "Collects performance metrics",
    init: (codemaster) => {
      codemaster.metrics = {
        calls: 0,
        errors: 0,
        avgResponseTime: 0
      };
    },
    hooks: {
      afterAgentCall: (ctx, codemaster) => {
        codemaster.metrics.calls++;
      },
      onError: (ctx, codemaster) => {
        codemaster.metrics.errors++;
      }
    }
  }),

  // Custom agent plugin
  customAgent: createPlugin({
    id: "custom-agent",
    name: "Custom Agent",
    description: "Adds a custom agent",
    extensions: {
      agents: [{
        id: "CUSTOM",
        name: "CUSTOM",
        role: "Custom Agent",
        emoji: "🎯",
        description: "A custom agent added via plugin",
        capabilities: ["custom-task"]
      }]
    }
  }),

  // Custom generator plugin
  customGenerator: createPlugin({
    id: "custom-generator",
    name: "Custom Generator",
    description: "Adds custom code generators",
    extensions: {
      generators: [{
        id: "custom",
        name: "Custom Template",
        description: "Generate custom code",
        generate: (spec) => ({
          type: "custom",
          content: `// Custom generated code\n// Spec: ${JSON.stringify(spec)}`
        })
      }]
    }
  })
};

export default PluginSystem;
