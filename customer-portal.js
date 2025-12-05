// NOIZYLAB CUSTOMER PORTAL WORKER
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    
    if (url.pathname === '/') {
      return new Response(getCustomerPortalHTML(), {
        headers: { 'Content-Type': 'text/html' }
      });
    }
    
    if (url.pathname.startsWith('/track/')) {
      const repairId = url.pathname.split('/')[2];
      return new Response(getTrackingHTML(repairId), {
        headers: { 'Content-Type': 'text/html' }
      });
    }
    
    return new Response('Not Found', { status: 404 });
  }
};

function getCustomerPortalHTML() {
  return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NOIZYLAB CPU Repair - Submit Your Device</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }
        
        .header {
            text-align: center;
            margin-bottom: 40px;
        }
        
        .logo {
            font-size: 48px;
            font-weight: 900;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }
        
        .tagline {
            color: #666;
            font-size: 18px;
        }
        
        .form-group {
            margin-bottom: 25px;
        }
        
        label {
            display: block;
            font-weight: 600;
            margin-bottom: 8px;
            color: #333;
        }
        
        input, textarea, select {
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 16px;
            transition: border-color 0.3s;
        }
        
        input:focus, textarea:focus, select:focus {
            outline: none;
            border-color: #667eea;
        }
        
        textarea {
            min-height: 120px;
            resize: vertical;
        }
        
        .btn {
            width: 100%;
            padding: 16px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 18px;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s;
        }
        
        .btn:hover {
            transform: translateY(-2px);
        }
        
        .btn:active {
            transform: translateY(0);
        }
        
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-top: 40px;
            padding-top: 40px;
            border-top: 2px solid #f0f0f0;
        }
        
        .feature {
            text-align: center;
        }
        
        .feature-icon {
            font-size: 32px;
            margin-bottom: 10px;
        }
        
        .feature-text {
            color: #666;
            font-size: 14px;
        }
        
        .success {
            background: #4caf50;
            color: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            text-align: center;
        }
        
        .error {
            background: #f44336;
            color: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="logo">NOIZYLAB</div>
            <div class="tagline">Professional CPU Repair Service</div>
        </div>
        
        <div id="message"></div>
        
        <form id="repairForm">
            <div class="form-group">
                <label for="name">Your Name *</label>
                <input type="text" id="name" required>
            </div>
            
            <div class="form-group">
                <label for="email">Email Address *</label>
                <input type="email" id="email" required>
            </div>
            
            <div class="form-group">
                <label for="phone">Phone Number</label>
                <input type="tel" id="phone">
            </div>
            
            <div class="form-group">
                <label for="device_type">Device Type *</label>
                <select id="device_type" required>
                    <option value="">Select device type...</option>
                    <option value="Desktop PC">Desktop PC</option>
                    <option value="Laptop">Laptop</option>
                    <option value="Gaming PC">Gaming PC</option>
                    <option value="Workstation">Workstation</option>
                    <option value="Server">Server</option>
                    <option value="Other">Other</option>
                </select>
            </div>
            
            <div class="form-group">
                <label for="brand">Brand</label>
                <input type="text" id="brand" placeholder="Dell, HP, Custom Build, etc.">
            </div>
            
            <div class="form-group">
                <label for="model">Model</label>
                <input type="text" id="model">
            </div>
            
            <div class="form-group">
                <label for="issue">Describe the Problem *</label>
                <textarea id="issue" required placeholder="Please describe what's happening with your device..."></textarea>
            </div>
            
            <button type="submit" class="btn">Submit Repair Request</button>
        </form>
        
        <div class="features">
            <div class="feature">
                <div class="feature-icon">⚡</div>
                <div class="feature-text">Fast turnaround - most repairs in 24-48 hours</div>
            </div>
            <div class="feature">
                <div class="feature-icon">🔒</div>
                <div class="feature-text">Your data is safe - secure handling guaranteed</div>
            </div>
            <div class="feature">
                <div class="feature-icon">💰</div>
                <div class="feature-text">Fair pricing - $89 standard diagnostic</div>
            </div>
        </div>
    </div>
    
    <script>
        const API_URL = 'https://noizylab-api.fishmusicinc.workers.dev';
        
        document.getElementById('repairForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const messageDiv = document.getElementById('message');
            messageDiv.innerHTML = '';
            
            const formData = {
                name: document.getElementById('name').value,
                email: document.getElementById('email').value,
                phone: document.getElementById('phone').value,
                device_type: document.getElementById('device_type').value,
                brand: document.getElementById('brand').value,
                model: document.getElementById('model').value,
                issue_description: document.getElementById('issue').value
            };
            
            try {
                // Create customer
                const customerResponse = await fetch(API_URL + '/api/customers', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        email: formData.email,
                        name: formData.name,
                        phone: formData.phone
                    })
                });
                
                const customerData = await customerResponse.json();
                
                // Create repair
                const repairResponse = await fetch(API_URL + '/api/repairs', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        customer_id: customerData.customer_id,
                        device_type: formData.device_type,
                        brand: formData.brand,
                        model: formData.model,
                        issue_description: formData.issue_description
                    })
                });
                
                const repairData = await repairResponse.json();
                
                if (repairData.success) {
                    messageDiv.innerHTML = \`
                        <div class="success">
                            <h3>Repair Request Submitted!</h3>
                            <p>Your repair ID is: <strong>\${repairData.repair_id}</strong></p>
                            <p>Check your email for tracking information.</p>
                            <p><a href="/track/\${repairData.repair_id}" style="color: white; text-decoration: underline;">Track your repair here</a></p>
                        </div>
                    \`;
                    document.getElementById('repairForm').reset();
                } else {
                    throw new Error(repairData.error || 'Submission failed');
                }
                
            } catch (error) {
                messageDiv.innerHTML = \`
                    <div class="error">
                        <p>Error: \${error.message}</p>
                        <p>Please try again or contact us directly.</p>
                    </div>
                \`;
            }
        });
    </script>
</body>
</html>`;
}

function getTrackingHTML(repairId) {
  return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Track Repair - NOIZYLAB</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 900px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }
        
        .header {
            text-align: center;
            margin-bottom: 40px;
        }
        
        .logo {
            font-size: 36px;
            font-weight: 900;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .repair-id {
            font-size: 24px;
            color: #333;
            margin: 20px 0;
        }
        
        .status-badge {
            display: inline-block;
            padding: 8px 16px;
            border-radius: 20px;
            font-weight: 600;
            margin: 10px 0;
        }
        
        .status-intake { background: #ffc107; color: #000; }
        .status-diagnosed { background: #2196f3; color: white; }
        .status-in_progress { background: #ff9800; color: white; }
        .status-completed { background: #4caf50; color: white; }
        
        .info-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }
        
        .info-box {
            padding: 20px;
            background: #f5f5f5;
            border-radius: 12px;
        }
        
        .info-label {
            font-size: 12px;
            color: #666;
            text-transform: uppercase;
            margin-bottom: 5px;
        }
        
        .info-value {
            font-size: 18px;
            font-weight: 600;
            color: #333;
        }
        
        .timeline {
            margin: 40px 0;
        }
        
        .timeline-item {
            padding: 20px;
            border-left: 3px solid #667eea;
            margin-left: 20px;
            margin-bottom: 20px;
            position: relative;
        }
        
        .timeline-item::before {
            content: '';
            position: absolute;
            left: -8px;
            top: 25px;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: #667eea;
        }
        
        .timeline-status {
            font-weight: 600;
            color: #667eea;
            margin-bottom: 5px;
        }
        
        .timeline-date {
            font-size: 14px;
            color: #999;
        }
        
        .loading {
            text-align: center;
            padding: 40px;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="logo">NOIZYLAB</div>
            <div class="repair-id">Tracking: ${repairId}</div>
        </div>
        
        <div id="content" class="loading">
            <p>Loading repair information...</p>
        </div>
    </div>
    
    <script>
        const API_URL = 'https://noizylab-api.fishmusicinc.workers.dev';
        const REPAIR_ID = '${repairId}';
        
        async function loadRepairInfo() {
            try {
                const response = await fetch(API_URL + '/api/repairs/' + REPAIR_ID);
                const data = await response.json();
                
                if (data.error) {
                    document.getElementById('content').innerHTML = \`
                        <div style="text-align: center; color: #f44336;">
                            <h3>Repair Not Found</h3>
                            <p>The repair ID "\${REPAIR_ID}" could not be found.</p>
                        </div>
                    \`;
                    return;
                }
                
                const { repair, history } = data;
                
                const statusClass = 'status-' + repair.status.replace(' ', '_');
                
                let html = \`
                    <div style="text-align: center;">
                        <span class="status-badge \${statusClass}">\${repair.status.toUpperCase()}</span>
                    </div>
                    
                    <div class="info-grid">
                        <div class="info-box">
                            <div class="info-label">Customer</div>
                            <div class="info-value">\${repair.customer_name}</div>
                        </div>
                        <div class="info-box">
                            <div class="info-label">Device</div>
                            <div class="info-value">\${repair.device_type}</div>
                        </div>
                        <div class="info-box">
                            <div class="info-label">Estimated Cost</div>
                            <div class="info-value">$\${repair.estimated_cost}</div>
                        </div>
                        <div class="info-box">
                            <div class="info-label">Intake Date</div>
                            <div class="info-value">\${new Date(repair.intake_date).toLocaleDateString()}</div>
                        </div>
                    </div>
                    
                    <div style="padding: 20px; background: #f9f9f9; border-radius: 12px; margin: 20px 0;">
                        <div class="info-label">Issue Description</div>
                        <p style="margin-top: 10px; color: #333;">\${repair.issue_description}</p>
                    </div>
                \`;
                
                if (repair.ai_diagnosis) {
                    html += \`
                        <div style="padding: 20px; background: #e3f2fd; border-radius: 12px; margin: 20px 0;">
                            <div class="info-label">Diagnosis</div>
                            <p style="margin-top: 10px; color: #333;">\${repair.ai_diagnosis}</p>
                        </div>
                    \`;
                }
                
                if (history && history.length > 0) {
                    html += '<div class="timeline"><h3 style="margin-bottom: 20px;">Status History</h3>';
                    history.forEach(item => {
                        html += \`
                            <div class="timeline-item">
                                <div class="timeline-status">\${item.new_status.toUpperCase()}</div>
                                <div class="timeline-date">\${new Date(item.timestamp).toLocaleString()}</div>
                                \${item.notes ? '<p style="margin-top: 10px; color: #666;">' + item.notes + '</p>' : ''}
                            </div>
                        \`;
                    });
                    html += '</div>';
                }
                
                document.getElementById('content').innerHTML = html;
                
            } catch (error) {
                document.getElementById('content').innerHTML = \`
                    <div style="text-align: center; color: #f44336;">
                        <h3>Error Loading Repair</h3>
                        <p>\${error.message}</p>
                    </div>
                \`;
            }
        }
        
        loadRepairInfo();
        // Refresh every 30 seconds
        setInterval(loadRepairInfo, 30000);
    </script>
</body>
</html>`;
}
