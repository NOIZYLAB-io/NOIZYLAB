# ROB OS - EMPIRE ENGINE
# =======================
# NoizyLab + FishMusicInc = One organism funding Rob & Carolynne for life
# "ALEX WARD CAN MARKET ANYTHING HE THINKS OF FOR ME!!"

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime

class Brand(Enum):
    NOIZYLAB = "noizylab"
    FISHMUSIC = "fishmusic"
    SECONDLIFE = "2ndlife"
    HERITAGE = "heritage"

class ServiceTier(Enum):
    QUICK = "quick"           # Quick triage / quick fix
    STANDARD = "standard"     # Deep clean / full service
    VIP = "vip"               # Retainer / ongoing care

@dataclass
class Service:
    """A service offering."""
    id: str
    brand: Brand
    name: str
    tagline: str
    description: str
    tier: ServiceTier
    price_range: str
    deliverables: List[str]
    duration: str
    recurring: bool = False

@dataclass
class RevenueStream:
    """A revenue stream in the empire."""
    id: str
    brand: Brand
    name: str
    monthly_target: float
    current_monthly: float = 0.0
    clients: int = 0
    notes: str = ""

# ============================================
# THE NOIZYLAB + FISHMUSIC EMPIRE
# ============================================

SERVICES: Dict[str, Service] = {
    
    # ========== NOIZYLAB SERVICES ==========
    
    "nl_quick_triage": Service(
        id="nl_quick_triage",
        brand=Brand.NOIZYLAB,
        name="Quick Triage",
        tagline="Find out what's wrong, fast.",
        description="30-45 minute remote or in-person diagnostic. Written summary and clear recommendation.",
        tier=ServiceTier.QUICK,
        price_range="$49-79",
        deliverables=[
            "Diagnostic session (30-45 min)",
            "Written summary of findings",
            "Clear recommendation for next steps"
        ],
        duration="30-45 min",
        recurring=False
    ),
    
    "nl_deep_clean": Service(
        id="nl_deep_clean",
        brand=Brand.NOIZYLAB,
        name="Deep Clean & Optimize",
        tagline="Make it sing again.",
        description="Full system cleanup, updates, performance tuning. Optional light automation.",
        tier=ServiceTier.STANDARD,
        price_range="$149-249",
        deliverables=[
            "Full system cleanup",
            "Updates and security patches",
            "Performance optimization",
            "Startup bloat removal",
            "Basic backup check",
            "Written report"
        ],
        duration="2-3 hours",
        recurring=False
    ),
    
    "nl_data_rescue": Service(
        id="nl_data_rescue",
        brand=Brand.NOIZYLAB,
        name="Data-First Rescue",
        tagline="Your files are priority one.",
        description="When the machine is dying but the data must survive. Careful, data-first approach.",
        tier=ServiceTier.STANDARD,
        price_range="$199-399",
        deliverables=[
            "Risk assessment",
            "Data preservation strategy",
            "Careful extraction/backup",
            "Recovery lab referral if needed",
            "Full documentation"
        ],
        duration="2-4 hours",
        recurring=False
    ),
    
    "nl_vip_care": Service(
        id="nl_vip_care",
        brand=Brand.NOIZYLAB,
        name="VIP Care Plan",
        tagline="Never face tech alone again.",
        description="Monthly retainer. Proactive monitoring, priority support, peace of mind.",
        tier=ServiceTier.VIP,
        price_range="$99-199/month",
        deliverables=[
            "Monthly health check",
            "Proactive monitoring",
            "Priority support (same-day response)",
            "Quarterly tune-up included",
            "Backup verification",
            "Direct line to Rob"
        ],
        duration="Ongoing",
        recurring=True
    ),
    
    # ========== FISHMUSIC SERVICES ==========
    
    "fm_audio_resurrection": Service(
        id="fm_audio_resurrection",
        brand=Brand.FISHMUSIC,
        name="Audio Resurrection",
        tagline="Bring your old recordings back to life.",
        description="Old mixes, sessions, tapes → cleaned, modern loudness, safely archived.",
        tier=ServiceTier.STANDARD,
        price_range="$199-499/project",
        deliverables=[
            "Audio restoration",
            "Noise reduction",
            "Modern loudness optimization",
            "Multiple format delivery",
            "Archival backup"
        ],
        duration="1-2 weeks",
        recurring=False
    ),
    
    "fm_sonic_polish": Service(
        id="fm_sonic_polish",
        brand=Brand.FISHMUSIC,
        name="Signature Sound Polish",
        tagline="The final touch that makes it yours.",
        description="Artists/producers send tracks → final touch, loudness, glue, that Fish sound.",
        tier=ServiceTier.STANDARD,
        price_range="$99-299/track",
        deliverables=[
            "Final mix polish",
            "Loudness optimization",
            "Stereo enhancement",
            "Multiple format masters"
        ],
        duration="3-5 days",
        recurring=False
    ),
    
    "fm_2ndlife_revival": Service(
        id="fm_2ndlife_revival",
        brand=Brand.SECONDLIFE,
        name="2NDLIFE Analog Revival",
        tagline="Analog warmth, digital precision.",
        description="Premium tier: analog gear in the loop, before/after examples, the full treatment.",
        tier=ServiceTier.VIP,
        price_range="$499-999/project",
        deliverables=[
            "Analog processing chain",
            "Before/after documentation",
            "High-resolution masters",
            "Archival package",
            "Certificate of authenticity"
        ],
        duration="2-3 weeks",
        recurring=False
    ),
    
    # ========== HERITAGE (FUTURE) ==========
    
    "heritage_voice_legacy": Service(
        id="heritage_voice_legacy",
        brand=Brand.HERITAGE,
        name="Voice Legacy Package",
        tagline="Your voice, preserved forever.",
        description="Premium voice preservation and AI training for legacy purposes.",
        tier=ServiceTier.VIP,
        price_range="$2,999-9,999",
        deliverables=[
            "Professional voice recording session",
            "AI voice model training",
            "Ethical usage framework",
            "Family access controls",
            "Perpetual storage"
        ],
        duration="1-2 months",
        recurring=False
    )
}


class EmpireEngine:
    """
    The Empire Engine - Manages all revenue streams for Rob & Carolynne.
    """
    
    def __init__(self):
        self.services = SERVICES
        self.revenue_streams: Dict[str, RevenueStream] = {}
        self.comfort_target: float = 0.0  # Monthly comfort number
        
        # Initialize revenue streams
        self._init_revenue_streams()
    
    def _init_revenue_streams(self):
        """Initialize the revenue stream tracking."""
        self.revenue_streams = {
            "nl_services": RevenueStream(
                id="nl_services",
                brand=Brand.NOIZYLAB,
                name="NoizyLab Services",
                monthly_target=0.0,
                notes="Quick triage + Deep clean + Data rescue"
            ),
            "nl_retainers": RevenueStream(
                id="nl_retainers",
                brand=Brand.NOIZYLAB,
                name="VIP Care Plans",
                monthly_target=0.0,
                notes="Recurring monthly retainers"
            ),
            "fm_services": RevenueStream(
                id="fm_services",
                brand=Brand.FISHMUSIC,
                name="FishMusic Services",
                monthly_target=0.0,
                notes="Audio resurrection + Polish + 2NDLIFE"
            ),
            "ip_products": RevenueStream(
                id="ip_products",
                brand=Brand.HERITAGE,
                name="IP & Products",
                monthly_target=0.0,
                notes="Templates, sound packs, Heritage, future products"
            )
        }
    
    def set_comfort_target(self, monthly_amount: float):
        """
        Set the monthly comfort target for Rob & Carolynne.
        """
        self.comfort_target = monthly_amount
        
        # Distribute across streams (recommended split)
        # 60% services, 25% retainers, 15% IP
        self.revenue_streams["nl_services"].monthly_target = monthly_amount * 0.35
        self.revenue_streams["nl_retainers"].monthly_target = monthly_amount * 0.25
        self.revenue_streams["fm_services"].monthly_target = monthly_amount * 0.25
        self.revenue_streams["ip_products"].monthly_target = monthly_amount * 0.15
    
    def get_service(self, service_id: str) -> Optional[Service]:
        return self.services.get(service_id)
    
    def get_services_by_brand(self, brand: Brand) -> List[Service]:
        return [s for s in self.services.values() if s.brand == brand]
    
    def get_recurring_services(self) -> List[Service]:
        return [s for s in self.services.values() if s.recurring]
    
    def get_revenue_dashboard(self) -> Dict[str, Any]:
        """
        Get the revenue dashboard data.
        """
        total_current = sum(s.current_monthly for s in self.revenue_streams.values())
        total_target = self.comfort_target
        
        return {
            "comfort_target": self.comfort_target,
            "current_total": total_current,
            "gap": max(0, total_target - total_current),
            "progress_percent": (total_current / total_target * 100) if total_target > 0 else 0,
            "streams": [
                {
                    "id": s.id,
                    "name": s.name,
                    "brand": s.brand.value,
                    "target": s.monthly_target,
                    "current": s.current_monthly,
                    "clients": s.clients,
                    "progress": (s.current_monthly / s.monthly_target * 100) if s.monthly_target > 0 else 0
                }
                for s in self.revenue_streams.values()
            ],
            "message": self._get_status_message(total_current, total_target)
        }
    
    def _get_status_message(self, current: float, target: float) -> str:
        if target == 0:
            return "Set your comfort target to start tracking."
        
        progress = current / target
        if progress >= 1.0:
            return "🎉 Comfort target reached! You're funded."
        elif progress >= 0.75:
            return "Almost there. Keep the momentum."
        elif progress >= 0.5:
            return "Halfway to comfort. Good progress."
        elif progress >= 0.25:
            return "Building momentum. Every client counts."
        else:
            return "Early days. Focus on quick wins."
    
    def get_service_menu(self) -> Dict[str, Any]:
        """
        Get the complete service menu for marketing.
        """
        return {
            "noizylab": {
                "brand": "NOIZYLAB",
                "tagline": "Tech repair that treats you like a human.",
                "services": [
                    {
                        "name": s.name,
                        "tagline": s.tagline,
                        "price": s.price_range,
                        "tier": s.tier.value
                    }
                    for s in self.get_services_by_brand(Brand.NOIZYLAB)
                ]
            },
            "fishmusic": {
                "brand": "FISH MUSIC INC",
                "tagline": "40 years of sound, at your service.",
                "services": [
                    {
                        "name": s.name,
                        "tagline": s.tagline,
                        "price": s.price_range,
                        "tier": s.tier.value
                    }
                    for s in self.get_services_by_brand(Brand.FISHMUSIC)
                ]
            },
            "2ndlife": {
                "brand": "2NDLIFE",
                "tagline": "Analog revival. Digital precision.",
                "services": [
                    {
                        "name": s.name,
                        "tagline": s.tagline,
                        "price": s.price_range,
                        "tier": s.tier.value
                    }
                    for s in self.get_services_by_brand(Brand.SECONDLIFE)
                ]
            }
        }
    
    def calculate_jobs_needed(self) -> Dict[str, Any]:
        """
        Calculate how many jobs are needed to hit comfort target.
        """
        if self.comfort_target == 0:
            return {"error": "Set comfort target first"}
        
        # Average prices for calculation
        avg_prices = {
            "nl_quick": 65,
            "nl_deep": 200,
            "nl_vip": 150,  # Monthly
            "fm_resurrection": 350,
            "fm_polish": 200
        }
        
        # Calculate different scenarios
        scenarios = {
            "all_quick_triage": {
                "jobs_needed": int(self.comfort_target / avg_prices["nl_quick"]),
                "description": "If you only did Quick Triage"
            },
            "mixed_noizylab": {
                "quick": int(self.comfort_target * 0.3 / avg_prices["nl_quick"]),
                "deep": int(self.comfort_target * 0.4 / avg_prices["nl_deep"]),
                "vip_clients": int(self.comfort_target * 0.3 / avg_prices["nl_vip"]),
                "description": "Balanced NoizyLab mix (30% quick, 40% deep, 30% VIP)"
            },
            "recommended": {
                "nl_deep": 3,
                "nl_vip_clients": 5,
                "fm_projects": 2,
                "description": "Sustainable mix: 3 deep cleans + 5 VIP retainers + 2 audio projects/month"
            }
        }
        
        return {
            "comfort_target": self.comfort_target,
            "scenarios": scenarios,
            "note": "VIP retainers are the key - recurring revenue means less hustle."
        }


# Singleton instance
_empire_engine = None

def get_empire_engine() -> EmpireEngine:
    global _empire_engine
    if _empire_engine is None:
        _empire_engine = EmpireEngine()
    return _empire_engine

