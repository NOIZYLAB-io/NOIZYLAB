// NOIZYLAB CORE API WORKER
// Handles all backend operations, AI diagnostics, database access

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname;

    // CORS headers
    const corsHeaders = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    };

    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders });
    }

    try {
      // Route handling
      if (path === '/api/health') {
        return jsonResponse({ status: 'operational', timestamp: new Date().toISOString() }, corsHeaders);
      }

      // CUSTOMER ENDPOINTS
      if (path === '/api/customers' && request.method === 'POST') {
        return await createCustomer(request, env, corsHeaders);
      }
      if (path === '/api/customers' && request.method === 'GET') {
        return await listCustomers(url, env, corsHeaders);
      }
      if (path.startsWith('/api/customers/') && request.method === 'GET') {
        const customerId = path.split('/')[3];
        return await getCustomer(customerId, env, corsHeaders);
      }

      // REPAIR ENDPOINTS
      if (path === '/api/repairs' && request.method === 'POST') {
        return await createRepair(request, env, corsHeaders);
      }
      if (path === '/api/repairs' && request.method === 'GET') {
        return await listRepairs(url, env, corsHeaders);
      }
      if (path.startsWith('/api/repairs/') && request.method === 'GET') {
        const repairId = path.split('/')[3];
        return await getRepair(repairId, env, corsHeaders);
      }
      if (path.startsWith('/api/repairs/') && request.method === 'PUT') {
        const repairId = path.split('/')[3];
        return await updateRepair(repairId, request, env, corsHeaders);
      }

      // AI DIAGNOSTIC ENDPOINTS
      if (path === '/api/diagnose' && request.method === 'POST') {
        return await aiDiagnose(request, env, corsHeaders);
      }

      // ANALYTICS ENDPOINTS
      if (path === '/api/analytics/today' && request.method === 'GET') {
        return await getTodayAnalytics(env, corsHeaders);
      }
      if (path === '/api/analytics/range' && request.method === 'GET') {
        return await getAnalyticsRange(url, env, corsHeaders);
      }

      // EMAIL ENDPOINTS
      if (path === '/api/email/send' && request.method === 'POST') {
        return await sendEmail(request, env, corsHeaders);
      }
      if (path === '/api/email/queue' && request.method === 'GET') {
        return await getEmailQueue(env, corsHeaders);
      }

      // VOICE COMMAND ENDPOINT
      if (path === '/api/voice' && request.method === 'POST') {
        return await processVoiceCommand(request, env, corsHeaders);
      }

      // DASHBOARD DATA
      if (path === '/api/dashboard' && request.method === 'GET') {
        return await getDashboardData(env, corsHeaders);
      }

      return jsonResponse({ error: 'Not found' }, corsHeaders, 404);

    } catch (error) {
      return jsonResponse({ error: error.message }, corsHeaders, 500);
    }
  }
};

// CUSTOMER FUNCTIONS
async function createCustomer(request, env, corsHeaders) {
  const data = await request.json();
  const customerId = generateId('CUST');
  
  const result = await env.DB.prepare(`
    INSERT INTO customers (customer_id, email, name, phone, address, city, province, postal_code, preferred_contact)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
  `).bind(
    customerId,
    data.email,
    data.name,
    data.phone || null,
    data.address || null,
    data.city || null,
    data.province || null,
    data.postal_code || null,
    data.preferred_contact || 'email'
  ).run();

  return jsonResponse({ 
    success: true, 
    customer_id: customerId,
    message: 'Customer created successfully' 
  }, corsHeaders);
}

async function getCustomer(customerId, env, corsHeaders) {
  const customer = await env.DB.prepare('SELECT * FROM customers WHERE customer_id = ?')
    .bind(customerId).first();
  
  if (!customer) {
    return jsonResponse({ error: 'Customer not found' }, corsHeaders, 404);
  }
  
  return jsonResponse({ customer }, corsHeaders);
}

async function listCustomers(url, env, corsHeaders) {
  const limit = url.searchParams.get('limit') || 50;
  const offset = url.searchParams.get('offset') || 0;
  
  const customers = await env.DB.prepare(`
    SELECT * FROM customers ORDER BY created_at DESC LIMIT ? OFFSET ?
  `).bind(limit, offset).all();
  
  return jsonResponse({ customers: customers.results }, corsHeaders);
}

// REPAIR FUNCTIONS
async function createRepair(request, env, corsHeaders) {
  const data = await request.json();
  const repairId = generateId('REP');
  
  // Check if customer exists
  const customer = await env.DB.prepare('SELECT customer_id FROM customers WHERE customer_id = ?')
    .bind(data.customer_id).first();
  
  if (!customer) {
    return jsonResponse({ error: 'Customer not found' }, corsHeaders, 404);
  }
  
  // Insert repair
  await env.DB.prepare(`
    INSERT INTO repairs (
      repair_id, customer_id, device_type, brand, model, serial_number,
      issue_description, priority, estimated_cost, status
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'intake')
  `).bind(
    repairId,
    data.customer_id,
    data.device_type,
    data.brand || null,
    data.model || null,
    data.serial_number || null,
    data.issue_description,
    data.priority || 'normal',
    data.estimated_cost || 89.00
  ).run();
  
  // Log status change
  await env.DB.prepare(`
    INSERT INTO status_history (repair_id, new_status, changed_by, notes)
    VALUES (?, 'intake', 'system', 'Repair created')
  `).bind(repairId).run();
  
  // Queue welcome email
  await queueEmail(env, {
    repair_id: repairId,
    customer_id: data.customer_id,
    template: 'welcome',
    priority: 8
  });
  
  return jsonResponse({ 
    success: true, 
    repair_id: repairId,
    message: 'Repair created successfully' 
  }, corsHeaders);
}

async function getRepair(repairId, env, corsHeaders) {
  const repair = await env.DB.prepare(`
    SELECT r.*, c.name as customer_name, c.email as customer_email
    FROM repairs r
    JOIN customers c ON r.customer_id = c.customer_id
    WHERE r.repair_id = ?
  `).bind(repairId).first();
  
  if (!repair) {
    return jsonResponse({ error: 'Repair not found' }, corsHeaders, 404);
  }
  
  // Get status history
  const history = await env.DB.prepare(`
    SELECT * FROM status_history WHERE repair_id = ? ORDER BY timestamp DESC
  `).bind(repairId).all();
  
  return jsonResponse({ 
    repair,
    history: history.results 
  }, corsHeaders);
}

async function listRepairs(url, env, corsHeaders) {
  const status = url.searchParams.get('status');
  const limit = url.searchParams.get('limit') || 50;
  const offset = url.searchParams.get('offset') || 0;
  
  let query = `
    SELECT r.*, c.name as customer_name, c.email as customer_email
    FROM repairs r
    JOIN customers c ON r.customer_id = c.customer_id
  `;
  
  const params = [];
  if (status) {
    query += ' WHERE r.status = ?';
    params.push(status);
  }
  
  query += ' ORDER BY r.intake_date DESC LIMIT ? OFFSET ?';
  params.push(limit, offset);
  
  const repairs = await env.DB.prepare(query).bind(...params).all();
  
  return jsonResponse({ repairs: repairs.results }, corsHeaders);
}

async function updateRepair(repairId, request, env, corsHeaders) {
  const data = await request.json();
  
  // Get current repair
  const current = await env.DB.prepare('SELECT status FROM repairs WHERE repair_id = ?')
    .bind(repairId).first();
  
  if (!current) {
    return jsonResponse({ error: 'Repair not found' }, corsHeaders, 404);
  }
  
  // Build update query dynamically
  const updates = [];
  const values = [];
  
  const allowedFields = ['status', 'ai_diagnosis', 'ai_confidence', 'priority', 
    'estimated_cost', 'actual_cost', 'estimated_time', 'actual_time', 
    'parts_needed', 'parts_cost', 'diagnostic_notes', 'repair_notes',
    'customer_satisfaction', 'payment_status', 'payment_method'];
  
  for (const field of allowedFields) {
    if (data[field] !== undefined) {
      updates.push(`${field} = ?`);
      values.push(data[field]);
    }
  }
  
  // Handle date fields
  if (data.status === 'in_progress' && !current.start_date) {
    updates.push('start_date = CURRENT_TIMESTAMP');
  }
  if (data.status === 'completed' && !current.completion_date) {
    updates.push('completion_date = CURRENT_TIMESTAMP');
  }
  
  updates.push('updated_at = CURRENT_TIMESTAMP');
  values.push(repairId);
  
  await env.DB.prepare(`
    UPDATE repairs SET ${updates.join(', ')} WHERE repair_id = ?
  `).bind(...values).run();
  
  // Log status change if status changed
  if (data.status && data.status !== current.status) {
    await env.DB.prepare(`
      INSERT INTO status_history (repair_id, old_status, new_status, changed_by, notes)
      VALUES (?, ?, ?, ?, ?)
    `).bind(repairId, current.status, data.status, data.changed_by || 'system', data.notes || '').run();
    
    // Queue appropriate email based on status
    if (data.status === 'diagnosed') {
      await queueEmail(env, {
        repair_id: repairId,
        template: 'diagnosis_complete',
        priority: 9
      });
    } else if (data.status === 'completed') {
      await queueEmail(env, {
        repair_id: repairId,
        template: 'repair_complete',
        priority: 10
      });
    }
  }
  
  return jsonResponse({ 
    success: true,
    message: 'Repair updated successfully' 
  }, corsHeaders);
}

// AI DIAGNOSTIC FUNCTION
async function aiDiagnose(request, env, corsHeaders) {
  const { repair_id, issue_description, device_type, additional_info } = await request.json();
  
  // Build diagnostic prompt
  const prompt = `You are an expert CPU repair technician analyzing a customer issue.

Device Type: ${device_type}
Issue Description: ${issue_description}
${additional_info ? `Additional Info: ${additional_info}` : ''}

Provide a concise diagnostic analysis in JSON format with:
{
  "diagnosis": "Clear diagnosis of the issue",
  "likely_cause": "Most likely cause",
  "severity": "low|medium|high",
  "confidence": 0.0-1.0,
  "estimated_cost": number,
  "estimated_time": hours as number,
  "parts_needed": ["part1", "part2"],
  "repair_steps": ["step1", "step2"],
  "warnings": ["any warnings or concerns"]
}`;

  const startTime = Date.now();
  
  try {
    // Call Claude API
    const response = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'anthropic-version': '2023-06-01',
        'x-api-key': env.ANTHROPIC_API_KEY
      },
      body: JSON.stringify({
        model: 'claude-sonnet-4-20250514',
        max_tokens: 2000,
        messages: [{
          role: 'user',
          content: prompt
        }]
      })
    });
    
    const aiResponse = await response.json();
    const processingTime = Date.now() - startTime;
    
    // Parse AI response
    const content = aiResponse.content[0].text;
    let diagnosis;
    
    try {
      // Try to extract JSON from the response
      const jsonMatch = content.match(/\{[\s\S]*\}/);
      diagnosis = jsonMatch ? JSON.parse(jsonMatch[0]) : { diagnosis: content };
    } catch (e) {
      diagnosis = { diagnosis: content };
    }
    
    // Log diagnostic
    await env.DB.prepare(`
      INSERT INTO diagnostic_logs (repair_id, log_type, ai_model, prompt_used, response, confidence, processing_time)
      VALUES (?, 'diagnosis', 'claude-sonnet-4', ?, ?, ?, ?)
    `).bind(
      repair_id,
      prompt,
      content,
      diagnosis.confidence || 0.8,
      processingTime
    ).run();
    
    // Update repair with diagnosis
    await env.DB.prepare(`
      UPDATE repairs 
      SET ai_diagnosis = ?, ai_confidence = ?, status = 'diagnosed', updated_at = CURRENT_TIMESTAMP
      WHERE repair_id = ?
    `).bind(
      diagnosis.diagnosis,
      diagnosis.confidence || 0.8,
      repair_id
    ).run();
    
    return jsonResponse({
      success: true,
      diagnosis,
      processing_time: processingTime
    }, corsHeaders);
    
  } catch (error) {
    return jsonResponse({
      error: 'AI diagnosis failed',
      details: error.message
    }, corsHeaders, 500);
  }
}

// ANALYTICS FUNCTIONS
async function getTodayAnalytics(env, corsHeaders) {
  const today = new Date().toISOString().split('T')[0];
  
  const analytics = await env.DB.prepare(`
    SELECT * FROM analytics WHERE date = ?
  `).bind(today).first();
  
  // Get real-time stats
  const stats = await env.DB.prepare(`
    SELECT 
      COUNT(*) as total_repairs,
      SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) as completed_today,
      SUM(CASE WHEN status = 'completed' THEN actual_cost ELSE 0 END) as revenue_today,
      AVG(CASE WHEN status = 'completed' THEN actual_time ELSE NULL END) as avg_time
    FROM repairs
    WHERE DATE(intake_date) = ?
  `).bind(today).first();
  
  return jsonResponse({
    analytics: analytics || {},
    live_stats: stats
  }, corsHeaders);
}

async function getAnalyticsRange(url, env, corsHeaders) {
  const startDate = url.searchParams.get('start');
  const endDate = url.searchParams.get('end');
  
  const analytics = await env.DB.prepare(`
    SELECT * FROM analytics WHERE date BETWEEN ? AND ? ORDER BY date ASC
  `).bind(startDate, endDate).all();
  
  return jsonResponse({
    analytics: analytics.results
  }, corsHeaders);
}

// EMAIL FUNCTIONS
async function queueEmail(env, { repair_id, customer_id, template, priority }) {
  // Get repair and customer data
  const data = await env.DB.prepare(`
    SELECT r.*, c.name, c.email
    FROM repairs r
    JOIN customers c ON r.customer_id = c.customer_id
    WHERE r.repair_id = ?
  `).bind(repair_id || customer_id).first();
  
  if (!data) return;
  
  // Get template
  const tpl = await env.DB.prepare(`
    SELECT * FROM templates WHERE template_id = ?
  `).bind(template).first();
  
  if (!tpl) return;
  
  // Replace variables in template
  let subject = tpl.subject;
  let body = tpl.content;
  
  const vars = {
    customer_name: data.name,
    repair_id: repair_id || data.repair_id,
    device_type: data.device_type,
    diagnosis: data.ai_diagnosis,
    cost: data.estimated_cost || 89,
    time: data.estimated_time || 2,
    repair_notes: data.repair_notes,
    total_cost: data.actual_cost || data.estimated_cost,
    warranty_days: 30,
    payment_instructions: 'Payment accepted: Cash, Credit, E-Transfer',
    estimated_completion: new Date(Date.now() + 48*3600000).toLocaleDateString()
  };
  
  for (const [key, value] of Object.entries(vars)) {
    subject = subject.replace(new RegExp(`{{${key}}}`, 'g'), value);
    body = body.replace(new RegExp(`{{${key}}}`, 'g'), value);
  }
  
  // Queue email
  await env.DB.prepare(`
    INSERT INTO email_queue (repair_id, customer_id, email_to, email_subject, email_body, email_type, priority)
    VALUES (?, ?, ?, ?, ?, ?, ?)
  `).bind(
    repair_id,
    customer_id || data.customer_id,
    data.email,
    subject,
    body,
    template,
    priority || 5
  ).run();
}

async function sendEmail(request, env, corsHeaders) {
  const { to, subject, body, repair_id } = await request.json();
  
  // Here you would integrate with your email service (SendGrid, Mailgun, etc.)
  // For now, just queue it
  await env.DB.prepare(`
    INSERT INTO email_queue (email_to, email_subject, email_body, repair_id, priority, status)
    VALUES (?, ?, ?, ?, 10, 'queued')
  `).bind(to, subject, body, repair_id || null).run();
  
  return jsonResponse({
    success: true,
    message: 'Email queued for sending'
  }, corsHeaders);
}

async function getEmailQueue(env, corsHeaders) {
  const queue = await env.DB.prepare(`
    SELECT * FROM email_queue WHERE status = 'queued' ORDER BY priority DESC, created_at ASC LIMIT 50
  `).all();
  
  return jsonResponse({
    queue: queue.results
  }, corsHeaders);
}

// VOICE COMMAND PROCESSING
async function processVoiceCommand(request, env, corsHeaders) {
  const { command, context } = await request.json();
  
  // Log voice command
  const startTime = Date.now();
  
  // Simple intent recognition (could be enhanced with AI)
  let intent = 'unknown';
  let response = 'Command not recognized';
  let params = {};
  
  const lowerCommand = command.toLowerCase();
  
  // Status check
  if (lowerCommand.includes('status') || lowerCommand.includes('how many')) {
    intent = 'check_status';
    const stats = await env.DB.prepare(`
      SELECT 
        COUNT(*) as total,
        SUM(CASE WHEN status = 'intake' THEN 1 ELSE 0 END) as intake,
        SUM(CASE WHEN status = 'in_progress' THEN 1 ELSE 0 END) as in_progress,
        SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) as completed_today
      FROM repairs
      WHERE DATE(intake_date) = DATE('now')
    `).first();
    
    response = `Today: ${stats.completed_today} completed, ${stats.in_progress} in progress, ${stats.intake} in intake. Total: ${stats.total} repairs.`;
  }
  
  // Start next repair
  else if (lowerCommand.includes('next repair') || lowerCommand.includes('start next')) {
    intent = 'start_next';
    const nextRepair = await env.DB.prepare(`
      SELECT repair_id, device_type, customer_id FROM repairs WHERE status = 'intake' ORDER BY priority DESC, intake_date ASC LIMIT 1
    `).first();
    
    if (nextRepair) {
      await env.DB.prepare(`
        UPDATE repairs SET status = 'in_progress', start_date = CURRENT_TIMESTAMP WHERE repair_id = ?
      `).bind(nextRepair.repair_id).run();
      
      response = `Starting repair ${nextRepair.repair_id} - ${nextRepair.device_type}`;
      params = { repair_id: nextRepair.repair_id };
    } else {
      response = 'No repairs in queue';
    }
  }
  
  // Complete repair
  else if (lowerCommand.includes('complete') || lowerCommand.includes('finished')) {
    intent = 'complete_repair';
    const repairId = context?.repair_id;
    
    if (repairId) {
      await env.DB.prepare(`
        UPDATE repairs SET status = 'completed', completion_date = CURRENT_TIMESTAMP WHERE repair_id = ?
      `).bind(repairId).run();
      
      await queueEmail(env, {
        repair_id: repairId,
        template: 'repair_complete',
        priority: 10
      });
      
      response = `Repair ${repairId} marked complete. Customer notified.`;
    } else {
      response = 'No active repair specified';
    }
  }
  
  // Revenue check
  else if (lowerCommand.includes('revenue') || lowerCommand.includes('money')) {
    intent = 'check_revenue';
    const revenue = await env.DB.prepare(`
      SELECT SUM(actual_cost) as total FROM repairs WHERE status = 'completed' AND DATE(completion_date) = DATE('now')
    `).first();
    
    response = `Today's revenue: $${revenue.total || 0}`;
  }
  
  const processingTime = Date.now() - startTime;
  
  // Log command
  await env.DB.prepare(`
    INSERT INTO voice_commands (command, intent, parameters, response, execution_status, execution_time)
    VALUES (?, ?, ?, ?, 'success', ?)
  `).bind(command, intent, JSON.stringify(params), response, processingTime).run();
  
  return jsonResponse({
    intent,
    response,
    params,
    processing_time: processingTime
  }, corsHeaders);
}

// DASHBOARD DATA
async function getDashboardData(env, corsHeaders) {
  const today = new Date().toISOString().split('T')[0];
  
  // Today's stats
  const todayStats = await env.DB.prepare(`
    SELECT 
      COUNT(*) as total_repairs,
      SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) as completed,
      SUM(CASE WHEN status = 'in_progress' THEN 1 ELSE 0 END) as in_progress,
      SUM(CASE WHEN status = 'intake' THEN 1 ELSE 0 END) as pending,
      SUM(CASE WHEN status = 'completed' THEN actual_cost ELSE 0 END) as revenue
    FROM repairs
    WHERE DATE(intake_date) = ?
  `).bind(today).first();
  
  // Goal progress (12 repairs/day)
  const goalProgress = (todayStats.completed / 12) * 100;
  
  // Recent repairs
  const recentRepairs = await env.DB.prepare(`
    SELECT r.*, c.name as customer_name
    FROM repairs r
    JOIN customers c ON r.customer_id = c.customer_id
    ORDER BY r.updated_at DESC
    LIMIT 10
  `).all();
  
  // Week stats
  const weekStats = await env.DB.prepare(`
    SELECT 
      COUNT(*) as total,
      SUM(CASE WHEN status = 'completed' THEN actual_cost ELSE 0 END) as revenue
    FROM repairs
    WHERE intake_date >= DATE('now', '-7 days')
  `).first();
  
  return jsonResponse({
    today: {
      ...todayStats,
      goal_progress: goalProgress,
      goal: 12,
      revenue_goal: 89 * 12
    },
    week: weekStats,
    recent_repairs: recentRepairs.results
  }, corsHeaders);
}

// UTILITY FUNCTIONS
function generateId(prefix) {
  return `${prefix}-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`.toUpperCase();
}

function jsonResponse(data, headers = {}, status = 200) {
  return new Response(JSON.stringify(data, null, 2), {
    status,
    headers: {
      'Content-Type': 'application/json',
      ...headers
    }
  });
}
