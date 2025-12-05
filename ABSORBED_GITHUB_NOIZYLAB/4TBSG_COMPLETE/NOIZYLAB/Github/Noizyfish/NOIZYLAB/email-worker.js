// Email Worker Template for NoizyLab
// ===================================
// Cloudflare Worker for email processing and routing

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    
    // Email processing endpoint
    if (url.pathname === '/email/process' && request.method === 'POST') {
      const emailData = await request.json();
      
      // Process email
      const result = await processEmail(emailData, env);
      
      return new Response(JSON.stringify(result), {
        headers: { 'Content-Type': 'application/json' }
      });
    }
    
    // Email validation endpoint
    if (url.pathname === '/email/validate' && request.method === 'POST') {
      const { email } = await request.json();
      const isValid = validateEmail(email);
      
      return new Response(JSON.stringify({ valid: isValid }), {
        headers: { 'Content-Type': 'application/json' }
      });
    }
    
    return new Response('NoizyLab Email Worker', { status: 200 });
  }
};

async function processEmail(emailData, env) {
  // Use D1 database if available
  if (env.DB) {
    await env.DB.prepare(
      'INSERT INTO email_log (email, subject, processed_at) VALUES (?, ?, ?)'
    ).bind(emailData.email, emailData.subject, new Date().toISOString()).run();
  }
  
  return {
    status: 'processed',
    email: emailData.email,
    timestamp: new Date().toISOString()
  };
}

function validateEmail(email) {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(email);
}

