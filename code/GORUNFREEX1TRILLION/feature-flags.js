/**
 * GORUNFREEX1TRILLION - FEATURE FLAGS
 * A/B Testing, Gradual Rollouts, Targeting Rules, Remote Config
 */

const { EventEmitter } = require('events');
const crypto = require('crypto');

// ============================================
// FEATURE FLAG MANAGER
// ============================================

class FeatureFlagManager extends EventEmitter {
  constructor(options = {}) {
    super();
    this.flags = new Map();
    this.overrides = new Map();
    this.experiments = new Map();
    this.analytics = new Map();
    this.syncInterval = options.syncInterval || 60000;
    this.storage = options.storage || new MemoryStorage();
  }

  // Define a feature flag
  define(key, config = {}) {
    const flag = new FeatureFlag({
      key,
      enabled: config.enabled ?? false,
      description: config.description || '',
      defaultValue: config.defaultValue ?? false,
      rules: config.rules || [],
      rolloutPercentage: config.rolloutPercentage ?? 100,
      variants: config.variants || null,
      metadata: config.metadata || {}
    });

    this.flags.set(key, flag);
    this.emit('flag:defined', { key, flag });
    return flag;
  }

  // Check if feature is enabled for a user
  isEnabled(key, context = {}) {
    // Check overrides first
    const override = this.overrides.get(`${key}:${context.userId}`);
    if (override !== undefined) return override;

    const flag = this.flags.get(key);
    if (!flag) return false;

    const result = flag.evaluate(context);
    this.trackEvaluation(key, context, result);
    return result;
  }

  // Get variant for A/B test
  getVariant(key, context = {}) {
    const flag = this.flags.get(key);
    if (!flag || !flag.variants) return null;

    const variant = flag.getVariant(context);
    this.trackVariant(key, context, variant);
    return variant;
  }

  // Get flag value (for remote config)
  getValue(key, context = {}, defaultValue = null) {
    const flag = this.flags.get(key);
    if (!flag) return defaultValue;

    if (!flag.evaluate(context)) return defaultValue;
    return flag.getValue(context) ?? defaultValue;
  }

  // Override flag for specific user
  setOverride(key, userId, value) {
    this.overrides.set(`${key}:${userId}`, value);
    this.emit('override:set', { key, userId, value });
  }

  clearOverride(key, userId) {
    this.overrides.delete(`${key}:${userId}`);
  }

  // Enable/disable flag globally
  enable(key) {
    const flag = this.flags.get(key);
    if (flag) {
      flag.enabled = true;
      this.emit('flag:enabled', { key });
    }
  }

  disable(key) {
    const flag = this.flags.get(key);
    if (flag) {
      flag.enabled = false;
      this.emit('flag:disabled', { key });
    }
  }

  // Set rollout percentage
  setRollout(key, percentage) {
    const flag = this.flags.get(key);
    if (flag) {
      flag.rolloutPercentage = Math.max(0, Math.min(100, percentage));
      this.emit('flag:rollout', { key, percentage: flag.rolloutPercentage });
    }
  }

  // Analytics tracking
  trackEvaluation(key, context, result) {
    const stats = this.analytics.get(key) || { evaluations: 0, enabled: 0, disabled: 0 };
    stats.evaluations++;
    result ? stats.enabled++ : stats.disabled++;
    this.analytics.set(key, stats);
  }

  trackVariant(key, context, variant) {
    const stats = this.analytics.get(`${key}:variants`) || {};
    stats[variant] = (stats[variant] || 0) + 1;
    this.analytics.set(`${key}:variants`, stats);
  }

  getAnalytics(key) {
    return {
      evaluations: this.analytics.get(key),
      variants: this.analytics.get(`${key}:variants`)
    };
  }

  // Bulk operations
  getAllFlags() {
    return Array.from(this.flags.values()).map(f => f.toJSON());
  }

  importFlags(flags) {
    flags.forEach(config => this.define(config.key, config));
  }

  exportFlags() {
    return this.getAllFlags();
  }

  // Persistence
  async save() {
    await this.storage.set('flags', this.exportFlags());
    await this.storage.set('overrides', Object.fromEntries(this.overrides));
  }

  async load() {
    const flags = await this.storage.get('flags');
    const overrides = await this.storage.get('overrides');

    if (flags) this.importFlags(flags);
    if (overrides) {
      Object.entries(overrides).forEach(([k, v]) => this.overrides.set(k, v));
    }
  }
}

// ============================================
// FEATURE FLAG
// ============================================

class FeatureFlag {
  constructor(config) {
    this.key = config.key;
    this.enabled = config.enabled;
    this.description = config.description;
    this.defaultValue = config.defaultValue;
    this.rules = config.rules;
    this.rolloutPercentage = config.rolloutPercentage;
    this.variants = config.variants;
    this.value = config.value;
    this.metadata = config.metadata;
    this.createdAt = Date.now();
    this.updatedAt = Date.now();
  }

  evaluate(context = {}) {
    if (!this.enabled) return false;

    // Check rules
    for (const rule of this.rules) {
      if (this.evaluateRule(rule, context)) {
        return rule.serve ?? true;
      }
    }

    // Check rollout percentage
    if (this.rolloutPercentage < 100) {
      const hash = this.hashContext(context);
      if (hash > this.rolloutPercentage) return false;
    }

    return this.defaultValue;
  }

  evaluateRule(rule, context) {
    const { attribute, operator, value } = rule;
    const contextValue = this.getContextValue(context, attribute);

    switch (operator) {
      case 'eq': case '==': return contextValue === value;
      case 'ne': case '!=': return contextValue !== value;
      case 'gt': case '>': return contextValue > value;
      case 'gte': case '>=': return contextValue >= value;
      case 'lt': case '<': return contextValue < value;
      case 'lte': case '<=': return contextValue <= value;
      case 'in': return Array.isArray(value) && value.includes(contextValue);
      case 'nin': return Array.isArray(value) && !value.includes(contextValue);
      case 'contains': return String(contextValue).includes(value);
      case 'startsWith': return String(contextValue).startsWith(value);
      case 'endsWith': return String(contextValue).endsWith(value);
      case 'matches': return new RegExp(value).test(String(contextValue));
      case 'exists': return contextValue !== undefined;
      case 'semver_gt': return this.compareSemver(contextValue, value) > 0;
      case 'semver_lt': return this.compareSemver(contextValue, value) < 0;
      case 'percentage': return this.hashContext(context) <= value;
      default: return false;
    }
  }

  getContextValue(context, path) {
    return path.split('.').reduce((obj, key) => obj?.[key], context);
  }

  getVariant(context) {
    if (!this.variants || this.variants.length === 0) return null;

    const hash = this.hashContext(context, this.key + ':variant');
    let cumulative = 0;

    for (const variant of this.variants) {
      cumulative += variant.weight || (100 / this.variants.length);
      if (hash <= cumulative) return variant.name;
    }

    return this.variants[0].name;
  }

  getValue(context) {
    if (this.variants) {
      const variant = this.getVariant(context);
      const v = this.variants.find(v => v.name === variant);
      return v?.value ?? this.value;
    }
    return this.value;
  }

  hashContext(context, salt = '') {
    const identifier = context.userId || context.sessionId || context.deviceId || 'anonymous';
    const str = `${this.key}:${identifier}:${salt}`;
    let hash = 0;
    for (let i = 0; i < str.length; i++) {
      hash = ((hash << 5) - hash) + str.charCodeAt(i);
      hash = hash & hash;
    }
    return Math.abs(hash % 100);
  }

  compareSemver(a, b) {
    const pa = String(a).split('.').map(Number);
    const pb = String(b).split('.').map(Number);
    for (let i = 0; i < 3; i++) {
      if ((pa[i] || 0) > (pb[i] || 0)) return 1;
      if ((pa[i] || 0) < (pb[i] || 0)) return -1;
    }
    return 0;
  }

  toJSON() {
    return {
      key: this.key,
      enabled: this.enabled,
      description: this.description,
      defaultValue: this.defaultValue,
      rules: this.rules,
      rolloutPercentage: this.rolloutPercentage,
      variants: this.variants,
      value: this.value,
      metadata: this.metadata,
      createdAt: this.createdAt,
      updatedAt: this.updatedAt
    };
  }
}

// ============================================
// A/B EXPERIMENT
// ============================================

class Experiment {
  constructor(config) {
    this.id = config.id || crypto.randomBytes(8).toString('hex');
    this.name = config.name;
    this.description = config.description || '';
    this.variants = config.variants || [
      { name: 'control', weight: 50 },
      { name: 'treatment', weight: 50 }
    ];
    this.metrics = config.metrics || [];
    this.status = config.status || 'draft'; // draft, running, paused, completed
    this.startDate = config.startDate || null;
    this.endDate = config.endDate || null;
    this.sampleSize = config.sampleSize || null;
    this.assignments = new Map();
    this.results = new Map();
  }

  assign(userId) {
    if (this.assignments.has(userId)) {
      return this.assignments.get(userId);
    }

    const hash = this.hashUser(userId);
    let cumulative = 0;
    let assigned = this.variants[0].name;

    for (const variant of this.variants) {
      cumulative += variant.weight;
      if (hash <= cumulative) {
        assigned = variant.name;
        break;
      }
    }

    this.assignments.set(userId, assigned);
    return assigned;
  }

  hashUser(userId) {
    let hash = 0;
    const str = `${this.id}:${userId}`;
    for (let i = 0; i < str.length; i++) {
      hash = ((hash << 5) - hash) + str.charCodeAt(i);
      hash = hash & hash;
    }
    return Math.abs(hash % 100);
  }

  trackConversion(userId, metricName, value = 1) {
    const variant = this.assignments.get(userId);
    if (!variant) return;

    const key = `${variant}:${metricName}`;
    const current = this.results.get(key) || { count: 0, sum: 0, values: [] };
    current.count++;
    current.sum += value;
    current.values.push(value);
    this.results.set(key, current);
  }

  getResults() {
    const results = {};

    for (const variant of this.variants) {
      results[variant.name] = {
        assignments: Array.from(this.assignments.values()).filter(v => v === variant.name).length,
        metrics: {}
      };

      for (const metric of this.metrics) {
        const key = `${variant.name}:${metric}`;
        const data = this.results.get(key) || { count: 0, sum: 0, values: [] };
        results[variant.name].metrics[metric] = {
          conversions: data.count,
          total: data.sum,
          rate: results[variant.name].assignments > 0
            ? (data.count / results[variant.name].assignments * 100).toFixed(2)
            : 0
        };
      }
    }

    return results;
  }

  start() { this.status = 'running'; this.startDate = Date.now(); }
  pause() { this.status = 'paused'; }
  complete() { this.status = 'completed'; this.endDate = Date.now(); }
}

// ============================================
// STORAGE
// ============================================

class MemoryStorage {
  constructor() { this.data = new Map(); }
  async get(key) { return this.data.get(key); }
  async set(key, value) { this.data.set(key, value); }
  async delete(key) { this.data.delete(key); }
}

// ============================================
// TARGETING RULES BUILDER
// ============================================

class RulesBuilder {
  constructor() { this.rules = []; }

  when(attribute) {
    this.currentAttribute = attribute;
    return this;
  }

  is(value) { return this.addRule('eq', value); }
  isNot(value) { return this.addRule('ne', value); }
  greaterThan(value) { return this.addRule('gt', value); }
  lessThan(value) { return this.addRule('lt', value); }
  isIn(values) { return this.addRule('in', values); }
  isNotIn(values) { return this.addRule('nin', values); }
  contains(value) { return this.addRule('contains', value); }
  matches(pattern) { return this.addRule('matches', pattern); }
  percentage(pct) { return this.addRule('percentage', pct); }

  addRule(operator, value) {
    this.rules.push({
      attribute: this.currentAttribute,
      operator,
      value,
      serve: true
    });
    return this;
  }

  serve(value) {
    if (this.rules.length > 0) {
      this.rules[this.rules.length - 1].serve = value;
    }
    return this;
  }

  build() { return this.rules; }
}

// ============================================
// EXPORTS
// ============================================

module.exports = {
  FeatureFlagManager,
  FeatureFlag,
  Experiment,
  RulesBuilder,
  MemoryStorage,

  createManager: (options) => new FeatureFlagManager(options),
  createExperiment: (config) => new Experiment(config),
  rules: () => new RulesBuilder()
};
