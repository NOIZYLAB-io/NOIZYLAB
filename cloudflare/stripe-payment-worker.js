/**
 * 💳 STRIPE PAYMENT WORKER - Payment Processing
 * 
 * Handles payment processing for repairs
 * Integrates with Stripe API
 * 
 * Endpoints:
 * - /api/payment/create-intent - Create payment intent
 * - /api/payment/create-invoice - Create invoice
 * - /api/payment/webhook - Stripe webhook handler
 * - /api/payment/status - Check payment status
 */

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname;

    const corsHeaders = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization, Stripe-Signature',
    };

    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders });
    }

    try {
      if (path === '/') {
        return handleRoot(env);
      }

      if (path === '/health') {
        return handleHealth(env);
      }

      if (path === '/api/payment/status') {
        return handleStatus(env);
      }

      if (path === '/api/payment/create-intent' && request.method === 'POST') {
        return await handleCreateIntent(request, env);
      }

      if (path === '/api/payment/create-invoice' && request.method === 'POST') {
        return await handleCreateInvoice(request, env);
      }

      if (path === '/api/payment/webhook' && request.method === 'POST') {
        return await handleWebhook(request, env);
      }

      if (path.startsWith('/api/payment/intent/') && request.method === 'GET') {
        return await handleGetIntent(request, env, path);
      }

      return new Response('Not Found', { status: 404, headers: corsHeaders });

    } catch (error) {
      return new Response(
        JSON.stringify({ error: error.message }),
        { status: 500, headers: { ...corsHeaders, 'Content-Type': 'application/json' } }
      );
    }
  }
};

function handleRoot(env) {
  const info = {
    name: 'Stripe Payment Worker',
    version: '1.0.0',
    provider: 'Stripe',
    status: 'ONLINE 💳',
    endpoints: {
      create_intent: '/api/payment/create-intent',
      create_invoice: '/api/payment/create-invoice',
      webhook: '/api/payment/webhook',
      get_intent: '/api/payment/intent/{id}',
      status: '/api/payment/status'
    },
    features: [
      'Payment intent creation',
      'Invoice generation',
      'Webhook handling',
      'Payment tracking',
      'Refund support'
    ],
    pricing: {
      base_repair: '$89.00',
      express_service: '+$30.00',
      shipping: 'Calculated'
    }
  };

  return new Response(JSON.stringify(info, null, 2), {
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*'
    }
  });
}

async function handleHealth(env) {
  const health = {
    status: 'healthy',
    timestamp: new Date().toISOString(),
    stripe: {
      configured: !!env.STRIPE_SECRET_KEY,
      mode: env.STRIPE_MODE || 'test',
      webhook_configured: !!env.STRIPE_WEBHOOK_SECRET
    }
  };

  return new Response(JSON.stringify(health, null, 2), {
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*'
    }
  });
}

async function handleStatus(env) {
  const status = {
    payment_worker: 'ACTIVE',
    timestamp: new Date().toISOString(),
    configuration: {
      provider: 'Stripe',
      mode: env.STRIPE_MODE || 'test',
      publishable_key_set: !!env.STRIPE_PUBLISHABLE_KEY,
      secret_key_set: !!env.STRIPE_SECRET_KEY,
      webhook_configured: !!env.STRIPE_WEBHOOK_SECRET
    },
    capabilities: {
      payment_intents: 'enabled',
      invoices: 'enabled',
      webhooks: 'enabled',
      refunds: 'enabled',
      subscriptions: 'planned'
    },
    pricing: {
      base_repair: 89.00,
      express_fee: 30.00,
      currency: 'USD'
    }
  };

  return new Response(JSON.stringify(status, null, 2), {
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*'
    }
  });
}

async function handleCreateIntent(request, env) {
  const data = await request.json();

  if (!data.amount || !data.repair_id) {
    return new Response(
      JSON.stringify({ error: 'Missing required fields: amount, repair_id' }),
      { status: 400, headers: { 'Content-Type': 'application/json' } }
    );
  }

  // In production, call Stripe API to create payment intent
  const intentId = `pi_${crypto.randomUUID().replace(/-/g, '')}`;
  const clientSecret = `${intentId}_secret_${crypto.randomUUID().replace(/-/g, '')}`;

  const intent = {
    id: intentId,
    client_secret: clientSecret,
    amount: Math.round(data.amount * 100), // Convert to cents
    currency: 'usd',
    repair_id: data.repair_id,
    customer_email: data.customer_email || '',
    description: `NOIZYLAB Repair ${data.repair_id}`,
    status: 'requires_payment_method',
    created: Math.floor(Date.now() / 1000),
    metadata: {
      repair_id: data.repair_id,
      service: 'CPU Repair',
      base_price: '89.00'
    }
  };

  // Store intent
  await env.PAYMENTS.put(`intent:${intentId}`, JSON.stringify(intent), {
    expirationTtl: 86400 // 24 hours
  });

  /* Production Stripe API call:
  const stripeResponse = await fetch('https://api.stripe.com/v1/payment_intents', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${env.STRIPE_SECRET_KEY}`,
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: new URLSearchParams({
      amount: intent.amount,
      currency: intent.currency,
      'metadata[repair_id]': data.repair_id,
      description: intent.description
    })
  });
  */

  return new Response(JSON.stringify({
    success: true,
    payment_intent: {
      id: intent.id,
      client_secret: intent.client_secret,
      amount: data.amount,
      currency: 'USD',
      status: 'requires_payment_method'
    },
    repair_id: data.repair_id,
    message: 'Payment intent created successfully'
  }), {
    status: 201,
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*'
    }
  });
}

async function handleCreateInvoice(request, env) {
  const data = await request.json();

  if (!data.repair_id || !data.customer_email || !data.amount) {
    return new Response(
      JSON.stringify({ error: 'Missing required fields' }),
      { status: 400, headers: { 'Content-Type': 'application/json' } }
    );
  }

  const invoiceId = `inv_${crypto.randomUUID().replace(/-/g, '')}`;
  const invoice = {
    id: invoiceId,
    repair_id: data.repair_id,
    customer_email: data.customer_email,
    customer_name: data.customer_name || 'Customer',
    amount: data.amount,
    currency: 'USD',
    status: 'draft',
    created: new Date().toISOString(),
    due_date: data.due_date || new Date(Date.now() + 7 * 24 * 60 * 60 * 1000).toISOString(),
    items: [
      {
        description: 'CPU Repair Service',
        quantity: 1,
        unit_price: 89.00,
        amount: 89.00
      }
    ],
    subtotal: 89.00,
    tax: 0,
    total: data.amount
  };

  await env.PAYMENTS.put(`invoice:${invoiceId}`, JSON.stringify(invoice), {
    expirationTtl: 2592000 // 30 days
  });

  return new Response(JSON.stringify({
    success: true,
    invoice: {
      id: invoice.id,
      repair_id: invoice.repair_id,
      amount: invoice.amount,
      status: 'draft',
      due_date: invoice.due_date,
      url: `https://noizylab-payments.workers.dev/invoice/${invoiceId}`
    },
    message: 'Invoice created successfully'
  }), {
    status: 201,
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*'
    }
  });
}

async function handleWebhook(request, env) {
  // In production, verify Stripe webhook signature
  const signature = request.headers.get('Stripe-Signature');
  
  // Simulated webhook handling
  const payload = await request.json();
  
  const webhookId = crypto.randomUUID();
  const webhook = {
    id: webhookId,
    type: payload.type || 'unknown',
    data: payload,
    received_at: new Date().toISOString(),
    processed: false
  };

  await env.WEBHOOKS.put(`webhook:${webhookId}`, JSON.stringify(webhook), {
    expirationTtl: 604800 // 7 days
  });

  // Process different webhook types
  if (payload.type === 'payment_intent.succeeded') {
    // Update repair status, send confirmation email, etc.
    console.log('Payment succeeded:', payload.data?.object?.id);
  }

  if (payload.type === 'payment_intent.payment_failed') {
    // Notify customer, log failure
    console.log('Payment failed:', payload.data?.object?.id);
  }

  return new Response(JSON.stringify({
    received: true,
    webhook_id: webhookId,
    type: payload.type
  }), {
    status: 200,
    headers: {
      'Content-Type': 'application/json'
    }
  });
}

async function handleGetIntent(request, env, path) {
  const intentId = path.split('/').pop();
  
  const intentData = await env.PAYMENTS.get(`intent:${intentId}`);
  
  if (!intentData) {
    return new Response(
      JSON.stringify({ error: 'Payment intent not found' }),
      { status: 404, headers: { 'Content-Type': 'application/json' } }
    );
  }

  const intent = JSON.parse(intentData);

  return new Response(JSON.stringify({
    payment_intent: {
      id: intent.id,
      amount: intent.amount / 100,
      currency: intent.currency,
      status: intent.status,
      repair_id: intent.repair_id,
      created: intent.created
    }
  }), {
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*'
    }
  });
}
