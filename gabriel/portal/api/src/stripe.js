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
 * Send confirmation email via Resend
 */
async function sendConfirmationEmail(email, productId, scans, env) {
  const product = PRODUCTS[productId];
  if (!product || !env.RESEND_API_KEY) {
    console.log(`Skipping email: missing product or API key`);
    return;
  }

  const isUnlimited = scans === -1;
  const scansText = isUnlimited ? 'Unlimited scans' : `${scans} scan${scans > 1 ? 's' : ''}`;

  try {
    await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${env.RESEND_API_KEY}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        from: 'NoizyLab GABRIEL <noreply@noizylab.com>',
        reply_to: 'support@noizylab.com',
        to: [email],
        subject: `✅ Payment confirmed - ${product.name}`,
        html: `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #0a0a0a; color: #ffffff; margin: 0; padding: 40px 20px; }
    .container { max-width: 600px; margin: 0 auto; }
    .header { text-align: center; margin-bottom: 40px; }
    .logo { font-size: 24px; font-weight: bold; color: #22c55e; }
    .content { background: #111; border-radius: 16px; padding: 32px; border: 1px solid #222; }
    h1 { color: #22c55e; margin: 0 0 8px 0; }
    .subtitle { color: #888; margin: 0 0 24px 0; }
    .receipt { background: #1a1a1a; border-radius: 12px; padding: 24px; margin: 24px 0; }
    .receipt-row { display: flex; justify-content: space-between; padding: 12px 0; border-bottom: 1px solid #333; }
    .receipt-row:last-child { border-bottom: none; }
    .receipt-label { color: #888; }
    .receipt-value { font-weight: 600; }
    .total { font-size: 24px; color: #22c55e; }
    p { line-height: 1.6; color: #888; margin: 16px 0; }
    .button { display: inline-block; background: #22c55e; color: #000; padding: 14px 28px; border-radius: 8px; text-decoration: none; font-weight: 600; margin: 24px 0; }
    .footer { text-align: center; margin-top: 40px; color: #666; font-size: 12px; }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <div class="logo">🔬 NoizyLab GABRIEL</div>
    </div>
    <div class="content">
      <h1>Payment Received ✓</h1>
      <p class="subtitle">Thank you for your purchase!</p>

      <div class="receipt">
        <div class="receipt-row">
          <span class="receipt-label">Product</span>
          <span class="receipt-value">${product.name}</span>
        </div>
        <div class="receipt-row">
          <span class="receipt-label">Scans Included</span>
          <span class="receipt-value">${scansText}</span>
        </div>
        <div class="receipt-row">
          <span class="receipt-label">Date</span>
          <span class="receipt-value">${new Date().toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })}</span>
        </div>
        <div class="receipt-row">
          <span class="receipt-label">Amount Paid</span>
          <span class="receipt-value total">$${(product.price / 100).toFixed(2)}</span>
        </div>
      </div>

      <a href="https://gabriel.noizylab.com/dashboard" class="button">Start Scanning →</a>

      <p style="font-size: 12px; color: #666;">This receipt is for your records. For billing questions, reply to this email.</p>
    </div>
    <div class="footer">
      <p>NoizyLab Inc. • Anaheim, California</p>
    </div>
  </div>
</body>
</html>
        `,
      }),
    });
    console.log(`Confirmation email sent to ${email}`);
  } catch (error) {
    console.error('Failed to send confirmation email:', error);
  }
}

/**
 * Send payment failed email via Resend
 */
async function sendPaymentFailedEmail(email, env) {
  if (!env.RESEND_API_KEY) {
    console.log(`Skipping email: missing API key`);
    return;
  }

  try {
    await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${env.RESEND_API_KEY}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        from: 'NoizyLab GABRIEL <noreply@noizylab.com>',
        reply_to: 'support@noizylab.com',
        to: [email],
        subject: '⚠️ Payment failed - Action required',
        html: `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #0a0a0a; color: #ffffff; margin: 0; padding: 40px 20px; }
    .container { max-width: 600px; margin: 0 auto; }
    .header { text-align: center; margin-bottom: 40px; }
    .logo { font-size: 24px; font-weight: bold; color: #22c55e; }
    .content { background: #111; border-radius: 16px; padding: 32px; border: 1px solid #ef4444; }
    h1 { color: #ef4444; margin: 0 0 16px 0; }
    p { line-height: 1.6; color: #888; margin: 16px 0; }
    .button { display: inline-block; background: #22c55e; color: #000; padding: 14px 28px; border-radius: 8px; text-decoration: none; font-weight: 600; margin: 24px 0; }
    .footer { text-align: center; margin-top: 40px; color: #666; font-size: 12px; }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <div class="logo">🔬 NoizyLab GABRIEL</div>
    </div>
    <div class="content">
      <h1>⚠️ Payment Failed</h1>
      <p>We couldn't process your payment. This may be due to:</p>
      <ul style="color: #888; margin: 16px 0;">
        <li>Insufficient funds</li>
        <li>Expired card</li>
        <li>Card declined by bank</li>
      </ul>
      <p>Please update your payment method to continue using GABRIEL without interruption.</p>

      <a href="https://gabriel.noizylab.com/billing" class="button">Update Payment Method →</a>

      <p style="font-size: 12px; color: #666;">Questions? Reply to this email and we'll help you out.</p>
    </div>
    <div class="footer">
      <p>NoizyLab Inc. • Anaheim, California</p>
    </div>
  </div>
</body>
</html>
        `,
      }),
    });
    console.log(`Payment failed email sent to ${email}`);
  } catch (error) {
    console.error('Failed to send payment failed email:', error);
  }
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
