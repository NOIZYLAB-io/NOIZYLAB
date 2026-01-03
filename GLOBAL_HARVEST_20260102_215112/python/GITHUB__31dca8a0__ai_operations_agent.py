#!/usr/bin/env python3
"""
AI Operations Agent - Intelligent System Assistant
==================================================
Uses AI/LLM to analyze, diagnose, and recommend solutions
"""

import os
import json
import sqlite3
from datetime import datetime
from typing import Dict, List, Optional
from pathlib import Path
import requests


class AIOperationsAgent:
    """AI-powered operations assistant"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.use_local = not self.api_key  # Use local if no API key
        
        self.db_path = Path(__file__).parent / "ai_operations.db"
        self._init_database()
        
        # System context
        self.system_context = """You are an expert DevOps AI assistant for NoizyLab Portal.
You analyze system metrics, logs, alerts, and network events.
Provide clear, actionable recommendations.
Focus on root causes and preventive measures."""
        
        print(f"🤖 AI Operations Agent initialized ({'OpenAI' if self.api_key else 'Local'} mode)")
    
    def _init_database(self):
        """Initialize AI operations database"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ai_analyses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                analysis_type TEXT,
                input_data TEXT,
                ai_response TEXT,
                recommendations TEXT,
                confidence REAL,
                tokens_used INTEGER
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ai_predictions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                prediction_type TEXT,
                predicted_value TEXT,
                actual_value TEXT,
                accuracy REAL,
                model_version TEXT
            )
        """)
        
        conn.commit()
        conn.close()
    
    def analyze_alerts(self, alerts: List[Dict]) -> Dict:
        """
        AI-powered alert analysis
        
        Returns:
            Analysis with root cause, impact, and recommendations
        """
        if not alerts:
            return {"error": "No alerts to analyze"}
        
        # Prepare context
        alert_summary = self._summarize_alerts(alerts)
        
        prompt = f"""Analyze these system alerts and provide:
1. Root cause analysis
2. Impact assessment (Low/Medium/High/Critical)
3. Immediate actions needed
4. Preventive measures

Alerts:
{alert_summary}

Respond in JSON format with keys: root_cause, impact, immediate_actions (list), preventive_measures (list), confidence (0-1)"""
        
        response = self._query_llm(prompt)
        
        # Parse and save
        try:
            analysis = json.loads(response)
            self._save_analysis("alert_analysis", alert_summary, response, 
                              json.dumps(analysis.get("immediate_actions", [])),
                              analysis.get("confidence", 0.5))
            return analysis
        except:
            return {
                "root_cause": "Analysis pending",
                "impact": "Medium",
                "immediate_actions": ["Review alerts manually"],
                "preventive_measures": ["Enable monitoring"],
                "raw_response": response
            }
    
    def diagnose_issue(self, issue_description: str, context: Dict = None) -> Dict:
        """
        AI-powered issue diagnosis
        
        Args:
            issue_description: Description of the issue
            context: Additional context (metrics, logs, etc.)
        
        Returns:
            Diagnosis with likely causes and solutions
        """
        context_str = json.dumps(context, indent=2) if context else "No additional context"
        
        prompt = f"""Diagnose this system issue:

Issue: {issue_description}

Context:
{context_str}

Provide:
1. Most likely causes (ranked by probability)
2. Step-by-step diagnostic procedure
3. Solutions for each cause
4. Time estimate for resolution

Respond in JSON format."""
        
        response = self._query_llm(prompt)
        
        try:
            diagnosis = json.loads(response)
            self._save_analysis("issue_diagnosis", issue_description, response,
                              json.dumps(diagnosis.get("solutions", [])), 0.7)
            return diagnosis
        except:
            return {"raw_response": response}
    
    def explain_metrics(self, metrics: Dict) -> str:
        """
        AI explains what metrics mean in plain English
        
        Args:
            metrics: System metrics
        
        Returns:
            Plain English explanation
        """
        metrics_str = json.dumps(metrics, indent=2)
        
        prompt = f"""Explain these system metrics in simple terms:

{metrics_str}

Provide:
1. What these numbers mean
2. Is this good or bad?
3. What should the user watch for?
4. Any concerns?

Use plain, non-technical language."""
        
        explanation = self._query_llm(prompt)
        self._save_analysis("metrics_explanation", metrics_str, explanation, "", 0.8)
        
        return explanation
    
    def suggest_optimizations(self, system_state: Dict) -> List[Dict]:
        """
        AI suggests system optimizations
        
        Args:
            system_state: Current system state
        
        Returns:
            List of optimization suggestions
        """
        state_str = json.dumps(system_state, indent=2)
        
        prompt = f"""Analyze this system state and suggest optimizations:

{state_str}

For each optimization, provide:
1. What to optimize
2. Why it matters
3. How to do it (specific steps)
4. Expected improvement
5. Risk level (Low/Medium/High)

Respond as JSON array."""
        
        response = self._query_llm(prompt)
        
        try:
            optimizations = json.loads(response)
            self._save_analysis("optimization_suggestions", state_str, response,
                              json.dumps(optimizations), 0.6)
            return optimizations
        except:
            return []
    
    def predict_capacity(self, historical_data: List[Dict]) -> Dict:
        """
        AI-powered capacity planning
        
        Args:
            historical_data: Historical metrics
        
        Returns:
            Capacity predictions and recommendations
        """
        data_summary = self._summarize_data(historical_data)
        
        prompt = f"""Analyze this historical data and predict capacity needs:

{data_summary}

Provide:
1. Current trend (increasing/stable/decreasing)
2. When will we hit 80% capacity?
3. When will we hit 100% capacity?
4. Recommended actions
5. Confidence level

Respond in JSON format."""
        
        response = self._query_llm(prompt)
        
        try:
            prediction = json.loads(response)
            self._save_analysis("capacity_prediction", data_summary, response,
                              json.dumps(prediction.get("recommended_actions", [])),
                              prediction.get("confidence", 0.5))
            return prediction
        except:
            return {"raw_response": response}
    
    def natural_query(self, question: str) -> str:
        """
        Ask AI questions about your system in natural language
        
        Args:
            question: Natural language question
        
        Returns:
            AI answer
        """
        # Get recent system context
        context = self._get_system_context()
        
        prompt = f"""Answer this question about the NoizyLab system:

Question: {question}

Current System State:
{context}

Provide a clear, concise answer."""
        
        answer = self._query_llm(prompt)
        self._save_analysis("natural_query", question, answer, "", 0.7)
        
        return answer
    
    def generate_incident_report(self, incident_data: Dict) -> str:
        """
        AI generates a professional incident report
        
        Args:
            incident_data: Incident details
        
        Returns:
            Formatted incident report
        """
        data_str = json.dumps(incident_data, indent=2)
        
        prompt = f"""Generate a professional incident report:

Incident Data:
{data_str}

Include:
1. Executive Summary
2. Timeline
3. Root Cause
4. Impact Analysis
5. Resolution Steps
6. Preventive Measures
7. Lessons Learned

Format as a professional report."""
        
        report = self._query_llm(prompt)
        self._save_analysis("incident_report", data_str, report, "", 0.9)
        
        return report
    
    def smart_alert_routing(self, alert: Dict) -> Dict:
        """
        AI decides who should be notified and how
        
        Args:
            alert: Alert details
        
        Returns:
            Routing decision
        """
        alert_str = json.dumps(alert, indent=2)
        
        prompt = f"""Decide how to route this alert:

{alert_str}

Determine:
1. Severity (Low/Medium/High/Critical)
2. Who should be notified (on-call/team/manager/all)
3. Notification channels (slack/email/sms/phone)
4. Urgency (can-wait/soon/immediate/emergency)
5. Auto-escalation needed? (yes/no)

Respond in JSON format."""
        
        response = self._query_llm(prompt)
        
        try:
            routing = json.loads(response)
            return routing
        except:
            return {
                "severity": "Medium",
                "notify": ["on-call"],
                "channels": ["slack"],
                "urgency": "soon"
            }
    
    def _query_llm(self, prompt: str, max_tokens: int = 1000) -> str:
        """Query LLM (OpenAI or local)"""
        if self.use_local:
            return self._query_local_llm(prompt)
        else:
            return self._query_openai(prompt, max_tokens)
    
    def _query_openai(self, prompt: str, max_tokens: int) -> str:
        """Query OpenAI API"""
        try:
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "gpt-4o-mini",  # Fast and cheap
                    "messages": [
                        {"role": "system", "content": self.system_context},
                        {"role": "user", "content": prompt}
                    ],
                    "max_tokens": max_tokens,
                    "temperature": 0.3  # More focused responses
                },
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                return data["choices"][0]["message"]["content"]
            else:
                return f"Error: {response.status_code}"
        
        except Exception as e:
            return f"Error querying OpenAI: {str(e)}"
    
    def _query_local_llm(self, prompt: str) -> str:
        """Query local LLM (Ollama/LM Studio)"""
        # Try Ollama first (localhost:11434)
        try:
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "llama2",
                    "prompt": f"{self.system_context}\n\n{prompt}",
                    "stream": False
                },
                timeout=30
            )
            
            if response.status_code == 200:
                return response.json()["response"]
        except:
            pass
        
        # Fallback to rule-based analysis
        return self._rule_based_analysis(prompt)
    
    def _rule_based_analysis(self, prompt: str) -> str:
        """Fallback rule-based analysis when no LLM available"""
        if "alert" in prompt.lower():
            return json.dumps({
                "root_cause": "Multiple alerts detected - manual review recommended",
                "impact": "Medium",
                "immediate_actions": ["Review system logs", "Check resource usage"],
                "preventive_measures": ["Enable detailed monitoring", "Set up alerts"],
                "confidence": 0.5
            })
        elif "optimize" in prompt.lower():
            return json.dumps([{
                "optimization": "Review resource usage",
                "why": "Proactive optimization",
                "how": "Check CPU, memory, and disk usage",
                "improvement": "Varies",
                "risk": "Low"
            }])
        else:
            return "AI analysis not available. Please configure OpenAI API key or install local LLM."
    
    def _summarize_alerts(self, alerts: List[Dict]) -> str:
        """Summarize alerts for LLM"""
        summary = []
        for alert in alerts[:10]:  # Limit to recent 10
            summary.append(f"- [{alert.get('level', 'unknown')}] {alert.get('category', 'unknown')}: {alert.get('message', 'No message')}")
        return "\n".join(summary)
    
    def _summarize_data(self, data: List[Dict]) -> str:
        """Summarize data for LLM"""
        if not data:
            return "No data available"
        
        # Get key statistics
        summary = f"Data points: {len(data)}\n"
        summary += f"Time range: {data[0].get('timestamp', 'unknown')} to {data[-1].get('timestamp', 'unknown')}\n"
        summary += f"Sample data: {json.dumps(data[:5], indent=2)}"
        
        return summary
    
    def _get_system_context(self) -> str:
        """Get current system context"""
        import psutil
        
        context = {
            "cpu_percent": psutil.cpu_percent(),
            "memory_percent": psutil.virtual_memory().percent,
            "disk_percent": psutil.disk_usage('/').percent,
            "timestamp": datetime.now().isoformat()
        }
        
        return json.dumps(context, indent=2)
    
    def _save_analysis(self, analysis_type: str, input_data: str, 
                      response: str, recommendations: str, confidence: float):
        """Save analysis to database"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO ai_analyses 
            (analysis_type, input_data, ai_response, recommendations, confidence)
            VALUES (?, ?, ?, ?, ?)
        """, (analysis_type, input_data[:1000], response[:5000], recommendations[:2000], confidence))
        
        conn.commit()
        conn.close()
    
    def get_analysis_history(self, analysis_type: Optional[str] = None, limit: int = 10) -> List[Dict]:
        """Get analysis history"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        if analysis_type:
            cursor.execute("""
                SELECT timestamp, analysis_type, recommendations, confidence
                FROM ai_analyses
                WHERE analysis_type = ?
                ORDER BY timestamp DESC
                LIMIT ?
            """, (analysis_type, limit))
        else:
            cursor.execute("""
                SELECT timestamp, analysis_type, recommendations, confidence
                FROM ai_analyses
                ORDER BY timestamp DESC
                LIMIT ?
            """, (limit,))
        
        results = []
        for row in cursor.fetchall():
            results.append({
                "timestamp": row[0],
                "type": row[1],
                "recommendations": row[2],
                "confidence": row[3]
            })
        
        conn.close()
        return results


# Global AI agent
ai_agent = AIOperationsAgent()


# Convenience functions
def analyze_alerts(alerts: List[Dict]) -> Dict:
    """Analyze alerts with AI"""
    return ai_agent.analyze_alerts(alerts)


def diagnose(issue: str, context: Dict = None) -> Dict:
    """Diagnose issue with AI"""
    return ai_agent.diagnose_issue(issue, context)


def ask(question: str) -> str:
    """Ask AI a question"""
    return ai_agent.natural_query(question)


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="AI Operations Agent")
    parser.add_argument("action", choices=["analyze", "diagnose", "ask", "explain"])
    parser.add_argument("--input", help="Input data or question")
    
    args = parser.parse_args()
    
    agent = AIOperationsAgent()
    
    if args.action == "ask" and args.input:
        answer = agent.natural_query(args.input)
        print(f"\n🤖 AI: {answer}\n")
    
    elif args.action == "explain":
        import psutil
        metrics = {
            "cpu": psutil.cpu_percent(),
            "memory": psutil.virtual_memory().percent,
            "disk": psutil.disk_usage('/').percent
        }
        explanation = agent.explain_metrics(metrics)
        print(f"\n🤖 {explanation}\n")
    
    else:
        print("Example usage:")
        print('  python ai_operations_agent.py ask --input "Why is CPU high?"')
        print('  python ai_operations_agent.py explain')

