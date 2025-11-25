// ═══════════════════════════════════════════════════════════════════════════════
// METRICS COLLECTOR - REAL-TIME ANALYTICS & MONITORING
// Track performance, usage, and system health
// ═══════════════════════════════════════════════════════════════════════════════

import { EventEmitter } from 'events';

export class MetricsCollector extends EventEmitter {
  constructor(options = {}) {
    super();
    this.metrics = new Map();
    this.timers = new Map();
    this.history = new Map();
    this.alerts = [];
    this.config = {
      historySize: 1000,
      flushInterval: 60000,
      alertThresholds: {},
      ...options
    };

    this.initDefaultMetrics();
  }

  // ─── INITIALIZATION ────────────────────────────────────────────────────────

  initDefaultMetrics() {
    // System metrics
    this.createGauge("system.memory.used");
    this.createGauge("system.memory.total");
    this.createGauge("system.uptime");

    // Request metrics
    this.createCounter("requests.total");
    this.createCounter("requests.success");
    this.createCounter("requests.error");
    this.createHistogram("requests.duration");

    // Agent metrics
    this.createCounter("agents.calls");
    this.createHistogram("agents.duration");
    this.createCounter("agents.errors");

    // Task metrics
    this.createCounter("tasks.completed");
    this.createCounter("tasks.failed");
    this.createHistogram("tasks.duration");
    this.createGauge("tasks.queue.size");

    // Code generation
    this.createCounter("generation.total");
    this.createCounter("generation.lines");
    this.createHistogram("generation.duration");
  }

  // ─── METRIC TYPES ──────────────────────────────────────────────────────────

  createCounter(name) {
    this.metrics.set(name, {
      type: "counter",
      name,
      value: 0,
      labels: new Map()
    });
  }

  createGauge(name) {
    this.metrics.set(name, {
      type: "gauge",
      name,
      value: 0,
      labels: new Map()
    });
  }

  createHistogram(name, buckets = [10, 50, 100, 250, 500, 1000, 2500, 5000, 10000]) {
    this.metrics.set(name, {
      type: "histogram",
      name,
      buckets,
      values: [],
      count: 0,
      sum: 0
    });
  }

  // ─── METRIC OPERATIONS ─────────────────────────────────────────────────────

  increment(name, value = 1, labels = {}) {
    const metric = this.metrics.get(name);
    if (!metric || metric.type !== "counter") {
      this.createCounter(name);
      return this.increment(name, value, labels);
    }

    metric.value += value;

    // Track with labels
    const labelKey = JSON.stringify(labels);
    if (labelKey !== "{}") {
      const current = metric.labels.get(labelKey) || 0;
      metric.labels.set(labelKey, current + value);
    }

    this.recordHistory(name, metric.value);
    this.emit("metric", { name, type: "increment", value: metric.value, labels });

    return metric.value;
  }

  set(name, value, labels = {}) {
    const metric = this.metrics.get(name);
    if (!metric || metric.type !== "gauge") {
      this.createGauge(name);
      return this.set(name, value, labels);
    }

    metric.value = value;

    const labelKey = JSON.stringify(labels);
    if (labelKey !== "{}") {
      metric.labels.set(labelKey, value);
    }

    this.recordHistory(name, value);
    this.checkAlerts(name, value);
    this.emit("metric", { name, type: "gauge", value, labels });

    return value;
  }

  observe(name, value) {
    const metric = this.metrics.get(name);
    if (!metric || metric.type !== "histogram") {
      this.createHistogram(name);
      return this.observe(name, value);
    }

    metric.values.push(value);
    metric.count++;
    metric.sum += value;

    // Keep only recent values
    if (metric.values.length > this.config.historySize) {
      metric.values.shift();
    }

    this.emit("metric", { name, type: "histogram", value });

    return value;
  }

  // ─── TIMING ────────────────────────────────────────────────────────────────

  startTimer(name) {
    const timerId = `${name}-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
    this.timers.set(timerId, {
      name,
      startTime: Date.now()
    });
    return timerId;
  }

  endTimer(timerId) {
    const timer = this.timers.get(timerId);
    if (!timer) return null;

    const duration = Date.now() - timer.startTime;
    this.timers.delete(timerId);

    this.observe(timer.name, duration);
    return duration;
  }

  async time(name, fn) {
    const timerId = this.startTimer(name);
    try {
      return await fn();
    } finally {
      this.endTimer(timerId);
    }
  }

  // ─── QUERIES ───────────────────────────────────────────────────────────────

  get(name) {
    const metric = this.metrics.get(name);
    if (!metric) return null;

    switch (metric.type) {
      case "counter":
      case "gauge":
        return metric.value;

      case "histogram":
        return {
          count: metric.count,
          sum: metric.sum,
          avg: metric.count > 0 ? metric.sum / metric.count : 0,
          min: Math.min(...metric.values) || 0,
          max: Math.max(...metric.values) || 0,
          p50: this.percentile(metric.values, 50),
          p90: this.percentile(metric.values, 90),
          p99: this.percentile(metric.values, 99)
        };

      default:
        return null;
    }
  }

  getAll() {
    const all = {};
    this.metrics.forEach((metric, name) => {
      all[name] = this.get(name);
    });
    return all;
  }

  getByPrefix(prefix) {
    const filtered = {};
    this.metrics.forEach((metric, name) => {
      if (name.startsWith(prefix)) {
        filtered[name] = this.get(name);
      }
    });
    return filtered;
  }

  percentile(values, p) {
    if (values.length === 0) return 0;

    const sorted = [...values].sort((a, b) => a - b);
    const index = Math.ceil((p / 100) * sorted.length) - 1;
    return sorted[Math.max(0, index)];
  }

  // ─── HISTORY ───────────────────────────────────────────────────────────────

  recordHistory(name, value) {
    if (!this.history.has(name)) {
      this.history.set(name, []);
    }

    const history = this.history.get(name);
    history.push({
      value,
      timestamp: Date.now()
    });

    // Trim history
    while (history.length > this.config.historySize) {
      history.shift();
    }
  }

  getHistory(name, duration = 3600000) { // Last hour by default
    const history = this.history.get(name) || [];
    const cutoff = Date.now() - duration;

    return history.filter(h => h.timestamp >= cutoff);
  }

  // ─── ALERTS ────────────────────────────────────────────────────────────────

  setThreshold(name, options) {
    this.config.alertThresholds[name] = {
      min: options.min,
      max: options.max,
      onChange: options.onChange,
      callback: options.callback
    };
  }

  checkAlerts(name, value) {
    const threshold = this.config.alertThresholds[name];
    if (!threshold) return;

    let alert = null;

    if (threshold.max !== undefined && value > threshold.max) {
      alert = { name, type: "max_exceeded", value, threshold: threshold.max };
    }

    if (threshold.min !== undefined && value < threshold.min) {
      alert = { name, type: "min_exceeded", value, threshold: threshold.min };
    }

    if (alert) {
      alert.timestamp = new Date().toISOString();
      this.alerts.push(alert);
      this.emit("alert", alert);

      if (threshold.callback) {
        threshold.callback(alert);
      }
    }
  }

  getAlerts(limit = 100) {
    return this.alerts.slice(-limit);
  }

  clearAlerts() {
    this.alerts = [];
  }

  // ─── AGGREGATIONS ──────────────────────────────────────────────────────────

  rate(name, interval = 60000) {
    const history = this.getHistory(name, interval);
    if (history.length < 2) return 0;

    const first = history[0];
    const last = history[history.length - 1];
    const timeDiff = (last.timestamp - first.timestamp) / 1000; // seconds

    return timeDiff > 0 ? (last.value - first.value) / timeDiff : 0;
  }

  // ─── EXPORT ────────────────────────────────────────────────────────────────

  toPrometheus() {
    const lines = [];

    this.metrics.forEach((metric, name) => {
      const promName = name.replace(/\./g, "_");

      switch (metric.type) {
        case "counter":
          lines.push(`# TYPE ${promName} counter`);
          lines.push(`${promName} ${metric.value}`);
          break;

        case "gauge":
          lines.push(`# TYPE ${promName} gauge`);
          lines.push(`${promName} ${metric.value}`);
          break;

        case "histogram":
          lines.push(`# TYPE ${promName} histogram`);
          lines.push(`${promName}_count ${metric.count}`);
          lines.push(`${promName}_sum ${metric.sum}`);
          metric.buckets.forEach(bucket => {
            const count = metric.values.filter(v => v <= bucket).length;
            lines.push(`${promName}_bucket{le="${bucket}"} ${count}`);
          });
          break;
      }
    });

    return lines.join("\n");
  }

  toJSON() {
    return {
      timestamp: new Date().toISOString(),
      metrics: this.getAll(),
      alerts: this.alerts.slice(-10)
    };
  }

  // ─── RESET ─────────────────────────────────────────────────────────────────

  reset(name = null) {
    if (name) {
      const metric = this.metrics.get(name);
      if (metric) {
        if (metric.type === "histogram") {
          metric.values = [];
          metric.count = 0;
          metric.sum = 0;
        } else {
          metric.value = 0;
          metric.labels.clear();
        }
      }
    } else {
      this.metrics.forEach((metric, name) => this.reset(name));
    }
  }
}

export default MetricsCollector;
