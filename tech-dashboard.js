// NOIZYLAB TECH DASHBOARD WORKER
// Voice-controlled, touchscreen-optimized interface for Rob
export default {
  async fetch(request, env) {
    return new Response(getTechDashboardHTML(), {
      headers: { 'Content-Type': 'text/html' }
    });
  }
};

function getTechDashboardHTML() {
  return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>NOIZYLAB Tech Dashboard - R.S.P. GORUNFREE</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: #0a0e27;
            color: #ffffff;
            overflow-x: hidden;
        }
        
        /* HEADER */
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        }
        
        .header-content {
            max-width: 1600px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .logo {
            font-size: 32px;
            font-weight: 900;
        }
        
        .stats-bar {
            display: flex;
            gap: 30px;
        }
        
        .stat {
            text-align: center;
        }
        
        .stat-value {
            font-size: 32px;
            font-weight: 900;
        }
        
        .stat-label {
            font-size: 12px;
            opacity: 0.8;
            text-transform: uppercase;
        }
        
        /* VOICE CONTROL */
        .voice-control {
            position: fixed;
            bottom: 30px;
            right: 30px;
            z-index: 200;
        }
        
        .voice-btn {
            width: 80px;
            height: 80px;
            border-radius: 50%;
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            border: none;
            font-size: 40px;
            cursor: pointer;
            box-shadow: 0 8px 30px rgba(240, 147, 251, 0.4);
            transition: transform 0.2s;
        }
        
        .voice-btn:active {
            transform: scale(0.95);
        }
        
        .voice-btn.listening {
            animation: pulse 1.5s infinite;
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); box-shadow: 0 8px 30px rgba(240, 147, 251, 0.4); }
            50% { transform: scale(1.1); box-shadow: 0 8px 40px rgba(240, 147, 251, 0.8); }
        }
        
        /* MAIN GRID */
        .main-grid {
            max-width: 1600px;
            margin: 30px auto;
            padding: 0 30px;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 30px;
        }
        
        /* CARDS */
        .card {
            background: #1a1f3a;
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
        }
        
        .card-title {
            font-size: 24px;
            font-weight: 700;
            margin-bottom: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        /* GOAL PROGRESS */
        .goal-ring {
            width: 200px;
            height: 200px;
            margin: 20px auto;
            position: relative;
        }
        
        .goal-ring svg {
            transform: rotate(-90deg);
        }
        
        .goal-ring circle {
            fill: none;
            stroke-width: 20;
        }
        
        .goal-ring .bg {
            stroke: #2a3050;
        }
        
        .goal-ring .progress {
            stroke: url(#gradient);
            stroke-linecap: round;
            transition: stroke-dashoffset 0.5s;
        }
        
        .goal-text {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
        }
        
        .goal-number {
            font-size: 48px;
            font-weight: 900;
        }
        
        .goal-label {
            font-size: 14px;
            opacity: 0.7;
        }
        
        /* REPAIR LIST */
        .repair-item {
            background: #242943;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 15px;
            cursor: pointer;
            transition: transform 0.2s;
            border-left: 4px solid;
        }
        
        .repair-item:hover {
            transform: translateX(5px);
        }
        
        .repair-item.intake { border-color: #ffc107; }
        .repair-item.diagnosed { border-color: #2196f3; }
        .repair-item.in_progress { border-color: #ff9800; }
        .repair-item.completed { border-color: #4caf50; }
        
        .repair-id {
            font-weight: 700;
            font-size: 18px;
            margin-bottom: 5px;
        }
        
        .repair-device {
            color: #aaa;
            margin-bottom: 10px;
        }
        
        .repair-status {
            display: inline-block;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
        }
        
        .status-intake { background: #ffc107; color: #000; }
        .status-diagnosed { background: #2196f3; color: white; }
        .status-in_progress { background: #ff9800; color: white; }
        .status-completed { background: #4caf50; color: white; }
        
        /* ACTION BUTTONS */
        .action-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 15px;
        }
        
        .action-btn {
            padding: 60px 20px;
            border: none;
            border-radius: 16px;
            font-size: 24px;
            font-weight: 700;
            cursor: pointer;
            transition: transform 0.2s;
            color: white;
        }
        
        .action-btn:active {
            transform: scale(0.98);
        }
        
        .btn-start {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        
        .btn-complete {
            background: linear-gradient(135deg, #4caf50 0%, #45a049 100%);
        }
        
        .btn-diagnose {
            background: linear-gradient(135deg, #2196f3 0%, #1976d2 100%);
        }
        
        .btn-refresh {
            background: linear-gradient(135deg, #ff9800 0%, #f57c00 100%);
        }
        
        /* LOADING */
        .loading {
            text-align: center;
            padding: 40px;
            color: #666;
        }
        
        /* VOICE FEEDBACK */
        .voice-feedback {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: rgba(0,0,0,0.9);
            padding: 40px;
            border-radius: 20px;
            text-align: center;
            display: none;
            z-index: 300;
        }
        
        .voice-feedback.show {
            display: block;
        }
        
        .voice-transcript {
            font-size: 24px;
            margin-bottom: 20px;
        }
        
        .voice-response {
            font-size: 18px;
            color: #4caf50;
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="header-content">
            <div class="logo">NOIZYLAB 🔧</div>
            <div class="stats-bar">
                <div class="stat">
                    <div class="stat-value" id="todayCompleted">0</div>
                    <div class="stat-label">Completed Today</div>
                </div>
                <div class="stat">
                    <div class="stat-value" id="todayRevenue">$0</div>
                    <div class="stat-label">Today's Revenue</div>
                </div>
                <div class="stat">
                    <div class="stat-value" id="inProgress">0</div>
                    <div class="stat-label">In Progress</div>
                </div>
            </div>
        </div>
    </div>
    
    <div class="main-grid">
        <!-- DAILY GOAL CARD -->
        <div class="card">
            <div class="card-title">
                Daily Goal
                <span id="goalDate"></span>
            </div>
            <div class="goal-ring">
                <svg width="200" height="200">
                    <defs>
                        <linearGradient id="gradient" x1="0%" y1="0%" x2="100%" y2="100%">
                            <stop offset="0%" style="stop-color:#667eea" />
                            <stop offset="100%" style="stop-color:#764ba2" />
                        </linearGradient>
                    </defs>
                    <circle class="bg" cx="100" cy="100" r="85" />
                    <circle class="progress" cx="100" cy="100" r="85" id="progressCircle" />
                </svg>
                <div class="goal-text">
                    <div class="goal-number" id="goalProgress">0/12</div>
                    <div class="goal-label">Repairs</div>
                </div>
            </div>
        </div>
        
        <!-- QUICK ACTIONS CARD -->
        <div class="card">
            <div class="card-title">Quick Actions</div>
            <div class="action-grid">
                <button class="action-btn btn-start" onclick="startNextRepair()">
                    ▶️<br>Start Next
                </button>
                <button class="action-btn btn-complete" onclick="completeRepair()">
                    ✓<br>Complete
                </button>
                <button class="action-btn btn-diagnose" onclick="runDiagnostic()">
                    🔍<br>Diagnose
                </button>
                <button class="action-btn btn-refresh" onclick="refreshDashboard()">
                    🔄<br>Refresh
                </button>
            </div>
        </div>
        
        <!-- PENDING REPAIRS -->
        <div class="card">
            <div class="card-title">
                Pending Repairs
                <span id="pendingCount">0</span>
            </div>
            <div id="pendingList" class="loading">Loading...</div>
        </div>
        
        <!-- IN PROGRESS REPAIRS -->
        <div class="card">
            <div class="card-title">
                In Progress
                <span id="inProgressCount">0</span>
            </div>
            <div id="inProgressList" class="loading">Loading...</div>
        </div>
    </div>
    
    <!-- VOICE CONTROL -->
    <div class="voice-control">
        <button class="voice-btn" id="voiceBtn" onclick="toggleVoiceControl()">🎤</button>
    </div>
    
    <!-- VOICE FEEDBACK -->
    <div class="voice-feedback" id="voiceFeedback">
        <div class="voice-transcript" id="voiceTranscript"></div>
        <div class="voice-response" id="voiceResponse"></div>
    </div>
    
    <script>
        const API_URL = 'https://noizylab-api.fishmusicinc.workers.dev';
        let selectedRepairId = null;
        let recognition = null;
        
        // Initialize
        document.addEventListener('DOMContentLoaded', () => {
            refreshDashboard();
            setInterval(refreshDashboard, 30000); // Auto-refresh every 30 seconds
            document.getElementById('goalDate').textContent = new Date().toLocaleDateString();
            initVoiceRecognition();
        });
        
        // Voice Recognition Setup
        function initVoiceRecognition() {
            if ('webkitSpeechRecognition' in window) {
                recognition = new webkitSpeechRecognition();
                recognition.continuous = false;
                recognition.interimResults = false;
                
                recognition.onresult = async (event) => {
                    const transcript = event.results[0][0].transcript;
                    await processVoiceCommand(transcript);
                };
                
                recognition.onend = () => {
                    document.getElementById('voiceBtn').classList.remove('listening');
                };
            }
        }
        
        function toggleVoiceControl() {
            if (recognition) {
                const btn = document.getElementById('voiceBtn');
                if (btn.classList.contains('listening')) {
                    recognition.stop();
                } else {
                    btn.classList.add('listening');
                    recognition.start();
                }
            } else {
                alert('Voice recognition not supported in this browser');
            }
        }
        
        async function processVoiceCommand(transcript) {
            const feedback = document.getElementById('voiceFeedback');
            const transcriptEl = document.getElementById('voiceTranscript');
            const responseEl = document.getElementById('voiceResponse');
            
            transcriptEl.textContent = \`You said: "\${transcript}"\`;
            responseEl.textContent = 'Processing...';
            feedback.classList.add('show');
            
            try {
                const response = await fetch(API_URL + '/api/voice', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        command: transcript,
                        context: { repair_id: selectedRepairId }
                    })
                });
                
                const data = await response.json();
                responseEl.textContent = data.response;
                
                // Speak response
                if ('speechSynthesis' in window) {
                    const utterance = new SpeechSynthesisUtterance(data.response);
                    speechSynthesis.speak(utterance);
                }
                
                // Refresh dashboard after command
                setTimeout(() => {
                    refreshDashboard();
                    feedback.classList.remove('show');
                }, 3000);
                
            } catch (error) {
                responseEl.textContent = 'Error: ' + error.message;
            }
        }
        
        // Dashboard Functions
        async function refreshDashboard() {
            try {
                const response = await fetch(API_URL + '/api/dashboard');
                const data = await response.json();
                
                // Update stats
                document.getElementById('todayCompleted').textContent = data.today.completed || 0;
                document.getElementById('todayRevenue').textContent = '$' + (data.today.revenue || 0);
                document.getElementById('inProgress').textContent = data.today.in_progress || 0;
                
                // Update goal progress
                const completed = data.today.completed || 0;
                const goal = 12;
                const progress = Math.min((completed / goal) * 100, 100);
                
                document.getElementById('goalProgress').textContent = \`\${completed}/\${goal}\`;
                
                const circle = document.getElementById('progressCircle');
                const circumference = 2 * Math.PI * 85;
                circle.style.strokeDasharray = circumference;
                circle.style.strokeDashoffset = circumference - (progress / 100 * circumference);
                
                // Update repair lists
                const pending = data.recent_repairs.filter(r => r.status === 'intake');
                const inProgress = data.recent_repairs.filter(r => r.status === 'in_progress');
                
                document.getElementById('pendingCount').textContent = pending.length;
                document.getElementById('inProgressCount').textContent = inProgress.length;
                
                displayRepairs('pendingList', pending);
                displayRepairs('inProgressList', inProgress);
                
            } catch (error) {
                console.error('Dashboard refresh failed:', error);
            }
        }
        
        function displayRepairs(elementId, repairs) {
            const container = document.getElementById(elementId);
            
            if (repairs.length === 0) {
                container.innerHTML = '<p style="text-align: center; color: #666; padding: 20px;">No repairs</p>';
                return;
            }
            
            container.innerHTML = repairs.map(repair => \`
                <div class="repair-item \${repair.status}" onclick="selectRepair('\${repair.repair_id}')">
                    <div class="repair-id">\${repair.repair_id}</div>
                    <div class="repair-device">\${repair.device_type} - \${repair.customer_name}</div>
                    <span class="repair-status status-\${repair.status}">\${repair.status.toUpperCase()}</span>
                </div>
            \`).join('');
        }
        
        function selectRepair(repairId) {
            selectedRepairId = repairId;
            // Highlight selected
            document.querySelectorAll('.repair-item').forEach(el => {
                el.style.border = '2px solid transparent';
            });
            event.target.closest('.repair-item').style.border = '2px solid #667eea';
        }
        
        async function startNextRepair() {
            if (confirm('Start the next repair in the queue?')) {
                await processVoiceCommand('start next repair');
            }
        }
        
        async function completeRepair() {
            if (!selectedRepairId) {
                alert('Please select a repair first');
                return;
            }
            if (confirm(\`Mark repair \${selectedRepairId} as complete?\`)) {
                await processVoiceCommand(\`complete repair \${selectedRepairId}\`);
            }
        }
        
        async function runDiagnostic() {
            if (!selectedRepairId) {
                alert('Please select a repair first');
                return;
            }
            
            // Get repair details
            const response = await fetch(API_URL + '/api/repairs/' + selectedRepairId);
            const data = await response.json();
            
            if (data.repair) {
                // Run AI diagnostic
                const diagResponse = await fetch(API_URL + '/api/diagnose', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        repair_id: selectedRepairId,
                        device_type: data.repair.device_type,
                        issue_description: data.repair.issue_description
                    })
                });
                
                const diagData = await diagResponse.json();
                
                if (diagData.success) {
                    alert('AI Diagnostic Complete!\\n\\n' + JSON.stringify(diagData.diagnosis, null, 2));
                    refreshDashboard();
                }
            }
        }
    </script>
</body>
</html>`;
}
