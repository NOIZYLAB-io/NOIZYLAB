// NOIZYLAB ANALYTICS DASHBOARD WORKER
// Advanced analytics, charts, and business intelligence

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    
    if (url.pathname === '/') {
      return new Response(getAnalyticsDashboardHTML(), {
        headers: { 'Content-Type': 'text/html' }
      });
    }
    
    if (url.pathname === '/api/analytics/summary') {
      return await getAnalyticsSummary(env);
    }
    
    if (url.pathname === '/api/analytics/trends') {
      return await getTrends(env, url);
    }
    
    if (url.pathname === '/api/analytics/customers') {
      return await getCustomerAnalytics(env);
    }
    
    return new Response('Not Found', { status: 404 });
  }
};

async function getAnalyticsSummary(env) {
  // Last 30 days summary
  const summary = await env.DB.prepare(`
    SELECT 
      COUNT(*) as total_repairs,
      SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) as completed_repairs,
      SUM(CASE WHEN status = 'completed' THEN actual_cost ELSE 0 END) as total_revenue,
      AVG(CASE WHEN status = 'completed' THEN actual_time ELSE NULL END) as avg_repair_time,
      AVG(CASE WHEN status = 'completed' AND customer_satisfaction IS NOT NULL THEN customer_satisfaction ELSE NULL END) as avg_satisfaction,
      COUNT(DISTINCT customer_id) as unique_customers,
      SUM(parts_cost) as total_parts_cost
    FROM repairs
    WHERE intake_date >= DATE('now', '-30 days')
  `).first();
  
  // Calculate metrics
  const completionRate = summary.total_repairs > 0 
    ? (summary.completed_repairs / summary.total_repairs * 100).toFixed(1)
    : 0;
  
  const avgRevenue = summary.completed_repairs > 0
    ? (summary.total_revenue / summary.completed_repairs).toFixed(2)
    : 0;
  
  const profit = summary.total_revenue - summary.total_parts_cost;
  const profitMargin = summary.total_revenue > 0
    ? (profit / summary.total_revenue * 100).toFixed(1)
    : 0;
  
  return Response.json({
    period: 'Last 30 Days',
    summary: {
      ...summary,
      completion_rate: completionRate,
      avg_revenue_per_repair: avgRevenue,
      profit: profit,
      profit_margin: profitMargin
    }
  });
}

async function getTrends(env, url) {
  const days = parseInt(url.searchParams.get('days') || '30');
  
  const trends = await env.DB.prepare(`
    SELECT 
      DATE(intake_date) as date,
      COUNT(*) as repairs,
      SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) as completed,
      SUM(CASE WHEN status = 'completed' THEN actual_cost ELSE 0 END) as revenue,
      AVG(CASE WHEN status = 'completed' THEN actual_time ELSE NULL END) as avg_time
    FROM repairs
    WHERE intake_date >= DATE('now', '-' || ? || ' days')
    GROUP BY DATE(intake_date)
    ORDER BY date ASC
  `).bind(days).all();
  
  return Response.json({
    period: `Last ${days} Days`,
    trends: trends.results
  });
}

async function getCustomerAnalytics(env) {
  // Top customers by revenue
  const topCustomers = await env.DB.prepare(`
    SELECT 
      c.customer_id,
      c.name,
      c.email,
      COUNT(r.id) as repair_count,
      SUM(r.actual_cost) as total_spent,
      AVG(r.customer_satisfaction) as avg_satisfaction,
      MAX(r.intake_date) as last_repair
    FROM customers c
    JOIN repairs r ON c.customer_id = r.customer_id
    WHERE r.status = 'completed'
    GROUP BY c.customer_id
    ORDER BY total_spent DESC
    LIMIT 20
  `).all();
  
  // Customer retention
  const retention = await env.DB.prepare(`
    SELECT 
      SUM(CASE WHEN repair_count = 1 THEN 1 ELSE 0 END) as one_time,
      SUM(CASE WHEN repair_count > 1 THEN 1 ELSE 0 END) as repeat,
      COUNT(*) as total
    FROM (
      SELECT customer_id, COUNT(*) as repair_count
      FROM repairs
      WHERE status = 'completed'
      GROUP BY customer_id
    )
  `).first();
  
  const repeatRate = retention.total > 0
    ? (retention.repeat / retention.total * 100).toFixed(1)
    : 0;
  
  return Response.json({
    top_customers: topCustomers.results,
    retention: {
      ...retention,
      repeat_rate: repeatRate
    }
  });
}

function getAnalyticsDashboardHTML() {
  return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NOIZYLAB Analytics Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #0a0e27;
            color: #ffffff;
            padding: 20px;
        }
        
        .header {
            text-align: center;
            padding: 40px 0;
        }
        
        .logo {
            font-size: 48px;
            font-weight: 900;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .metrics-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            max-width: 1400px;
            margin: 0 auto 40px;
        }
        
        .metric-card {
            background: #1a1f3a;
            padding: 30px;
            border-radius: 16px;
            text-align: center;
        }
        
        .metric-value {
            font-size: 48px;
            font-weight: 900;
            margin: 10px 0;
        }
        
        .metric-label {
            font-size: 14px;
            color: #888;
            text-transform: uppercase;
        }
        
        .chart-container {
            background: #1a1f3a;
            padding: 30px;
            border-radius: 16px;
            max-width: 1400px;
            margin: 0 auto 40px;
        }
        
        .chart-title {
            font-size: 24px;
            font-weight: 700;
            margin-bottom: 20px;
        }
        
        canvas {
            max-height: 400px;
        }
        
        .customer-table {
            background: #1a1f3a;
            padding: 30px;
            border-radius: 16px;
            max-width: 1400px;
            margin: 0 auto;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
        }
        
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #2a3050;
        }
        
        th {
            color: #888;
            font-size: 12px;
            text-transform: uppercase;
        }
        
        .loading {
            text-align: center;
            padding: 40px;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo">NOIZYLAB</div>
        <h2>Business Analytics Dashboard</h2>
    </div>
    
    <div class="metrics-grid" id="metricsGrid">
        <div class="metric-card">
            <div class="metric-label">Total Revenue</div>
            <div class="metric-value" id="totalRevenue">$0</div>
        </div>
        <div class="metric-card">
            <div class="metric-label">Completed Repairs</div>
            <div class="metric-value" id="completedRepairs">0</div>
        </div>
        <div class="metric-card">
            <div class="metric-label">Avg Repair Time</div>
            <div class="metric-value" id="avgRepairTime">0h</div>
        </div>
        <div class="metric-card">
            <div class="metric-label">Customer Satisfaction</div>
            <div class="metric-value" id="avgSatisfaction">0.0</div>
        </div>
        <div class="metric-card">
            <div class="metric-label">Profit Margin</div>
            <div class="metric-value" id="profitMargin">0%</div>
        </div>
        <div class="metric-card">
            <div class="metric-label">Unique Customers</div>
            <div class="metric-value" id="uniqueCustomers">0</div>
        </div>
    </div>
    
    <div class="chart-container">
        <div class="chart-title">30-Day Revenue Trend</div>
        <canvas id="revenueChart"></canvas>
    </div>
    
    <div class="chart-container">
        <div class="chart-title">Repair Volume Trend</div>
        <canvas id="volumeChart"></canvas>
    </div>
    
    <div class="customer-table">
        <div class="chart-title">Top Customers</div>
        <table id="customersTable">
            <thead>
                <tr>
                    <th>Customer</th>
                    <th>Email</th>
                    <th>Repairs</th>
                    <th>Total Spent</th>
                    <th>Satisfaction</th>
                    <th>Last Repair</th>
                </tr>
            </thead>
            <tbody id="customersBody">
                <tr><td colspan="6" class="loading">Loading...</td></tr>
            </tbody>
        </table>
    </div>
    
    <script>
        const API_URL = window.location.origin;
        
        async function loadAnalytics() {
            // Load summary
            const summary = await fetch(API_URL + '/api/analytics/summary').then(r => r.json());
            
            document.getElementById('totalRevenue').textContent = '$' + summary.summary.total_revenue.toFixed(0);
            document.getElementById('completedRepairs').textContent = summary.summary.completed_repairs;
            document.getElementById('avgRepairTime').textContent = (summary.summary.avg_repair_time || 0).toFixed(1) + 'h';
            document.getElementById('avgSatisfaction').textContent = (summary.summary.avg_satisfaction || 0).toFixed(1) + '/5';
            document.getElementById('profitMargin').textContent = summary.summary.profit_margin + '%';
            document.getElementById('uniqueCustomers').textContent = summary.summary.unique_customers;
            
            // Load trends
            const trends = await fetch(API_URL + '/api/analytics/trends?days=30').then(r => r.json());
            
            // Revenue chart
            new Chart(document.getElementById('revenueChart'), {
                type: 'line',
                data: {
                    labels: trends.trends.map(t => t.date),
                    datasets: [{
                        label: 'Daily Revenue',
                        data: trends.trends.map(t => t.revenue),
                        borderColor: '#667eea',
                        backgroundColor: 'rgba(102, 126, 234, 0.1)',
                        tension: 0.4,
                        fill: true
                    }]
                },
                options: {
                    responsive: true,
                    plugins: { legend: { display: false } },
                    scales: {
                        y: { beginAtZero: true, ticks: { color: '#888' } },
                        x: { ticks: { color: '#888' } }
                    }
                }
            });
            
            // Volume chart
            new Chart(document.getElementById('volumeChart'), {
                type: 'bar',
                data: {
                    labels: trends.trends.map(t => t.date),
                    datasets: [{
                        label: 'Repairs Completed',
                        data: trends.trends.map(t => t.completed),
                        backgroundColor: '#4caf50'
                    }]
                },
                options: {
                    responsive: true,
                    plugins: { legend: { display: false } },
                    scales: {
                        y: { beginAtZero: true, ticks: { color: '#888' } },
                        x: { ticks: { color: '#888' } }
                    }
                }
            });
            
            // Load customers
            const customers = await fetch(API_URL + '/api/analytics/customers').then(r => r.json());
            
            const tbody = document.getElementById('customersBody');
            tbody.innerHTML = customers.top_customers.map(c => \`
                <tr>
                    <td>\${c.name}</td>
                    <td>\${c.email}</td>
                    <td>\${c.repair_count}</td>
                    <td>$\${c.total_spent.toFixed(0)}</td>
                    <td>\${(c.avg_satisfaction || 0).toFixed(1)}/5</td>
                    <td>\${new Date(c.last_repair).toLocaleDateString()}</td>
                </tr>
            \`).join('');
        }
        
        loadAnalytics();
        setInterval(loadAnalytics, 60000); // Refresh every minute
    </script>
</body>
</html>`;
}

// WRANGLER.TOML CONFIGURATION:
/*
name = "noizylab-analytics"
main = "analytics-worker.js"
compatibility_date = "2024-11-01"
account_id = "your-account-id"

[[d1_databases]]
binding = "DB"
database_name = "noizylab-repairs"
database_id = "your-database-id"
*/
