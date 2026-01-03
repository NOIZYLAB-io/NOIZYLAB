/**
 * GABRIEL UNIFIED DASHBOARD
 * Visual interface for monitoring and controlling all integrated systems
 */

class UnifiedDashboard {
    constructor(container) {
        this.container = container;
        this.integrationHub = null;
        this.widgets = new Map();
        this.updateInterval = null;
        this.refreshRate = 5000; // 5 seconds
    }
    
    async init(integrationHub) {
        console.log('[Dashboard] Initializing unified dashboard...');
        
        this.integrationHub = integrationHub;
        
        // Create dashboard UI
        this.createDashboardUI();
        
        // Setup widgets for each system
        this.createSystemWidgets();
        
        // Start auto-refresh
        this.startAutoRefresh();
        
        // Listen to integration hub events
        this.setupEventListeners();
        
        console.log('[Dashboard] Dashboard initialized');
    }
    
    createDashboardUI() {
        const dashboardHTML = `
            <div id="unified-dashboard" class="dashboard-container">
                <div class="dashboard-header">
                    <h2>🎯 GABRIEL Command Center</h2>
                    <div class="dashboard-controls">
                        <button id="refresh-all" class="dashboard-btn">🔄 Refresh</button>
                        <button id="health-check" class="dashboard-btn">❤️ Health Check</button>
                        <button id="toggle-dashboard" class="dashboard-btn">📊 Toggle</button>
                    </div>
                </div>
                
                <div class="dashboard-grid" id="dashboard-grid">
                    <!-- Widgets will be added here -->
                </div>
                
                <div class="dashboard-console" id="dashboard-console">
                    <div class="console-header">
                        <span>📟 System Console</span>
                        <button id="clear-console">Clear</button>
                    </div>
                    <div class="console-output" id="console-output"></div>
                    <div class="console-input-container">
                        <input type="text" id="console-input" placeholder="Enter command...">
                        <button id="console-execute">Execute</button>
                    </div>
                </div>
            </div>
        `;
        
        const dashboardElement = document.createElement('div');
        dashboardElement.innerHTML = dashboardHTML;
        this.container.appendChild(dashboardElement);
        
        // Add styles
        this.injectStyles();
        
        // Bind event handlers
        this.bindEventHandlers();
    }
    
    createSystemWidgets() {
        const grid = document.getElementById('dashboard-grid');
        
        const systems = [
            {
                id: 'noizylab',
                name: 'NOIZYLAB',
                icon: '🔧',
                color: '#4facfe',
                metrics: ['Operations', 'Agents', 'Tasks']
            },
            {
                id: 'myfamily',
                name: 'MyFamily AI',
                icon: '👨‍👩‍👧‍👦',
                color: '#00f2fe',
                metrics: ['Members', 'Alerts', 'Schedule']
            },
            {
                id: 'gdrive',
                name: 'GDrive Stream',
                icon: '☁️',
                color: '#ffd700',
                metrics: ['Files', 'Storage', 'Streams']
            },
            {
                id: 'flow',
                name: 'Flow Extension',
                icon: '🌊',
                color: '#9b59b6',
                metrics: ['Active', 'Captures', 'Processing']
            },
            {
                id: 'techtool',
                name: 'TechTool',
                icon: '⚡',
                color: '#e74c3c',
                metrics: ['Commands', 'Status', 'History']
            },
            {
                id: 'architect',
                name: 'Chief Architect',
                icon: '🏗️',
                color: '#2ecc71',
                metrics: ['Health', 'Optimizations', 'Recommendations']
            },
            {
                id: 'network',
                name: 'Network Monitor',
                icon: '🌐',
                color: '#3498db',
                metrics: ['Status', 'Ports Active', 'Last Backup']
            }
        ];
        
        systems.forEach(system => {
            const widget = this.createWidget(system);
            grid.appendChild(widget);
            this.widgets.set(system.id, widget);
        });
    }
    
    createWidget(system) {
        const widget = document.createElement('div');
        widget.className = 'dashboard-widget';
        widget.id = `widget-${system.id}`;
        widget.style.borderColor = system.color;
        
        widget.innerHTML = `
            <div class="widget-header" style="background: ${system.color}20;">
                <span class="widget-icon">${system.icon}</span>
                <span class="widget-name">${system.name}</span>
                <span class="widget-status" id="status-${system.id}">⚪</span>
            </div>
            <div class="widget-body">
                ${system.metrics.map(metric => `
                    <div class="widget-metric">
                        <span class="metric-label">${metric}:</span>
                        <span class="metric-value" id="${system.id}-${metric.toLowerCase()}">--</span>
                    </div>
                `).join('')}
            </div>
            <div class="widget-footer">
                <button class="widget-btn" onclick="dashboard.viewSystem('${system.id}')">View</button>
                <button class="widget-btn" onclick="dashboard.controlSystem('${system.id}')">Control</button>
            </div>
        `;
        
        return widget;
    }
    
    async updateAllWidgets() {
        if (!this.integrationHub) return;
        
        try {
            // Get status of all systems
            const systemsStatus = await this.integrationHub.getAllSystemsStatus();
            
            systemsStatus.forEach(system => {
                this.updateWidgetStatus(system.name, system.status);
            });
            
            // Update individual system metrics
            await this.updateNoizylabWidget();
            await this.updateFamilyWidget();
            await this.updateGDriveWidget();
            await this.updateNetworkWidget();
            
        } catch (error) {
            console.error('[Dashboard] Update failed:', error);
            this.logToConsole('Error updating dashboard: ' + error.message, 'error');
        }
    }
    
    async updateNoizylabWidget() {
        try {
            const status = await this.integrationHub.getNoizylabStatus();
            this.updateMetric('noizylab', 'operations', status.operations || 0);
            this.updateMetric('noizylab', 'agents', status.agents || 0);
            this.updateMetric('noizylab', 'tasks', status.tasks || 0);
        } catch (error) {
            this.updateMetric('noizylab', 'operations', 'N/A');
        }
    }
    
    async updateFamilyWidget() {
        try {
            const status = await this.integrationHub.getFamilyAIStatus();
            this.updateMetric('myfamily', 'members', status.members || 0);
            this.updateMetric('myfamily', 'alerts', status.alerts || 0);
            this.updateMetric('myfamily', 'schedule', status.todayEvents || 0);
        } catch (error) {
            this.updateMetric('myfamily', 'members', 'N/A');
        }
    }
    
    async updateGDriveWidget() {
        try {
            const files = await this.integrationHub.listGDriveFiles();
            this.updateMetric('gdrive', 'files', files.length || 0);
            this.updateMetric('gdrive', 'storage', '-- GB');
            this.updateMetric('gdrive', 'streams', 0);
        } catch (error) {
            this.updateMetric('gdrive', 'files', 'N/A');
        }
    }
    
    async updateNetworkWidget() {
        try {
            const status = await this.integrationHub.getNetworkStatus();
            this.updateMetric('network', 'status', status.status || 'Unknown');
            this.updateMetric('network', 'ports active', status.ports_active + '/' + status.ports_total);
            this.updateMetric('network', 'last backup', 'Recent');
        } catch (error) {
            this.updateMetric('network', 'status', 'N/A');
        }
    }
    
    updateWidgetStatus(systemId, status) {
        const statusElement = document.getElementById(`status-${systemId}`);
        if (!statusElement) return;
        
        const statusIcons = {
            'connected': '🟢',
            'discovered': '🟡',
            'disconnected': '⚪',
            'error': '🔴'
        };
        
        statusElement.textContent = statusIcons[status] || '⚪';
        statusElement.title = status;
    }
    
    updateMetric(systemId, metric, value) {
        const metricElement = document.getElementById(`${systemId}-${metric}`);
        if (metricElement) {
            metricElement.textContent = value;
        }
    }
    
    viewSystem(systemId) {
        this.logToConsole(`Opening ${systemId} detailed view...`, 'info');
        
        // Create detailed view modal
        const modal = this.createSystemModal(systemId);
        document.body.appendChild(modal);
    }
    
    controlSystem(systemId) {
        this.logToConsole(`Opening ${systemId} control panel...`, 'info');
        
        // Create control panel modal
        const controlPanel = this.createControlPanel(systemId);
        document.body.appendChild(controlPanel);
    }
    
    createSystemModal(systemId) {
        const modal = document.createElement('div');
        modal.className = 'dashboard-modal';
        modal.innerHTML = `
            <div class="modal-content">
                <div class="modal-header">
                    <h3>${systemId.toUpperCase()} Details</h3>
                    <button class="modal-close" onclick="this.closest('.dashboard-modal').remove()">×</button>
                </div>
                <div class="modal-body">
                    <div id="system-details-${systemId}">Loading...</div>
                </div>
            </div>
        `;
        
        // Load system details
        this.loadSystemDetails(systemId, modal.querySelector(`#system-details-${systemId}`));
        
        return modal;
    }
    
    async loadSystemDetails(systemId, container) {
        try {
            const analysis = await this.integrationHub.analyzeSystemArchitecture(systemId);
            
            container.innerHTML = `
                <div class="system-analysis">
                    <h4>System Architecture</h4>
                    <pre>${JSON.stringify(analysis.architecture, null, 2)}</pre>
                    
                    <h4>Health Score: ${analysis.healthScore}%</h4>
                    <div class="health-bar">
                        <div class="health-fill" style="width: ${analysis.healthScore}%"></div>
                    </div>
                    
                    <h4>Recommendations</h4>
                    <ul>
                        ${analysis.recommendations.map(r => `<li>${r}</li>`).join('')}
                    </ul>
                </div>
            `;
        } catch (error) {
            container.innerHTML = `<p class="error">Failed to load details: ${error.message}</p>`;
        }
    }
    
    createControlPanel(systemId) {
        const panel = document.createElement('div');
        panel.className = 'dashboard-modal';
        panel.innerHTML = `
            <div class="modal-content">
                <div class="modal-header">
                    <h3>${systemId.toUpperCase()} Control Panel</h3>
                    <button class="modal-close" onclick="this.closest('.dashboard-modal').remove()">×</button>
                </div>
                <div class="modal-body">
                    <div class="control-grid">
                        <button class="control-btn" onclick="dashboard.restartSystem('${systemId}')">🔄 Restart</button>
                        <button class="control-btn" onclick="dashboard.optimizeSystem('${systemId}')">⚡ Optimize</button>
                        <button class="control-btn" onclick="dashboard.viewLogs('${systemId}')">📋 Logs</button>
                        <button class="control-btn" onclick="dashboard.configureSystem('${systemId}')">⚙️ Configure</button>
                    </div>
                </div>
            </div>
        `;
        
        return panel;
    }
    
    async restartSystem(systemId) {
        this.logToConsole(`Restarting ${systemId}...`, 'info');
        await this.integrationHub.connectToSystem(systemId, this.integrationHub.systems[systemId].url);
        this.logToConsole(`${systemId} restarted successfully`, 'success');
    }
    
    async optimizeSystem(systemId) {
        this.logToConsole(`Optimizing ${systemId}...`, 'info');
        const result = await this.integrationHub.optimizeSystem(systemId);
        this.logToConsole(`Optimization complete: ${JSON.stringify(result)}`, 'success');
    }
    
    viewLogs(systemId) {
        this.logToConsole(`Fetching logs for ${systemId}...`, 'info');
        // Implementation for viewing logs
    }
    
    configureSystem(systemId) {
        this.logToConsole(`Opening configuration for ${systemId}...`, 'info');
        // Implementation for system configuration
    }
    
    logToConsole(message, type = 'info') {
        const consoleOutput = document.getElementById('console-output');
        if (!consoleOutput) return;
        
        const timestamp = new Date().toLocaleTimeString();
        const logEntry = document.createElement('div');
        logEntry.className = `console-entry console-${type}`;
        logEntry.innerHTML = `<span class="console-time">[${timestamp}]</span> ${message}`;
        
        consoleOutput.appendChild(logEntry);
        consoleOutput.scrollTop = consoleOutput.scrollHeight;
    }
    
    async executeConsoleCommand(command) {
        this.logToConsole(`> ${command}`, 'command');
        
        try {
            // Try to process as voice command
            const result = await this.integrationHub.processVoiceCommand(command);
            
            if (result.success) {
                this.logToConsole(`✓ Command executed: ${JSON.stringify(result.result)}`, 'success');
            } else {
                this.logToConsole(`✗ Command failed: ${result.error}`, 'error');
            }
        } catch (error) {
            this.logToConsole(`✗ Error: ${error.message}`, 'error');
        }
    }
    
    startAutoRefresh() {
        this.updateAllWidgets(); // Initial update
        
        this.updateInterval = setInterval(() => {
            this.updateAllWidgets();
        }, this.refreshRate);
    }
    
    stopAutoRefresh() {
        if (this.updateInterval) {
            clearInterval(this.updateInterval);
            this.updateInterval = null;
        }
    }
    
    setupEventListeners() {
        // Listen to integration hub events
        this.integrationHub.on('system:connected', (event) => {
            const { systemName } = event.detail;
            this.logToConsole(`System connected: ${systemName}`, 'success');
            this.updateAllWidgets();
        });
        
        this.integrationHub.on('command:executed', (event) => {
            const { commandName, result } = event.detail;
            this.logToConsole(`Command executed: ${commandName}`, 'info');
        });
        
        this.integrationHub.on('command:failed', (event) => {
            const { commandName, error } = event.detail;
            this.logToConsole(`Command failed: ${commandName} - ${error.message}`, 'error');
        });
    }
    
    bindEventHandlers() {
        document.getElementById('refresh-all')?.addEventListener('click', () => {
            this.updateAllWidgets();
            this.logToConsole('Dashboard refreshed', 'info');
        });
        
        document.getElementById('health-check')?.addEventListener('click', async () => {
            this.logToConsole('Running health check...', 'info');
            const health = await this.integrationHub.performHealthCheck();
            this.logToConsole(`Health check complete: ${JSON.stringify(health)}`, 'success');
        });
        
        document.getElementById('toggle-dashboard')?.addEventListener('click', () => {
            const dashboard = document.getElementById('unified-dashboard');
            dashboard.classList.toggle('minimized');
        });
        
        document.getElementById('clear-console')?.addEventListener('click', () => {
            document.getElementById('console-output').innerHTML = '';
        });
        
        document.getElementById('console-execute')?.addEventListener('click', () => {
            const input = document.getElementById('console-input');
            if (input.value.trim()) {
                this.executeConsoleCommand(input.value);
                input.value = '';
            }
        });
        
        document.getElementById('console-input')?.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                document.getElementById('console-execute').click();
            }
        });
    }
    
    injectStyles() {
        const styles = `
            <style>
                .dashboard-container {
                    position: fixed;
                    top: 100px;
                    left: 20px;
                    width: 400px;
                    max-height: calc(100vh - 120px);
                    background: rgba(0, 0, 0, 0.95);
                    border: 2px solid rgba(79, 172, 254, 0.5);
                    border-radius: 15px;
                    backdrop-filter: blur(20px);
                    overflow: hidden;
                    z-index: 1000;
                    display: flex;
                    flex-direction: column;
                    transition: all 0.3s ease;
                }
                
                .dashboard-container.minimized {
                    height: 60px;
                }
                
                .dashboard-container.minimized .dashboard-grid,
                .dashboard-container.minimized .dashboard-console {
                    display: none;
                }
                
                .dashboard-header {
                    padding: 15px;
                    background: rgba(79, 172, 254, 0.2);
                    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                }
                
                .dashboard-header h2 {
                    margin: 0;
                    font-size: 18px;
                    color: #4facfe;
                }
                
                .dashboard-controls {
                    display: flex;
                    gap: 8px;
                }
                
                .dashboard-btn {
                    background: rgba(255, 255, 255, 0.1);
                    border: 1px solid rgba(255, 255, 255, 0.2);
                    border-radius: 5px;
                    padding: 5px 10px;
                    color: white;
                    font-size: 12px;
                    cursor: pointer;
                    transition: all 0.2s;
                }
                
                .dashboard-btn:hover {
                    background: rgba(79, 172, 254, 0.3);
                    border-color: #4facfe;
                }
                
                .dashboard-grid {
                    padding: 15px;
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    gap: 10px;
                    overflow-y: auto;
                    max-height: 300px;
                }
                
                .dashboard-widget {
                    background: rgba(255, 255, 255, 0.05);
                    border: 2px solid rgba(255, 255, 255, 0.1);
                    border-radius: 10px;
                    padding: 10px;
                    transition: all 0.2s;
                }
                
                .dashboard-widget:hover {
                    transform: translateY(-2px);
                    box-shadow: 0 5px 15px rgba(79, 172, 254, 0.3);
                }
                
                .widget-header {
                    display: flex;
                    align-items: center;
                    gap: 8px;
                    padding: 8px;
                    border-radius: 5px;
                    margin-bottom: 10px;
                }
                
                .widget-icon {
                    font-size: 20px;
                }
                
                .widget-name {
                    flex: 1;
                    font-weight: bold;
                    font-size: 12px;
                }
                
                .widget-status {
                    font-size: 16px;
                }
                
                .widget-body {
                    font-size: 11px;
                    margin-bottom: 10px;
                }
                
                .widget-metric {
                    display: flex;
                    justify-content: space-between;
                    margin-bottom: 5px;
                    padding: 3px 0;
                    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
                }
                
                .metric-label {
                    color: #a0a0a0;
                }
                
                .metric-value {
                    color: #4facfe;
                    font-weight: bold;
                }
                
                .widget-footer {
                    display: flex;
                    gap: 5px;
                }
                
                .widget-btn {
                    flex: 1;
                    background: rgba(79, 172, 254, 0.2);
                    border: 1px solid rgba(79, 172, 254, 0.3);
                    border-radius: 5px;
                    padding: 5px;
                    color: white;
                    font-size: 10px;
                    cursor: pointer;
                    transition: all 0.2s;
                }
                
                .widget-btn:hover {
                    background: rgba(79, 172, 254, 0.4);
                }
                
                .dashboard-console {
                    border-top: 1px solid rgba(255, 255, 255, 0.1);
                    display: flex;
                    flex-direction: column;
                    max-height: 200px;
                }
                
                .console-header {
                    padding: 10px;
                    background: rgba(255, 255, 255, 0.05);
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    font-size: 12px;
                    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
                }
                
                .console-header button {
                    background: rgba(255, 255, 255, 0.1);
                    border: none;
                    padding: 3px 8px;
                    border-radius: 3px;
                    color: white;
                    font-size: 10px;
                    cursor: pointer;
                }
                
                .console-output {
                    flex: 1;
                    padding: 10px;
                    overflow-y: auto;
                    font-family: 'Courier New', monospace;
                    font-size: 11px;
                    min-height: 100px;
                }
                
                .console-entry {
                    margin-bottom: 5px;
                    padding: 3px;
                }
                
                .console-time {
                    color: #888;
                }
                
                .console-info { color: #4facfe; }
                .console-success { color: #2ecc71; }
                .console-error { color: #e74c3c; }
                .console-command { color: #ffd700; }
                
                .console-input-container {
                    display: flex;
                    padding: 10px;
                    gap: 5px;
                    border-top: 1px solid rgba(255, 255, 255, 0.1);
                }
                
                .console-input-container input {
                    flex: 1;
                    background: rgba(255, 255, 255, 0.1);
                    border: 1px solid rgba(255, 255, 255, 0.2);
                    border-radius: 5px;
                    padding: 5px 10px;
                    color: white;
                    font-size: 11px;
                    font-family: 'Courier New', monospace;
                }
                
                .console-input-container button {
                    background: #4facfe;
                    border: none;
                    border-radius: 5px;
                    padding: 5px 15px;
                    color: white;
                    font-size: 11px;
                    cursor: pointer;
                }
                
                .dashboard-modal {
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100vw;
                    height: 100vh;
                    background: rgba(0, 0, 0, 0.8);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    z-index: 10000;
                }
                
                .modal-content {
                    background: rgba(20, 20, 30, 0.98);
                    border: 2px solid rgba(79, 172, 254, 0.5);
                    border-radius: 15px;
                    width: 80%;
                    max-width: 800px;
                    max-height: 80vh;
                    overflow: auto;
                }
                
                .modal-header {
                    padding: 20px;
                    background: rgba(79, 172, 254, 0.2);
                    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                }
                
                .modal-header h3 {
                    margin: 0;
                    color: #4facfe;
                }
                
                .modal-close {
                    background: none;
                    border: none;
                    color: white;
                    font-size: 30px;
                    cursor: pointer;
                    line-height: 1;
                }
                
                .modal-body {
                    padding: 20px;
                    color: white;
                }
                
                .control-grid {
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    gap: 15px;
                }
                
                .control-btn {
                    background: rgba(79, 172, 254, 0.2);
                    border: 2px solid rgba(79, 172, 254, 0.4);
                    border-radius: 10px;
                    padding: 20px;
                    color: white;
                    font-size: 16px;
                    cursor: pointer;
                    transition: all 0.2s;
                }
                
                .control-btn:hover {
                    background: rgba(79, 172, 254, 0.4);
                    transform: translateY(-2px);
                }
            </style>
        `;
        
        document.head.insertAdjacentHTML('beforeend', styles);
    }
    
    dispose() {
        this.stopAutoRefresh();
        if (this.container) {
            this.container.innerHTML = '';
        }
    }
}

// Make dashboard globally accessible
let dashboard = null;
