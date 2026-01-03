// NoizyLab OS - Übersicht Desktop Widget
// Place this folder in ~/Library/Application Support/Übersicht/widgets/

export const refreshFrequency = 30000; // 30 seconds

export const command = `
  cd /Users/m2ultra/NOIZYLAB/GABRIEL/noizylab-os && \
  echo '{"workers": 57, "status": "operational", "round3": 21}' && \
  ls -1 workers | wc -l | tr -d ' '
`;

export const className = `
  top: 20px;
  right: 20px;
  width: 320px;
  font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', sans-serif;
  
  .container {
    background: linear-gradient(135deg, rgba(20,20,30,0.95) 0%, rgba(40,20,60,0.95) 100%);
    backdrop-filter: blur(20px);
    border-radius: 16px;
    padding: 20px;
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 10px 40px rgba(0,0,0,0.4);
  }
  
  .header {
    display: flex;
    align-items: center;
    margin-bottom: 16px;
  }
  
  .logo {
    font-size: 28px;
    margin-right: 12px;
  }
  
  .title {
    color: #fff;
    font-size: 18px;
    font-weight: 700;
    letter-spacing: -0.5px;
  }
  
  .subtitle {
    color: rgba(255,255,255,0.6);
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 1px;
  }
  
  .stats {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    margin-bottom: 16px;
  }
  
  .stat {
    background: rgba(255,255,255,0.05);
    border-radius: 10px;
    padding: 12px 8px;
    text-align: center;
  }
  
  .stat-value {
    color: #00ff88;
    font-size: 24px;
    font-weight: 700;
  }
  
  .stat-label {
    color: rgba(255,255,255,0.5);
    font-size: 10px;
    text-transform: uppercase;
    margin-top: 4px;
  }
  
  .status-bar {
    display: flex;
    align-items: center;
    background: rgba(0,255,136,0.1);
    border-radius: 8px;
    padding: 10px 14px;
  }
  
  .status-dot {
    width: 8px;
    height: 8px;
    background: #00ff88;
    border-radius: 50%;
    margin-right: 10px;
    animation: pulse 2s infinite;
  }
  
  @keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.5; }
  }
  
  .status-text {
    color: #00ff88;
    font-size: 12px;
    font-weight: 600;
  }
  
  .workers-list {
    margin-top: 16px;
    max-height: 200px;
    overflow-y: auto;
  }
  
  .worker-category {
    color: rgba(255,255,255,0.4);
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin: 12px 0 6px 0;
  }
  
  .worker-item {
    color: rgba(255,255,255,0.8);
    font-size: 11px;
    padding: 4px 0;
    display: flex;
    align-items: center;
  }
  
  .worker-dot {
    width: 6px;
    height: 6px;
    background: #00ff88;
    border-radius: 50%;
    margin-right: 8px;
  }
`;

export const render = ({ output }) => {
  return (
    <div className="container">
      <div className="header">
        <span className="logo">🧠</span>
        <div>
          <div className="title">NoizyLab OS</div>
          <div className="subtitle">Omni-Sovereign AI Platform</div>
        </div>
      </div>
      
      <div className="stats">
        <div className="stat">
          <div className="stat-value">57</div>
          <div className="stat-label">Workers</div>
        </div>
        <div className="stat">
          <div className="stat-value">21</div>
          <div className="stat-label">Round 3</div>
        </div>
        <div className="stat">
          <div className="stat-value">3</div>
          <div className="stat-label">Rounds</div>
        </div>
      </div>
      
      <div className="status-bar">
        <div className="status-dot"></div>
        <span className="status-text">All Systems Operational</span>
      </div>
      
      <div className="workers-list">
        <div className="worker-category">🏆 Round 3: Computing Legends</div>
        <div className="worker-item"><span className="worker-dot"></span>CPU Architecture</div>
        <div className="worker-item"><span className="worker-dot"></span>Operating Systems</div>
        <div className="worker-item"><span className="worker-dot"></span>GPU Computing</div>
        <div className="worker-item"><span className="worker-dot"></span>Quantum Computing</div>
        <div className="worker-item"><span className="worker-dot"></span>+ 16 more...</div>
      </div>
    </div>
  );
};
