#!/usr/bin/env python3
"""
AI Predictive Capacity Planner
===============================
Predicts when you'll run out of resources and what to do about it
"""

import sqlite3
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Tuple
from pathlib import Path
import requests
import os
import json


class PredictiveCapacityPlanner:
    """AI-powered capacity planning"""
    
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.monitoring_db = Path("/Users/m2ultra/NOIZYLAB/monitoring/monitoring.db")
    
    def predict_resource_exhaustion(self) -> Dict:
        """
        Predict when resources will be exhausted
        
        Returns:
            Predictions for CPU, memory, disk
        """
        predictions = {}
        
        # Get historical data
        cpu_data = self._get_historical_data("cpu_percent", days=7)
        memory_data = self._get_historical_data("memory_percent", days=7)
        disk_data = self._get_historical_data("disk_percent", days=30)
        
        # Predict each resource
        if cpu_data:
            predictions["cpu"] = self._predict_exhaustion(cpu_data, "CPU", 95.0)
        
        if memory_data:
            predictions["memory"] = self._predict_exhaustion(memory_data, "Memory", 95.0)
        
        if disk_data:
            predictions["disk"] = self._predict_exhaustion(disk_data, "Disk", 95.0)
        
        # Get AI recommendations
        if any(p.get("days_until_exhaustion", 999) < 30 for p in predictions.values()):
            predictions["ai_recommendations"] = self._get_ai_recommendations(predictions)
        
        return predictions
    
    def _get_historical_data(self, metric: str, days: int) -> List[Tuple[datetime, float]]:
        """Get historical metric data"""
        if not self.monitoring_db.exists():
            return []
        
        conn = sqlite3.connect(str(self.monitoring_db))
        cursor = conn.cursor()
        
        try:
            cursor.execute(f"""
                SELECT timestamp, {metric}
                FROM system_metrics
                WHERE timestamp > datetime('now', '-{days} days')
                ORDER BY timestamp
            """)
            
            data = [(datetime.fromisoformat(row[0]), row[1]) for row in cursor.fetchall()]
            conn.close()
            return data
        except:
            conn.close()
            return []
    
    def _predict_exhaustion(self, data: List[Tuple[datetime, float]], 
                           resource_name: str, threshold: float) -> Dict:
        """Predict when resource will hit threshold"""
        if len(data) < 10:
            return {"error": "Insufficient data"}
        
        # Extract values and timestamps
        timestamps = np.array([(t - data[0][0]).total_seconds() / 86400 for t, v in data])  # Days since start
        values = np.array([v for t, v in data])
        
        # Linear regression
        slope, intercept = np.polyfit(timestamps, values, 1)
        
        # Current value
        current_value = values[-1]
        
        # Predict when threshold will be reached
        if slope > 0:  # Increasing trend
            days_until_exhaustion = (threshold - current_value) / (slope)
            exhaustion_date = datetime.now() + timedelta(days=days_until_exhaustion)
        else:
            days_until_exhaustion = None
            exhaustion_date = None
        
        # Calculate growth rate
        growth_rate = slope  # % per day
        
        return {
            "resource": resource_name,
            "current_value": float(current_value),
            "threshold": threshold,
            "trend": "increasing" if slope > 0 else "stable" if abs(slope) < 0.1 else "decreasing",
            "growth_rate_per_day": float(growth_rate),
            "days_until_exhaustion": float(days_until_exhaustion) if days_until_exhaustion and days_until_exhaustion > 0 else None,
            "exhaustion_date": exhaustion_date.isoformat() if exhaustion_date else None,
            "confidence": min(0.9, len(data) / 100)  # More data = more confidence
        }
    
    def _get_ai_recommendations(self, predictions: Dict) -> List[str]:
        """Get AI recommendations for capacity issues"""
        if not self.api_key:
            return self._rule_based_recommendations(predictions)
        
        predictions_str = json.dumps(predictions, indent=2, default=str)
        
        prompt = f"""Analyze these capacity predictions and provide specific recommendations:

{predictions_str}

Provide:
1. Immediate actions (if any resource < 7 days)
2. Short-term actions (if any resource < 30 days)
3. Long-term capacity planning advice
4. Cost optimization tips

Return as JSON array of recommendations."""
        
        try:
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers={"Authorization": f"Bearer {self.api_key}"},
                json={
                    "model": "gpt-4o-mini",
                    "messages": [
                        {"role": "system", "content": "You are a capacity planning expert."},
                        {"role": "user", "content": prompt}
                    ],
                    "max_tokens": 600
                },
                timeout=20
            )
            
            if response.status_code == 200:
                data = response.json()
                return json.loads(data["choices"][0]["message"]["content"])
        except:
            pass
        
        return self._rule_based_recommendations(predictions)
    
    def _rule_based_recommendations(self, predictions: Dict) -> List[str]:
        """Fallback recommendations"""
        recommendations = []
        
        for resource, pred in predictions.items():
            if isinstance(pred, dict) and pred.get("days_until_exhaustion"):
                days = pred["days_until_exhaustion"]
                
                if days < 7:
                    recommendations.append(f"🚨 URGENT: {pred['resource']} will be exhausted in {days:.0f} days - Take immediate action!")
                elif days < 30:
                    recommendations.append(f"⚠️ WARNING: {pred['resource']} will be exhausted in {days:.0f} days - Plan capacity increase")
                elif days < 90:
                    recommendations.append(f"ℹ️ INFO: {pred['resource']} trending up - Monitor and plan for future growth")
        
        if not recommendations:
            recommendations.append("✅ All resources within normal capacity - No immediate action needed")
        
        return recommendations
    
    def generate_capacity_report(self) -> str:
        """Generate comprehensive capacity report"""
        predictions = self.predict_resource_exhaustion()
        
        report = f"""
# Capacity Planning Report
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Resource Predictions

"""
        
        for resource, pred in predictions.items():
            if resource == "ai_recommendations":
                continue
            
            if isinstance(pred, dict) and "current_value" in pred:
                report += f"""
### {pred['resource']}
- Current Usage: {pred['current_value']:.1f}%
- Trend: {pred['trend']}
- Growth Rate: {pred.get('growth_rate_per_day', 0):.2f}% per day
"""
                
                if pred.get("days_until_exhaustion"):
                    report += f"- ⚠️ Exhaustion Date: {pred['exhaustion_date']} ({pred['days_until_exhaustion']:.0f} days)\n"
                else:
                    report += "- ✅ No exhaustion predicted\n"
        
        if "ai_recommendations" in predictions:
            report += "\n## Recommendations\n\n"
            for rec in predictions["ai_recommendations"]:
                report += f"- {rec}\n"
        
        return report


if __name__ == "__main__":
    planner = PredictiveCapacityPlanner()
    
    print("🔮 Running capacity prediction...\n")
    
    report = planner.generate_capacity_report()
    print(report)

