# ROB OS - CASH ENGINE
# =====================
# The money-making systems that fund Rob & Carolynne's life
# "Steady, boring money from repairs + maintenance"

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

class ProductType(Enum):
    SERVICE = "service"           # One-time service
    RETAINER = "retainer"         # Recurring monthly
    DIGITAL_PRODUCT = "digital"   # Sell once, deliver forever
    COURSE = "course"             # Educational content

@dataclass
class CashProduct:
    """A product or service that generates revenue."""
    id: str
    name: str
    tagline: str
    product_type: ProductType
    price: float
    recurring: bool = False
    
    # What's included
    deliverables: List[str] = field(default_factory=list)
    
    # Target market
    target_market: List[str] = field(default_factory=list)
    
    # Upsells
    upsells: List[str] = field(default_factory=list)

# ============================================
# THE CASH PRODUCTS
# ============================================

CASH_PRODUCTS: Dict[str, CashProduct] = {
    
    # ========== NOIZYLAB SERVICES ==========
    
    "calm_tech_package": CashProduct(
        id="calm_tech_package",
        name="NoizyLab Calm Tech Package",
        tagline="I make your computer boringly reliable.",
        product_type=ProductType.SERVICE,
        price=149.0,
        recurring=False,
        deliverables=[
            "Full triage + diagnostic",
            "System cleanup + optimization",
            "Backup setup + verification",
            "Basic AI shortcuts (updates, maintenance)",
            "1-page 'How to keep it calm' summary"
        ],
        target_market=[
            "Busy professionals",
            "Older users",
            "Small businesses",
            "People who just want it to work"
        ],
        upsells=["vip_care_plan", "family_rescue"]
    ),
    
    "family_rescue": CashProduct(
        id="family_rescue",
        name="2NDLIFE Family Computer Rescue",
        tagline="The whole family, sorted.",
        product_type=ProductType.SERVICE,
        price=349.0,
        recurring=False,
        deliverables=[
            "Multi-machine family tune-up (up to 4 devices)",
            "Standardized backups across all machines",
            "Parental safety setup",
            "Family tech sanity guide",
            "Yearly health check included"
        ],
        target_market=[
            "Families with multiple devices",
            "Parents worried about kids' safety",
            "Multi-generational households"
        ],
        upsells=["vip_care_plan"]
    ),
    
    "vip_care_plan": CashProduct(
        id="vip_care_plan",
        name="VIP Care Plan",
        tagline="Never face tech alone again.",
        product_type=ProductType.RETAINER,
        price=149.0,
        recurring=True,
        deliverables=[
            "Monthly health check",
            "Proactive monitoring",
            "Priority support (same-day response)",
            "Quarterly tune-up included",
            "Backup verification",
            "Direct line to Rob"
        ],
        target_market=[
            "Professionals who can't afford downtime",
            "Small business owners",
            "Creative professionals",
            "Anyone who hates tech surprises"
        ],
        upsells=[]
    ),
    
    "accessibility_audit": CashProduct(
        id="accessibility_audit",
        name="Accessibility Tech Upgrade Audit",
        tagline="Tech that works with your body, not against it.",
        product_type=ProductType.SERVICE,
        price=249.0,
        recurring=False,
        deliverables=[
            "Full accessibility audit of your tech setup",
            "Workflow optimization for your specific needs",
            "AI tool recommendations",
            "Concrete automation action plan",
            "Follow-up support session"
        ],
        target_market=[
            "Disabled creators",
            "Freelancers with physical limitations",
            "Small businesses with accessibility needs",
            "Anyone struggling with tech due to health"
        ],
        upsells=["vip_care_plan"]
    ),
    
    # ========== FISHMUSIC SERVICES ==========
    
    "song_resurrection": CashProduct(
        id="song_resurrection",
        name="FishMusic Song Resurrection Session",
        tagline="Give your old track a 2025 life.",
        product_type=ProductType.SERVICE,
        price=199.0,
        recurring=False,
        deliverables=[
            "Audio restoration + cleanup",
            "Modern loudness optimization",
            "Mix polish",
            "Multiple format delivery",
            "Short video walkthrough of changes"
        ],
        target_market=[
            "Musicians with old recordings",
            "Bands wanting to re-release classics",
            "Anyone with precious audio memories"
        ],
        upsells=["catalog_resurrection"]
    ),
    
    "catalog_resurrection": CashProduct(
        id="catalog_resurrection",
        name="Full Catalog Resurrection",
        tagline="Your whole catalog, brought back to life.",
        product_type=ProductType.SERVICE,
        price=999.0,
        recurring=False,
        deliverables=[
            "Up to 10 tracks fully restored",
            "Consistent sonic identity across catalog",
            "Master versions for streaming",
            "Archival quality preservation",
            "Catalog organization + metadata"
        ],
        target_market=[
            "Artists with extensive back catalogs",
            "Labels with legacy content",
            "Estates managing artist legacies"
        ],
        upsells=[]
    ),
    
    "analog_revival": CashProduct(
        id="analog_revival",
        name="2NDLIFE Analog Revival",
        tagline="Analog warmth, digital precision.",
        product_type=ProductType.SERVICE,
        price=499.0,
        recurring=False,
        deliverables=[
            "Analog processing chain treatment",
            "Before/after documentation",
            "High-resolution masters",
            "Archival package",
            "Certificate of authenticity"
        ],
        target_market=[
            "Audiophiles",
            "Vinyl enthusiasts",
            "Artists wanting premium treatment"
        ],
        upsells=[]
    ),
    
    # ========== DIGITAL PRODUCTS ==========
    
    "sonic_healing_pack": CashProduct(
        id="sonic_healing_pack",
        name="Sonic Healing Pack",
        tagline="Calm your nervous system with sound.",
        product_type=ProductType.DIGITAL_PRODUCT,
        price=29.0,
        recurring=False,
        deliverables=[
            "10 curated ambient tracks",
            "Themes: Focus, Sleep, Calm, Recovery",
            "High-quality audio files",
            "Usage guide for different states"
        ],
        target_market=[
            "Burnt-out professionals",
            "People with anxiety",
            "Anyone who uses sound to regulate"
        ],
        upsells=["sonic_healing_membership"]
    ),
    
    "template_pack": CashProduct(
        id="template_pack",
        name="NoizyLab Template Pack",
        tagline="The exact templates I use to run my business.",
        product_type=ProductType.DIGITAL_PRODUCT,
        price=49.0,
        recurring=False,
        deliverables=[
            "Client intake form template",
            "Repair report template",
            "Invoice template",
            "Audio restoration checklist",
            "MC96 folder structure template"
        ],
        target_market=[
            "Freelance tech support",
            "Audio engineers",
            "Anyone building a service business"
        ],
        upsells=[]
    ),
    
    # ========== HERITAGE ==========
    
    "heritage_interview": CashProduct(
        id="heritage_interview",
        name="Heritage Voice Recording Session",
        tagline="Preserve the voices that matter.",
        product_type=ProductType.SERVICE,
        price=499.0,
        recurring=False,
        deliverables=[
            "Guided voice recording session (2 hours)",
            "Family tree questions",
            "Message to future generations",
            "High-quality audio archive",
            "Transcription",
            "Optional: AI voice model preparation"
        ],
        target_market=[
            "Families wanting to preserve elder voices",
            "Anyone facing end-of-life situations",
            "People who value legacy"
        ],
        upsells=["heritage_voice_model"]
    ),
    
    "heritage_voice_model": CashProduct(
        id="heritage_voice_model",
        name="Heritage Voice Legacy Package",
        tagline="Their voice, preserved forever.",
        product_type=ProductType.SERVICE,
        price=2999.0,
        recurring=False,
        deliverables=[
            "Professional voice recording session",
            "AI voice model training",
            "Ethical usage framework",
            "Family access controls",
            "Perpetual storage"
        ],
        target_market=[
            "Families with means",
            "Public figures",
            "Artists wanting voice legacy"
        ],
        upsells=[]
    )
}


class CashEngine:
    """
    The Cash Engine - Manages all revenue-generating products and services.
    """
    
    def __init__(self):
        self.products = CASH_PRODUCTS
        self.active_clients: List[Dict[str, Any]] = []
        self.pipeline: List[Dict[str, Any]] = []
        self.monthly_revenue: float = 0.0
        self.monthly_target: float = 0.0
    
    def get_product(self, product_id: str) -> Optional[CashProduct]:
        return self.products.get(product_id)
    
    def get_all_products(self) -> Dict[str, CashProduct]:
        return self.products
    
    def get_services(self) -> List[CashProduct]:
        return [p for p in self.products.values() if p.product_type == ProductType.SERVICE]
    
    def get_retainers(self) -> List[CashProduct]:
        return [p for p in self.products.values() if p.product_type == ProductType.RETAINER]
    
    def get_digital_products(self) -> List[CashProduct]:
        return [p for p in self.products.values() if p.product_type == ProductType.DIGITAL_PRODUCT]
    
    def calculate_revenue_scenarios(self, target: float) -> Dict[str, Any]:
        """
        Calculate different scenarios to hit revenue target.
        """
        scenarios = {
            "all_calm_tech": {
                "product": "calm_tech_package",
                "jobs_needed": int(target / 149),
                "description": "If you only did Calm Tech Packages"
            },
            "retainer_focused": {
                "retainers_needed": int(target / 149),
                "description": "VIP retainers = recurring revenue = less hustle"
            },
            "recommended_mix": {
                "calm_tech_jobs": 3,
                "vip_retainers": 5,
                "audio_projects": 2,
                "estimated_monthly": (3 * 149) + (5 * 149) + (2 * 199),
                "description": "Sustainable mix: services + retainers + audio"
            }
        }
        return scenarios
    
    def get_quick_start_products(self) -> List[CashProduct]:
        """
        Get the products to focus on first for quick revenue.
        """
        return [
            self.products["calm_tech_package"],
            self.products["vip_care_plan"],
            self.products["song_resurrection"]
        ]
    
    def get_product_pitch(self, product_id: str) -> Dict[str, Any]:
        """
        Get a ready-to-use pitch for a product.
        """
        product = self.products.get(product_id)
        if not product:
            return {"error": "Product not found"}
        
        return {
            "headline": product.name,
            "tagline": product.tagline,
            "price": f"${product.price}" + ("/month" if product.recurring else ""),
            "what_you_get": product.deliverables,
            "perfect_for": product.target_market,
            "cta": "Book Now" if product.product_type == ProductType.SERVICE else "Buy Now"
        }
    
    def add_to_pipeline(self, client_name: str, product_id: str, notes: str = ""):
        """Add a potential client to the pipeline."""
        self.pipeline.append({
            "client": client_name,
            "product": product_id,
            "notes": notes,
            "added": datetime.now().isoformat(),
            "status": "lead"
        })
    
    def convert_client(self, client_name: str, product_id: str):
        """Convert a pipeline lead to active client."""
        product = self.products.get(product_id)
        if product:
            self.active_clients.append({
                "client": client_name,
                "product": product_id,
                "started": datetime.now().isoformat(),
                "revenue": product.price
            })
            if product.recurring:
                self.monthly_revenue += product.price
    
    def get_dashboard(self) -> Dict[str, Any]:
        """Get the cash engine dashboard."""
        return {
            "monthly_target": self.monthly_target,
            "monthly_revenue": self.monthly_revenue,
            "gap": max(0, self.monthly_target - self.monthly_revenue),
            "active_clients": len(self.active_clients),
            "pipeline_count": len(self.pipeline),
            "quick_start_products": [
                {"name": p.name, "price": p.price, "tagline": p.tagline}
                for p in self.get_quick_start_products()
            ]
        }


# Singleton instance
_cash_engine = None

def get_cash_engine() -> CashEngine:
    global _cash_engine
    if _cash_engine is None:
        _cash_engine = CashEngine()
    return _cash_engine

