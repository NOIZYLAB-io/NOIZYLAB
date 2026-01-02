#!/usr/bin/env python3
"""
AI Insights Generator - Gemini AI Integration
=============================================
Generates insights, anomalies, and recommendations from email data
"""

import sqlite3
import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import pandas as pd

try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False

# Get parent directory for default paths
_parent_dir = Path(__file__).parent.parent
_default_db_path = str(_parent_dir / "data" / "email_intelligence.db")

class AIInsightsGenerator:
    def __init__(self, db_path: str = None, api_key: str = None):
        self.db_path = db_path or _default_db_path
        self.api_key = api_key or os.getenv("GEMINI_API_KEY", "")
        
        if GEMINI_AVAILABLE and self.api_key:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel("gemini-1.5-flash")
        else:
            self.model = None
    
    def get_data_summary(self) -> Dict:
        """Get summary of email data"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Total
        cursor.execute("SELECT COUNT(*) FROM email_list")
        total = cursor.fetchone()[0]
        
        # Categories
        cursor.execute("SELECT category, COUNT(*) FROM email_list GROUP BY category")
        categories = {row[0] or "unknown": row[1] for row in cursor.fetchall()}
        
        # Spam stats
        cursor.execute("""
            SELECT 
                AVG(spam_score),
                COUNT(*) FILTER (WHERE spam_score > 0.7),
                MAX(spam_score)
            FROM email_list
        """)
        spam_avg, spam_count, spam_max = cursor.fetchone()
        
        # Validity stats
        cursor.execute("SELECT AVG(validity_score), MIN(validity_score) FROM email_list")
        validity_avg, validity_min = cursor.fetchone()
        
        # Recent trends
        cursor.execute("""
            SELECT DATE(processed_at), COUNT(*)
            FROM email_list
            WHERE processed_at >= datetime('now', '-7 days')
            GROUP BY DATE(processed_at)
            ORDER BY DATE(processed_at) DESC
        """)
        trends = {row[0]: row[1] for row in cursor.fetchall()}
        
        # Top spam domains
        cursor.execute("""
            SELECT 
                substr(email, instr(email, '@') + 1) as domain,
                COUNT(*) as count,
                AVG(spam_score) as avg_spam
            FROM email_list
            WHERE spam_score > 0.7
            GROUP BY domain
            ORDER BY count DESC
            LIMIT 5
        """)
        top_spam_domains = [{"domain": row[0], "count": row[1], "avg_spam": row[2]} for row in cursor.fetchall()]
        
        conn.close()
        
        return {
            "total": total,
            "categories": categories,
            "spam_avg": spam_avg or 0,
            "spam_count": spam_count or 0,
            "spam_max": spam_max or 0,
            "validity_avg": validity_avg or 0,
            "validity_min": validity_min or 0,
            "trends": trends,
            "top_spam_domains": top_spam_domains
        }
    
    def generate_insights(self) -> Dict:
        """Generate AI insights using Gemini"""
        data = self.get_data_summary()
        
        if not self.model:
            # Fallback to rule-based insights
            return self._generate_rule_based_insights(data)
        
        # Build prompt for Gemini
        prompt = f"""
        Analyze this email intelligence data and provide insights:
        
        Total Emails: {data['total']}
        Categories: {json.dumps(data['categories'])}
        Average Spam Score: {data['spam_avg']:.2f}
        High-Risk Spam Count: {data['spam_count']}
        Average Validity: {data['validity_avg']:.2f}
        Recent Trends (7 days): {json.dumps(data['trends'])}
        Top Spam Domains: {json.dumps(data['top_spam_domains'])}
        
        Provide a JSON response with:
        {{
            "summary": "Brief summary of the data",
            "key_insights": ["insight1", "insight2", "insight3"],
            "anomalies": ["anomaly1", "anomaly2"],
            "recommendations": ["rec1", "rec2", "rec3"],
            "trend_analysis": "Analysis of trends",
            "risk_assessment": "Overall risk level and why",
            "predictive_insights": "What to expect in the near future"
        }}
        """
        
        try:
            response = self.model.generate_content(prompt)
            result_text = response.text
            
            # Extract JSON
            json_match = json.search(r'\{.*\}', result_text, re.DOTALL)
            if json_match:
                insights = json.loads(json_match.group())
                insights['generated_at'] = datetime.now().isoformat()
                insights['data_snapshot'] = data
                return insights
            else:
                return self._parse_text_response(result_text, data)
        
        except Exception as e:
            print(f"Error generating AI insights: {e}")
            return self._generate_rule_based_insights(data)
    
    def _parse_text_response(self, text: str, data: Dict) -> Dict:
        """Parse text response into structured format"""
        return {
            "summary": text[:200],
            "key_insights": ["AI analysis available", "Review full response"],
            "anomalies": [],
            "recommendations": ["Review AI-generated insights"],
            "trend_analysis": "See summary",
            "risk_assessment": "Moderate",
            "predictive_insights": "Continue monitoring",
            "raw_response": text,
            "generated_at": datetime.now().isoformat()
        }
    
    def _generate_rule_based_insights(self, data: Dict) -> Dict:
        """Generate insights using rules (fallback)"""
        insights = {
            "summary": f"Analyzed {data['total']} emails with {data['spam_count']} high-risk spam",
            "key_insights": [],
            "anomalies": [],
            "recommendations": [],
            "trend_analysis": "",
            "risk_assessment": "",
            "predictive_insights": "",
            "generated_at": datetime.now().isoformat()
        }
        
        # Key insights
        if data['spam_count'] > data['total'] * 0.1:
            insights["key_insights"].append(f"High spam rate detected: {data['spam_count']} emails ({data['spam_count']/data['total']*100:.1f}%)")
        
        if data['validity_avg'] < 0.5:
            insights["key_insights"].append(f"Low average validity score: {data['validity_avg']*100:.1f}%")
        
        # Anomalies
        if data['spam_max'] > 0.9:
            insights["anomalies"].append(f"Very high spam score detected: {data['spam_max']:.2f}")
        
        # Recommendations
        if data['spam_count'] > 0:
            insights["recommendations"].append("Review and block high-risk spam domains")
        
        if data['validity_avg'] < 0.6:
            insights["recommendations"].append("Improve email validation process")
        
        insights["recommendations"].append("Monitor trends daily")
        
        # Risk assessment
        spam_rate = data['spam_count'] / data['total'] if data['total'] > 0 else 0
        if spam_rate > 0.2:
            insights["risk_assessment"] = "High - Immediate action recommended"
        elif spam_rate > 0.1:
            insights["risk_assessment"] = "Moderate - Monitor closely"
        else:
            insights["risk_assessment"] = "Low - Normal operations"
        
        return insights
    
    def predict_lead_score(self, email: str) -> Dict:
        """Predict lead quality score for an email"""
        data = self.get_data_summary()
        
        # Get email data
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT category, spam_score, validity_score, company_name, confidence_score
            FROM email_list
            WHERE email = ?
        """, (email,))
        
        row = cursor.fetchone()
        conn.close()
        
        if not row:
            return {"score": 0, "reason": "Email not found in database"}
        
        category, spam_score, validity_score, company_name, confidence = row
        
        # Calculate lead score
        base_score = 50
        
        # Category boost
        if category == "business":
            base_score += 30
        elif category == "personal":
            base_score += 10
        
        # Validity boost
        if validity_score:
            base_score += validity_score * 20
        
        # Spam penalty
        if spam_score:
            base_score -= spam_score * 40
        
        # Company name boost
        if company_name:
            base_score += 10
        
        # Confidence boost
        if confidence:
            base_score += confidence * 0.1
        
        score = max(0, min(100, base_score))
        
        return {
            "email": email,
            "lead_score": round(score, 2),
            "category": category,
            "company": company_name,
            "recommendation": "High priority" if score > 70 else "Medium priority" if score > 40 else "Low priority"
        }

if __name__ == "__main__":
    generator = AIInsightsGenerator()
    insights = generator.generate_insights()
    print(json.dumps(insights, indent=2))

