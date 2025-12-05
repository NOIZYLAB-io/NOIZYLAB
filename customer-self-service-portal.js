/**
 * CUSTOMER SELF-SERVICE PORTAL
 * One portal for all customer interactions across all domains
 * 
 * Features:
 * - Track repair status (NOIZYLAB)
 * - Monitor music projects (FishMusicInc)
 * - View API usage (NOIZY.AI)
 * - Update contact info
 * - View invoices & receipts
 * - File uploads
 * - Direct messaging
 * - Notification preferences
 * - Password-protected access
 */

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname;

    const corsHeaders = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, PUT, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    };

    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders });
    }

    try {
      // Authentication
      if (path === '/login' && request.method === 'POST') {
        return await handleLogin(request, env, corsHeaders);
      } else if (path === '/register' && request.method === 'POST') {
        return await handleRegister(request, env, corsHeaders);
      }
      
      // Main portal
      if (path === '/' || path === '/portal') {
        return handlePortalPage();
      }
      
      // Customer data
      else if (path === '/api/customer/profile') {
        return await handleGetProfile(request, env, corsHeaders);
      } else if (path === '/api/customer/profile' && request.method === 'PUT') {
        return await handleUpdateProfile(request, env, corsHeaders);
      }
      
      // Repairs (NOIZYLAB)
      else if (path === '/api/repairs') {
        return await handleGetRepairs(request, env, corsHeaders);
      } else if (path.startsWith('/api/repair/')) {
        return await handleGetRepair(request, env, corsHeaders);
      }
      
      // Projects (FishMusicInc)
      else if (path === '/api/projects') {
        return await handleGetProjects(request, env, corsHeaders);
      } else if (path.startsWith('/api/project/')) {
        return await handleGetProject(request, env, corsHeaders);
      }
      
      // API Usage (NOIZY.AI)
      else if (path === '/api/usage') {
        return await handleGetUsage(request, env, corsHeaders);
      }
      
      // Invoices
      else if (path === '/api/invoices') {
        return await handleGetInvoices(request, env, corsHeaders);
      }
      
      // Messages
      else if (path === '/api/messages') {
        return await handleGetMessages(request, env, corsHeaders);
      } else if (path === '/api/message' && request.method === 'POST') {
        return await handleSendMessage(request, env, corsHeaders);
      }
      
      // File uploads
      else if (path === '/api/upload' && request.method === 'POST') {
        return await handleFileUpload(request, env, corsHeaders);
      }
      
      // Notifications
      else if (path === '/api/notifications') {
        return await handleGetNotifications(request, env, corsHeaders);
      } else if (path === '/api/notifications/preferences' && request.method === 'PUT') {
        return await handleUpdateNotificationPrefs(request, env, corsHeaders);
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

function handlePortalPage() {
  const html = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customer Portal - Your Dashboard</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        
        .portal-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        
        .header {
            background: white;
            border-radius: 15px;
            padding: 2rem;
            margin-bottom: 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        }
        
        .header h1 {
            color: #667eea;
            font-size: 2rem;
        }
        
        .user-info {
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        
        .avatar {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1.5rem;
            font-weight: bold;
        }
        
        .tabs {
            display: flex;
            gap: 1rem;
            margin-bottom: 2rem;
            flex-wrap: wrap;
        }
        
        .tab {
            background: white;
            padding: 1rem 2rem;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        .tab:hover, .tab.active {
            background: #667eea;
            color: white;
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(102,126,234,0.3);
        }
        
        .content-area {
            background: white;
            border-radius: 15px;
            padding: 2rem;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
            min-height: 400px;
        }
        
        .tab-content {
            display: none;
        }
        
        .tab-content.active {
            display: block;
        }
        
        .item-card {
            background: #f8f9fa;
            border-radius: 10px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            border-left: 4px solid #667eea;
        }
        
        .item-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
        }
        
        .item-title {
            font-size: 1.2rem;
            font-weight: bold;
            color: #333;
        }
        
        .status-badge {
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: bold;
        }
        
        .status-received { background: #e3f2fd; color: #1976d2; }
        .status-in-progress { background: #fff3e0; color: #f57c00; }
        .status-completed { background: #e8f5e9; color: #388e3c; }
        
        .item-details {
            color: #666;
            line-height: 1.6;
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-bottom: 2rem;
        }
        
        .stat-box {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 10px;
            text-align: center;
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }
        
        .stat-label {
            font-size: 0.9rem;
            opacity: 0.9;
        }
        
        button {
            padding: 1rem 2rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s;
            font-weight: bold;
        }
        
        button:hover {
            transform: scale(1.05);
            box-shadow: 0 5px 20px rgba(102,126,234,0.4);
        }
        
        .message-box {
            background: #f8f9fa;
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            border-left: 4px solid #667eea;
        }
        
        .message-header {
            display: flex;
            justify-content: space-between;
            margin-bottom: 0.5rem;
        }
        
        .message-from {
            font-weight: bold;
            color: #667eea;
        }
        
        .message-time {
            color: #999;
            font-size: 0.9rem;
        }
        
        textarea {
            width: 100%;
            padding: 1rem;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            font-family: inherit;
            resize: vertical;
            min-height: 100px;
        }
        
        input[type="file"] {
            display: none;
        }
        
        .file-upload-btn {
            display: inline-block;
            padding: 1rem 2rem;
            background: white;
            color: #667eea;
            border: 2px solid #667eea;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s;
            font-weight: bold;
        }
        
        .file-upload-btn:hover {
            background: #667eea;
            color: white;
        }
        
        @media (max-width: 768px) {
            .header {
                flex-direction: column;
                text-align: center;
                gap: 1rem;
            }
            
            .tabs {
                flex-direction: column;
            }
            
            .tab {
                text-align: center;
            }
        }
    </style>
</head>
<body>
    <div class="portal-container">
        <!-- Header -->
        <div class="header">
            <div>
                <h1>Welcome Back! 👋</h1>
                <p id="customerName">Loading...</p>
            </div>
            <div class="user-info">
                <div class="avatar" id="avatar">R</div>
                <div>
                    <div id="userName">Rob Pickering</div>
                    <button onclick="logout()" style="padding: 0.5rem 1rem; font-size: 0.9rem;">Logout</button>
                </div>
            </div>
        </div>
        
        <!-- Quick Stats -->
        <div class="stats-grid">
            <div class="stat-box">
                <div class="stat-value" id="activeRepairs">0</div>
                <div class="stat-label">Active Repairs</div>
            </div>
            <div class="stat-box">
                <div class="stat-value" id="activeProjects">0</div>
                <div class="stat-label">Active Projects</div>
            </div>
            <div class="stat-box">
                <div class="stat-value" id="apiUsage">0</div>
                <div class="stat-label">API Requests</div>
            </div>
            <div class="stat-box">
                <div class="stat-value" id="unreadMessages">0</div>
                <div class="stat-label">Unread Messages</div>
            </div>
        </div>
        
        <!-- Tabs -->
        <div class="tabs">
            <div class="tab active" onclick="switchTab('repairs')">🔧 My Repairs</div>
            <div class="tab" onclick="switchTab('projects')">🎵 My Projects</div>
            <div class="tab" onclick="switchTab('api')">🤖 API Usage</div>
            <div class="tab" onclick="switchTab('messages')">💬 Messages</div>
            <div class="tab" onclick="switchTab('profile')">👤 Profile</div>
        </div>
        
        <!-- Content Area -->
        <div class="content-area">
            <!-- Repairs Tab -->
            <div class="tab-content active" id="repairs-content">
                <h2>My Computer Repairs</h2>
                <div id="repairsList">Loading repairs...</div>
            </div>
            
            <!-- Projects Tab -->
            <div class="tab-content" id="projects-content">
                <h2>My Music Projects</h2>
                <div id="projectsList">Loading projects...</div>
            </div>
            
            <!-- API Tab -->
            <div class="tab-content" id="api-content">
                <h2>API Usage & Analytics</h2>
                <div id="apiStats">Loading API stats...</div>
            </div>
            
            <!-- Messages Tab -->
            <div class="tab-content" id="messages-content">
                <h2>Messages</h2>
                <div id="messagesList" style="margin-bottom: 2rem;">Loading messages...</div>
                <h3>Send a Message</h3>
                <textarea id="newMessage" placeholder="Type your message here..."></textarea>
                <button onclick="sendMessage()" style="margin-top: 1rem;">Send Message</button>
            </div>
            
            <!-- Profile Tab -->
            <div class="tab-content" id="profile-content">
                <h2>My Profile</h2>
                <div id="profileInfo">Loading profile...</div>
            </div>
        </div>
    </div>
    
    <script>
        // Switch tabs
        function switchTab(tabName) {
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            event.target.classList.add('active');
            
            document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
            document.getElementById(tabName + '-content').classList.add('active');
            
            // Load content for the tab
            loadTabContent(tabName);
        }
        
        // Load tab content
        async function loadTabContent(tabName) {
            switch(tabName) {
                case 'repairs':
                    await loadRepairs();
                    break;
                case 'projects':
                    await loadProjects();
                    break;
                case 'api':
                    await loadAPIStats();
                    break;
                case 'messages':
                    await loadMessages();
                    break;
                case 'profile':
                    await loadProfile();
                    break;
            }
        }
        
        // Load repairs
        async function loadRepairs() {
            const repairs = [
                {
                    id: 'NZL-001',
                    device: 'MacBook Pro 13"',
                    issue: 'Won\\'t boot - water damage',
                    status: 'in-progress',
                    created: '2025-11-20',
                    estimated: '2025-11-27'
                },
                {
                    id: 'NZL-002',
                    device: 'iMac 27"',
                    issue: 'Hard drive replacement',
                    status: 'completed',
                    created: '2025-11-15',
                    completed: '2025-11-18'
                }
            ];
            
            const html = repairs.map(r => \`
                <div class="item-card">
                    <div class="item-header">
                        <div class="item-title">\${r.id} - \${r.device}</div>
                        <span class="status-badge status-\${r.status.replace('_', '-')}">\${r.status.replace('_', ' ').toUpperCase()}</span>
                    </div>
                    <div class="item-details">
                        <p><strong>Issue:</strong> \${r.issue}</p>
                        <p><strong>Submitted:</strong> \${r.created}</p>
                        \${r.status === 'completed' ? 
                            '<p><strong>Completed:</strong> ' + r.completed + '</p>' :
                            '<p><strong>Estimated:</strong> ' + r.estimated + '</p>'
                        }
                    </div>
                    <button onclick="viewDetails('\${r.id}')" style="margin-top: 1rem;">View Details</button>
                </div>
            \`).join('');
            
            document.getElementById('repairsList').innerHTML = html;
        }
        
        // Load projects
        async function loadProjects() {
            const projects = [
                {
                    id: 'FMI-001',
                    title: 'Podcast Theme Music',
                    type: 'Music Composition',
                    status: 'in-progress',
                    budget: '$1,500',
                    deadline: '2025-12-01'
                }
            ];
            
            const html = projects.map(p => \`
                <div class="item-card">
                    <div class="item-header">
                        <div class="item-title">\${p.id} - \${p.title}</div>
                        <span class="status-badge status-\${p.status.replace('_', '-')}">\${p.status.replace('_', ' ').toUpperCase()}</span>
                    </div>
                    <div class="item-details">
                        <p><strong>Type:</strong> \${p.type}</p>
                        <p><strong>Budget:</strong> \${p.budget}</p>
                        <p><strong>Deadline:</strong> \${p.deadline}</p>
                    </div>
                    <button onclick="viewProjectDetails('\${p.id}')" style="margin-top: 1rem;">View Project</button>
                </div>
            \`).join('');
            
            document.getElementById('projectsList').innerHTML = html;
        }
        
        // Load API stats
        async function loadAPIStats() {
            const html = \`
                <div class="stats-grid">
                    <div class="stat-box">
                        <div class="stat-value">2,340</div>
                        <div class="stat-label">Total Requests</div>
                    </div>
                    <div class="stat-box">
                        <div class="stat-value">450K</div>
                        <div class="stat-label">Tokens Used</div>
                    </div>
                    <div class="stat-box">
                        <div class="stat-value">$15.80</div>
                        <div class="stat-label">Current Cost</div>
                    </div>
                    <div class="stat-box">
                        <div class="stat-value">7,660</div>
                        <div class="stat-label">Remaining</div>
                    </div>
                </div>
                <h3>Recent API Calls</h3>
                <div class="item-card">
                    <p><strong>Model:</strong> claude-sonnet-4</p>
                    <p><strong>Tokens:</strong> 1,250</p>
                    <p><strong>Cost:</strong> $0.02</p>
                    <p><strong>Time:</strong> 2025-11-24 14:30:15</p>
                </div>
            \`;
            
            document.getElementById('apiStats').innerHTML = html;
        }
        
        // Load messages
        async function loadMessages() {
            const messages = [
                {
                    from: 'NOIZYLAB Support',
                    message: 'Your MacBook Pro repair is progressing well. Parts arrived today!',
                    time: '2 hours ago'
                },
                {
                    from: 'Fish Music Inc',
                    message: 'Draft composition ready for review. Check your email!',
                    time: '1 day ago'
                }
            ];
            
            const html = messages.map(m => \`
                <div class="message-box">
                    <div class="message-header">
                        <span class="message-from">\${m.from}</span>
                        <span class="message-time">\${m.time}</span>
                    </div>
                    <div>\${m.message}</div>
                </div>
            \`).join('');
            
            document.getElementById('messagesList').innerHTML = html;
        }
        
        // Load profile
        async function loadProfile() {
            const html = \`
                <div class="item-card">
                    <h3>Contact Information</h3>
                    <p><strong>Name:</strong> Rob Pickering</p>
                    <p><strong>Email:</strong> rp@fishmusicinc.com</p>
                    <p><strong>Phone:</strong> (555) 123-4567</p>
                    <button onclick="editProfile()" style="margin-top: 1rem;">Edit Profile</button>
                </div>
                <div class="item-card">
                    <h3>Notification Preferences</h3>
                    <p><label><input type="checkbox" checked> Email notifications</label></p>
                    <p><label><input type="checkbox" checked> SMS notifications</label></p>
                    <p><label><input type="checkbox"> Marketing emails</label></p>
                    <button onclick="savePreferences()" style="margin-top: 1rem;">Save Preferences</button>
                </div>
            \`;
            
            document.getElementById('profileInfo').innerHTML = html;
        }
        
        // Send message
        async function sendMessage() {
            const message = document.getElementById('newMessage').value;
            if (!message) {
                alert('Please enter a message');
                return;
            }
            
            alert('Message sent! We\\'ll respond within 24 hours.');
            document.getElementById('newMessage').value = '';
        }
        
        // Helper functions
        function viewDetails(id) {
            alert('Viewing details for ' + id);
        }
        
        function viewProjectDetails(id) {
            alert('Viewing project ' + id);
        }
        
        function editProfile() {
            alert('Profile editing functionality');
        }
        
        function savePreferences() {
            alert('Preferences saved!');
        }
        
        function logout() {
            alert('Logged out');
            window.location.href = '/login';
        }
        
        // Initialize
        window.addEventListener('DOMContentLoaded', () => {
            loadRepairs();
            document.getElementById('activeRepairs').textContent = '2';
            document.getElementById('activeProjects').textContent = '1';
            document.getElementById('apiUsage').textContent = '2.3K';
            document.getElementById('unreadMessages').textContent = '2';
        });
    </script>
</body>
</html>`;

  return new Response(html, {
    headers: { 'Content-Type': 'text/html; charset=utf-8' }
  });
}

// Authentication handlers
async function handleLogin(request, env, corsHeaders) {
  const data = await request.json();
  
  // Simplified auth for demo
  const token = 'customer_' + Math.random().toString(36).substring(7);
  
  return new Response(JSON.stringify({
    success: true,
    token: token,
    customer_id: 'CUST-001'
  }), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

async function handleRegister(request, env, corsHeaders) {
  const data = await request.json();
  
  const customerId = 'CUST-' + Date.now().toString(36).toUpperCase();
  
  return new Response(JSON.stringify({
    success: true,
    customer_id: customerId,
    message: 'Account created successfully'
  }), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

// Data handlers
async function handleGetProfile(request, env, corsHeaders) {
  const profile = {
    name: 'Rob Pickering',
    email: 'rp@fishmusicinc.com',
    phone: '(555) 123-4567',
    member_since: '2024-01-15'
  };
  
  return new Response(JSON.stringify(profile), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

async function handleUpdateProfile(request, env, corsHeaders) {
  const data = await request.json();
  
  return new Response(JSON.stringify({ success: true, updated: true }), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

async function handleGetRepairs(request, env, corsHeaders) {
  // Query repairs from database
  const repairs = [
    { id: 'NZL-001', status: 'in-progress', device: 'MacBook Pro' },
    { id: 'NZL-002', status: 'completed', device: 'iMac' }
  ];
  
  return new Response(JSON.stringify(repairs), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

async function handleGetRepair(request, env, corsHeaders) {
  const repairId = request.url.split('/').pop();
  
  const repair = {
    id: repairId,
    status: 'in-progress',
    device: 'MacBook Pro 13"',
    issue: 'Water damage',
    timeline: [
      { status: 'received', date: '2025-11-20', note: 'Device received' },
      { status: 'diagnosing', date: '2025-11-21', note: 'Initial diagnosis complete' },
      { status: 'in-repair', date: '2025-11-22', note: 'Repair in progress' }
    ]
  };
  
  return new Response(JSON.stringify(repair), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

async function handleGetProjects(request, env, corsHeaders) {
  const projects = [
    { id: 'FMI-001', title: 'Podcast Theme', status: 'in-progress' }
  ];
  
  return new Response(JSON.stringify(projects), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

async function handleGetProject(request, env, corsHeaders) {
  const projectId = request.url.split('/').pop();
  
  const project = {
    id: projectId,
    title: 'Podcast Theme Music',
    status: 'in-progress',
    budget: '$1,500',
    files: ['theme_draft_v1.mp3', 'theme_draft_v2.mp3']
  };
  
  return new Response(JSON.stringify(project), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

async function handleGetUsage(request, env, corsHeaders) {
  const usage = {
    requests: 2340,
    tokens: 450000,
    cost: 15.80,
    remaining: 7660
  };
  
  return new Response(JSON.stringify(usage), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

async function handleGetInvoices(request, env, corsHeaders) {
  const invoices = [
    { id: 'INV-001', amount: '$89', status: 'paid', date: '2025-11-18' },
    { id: 'INV-002', amount: '$750', status: 'pending', date: '2025-11-24' }
  ];
  
  return new Response(JSON.stringify(invoices), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

async function handleGetMessages(request, env, corsHeaders) {
  const messages = [
    {
      id: 'MSG-001',
      from: 'NOIZYLAB Support',
      message: 'Your repair is progressing well',
      time: '2025-11-24 14:30:00',
      read: false
    }
  ];
  
  return new Response(JSON.stringify(messages), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

async function handleSendMessage(request, env, corsHeaders) {
  const data = await request.json();
  
  const messageId = 'MSG-' + Date.now().toString(36).toUpperCase();
  
  return new Response(JSON.stringify({
    success: true,
    message_id: messageId,
    sent_at: new Date().toISOString()
  }), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

async function handleFileUpload(request, env, corsHeaders) {
  // In production, integrate with R2
  const fileId = 'FILE-' + Date.now().toString(36).toUpperCase();
  
  return new Response(JSON.stringify({
    success: true,
    file_id: fileId,
    url: 'https://storage.example.com/' + fileId
  }), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

async function handleGetNotifications(request, env, corsHeaders) {
  const notifications = [
    {
      id: 'NOTIF-001',
      type: 'repair_update',
      message: 'Your MacBook Pro repair is in progress',
      time: '2 hours ago',
      read: false
    }
  ];
  
  return new Response(JSON.stringify(notifications), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

async function handleUpdateNotificationPrefs(request, env, corsHeaders) {
  const data = await request.json();
  
  return new Response(JSON.stringify({
    success: true,
    preferences_updated: true
  }), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}
