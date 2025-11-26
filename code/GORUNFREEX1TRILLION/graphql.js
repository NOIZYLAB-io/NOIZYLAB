/**
 * GORUNFREEX1TRILLION - GRAPHQL ENGINE
 * Schema builder, resolvers, subscriptions, directives
 */

const { EventEmitter } = require('events');
const crypto = require('crypto');

// ============================================
// TYPE SYSTEM
// ============================================

const GraphQLTypes = {
  ID: 'ID', String: 'String', Int: 'Int', Float: 'Float', Boolean: 'Boolean',
  List: (type) => `[${type}]`, NonNull: (type) => `${type}!`,
  ListNonNull: (type) => `[${type}!]!`
};

class TypeBuilder {
  constructor(name) {
    this.name = name;
    this.fields = {};
    this.interfaces = [];
    this.description = '';
  }

  describe(desc) { this.description = desc; return this; }
  implements(...interfaces) { this.interfaces.push(...interfaces); return this; }

  field(name, type, options = {}) {
    this.fields[name] = { type, ...options };
    return this;
  }

  id(name = 'id') { return this.field(name, 'ID!'); }
  string(name, nullable = true) { return this.field(name, nullable ? 'String' : 'String!'); }
  int(name, nullable = true) { return this.field(name, nullable ? 'Int' : 'Int!'); }
  float(name, nullable = true) { return this.field(name, nullable ? 'Float' : 'Float!'); }
  boolean(name, nullable = true) { return this.field(name, nullable ? 'Boolean' : 'Boolean!'); }
  list(name, type) { return this.field(name, `[${type}]`); }
  ref(name, type, nullable = true) { return this.field(name, nullable ? type : `${type}!`); }

  build() {
    const impl = this.interfaces.length ? ` implements ${this.interfaces.join(' & ')}` : '';
    const desc = this.description ? `"""\n${this.description}\n"""\n` : '';
    const fields = Object.entries(this.fields)
      .map(([name, f]) => {
        const args = f.args ? `(${Object.entries(f.args).map(([k, v]) => `${k}: ${v}`).join(', ')})` : '';
        const fieldDesc = f.description ? `  """\n  ${f.description}\n  """\n` : '';
        return `${fieldDesc}  ${name}${args}: ${f.type}`;
      }).join('\n');
    return `${desc}type ${this.name}${impl} {\n${fields}\n}`;
  }
}

class InputBuilder {
  constructor(name) { this.name = name; this.fields = {}; }
  field(name, type) { this.fields[name] = type; return this; }
  build() {
    const fields = Object.entries(this.fields).map(([k, v]) => `  ${k}: ${v}`).join('\n');
    return `input ${this.name} {\n${fields}\n}`;
  }
}

class EnumBuilder {
  constructor(name) { this.name = name; this.values = []; }
  value(val, description) { this.values.push({ val, description }); return this; }
  build() {
    const values = this.values.map(v => v.description ? `  """\n  ${v.description}\n  """\n  ${v.val}` : `  ${v.val}`).join('\n');
    return `enum ${this.name} {\n${values}\n}`;
  }
}

// ============================================
// SCHEMA BUILDER
// ============================================

class SchemaBuilder {
  constructor() {
    this.types = [];
    this.queries = {};
    this.mutations = {};
    this.subscriptions = {};
    this.resolvers = { Query: {}, Mutation: {}, Subscription: {} };
    this.directives = [];
    this.scalars = [];
  }

  type(name) { const t = new TypeBuilder(name); this.types.push(t); return t; }
  input(name) { const i = new InputBuilder(name); this.types.push(i); return i; }
  enum(name) { const e = new EnumBuilder(name); this.types.push(e); return e; }

  scalar(name, description) {
    this.scalars.push({ name, description });
    return this;
  }

  query(name, returnType, args = {}, resolver) {
    this.queries[name] = { type: returnType, args };
    if (resolver) this.resolvers.Query[name] = resolver;
    return this;
  }

  mutation(name, returnType, args = {}, resolver) {
    this.mutations[name] = { type: returnType, args };
    if (resolver) this.resolvers.Mutation[name] = resolver;
    return this;
  }

  subscription(name, returnType, args = {}, resolver) {
    this.subscriptions[name] = { type: returnType, args };
    if (resolver) this.resolvers.Subscription[name] = resolver;
    return this;
  }

  directive(name, locations, args = {}) {
    this.directives.push({ name, locations, args });
    return this;
  }

  buildSchema() {
    const parts = [];

    // Scalars
    this.scalars.forEach(s => {
      if (s.description) parts.push(`"""\n${s.description}\n"""`);
      parts.push(`scalar ${s.name}`);
    });

    // Directives
    this.directives.forEach(d => {
      const args = Object.keys(d.args).length ? `(${Object.entries(d.args).map(([k, v]) => `${k}: ${v}`).join(', ')})` : '';
      parts.push(`directive @${d.name}${args} on ${d.locations.join(' | ')}`);
    });

    // Types
    this.types.forEach(t => parts.push(t.build()));

    // Query
    if (Object.keys(this.queries).length) {
      const fields = Object.entries(this.queries).map(([name, q]) => {
        const args = Object.keys(q.args).length ? `(${Object.entries(q.args).map(([k, v]) => `${k}: ${v}`).join(', ')})` : '';
        return `  ${name}${args}: ${q.type}`;
      }).join('\n');
      parts.push(`type Query {\n${fields}\n}`);
    }

    // Mutation
    if (Object.keys(this.mutations).length) {
      const fields = Object.entries(this.mutations).map(([name, m]) => {
        const args = Object.keys(m.args).length ? `(${Object.entries(m.args).map(([k, v]) => `${k}: ${v}`).join(', ')})` : '';
        return `  ${name}${args}: ${m.type}`;
      }).join('\n');
      parts.push(`type Mutation {\n${fields}\n}`);
    }

    // Subscription
    if (Object.keys(this.subscriptions).length) {
      const fields = Object.entries(this.subscriptions).map(([name, s]) => {
        const args = Object.keys(s.args).length ? `(${Object.entries(s.args).map(([k, v]) => `${k}: ${v}`).join(', ')})` : '';
        return `  ${name}${args}: ${s.type}`;
      }).join('\n');
      parts.push(`type Subscription {\n${fields}\n}`);
    }

    return parts.join('\n\n');
  }

  getResolvers() { return this.resolvers; }
}

// ============================================
// QUERY PARSER
// ============================================

class QueryParser {
  parse(query) {
    const cleaned = query.replace(/\s+/g, ' ').trim();
    const operationMatch = cleaned.match(/^(query|mutation|subscription)?\s*(\w+)?\s*(\([^)]*\))?\s*{/);

    return {
      operation: operationMatch?.[1] || 'query',
      name: operationMatch?.[2] || null,
      variables: this.parseVariables(operationMatch?.[3]),
      selections: this.parseSelections(cleaned)
    };
  }

  parseVariables(str) {
    if (!str) return {};
    const vars = {};
    const matches = str.matchAll(/\$(\w+):\s*(\w+!?)/g);
    for (const match of matches) vars[match[1]] = match[2];
    return vars;
  }

  parseSelections(query) {
    const bodyMatch = query.match(/{([^{}]*(?:{[^{}]*}[^{}]*)*)}/);
    if (!bodyMatch) return [];

    const body = bodyMatch[1].trim();
    const selections = [];
    const fieldRegex = /(\w+)(?:\s*\([^)]*\))?\s*(?:{[^{}]*})?/g;
    let match;
    while ((match = fieldRegex.exec(body)) !== null) {
      selections.push(match[1]);
    }
    return selections;
  }
}

// ============================================
// EXECUTOR
// ============================================

class GraphQLExecutor extends EventEmitter {
  constructor(schema, resolvers) {
    super();
    this.schema = schema;
    this.resolvers = resolvers;
    this.parser = new QueryParser();
    this.middleware = [];
  }

  use(fn) { this.middleware.push(fn); return this; }

  async execute(query, variables = {}, context = {}) {
    const startTime = Date.now();

    try {
      const parsed = this.parser.parse(query);
      const operationResolvers = this.resolvers[this.capitalize(parsed.operation)] || {};

      // Run middleware
      for (const mw of this.middleware) {
        await mw({ query, variables, context, parsed });
      }

      const data = {};
      for (const field of parsed.selections) {
        const resolver = operationResolvers[field];
        if (resolver) {
          data[field] = await resolver({}, variables, context);
        } else {
          data[field] = null;
        }
      }

      const result = { data };
      this.emit('executed', { query, variables, duration: Date.now() - startTime, result });
      return result;

    } catch (error) {
      const result = {
        data: null,
        errors: [{ message: error.message, locations: [], path: [] }]
      };
      this.emit('error', { query, variables, error });
      return result;
    }
  }

  capitalize(str) { return str.charAt(0).toUpperCase() + str.slice(1); }
}

// ============================================
// SUBSCRIPTION MANAGER
// ============================================

class SubscriptionManager extends EventEmitter {
  constructor() {
    super();
    this.subscriptions = new Map();
  }

  subscribe(id, channel, callback) {
    if (!this.subscriptions.has(channel)) {
      this.subscriptions.set(channel, new Map());
    }
    this.subscriptions.get(channel).set(id, callback);
    return () => this.unsubscribe(id, channel);
  }

  unsubscribe(id, channel) {
    this.subscriptions.get(channel)?.delete(id);
  }

  publish(channel, data) {
    const subscribers = this.subscriptions.get(channel);
    if (subscribers) {
      for (const [id, callback] of subscribers) {
        callback(data);
      }
    }
    this.emit('published', { channel, data, subscriberCount: subscribers?.size || 0 });
  }

  asyncIterator(channel) {
    const queue = [];
    let resolve = null;

    const id = crypto.randomBytes(8).toString('hex');
    this.subscribe(id, channel, (data) => {
      if (resolve) { resolve({ value: data, done: false }); resolve = null; }
      else queue.push(data);
    });

    return {
      [Symbol.asyncIterator]() { return this; },
      next: () => {
        if (queue.length) return Promise.resolve({ value: queue.shift(), done: false });
        return new Promise(r => { resolve = r; });
      },
      return: () => { this.unsubscribe(id, channel); return Promise.resolve({ done: true }); }
    };
  }
}

// ============================================
// DATA LOADER (N+1 PREVENTION)
// ============================================

class DataLoader {
  constructor(batchFn, options = {}) {
    this.batchFn = batchFn;
    this.cache = options.cache !== false ? new Map() : null;
    this.batch = [];
    this.batchScheduled = false;
    this.maxBatchSize = options.maxBatchSize || 100;
  }

  load(key) {
    if (this.cache?.has(key)) return Promise.resolve(this.cache.get(key));

    return new Promise((resolve, reject) => {
      this.batch.push({ key, resolve, reject });
      if (!this.batchScheduled) {
        this.batchScheduled = true;
        process.nextTick(() => this.executeBatch());
      }
    });
  }

  async loadMany(keys) { return Promise.all(keys.map(k => this.load(k))); }

  async executeBatch() {
    const batch = this.batch.splice(0, this.maxBatchSize);
    this.batchScheduled = this.batch.length > 0;

    if (this.batchScheduled) process.nextTick(() => this.executeBatch());

    const keys = batch.map(b => b.key);
    try {
      const results = await this.batchFn(keys);
      batch.forEach((b, i) => {
        if (this.cache) this.cache.set(b.key, results[i]);
        b.resolve(results[i]);
      });
    } catch (error) {
      batch.forEach(b => b.reject(error));
    }
  }

  clear(key) { this.cache?.delete(key); return this; }
  clearAll() { this.cache?.clear(); return this; }
  prime(key, value) { this.cache?.set(key, value); return this; }
}

// ============================================
// GRAPHQL SERVER
// ============================================

class GraphQLServer extends EventEmitter {
  constructor(options = {}) {
    super();
    this.schema = options.schema;
    this.resolvers = options.resolvers || {};
    this.executor = new GraphQLExecutor(this.schema, this.resolvers);
    this.subscriptions = new SubscriptionManager();
    this.playground = options.playground !== false;
    this.introspection = options.introspection !== false;
  }

  async handleRequest(req, res) {
    if (req.method === 'GET' && this.playground) {
      return this.servePlayground(res);
    }

    if (req.method === 'POST') {
      const body = await this.parseBody(req);
      const context = { req, res };
      const result = await this.executor.execute(body.query, body.variables, context);

      res.setHeader('Content-Type', 'application/json');
      res.end(JSON.stringify(result));
      return;
    }

    res.statusCode = 405;
    res.end('Method Not Allowed');
  }

  async parseBody(req) {
    return new Promise((resolve) => {
      const chunks = [];
      req.on('data', c => chunks.push(c));
      req.on('end', () => {
        try { resolve(JSON.parse(Buffer.concat(chunks).toString())); }
        catch { resolve({}); }
      });
    });
  }

  servePlayground(res) {
    res.setHeader('Content-Type', 'text/html');
    res.end(`<!DOCTYPE html><html><head><title>GraphQL Playground</title>
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/graphql-playground-react/build/static/css/index.css"/>
      <script src="https://cdn.jsdelivr.net/npm/graphql-playground-react/build/static/js/middleware.js"></script>
    </head><body><div id="root"></div><script>
      GraphQLPlayground.init(document.getElementById('root'), { endpoint: window.location.href })
    </script></body></html>`);
  }

  listen(port, callback) {
    const http = require('http');
    const server = http.createServer((req, res) => this.handleRequest(req, res));
    server.listen(port, callback);
    return server;
  }
}

// ============================================
// EXPORTS
// ============================================

module.exports = {
  GraphQLTypes,
  TypeBuilder,
  InputBuilder,
  EnumBuilder,
  SchemaBuilder,
  QueryParser,
  GraphQLExecutor,
  SubscriptionManager,
  DataLoader,
  GraphQLServer,

  createSchema: () => new SchemaBuilder(),
  createServer: (options) => new GraphQLServer(options),
  createDataLoader: (batchFn, options) => new DataLoader(batchFn, options),

  // Quick type helpers
  t: GraphQLTypes
};
