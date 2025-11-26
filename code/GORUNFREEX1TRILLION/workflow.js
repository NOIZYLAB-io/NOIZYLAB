/**
 * GORUNFREEX1TRILLION - WORKFLOW AUTOMATION ENGINE
 * Visual automation builder, Triggers, Actions, Conditions (like Zapier/n8n)
 */

const { EventEmitter } = require('events');
const crypto = require('crypto');

// ============================================
// WORKFLOW ENGINE
// ============================================

class WorkflowEngine extends EventEmitter {
  constructor() {
    super();
    this.workflows = new Map();
    this.triggers = new Map();
    this.actions = new Map();
    this.executions = new Map();
    this.setupDefaultActions();
  }

  setupDefaultActions() {
    // HTTP Request
    this.registerAction('http.request', async (config, context) => {
      const { url, method = 'GET', headers = {}, body } = config;
      console.log(`[HTTP] ${method} ${url}`);
      return { status: 200, data: { mock: true } };
    });

    // Delay
    this.registerAction('delay', async (config) => {
      await new Promise(r => setTimeout(r, config.ms || 1000));
      return { delayed: config.ms };
    });

    // Transform data
    this.registerAction('transform', async (config, context) => {
      const { expression } = config;
      return eval(`(${expression})`)(context.data);
    });

    // Filter
    this.registerAction('filter', async (config, context) => {
      const { condition } = config;
      const pass = eval(`(${condition})`)(context.data);
      return { pass, data: pass ? context.data : null };
    });

    // Log
    this.registerAction('log', async (config, context) => {
      console.log(`[Workflow Log]`, config.message || context.data);
      return { logged: true };
    });

    // Set variable
    this.registerAction('setVariable', async (config, context) => {
      context.variables[config.name] = config.value;
      return { set: config.name };
    });

    // Send email
    this.registerAction('email.send', async (config) => {
      console.log(`[Email] Sending to ${config.to}: ${config.subject}`);
      return { sent: true, to: config.to };
    });

    // Webhook
    this.registerAction('webhook', async (config) => {
      console.log(`[Webhook] POST ${config.url}`);
      return { delivered: true };
    });

    // Database operations
    this.registerAction('db.query', async (config) => {
      console.log(`[DB] Query: ${config.query}`);
      return { rows: [] };
    });

    this.registerAction('db.insert', async (config) => {
      console.log(`[DB] Insert into ${config.table}`);
      return { inserted: true, id: crypto.randomBytes(8).toString('hex') };
    });
  }

  registerAction(name, handler) {
    this.actions.set(name, handler);
    return this;
  }

  registerTrigger(name, config) {
    this.triggers.set(name, config);
    return this;
  }

  createWorkflow(config) {
    const workflow = new Workflow(config, this);
    this.workflows.set(workflow.id, workflow);
    this.emit('workflow:created', { workflowId: workflow.id });
    return workflow;
  }

  getWorkflow(id) { return this.workflows.get(id); }

  deleteWorkflow(id) {
    const workflow = this.workflows.get(id);
    if (workflow) {
      workflow.stop();
      this.workflows.delete(id);
      this.emit('workflow:deleted', { workflowId: id });
    }
  }

  async executeAction(actionName, config, context) {
    const handler = this.actions.get(actionName);
    if (!handler) throw new Error(`Action '${actionName}' not found`);
    return handler(config, context);
  }

  // Trigger a workflow by trigger name
  async trigger(triggerName, data) {
    const results = [];
    for (const [id, workflow] of this.workflows) {
      if (workflow.trigger?.type === triggerName && workflow.enabled) {
        const result = await workflow.execute(data);
        results.push({ workflowId: id, result });
      }
    }
    return results;
  }

  getWorkflows() { return Array.from(this.workflows.values()); }
  getExecutions() { return Array.from(this.executions.values()); }
}

// ============================================
// WORKFLOW
// ============================================

class Workflow extends EventEmitter {
  constructor(config, engine) {
    super();
    this.id = config.id || crypto.randomBytes(8).toString('hex');
    this.name = config.name || 'Untitled Workflow';
    this.description = config.description || '';
    this.engine = engine;
    this.trigger = config.trigger || null;
    this.nodes = new Map();
    this.connections = [];
    this.enabled = config.enabled !== false;
    this.createdAt = Date.now();
    this.lastRunAt = null;
    this.runCount = 0;

    if (config.nodes) {
      config.nodes.forEach(n => this.addNode(n));
    }
    if (config.connections) {
      this.connections = config.connections;
    }
  }

  addNode(config) {
    const node = new WorkflowNode(config);
    this.nodes.set(node.id, node);
    return node;
  }

  removeNode(nodeId) {
    this.nodes.delete(nodeId);
    this.connections = this.connections.filter(c => c.from !== nodeId && c.to !== nodeId);
  }

  connect(fromNodeId, toNodeId, condition = null) {
    this.connections.push({ from: fromNodeId, to: toNodeId, condition });
    return this;
  }

  getNextNodes(nodeId) {
    return this.connections
      .filter(c => c.from === nodeId)
      .map(c => ({ node: this.nodes.get(c.to), condition: c.condition }));
  }

  async execute(inputData = {}) {
    const execution = new WorkflowExecution(this);
    this.engine.executions.set(execution.id, execution);

    execution.start(inputData);
    this.emit('execution:started', { executionId: execution.id });

    try {
      // Find start node (trigger or first node)
      const startNode = this.trigger
        ? Array.from(this.nodes.values()).find(n => n.type === 'trigger')
        : Array.from(this.nodes.values())[0];

      if (!startNode) throw new Error('No start node found');

      await this.executeNode(startNode, execution);

      execution.complete();
      this.lastRunAt = Date.now();
      this.runCount++;
      this.emit('execution:completed', { executionId: execution.id });

    } catch (error) {
      execution.fail(error);
      this.emit('execution:failed', { executionId: execution.id, error });
    }

    return execution.getResult();
  }

  async executeNode(node, execution) {
    execution.setCurrentNode(node.id);

    try {
      const input = execution.getNodeInput(node.id);
      const result = await node.execute(this.engine, execution.context, input);

      execution.recordNodeResult(node.id, result);

      // Execute next nodes
      const nextNodes = this.getNextNodes(node.id);
      for (const { node: nextNode, condition } of nextNodes) {
        if (!nextNode) continue;

        // Check condition
        if (condition) {
          const pass = this.evaluateCondition(condition, result, execution.context);
          if (!pass) continue;
        }

        await this.executeNode(nextNode, execution);
      }

    } catch (error) {
      execution.recordNodeError(node.id, error);
      throw error;
    }
  }

  evaluateCondition(condition, data, context) {
    try {
      const fn = new Function('data', 'context', `return ${condition}`);
      return fn(data, context);
    } catch {
      return false;
    }
  }

  enable() { this.enabled = true; }
  disable() { this.enabled = false; }
  stop() { this.disable(); }

  toJSON() {
    return {
      id: this.id,
      name: this.name,
      description: this.description,
      trigger: this.trigger,
      nodes: Array.from(this.nodes.values()).map(n => n.toJSON()),
      connections: this.connections,
      enabled: this.enabled,
      createdAt: this.createdAt,
      lastRunAt: this.lastRunAt,
      runCount: this.runCount
    };
  }
}

// ============================================
// WORKFLOW NODE
// ============================================

class WorkflowNode {
  constructor(config) {
    this.id = config.id || crypto.randomBytes(6).toString('hex');
    this.type = config.type;
    this.name = config.name || config.type;
    this.config = config.config || {};
    this.position = config.position || { x: 0, y: 0 };
  }

  async execute(engine, context, input) {
    // Handle built-in node types
    switch (this.type) {
      case 'trigger':
        return input;

      case 'condition':
        const pass = engine.evaluateCondition?.(this.config.condition, input, context) ?? true;
        return { pass, data: input };

      case 'loop':
        const items = Array.isArray(input) ? input : [input];
        const results = [];
        for (const item of items) {
          results.push(item);
        }
        return results;

      case 'merge':
        return { merged: input };

      case 'split':
        return Array.isArray(input) ? input : [input];

      default:
        return engine.executeAction(this.type, this.config, { ...context, data: input });
    }
  }

  toJSON() {
    return {
      id: this.id,
      type: this.type,
      name: this.name,
      config: this.config,
      position: this.position
    };
  }
}

// ============================================
// WORKFLOW EXECUTION
// ============================================

class WorkflowExecution {
  constructor(workflow) {
    this.id = crypto.randomBytes(8).toString('hex');
    this.workflowId = workflow.id;
    this.status = 'pending';
    this.context = { variables: {}, data: null };
    this.nodeResults = new Map();
    this.nodeErrors = new Map();
    this.currentNodeId = null;
    this.startedAt = null;
    this.completedAt = null;
    this.error = null;
  }

  start(inputData) {
    this.status = 'running';
    this.startedAt = Date.now();
    this.context.data = inputData;
  }

  complete() {
    this.status = 'completed';
    this.completedAt = Date.now();
  }

  fail(error) {
    this.status = 'failed';
    this.completedAt = Date.now();
    this.error = error.message;
  }

  setCurrentNode(nodeId) { this.currentNodeId = nodeId; }

  recordNodeResult(nodeId, result) {
    this.nodeResults.set(nodeId, result);
    this.context.data = result;
  }

  recordNodeError(nodeId, error) {
    this.nodeErrors.set(nodeId, error.message);
  }

  getNodeInput(nodeId) {
    return this.context.data;
  }

  getResult() {
    return {
      id: this.id,
      workflowId: this.workflowId,
      status: this.status,
      data: this.context.data,
      nodeResults: Object.fromEntries(this.nodeResults),
      errors: Object.fromEntries(this.nodeErrors),
      duration: this.completedAt ? this.completedAt - this.startedAt : null,
      error: this.error
    };
  }
}

// ============================================
// WORKFLOW BUILDER (FLUENT API)
// ============================================

class WorkflowBuilder {
  constructor(engine) {
    this.engine = engine;
    this.config = { nodes: [], connections: [] };
    this.lastNodeId = null;
  }

  name(n) { this.config.name = n; return this; }
  description(d) { this.config.description = d; return this; }

  trigger(type, config = {}) {
    const node = { id: 'trigger', type: 'trigger', name: type, config };
    this.config.trigger = { type, config };
    this.config.nodes.push(node);
    this.lastNodeId = 'trigger';
    return this;
  }

  then(type, config = {}, name) {
    const id = crypto.randomBytes(4).toString('hex');
    this.config.nodes.push({ id, type, name: name || type, config });
    if (this.lastNodeId) {
      this.config.connections.push({ from: this.lastNodeId, to: id });
    }
    this.lastNodeId = id;
    return this;
  }

  condition(expression) {
    const id = crypto.randomBytes(4).toString('hex');
    this.config.nodes.push({ id, type: 'condition', name: 'Condition', config: { condition: expression } });
    if (this.lastNodeId) {
      this.config.connections.push({ from: this.lastNodeId, to: id });
    }
    this.lastNodeId = id;
    return this;
  }

  branch(truePath, falsePath) {
    const conditionId = this.lastNodeId;

    if (truePath) {
      const trueId = crypto.randomBytes(4).toString('hex');
      this.config.nodes.push({ id: trueId, ...truePath });
      this.config.connections.push({ from: conditionId, to: trueId, condition: 'data.pass === true' });
    }

    if (falsePath) {
      const falseId = crypto.randomBytes(4).toString('hex');
      this.config.nodes.push({ id: falseId, ...falsePath });
      this.config.connections.push({ from: conditionId, to: falseId, condition: 'data.pass === false' });
    }

    return this;
  }

  loop(itemsExpression) {
    return this.then('loop', { items: itemsExpression }, 'Loop');
  }

  delay(ms) {
    return this.then('delay', { ms }, 'Delay');
  }

  http(url, method = 'GET', config = {}) {
    return this.then('http.request', { url, method, ...config }, 'HTTP Request');
  }

  email(to, subject, body) {
    return this.then('email.send', { to, subject, body }, 'Send Email');
  }

  webhook(url, payload) {
    return this.then('webhook', { url, payload }, 'Webhook');
  }

  log(message) {
    return this.then('log', { message }, 'Log');
  }

  transform(expression) {
    return this.then('transform', { expression }, 'Transform');
  }

  build() {
    return this.engine.createWorkflow(this.config);
  }
}

// ============================================
// CRON SCHEDULER
// ============================================

class CronScheduler extends EventEmitter {
  constructor(engine) {
    super();
    this.engine = engine;
    this.jobs = new Map();
    this.timers = new Map();
  }

  schedule(workflowId, cronExpression, data = {}) {
    const job = {
      id: crypto.randomBytes(6).toString('hex'),
      workflowId,
      cron: cronExpression,
      data,
      nextRun: this.getNextRun(cronExpression),
      enabled: true
    };

    this.jobs.set(job.id, job);
    this.scheduleNext(job);

    return job;
  }

  getNextRun(cron) {
    // Simplified - returns next minute for demo
    return Date.now() + 60000;
  }

  scheduleNext(job) {
    if (!job.enabled) return;

    const delay = job.nextRun - Date.now();
    if (delay <= 0) {
      job.nextRun = this.getNextRun(job.cron);
      this.scheduleNext(job);
      return;
    }

    const timer = setTimeout(async () => {
      if (!job.enabled) return;

      this.emit('job:executing', { jobId: job.id });
      await this.engine.getWorkflow(job.workflowId)?.execute(job.data);

      job.nextRun = this.getNextRun(job.cron);
      this.scheduleNext(job);
    }, delay);

    this.timers.set(job.id, timer);
  }

  cancel(jobId) {
    const timer = this.timers.get(jobId);
    if (timer) clearTimeout(timer);
    this.jobs.delete(jobId);
    this.timers.delete(jobId);
  }

  pause(jobId) {
    const job = this.jobs.get(jobId);
    if (job) job.enabled = false;
  }

  resume(jobId) {
    const job = this.jobs.get(jobId);
    if (job) {
      job.enabled = true;
      job.nextRun = this.getNextRun(job.cron);
      this.scheduleNext(job);
    }
  }

  getJobs() { return Array.from(this.jobs.values()); }
}

// ============================================
// EXPORTS
// ============================================

module.exports = {
  WorkflowEngine,
  Workflow,
  WorkflowNode,
  WorkflowExecution,
  WorkflowBuilder,
  CronScheduler,

  createEngine: () => new WorkflowEngine(),
  createBuilder: (engine) => new WorkflowBuilder(engine),
  createScheduler: (engine) => new CronScheduler(engine)
};
