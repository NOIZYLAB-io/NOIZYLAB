// ═══════════════════════════════════════════════════════════════════════════════
// TASK QUEUE - BACKGROUND JOB PROCESSING
// Queue, schedule, and execute tasks asynchronously
// ═══════════════════════════════════════════════════════════════════════════════

import { EventEmitter } from 'events';

export class TaskQueue extends EventEmitter {
  constructor(options = {}) {
    super();
    this.queues = new Map();
    this.workers = new Map();
    this.running = new Map();
    this.completed = [];
    this.failed = [];
    this.config = {
      maxRetries: 3,
      retryDelay: 1000,
      concurrency: 5,
      defaultQueue: "default",
      ...options
    };

    this.stats = {
      processed: 0,
      failed: 0,
      retried: 0,
      avgProcessTime: 0
    };

    // Create default queue
    this.createQueue("default");
    this.createQueue("high");
    this.createQueue("low");
  }

  // ─── QUEUE MANAGEMENT ──────────────────────────────────────────────────────

  createQueue(name, options = {}) {
    if (this.queues.has(name)) {
      return this.queues.get(name);
    }

    const queue = {
      name,
      tasks: [],
      paused: false,
      concurrency: options.concurrency || this.config.concurrency,
      runningCount: 0,
      ...options
    };

    this.queues.set(name, queue);
    return queue;
  }

  getQueue(name) {
    return this.queues.get(name);
  }

  deleteQueue(name) {
    if (name === "default") {
      throw new Error("Cannot delete default queue");
    }
    this.queues.delete(name);
  }

  // ─── TASK OPERATIONS ───────────────────────────────────────────────────────

  add(taskConfig) {
    const {
      name,
      handler,
      data = {},
      queue = this.config.defaultQueue,
      priority = 0,
      delay = 0,
      retries = this.config.maxRetries,
      timeout = 30000,
      onComplete,
      onFailed
    } = taskConfig;

    const task = {
      id: `task-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`,
      name,
      handler,
      data,
      queue,
      priority,
      delay,
      retries,
      retriesLeft: retries,
      timeout,
      onComplete,
      onFailed,
      status: "pending",
      createdAt: new Date().toISOString(),
      scheduledFor: delay > 0 ? new Date(Date.now() + delay).toISOString() : null,
      attempts: 0
    };

    const targetQueue = this.queues.get(queue);
    if (!targetQueue) {
      throw new Error(`Queue not found: ${queue}`);
    }

    // Insert by priority (higher priority first)
    const insertIndex = targetQueue.tasks.findIndex(t => t.priority < priority);
    if (insertIndex === -1) {
      targetQueue.tasks.push(task);
    } else {
      targetQueue.tasks.splice(insertIndex, 0, task);
    }

    this.emit("taskAdded", task);

    // Schedule delayed tasks
    if (delay > 0) {
      setTimeout(() => this.processQueue(queue), delay);
    } else {
      setImmediate(() => this.processQueue(queue));
    }

    return task;
  }

  addBulk(tasks, options = {}) {
    return tasks.map(task => this.add({ ...task, ...options }));
  }

  // ─── TASK PROCESSING ───────────────────────────────────────────────────────

  async processQueue(queueName) {
    const queue = this.queues.get(queueName);
    if (!queue || queue.paused) return;

    // Check concurrency
    if (queue.runningCount >= queue.concurrency) {
      return;
    }

    // Get next task
    const taskIndex = queue.tasks.findIndex(t => {
      if (t.status !== "pending") return false;
      if (t.scheduledFor && new Date(t.scheduledFor) > new Date()) return false;
      return true;
    });

    if (taskIndex === -1) return;

    const task = queue.tasks[taskIndex];
    queue.tasks.splice(taskIndex, 1);

    // Execute task
    await this.executeTask(task, queue);

    // Continue processing
    setImmediate(() => this.processQueue(queueName));
  }

  async executeTask(task, queue) {
    task.status = "running";
    task.startedAt = new Date().toISOString();
    task.attempts++;
    queue.runningCount++;

    this.running.set(task.id, task);
    this.emit("taskStarted", task);

    const startTime = Date.now();

    try {
      // Execute with timeout
      const result = await Promise.race([
        this.runHandler(task),
        this.createTimeout(task.timeout)
      ]);

      // Success
      task.status = "completed";
      task.completedAt = new Date().toISOString();
      task.duration = Date.now() - startTime;
      task.result = result;

      this.stats.processed++;
      this.updateAvgProcessTime(task.duration);

      this.completed.push(task);
      this.emit("taskCompleted", task);

      if (task.onComplete) {
        task.onComplete(result, task);
      }

    } catch (error) {
      task.error = error.message;

      // Check for retries
      if (task.retriesLeft > 0) {
        task.retriesLeft--;
        task.status = "pending";
        this.stats.retried++;

        // Re-queue with delay
        setTimeout(() => {
          queue.tasks.push(task);
          this.processQueue(queue.name);
        }, this.config.retryDelay * task.attempts);

        this.emit("taskRetrying", task);

      } else {
        // Failed permanently
        task.status = "failed";
        task.failedAt = new Date().toISOString();
        task.duration = Date.now() - startTime;

        this.stats.failed++;
        this.failed.push(task);
        this.emit("taskFailed", task);

        if (task.onFailed) {
          task.onFailed(error, task);
        }
      }
    } finally {
      queue.runningCount--;
      this.running.delete(task.id);
    }
  }

  async runHandler(task) {
    if (typeof task.handler === "function") {
      return await task.handler(task.data, task);
    } else if (typeof task.handler === "string" && this.workers.has(task.handler)) {
      const worker = this.workers.get(task.handler);
      return await worker(task.data, task);
    }
    throw new Error(`Invalid handler for task: ${task.name}`);
  }

  createTimeout(ms) {
    return new Promise((_, reject) => {
      setTimeout(() => reject(new Error("Task timeout")), ms);
    });
  }

  // ─── WORKERS ───────────────────────────────────────────────────────────────

  registerWorker(name, handler) {
    this.workers.set(name, handler);
  }

  unregisterWorker(name) {
    this.workers.delete(name);
  }

  // ─── QUEUE CONTROL ─────────────────────────────────────────────────────────

  pause(queueName = null) {
    if (queueName) {
      const queue = this.queues.get(queueName);
      if (queue) queue.paused = true;
    } else {
      this.queues.forEach(q => q.paused = true);
    }
  }

  resume(queueName = null) {
    if (queueName) {
      const queue = this.queues.get(queueName);
      if (queue) {
        queue.paused = false;
        this.processQueue(queueName);
      }
    } else {
      this.queues.forEach(q => {
        q.paused = false;
        this.processQueue(q.name);
      });
    }
  }

  // ─── TASK RETRIEVAL ────────────────────────────────────────────────────────

  getTask(taskId) {
    // Check running
    if (this.running.has(taskId)) {
      return this.running.get(taskId);
    }

    // Check queues
    for (const queue of this.queues.values()) {
      const task = queue.tasks.find(t => t.id === taskId);
      if (task) return task;
    }

    // Check completed/failed
    return this.completed.find(t => t.id === taskId) ||
           this.failed.find(t => t.id === taskId);
  }

  getPending(queueName = null) {
    if (queueName) {
      return this.queues.get(queueName)?.tasks.filter(t => t.status === "pending") || [];
    }

    const pending = [];
    this.queues.forEach(q => {
      pending.push(...q.tasks.filter(t => t.status === "pending"));
    });
    return pending;
  }

  getRunning() {
    return Array.from(this.running.values());
  }

  getCompleted(limit = 100) {
    return this.completed.slice(-limit);
  }

  getFailed(limit = 100) {
    return this.failed.slice(-limit);
  }

  // ─── STATS ─────────────────────────────────────────────────────────────────

  updateAvgProcessTime(duration) {
    const total = this.stats.processed;
    this.stats.avgProcessTime = (this.stats.avgProcessTime * (total - 1) + duration) / total;
  }

  getStats() {
    const queueStats = {};
    this.queues.forEach((q, name) => {
      queueStats[name] = {
        pending: q.tasks.filter(t => t.status === "pending").length,
        running: q.runningCount,
        paused: q.paused
      };
    });

    return {
      ...this.stats,
      avgProcessTime: Math.round(this.stats.avgProcessTime),
      running: this.running.size,
      queues: queueStats
    };
  }

  // ─── CLEANUP ───────────────────────────────────────────────────────────────

  clear(queueName = null) {
    if (queueName) {
      const queue = this.queues.get(queueName);
      if (queue) queue.tasks = [];
    } else {
      this.queues.forEach(q => q.tasks = []);
    }
  }

  clearCompleted() {
    this.completed = [];
  }

  clearFailed() {
    this.failed = [];
  }

  // ─── SCHEDULED TASKS ───────────────────────────────────────────────────────

  schedule(taskConfig, cronExpression) {
    // Simple cron-like scheduling
    const { interval, at } = this.parseCron(cronExpression);

    const scheduleNext = () => {
      const delay = this.calculateNextRun(interval, at);
      setTimeout(() => {
        this.add(taskConfig);
        scheduleNext();
      }, delay);
    };

    scheduleNext();
    return { scheduled: true, expression: cronExpression };
  }

  parseCron(expression) {
    // Simplified cron parsing
    // Supports: "every 5m", "every 1h", "at 09:00"
    if (expression.startsWith("every ")) {
      const match = expression.match(/every (\d+)(m|h|s)/);
      if (match) {
        const multipliers = { s: 1000, m: 60000, h: 3600000 };
        return { interval: parseInt(match[1]) * multipliers[match[2]] };
      }
    }
    if (expression.startsWith("at ")) {
      const time = expression.replace("at ", "");
      return { at: time };
    }
    return { interval: 3600000 }; // Default: 1 hour
  }

  calculateNextRun(interval, at) {
    if (interval) return interval;
    if (at) {
      const [hours, minutes] = at.split(":").map(Number);
      const next = new Date();
      next.setHours(hours, minutes, 0, 0);
      if (next <= new Date()) {
        next.setDate(next.getDate() + 1);
      }
      return next.getTime() - Date.now();
    }
    return 3600000;
  }
}

export default TaskQueue;
