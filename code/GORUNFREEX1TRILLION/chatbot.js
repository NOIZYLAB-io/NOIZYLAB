/**
 * GORUNFREEX1TRILLION - AI CHATBOT ENGINE
 * Conversational AI, Intent detection, Dialogue management, NLU
 */

const { EventEmitter } = require('events');
const crypto = require('crypto');

// ============================================
// INTENT CLASSIFIER
// ============================================

class IntentClassifier {
  constructor() {
    this.intents = new Map();
    this.patterns = [];
  }

  addIntent(name, patterns, handler) {
    this.intents.set(name, { name, patterns, handler });
    patterns.forEach(pattern => {
      this.patterns.push({
        intent: name,
        pattern: this.compilePattern(pattern),
        original: pattern
      });
    });
    return this;
  }

  compilePattern(pattern) {
    // Convert pattern to regex, supporting {entity} placeholders
    const escaped = pattern.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    const withEntities = escaped.replace(/\\{(\w+)\\}/g, '(?<$1>.+?)');
    return new RegExp(`^${withEntities}$`, 'i');
  }

  classify(text) {
    const normalized = text.toLowerCase().trim();
    let bestMatch = null;
    let bestScore = 0;

    for (const { intent, pattern, original } of this.patterns) {
      const match = normalized.match(pattern);
      if (match) {
        const score = original.length / text.length;
        if (score > bestScore) {
          bestScore = score;
          bestMatch = {
            intent,
            confidence: Math.min(score * 1.2, 1),
            entities: match.groups || {},
            pattern: original
          };
        }
      }
    }

    // Fallback to keyword matching
    if (!bestMatch) {
      for (const [name, intent] of this.intents) {
        for (const pattern of intent.patterns) {
          const keywords = pattern.toLowerCase().split(/\s+/).filter(w => w.length > 3);
          const matches = keywords.filter(k => normalized.includes(k));
          const score = matches.length / keywords.length;
          if (score > bestScore && score > 0.3) {
            bestScore = score;
            bestMatch = { intent: name, confidence: score * 0.8, entities: {}, pattern };
          }
        }
      }
    }

    return bestMatch || { intent: 'unknown', confidence: 0, entities: {} };
  }

  getHandler(intentName) {
    return this.intents.get(intentName)?.handler;
  }
}

// ============================================
// ENTITY EXTRACTOR
// ============================================

class EntityExtractor {
  constructor() {
    this.extractors = new Map();
    this.setupDefaults();
  }

  setupDefaults() {
    // Email
    this.addExtractor('email', /[\w.-]+@[\w.-]+\.\w+/gi);
    // Phone
    this.addExtractor('phone', /(\+?1?[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}/g);
    // URL
    this.addExtractor('url', /https?:\/\/[^\s]+/gi);
    // Number
    this.addExtractor('number', /\b\d+(?:\.\d+)?\b/g);
    // Date
    this.addExtractor('date', /\b\d{1,2}[\/\-]\d{1,2}[\/\-]\d{2,4}\b/g);
    // Time
    this.addExtractor('time', /\b\d{1,2}:\d{2}(?::\d{2})?\s*(?:am|pm)?\b/gi);
    // Currency
    this.addExtractor('currency', /\$\d+(?:,\d{3})*(?:\.\d{2})?/g);
  }

  addExtractor(name, pattern) {
    this.extractors.set(name, pattern);
    return this;
  }

  extract(text) {
    const entities = {};

    for (const [name, pattern] of this.extractors) {
      const matches = text.match(pattern);
      if (matches) {
        entities[name] = matches.length === 1 ? matches[0] : matches;
      }
    }

    return entities;
  }
}

// ============================================
// DIALOGUE STATE
// ============================================

class DialogueState {
  constructor(sessionId) {
    this.sessionId = sessionId;
    this.context = {};
    this.history = [];
    this.slots = {};
    this.currentIntent = null;
    this.awaitingSlot = null;
    this.turnCount = 0;
    this.createdAt = Date.now();
    this.lastActivityAt = Date.now();
  }

  addTurn(role, content, metadata = {}) {
    this.history.push({
      role,
      content,
      timestamp: Date.now(),
      turnNumber: ++this.turnCount,
      ...metadata
    });
    this.lastActivityAt = Date.now();
  }

  setSlot(name, value) { this.slots[name] = value; }
  getSlot(name) { return this.slots[name]; }
  clearSlots() { this.slots = {}; }

  setContext(key, value) { this.context[key] = value; }
  getContext(key) { return this.context[key]; }
  clearContext() { this.context = {}; }

  getLastTurns(n = 5) { return this.history.slice(-n); }
  getFullHistory() { return this.history; }
}

// ============================================
// DIALOGUE MANAGER
// ============================================

class DialogueManager extends EventEmitter {
  constructor(options = {}) {
    super();
    this.sessions = new Map();
    this.flows = new Map();
    this.sessionTimeout = options.sessionTimeout || 30 * 60 * 1000; // 30 min
  }

  getSession(sessionId) {
    let session = this.sessions.get(sessionId);
    if (!session) {
      session = new DialogueState(sessionId);
      this.sessions.set(sessionId, session);
      this.emit('session:created', { sessionId });
    }
    return session;
  }

  destroySession(sessionId) {
    this.sessions.delete(sessionId);
    this.emit('session:destroyed', { sessionId });
  }

  addFlow(name, flow) {
    this.flows.set(name, flow);
    return this;
  }

  async executeFlow(session, flowName, input) {
    const flow = this.flows.get(flowName);
    if (!flow) throw new Error(`Flow '${flowName}' not found`);

    session.currentIntent = flowName;
    return flow.execute(session, input);
  }

  cleanupSessions() {
    const now = Date.now();
    for (const [id, session] of this.sessions) {
      if (now - session.lastActivityAt > this.sessionTimeout) {
        this.destroySession(id);
      }
    }
  }
}

// ============================================
// CONVERSATION FLOW
// ============================================

class ConversationFlow {
  constructor(name) {
    this.name = name;
    this.steps = [];
    this.slots = [];
  }

  requireSlot(name, prompt, validator) {
    this.slots.push({ name, prompt, validator });
    return this;
  }

  addStep(handler) {
    this.steps.push(handler);
    return this;
  }

  async execute(session, input) {
    // Check for missing required slots
    for (const slot of this.slots) {
      if (!session.getSlot(slot.name)) {
        if (session.awaitingSlot === slot.name && input) {
          // Validate and store the slot value
          if (!slot.validator || slot.validator(input)) {
            session.setSlot(slot.name, input);
            session.awaitingSlot = null;
          } else {
            return { response: `Invalid ${slot.name}. ${slot.prompt}`, awaitingInput: true };
          }
        } else {
          session.awaitingSlot = slot.name;
          return { response: slot.prompt, awaitingInput: true };
        }
      }
    }

    // Execute steps
    let result = { response: '' };
    for (const step of this.steps) {
      result = await step(session, input);
      if (result.stop) break;
    }

    return result;
  }
}

// ============================================
// RESPONSE GENERATOR
// ============================================

class ResponseGenerator {
  constructor() {
    this.templates = new Map();
    this.variations = new Map();
  }

  addTemplate(name, templates) {
    this.templates.set(name, Array.isArray(templates) ? templates : [templates]);
    return this;
  }

  addVariation(name, variations) {
    this.variations.set(name, variations);
    return this;
  }

  generate(templateName, variables = {}) {
    const templates = this.templates.get(templateName);
    if (!templates) return `[Missing template: ${templateName}]`;

    let response = templates[Math.floor(Math.random() * templates.length)];

    // Replace variables
    response = response.replace(/\{(\w+)\}/g, (_, key) => variables[key] || `{${key}}`);

    // Replace variations
    response = response.replace(/\[(\w+)\]/g, (_, key) => {
      const vars = this.variations.get(key);
      return vars ? vars[Math.floor(Math.random() * vars.length)] : `[${key}]`;
    });

    return response;
  }
}

// ============================================
// CHATBOT
// ============================================

class Chatbot extends EventEmitter {
  constructor(options = {}) {
    super();
    this.name = options.name || 'NOIZYBOT';
    this.classifier = new IntentClassifier();
    this.extractor = new EntityExtractor();
    this.dialogueManager = new DialogueManager(options);
    this.responseGenerator = new ResponseGenerator();
    this.fallbackHandler = null;
    this.middleware = [];

    this.setupDefaultResponses();
  }

  setupDefaultResponses() {
    this.responseGenerator
      .addTemplate('greeting', [
        'Hello! How can I help you today?',
        'Hi there! What can I do for you?',
        'Hey! How may I assist you?'
      ])
      .addTemplate('farewell', [
        'Goodbye! Have a great day!',
        'See you later! Take care!',
        'Bye! Feel free to come back anytime!'
      ])
      .addTemplate('unknown', [
        "I'm not sure I understand. Could you rephrase that?",
        "Sorry, I didn't catch that. Can you try again?",
        "I'm still learning! Could you explain what you need differently?"
      ])
      .addTemplate('error', [
        'Oops! Something went wrong. Please try again.',
        'Sorry, I encountered an error. Let me try that again.'
      ]);
  }

  intent(name, patterns, handler) {
    this.classifier.addIntent(name, patterns, handler);
    return this;
  }

  entity(name, pattern) {
    this.extractor.addExtractor(name, pattern);
    return this;
  }

  flow(name, flow) {
    this.dialogueManager.addFlow(name, flow);
    return this;
  }

  template(name, templates) {
    this.responseGenerator.addTemplate(name, templates);
    return this;
  }

  use(middleware) {
    this.middleware.push(middleware);
    return this;
  }

  onFallback(handler) {
    this.fallbackHandler = handler;
    return this;
  }

  async process(sessionId, message) {
    const session = this.dialogueManager.getSession(sessionId);
    session.addTurn('user', message);

    const startTime = Date.now();

    try {
      // Run middleware
      let context = { session, message, entities: {}, intent: null };
      for (const mw of this.middleware) {
        context = await mw(context) || context;
      }

      // Extract entities
      context.entities = { ...context.entities, ...this.extractor.extract(message) };

      // Handle awaiting slot
      if (session.awaitingSlot && session.currentIntent) {
        const result = await this.dialogueManager.executeFlow(session, session.currentIntent, message);
        session.addTurn('assistant', result.response);
        return this.formatResponse(result, session, startTime);
      }

      // Classify intent
      const classification = this.classifier.classify(message);
      context.intent = classification;

      this.emit('intent:classified', { sessionId, classification });

      // Handle unknown intent
      if (classification.intent === 'unknown' || classification.confidence < 0.3) {
        if (this.fallbackHandler) {
          const result = await this.fallbackHandler(session, message, context);
          session.addTurn('assistant', result.response);
          return this.formatResponse(result, session, startTime);
        }
        const response = this.responseGenerator.generate('unknown');
        session.addTurn('assistant', response);
        return this.formatResponse({ response }, session, startTime);
      }

      // Execute handler or flow
      const handler = this.classifier.getHandler(classification.intent);
      let result;

      if (handler) {
        result = await handler(session, message, {
          entities: { ...context.entities, ...classification.entities },
          intent: classification
        });
      } else if (this.dialogueManager.flows.has(classification.intent)) {
        result = await this.dialogueManager.executeFlow(session, classification.intent, message);
      } else {
        result = { response: this.responseGenerator.generate('unknown') };
      }

      session.addTurn('assistant', result.response);
      return this.formatResponse(result, session, startTime);

    } catch (error) {
      this.emit('error', { sessionId, error });
      const response = this.responseGenerator.generate('error');
      session.addTurn('assistant', response, { error: error.message });
      return this.formatResponse({ response, error: error.message }, session, startTime);
    }
  }

  formatResponse(result, session, startTime) {
    return {
      sessionId: session.sessionId,
      response: result.response,
      intent: session.currentIntent,
      entities: result.entities || {},
      awaitingInput: result.awaitingInput || false,
      actions: result.actions || [],
      context: result.context || {},
      processingTime: Date.now() - startTime
    };
  }

  getSession(sessionId) { return this.dialogueManager.getSession(sessionId); }
  destroySession(sessionId) { this.dialogueManager.destroySession(sessionId); }
}

// ============================================
// QUICK REPLY BUILDER
// ============================================

class QuickReplyBuilder {
  constructor() { this.replies = []; }
  add(text, payload) { this.replies.push({ text, payload }); return this; }
  build() { return this.replies; }
}

// ============================================
// CARD BUILDER
// ============================================

class CardBuilder {
  constructor() {
    this.card = { title: '', subtitle: '', image: null, buttons: [] };
  }
  title(t) { this.card.title = t; return this; }
  subtitle(s) { this.card.subtitle = s; return this; }
  image(url) { this.card.image = url; return this; }
  button(text, action, payload) { this.card.buttons.push({ text, action, payload }); return this; }
  build() { return this.card; }
}

// ============================================
// EXPORTS
// ============================================

module.exports = {
  Chatbot,
  IntentClassifier,
  EntityExtractor,
  DialogueManager,
  DialogueState,
  ConversationFlow,
  ResponseGenerator,
  QuickReplyBuilder,
  CardBuilder,

  createBot: (options) => new Chatbot(options),
  createFlow: (name) => new ConversationFlow(name),
  createQuickReplies: () => new QuickReplyBuilder(),
  createCard: () => new CardBuilder()
};
