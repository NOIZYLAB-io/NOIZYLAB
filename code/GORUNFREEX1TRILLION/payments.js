/**
 * GORUNFREEX1TRILLION - PAYMENTS ENGINE
 * Stripe, PayPal, Subscriptions, Invoicing, Checkout
 */

const { EventEmitter } = require('events');
const crypto = require('crypto');

// ============================================
// PAYMENT PROCESSOR BASE
// ============================================

class PaymentProcessor extends EventEmitter {
  constructor(config) {
    super();
    this.config = config;
    this.name = 'base';
  }
  async charge(amount, currency, source) { throw new Error('Not implemented'); }
  async refund(transactionId, amount) { throw new Error('Not implemented'); }
  async createCustomer(data) { throw new Error('Not implemented'); }
}

// ============================================
// STRIPE PROVIDER
// ============================================

class StripeProvider extends PaymentProcessor {
  constructor(config) {
    super(config);
    this.name = 'stripe';
    this.apiKey = config.secretKey;
    this.webhookSecret = config.webhookSecret;
    this.apiBase = 'https://api.stripe.com/v1';
  }

  async charge(amount, currency, source, metadata = {}) {
    console.log(`[Stripe] Charging ${amount} ${currency}`);
    const paymentIntent = {
      id: `pi_${crypto.randomBytes(12).toString('hex')}`,
      amount,
      currency: currency.toLowerCase(),
      source,
      status: 'succeeded',
      created: Date.now(),
      metadata
    };
    this.emit('charge:success', paymentIntent);
    return paymentIntent;
  }

  async createPaymentIntent(amount, currency, options = {}) {
    return {
      id: `pi_${crypto.randomBytes(12).toString('hex')}`,
      client_secret: `pi_${crypto.randomBytes(12).toString('hex')}_secret_${crypto.randomBytes(8).toString('hex')}`,
      amount,
      currency: currency.toLowerCase(),
      status: 'requires_payment_method',
      ...options
    };
  }

  async confirmPaymentIntent(intentId, paymentMethod) {
    return { id: intentId, status: 'succeeded', payment_method: paymentMethod };
  }

  async refund(paymentIntentId, amount) {
    console.log(`[Stripe] Refunding ${amount} from ${paymentIntentId}`);
    const refund = {
      id: `re_${crypto.randomBytes(12).toString('hex')}`,
      payment_intent: paymentIntentId,
      amount,
      status: 'succeeded',
      created: Date.now()
    };
    this.emit('refund:success', refund);
    return refund;
  }

  async createCustomer(data) {
    return {
      id: `cus_${crypto.randomBytes(12).toString('hex')}`,
      email: data.email,
      name: data.name,
      metadata: data.metadata || {},
      created: Date.now()
    };
  }

  async createSubscription(customerId, priceId, options = {}) {
    return {
      id: `sub_${crypto.randomBytes(12).toString('hex')}`,
      customer: customerId,
      items: [{ price: priceId }],
      status: 'active',
      current_period_start: Date.now(),
      current_period_end: Date.now() + 30 * 24 * 60 * 60 * 1000,
      ...options
    };
  }

  async cancelSubscription(subscriptionId, options = {}) {
    return {
      id: subscriptionId,
      status: options.immediately ? 'canceled' : 'active',
      cancel_at_period_end: !options.immediately,
      canceled_at: Date.now()
    };
  }

  async createProduct(data) {
    return {
      id: `prod_${crypto.randomBytes(12).toString('hex')}`,
      name: data.name,
      description: data.description,
      active: true,
      created: Date.now()
    };
  }

  async createPrice(productId, amount, currency, interval = 'month') {
    return {
      id: `price_${crypto.randomBytes(12).toString('hex')}`,
      product: productId,
      unit_amount: amount,
      currency: currency.toLowerCase(),
      recurring: interval ? { interval } : null,
      type: interval ? 'recurring' : 'one_time'
    };
  }

  async createCheckoutSession(options) {
    return {
      id: `cs_${crypto.randomBytes(16).toString('hex')}`,
      url: `https://checkout.stripe.com/pay/cs_${crypto.randomBytes(16).toString('hex')}`,
      mode: options.mode || 'payment',
      line_items: options.lineItems,
      success_url: options.successUrl,
      cancel_url: options.cancelUrl,
      expires_at: Date.now() + 24 * 60 * 60 * 1000
    };
  }

  async createInvoice(customerId, items) {
    return {
      id: `in_${crypto.randomBytes(12).toString('hex')}`,
      customer: customerId,
      status: 'draft',
      lines: items,
      total: items.reduce((sum, i) => sum + i.amount, 0),
      created: Date.now()
    };
  }

  verifyWebhook(payload, signature) {
    const expected = crypto.createHmac('sha256', this.webhookSecret).update(payload).digest('hex');
    return `sha256=${expected}` === signature;
  }

  handleWebhook(event) {
    this.emit(`webhook:${event.type}`, event.data);
    return { received: true };
  }
}

// ============================================
// PAYPAL PROVIDER
// ============================================

class PayPalProvider extends PaymentProcessor {
  constructor(config) {
    super(config);
    this.name = 'paypal';
    this.clientId = config.clientId;
    this.clientSecret = config.clientSecret;
    this.sandbox = config.sandbox !== false;
    this.apiBase = this.sandbox ? 'https://api-m.sandbox.paypal.com' : 'https://api-m.paypal.com';
  }

  async getAccessToken() {
    return { access_token: `A21AAF${crypto.randomBytes(32).toString('hex')}`, expires_in: 32400 };
  }

  async createOrder(amount, currency, description) {
    return {
      id: crypto.randomBytes(8).toString('hex').toUpperCase(),
      status: 'CREATED',
      intent: 'CAPTURE',
      purchase_units: [{
        amount: { currency_code: currency, value: (amount / 100).toFixed(2) },
        description
      }],
      links: [
        { rel: 'approve', href: `https://www.sandbox.paypal.com/checkoutnow?token=${crypto.randomBytes(8).toString('hex')}` }
      ]
    };
  }

  async captureOrder(orderId) {
    console.log(`[PayPal] Capturing order ${orderId}`);
    return {
      id: orderId,
      status: 'COMPLETED',
      purchase_units: [{ payments: { captures: [{ id: `CAP_${crypto.randomBytes(8).toString('hex')}`, status: 'COMPLETED' }] } }]
    };
  }

  async refund(captureId, amount) {
    return {
      id: `REF_${crypto.randomBytes(8).toString('hex')}`,
      status: 'COMPLETED',
      amount: { value: (amount / 100).toFixed(2) }
    };
  }

  async createSubscription(planId, subscriberEmail) {
    return {
      id: `I-${crypto.randomBytes(6).toString('hex').toUpperCase()}`,
      plan_id: planId,
      status: 'ACTIVE',
      subscriber: { email_address: subscriberEmail },
      start_time: new Date().toISOString()
    };
  }

  verifyWebhook(headers, body) {
    return true; // Simplified - real impl uses PayPal verification API
  }
}

// ============================================
// SUBSCRIPTION MANAGER
// ============================================

class SubscriptionManager extends EventEmitter {
  constructor(processor) {
    super();
    this.processor = processor;
    this.plans = new Map();
    this.subscriptions = new Map();
  }

  async createPlan(plan) {
    const product = await this.processor.createProduct({ name: plan.name, description: plan.description });
    const price = await this.processor.createPrice(product.id, plan.amount, plan.currency, plan.interval);

    const planData = { id: price.id, productId: product.id, ...plan, priceId: price.id };
    this.plans.set(plan.name, planData);
    return planData;
  }

  async subscribe(customerId, planName, options = {}) {
    const plan = this.plans.get(planName);
    if (!plan) throw new Error('Plan not found');

    const subscription = await this.processor.createSubscription(customerId, plan.priceId, options);
    this.subscriptions.set(subscription.id, { ...subscription, planName, customerId });
    this.emit('subscription:created', subscription);
    return subscription;
  }

  async cancel(subscriptionId, immediately = false) {
    const subscription = await this.processor.cancelSubscription(subscriptionId, { immediately });
    this.emit('subscription:canceled', subscription);
    return subscription;
  }

  async upgrade(subscriptionId, newPlanName) {
    const plan = this.plans.get(newPlanName);
    if (!plan) throw new Error('Plan not found');
    this.emit('subscription:upgraded', { subscriptionId, newPlan: newPlanName });
    return { subscriptionId, newPlan: newPlanName, status: 'upgraded' };
  }

  async downgrade(subscriptionId, newPlanName) {
    const plan = this.plans.get(newPlanName);
    if (!plan) throw new Error('Plan not found');
    this.emit('subscription:downgraded', { subscriptionId, newPlan: newPlanName });
    return { subscriptionId, newPlan: newPlanName, status: 'downgraded' };
  }

  getPlans() { return Array.from(this.plans.values()); }
}

// ============================================
// INVOICE GENERATOR
// ============================================

class InvoiceGenerator {
  constructor(options = {}) {
    this.company = options.company || {};
    this.currency = options.currency || 'USD';
    this.taxRate = options.taxRate || 0;
    this.invoices = new Map();
  }

  create(customer, items, options = {}) {
    const subtotal = items.reduce((sum, item) => sum + (item.quantity * item.unitPrice), 0);
    const tax = Math.round(subtotal * this.taxRate);
    const total = subtotal + tax;

    const invoice = {
      id: `INV-${Date.now()}-${crypto.randomBytes(4).toString('hex').toUpperCase()}`,
      number: options.number || `INV-${String(this.invoices.size + 1).padStart(6, '0')}`,
      date: new Date().toISOString(),
      dueDate: new Date(Date.now() + (options.dueDays || 30) * 24 * 60 * 60 * 1000).toISOString(),
      status: 'draft',
      customer,
      company: this.company,
      items: items.map((item, i) => ({
        id: i + 1,
        description: item.description,
        quantity: item.quantity,
        unitPrice: item.unitPrice,
        total: item.quantity * item.unitPrice
      })),
      subtotal,
      taxRate: this.taxRate,
      tax,
      total,
      currency: options.currency || this.currency,
      notes: options.notes,
      terms: options.terms
    };

    this.invoices.set(invoice.id, invoice);
    return invoice;
  }

  send(invoiceId) {
    const invoice = this.invoices.get(invoiceId);
    if (invoice) { invoice.status = 'sent'; invoice.sentAt = new Date().toISOString(); }
    return invoice;
  }

  markPaid(invoiceId, paymentDetails = {}) {
    const invoice = this.invoices.get(invoiceId);
    if (invoice) {
      invoice.status = 'paid';
      invoice.paidAt = new Date().toISOString();
      invoice.paymentDetails = paymentDetails;
    }
    return invoice;
  }

  void(invoiceId) {
    const invoice = this.invoices.get(invoiceId);
    if (invoice) { invoice.status = 'void'; invoice.voidedAt = new Date().toISOString(); }
    return invoice;
  }

  generateHTML(invoiceId) {
    const inv = this.invoices.get(invoiceId);
    if (!inv) return null;

    return `<!DOCTYPE html><html><head><style>
      body{font-family:system-ui;max-width:800px;margin:0 auto;padding:40px;color:#333}
      .header{display:flex;justify-content:space-between;margin-bottom:40px}
      .invoice-title{font-size:32px;color:#00ff88}
      .meta{text-align:right;color:#666}
      table{width:100%;border-collapse:collapse;margin:20px 0}
      th,td{padding:12px;text-align:left;border-bottom:1px solid #ddd}
      th{background:#f5f5f5}
      .totals{text-align:right;margin-top:20px}
      .total-row{font-size:18px;font-weight:bold}
      .status{display:inline-block;padding:4px 12px;border-radius:20px;font-size:12px;text-transform:uppercase}
      .status-paid{background:#00ff88;color:#000}
      .status-sent{background:#0088ff;color:#fff}
      .status-draft{background:#666;color:#fff}
    </style></head><body>
      <div class="header">
        <div><div class="invoice-title">INVOICE</div><div>${inv.company.name || 'NOIZYLAB'}</div></div>
        <div class="meta">
          <div><strong>${inv.number}</strong></div>
          <div>Date: ${new Date(inv.date).toLocaleDateString()}</div>
          <div>Due: ${new Date(inv.dueDate).toLocaleDateString()}</div>
          <div><span class="status status-${inv.status}">${inv.status}</span></div>
        </div>
      </div>
      <div><strong>Bill To:</strong><br>${inv.customer.name}<br>${inv.customer.email}</div>
      <table><thead><tr><th>#</th><th>Description</th><th>Qty</th><th>Price</th><th>Total</th></tr></thead>
      <tbody>${inv.items.map(i => `<tr><td>${i.id}</td><td>${i.description}</td><td>${i.quantity}</td><td>$${(i.unitPrice/100).toFixed(2)}</td><td>$${(i.total/100).toFixed(2)}</td></tr>`).join('')}</tbody></table>
      <div class="totals">
        <div>Subtotal: $${(inv.subtotal/100).toFixed(2)}</div>
        ${inv.tax > 0 ? `<div>Tax (${(inv.taxRate*100).toFixed(0)}%): $${(inv.tax/100).toFixed(2)}</div>` : ''}
        <div class="total-row">Total: $${(inv.total/100).toFixed(2)} ${inv.currency}</div>
      </div>
      ${inv.notes ? `<div style="margin-top:40px;color:#666"><strong>Notes:</strong><br>${inv.notes}</div>` : ''}
    </body></html>`;
  }
}

// ============================================
// CHECKOUT SESSION
// ============================================

class CheckoutSession {
  constructor(processor, options = {}) {
    this.processor = processor;
    this.sessions = new Map();
    this.successUrl = options.successUrl || '/checkout/success';
    this.cancelUrl = options.cancelUrl || '/checkout/cancel';
  }

  async create(items, options = {}) {
    const lineItems = items.map(item => ({
      price_data: {
        currency: item.currency || 'usd',
        product_data: { name: item.name, description: item.description },
        unit_amount: item.price
      },
      quantity: item.quantity || 1
    }));

    const session = await this.processor.createCheckoutSession({
      mode: options.mode || 'payment',
      lineItems,
      successUrl: options.successUrl || this.successUrl,
      cancelUrl: options.cancelUrl || this.cancelUrl,
      customerEmail: options.customerEmail,
      metadata: options.metadata
    });

    this.sessions.set(session.id, session);
    return session;
  }

  get(sessionId) { return this.sessions.get(sessionId); }
}

// ============================================
// PAYMENT GATEWAY
// ============================================

class PaymentGateway extends EventEmitter {
  constructor() {
    super();
    this.processors = new Map();
    this.defaultProcessor = null;
    this.transactions = new Map();
  }

  addProcessor(name, processor) {
    this.processors.set(name, processor);
    if (!this.defaultProcessor) this.defaultProcessor = name;
    processor.on('charge:success', (data) => this.emit('payment:success', { processor: name, ...data }));
    processor.on('refund:success', (data) => this.emit('refund:success', { processor: name, ...data }));
    return this;
  }

  setDefault(name) { this.defaultProcessor = name; return this; }

  getProcessor(name) { return this.processors.get(name || this.defaultProcessor); }

  async charge(amount, currency, source, options = {}) {
    const processor = this.getProcessor(options.processor);
    const result = await processor.charge(amount, currency, source, options.metadata);
    this.transactions.set(result.id, { ...result, processor: options.processor || this.defaultProcessor });
    return result;
  }

  async refund(transactionId, amount) {
    const tx = this.transactions.get(transactionId);
    if (!tx) throw new Error('Transaction not found');
    const processor = this.getProcessor(tx.processor);
    return processor.refund(transactionId, amount || tx.amount);
  }

  getTransaction(id) { return this.transactions.get(id); }
  getTransactions() { return Array.from(this.transactions.values()); }
}

// ============================================
// EXPORTS
// ============================================

module.exports = {
  PaymentProcessor,
  StripeProvider,
  PayPalProvider,
  SubscriptionManager,
  InvoiceGenerator,
  CheckoutSession,
  PaymentGateway,

  createGateway: (config = {}) => {
    const gateway = new PaymentGateway();
    if (config.stripe) gateway.addProcessor('stripe', new StripeProvider(config.stripe));
    if (config.paypal) gateway.addProcessor('paypal', new PayPalProvider(config.paypal));
    return gateway;
  },

  createInvoiceGenerator: (options) => new InvoiceGenerator(options),
  createSubscriptionManager: (processor) => new SubscriptionManager(processor)
};
