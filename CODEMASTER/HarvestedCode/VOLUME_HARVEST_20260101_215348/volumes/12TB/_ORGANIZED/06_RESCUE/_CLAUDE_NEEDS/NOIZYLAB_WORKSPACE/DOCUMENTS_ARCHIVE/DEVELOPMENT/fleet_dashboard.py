
import streamlit as st
import json
import os

AGENT_COUNT = 10000
AGENTS_FILE = "fleet_agents.json"

if not os.path.exists(AGENTS_FILE):
    agents = [
        {
            "id": f"macbot_{i:05d}",
            "role": "Apple Support Agent",
            "status": "Idle"
        } for i in range(1, AGENT_COUNT + 1)
    ]
    with open(AGENTS_FILE, "w") as f:
        json.dump(agents, f, indent=2)
else:
    with open(AGENTS_FILE, "r") as f:
        agents = json.load(f)

st.set_page_config(page_title="Fleet AI Dashboard", layout="wide")
st.title("🚀 Fleet AI Support Dashboard")

search_query = st.text_input("🔍 Search Agents by ID or Role")

filtered_agents = [agent for agent in agents if search_query.lower() in agent['id'].lower() or search_query.lower() in agent['role'].lower()]

st.subheader(f"📋 Showing {len(filtered_agents)} of {len(agents)} Agents")

for agent in filtered_agents[:100]:
    col1, col2, col3 = st.columns([3, 2, 2])
    with col1:
        st.text(f"🧠 {agent['id']}")
    with col2:
        st.text(f"Role: {agent['role']}")
    with col3:
        st.text(f"Status: {agent['status']}")
