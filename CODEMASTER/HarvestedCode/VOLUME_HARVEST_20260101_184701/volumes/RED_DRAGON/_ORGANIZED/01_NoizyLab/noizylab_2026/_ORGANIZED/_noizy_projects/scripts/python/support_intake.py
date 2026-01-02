"""
AI Support Intake System for Mission Control 96
Handles client submissions via info@noizyfish.com with image analysis and voice transcription
"""

import os
import json
import base64
import uuid
import tempfile
import mimetypes
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from enum import Enum
import requests
from dotenv import load_dotenv

load_dotenv()

class IssueCategory(Enum):
    HARDWARE = "hardware"
    SOFTWARE = "software"
    NETWORK = "network"
    SECURITY = "security"
    PERFORMANCE = "performance"
    USER_ERROR = "user_error"
    UNKNOWN = "unknown"

class IssuePriority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class SupportTicketStatus(Enum):
    SUBMITTED = "submitted"
    ANALYZING = "analyzing"
    CATEGORIZED = "categorized"
    ASSIGNED = "assigned"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"

@dataclass
class SupportTicket:
    """Represents a client support ticket"""
    id: str
    client_email: str
    client_name: Optional[str]
    submitted_at: datetime
    status: SupportTicketStatus
    category: IssueCategory
    priority: IssuePriority
    title: str
    description: str
    voice_transcription: Optional[str]
    image_analysis: Optional[Dict[str, Any]]
    ai_recommendations: Optional[Dict[str, Any]]
    attachments: List[Dict[str, str]]
    resolution_notes: Optional[str]
    assigned_to: Optional[str]
    resolved_at: Optional[datetime]

class AIAnalysisEngine:
    """AI engine for analyzing support requests"""
    
    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY", "")
        self.elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY", "")
        
    def transcribe_voice_message(self, audio_file_path: str) -> Dict[str, Any]:
        """Transcribe voice message using OpenAI Whisper"""
        try:
            if not self.openai_api_key or self.openai_api_key == "...":
                return {
                    "success": False,
                    "error": "OpenAI API key not configured",
                    "transcription": "Voice transcription unavailable - API not configured"
                }
            
            headers = {
                "Authorization": f"Bearer {self.openai_api_key}"
            }
            
            with open(audio_file_path, 'rb') as audio_file:
                files = {
                    'file': audio_file,
                    'model': (None, 'whisper-1'),
                    'response_format': (None, 'json')
                }
                
                response = requests.post(
                    "https://api.openai.com/v1/audio/transcriptions",
                    headers=headers,
                    files=files,
                    timeout=30
                )
            
            if response.status_code == 200:
                result = response.json()
                return {
                    "success": True,
                    "transcription": result.get("text", ""),
                    "language": result.get("language", "unknown")
                }
            else:
                return {
                    "success": False,
                    "error": f"OpenAI API error: {response.status_code}",
                    "transcription": "Voice transcription failed"
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "transcription": "Voice transcription failed due to technical error"
            }
    
    def analyze_image(self, image_file_path: str) -> Dict[str, Any]:
        """Analyze image using OpenAI Vision API"""
        try:
            if not self.openai_api_key or self.openai_api_key == "...":
                return {
                    "success": False,
                    "error": "OpenAI API key not configured",
                    "analysis": "Image analysis unavailable - API not configured"
                }
            
            # Read and encode image
            with open(image_file_path, 'rb') as image_file:
                image_data = base64.b64encode(image_file.read()).decode('utf-8')
            
            # Determine image type
            mime_type, _ = mimetypes.guess_type(image_file_path)
            if not mime_type or not mime_type.startswith('image/'):
                mime_type = 'image/jpeg'
            
            headers = {
                "Authorization": f"Bearer {self.openai_api_key}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": "gpt-4-vision-preview",
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": """Analyze this image for technical support purposes. Identify:
1. What type of device or screen is shown
2. Any visible error messages or issues
3. Hardware problems (physical damage, wear, etc.)
4. Software problems (error dialogs, interface issues, etc.)
5. Specific recommendations for fixing the issue
6. Whether this appears to be a hardware or software problem
7. Estimated severity level (low, medium, high, critical)

Provide a detailed technical analysis suitable for IT support."""
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:{mime_type};base64,{image_data}"
                                }
                            }
                        ]
                    }
                ],
                "max_tokens": 500
            }
            
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                analysis_text = result.get("choices", [{}])[0].get("message", {}).get("content", "")
                
                return {
                    "success": True,
                    "analysis": analysis_text,
                    "model_used": "gpt-4-vision-preview"
                }
            else:
                return {
                    "success": False,
                    "error": f"OpenAI Vision API error: {response.status_code}",
                    "analysis": "Image analysis failed"
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "analysis": "Image analysis failed due to technical error"
            }
    
    def categorize_issue(self, description: str, voice_transcription: str = "", image_analysis: str = "") -> Dict[str, Any]:
        """Categorize issue using AI analysis"""
        try:
            if not self.openai_api_key or self.openai_api_key == "...":
                return self._fallback_categorization(description, voice_transcription, image_analysis)
            
            # Combine all available information
            combined_text = f"""
            Description: {description}
            Voice Transcription: {voice_transcription}
            Image Analysis: {image_analysis}
            """
            
            headers = {
                "Authorization": f"Bearer {self.openai_api_key}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": "gpt-4",
                "messages": [
                    {
                        "role": "system",
                        "content": """You are an expert IT support categorization system. Analyze the provided information and categorize the issue.

Categories:
- HARDWARE: Physical components, damage, connectivity issues, peripheral problems
- SOFTWARE: Applications, OS issues, drivers, updates, crashes
- NETWORK: Internet, WiFi, connectivity, DNS, routing issues  
- SECURITY: Malware, viruses, unauthorized access, data breaches
- PERFORMANCE: Slow performance, high CPU/memory usage, optimization
- USER_ERROR: Misunderstanding, training needed, user mistakes
- UNKNOWN: Cannot determine from available information

Priority Levels:
- CRITICAL: System down, data loss, security breach
- HIGH: Major functionality affected, many users impacted
- MEDIUM: Some functionality affected, workarounds available
- LOW: Minor issues, cosmetic problems, feature requests

Also provide:
1. Specific fix recommendations (remote vs local)
2. Estimated resolution time
3. Required tools or access level
4. Step-by-step resolution plan

Return a JSON response with: category, priority, confidence_score (0-100), recommendations, resolution_plan, remote_fixable (true/false)"""
                    },
                    {
                        "role": "user",
                        "content": combined_text
                    }
                ],
                "max_tokens": 600,
                "temperature": 0.3
            }
            
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                ai_response = result.get("choices", [{}])[0].get("message", {}).get("content", "")
                
                # Try to parse JSON response
                try:
                    categorization = json.loads(ai_response)
                except json.JSONDecodeError:
                    # Fallback if AI doesn't return valid JSON
                    categorization = self._parse_ai_response(ai_response)
                
                return {
                    "success": True,
                    "categorization": categorization,
                    "raw_response": ai_response
                }
            else:
                return self._fallback_categorization(description, voice_transcription, image_analysis)
                
        except Exception as e:
            return self._fallback_categorization(description, voice_transcription, image_analysis)
    
    def _fallback_categorization(self, description: str, voice_transcription: str = "", image_analysis: str = "") -> Dict[str, Any]:
        """Fallback categorization using keyword analysis"""
        combined_text = f"{description} {voice_transcription} {image_analysis}".lower()
        
        # Hardware keywords
        hardware_keywords = [
            "broken", "cracked", "damaged", "screen", "display", "keyboard", "mouse",
            "power", "battery", "charging", "connector", "cable", "port", "usb",
            "hard drive", "disk", "memory", "ram", "cpu", "fan", "overheating",
            "physical", "drop", "spill", "liquid", "hardware"
        ]
        
        # Software keywords  
        software_keywords = [
            "crash", "freeze", "hang", "error message", "blue screen", "update",
            "install", "application", "program", "software", "driver", "boot",
            "startup", "login", "password", "corrupt", "virus", "malware"
        ]
        
        # Network keywords
        network_keywords = [
            "internet", "wifi", "network", "connection", "dns", "router",
            "ethernet", "bandwidth", "slow internet", "can't connect"
        ]
        
        # Count keyword matches
        hardware_score = sum(1 for keyword in hardware_keywords if keyword in combined_text)
        software_score = sum(1 for keyword in software_keywords if keyword in combined_text)
        network_score = sum(1 for keyword in network_keywords if keyword in combined_text)
        
        # Determine category
        if hardware_score > software_score and hardware_score > network_score:
            category = "HARDWARE"
            confidence = min(90, hardware_score * 15)
        elif network_score > software_score and network_score > hardware_score:
            category = "NETWORK" 
            confidence = min(90, network_score * 15)
        elif software_score > 0:
            category = "SOFTWARE"
            confidence = min(90, software_score * 15)
        else:
            category = "UNKNOWN"
            confidence = 30
        
        # Determine priority
        critical_keywords = ["won't turn on", "data loss", "security breach", "hacked"]
        high_keywords = ["can't work", "urgent", "important", "deadline"]
        
        if any(keyword in combined_text for keyword in critical_keywords):
            priority = "CRITICAL"
        elif any(keyword in combined_text for keyword in high_keywords):
            priority = "HIGH"
        elif hardware_score > 0:
            priority = "MEDIUM"  # Hardware issues often need physical attention
        else:
            priority = "LOW"
        
        return {
            "success": True,
            "categorization": {
                "category": category,
                "priority": priority,
                "confidence_score": confidence,
                "recommendations": [
                    "Issue categorized using keyword analysis",
                    "Manual review recommended for accurate assessment",
                    "Consider requesting additional information from client"
                ],
                "resolution_plan": [
                    "1. Review client submission details",
                    "2. Contact client for clarification if needed",
                    "3. Assign to appropriate technician",
                    "4. Determine remote vs on-site resolution"
                ],
                "remote_fixable": category in ["SOFTWARE", "NETWORK"]
            },
            "fallback_used": True
        }
    
    def _parse_ai_response(self, response: str) -> Dict[str, Any]:
        """Parse AI response when JSON parsing fails"""
        # Extract key information using simple parsing
        category = "UNKNOWN"
        priority = "MEDIUM"
        
        if "HARDWARE" in response.upper():
            category = "HARDWARE"
        elif "SOFTWARE" in response.upper():
            category = "SOFTWARE"
        elif "NETWORK" in response.upper():
            category = "NETWORK"
        elif "SECURITY" in response.upper():
            category = "SECURITY"
        elif "PERFORMANCE" in response.upper():
            category = "PERFORMANCE"
        
        if "CRITICAL" in response.upper():
            priority = "CRITICAL"
        elif "HIGH" in response.upper():
            priority = "HIGH"
        elif "LOW" in response.upper():
            priority = "LOW"
        
        return {
            "category": category,
            "priority": priority,
            "confidence_score": 70,
            "recommendations": ["AI analysis completed", "Manual review recommended"],
            "resolution_plan": ["Review and assign to technician"],
            "remote_fixable": "remote" in response.lower()
        }

class SupportTicketManager:
    """Manages support tickets and AI analysis"""
    
    def __init__(self):
        self.tickets: Dict[str, SupportTicket] = {}
        self.ai_engine = AIAnalysisEngine()
        self.upload_directory = "/tmp/mc96_uploads"
        
        # Create upload directory if it doesn't exist
        os.makedirs(self.upload_directory, exist_ok=True)
    
    def create_ticket(self, client_email: str, client_name: str, description: str,
                     voice_file: Optional[str] = None, image_files: Optional[List[str]] = None) -> str:
        """Create a new support ticket"""
        ticket_id = f"MC96-{uuid.uuid4().hex[:8].upper()}"
        
        # Initialize ticket
        ticket = SupportTicket(
            id=ticket_id,
            client_email=client_email,
            client_name=client_name,
            submitted_at=datetime.now(),
            status=SupportTicketStatus.SUBMITTED,
            category=IssueCategory.UNKNOWN,
            priority=IssuePriority.MEDIUM,
            title=f"Support Request - {ticket_id}",
            description=description,
            voice_transcription=None,
            image_analysis=None,
            ai_recommendations=None,
            attachments=[],
            resolution_notes=None,
            assigned_to=None,
            resolved_at=None
        )
        
        self.tickets[ticket_id] = ticket
        
        # Process attachments asynchronously
        self._process_ticket_async(ticket_id, voice_file, image_files or [])
        
        return ticket_id
    
    def _process_ticket_async(self, ticket_id: str, voice_file: Optional[str], image_files: List[str]):
        """Process ticket attachments and AI analysis"""
        import threading
        
        def process():
            ticket = self.tickets[ticket_id]
            ticket.status = SupportTicketStatus.ANALYZING
            
            voice_transcription = ""
            image_analysis = ""
            
            # Process voice file
            if voice_file:
                voice_result = self.ai_engine.transcribe_voice_message(voice_file)
                if voice_result["success"]:
                    voice_transcription = voice_result["transcription"]
                    ticket.voice_transcription = voice_transcription
                    ticket.attachments.append({
                        "type": "voice",
                        "filename": os.path.basename(voice_file),
                        "transcription": voice_transcription
                    })
            
            # Process image files
            for image_file in image_files:
                image_result = self.ai_engine.analyze_image(image_file)
                if image_result["success"]:
                    image_analysis += f"\n{image_result['analysis']}"
                    ticket.attachments.append({
                        "type": "image",
                        "filename": os.path.basename(image_file),
                        "analysis": image_result["analysis"]
                    })
            
            ticket.image_analysis = {"combined_analysis": image_analysis.strip()}
            
            # Categorize issue
            categorization_result = self.ai_engine.categorize_issue(
                ticket.description, voice_transcription, image_analysis
            )
            
            if categorization_result["success"]:
                cat_data = categorization_result["categorization"]
                ticket.category = IssueCategory(cat_data["category"].lower())
                ticket.priority = IssuePriority(cat_data["priority"].lower())
                ticket.ai_recommendations = cat_data
                ticket.title = f"{cat_data['category']} Issue - {ticket_id}"
            
            ticket.status = SupportTicketStatus.CATEGORIZED
        
        thread = threading.Thread(target=process)
        thread.daemon = True
        thread.start()
    
    def get_ticket(self, ticket_id: str) -> Optional[Dict[str, Any]]:
        """Get ticket details"""
        ticket = self.tickets.get(ticket_id)
        if ticket:
            return asdict(ticket)
        return None
    
    def get_tickets(self, status: Optional[SupportTicketStatus] = None,
                   category: Optional[IssueCategory] = None) -> List[Dict[str, Any]]:
        """Get list of tickets with optional filtering"""
        tickets = list(self.tickets.values())
        
        if status:
            tickets = [t for t in tickets if t.status == status]
        
        if category:
            tickets = [t for t in tickets if t.category == category]
        
        # Sort by submission time (newest first)
        tickets.sort(key=lambda t: t.submitted_at, reverse=True)
        
        return [asdict(t) for t in tickets]
    
    def update_ticket_status(self, ticket_id: str, status: SupportTicketStatus,
                           notes: Optional[str] = None, assigned_to: Optional[str] = None) -> bool:
        """Update ticket status"""
        ticket = self.tickets.get(ticket_id)
        if not ticket:
            return False
        
        ticket.status = status
        
        if notes:
            ticket.resolution_notes = notes
        
        if assigned_to:
            ticket.assigned_to = assigned_to
        
        if status == SupportTicketStatus.RESOLVED:
            ticket.resolved_at = datetime.now()
        
        return True
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get support ticket statistics"""
        total_tickets = len(self.tickets)
        
        # Count by status
        status_counts = {}
        for status in SupportTicketStatus:
            status_counts[status.value] = len([t for t in self.tickets.values() if t.status == status])
        
        # Count by category
        category_counts = {}
        for category in IssueCategory:
            category_counts[category.value] = len([t for t in self.tickets.values() if t.category == category])
        
        # Count by priority
        priority_counts = {}
        for priority in IssuePriority:
            priority_counts[priority.value] = len([t for t in self.tickets.values() if t.priority == priority])
        
        return {
            "total_tickets": total_tickets,
            "status_counts": status_counts,
            "category_counts": category_counts,
            "priority_counts": priority_counts,
            "ai_engine_configured": bool(self.ai_engine.openai_api_key and self.ai_engine.openai_api_key != "...")
        }

# Global support ticket manager
support_manager = SupportTicketManager()