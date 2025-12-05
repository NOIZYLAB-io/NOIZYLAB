#!/usr/bin/env python3
"""
🚀 NOIZYLAB.CA - COMPLETE CLIENT PORTAL
Check-in system, payments, invoicing, client management - TONIGHT!
"""

from flask import Flask, render_template_string, request, jsonify, redirect, session, url_for
import json
import os
import sys
from datetime import datetime, timedelta
import secrets
import hashlib

# Import Mail.app email system (WORKS WITH NO PASSWORDS!)
sys.path.append('../FishMusic_Email_System')
try:
    from MAIL_APP_COMPLETE_SYSTEM import MailAppMailer
    mailer = MailAppMailer()
    EMAIL_READY = True
    print("🍎 Mail.app Email System: READY!!")
except:
    EMAIL_READY = False
    print("⚠️  Email system not found - will mock emails")

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

# DATABASE (JSON for tonight, Supabase later!)
DATA_DIR = "portal_data"
os.makedirs(DATA_DIR, exist_ok=True)

# HOMEPAGE - NOIZYLAB.CA PORTAL
PORTAL_HOME_HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NoizyLab Portal - Client & Project Management</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
            background: linear-gradient(135deg, #0f0f23 0%, #1a1a3e 100%);
            color: #fff;
            min-height: 100vh;
        }
        
        .header {
            background: rgba(0,0,0,0.5);
            padding: 20px 40px;
            backdrop-filter: blur(10px);
            border-bottom: 2px solid #00ff88;
        }
        
        .header h1 {
            color: #00ff88;
            font-size: 2rem;
        }
        
        .header .subtitle {
            color: #888;
            font-size: 0.9rem;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 40px 20px;
        }
        
        .dashboard-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }
        
        .card {
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(0,255,136,0.2);
            border-radius: 10px;
            padding: 30px;
            transition: all 0.3s;
        }
        
        .card:hover {
            background: rgba(255,255,255,0.08);
            border-color: #00ff88;
            transform: translateY(-5px);
        }
        
        .card h2 {
            color: #00ff88;
            margin-bottom: 15px;
            font-size: 1.5rem;
        }
        
        .stat-big {
            font-size: 3rem;
            font-weight: bold;
            color: #00ff88;
            margin: 10px 0;
        }
        
        .btn {
            display: inline-block;
            background: #00ff88;
            color: #0f0f23;
            padding: 12px 30px;
            border-radius: 5px;
            text-decoration: none;
            font-weight: 600;
            border: none;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .btn:hover {
            background: #00cc6a;
            transform: translateY(-2px);
        }
        
        .btn-secondary {
            background: transparent;
            border: 2px solid #00ff88;
            color: #00ff88;
        }
        
        .btn-secondary:hover {
            background: #00ff88;
            color: #0f0f23;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        
        th, td {
            padding: 15px;
            text-align: left;
            border-bottom: 1px solid rgba(0,255,136,0.1);
        }
        
        th {
            background: rgba(0,255,136,0.1);
            color: #00ff88;
            font-weight: 600;
        }
        
        tr:hover {
            background: rgba(0,255,136,0.05);
        }
        
        .status-badge {
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
        }
        
        .status-active { background: #00ff88; color: #0f0f23; }
        .status-pending { background: #ffa500; color: #0f0f23; }
        .status-completed { background: #888; color: #fff; }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        label {
            display: block;
            margin-bottom: 8px;
            color: #00ff88;
            font-weight: 500;
        }
        
        input, textarea, select {
            width: 100%;
            padding: 12px;
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(0,255,136,0.3);
            border-radius: 5px;
            color: #fff;
            font-size: 1rem;
        }
        
        input:focus, textarea:focus, select:focus {
            outline: none;
            border-color: #00ff88;
            background: rgba(255,255,255,0.08);
        }
        
        textarea {
            min-height: 120px;
            resize: vertical;
        }
        
        .success-msg {
            background: #00ff88;
            color: #0f0f23;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 20px;
            font-weight: 600;
        }
        
        .tabs {
            display: flex;
            gap: 10px;
            margin-bottom: 30px;
            border-bottom: 2px solid rgba(0,255,136,0.2);
        }
        
        .tab {
            padding: 15px 25px;
            cursor: pointer;
            border-bottom: 2px solid transparent;
            transition: all 0.3s;
            color: #888;
        }
        
        .tab.active {
            color: #00ff88;
            border-bottom-color: #00ff88;
        }
        
        .tab-content {
            display: none;
        }
        
        .tab-content.active {
            display: block;
        }
        
        @media (max-width: 768px) {
            .dashboard-grid {
                grid-template-columns: 1fr;
            }
            .header h1 {
                font-size: 1.5rem;
            }
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🔬 NoizyLab Portal</h1>
        <div class="subtitle">Complete Client & Project Management | noizylab.ca</div>
    </div>
    
    <div class="container">
        <!-- DASHBOARD STATS -->
        <div class="dashboard-grid">
            <div class="card">
                <h2>📊 Active Projects</h2>
                <div class="stat-big">{{ stats.active_projects }}</div>
                <p>Currently in progress</p>
            </div>
            
            <div class="card">
                <h2>👥 Active Clients</h2>
                <div class="stat-big">{{ stats.active_clients }}</div>
                <p>Managing relationships</p>
            </div>
            
            <div class="card">
                <h2>💰 This Month</h2>
                <div class="stat-big">${{ stats.revenue_month }}</div>
                <p>Revenue generated</p>
            </div>
            
            <div class="card">
                <h2>✅ Check-ins Today</h2>
                <div class="stat-big">{{ stats.checkins_today }}</div>
                <p>Project updates logged</p>
            </div>
        </div>
        
        <!-- TABS -->
        <div class="tabs">
            <div class="tab active" onclick="switchTab('checkin')">📝 Check-In</div>
            <div class="tab" onclick="switchTab('projects')">📁 Projects</div>
            <div class="tab" onclick="switchTab('clients')">👥 Clients</div>
            <div class="tab" onclick="switchTab('payments')">💳 Payments</div>
            <div class="tab" onclick="switchTab('invoices')">🧾 Invoices</div>
        </div>
        
        <!-- CHECK-IN TAB -->
        <div id="checkin" class="tab-content active">
            <div class="card">
                <h2>📝 Project Check-In</h2>
                <p style="margin-bottom: 20px; color: #888;">Log your daily progress & updates</p>
                
                <form action="/checkin" method="post">
                    <div class="form-group">
                        <label>Project</label>
                        <select name="project_id" required>
                            <option value="">Select project...</option>
                            {% for project in projects %}
                            <option value="{{ project.id }}">{{ project.name }}</option>
                            {% endfor %}
                        </select>
                    </div>
                    
                    <div class="form-group">
                        <label>Status</label>
                        <select name="status" required>
                            <option value="in_progress">In Progress</option>
                            <option value="blocked">Blocked</option>
                            <option value="review">Ready for Review</option>
                            <option value="completed">Completed</option>
                        </select>
                    </div>
                    
                    <div class="form-group">
                        <label>Hours Worked Today</label>
                        <input type="number" name="hours" step="0.5" required>
                    </div>
                    
                    <div class="form-group">
                        <label>Update / Notes</label>
                        <textarea name="notes" placeholder="What did you accomplish today?"></textarea>
                    </div>
                    
                    <button type="submit" class="btn">Submit Check-In</button>
                </form>
            </div>
        </div>
        
        <!-- PROJECTS TAB -->
        <div id="projects" class="tab-content">
            <div class="card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                    <h2>📁 All Projects</h2>
                    <button class="btn" onclick="showNewProjectForm()">+ New Project</button>
                </div>
                
                <table>
                    <thead>
                        <tr>
                            <th>Project</th>
                            <th>Client</th>
                            <th>Status</th>
                            <th>Budget</th>
                            <th>Deadline</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for project in projects %}
                        <tr>
                            <td><strong>{{ project.name }}</strong></td>
                            <td>{{ project.client_name }}</td>
                            <td><span class="status-badge status-{{ project.status }}">{{ project.status }}</span></td>
                            <td>${{ project.budget }}</td>
                            <td>{{ project.deadline }}</td>
                            <td>
                                <button class="btn btn-secondary" style="padding: 5px 15px; font-size: 0.85rem;">View</button>
                            </td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
        
        <!-- CLIENTS TAB -->
        <div id="clients" class="tab-content">
            <div class="card">
                <h2>👥 Client Management</h2>
                <button class="btn" style="margin: 20px 0;">+ Add Client</button>
                
                <table>
                    <thead>
                        <tr>
                            <th>Client</th>
                            <th>Email</th>
                            <th>Projects</th>
                            <th>Total Paid</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for client in clients %}
                        <tr>
                            <td><strong>{{ client.name }}</strong></td>
                            <td>{{ client.email }}</td>
                            <td>{{ client.project_count }}</td>
                            <td>${{ client.total_paid }}</td>
                            <td><span class="status-badge status-active">Active</span></td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
        
        <!-- PAYMENTS TAB -->
        <div id="payments" class="tab-content">
            <div class="card">
                <h2>💳 Payment Tracking</h2>
                
                <div style="margin: 20px 0;">
                    <h3 style="color: #00ff88; margin-bottom: 15px;">Quick Actions</h3>
                    <button class="btn">Record Payment</button>
                    <button class="btn btn-secondary">Generate Invoice</button>
                    <button class="btn btn-secondary">Send Reminder</button>
                </div>
                
                <table>
                    <thead>
                        <tr>
                            <th>Date</th>
                            <th>Client</th>
                            <th>Project</th>
                            <th>Amount</th>
                            <th>Status</th>
                            <th>Method</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for payment in payments %}
                        <tr>
                            <td>{{ payment.date }}</td>
                            <td>{{ payment.client }}</td>
                            <td>{{ payment.project }}</td>
                            <td>${{ payment.amount }}</td>
                            <td><span class="status-badge status-{{ payment.status }}">{{ payment.status }}</span></td>
                            <td>{{ payment.method }}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
        
        <!-- INVOICES TAB -->
        <div id="invoices" class="tab-content">
            <div class="card">
                <h2>🧾 Invoice Management</h2>
                
                <form action="/create-invoice" method="post" style="margin: 20px 0;">
                    <h3 style="color: #00ff88; margin-bottom: 15px;">Create New Invoice</h3>
                    
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                        <div class="form-group">
                            <label>Client</label>
                            <select name="client_id" required>
                                <option value="">Select client...</option>
                                {% for client in clients %}
                                <option value="{{ client.id }}">{{ client.name }}</option>
                                {% endfor %}
                            </select>
                        </div>
                        
                        <div class="form-group">
                            <label>Project</label>
                            <select name="project_id" required>
                                <option value="">Select project...</option>
                                {% for project in projects %}
                                <option value="{{ project.id }}">{{ project.name }}</option>
                                {% endfor %}
                            </select>
                        </div>
                        
                        <div class="form-group">
                            <label>Amount</label>
                            <input type="number" name="amount" step="0.01" required>
                        </div>
                        
                        <div class="form-group">
                            <label>Due Date</label>
                            <input type="date" name="due_date" required>
                        </div>
                    </div>
                    
                    <div class="form-group">
                        <label>Description / Line Items</label>
                        <textarea name="description" placeholder="Services provided..."></textarea>
                    </div>
                    
                    <button type="submit" class="btn">Create & Send Invoice</button>
                </form>
                
                <h3 style="color: #00ff88; margin: 30px 0 15px 0;">Recent Invoices</h3>
                <table>
                    <thead>
                        <tr>
                            <th>Invoice #</th>
                            <th>Client</th>
                            <th>Amount</th>
                            <th>Due Date</th>
                            <th>Status</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for invoice in invoices %}
                        <tr>
                            <td><strong>#{{ invoice.number }}</strong></td>
                            <td>{{ invoice.client_name }}</td>
                            <td>${{ invoice.amount }}</td>
                            <td>{{ invoice.due_date }}</td>
                            <td><span class="status-badge status-{{ invoice.status }}">{{ invoice.status }}</span></td>
                            <td>
                                <button class="btn btn-secondary" style="padding: 5px 15px; font-size: 0.85rem;">View PDF</button>
                            </td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
    </div>
    
    <script>
        function switchTab(tabName) {
            // Hide all tabs
            document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.tab').forEach(el => el.classList.remove('active'));
            
            // Show selected tab
            document.getElementById(tabName).classList.add('active');
            event.target.classList.add('active');
        }
        
        function showNewProjectForm() {
            alert('New Project form coming up!');
        }
    </script>
</body>
</html>
"""

# DATA STORAGE (Simple JSON for tonight)
class DataStore:
    """Simple JSON data storage"""
    
    @staticmethod
    def load(filename):
        filepath = os.path.join(DATA_DIR, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                return json.load(f)
        return []
    
    @staticmethod
    def save(filename, data):
        filepath = os.path.join(DATA_DIR, filename)
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)

# Initialize with demo data
def init_demo_data():
    """Create demo data for tonight"""
    
    # Demo clients
    clients = [
        {
            'id': 1,
            'name': 'Gavin Lumsden (Rogers)',
            'email': 'gavin@rogers.com',
            'company': 'Rogers Media',
            'project_count': 1,
            'total_paid': 0,
            'status': 'active'
        }
    ]
    DataStore.save('clients.json', clients)
    
    # Demo projects
    projects = [
        {
            'id': 1,
            'name': 'DESIGN REUNION Mix',
            'client_id': 1,
            'client_name': 'Gavin Lumsden (Rogers)',
            'status': 'in_progress',
            'budget': 0,
            'deadline': '2026-01-31',
            'created': datetime.now().isoformat()
        }
    ]
    DataStore.save('projects.json', projects)
    
    # Demo payments
    payments = []
    DataStore.save('payments.json', payments)
    
    # Demo invoices
    invoices = []
    DataStore.save('invoices.json', invoices)
    
    # Demo check-ins
    checkins = []
    DataStore.save('checkins.json', checkins)

# Routes
@app.route('/')
def home():
    """Portal homepage"""
    clients = DataStore.load('clients.json')
    projects = DataStore.load('projects.json')
    payments = DataStore.load('payments.json')
    invoices = DataStore.load('invoices.json')
    checkins = DataStore.load('checkins.json')
    
    # Calculate stats
    stats = {
        'active_projects': len([p for p in projects if p['status'] == 'in_progress']),
        'active_clients': len([c for c in clients if c['status'] == 'active']),
        'revenue_month': sum(p['amount'] for p in payments if p.get('status') == 'completed'),
        'checkins_today': len([c for c in checkins if c.get('date', '').startswith(datetime.now().strftime('%Y-%m-%d'))])
    }
    
    return render_template_string(
        PORTAL_HOME_HTML,
        stats=stats,
        projects=projects,
        clients=clients,
        payments=payments,
        invoices=invoices
    )

@app.route('/checkin', methods=['POST'])
def submit_checkin():
    """Submit project check-in"""
    checkins = DataStore.load('checkins.json')
    
    new_checkin = {
        'id': len(checkins) + 1,
        'project_id': request.form.get('project_id'),
        'status': request.form.get('status'),
        'hours': float(request.form.get('hours')),
        'notes': request.form.get('notes'),
        'date': datetime.now().isoformat(),
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    checkins.append(new_checkin)
    DataStore.save('checkins.json', checkins)
    
    # Send email notification via Mail.app
    if EMAIL_READY:
        projects = DataStore.load('projects.json')
        project = next((p for p in projects if str(p['id']) == str(new_checkin['project_id'])), None)
        
        if project:
            mailer.send_checkin_notification(
                project['name'],
                new_checkin['status'],
                new_checkin['hours'],
                new_checkin['notes']
            )
    
    return redirect('/')

@app.route('/create-invoice', methods=['POST'])
def create_invoice():
    """Create new invoice"""
    invoices = DataStore.load('invoices.json')
    clients = DataStore.load('clients.json')
    
    client_id = request.form.get('client_id')
    client = next((c for c in clients if str(c['id']) == str(client_id)), None)
    
    invoice_number = f"NL{datetime.now().strftime('%Y%m%d')}{len(invoices)+1:03d}"
    
    new_invoice = {
        'id': len(invoices) + 1,
        'number': invoice_number,
        'client_id': client_id,
        'client_name': client['name'] if client else 'Unknown',
        'client_email': client['email'] if client else '',
        'project_id': request.form.get('project_id'),
        'amount': float(request.form.get('amount')),
        'description': request.form.get('description'),
        'due_date': request.form.get('due_date'),
        'status': 'pending',
        'created': datetime.now().isoformat(),
        'created_display': datetime.now().strftime('%Y-%m-%d')
    }
    
    invoices.append(new_invoice)
    DataStore.save('invoices.json', invoices)
    
    # Send invoice email via Mail.app
    if EMAIL_READY and client:
        mailer.send_invoice(
            client['email'],
            client['name'],
            invoice_number,
            new_invoice['amount'],
            new_invoice['description'],
            new_invoice['due_date']
        )
    
    return redirect('/')

@app.route('/api/checkins')
def get_checkins():
    """API endpoint for check-ins"""
    return jsonify(DataStore.load('checkins.json'))

@app.route('/api/stats')
def get_stats():
    """API endpoint for stats"""
    projects = DataStore.load('projects.json')
    clients = DataStore.load('clients.json')
    payments = DataStore.load('payments.json')
    checkins = DataStore.load('checkins.json')
    
    return jsonify({
        'total_projects': len(projects),
        'active_projects': len([p for p in projects if p['status'] == 'in_progress']),
        'total_clients': len(clients),
        'total_revenue': sum(p.get('amount', 0) for p in payments if p.get('status') == 'completed'),
        'checkins_total': len(checkins)
    })

if __name__ == '__main__':
    # Initialize demo data
    if not os.path.exists(os.path.join(DATA_DIR, 'clients.json')):
        init_demo_data()
    
    print("🔬 NOIZYLAB.CA PORTAL - STARTING...")
    print("=" * 60)
    print("🌐 Portal: http://localhost:4000")
    print("📝 Check-ins: Track daily progress")
    print("💳 Payments: Full payment tracking")
    print("🧾 Invoices: Generate & send invoices")
    print("👥 Clients: Complete client management")
    print("=" * 60)
    print("NOIZYLAB.CA - GORUNFREE! 🚀")
    print()
    
    app.run(host='0.0.0.0', port=4000, debug=True)

