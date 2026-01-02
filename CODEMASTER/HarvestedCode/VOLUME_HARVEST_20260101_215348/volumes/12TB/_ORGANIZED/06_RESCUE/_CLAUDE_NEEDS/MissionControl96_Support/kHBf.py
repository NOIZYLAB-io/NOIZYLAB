"""
TeamViewer API Client for Mission Control 96
Integrates with TeamViewer Web API for remote support sessions
"""

import requests
import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from dotenv import load_dotenv

load_dotenv()

class TeamViewerClient:
    """TeamViewer API client for managing remote support sessions"""
    
    def __init__(self):
        self.token = os.getenv("TEAMVIEWER_API_TOKEN", "")
        self.base_url = "https://webapi.teamviewer.com/api/v1"
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
    
    def is_configured(self) -> bool:
        """Check if TeamViewer API is properly configured"""
        return bool(self.token and self.token != "...")
    
    def get_account_info(self) -> Dict[str, Any]:
        """Get account information"""
        try:
            response = self.session.get(f"{self.base_url}/account")
            if response.status_code == 200:
                return {
                    "status": "success",
                    "data": response.json(),
                    "configured": True
                }
            else:
                return {
                    "status": "error",
                    "error": f"HTTP {response.status_code}: {response.text}",
                    "configured": False
                }
        except requests.RequestException as e:
            return {
                "status": "error",
                "error": f"Connection failed: {str(e)}",
                "configured": False
            }
    
    def get_devices(self, online_only: bool = False) -> Dict[str, Any]:
        """Get list of devices in the account"""
        try:
            params = {"online_state": "online"} if online_only else {}
            response = self.session.get(f"{self.base_url}/devices", params=params)
            
            if response.status_code == 200:
                devices_data = response.json()
                return {
                    "status": "success",
                    "devices": devices_data.get("devices", []),
                    "total_count": len(devices_data.get("devices", [])),
                    "online_count": len([d for d in devices_data.get("devices", []) if d.get("online_state") == "Online"])
                }
            else:
                return {
                    "status": "error",
                    "error": f"HTTP {response.status_code}: {response.text}"
                }
        except requests.RequestException as e:
            return {
                "status": "error",
                "error": f"Connection failed: {str(e)}"
            }
    
    def get_device_details(self, device_id: str) -> Dict[str, Any]:
        """Get detailed information about a specific device"""
        try:
            response = self.session.get(f"{self.base_url}/devices/{device_id}")
            
            if response.status_code == 200:
                return {
                    "status": "success",
                    "device": response.json()
                }
            else:
                return {
                    "status": "error",
                    "error": f"HTTP {response.status_code}: {response.text}"
                }
        except requests.RequestException as e:
            return {
                "status": "error",
                "error": f"Connection failed: {str(e)}"
            }
    
    def create_session(self, device_id: str, session_type: str = "remote_control") -> Dict[str, Any]:
        """Create a new remote session"""
        try:
            payload = {
                "device_id": device_id,
                "session_type": session_type,  # remote_control, file_transfer, vpn
                "group_id": None  # Optional: assign to specific group
            }
            
            response = self.session.post(f"{self.base_url}/sessions", json=payload)
            
            if response.status_code == 201:
                session_data = response.json()
                return {
                    "status": "success",
                    "session": session_data,
                    "session_id": session_data.get("id"),
                    "session_code": session_data.get("code"),
                    "support_session_token": session_data.get("support_session_token")
                }
            else:
                return {
                    "status": "error",
                    "error": f"HTTP {response.status_code}: {response.text}"
                }
        except requests.RequestException as e:
            return {
                "status": "error",
                "error": f"Connection failed: {str(e)}"
            }
    
    def get_sessions(self, active_only: bool = True) -> Dict[str, Any]:
        """Get list of sessions"""
        try:
            params = {}
            if active_only:
                params["states"] = "open"
            
            response = self.session.get(f"{self.base_url}/sessions", params=params)
            
            if response.status_code == 200:
                sessions_data = response.json()
                return {
                    "status": "success",
                    "sessions": sessions_data.get("sessions", []),
                    "total_count": len(sessions_data.get("sessions", [])),
                    "active_count": len([s for s in sessions_data.get("sessions", []) if s.get("state") == "open"])
                }
            else:
                return {
                    "status": "error",
                    "error": f"HTTP {response.status_code}: {response.text}"
                }
        except requests.RequestException as e:
            return {
                "status": "error",
                "error": f"Connection failed: {str(e)}"
            }
    
    def get_session_details(self, session_id: str) -> Dict[str, Any]:
        """Get detailed information about a specific session"""
        try:
            response = self.session.get(f"{self.base_url}/sessions/{session_id}")
            
            if response.status_code == 200:
                return {
                    "status": "success",
                    "session": response.json()
                }
            else:
                return {
                    "status": "error",
                    "error": f"HTTP {response.status_code}: {response.text}"
                }
        except requests.RequestException as e:
            return {
                "status": "error",
                "error": f"Connection failed: {str(e)}"
            }
    
    def end_session(self, session_id: str) -> Dict[str, Any]:
        """End a remote session"""
        try:
            response = self.session.delete(f"{self.base_url}/sessions/{session_id}")
            
            if response.status_code == 204:
                return {
                    "status": "success",
                    "message": "Session ended successfully"
                }
            else:
                return {
                    "status": "error",
                    "error": f"HTTP {response.status_code}: {response.text}"
                }
        except requests.RequestException as e:
            return {
                "status": "error",
                "error": f"Connection failed: {str(e)}"
            }
    
    def get_groups(self) -> Dict[str, Any]:
        """Get list of device groups"""
        try:
            response = self.session.get(f"{self.base_url}/groups")
            
            if response.status_code == 200:
                groups_data = response.json()
                return {
                    "status": "success",
                    "groups": groups_data.get("groups", []),
                    "total_count": len(groups_data.get("groups", []))
                }
            else:
                return {
                    "status": "error",
                    "error": f"HTTP {response.status_code}: {response.text}"
                }
        except requests.RequestException as e:
            return {
                "status": "error",
                "error": f"Connection failed: {str(e)}"
            }
    
    def create_device_group(self, name: str, policy_id: Optional[str] = None) -> Dict[str, Any]:
        """Create a new device group"""
        try:
            payload = {
                "name": name,
                "policy_id": policy_id
            }
            
            response = self.session.post(f"{self.base_url}/groups", json=payload)
            
            if response.status_code == 201:
                return {
                    "status": "success",
                    "group": response.json()
                }
            else:
                return {
                    "status": "error",
                    "error": f"HTTP {response.status_code}: {response.text}"
                }
        except requests.RequestException as e:
            return {
                "status": "error",
                "error": f"Connection failed: {str(e)}"
            }
    
    def get_connection_reports(self, days: int = 7) -> Dict[str, Any]:
        """Get connection reports for the last N days"""
        try:
            from_date = (datetime.now() - timedelta(days=days)).isoformat()
            to_date = datetime.now().isoformat()
            
            params = {
                "from_date": from_date,
                "to_date": to_date
            }
            
            response = self.session.get(f"{self.base_url}/reports/connections", params=params)
            
            if response.status_code == 200:
                reports_data = response.json()
                return {
                    "status": "success",
                    "reports": reports_data.get("records", []),
                    "total_sessions": len(reports_data.get("records", [])),
                    "date_range": f"{days} days"
                }
            else:
                return {
                    "status": "error",
                    "error": f"HTTP {response.status_code}: {response.text}"
                }
        except requests.RequestException as e:
            return {
                "status": "error",
                "error": f"Connection failed: {str(e)}"
            }
    
    def health_check(self) -> Dict[str, Any]:
        """Perform a comprehensive health check of TeamViewer integration"""
        health_status = {
            "timestamp": datetime.now().isoformat(),
            "api_configured": self.is_configured(),
            "connection_status": "unknown",
            "account_accessible": False,
            "devices_accessible": False,
            "sessions_accessible": False,
            "total_devices": 0,
            "online_devices": 0,
            "active_sessions": 0,
            "last_error": None
        }
        
        if not self.is_configured():
            health_status["last_error"] = "TeamViewer API token not configured"
            return health_status
        
        # Test account access
        account_result = self.get_account_info()
        if account_result["status"] == "success":
            health_status["account_accessible"] = True
            health_status["connection_status"] = "connected"
        else:
            health_status["last_error"] = account_result.get("error", "Account access failed")
            return health_status
        
        # Test devices access
        devices_result = self.get_devices()
        if devices_result["status"] == "success":
            health_status["devices_accessible"] = True
            health_status["total_devices"] = devices_result["total_count"]
            health_status["online_devices"] = devices_result["online_count"]
        
        # Test sessions access
        sessions_result = self.get_sessions()
        if sessions_result["status"] == "success":
            health_status["sessions_accessible"] = True
            health_status["active_sessions"] = sessions_result["active_count"]
        
        return health_status

# Global instance for use in FastAPI endpoints
teamviewer = TeamViewerClient()