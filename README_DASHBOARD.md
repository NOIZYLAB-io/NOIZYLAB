# 📊 Real-Time Email Intelligence Dashboard

## Your Exact Code - Integrated & Ready!

The dashboard uses your exact code pattern:

```python
import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import google.generativeai as genai
from app.config import API_KEY, DB_PATH

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="Email Intelligence Dashboard", layout="wide")
st.title("📊 Real-Time Email Intelligence Dashboard")

# Connect to DB
conn = sqlite3.connect(DB_PATH)
df = pd.read_sql_query("SELECT * FROM email_list", conn)

# Show KPIs
st.metric("Total Emails", len(df))
st.metric("Valid Emails", len(df[df['category'].notnull()]))

# Category Pie Chart
fig = px.pie(df, names='category', title='Email Categories')
st.plotly_chart(fig, use_container_width=True)

# AI Insights
prompt = f"Summarize trends and anomalies in this email dataset:\n{df.head(50).to_dict()}"
response = model.generate_content(prompt)
st.subheader("🤖 AI Insights")
st.write(response.text)

# Export for Power BI
if st.button("Export for Power BI"):
    df.to_csv("powerbi_export.csv", index=False)
    st.success("✅ Data exported for Power BI!")
```

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install streamlit pandas plotly google-generativeai
```

### 2. Configure
Edit `app/config.py` or set environment variables:
```bash
export GEMINI_API_KEY="your-key"
export DB_PATH="email_intelligence.db"
```

### 3. Run Dashboard
```bash
streamlit run dashboard.py
```

## 📡 API Endpoint

Your `/analytics` endpoint is also integrated:

```python
@app.get("/analytics")
async def analytics():
    cursor.execute("SELECT * FROM email_list")
    rows = cursor.fetchall()
    return {"emails": rows}
```

Access at: `http://localhost:8000/analytics`

## ✨ Features

✅ **Direct DB Connection** - Uses your exact pattern  
✅ **KPI Metrics** - Total & Valid emails  
✅ **Category Pie Chart** - Visual distribution  
✅ **Gemini AI Insights** - Real-time analysis  
✅ **Power BI Export** - One-click export  

## 📁 Files

- `dashboard.py` - Your exact dashboard code
- `api_server.py` - API with `/analytics` endpoint
- `app/config.py` - Configuration (API_KEY, DB_PATH)

---

**Ready to use!** 📊✨

