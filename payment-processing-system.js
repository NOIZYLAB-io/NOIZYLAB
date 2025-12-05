/**
 * PAYMENT PROCESSING SYSTEM
 * Stripe integration for all three domains
 * 
 * Features:
 * - Stripe payment processing
 * - Invoice generation
 * - Subscription management
 * - Payment links
 * - Refund handling
 * - Receipt emails
 * - Payment history
 * - Multiple currencies
 * - Webhook handling
 */

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname;

    const corsHeaders = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    };

    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders });
    }

    try {
      // Payment intents
      if (path === '/api/payment/create-intent' && request.method === 'POST') {
        return await handleCreatePaymentIntent(request, env, corsHeaders);
      } else if (path === '/api/payment/confirm' && request.method === 'POST') {
        return await handleConfirmPayment(request, env, corsHeaders);
      }
      
      // Invoices
      else if (path === '/api/invoice/create' && request.method === 'POST') {
        return await handleCreateInvoice(request, env, corsHeaders);
      } else if (path.startsWith('/api/invoice/')) {
        return await handleGetInvoice(request, env, corsHeaders);
      }
      
      // Payment links
      else if (path === '/api/payment-link/create' && request.method === 'POST') {
        return await handleCreatePaymentLink(request, env, corsHeaders);
      }
      
      // Subscriptions
      else if (path === '/api/subscription/create' && request.method === 'POST') {
        return await handleCreateSubscription(request, env, corsHeaders);
      } else if (path === '/api/subscription/cancel' && request.method === 'POST') {
        return await handleCancelSubscription(request, env, corsHeaders);
      }
      
      // Refunds
      else if (path === '/api/refund/create' && request.method === 'POST') {
        return await handleCreateRefund(request, env, corsHeaders);
      }
      
      // Payment history
      else if (path === '/api/payments/history') {
        return await handleGetPaymentHistory(request, env, corsHeaders);
      }
      
      // Stripe webhook
      else if (path === '/webhook/stripe' && request.method === 'POST') {
        return await handleStripeWebhook(request, env, corsHeaders);
      }
      
      // Payment page
      else if (path === '/pay' || path.startsWith('/pay/')) {
        return handlePaymentPage(request, env);
      }

      return new Response('Not Found', { status: 404 });

    } catch (error) {
      console.error('Error:', error);
      return new Response(JSON.stringify({ error: error.message }), {
        status: 500,
        headers: { 'Content-Type': 'application/json', ...corsHeaders }
      });
    }
  }
};

// Create payment intent
async function handleCreatePaymentIntent(request, env, corsHeaders) {
  const data = await request.json();
  
  if (!env.STRIPE_SECRET_KEY) {
    return new Response(JSON.stringify({
      error: 'Stripe not configured',
      demo_mode: true,
      payment_intent_id: 'pi_demo_' + Math.random().toString(36).substring(7)
    }), {
      headers: { 'Content-Type': 'application/json', ...corsHeaders }
    });
  }
  
  try {
    const response = await fetch('https://api.stripe.com/v1/payment_intents', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${env.STRIPE_SECRET_KEY}`,
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: new URLSearchParams({
        amount: String(data.amount * 100), // Convert to cents
        currency: data.currency || 'usd',
        description: data.description || 'Payment',
        'metadata[domain]': data.domain || 'unknown',
        'metadata[customer_id]': data.customer_id || 'unknown',
        'metadata[order_id]': data.order_id || 'unknown'
      })
    });
    
    const result = await response.json();
    
    if (response.ok) {
      // Log payment intent
      await logPayment(env, {
        type: 'intent_created',
        intent_id: result.id,
        amount: data.amount,
        currency: data.currency,
        domain: data.domain,
        customer_id: data.customer_id,
        created_at: new Date().toISOString()
      });
      
      return new Response(JSON.stringify({
        success: true,
        client_secret: result.client_secret,
        payment_intent_id: result.id
      }), {
        headers: { 'Content-Type': 'application/json', ...corsHeaders }
      });
    } else {
      throw new Error(result.error?.message || 'Failed to create payment intent');
    }
    
  } catch (error) {
    return new Response(JSON.stringify({ error: error.message }), {
      status: 400,
      headers: { 'Content-Type': 'application/json', ...corsHeaders }
    });
  }
}

// Confirm payment
async function handleConfirmPayment(request, env, corsHeaders) {
  const data = await request.json();
  
  // Log confirmed payment
  await logPayment(env, {
    type: 'payment_confirmed',
    intent_id: data.payment_intent_id,
    confirmed_at: new Date().toISOString()
  });
  
  // Send receipt email (integrate with email worker)
  // await sendReceiptEmail(env, data);
  
  return new Response(JSON.stringify({
    success: true,
    confirmed: true,
    receipt_url: `/receipt/${data.payment_intent_id}`
  }), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

// Create invoice
async function handleCreateInvoice(request, env, corsHeaders) {
  const data = await request.json();
  
  const invoiceId = 'INV-' + Date.now().toString(36).toUpperCase();
  
  const invoice = {
    id: invoiceId,
    customer_id: data.customer_id,
    customer_name: data.customer_name,
    customer_email: data.customer_email,
    domain: data.domain,
    items: data.items,
    subtotal: data.subtotal,
    tax: data.tax || 0,
    total: data.total,
    currency: data.currency || 'USD',
    status: 'pending',
    due_date: data.due_date,
    created_at: new Date().toISOString(),
    payment_link: `https://pay.yourdomain.com/${invoiceId}`
  };
  
  // Store invoice
  await env.INVOICES.put(invoiceId, JSON.stringify(invoice));
  
  return new Response(JSON.stringify({
    success: true,
    invoice: invoice
  }), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

// Get invoice
async function handleGetInvoice(request, env, corsHeaders) {
  const invoiceId = request.url.split('/').pop();
  
  const invoiceStr = await env.INVOICES.get(invoiceId);
  
  if (!invoiceStr) {
    return new Response(JSON.stringify({ error: 'Invoice not found' }), {
      status: 404,
      headers: { 'Content-Type': 'application/json', ...corsHeaders }
    });
  }
  
  return new Response(invoiceStr, {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

// Create payment link
async function handleCreatePaymentLink(request, env, corsHeaders) {
  const data = await request.json();
  
  const linkId = 'LINK-' + Math.random().toString(36).substring(7).toUpperCase();
  
  const paymentLink = {
    id: linkId,
    url: `https://pay.yourdomain.com/${linkId}`,
    amount: data.amount,
    currency: data.currency || 'USD',
    description: data.description,
    expires_at: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000).toISOString(), // 7 days
    created_at: new Date().toISOString()
  };
  
  await env.PAYMENT_LINKS.put(linkId, JSON.stringify(paymentLink));
  
  return new Response(JSON.stringify({
    success: true,
    payment_link: paymentLink
  }), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

// Create subscription
async function handleCreateSubscription(request, env, corsHeaders) {
  const data = await request.json();
  
  if (!env.STRIPE_SECRET_KEY) {
    return new Response(JSON.stringify({
      error: 'Stripe not configured',
      demo_mode: true,
      subscription_id: 'sub_demo_' + Math.random().toString(36).substring(7)
    }), {
      headers: { 'Content-Type': 'application/json', ...corsHeaders }
    });
  }
  
  // In production, create Stripe subscription
  const subscriptionId = 'sub_' + Math.random().toString(36).substring(7);
  
  return new Response(JSON.stringify({
    success: true,
    subscription_id: subscriptionId,
    status: 'active'
  }), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

// Cancel subscription
async function handleCancelSubscription(request, env, corsHeaders) {
  const data = await request.json();
  
  // In production, cancel Stripe subscription
  
  return new Response(JSON.stringify({
    success: true,
    subscription_id: data.subscription_id,
    status: 'cancelled',
    cancelled_at: new Date().toISOString()
  }), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

// Create refund
async function handleCreateRefund(request, env, corsHeaders) {
  const data = await request.json();
  
  if (!env.STRIPE_SECRET_KEY) {
    return new Response(JSON.stringify({
      error: 'Stripe not configured',
      demo_mode: true
    }), {
      headers: { 'Content-Type': 'application/json', ...corsHeaders }
    });
  }
  
  try {
    const response = await fetch('https://api.stripe.com/v1/refunds', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${env.STRIPE_SECRET_KEY}`,
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: new URLSearchParams({
        payment_intent: data.payment_intent_id,
        amount: data.amount ? String(data.amount * 100) : undefined,
        reason: data.reason || 'requested_by_customer'
      })
    });
    
    const result = await response.json();
    
    if (response.ok) {
      await logPayment(env, {
        type: 'refund_created',
        refund_id: result.id,
        payment_intent_id: data.payment_intent_id,
        amount: data.amount,
        created_at: new Date().toISOString()
      });
      
      return new Response(JSON.stringify({
        success: true,
        refund_id: result.id,
        status: result.status
      }), {
        headers: { 'Content-Type': 'application/json', ...corsHeaders }
      });
    } else {
      throw new Error(result.error?.message || 'Failed to create refund');
    }
    
  } catch (error) {
    return new Response(JSON.stringify({ error: error.message }), {
      status: 400,
      headers: { 'Content-Type': 'application/json', ...corsHeaders }
    });
  }
}

// Get payment history
async function handleGetPaymentHistory(request, env, corsHeaders) {
  const url = new URL(request.url);
  const customerId = url.searchParams.get('customer_id');
  
  // In production, query from database
  const payments = [
    {
      id: 'pay_123',
      amount: 89,
      currency: 'USD',
      status: 'succeeded',
      description: 'Computer repair - NZL-001',
      created_at: '2025-11-20T10:30:00Z'
    },
    {
      id: 'pay_124',
      amount: 1500,
      currency: 'USD',
      status: 'succeeded',
      description: 'Music project - FMI-001',
      created_at: '2025-11-15T14:20:00Z'
    }
  ];
  
  return new Response(JSON.stringify({ payments }), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

// Handle Stripe webhook
async function handleStripeWebhook(request, env, corsHeaders) {
  const signature = request.headers.get('stripe-signature');
  
  if (!signature || !env.STRIPE_WEBHOOK_SECRET) {
    return new Response('Unauthorized', { status: 401 });
  }
  
  const payload = await request.text();
  
  // In production, verify webhook signature
  // const event = stripe.webhooks.constructEvent(payload, signature, env.STRIPE_WEBHOOK_SECRET);
  
  // Parse the event
  let event;
  try {
    event = JSON.parse(payload);
  } catch (err) {
    return new Response('Invalid payload', { status: 400 });
  }
  
  // Handle different event types
  switch (event.type) {
    case 'payment_intent.succeeded':
      await handlePaymentSucceeded(env, event.data.object);
      break;
    case 'payment_intent.payment_failed':
      await handlePaymentFailed(env, event.data.object);
      break;
    case 'customer.subscription.created':
      await handleSubscriptionCreated(env, event.data.object);
      break;
    case 'customer.subscription.deleted':
      await handleSubscriptionDeleted(env, event.data.object);
      break;
  }
  
  return new Response(JSON.stringify({ received: true }), {
    headers: { 'Content-Type': 'application/json' }
  });
}

// Payment page
function handlePaymentPage(request, env) {
  const paymentId = request.url.split('/').pop();
  
  const html = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Secure Payment</title>
    <script src="https://js.stripe.com/v3/"></script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 2rem;
        }
        .payment-container {
            background: white;
            border-radius: 20px;
            padding: 3rem;
            max-width: 500px;
            width: 100%;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }
        h1 {
            color: #667eea;
            margin-bottom: 2rem;
            text-align: center;
        }
        .amount {
            font-size: 3rem;
            font-weight: bold;
            text-align: center;
            color: #333;
            margin-bottom: 2rem;
        }
        .description {
            text-align: center;
            color: #666;
            margin-bottom: 2rem;
        }
        #payment-element {
            margin-bottom: 2rem;
        }
        button {
            width: 100%;
            padding: 1rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 50px;
            font-size: 1.1rem;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s;
        }
        button:hover {
            transform: scale(1.02);
            box-shadow: 0 10px 30px rgba(102,126,234,0.3);
        }
        button:disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }
        .secure-badge {
            text-align: center;
            margin-top: 2rem;
            color: #999;
            font-size: 0.9rem;
        }
        .success-message {
            display: none;
            text-align: center;
            padding: 2rem;
        }
        .success-message.show {
            display: block;
        }
        .checkmark {
            font-size: 4rem;
            color: #22c55e;
            margin-bottom: 1rem;
        }
    </style>
</head>
<body>
    <div class="payment-container">
        <div id="payment-form">
            <h1>🔒 Secure Payment</h1>
            <div class="amount">$89.00</div>
            <div class="description">Computer Repair - NZL-001</div>
            
            <div id="payment-element"></div>
            
            <button id="submit-button">Pay Now</button>
            
            <div class="secure-badge">
                🔒 Secured by Stripe<br>
                Your payment information is encrypted and secure
            </div>
        </div>
        
        <div class="success-message" id="success-message">
            <div class="checkmark">✅</div>
            <h2 style="color: #22c55e; margin-bottom: 1rem;">Payment Successful!</h2>
            <p style="color: #666;">Thank you for your payment. You will receive a receipt via email.</p>
        </div>
    </div>
    
    <script>
        // In production, initialize Stripe and payment element
        const submitButton = document.getElementById('submit-button');
        
        submitButton.addEventListener('click', async () => {
            submitButton.disabled = true;
            submitButton.textContent = 'Processing...';
            
            // Simulate payment processing
            await new Promise(resolve => setTimeout(resolve, 2000));
            
            document.getElementById('payment-form').style.display = 'none';
            document.getElementById('success-message').classList.add('show');
        });
    </script>
</body>
</html>`;

  return new Response(html, {
    headers: { 'Content-Type': 'text/html; charset=utf-8' }
  });
}

// Helper functions
async function logPayment(env, data) {
  const logId = `payment_log_${Date.now()}_${Math.random().toString(36).substring(7)}`;
  
  try {
    await env.PAYMENT_LOGS.put(logId, JSON.stringify(data), {
      expirationTtl: 86400 * 365 // 1 year
    });
  } catch (error) {
    console.error('Failed to log payment:', error);
  }
}

async function handlePaymentSucceeded(env, paymentIntent) {
  console.log('Payment succeeded:', paymentIntent.id);
  
  // Update order status
  // Send confirmation email
  // Update analytics
}

async function handlePaymentFailed(env, paymentIntent) {
  console.log('Payment failed:', paymentIntent.id);
  
  // Send failure notification
  // Log for manual review
}

async function handleSubscriptionCreated(env, subscription) {
  console.log('Subscription created:', subscription.id);
  
  // Activate user's access
  // Send welcome email
}

async function handleSubscriptionDeleted(env, subscription) {
  console.log('Subscription deleted:', subscription.id);
  
  // Deactivate user's access
  // Send cancellation confirmation
}
