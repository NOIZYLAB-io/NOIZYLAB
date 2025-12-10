# 🚀 Quick Start - Real-Time Dashboard

## Start Everything

```bash
cd ~/NOIZYLAB/email-intelligence
./start_dashboard.sh
```

## Or Start Manually

### Terminal 1 - API Server
```bash
python api_server.py
```

### Terminal 2 - Dashboard
```bash
streamlit run dashboard.py
```

## Access

- **Dashboard**: http://localhost:8501
- **API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## Features

✅ **Real-Time Metrics** - Total emails, valid emails, spam rate  
✅ **Category Pie Chart** - Visual distribution  
✅ **AI Insights** - Gemini AI analysis  
✅ **Power BI Export** - One-click export  
✅ **Auto-Refresh** - Configurable refresh interval  

## Configuration

Create `.env` or set environment variables:

```bash
export GEMINI_API_KEY="your-key"
export DB_PATH="email_intelligence.db"
```

Or use `app/config.py` for configuration.

## API Endpoints

- `GET /analytics` - Get all email data (your format)
- `GET /api/analytics` - Enhanced analytics
- `GET /api/powerbi` - Power BI CSV
- `GET /api/insights` - AI insights
- `WS /ws` - WebSocket real-time

---

**Ready to use!** 📊✨

