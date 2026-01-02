#!/usr/bin/env python3
"""
Slack Analytics Engine
======================
Advanced analytics and insights for Slack integration
"""

import sqlite3
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Any
from pathlib import Path
import pandas as pd
import numpy as np
from collections import defaultdict, Counter


class SlackAnalytics:
    """Advanced analytics for Slack data"""
    
    def __init__(self, db_path: str = None):
        if db_path is None:
            db_path = Path(__file__).parent / "slack_data.db"
        self.db_path = db_path
    
    def get_message_volume_by_hour(self, days: int = 7) -> Dict[int, int]:
        """Get message volume by hour of day"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute(f"""
            SELECT strftime('%H', sent_at) as hour, COUNT(*) as count
            FROM slack_notifications
            WHERE sent_at > datetime('now', '-{days} days')
            GROUP BY hour
            ORDER BY hour
        """)
        
        result = {int(hour): count for hour, count in cursor.fetchall()}
        conn.close()
        
        return result
    
    def get_message_volume_by_day(self, days: int = 30) -> Dict[str, int]:
        """Get message volume by day"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute(f"""
            SELECT DATE(sent_at) as day, COUNT(*) as count
            FROM slack_notifications
            WHERE sent_at > datetime('now', '-{days} days')
            GROUP BY day
            ORDER BY day
        """)
        
        result = {day: count for day, count in cursor.fetchall()}
        conn.close()
        
        return result
    
    def get_top_channels(self, limit: int = 10, days: int = 30) -> List[Tuple[str, int]]:
        """Get most active channels"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute(f"""
            SELECT channel, COUNT(*) as count
            FROM slack_notifications
            WHERE sent_at > datetime('now', '-{days} days')
            GROUP BY channel
            ORDER BY count DESC
            LIMIT {limit}
        """)
        
        result = cursor.fetchall()
        conn.close()
        
        return result
    
    def get_notification_types(self, days: int = 30) -> Dict[str, int]:
        """Get breakdown of notification types"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute(f"""
            SELECT notification_type, COUNT(*) as count
            FROM slack_notifications
            WHERE sent_at > datetime('now', '-{days} days')
            GROUP BY notification_type
            ORDER BY count DESC
        """)
        
        result = {ntype: count for ntype, count in cursor.fetchall()}
        conn.close()
        
        return result
    
    def get_success_rate(self, days: int = 30) -> Dict[str, Any]:
        """Calculate notification success rate"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute(f"""
            SELECT 
                COUNT(*) as total,
                SUM(CASE WHEN status = 'sent' THEN 1 ELSE 0 END) as successful,
                SUM(CASE WHEN status = 'failed' THEN 1 ELSE 0 END) as failed
            FROM slack_notifications
            WHERE sent_at > datetime('now', '-{days} days')
        """)
        
        total, successful, failed = cursor.fetchone()
        conn.close()
        
        success_rate = (successful / total * 100) if total > 0 else 0
        
        return {
            "total": total,
            "successful": successful,
            "failed": failed,
            "success_rate": success_rate
        }
    
    def get_peak_hours(self, days: int = 7) -> List[Tuple[int, int]]:
        """Get peak usage hours"""
        hourly = self.get_message_volume_by_hour(days)
        sorted_hours = sorted(hourly.items(), key=lambda x: x[1], reverse=True)
        return sorted_hours[:5]
    
    def get_user_activity(self, limit: int = 10) -> List[Tuple[str, int]]:
        """Get most active users (from commands)"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute(f"""
            SELECT user_name, COUNT(*) as count
            FROM slack_commands
            WHERE user_name IS NOT NULL
            GROUP BY user_name
            ORDER BY count DESC
            LIMIT {limit}
        """)
        
        result = cursor.fetchall()
        conn.close()
        
        return result
    
    def get_command_usage(self) -> Dict[str, int]:
        """Get command usage statistics"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT command, COUNT(*) as count
            FROM slack_commands
            GROUP BY command
            ORDER BY count DESC
        """)
        
        result = {cmd: count for cmd, count in cursor.fetchall()}
        conn.close()
        
        return result
    
    def get_growth_trend(self, days: int = 30) -> Dict[str, float]:
        """Calculate growth trend"""
        daily_volume = self.get_message_volume_by_day(days)
        
        if len(daily_volume) < 2:
            return {"trend": 0.0, "direction": "stable"}
        
        values = list(daily_volume.values())
        
        # Simple linear regression
        x = np.arange(len(values))
        y = np.array(values)
        
        if len(x) > 0:
            slope, intercept = np.polyfit(x, y, 1)
            
            direction = "increasing" if slope > 0 else "decreasing" if slope < 0 else "stable"
            
            return {
                "trend": float(slope),
                "direction": direction,
                "current_avg": float(np.mean(values[-7:])) if len(values) >= 7 else float(np.mean(values))
            }
        
        return {"trend": 0.0, "direction": "stable"}
    
    def get_channel_health(self) -> List[Dict[str, Any]]:
        """Analyze channel health and activity"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT 
                c.name,
                c.member_count,
                COUNT(n.id) as message_count,
                MAX(n.sent_at) as last_activity
            FROM slack_channels c
            LEFT JOIN slack_notifications n ON c.name = REPLACE(n.channel, '#', '')
            GROUP BY c.name
            ORDER BY message_count DESC
        """)
        
        channels = []
        for name, members, messages, last_activity in cursor.fetchall():
            # Calculate activity score
            days_since_activity = 999
            if last_activity:
                last_dt = datetime.fromisoformat(last_activity)
                days_since_activity = (datetime.now() - last_dt).days
            
            activity_score = "active" if days_since_activity < 7 else "moderate" if days_since_activity < 30 else "inactive"
            
            channels.append({
                "name": name,
                "members": members,
                "messages": messages,
                "last_activity": last_activity,
                "days_since_activity": days_since_activity,
                "activity_score": activity_score
            })
        
        conn.close()
        return channels
    
    def generate_report(self, days: int = 7) -> Dict[str, Any]:
        """Generate comprehensive analytics report"""
        return {
            "period": f"Last {days} days",
            "generated_at": datetime.now().isoformat(),
            "overview": self.get_success_rate(days),
            "top_channels": self.get_top_channels(10, days),
            "notification_types": self.get_notification_types(days),
            "peak_hours": self.get_peak_hours(days),
            "user_activity": self.get_user_activity(10),
            "command_usage": self.get_command_usage(),
            "growth_trend": self.get_growth_trend(days),
            "hourly_distribution": self.get_message_volume_by_hour(days),
            "daily_volume": self.get_message_volume_by_day(days)
        }
    
    def get_anomalies(self, days: int = 7) -> List[Dict[str, Any]]:
        """Detect usage anomalies"""
        hourly = self.get_message_volume_by_hour(days)
        
        if not hourly:
            return []
        
        values = list(hourly.values())
        mean = np.mean(values)
        std = np.std(values)
        
        anomalies = []
        for hour, count in hourly.items():
            z_score = (count - mean) / std if std > 0 else 0
            
            if abs(z_score) > 2:  # 2 standard deviations
                anomalies.append({
                    "hour": hour,
                    "count": count,
                    "z_score": float(z_score),
                    "type": "spike" if z_score > 0 else "drop"
                })
        
        return anomalies
    
    def predict_next_hour_volume(self) -> int:
        """Simple prediction for next hour's volume"""
        hourly = self.get_message_volume_by_hour(7)
        
        current_hour = datetime.now().hour
        
        # Get average for this hour over past week
        if current_hour in hourly:
            return hourly[current_hour]
        
        # Return overall average
        return int(np.mean(list(hourly.values()))) if hourly else 0


class NetworkAnalytics:
    """Advanced analytics for network monitoring"""
    
    def __init__(self, db_path: str = None):
        if db_path is None:
            db_path = Path("/Users/m2ultra/NOIZYLAB/network/network_devices.db")
        self.db_path = db_path
    
    def get_handshake_success_rate(self, days: int = 7) -> Dict[str, Any]:
        """Calculate handshake success rate"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute(f"""
            SELECT 
                COUNT(*) as total,
                SUM(CASE WHEN success = 1 THEN 1 ELSE 0 END) as successful,
                AVG(CASE WHEN success = 1 THEN response_time ELSE NULL END) as avg_response_time
            FROM handshake_log
            WHERE timestamp > datetime('now', '-{days} days')
        """)
        
        total, successful, avg_time = cursor.fetchone()
        conn.close()
        
        success_rate = (successful / total * 100) if total > 0 else 0
        
        return {
            "total": total or 0,
            "successful": successful or 0,
            "failed": (total - successful) if total else 0,
            "success_rate": success_rate,
            "avg_response_time": avg_time or 0
        }
    
    def get_handshake_by_type(self, days: int = 7) -> Dict[str, Dict[str, int]]:
        """Get handshake statistics by type"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute(f"""
            SELECT 
                handshake_type,
                COUNT(*) as total,
                SUM(CASE WHEN success = 1 THEN 1 ELSE 0 END) as successful
            FROM handshake_log
            WHERE timestamp > datetime('now', '-{days} days')
            GROUP BY handshake_type
            ORDER BY total DESC
        """)
        
        result = {}
        for htype, total, successful in cursor.fetchall():
            result[htype] = {
                "total": total,
                "successful": successful,
                "failed": total - successful,
                "success_rate": (successful / total * 100) if total > 0 else 0
            }
        
        conn.close()
        return result
    
    def get_device_activity(self, days: int = 30) -> List[Dict[str, Any]]:
        """Get device activity timeline"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute(f"""
            SELECT 
                mac_address,
                hostname,
                COUNT(*) as connections,
                MAX(timestamp) as last_seen
            FROM port_events
            WHERE timestamp > datetime('now', '-{days} days')
            AND event_type = 'link_up'
            GROUP BY mac_address
            ORDER BY connections DESC
        """)
        
        devices = []
        for mac, hostname, connections, last_seen in cursor.fetchall():
            devices.append({
                "mac_address": mac,
                "hostname": hostname or "Unknown",
                "connections": connections,
                "last_seen": last_seen
            })
        
        conn.close()
        return devices
    
    def get_port_utilization(self) -> Dict[int, Dict[str, Any]]:
        """Analyze port utilization patterns"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        result = {}
        for port in range(1, 11):
            cursor.execute("""
                SELECT 
                    COUNT(*) as events,
                    SUM(CASE WHEN event_type = 'link_up' THEN 1 ELSE 0 END) as connections
                FROM port_events
                WHERE port = ?
            """, (port,))
            
            events, connections = cursor.fetchone()
            
            result[port] = {
                "total_events": events or 0,
                "connections": connections or 0,
                "utilization": "high" if connections > 10 else "medium" if connections > 5 else "low"
            }
        
        conn.close()
        return result
    
    def get_mc96_performance(self) -> Dict[str, Any]:
        """Get MC96-specific performance metrics"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT 
                COUNT(*) as total,
                AVG(response_time) as avg_response_time,
                MIN(response_time) as min_response_time,
                MAX(response_time) as max_response_time
            FROM handshake_log
            WHERE handshake_type = 'mc96'
            AND success = 1
        """)
        
        total, avg_time, min_time, max_time = cursor.fetchone()
        
        cursor.execute("""
            SELECT COUNT(*) FROM mc96_devices WHERE status = 'active'
        """)
        
        active_devices = cursor.fetchone()[0]
        
        conn.close()
        
        return {
            "total_handshakes": total or 0,
            "active_devices": active_devices or 0,
            "avg_response_time": avg_time or 0,
            "min_response_time": min_time or 0,
            "max_response_time": max_time or 0,
            "performance": "excellent" if avg_time and avg_time < 3 else "good" if avg_time and avg_time < 5 else "needs_improvement"
        }
    
    def generate_report(self, days: int = 7) -> Dict[str, Any]:
        """Generate comprehensive network analytics report"""
        return {
            "period": f"Last {days} days",
            "generated_at": datetime.now().isoformat(),
            "handshake_stats": self.get_handshake_success_rate(days),
            "handshake_by_type": self.get_handshake_by_type(days),
            "device_activity": self.get_device_activity(days),
            "port_utilization": self.get_port_utilization(),
            "mc96_performance": self.get_mc96_performance()
        }


if __name__ == "__main__":
    # Test analytics
    print("📊 Slack Analytics")
    print("=" * 50)
    
    slack_analytics = SlackAnalytics()
    report = slack_analytics.generate_report(7)
    
    print(f"\nOverview:")
    print(f"  Total: {report['overview']['total']}")
    print(f"  Success Rate: {report['overview']['success_rate']:.1f}%")
    
    print(f"\nTop Channels:")
    for channel, count in report['top_channels'][:5]:
        print(f"  {channel}: {count} messages")
    
    print(f"\n\n📊 Network Analytics")
    print("=" * 50)
    
    network_analytics = NetworkAnalytics()
    net_report = network_analytics.generate_report(7)
    
    print(f"\nHandshake Stats:")
    print(f"  Total: {net_report['handshake_stats']['total']}")
    print(f"  Success Rate: {net_report['handshake_stats']['success_rate']:.1f}%")
    print(f"  Avg Response: {net_report['handshake_stats']['avg_response_time']:.2f}s")
    
    print(f"\nMC96 Performance:")
    mc96 = net_report['mc96_performance']
    print(f"  Active Devices: {mc96['active_devices']}")
    print(f"  Avg Response: {mc96['avg_response_time']:.2f}s")
    print(f"  Performance: {mc96['performance']}")

