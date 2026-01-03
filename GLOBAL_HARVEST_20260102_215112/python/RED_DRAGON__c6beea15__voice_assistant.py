"""
AI Voice Assistant for Support Intake - Mission Control 96
Uses ElevenLabs Sarah voice to guide clients and promote Noizyfish.com
"""

import os
import requests
import base64
import tempfile
from datetime import datetime
from typing import Dict, List, Any, Optional
from dotenv import load_dotenv

load_dotenv()

class VoiceAssistant:
    """AI Voice Assistant using ElevenLabs Sarah voice"""
    
    def __init__(self):
        self.elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY", "")
        self.voice_id = os.getenv("ELEVENLABS_VOICE", "Sarah")
        self.model = os.getenv("ELEVENLABS_MODEL", "eleven_turbo_v2")
        self.base_url = "https://api.elevenlabs.io/v1"
        
    def is_configured(self) -> bool:
        """Check if ElevenLabs is properly configured"""
        return bool(self.elevenlabs_api_key and self.elevenlabs_api_key != "...")
    
    def generate_voice_response(self, text: str, voice_settings: Optional[Dict] = None) -> Dict[str, Any]:
        """Generate voice response using ElevenLabs"""
        try:
            if not self.is_configured():
                return {
                    "success": False,
                    "error": "ElevenLabs API not configured",
                    "audio_url": None
                }
            
            # Default voice settings for Sarah
            if voice_settings is None:
                voice_settings = {
                    "stability": 0.5,
                    "similarity_boost": 0.8,
                    "style": 0.2,
                    "use_speaker_boost": True
                }
            
            headers = {
                "Accept": "audio/mpeg",
                "Content-Type": "application/json",
                "xi-api-key": self.elevenlabs_api_key
            }
            
            data = {
                "text": text,
                "model_id": self.model,
                "voice_settings": voice_settings
            }
            
            response = requests.post(
                f"{self.base_url}/text-to-speech/{self.voice_id}",
                json=data,
                headers=headers,
                timeout=30
            )
            
            if response.status_code == 200:
                # Save audio to temporary file
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
                    temp_file.write(response.content)
                    audio_path = temp_file.name
                
                # Convert to base64 for web delivery
                audio_base64 = base64.b64encode(response.content).decode('utf-8')
                
                return {
                    "success": True,
                    "audio_path": audio_path,
                    "audio_base64": audio_base64,
                    "audio_url": f"data:audio/mpeg;base64,{audio_base64}",
                    "text": text
                }
            else:
                return {
                    "success": False,
                    "error": f"ElevenLabs API error: {response.status_code}",
                    "audio_url": None
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "audio_url": None
            }

class AutoReplySystem:
    """Intelligent auto-reply system for support emails"""
    
    def __init__(self):
        self.voice_assistant = VoiceAssistant()
        self.conversation_flows = self._initialize_conversation_flows()
    
    def _initialize_conversation_flows(self) -> Dict[str, Dict[str, Any]]:
        """Initialize conversation flow templates"""
        return {
            "welcome": {
                "text": """Hi there! I'm Sarah, your AI assistant from Noizyfish Support. Thank you for reaching out to us at info@noizyfish.com. 

I'm here to help you get the best possible support for your technical issue. To provide you with the most accurate assistance, I'll need to gather some information from you.

Please listen carefully to the following prompts and provide as much detail as possible. This will help our expert technicians resolve your issue quickly and efficiently.""",
                "next_prompts": ["issue_description", "device_info", "subscription_offer"]
            },
            
            "issue_description": {
                "text": """First, please describe your technical issue in detail. You can either type your response or record a voice message. 

Be specific about:
- What exactly is happening?
- When did the problem start?
- What were you doing when it occurred?
- Have you tried any troubleshooting steps?

If you have any photos or screenshots of the issue, please attach them as well. Visual information helps our technicians understand the problem much faster.""",
                "next_prompts": ["device_info"]
            },
            
            "device_info": {
                "text": """Great! Now I need some information about your device:

- What type of device are you using? (Mac, PC, iPhone, iPad, etc.)
- What operating system version?
- When did you last restart or update your device?

This information helps us determine whether your issue is hardware-related, like a physical component problem, or software-related, like an application or system issue.""",
                "next_prompts": ["urgency_assessment", "subscription_offer"]
            },
            
            "urgency_assessment": {
                "text": """To prioritize your support request appropriately:

Is this issue preventing you from working or causing significant disruption? 
- Critical: System completely down, can't work at all
- High: Major features affected, impacting productivity  
- Medium: Some functionality lost, but workarounds available
- Low: Minor inconvenience or cosmetic issue

Please let me know the urgency level so we can respond accordingly.""",
                "next_prompts": ["subscription_offer", "next_steps"]
            },
            
            "subscription_offer": {
                "text": """Before we proceed, I'd love to tell you about Noizyfish.com - your gateway to premium technical support and exclusive services!

As a Noizyfish subscriber, you'll get:
- Priority support with faster response times
- Access to our premium diagnostic tools
- Exclusive tutorials and tech tips
- Remote support sessions with certified technicians
- Monthly tech health check-ups for your devices

Visit Noizyfish.com today and use code SUPPORT20 for 20% off your first month! 

Our premium subscribers get issues resolved 3x faster on average. Would you like me to help you sign up right now?""",
                "next_prompts": ["next_steps", "subscription_benefits"]
            },
            
            "subscription_benefits": {
                "text": """Let me tell you more about what makes Noizyfish.com special:

🚀 Instant Access: Get help the moment you need it
🔧 Expert Technicians: Certified professionals with years of experience  
📱 Multi-Device Support: We handle Mac, PC, iPhone, iPad, and more
🔒 Secure & Private: Your data stays protected with enterprise-grade security
💡 Proactive Care: We prevent problems before they happen

Plus, subscribers get access to our exclusive Mission Control dashboard where you can track all your devices, schedule maintenance, and get predictive insights about potential issues.

Ready to upgrade your tech support experience?""",
                "next_prompts": ["next_steps"]
            },
            
            "next_steps": {
                "text": """Perfect! Here's what happens next:

1. Our AI system will analyze your issue and categorize it as hardware or software
2. We'll assign the right specialist to your case
3. You'll receive a detailed action plan within 2 hours
4. For urgent issues, we can start a remote session immediately

Your support ticket number is MC96-[TICKET_ID]. Please keep this for your records.

If you're a Noizyfish subscriber, you'll get priority handling. If not, there's still time to upgrade for faster service!

Thank you for choosing Noizyfish Support. We'll have you back up and running in no time!""",
                "next_prompts": []
            },
            
            "hardware_detected": {
                "text": """Based on your description, this appears to be a hardware-related issue. This typically means there's a problem with a physical component of your device.

Hardware issues often require:
- Physical inspection of the device
- Potential component replacement
- On-site or in-store service

Don't worry - as a Noizyfish subscriber, you get access to our network of certified repair partners with discounted rates. We'll coordinate everything for you.

For non-subscribers, we can still help connect you with trusted repair services in your area.""",
                "next_prompts": ["next_steps"]
            },
            
            "software_detected": {
                "text": """Good news! This looks like a software issue, which means we can likely fix it remotely without any physical repairs needed.

Software issues can often be resolved through:
- System updates or patches
- Application reinstallation
- Configuration adjustments
- Remote troubleshooting sessions

This is perfect for our remote support service! Noizyfish subscribers can get immediate screen sharing sessions with our technicians. We'll fix it while you watch, and explain what we're doing so you can prevent it in the future.""",
                "next_prompts": ["next_steps"]
            }
        }
    
    def generate_auto_reply(self, context: str = "welcome", client_email: str = "", 
                          issue_details: Dict[str, Any] = None) -> Dict[str, Any]:
        """Generate intelligent auto-reply with voice"""
        try:
            # Get the appropriate conversation flow
            flow = self.conversation_flows.get(context, self.conversation_flows["welcome"])
            
            # Personalize the message if we have client info
            reply_text = flow["text"]
            if issue_details and "[TICKET_ID]" in reply_text:
                ticket_id = issue_details.get("ticket_id", "PENDING")
                reply_text = reply_text.replace("[TICKET_ID]", ticket_id)
            
            # Generate voice response
            voice_response = self.voice_assistant.generate_voice_response(reply_text)
            
            # Create comprehensive reply
            auto_reply = {
                "timestamp": datetime.now().isoformat(),
                "context": context,
                "text_response": reply_text,
                "voice_response": voice_response,
                "next_prompts": flow.get("next_prompts", []),
                "client_email": client_email,
                "html_response": self._generate_html_response(reply_text, voice_response, context),
                "suggested_actions": self._get_suggested_actions(context)
            }
            
            return auto_reply
            
        except Exception as e:
            return {
                "error": f"Auto-reply generation failed: {str(e)}",
                "timestamp": datetime.now().isoformat()
            }
    
    def _generate_html_response(self, text: str, voice_response: Dict[str, Any], context: str) -> str:
        """Generate HTML email response with embedded audio"""
        audio_player = ""
        if voice_response.get("success") and voice_response.get("audio_url"):
            audio_player = f"""
            <div style="margin: 20px 0; padding: 15px; background: #f0f8ff; border-radius: 8px; border-left: 4px solid #007bff;">
                <h4 style="color: #007bff; margin: 0 0 10px 0;">🎧 Listen to Sarah's Voice Message:</h4>
                <audio controls style="width: 100%;">
                    <source src="{voice_response['audio_url']}" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
                <p style="font-size: 12px; color: #666; margin: 5px 0 0 0;">
                    Can't hear the audio? The message is also written below.
                </p>
            </div>
            """
        
        subscription_cta = ""
        if context in ["subscription_offer", "subscription_benefits"]:
            subscription_cta = """
            <div style="margin: 20px 0; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 12px; text-align: center;">
                <h3 style="color: white; margin: 0 0 15px 0;">🚀 Upgrade to Noizyfish Premium</h3>
                <a href="https://noizyfish.com/subscribe?code=SUPPORT20" 
                   style="display: inline-block; background: #ff6b6b; color: white; padding: 12px 24px; 
                          text-decoration: none; border-radius: 6px; font-weight: bold; margin: 10px;">
                    Subscribe Now - 20% Off!
                </a>
                <p style="color: #e0e6ed; font-size: 14px; margin: 10px 0 0 0;">
                    Use code SUPPORT20 at checkout
                </p>
            </div>
            """
        
        html_template = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Noizyfish Support - AI Assistant Response</title>
        </head>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; padding: 20px;">
            
            <div style="text-align: center; margin-bottom: 30px;">
                <h1 style="color: #007bff; margin: 0;">🐠 Noizyfish Support</h1>
                <p style="color: #666; margin: 5px 0;">AI-Powered Technical Assistance</p>
            </div>
            
            {audio_player}
            
            <div style="background: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
                <div style="white-space: pre-line; font-size: 16px; line-height: 1.6;">
                    {text}
                </div>
            </div>
            
            {subscription_cta}
            
            <div style="margin: 30px 0; padding: 20px; background: #f8f9fa; border-radius: 8px;">
                <h4 style="color: #28a745; margin: 0 0 15px 0;">📋 Next Steps:</h4>
                <ul style="margin: 0; padding-left: 20px;">
                    <li>Reply to this email with your detailed response</li>
                    <li>Attach any relevant photos or screenshots</li>
                    <li>Record a voice message if preferred</li>
                    <li>Visit <a href="https://noizyfish.com">noizyfish.com</a> for premium support</li>
                </ul>
            </div>
            
            <div style="text-align: center; margin-top: 30px; padding: 20px; border-top: 1px solid #eee;">
                <p style="font-size: 14px; color: #666;">
                    This message was generated by Sarah, your AI assistant at Noizyfish Support.<br>
                    For immediate assistance, visit <a href="https://noizyfish.com">noizyfish.com</a>
                </p>
                <div style="margin: 15px 0;">
                    <a href="https://noizyfish.com" style="margin: 0 10px; color: #007bff; text-decoration: none;">🌐 Website</a>
                    <a href="mailto:info@noizyfish.com" style="margin: 0 10px; color: #007bff; text-decoration: none;">📧 Email</a>
                    <a href="https://noizyfish.com/subscribe" style="margin: 0 10px; color: #007bff; text-decoration: none;">⭐ Subscribe</a>
                </div>
            </div>
            
        </body>
        </html>
        """
        
        return html_template
    
    def _get_suggested_actions(self, context: str) -> List[str]:
        """Get suggested actions based on context"""
        action_map = {
            "welcome": [
                "Collect detailed issue description",
                "Request device information", 
                "Offer subscription benefits"
            ],
            "issue_description": [
                "Analyze description for keywords",
                "Request additional details if needed",
                "Categorize as hardware/software"
            ],
            "hardware_detected": [
                "Schedule on-site evaluation",
                "Connect with repair partners",
                "Provide cost estimates"
            ],
            "software_detected": [
                "Offer remote troubleshooting",
                "Schedule screen sharing session",
                "Provide quick fixes"
            ],
            "subscription_offer": [
                "Track conversion metrics",
                "Follow up in 24 hours",
                "Provide trial access"
            ]
        }
        
        return action_map.get(context, ["Process client response", "Escalate to human agent"])
    
    def generate_contextual_reply(self, issue_category: str, priority: str, 
                                client_info: Dict[str, Any] = None) -> Dict[str, Any]:
        """Generate contextual auto-reply based on issue analysis"""
        
        if issue_category.upper() == "HARDWARE":
            context = "hardware_detected"
        elif issue_category.upper() == "SOFTWARE":
            context = "software_detected"
        elif priority.upper() in ["CRITICAL", "HIGH"]:
            context = "urgency_assessment"
        else:
            context = "subscription_offer"
        
        return self.generate_auto_reply(
            context=context,
            client_email=client_info.get("email", "") if client_info else "",
            issue_details={"priority": priority, "category": issue_category}
        )

# Global auto-reply system
auto_reply_system = AutoReplySystem()