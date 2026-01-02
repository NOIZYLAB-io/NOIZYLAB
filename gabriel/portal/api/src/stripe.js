/**
 * Stripe Payment Integration for NoizyLab
 * 
 * Products:
 * - Golden Audit: $4.99/scan (one-time)
 * - Legacy Kit: $29/bundle (10 scans, one-time)
 * - Pro Subscription: $99/month (unlimited)
 * - Enterprise: Custom pricing
 */

// Price IDs - Replace with your actual Stripe price IDs
const PRICES = {
  GOLDEN_AUDIT: 'price_golden_audit_499',
  LEGACY_KIT: 'price_legacy_kit_2900',
  PRO_MONTHLY: 'price_pro_monthly_9900',
  PRO_YEARLY: 'price_pro_yearly_99900'
};

// Product metadata
const PRODUCTS = {
  golden_audit: {
    name: 'Golden Audit',
    price: 499, // cents
    currency: 'usd',
    description: 'Single PCB scan with AI analysis',
    features: ['1 board scan', 'Defect detection', 'Basic repair guidance', 'PDF report'],
    scans: 1
  },
  legacy_kit: {
    name: 'Legacy Restoration Kit',
    price: 2900,
    currency: 'usd',
    description: 'Bundle for vintage electronics restoration',
    features: ['10 board scans', 'Priority processing', 'AR overlay', 'Voice guidance', 'Component sourcing tips'],
    scans: 10
  },
  pro_monthly: {
    name: 'Pro Subscription',
    price: 9900,
    currency: 'usd',
    description: 'Unlimited scans for professionals',
    features: ['Unlimited scans', 'Custom Golden References', 'API access', 'White-label reports', 'Priority support'],
    scans: -1, // unlimited
    interval: 'month'
  },
  pro_yearly: {
    name: 'Pro Annual',
    price: 99900,
    currency: 'usd',
    description: 'Best value - 2 months free',
    features: ['Everything in Pro', '2 months free', 'Annual billing'],
    scans: -1,
    interval: 'year'
  }
};

/**
 * Create a Stripe Checkout session
 */
export async function createCheckoutSession(request, env) {
  const { productId, customerId, successUrl, cancelUrl } = await request.json();
  
  const product = PRODUCTS[productId];
  if (!product) {
    return new Response(JSON.stringify({ error: 'Invalid product' }), { 
      status: 400,
      headers: { 'Content-Type': 'application/json' }
    });
  }
  
  const isSubscription = product.interval !== undefined;
  
  const sessionParams = new URLSearchParams({
    'payment_method_types[]': 'card',
    'line_items[0][price_data][currency]': product.currency,
    'line_items[0][price_data][product_data][name]': product.name,
    'line_items[0][price_data][product_data][description]': product.description,
    'line_items[0][price_data][unit_amount]': product.price.toString(),
    'line_items[0][quantity]': '1',
    'mode': isSubscription ? 'subscription' : 'payment',
    'success_url': successUrl || 'https://noizylab.ai/success?session_id={CHECKOUT_SESSION_ID}',
    'cancel_url': cancelUrl || 'https://noizylab.ai/pricing',
    'metadata[product_id]': productId,
    'metadata[scans]': product.scans.toString()
  });
  
  // Add recurring interval for subscriptions
  if (isSubscription) {
    sessionParams.append('line_items[0][price_data][recurring][interval]', product.interval);
  }
  
  // Add customer if provided
  if (customerId) {
    sessionParams.append('customer', customerId);
  }
  
  const response = await fetch('https://api.stripe.com/v1/checkout/sessions', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${env.STRIPE_SECRET_KEY}`,
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: sessionParams
  });
  
  const session = await response.json();
  
  if (session.error) {
    return new Response(JSON.stringify({ error: session.error.message }), {
      status: 400,
      headers: { 'Content-Type': 'application/json' }
    });
  }
  
  return new Response(JSON.stringify({ 
    sessionId: session.id,
    url: session.url 
  }), {
    headers: { 'Content-Type': 'application/json' }
  });
}

/**
 * Handle Stripe webhooks
 */
export async function handleWebhook(request, env) {
  const signature = request.headers.get('stripe-signature');
  const body = await request.text();
  
  // Verify webhook signature
  const isValid = await verifyWebhookSignature(body, signature, env.STRIPE_WEBHOOK_SECRET);
  if (!isValid) {
    return new Response('Invalid signature', { status: 400 });
  }
  
  const event = JSON.parse(body);
  
  switch (event.type) {
    case 'checkout.session.completed':
      await handleCheckoutComplete(event.data.object, env);
      break;
      
    case 'customer.subscription.created':
    case 'customer.subscription.updated':
      await handleSubscriptionUpdate(event.data.object, env);
      break;
      
    case 'customer.subscription.deleted':
      await handleSubscriptionCanceled(event.data.object, env);
      break;
      
    case 'invoice.payment_succeeded':
      await handleInvoicePaid(event.data.object, env);
      break;
      
    case 'invoice.payment_failed':
      await handlePaymentFailed(event.data.object, env);
      break;
  }
  
  return new Response(JSON.stringify({ received: true }), {
    headers: { 'Content-Type': 'application/json' }
  });
}

/**
 * Handle successful checkout
 */
async function handleCheckoutComplete(session, env) {
  const { customer, metadata, customer_email } = session;
  const productId = metadata.product_id;
  const scans = parseInt(metadata.scans);
  
  // Get or create user record
  let user = await env.KV_USERS.get(`user:${customer}`);
  if (user) {
    user = JSON.parse(user);
  } else {
    user = {
      id: customer,
      email: customer_email,
      scansRemaining: 0,
      totalScans: 0,
      subscription: null,
      createdAt: new Date().toISOString()
    };
  }
  
  // Add scans for one-time purchases
  if (scans > 0) {
    user.scansRemaining += scans;
    user.totalScans += scans;
  }
  
  // Track purchase
  user.purchases = user.purchases || [];
  user.purchases.push({
    productId,
    scans,
    timestamp: new Date().toISOString(),
    sessionId: session.id
  });
  
  await env.KV_USERS.put(`user:${customer}`, JSON.stringify(user));
  
  // Send confirmation email (via queue or direct)
  await sendConfirmationEmail(user.email, productId, scans, env);
}

/**
 * Handle subscription updates
 */
async function handleSubscriptionUpdate(subscription, env) {
  const { customer, status, current_period_end } = subscription;
  
  let user = await env.KV_USERS.get(`user:${customer}`);
  if (user) {
    user = JSON.parse(user);
    user.subscription = {
      id: subscription.id,
      status,
      currentPeriodEnd: new Date(current_period_end * 1000).toISOString(),
      plan: subscription.items.data[0]?.price?.id
    };
    
    // Pro subscribers get unlimited scans
    if (status === 'active') {
      user.scansRemaining = -1; // unlimited
    }
    
    await env.KV_USERS.put(`user:${customer}`, JSON.stringify(user));
  }
}

/**
 * Handle subscription cancellation
 */
async function handleSubscriptionCanceled(subscription, env) {
  const { customer } = subscription;
  
  let user = await env.KV_USERS.get(`user:${customer}`);
  if (user) {
    user = JSON.parse(user);
    user.subscription = null;
    user.scansRemaining = 0; // Reset to 0 when subscription ends
    await env.KV_USERS.put(`user:${customer}`, JSON.stringify(user));
  }
}

/**
 * Handle successful invoice payment (subscription renewal)
 */
async function handleInvoicePaid(invoice, env) {
  // Log successful payment for analytics
  const paymentRecord = {
    customerId: invoice.customer,
    amount: invoice.amount_paid,
    timestamp: new Date().toISOString(),
    invoiceId: invoice.id
  };
  
  // Store in analytics KV
  const monthKey = new Date().toISOString().slice(0, 7); // YYYY-MM
  let monthlyPayments = await env.KV_ANALYTICS.get(`payments:${monthKey}`);
  monthlyPayments = monthlyPayments ? JSON.parse(monthlyPayments) : [];
  monthlyPayments.push(paymentRecord);
  await env.KV_ANALYTICS.put(`payments:${monthKey}`, JSON.stringify(monthlyPayments));
}

/**
 * Handle failed payment
 */
async function handlePaymentFailed(invoice, env) {
  // Send payment failed notification
  const user = await env.KV_USERS.get(`user:${invoice.customer}`);
  if (user) {
    const userData = JSON.parse(user);
    await sendPaymentFailedEmail(userData.email, env);
  }
}

/**
 * Verify Stripe webhook signature
 */
async function verifyWebhookSignature(body, signature, secret) {
  if (!signature || !secret) return false;
  
  const parts = signature.split(',');
  let timestamp, sig;
  
  for (const part of parts) {
    const [key, value] = part.split('=');
    if (key === 't') timestamp = value;
    if (key === 'v1') sig = value;
  }
  
  if (!timestamp || !sig) return false;
  
  // Check timestamp is within 5 minutes
  const now = Math.floor(Date.now() / 1000);
  if (Math.abs(now - parseInt(timestamp)) > 300) return false;
  
  // Compute expected signature
  const payload = `${timestamp}.${body}`;
  const encoder = new TextEncoder();
  const key = await crypto.subtle.importKey(
    'raw',
    encoder.encode(secret),
    { name: 'HMAC', hash: 'SHA-256' },
    false,
    ['sign']
  );
  
  const signatureBuffer = await crypto.subtle.sign('HMAC', key, encoder.encode(payload));
  const expectedSig = Array.from(new Uint8Array(signatureBuffer))
    .map(b => b.toString(16).padStart(2, '0'))
    .join('');
  
  return sig === expectedSig;
}

/**
 * Send confirmation email (placeholder - integrate with your email provider)
 */
async function sendConfirmationEmail(email, productId, scans, env) {
  // TODO: Integrate with Resend, SendGrid, or Mailgun
  console.log(`Sending confirmation to ${email} for ${productId} (${scans} scans)`);
}

/**
 * Send payment failed email
 */
async function sendPaymentFailedEmail(email, env) {
  console.log(`Sending payment failed notification to ${email}`);
}

/**
 * Check if user has available scans
 */
export async function checkUserScans(customerId, env) {
  const user = await env.KV_USERS.get(`user:${customerId}`);
  if (!user) {
    return { hasScans: false, remaining: 0 };
  }
  
  const userData = JSON.parse(user);
  
  // -1 means unlimited (Pro subscription)
  if (userData.scansRemaining === -1) {
    return { hasScans: true, remaining: -1, unlimited: true };
  }
  
  return { 
    hasScans: userData.scansRemaining > 0, 
    remaining: userData.scansRemaining 
  };
}

/**
 * Consume a scan credit
 */
export async function consumeScan(customerId, env) {
  const user = await env.KV_USERS.get(`user:${customerId}`);
  if (!user) {
    return { success: false, error: 'User not found' };
  }
  
  const userData = JSON.parse(user);
  
  // Unlimited scans for Pro
  if (userData.scansRemaining === -1) {
    return { success: true, remaining: -1 };
  }
  
  if (userData.scansRemaining <= 0) {
    return { success: false, error: 'No scans remaining' };
  }
  
  userData.scansRemaining--;
  await env.KV_USERS.put(`user:${customerId}`, JSON.stringify(userData));
  
  return { success: true, remaining: userData.scansRemaining };
}

/**
 * Create customer portal session for managing subscriptions
 */
export async function createPortalSession(customerId, env) {
  const response = await fetch('https://api.stripe.com/v1/billing_portal/sessions', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${env.STRIPE_SECRET_KEY}`,
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: new URLSearchParams({
      'customer': customerId,
      'return_url': 'https://noizylab.ai/dashboard'
    })
  });
  
  const session = await response.json();
  return { url: session.url };
}

export { PRODUCTS, PRICES };
