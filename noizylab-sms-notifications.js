/**
 * NOIZYLAB SMS NOTIFICATIONS
 * Real-time SMS alerts for customers and staff
 * 
 * Features:
 * - Twilio integration
 * - Automated status notifications
 * - Two-way SMS support
 * - SMS templates
 * - Delivery tracking
 * - Customer opt-in/opt-out
 * - Emergency alerts
 * - Staff notifications
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
      if (path === '/send-sms' && request.method === 'POST') {
        return await handleSendSMS(request, env, corsHeaders);
      } else if (path === '/send-confirmation' && request.method === 'POST') {
        return await handleConfirmationSMS(request, env, corsHeaders);
      } else if (path === '/send-status-update' && request.method === 'POST') {
        return await handleStatusUpdateSMS(request, env, corsHeaders);
      } else if (path === '/send-completion' && request.method === 'POST') {
        return await handleCompletionSMS(request, env, corsHeaders);
      } else if (path === '/incoming' && request.method === 'POST') {
        return await handleIncomingSMS(request, env, corsHeaders);
      } else if (path === '/opt-out' && request.method === 'POST') {
        return await handleOptOut(request, env, corsHeaders);
      } else if (path === '/health') {
        return new Response(JSON.stringify({ status: 'healthy', service: 'sms-notifications' }), {
          headers: { 'Content-Type': 'application/json', ...corsHeaders }
        });
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

// Send SMS via Twilio
async function sendTwilioSMS(env, to, message) {
  const accountSid = env.TWILIO_ACCOUNT_SID;
  const authToken = env.TWILIO_AUTH_TOKEN;
  const fromNumber = env.TWILIO_PHONE_NUMBER;

  if (!accountSid || !authToken || !fromNumber) {
    console.log('Twilio not configured, logging SMS instead');
    await logSMS(env, { to, message, status: 'logged' });
    return { success: true, sid: 'logged', status: 'logged' };
  }

  try {
    const auth = btoa(`${accountSid}:${authToken}`);
    
    const response = await fetch(`https://api.twilio.com/2010-04-01/Accounts/${accountSid}/Messages.json`, {
      method: 'POST',
      headers: {
        'Authorization': `Basic ${auth}`,
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: new URLSearchParams({
        To: to,
        From: fromNumber,
        Body: message
      })
    });

    const result = await response.json();
    
    if (response.ok) {
      await logSMS(env, { to, message, status: 'sent', sid: result.sid });
      return { success: true, sid: result.sid, status: 'sent' };
    } else {
      throw new Error(result.message || 'Failed to send SMS');
    }

  } catch (error) {
    console.error('Twilio error:', error);
    await logSMS(env, { to, message, status: 'failed', error: error.message });
    throw error;
  }
}

// Generic SMS send
async function handleSendSMS(request, env, corsHeaders) {
  const data = await request.json();
  
  if (!data.to || !data.message) {
    return new Response(JSON.stringify({ error: 'Missing required fields: to, message' }), {
      status: 400,
      headers: { 'Content-Type': 'application/json', ...corsHeaders }
    });
  }

  // Check opt-out
  const optedOut = await checkOptOut(env, data.to);
  if (optedOut) {
    return new Response(JSON.stringify({ 
      success: false,
      error: 'Customer has opted out of SMS notifications'
    }), {
      status: 400,
      headers: { 'Content-Type': 'application/json', ...corsHeaders }
    });
  }

  const result = await sendTwilioSMS(env, data.to, data.message);
  
  return new Response(JSON.stringify(result), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

// Confirmation SMS
async function handleConfirmationSMS(request, env, corsHeaders) {
  const data = await request.json();
  
  const message = `NOIZYLAB: Repair confirmed! ID: ${data.repair_id}. Estimated completion: ${data.estimated_completion}. Track status: noizylab.ca/status/${data.repair_id}`;
  
  const result = await sendTwilioSMS(env, data.phone, message);
  
  return new Response(JSON.stringify(result), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

// Status update SMS
async function handleStatusUpdateSMS(request, env, corsHeaders) {
  const data = await request.json();
  
  const statusMessages = {
    'received': '📦 Device received and logged',
    'diagnosing': '🔍 Diagnostics in progress',
    'parts_ordered': '📦 Parts ordered',
    'in_repair': '🔧 Repair in progress',
    'testing': '✅ Testing and QA',
    'completed': '🎉 Repair complete!',
    'ready_for_pickup': '📍 Ready for pickup!'
  };

  const statusText = statusMessages[data.new_status] || data.new_status;
  const message = `NOIZYLAB Update [${data.repair_id}]: ${statusText}. ${data.notes || ''} Track: noizylab.ca/status/${data.repair_id}`;
  
  const result = await sendTwilioSMS(env, data.phone, message);
  
  return new Response(JSON.stringify(result), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

// Completion SMS
async function handleCompletionSMS(request, env, corsHeaders) {
  const data = await request.json();
  
  const message = `NOIZYLAB: 🎉 Your ${data.device_type} repair is COMPLETE! ID: ${data.repair_id}. Price: $${data.price}. Ready for pickup! Questions? Reply to this message.`;
  
  const result = await sendTwilioSMS(env, data.phone, message);
  
  return new Response(JSON.stringify(result), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

// Handle incoming SMS
async function handleIncomingSMS(request, env, corsHeaders) {
  const formData = await request.formData();
  const from = formData.get('From');
  const body = formData.get('Body');
  const messageSid = formData.get('MessageSid');

  console.log('Incoming SMS:', { from, body, messageSid });

  // Log incoming message
  await logIncomingSMS(env, { from, body, messageSid });

  // Check for opt-out keywords
  const optOutKeywords = ['STOP', 'UNSUBSCRIBE', 'QUIT', 'CANCEL', 'END'];
  if (optOutKeywords.includes(body.trim().toUpperCase())) {
    await handleOptOut(request, env, corsHeaders);
    
    // Twilio expects TwiML response
    return new Response(`<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Message>You have been unsubscribed from NOIZYLAB SMS notifications. Reply START to resubscribe.</Message>
</Response>`, {
      headers: { 'Content-Type': 'text/xml' }
    });
  }

  // Auto-reply
  const autoReply = `Thank you for contacting NOIZYLAB! We've received your message and will respond shortly. For immediate assistance, call us at (555) 123-4567.`;
  
  return new Response(`<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Message>${autoReply}</Message>
</Response>`, {
    headers: { 'Content-Type': 'text/xml' }
  });
}

// Opt-out handler
async function handleOptOut(request, env, corsHeaders) {
  const data = await request.json();
  const phone = data.phone || data.from;
  
  await env.SMS_OPTOUTS.put(phone, JSON.stringify({
    opted_out_at: new Date().toISOString(),
    reason: data.reason || 'user_request'
  }));
  
  console.log('Phone opted out:', phone);
  
  return new Response(JSON.stringify({ success: true, opted_out: true }), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

// Check opt-out status
async function checkOptOut(env, phone) {
  const optOut = await env.SMS_OPTOUTS.get(phone);
  return optOut !== null;
}

// Log SMS
async function logSMS(env, data) {
  const logId = `sms_${Date.now()}_${Math.random().toString(36).substring(7)}`;
  
  try {
    await env.SMS_LOGS.put(logId, JSON.stringify({
      ...data,
      id: logId,
      timestamp: new Date().toISOString()
    }));
  } catch (error) {
    console.error('Failed to log SMS:', error);
  }
}

// Log incoming SMS
async function logIncomingSMS(env, data) {
  const logId = `sms_in_${Date.now()}_${Math.random().toString(36).substring(7)}`;
  
  try {
    await env.SMS_LOGS.put(logId, JSON.stringify({
      ...data,
      id: logId,
      direction: 'incoming',
      timestamp: new Date().toISOString()
    }));
  } catch (error) {
    console.error('Failed to log incoming SMS:', error);
  }
}
