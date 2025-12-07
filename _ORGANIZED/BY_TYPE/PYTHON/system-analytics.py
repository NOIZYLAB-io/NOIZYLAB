#!/usr/bin/env python3
"""
System Analytics - Advanced Analytics for All Systems
====================================================
"""

import sqlite3
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
from pathlib import Path
from rich.console import Console

console = Console()

class SystemAnalytics:
    def __init__(self):
        self.base = Path("/Users/m2ultra/NOIZYLAB")
    
    def get_email_analytics(self):
        """Get email system analytics"""
        db_path = self.base / "email-intelligence/email_intelligence.db"
        
        if not db_path.exists():
            return None
        
        conn = sqlite3.connect(str(db_path))
        
        # Email stats
        df_emails = pd.read_sql_query("SELECT * FROM email_list", conn)
        
        # History stats
        try:
            df_history = pd.read_sql_query("SELECT * FROM email_history", conn)
        except:
            df_history = pd.DataFrame()
        
        # Contacts
        try:
            df_contacts = pd.read_sql_query("SELECT * FROM email_contacts", conn)
        except:
            df_contacts = pd.DataFrame()
        
        conn.close()
        
        return {
            "total_emails": len(df_emails),
            "valid_emails": len(df_emails[df_emails.get('valid', pd.Series([True]*len(df_emails))) == True]) if 'valid' in df_emails.columns else 0,
            "sent_emails": len(df_history[df_history.get('status') == 'sent']) if not df_history.empty else 0,
            "failed_emails": len(df_history[df_history.get('status') == 'failed']) if not df_history.empty else 0,
            "total_contacts": len(df_contacts),
            "email_trends": self._get_email_trends(df_history) if not df_history.empty else []
        }
    
    def _get_email_trends(self, df_history):
        """Get email sending trends"""
        if df_history.empty or 'sent_at' not in df_history.columns:
            return []
        
        df_history['sent_at'] = pd.to_datetime(df_history['sent_at'], errors='coerce')
        daily = df_history.groupby(df_history['sent_at'].dt.date).size()
        
        return [
            {"date": str(date), "count": int(count)}
            for date, count in daily.items()
        ]
    
    def get_system_health(self):
        """Get overall system health"""
        databases = [
            "email-intelligence/email_intelligence.db",
            "security/auth.db",
            "integrations/webhooks.db"
        ]
        
        health = {
            "databases": {},
            "services": {},
            "overall": "healthy"
        }
        
        for db_path in databases:
            full_path = self.base / db_path
            if full_path.exists():
                try:
                    conn = sqlite3.connect(str(full_path))
                    cursor = conn.cursor()
                    cursor.execute("SELECT COUNT(*) FROM sqlite_master")
                    health["databases"][db_path] = "healthy"
                    conn.close()
                except:
                    health["databases"][db_path] = "error"
                    health["overall"] = "warning"
            else:
                health["databases"][db_path] = "missing"
        
        return health
    
    def generate_report(self):
        """Generate comprehensive analytics report"""
        email_analytics = self.get_email_analytics()
        system_health = self.get_system_health()
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "email_system": email_analytics or {},
            "system_health": system_health,
            "summary": {
                "total_emails": email_analytics.get("total_emails", 0) if email_analytics else 0,
                "sent_emails": email_analytics.get("sent_emails", 0) if email_analytics else 0,
                "contacts": email_analytics.get("total_contacts", 0) if email_analytics else 0,
                "health_status": system_health.get("overall", "unknown")
            }
        }
        
        return report

if __name__ == "__main__":
    analytics = SystemAnalytics()
    report = analytics.generate_report()
    console.print("[bold blue]System Analytics Report[/bold blue]")
    console.print(report)

