# 📊 Real-Time AI Dashboard Guide

## 🚀 Quick Start

### Start Everything
```bash
cd ~/NOIZYLAB/email-intelligence
./start_dashboard.sh
```

This starts:
- ✅ FastAPI server (port 8000)
- ✅ Streamlit dashboard (port 8501)

### Manual Start

**Terminal 1 - API Server:**
```bash
python api_server.py
```

**Terminal 2 - Dashboard:**
```bash
streamlit run dashboard.py
```

## 📡 API Endpoints

### WebSocket (Real-time)
```
ws://localhost:8000/ws
```

### REST API
- `GET /api/analytics` - Get current analytics
- `GET /api/powerbi` - Power BI CSV export
- `GET /api/insights` - AI-generated insights
- `GET /api/stream` - SSE streaming

## 📊 Dashboard Features

### Real-Time Metrics
- Total emails analyzed
- Spam rate percentage
- Average validity score
- Category count

### Visualizations
- **Category Distribution** - Pie chart
- **Trends** - Line chart (last 7 days)
- **Power BI Data Table** - Preview of export data

### AI Insights
- Summary of data
- Key insights
- Anomalies detected
- Recommendations
- Trend analysis
- Risk assessment
- Predictive insights

### Power BI Integration
- Direct CSV download
- Real-time data preview
- Auto-refresh capability

## 🤖 AI Features

### Gemini AI Integration
The dashboard uses Gemini AI to:
- Analyze email patterns
- Detect anomalies
- Generate recommendations
- Predict trends
- Assess risk levels

### Lead Scoring
Predict lead quality for emails:
```python
from ai_insights import AIInsightsGenerator

generator = AIInsightsGenerator()
score = generator.predict_lead_score("user@example.com")
print(score)
```

## 🔧 Configuration

### Environment Variables
```bash
export GEMINI_API_KEY="your-key"
export EMAIL_DB_PATH="email_intelligence.db"
export API_URL="http://localhost:8000"
export WEBSOCKET_URL="ws://localhost:8000/ws"
```

### Dashboard Settings
- Auto-refresh toggle
- Refresh interval (1-10 seconds)
- Manual refresh button

## 📈 Power BI Integration

### Method 1: CSV Export
1. Click "Export to Power BI" in sidebar
2. Download CSV
3. Import to Power BI Desktop

### Method 2: Direct API
1. Power BI → Get Data → Web
2. Enter: `http://localhost:8000/api/powerbi`
3. Data refreshes automatically

### Method 3: WebSocket (Advanced)
Connect Power BI to WebSocket for real-time updates.

## 🎯 Use Cases

### 1. Real-Time Monitoring
- Watch email processing in real-time
- Get instant alerts for anomalies
- Monitor spam rates

### 2. Trend Analysis
- View 7-day trends
- Identify patterns
- Predict future volumes

### 3. Lead Scoring
- Score emails for quality
- Prioritize business emails
- Filter high-value leads

### 4. Anomaly Detection
- AI detects unusual patterns
- Alerts for high spam rates
- Identifies suspicious domains

## 🔄 Auto-Refresh

The dashboard auto-refreshes every 2 seconds (configurable):
- Toggle in sidebar
- Adjust interval
- Manual refresh available

## 📱 Access

- **Dashboard**: http://localhost:8501
- **API Docs**: http://localhost:8000/docs
- **WebSocket**: ws://localhost:8000/ws

## 🛠️ Troubleshooting

**Dashboard not loading:**
- Check API server is running
- Verify port 8501 is available
- Check API_URL configuration

**No data showing:**
- Ensure database exists
- Process some emails first
- Check database path

**AI insights not working:**
- Set GEMINI_API_KEY
- Check API key is valid
- Falls back to rule-based insights

## 🚀 Advanced Features

### Custom Visualizations
Add custom charts in `dashboard.py`:
```python
fig = px.bar(data, x='category', y='count')
st.plotly_chart(fig)
```

### WebSocket Integration
Connect to real-time updates:
```javascript
const ws = new WebSocket('ws://localhost:8000/ws');
ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    // Update UI
};
```

### Predictive Analytics
Use AI insights for predictions:
- Email volume forecasting
- Spam rate predictions
- Lead quality trends

---

**Real-Time Analytics & AI Insights** 📊🤖✨

