/**
 * NOIZYLAB BUSINESS PORTAL WORKER
 * Customer Intake & Repair Management
 * Production Ready for Cloudflare Workers
 */

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    
    const corsHeaders = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    };
    
    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders });
    }
    
    try {
      // Health check
      if (url.pathname === '/health') {
        return jsonResponse({
          status: 'operational',
          service: 'NOIZYLAB Business Portal',
          timestamp: new Date().toISOString()
        }, corsHeaders);
      }
      
      // Customer intake form
      if (url.pathname === '/intake' && request.method === 'POST') {
        return await handleIntake(request, env, corsHeaders);
      }
      
      // Get repair status
      if (url.pathname.startsWith('/status/')) {
        const repairId = url.pathname.split('/')[2];
        return await getRepairStatus(repairId, env, corsHeaders);
      }
      
      // List all repairs
      if (url.pathname === '/repairs' && request.method === 'GET') {
        return await listRepairs(env, corsHeaders);
      }
      
      // Update repair
      if (url.pathname.startsWith('/repair/') && request.method === 'PUT') {
        const repairId = url.pathname.split('/')[2];
        return await updateRepair(repairId, request, env, corsHeaders);
      }
      
      // Dashboard stats
      if (url.pathname === '/dashboard') {
        return await getDashboardStats(env, corsHeaders);
      }
      
      // Landing page
      if (url.pathname === '/' || url.pathname === '/index.html') {
        return htmlResponse(getLandingPage(), corsHeaders);
      }
      
      // Repair form page
      if (url.pathname === '/submit') {
        return htmlResponse(getSubmitPage(), corsHeaders);
      }
      
      return jsonResponse({ error: 'Not found' }, corsHeaders, 404);
      
    } catch (error) {
      return jsonResponse({ error: error.message }, corsHeaders, 500);
    }
  }
};

/**
 * Handle customer intake
 */
async function handleIntake(request, env, corsHeaders) {
  const data = await request.json();
  
  // Validate required fields
  const required = ['name', 'email', 'phone', 'device', 'issue'];
  for (const field of required) {
    if (!data[field]) {
      return jsonResponse({
        error: `Missing required field: ${field}`
      }, corsHeaders, 400);
    }
  }
  
  // Generate repair ID
  const repairId = generateRepairId();
  
  // Create repair record
  const repair = {
    id: repairId,
    customer: {
      name: data.name,
      email: data.email,
      phone: data.phone,
      address: data.address || ''
    },
    device: {
      type: data.device,
      model: data.model || '',
      serial: data.serial || ''
    },
    issue: data.issue,
    priority: data.priority || 'normal',
    status: 'pending',
    created_at: new Date().toISOString(),
    updated_at: new Date().toISOString(),
    estimated_completion: calculateEstimatedCompletion(),
    price: 89.00
  };
  
  // Store in D1 database
  try {
    await env.DB.prepare(`
      INSERT INTO repairs (
        id, customer_name, customer_email, customer_phone, 
        device_type, device_model, issue, status, 
        created_at, price
      ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    `).bind(
      repair.id,
      repair.customer.name,
      repair.customer.email,
      repair.customer.phone,
      repair.device.type,
      repair.device.model,
      repair.issue,
      repair.status,
      repair.created_at,
      repair.price
    ).run();
  } catch (error) {
    console.error('Database error:', error);
    // Continue even if DB fails - can store in KV as backup
  }
  
  // Store in KV as backup
  await env.REPAIRS.put(
    `repair:${repairId}`,
    JSON.stringify(repair),
    { expirationTtl: 7776000 } // 90 days
  );
  
  // Trigger workflow (if available)
  if (env.WORKFLOW) {
    try {
      await triggerWorkflow(repair, env);
    } catch (error) {
      console.error('Workflow trigger error:', error);
    }
  }
  
  // Send confirmation email (AI-generated)
  if (env.ANTHROPIC_API_KEY) {
    try {
      await sendConfirmationEmail(repair, env);
    } catch (error) {
      console.error('Email error:', error);
    }
  }
  
  return jsonResponse({
    success: true,
    repair_id: repairId,
    message: 'Repair request submitted successfully',
    estimated_completion: repair.estimated_completion,
    tracking_url: `/status/${repairId}`
  }, corsHeaders);
}

/**
 * Get repair status
 */
async function getRepairStatus(repairId, env, corsHeaders) {
  // Try KV first
  const repairData = await env.REPAIRS.get(`repair:${repairId}`);
  
  if (repairData) {
    const repair = JSON.parse(repairData);
    return jsonResponse({
      success: true,
      repair: repair
    }, corsHeaders);
  }
  
  // Try database
  try {
    const result = await env.DB.prepare(
      'SELECT * FROM repairs WHERE id = ?'
    ).bind(repairId).first();
    
    if (result) {
      return jsonResponse({
        success: true,
        repair: result
      }, corsHeaders);
    }
  } catch (error) {
    console.error('Database error:', error);
  }
  
  return jsonResponse({
    error: 'Repair not found'
  }, corsHeaders, 404);
}

/**
 * List all repairs
 */
async function listRepairs(env, corsHeaders) {
  try {
    const results = await env.DB.prepare(`
      SELECT * FROM repairs 
      ORDER BY created_at DESC 
      LIMIT 100
    `).all();
    
    return jsonResponse({
      success: true,
      repairs: results.results,
      count: results.results.length
    }, corsHeaders);
  } catch (error) {
    return jsonResponse({
      error: 'Database error',
      message: error.message
    }, corsHeaders, 500);
  }
}

/**
 * Update repair status
 */
async function updateRepair(repairId, request, env, corsHeaders) {
  const data = await request.json();
  
  try {
    // Update in database
    await env.DB.prepare(`
      UPDATE repairs 
      SET status = ?, updated_at = ?
      WHERE id = ?
    `).bind(
      data.status,
      new Date().toISOString(),
      repairId
    ).run();
    
    // Update in KV
    const repairData = await env.REPAIRS.get(`repair:${repairId}`);
    if (repairData) {
      const repair = JSON.parse(repairData);
      repair.status = data.status;
      repair.updated_at = new Date().toISOString();
      await env.REPAIRS.put(`repair:${repairId}`, JSON.stringify(repair));
    }
    
    return jsonResponse({
      success: true,
      message: 'Repair updated successfully'
    }, corsHeaders);
  } catch (error) {
    return jsonResponse({
      error: 'Update failed',
      message: error.message
    }, corsHeaders, 500);
  }
}

/**
 * Get dashboard statistics
 */
async function getDashboardStats(env, corsHeaders) {
  try {
    const stats = {
      total: 0,
      pending: 0,
      in_progress: 0,
      completed: 0,
      revenue: 0,
      avg_repair_time: 0
    };
    
    // Get counts by status
    const results = await env.DB.prepare(`
      SELECT 
        status,
        COUNT(*) as count,
        SUM(price) as total_price
      FROM repairs
      GROUP BY status
    `).all();
    
    for (const row of results.results) {
      stats.total += row.count;
      stats.revenue += row.total_price || 0;
      
      if (row.status === 'pending') stats.pending = row.count;
      if (row.status === 'in_progress') stats.in_progress = row.count;
      if (row.status === 'completed') stats.completed = row.count;
    }
    
    // Calculate monthly rate
    const monthlyRevenue = stats.revenue;
    const annualProjection = monthlyRevenue * 12;
    
    return jsonResponse({
      success: true,
      stats: stats,
      projections: {
        monthly_revenue: monthlyRevenue,
        annual_projection: annualProjection,
        target: 267000,
        gap: 267000 - annualProjection
      }
    }, corsHeaders);
  } catch (error) {
    return jsonResponse({
      error: 'Stats calculation failed',
      message: error.message
    }, corsHeaders, 500);
  }
}

/**
 * Trigger workflow
 */
async function triggerWorkflow(repair, env) {
  await fetch(`https://noizylab-workflow.${env.ACCOUNT_ID}.workers.dev/trigger`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ repair_id: repair.id })
  });
}

/**
 * Send confirmation email via Claude
 */
async function sendConfirmationEmail(repair, env) {
  const prompt = `Write a professional, friendly confirmation email for a computer repair submission:

Customer: ${repair.customer.name}
Device: ${repair.device.type} ${repair.device.model}
Issue: ${repair.issue}
Repair ID: ${repair.id}
Estimated completion: ${repair.estimated_completion}
Price: $${repair.price}

Keep it concise, reassuring, and professional.`;

  const response = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'x-api-key': env.ANTHROPIC_API_KEY,
      'anthropic-version': '2023-06-01'
    },
    body: JSON.stringify({
      model: 'claude-sonnet-4-20250514',
      max_tokens: 1024,
      messages: [{ role: 'user', content: prompt }]
    })
  });
  
  const data = await response.json();
  const email = data.content[0].text;
  
  // Here you would integrate with an email service
  console.log('Email generated:', email);
}

/**
 * Utility functions
 */
function generateRepairId() {
  const timestamp = Date.now().toString(36);
  const random = Math.random().toString(36).substr(2, 5);
  return `NZL-${timestamp}-${random}`.toUpperCase();
}

function calculateEstimatedCompletion() {
  const now = new Date();
  now.setDate(now.getDate() + 2); // 2 business days
  return now.toISOString().split('T')[0];
}

function jsonResponse(data, headers, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { ...headers, 'Content-Type': 'application/json' }
  });
}

function htmlResponse(html, headers) {
  return new Response(html, {
    headers: { ...headers, 'Content-Type': 'text/html' }
  });
}

/**
 * Landing page HTML
 */
function getLandingPage() {
  return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NOIZYLAB - Computer Repair Services</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            max-width: 800px;
            width: 100%;
            padding: 60px;
            text-align: center;
        }
        h1 {
            color: #667eea;
            font-size: 3em;
            margin-bottom: 10px;
        }
        .tagline {
            color: #666;
            font-size: 1.2em;
            margin-bottom: 40px;
        }
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 30px;
            margin: 40px 0;
            text-align: left;
        }
        .feature {
            padding: 20px;
            background: #f8f9fa;
            border-radius: 10px;
        }
        .feature h3 {
            color: #667eea;
            margin-bottom: 10px;
        }
        .cta {
            background: #667eea;
            color: white;
            border: none;
            padding: 20px 60px;
            font-size: 1.2em;
            border-radius: 50px;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
            margin-top: 30px;
            transition: all 0.3s;
        }
        .cta:hover {
            background: #764ba2;
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        }
        .price {
            font-size: 2.5em;
            color: #667eea;
            font-weight: bold;
            margin: 30px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔧 NOIZYLAB</h1>
        <p class="tagline">Professional Computer Repair Services</p>
        
        <div class="price">$89 Flat Rate</div>
        
        <div class="features">
            <div class="feature">
                <h3>⚡ Fast Turnaround</h3>
                <p>Most repairs completed in 2 business days</p>
            </div>
            <div class="feature">
                <h3>🎯 Expert Diagnosis</h3>
                <p>AI-powered diagnostics + 40 years experience</p>
            </div>
            <div class="feature">
                <h3>💰 Flat Pricing</h3>
                <p>$89 per repair, no hidden fees</p>
            </div>
            <div class="feature">
                <h3>🚚 Free Shipping</h3>
                <p>Prepaid labels included</p>
            </div>
        </div>
        
        <a href="/submit" class="cta">Submit Repair Request</a>
        
        <p style="margin-top: 40px; color: #999;">
            Powered by AI GENIUS | GORUNFREE Technology
        </p>
    </div>
</body>
</html>`;
}

/**
 * Submit form page
 */
function getSubmitPage() {
  return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Submit Repair - NOIZYLAB</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 40px 20px;
        }
        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            max-width: 600px;
            width: 100%;
            margin: 0 auto;
            padding: 40px;
        }
        h1 {
            color: #667eea;
            margin-bottom: 30px;
            text-align: center;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            color: #333;
            font-weight: 500;
        }
        input, textarea, select {
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 16px;
            transition: border 0.3s;
        }
        input:focus, textarea:focus, select:focus {
            outline: none;
            border-color: #667eea;
        }
        textarea {
            min-height: 100px;
            resize: vertical;
        }
        button {
            width: 100%;
            background: #667eea;
            color: white;
            border: none;
            padding: 15px;
            font-size: 18px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s;
        }
        button:hover {
            background: #764ba2;
        }
        .success {
            background: #10b981;
            color: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            display: none;
        }
        .error {
            background: #ef4444;
            color: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Submit Repair Request</h1>
        
        <div id="success" class="success"></div>
        <div id="error" class="error"></div>
        
        <form id="repairForm">
            <div class="form-group">
                <label for="name">Name *</label>
                <input type="text" id="name" required>
            </div>
            
            <div class="form-group">
                <label for="email">Email *</label>
                <input type="email" id="email" required>
            </div>
            
            <div class="form-group">
                <label for="phone">Phone *</label>
                <input type="tel" id="phone" required>
            </div>
            
            <div class="form-group">
                <label for="device">Device Type *</label>
                <select id="device" required>
                    <option value="">Select...</option>
                    <option value="Desktop PC">Desktop PC</option>
                    <option value="Laptop">Laptop</option>
                    <option value="Mac">Mac</option>
                    <option value="Server">Server</option>
                    <option value="Other">Other</option>
                </select>
            </div>
            
            <div class="form-group">
                <label for="model">Model</label>
                <input type="text" id="model">
            </div>
            
            <div class="form-group">
                <label for="issue">Describe the Issue *</label>
                <textarea id="issue" required></textarea>
            </div>
            
            <button type="submit">Submit Request ($89)</button>
        </form>
    </div>
    
    <script>
        document.getElementById('repairForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const data = {
                name: document.getElementById('name').value,
                email: document.getElementById('email').value,
                phone: document.getElementById('phone').value,
                device: document.getElementById('device').value,
                model: document.getElementById('model').value,
                issue: document.getElementById('issue').value
            };
            
            try {
                const response = await fetch('/intake', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });
                
                const result = await response.json();
                
                if (result.success) {
                    document.getElementById('success').textContent = 
                        \`Success! Your repair ID is: \${result.repair_id}. Check status at \${result.tracking_url}\`;
                    document.getElementById('success').style.display = 'block';
                    document.getElementById('repairForm').reset();
                } else {
                    throw new Error(result.error || 'Submission failed');
                }
            } catch (error) {
                document.getElementById('error').textContent = error.message;
                document.getElementById('error').style.display = 'block';
            }
        });
    </script>
</body>
</html>`;
}
