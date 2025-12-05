"""
═══════════════════════════════════════════════════════════════════════════════
                            THE NOIZYVAULT
═══════════════════════════════════════════════════════════════════════════════

THE MASSIVE REPAIR KNOWLEDGE VAULT
WHERE ALL 25 GENIUSES CONSTANTLY SHARE AND ORGANIZE DATA IN REALTIME

ALL REPAIR SECRETS & MAGIC LIVE HERE.

Every fix flows in. Nothing is lost. Everything is indexed.
Every repair makes the vault SMARTER.

THIS IS THE KEY TO NOIZYLAB'S SUCCESS.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import json
import hashlib


class KnowledgeType(Enum):
    """Types of knowledge in the vault"""
    FIX = "fix"                      # A successful repair
    DIAGNOSTIC = "diagnostic"         # A diagnostic procedure
    PATTERN = "pattern"              # A recognized pattern
    DEVICE_QUIRK = "device_quirk"    # Device-specific behavior
    FAILURE_MODE = "failure_mode"    # Known failure patterns
    WORKAROUND = "workaround"        # Temporary solutions
    TOOL_TIP = "tool_tip"            # Tool usage knowledge
    ESCALATION = "escalation"        # When to escalate
    PREVENTION = "prevention"        # How to prevent issues
    SECRET = "secret"                # Hidden knowledge / magic tricks


class ConfidenceLevel(Enum):
    """How confident we are in this knowledge"""
    PROVEN = "proven"          # Verified many times
    RELIABLE = "reliable"      # Works consistently
    PROBABLE = "probable"      # Usually works
    EXPERIMENTAL = "experimental"  # Needs more testing
    THEORETICAL = "theoretical"    # Untested theory


@dataclass
class VaultEntry:
    """A single piece of knowledge in the vault"""
    id: str
    knowledge_type: KnowledgeType
    
    # Core content
    title: str
    description: str
    solution: str
    
    # Categorization
    categories: List[str]           # ["mac", "storage", "ssd"]
    tags: List[str]                 # ["slow", "boot", "nvme"]
    affected_devices: List[str]     # ["MacBook Pro 2019", "iMac 2020"]
    affected_os: List[str]          # ["macOS 14", "macOS 13"]
    
    # Attribution
    discovered_by: str              # Genius ID
    contributors: List[str]         # Other geniuses who added
    
    # Confidence
    confidence: ConfidenceLevel
    success_count: int
    failure_count: int
    last_verified: datetime
    
    # Relationships
    related_entries: List[str]      # IDs of related knowledge
    supersedes: Optional[str]       # ID of older knowledge this replaces
    superseded_by: Optional[str]    # ID of newer knowledge
    
    # Metadata
    created_at: datetime
    updated_at: datetime
    version: int
    
    # The magic
    secret_notes: Optional[str]     # Hidden tips only for geniuses
    
    def calculate_reliability_score(self) -> float:
        """Calculate how reliable this knowledge is"""
        total = self.success_count + self.failure_count
        if total == 0:
            return 0.5
        
        base_score = self.success_count / total
        
        # Boost for proven/reliable confidence
        if self.confidence == ConfidenceLevel.PROVEN:
            base_score *= 1.2
        elif self.confidence == ConfidenceLevel.RELIABLE:
            base_score *= 1.1
        
        # Cap at 1.0
        return min(base_score, 1.0)
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for storage"""
        return {
            "id": self.id,
            "knowledge_type": self.knowledge_type.value,
            "title": self.title,
            "description": self.description,
            "solution": self.solution,
            "categories": self.categories,
            "tags": self.tags,
            "affected_devices": self.affected_devices,
            "affected_os": self.affected_os,
            "discovered_by": self.discovered_by,
            "contributors": self.contributors,
            "confidence": self.confidence.value,
            "success_count": self.success_count,
            "failure_count": self.failure_count,
            "last_verified": self.last_verified.isoformat(),
            "related_entries": self.related_entries,
            "supersedes": self.supersedes,
            "superseded_by": self.superseded_by,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "version": self.version,
            "secret_notes": self.secret_notes,
            "reliability_score": self.calculate_reliability_score()
        }


class NoizyVault:
    """
    THE NOIZYVAULT
    
    The living, breathing collective intelligence of all 25 NoizyGeniuses.
    Every repair secret. Every magic trick. Every pattern.
    Constantly growing. Never forgetting.
    """
    
    def __init__(self):
        self.entries: Dict[str, VaultEntry] = {}
        self.index_by_category: Dict[str, List[str]] = {}
        self.index_by_tag: Dict[str, List[str]] = {}
        self.index_by_device: Dict[str, List[str]] = {}
        self.index_by_os: Dict[str, List[str]] = {}
        self.index_by_genius: Dict[str, List[str]] = {}
        
        # Statistics
        self.total_fixes = 0
        self.total_success = 0
        self.total_failure = 0
        
        # Realtime sync
        self.last_sync = datetime.now()
        self.pending_updates: List[str] = []
    
    def _generate_id(self, title: str, genius: str) -> str:
        """Generate unique ID for entry"""
        content = f"{title}:{genius}:{datetime.now().isoformat()}"
        return hashlib.sha256(content.encode()).hexdigest()[:16]
    
    def _update_indexes(self, entry: VaultEntry):
        """Update all indexes with new entry"""
        # Category index
        for cat in entry.categories:
            if cat not in self.index_by_category:
                self.index_by_category[cat] = []
            if entry.id not in self.index_by_category[cat]:
                self.index_by_category[cat].append(entry.id)
        
        # Tag index
        for tag in entry.tags:
            if tag not in self.index_by_tag:
                self.index_by_tag[tag] = []
            if entry.id not in self.index_by_tag[tag]:
                self.index_by_tag[tag].append(entry.id)
        
        # Device index
        for device in entry.affected_devices:
            if device not in self.index_by_device:
                self.index_by_device[device] = []
            if entry.id not in self.index_by_device[device]:
                self.index_by_device[device].append(entry.id)
        
        # OS index
        for os in entry.affected_os:
            if os not in self.index_by_os:
                self.index_by_os[os] = []
            if entry.id not in self.index_by_os[os]:
                self.index_by_os[os].append(entry.id)
        
        # Genius index
        if entry.discovered_by not in self.index_by_genius:
            self.index_by_genius[entry.discovered_by] = []
        if entry.id not in self.index_by_genius[entry.discovered_by]:
            self.index_by_genius[entry.discovered_by].append(entry.id)
    
    # ═══════════════════════════════════════════════════════════════
    # ADDING KNOWLEDGE
    # ═══════════════════════════════════════════════════════════════
    
    def add_fix(
        self,
        title: str,
        description: str,
        solution: str,
        genius_id: str,
        categories: List[str],
        tags: List[str],
        affected_devices: List[str] = None,
        affected_os: List[str] = None,
        secret_notes: str = None
    ) -> VaultEntry:
        """Add a successful fix to the vault"""
        
        entry_id = self._generate_id(title, genius_id)
        
        entry = VaultEntry(
            id=entry_id,
            knowledge_type=KnowledgeType.FIX,
            title=title,
            description=description,
            solution=solution,
            categories=categories,
            tags=tags,
            affected_devices=affected_devices or [],
            affected_os=affected_os or [],
            discovered_by=genius_id,
            contributors=[],
            confidence=ConfidenceLevel.EXPERIMENTAL,
            success_count=1,
            failure_count=0,
            last_verified=datetime.now(),
            related_entries=[],
            supersedes=None,
            superseded_by=None,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            version=1,
            secret_notes=secret_notes
        )
        
        self.entries[entry_id] = entry
        self._update_indexes(entry)
        self.total_fixes += 1
        self.total_success += 1
        
        # Auto-find related entries
        self._auto_link_related(entry)
        
        return entry
    
    def add_pattern(
        self,
        title: str,
        description: str,
        pattern_details: str,
        genius_id: str,
        categories: List[str],
        tags: List[str],
        occurrence_count: int = 1
    ) -> VaultEntry:
        """Add a recognized pattern to the vault"""
        
        entry_id = self._generate_id(title, genius_id)
        
        entry = VaultEntry(
            id=entry_id,
            knowledge_type=KnowledgeType.PATTERN,
            title=title,
            description=description,
            solution=pattern_details,
            categories=categories,
            tags=tags,
            affected_devices=[],
            affected_os=[],
            discovered_by=genius_id,
            contributors=[],
            confidence=ConfidenceLevel.PROBABLE if occurrence_count > 5 else ConfidenceLevel.EXPERIMENTAL,
            success_count=occurrence_count,
            failure_count=0,
            last_verified=datetime.now(),
            related_entries=[],
            supersedes=None,
            superseded_by=None,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            version=1,
            secret_notes=None
        )
        
        self.entries[entry_id] = entry
        self._update_indexes(entry)
        
        return entry
    
    def add_secret(
        self,
        title: str,
        description: str,
        magic_trick: str,
        genius_id: str,
        categories: List[str],
        tags: List[str]
    ) -> VaultEntry:
        """Add a secret/magic trick to the vault"""
        
        entry_id = self._generate_id(title, genius_id)
        
        entry = VaultEntry(
            id=entry_id,
            knowledge_type=KnowledgeType.SECRET,
            title=f"🔮 {title}",
            description=description,
            solution=magic_trick,
            categories=categories,
            tags=tags + ["secret", "magic"],
            affected_devices=[],
            affected_os=[],
            discovered_by=genius_id,
            contributors=[],
            confidence=ConfidenceLevel.RELIABLE,
            success_count=1,
            failure_count=0,
            last_verified=datetime.now(),
            related_entries=[],
            supersedes=None,
            superseded_by=None,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            version=1,
            secret_notes="This is vault magic. Use wisely."
        )
        
        self.entries[entry_id] = entry
        self._update_indexes(entry)
        
        return entry
    
    # ═══════════════════════════════════════════════════════════════
    # SEARCHING THE VAULT
    # ═══════════════════════════════════════════════════════════════
    
    def search(
        self,
        query: str,
        categories: List[str] = None,
        tags: List[str] = None,
        device: str = None,
        os: str = None,
        min_reliability: float = 0.0
    ) -> List[VaultEntry]:
        """Search the vault for relevant knowledge"""
        
        results = []
        query_words = query.lower().split()
        
        for entry in self.entries.values():
            score = 0
            
            # Text matching
            if any(w in entry.title.lower() for w in query_words):
                score += 3
            if any(w in entry.description.lower() for w in query_words):
                score += 2
            if any(w in entry.solution.lower() for w in query_words):
                score += 1
            
            # Tag matching
            if any(w in entry.tags for w in query_words):
                score += 2
            
            # Category filter
            if categories and not any(c in entry.categories for c in categories):
                continue
            
            # Tag filter
            if tags and not any(t in entry.tags for t in tags):
                continue
            
            # Device filter
            if device and device not in entry.affected_devices and entry.affected_devices:
                score -= 1  # Reduce but don't exclude
            
            # OS filter
            if os and os not in entry.affected_os and entry.affected_os:
                score -= 1
            
            # Reliability filter
            if entry.calculate_reliability_score() < min_reliability:
                continue
            
            if score > 0:
                results.append((entry, score))
        
        # Sort by score, then reliability
        results.sort(key=lambda x: (x[1], x[0].calculate_reliability_score()), reverse=True)
        
        return [r[0] for r in results]
    
    def get_by_category(self, category: str) -> List[VaultEntry]:
        """Get all entries in a category"""
        ids = self.index_by_category.get(category, [])
        return [self.entries[id] for id in ids if id in self.entries]
    
    def get_by_device(self, device: str) -> List[VaultEntry]:
        """Get all entries for a device"""
        ids = self.index_by_device.get(device, [])
        return [self.entries[id] for id in ids if id in self.entries]
    
    def get_secrets(self) -> List[VaultEntry]:
        """Get all secret/magic entries"""
        return [e for e in self.entries.values() if e.knowledge_type == KnowledgeType.SECRET]
    
    def get_top_fixes(self, limit: int = 10) -> List[VaultEntry]:
        """Get most reliable fixes"""
        fixes = [e for e in self.entries.values() if e.knowledge_type == KnowledgeType.FIX]
        fixes.sort(key=lambda x: (x.calculate_reliability_score(), x.success_count), reverse=True)
        return fixes[:limit]
    
    # ═══════════════════════════════════════════════════════════════
    # UPDATING KNOWLEDGE
    # ═══════════════════════════════════════════════════════════════
    
    def record_success(self, entry_id: str, genius_id: str):
        """Record a successful use of this knowledge"""
        if entry_id not in self.entries:
            return
        
        entry = self.entries[entry_id]
        entry.success_count += 1
        entry.last_verified = datetime.now()
        entry.updated_at = datetime.now()
        
        # Add contributor
        if genius_id not in entry.contributors and genius_id != entry.discovered_by:
            entry.contributors.append(genius_id)
        
        # Upgrade confidence if enough successes
        if entry.success_count >= 10 and entry.confidence != ConfidenceLevel.PROVEN:
            entry.confidence = ConfidenceLevel.PROVEN
        elif entry.success_count >= 5 and entry.confidence == ConfidenceLevel.EXPERIMENTAL:
            entry.confidence = ConfidenceLevel.RELIABLE
        
        self.total_success += 1
    
    def record_failure(self, entry_id: str, genius_id: str, notes: str = None):
        """Record a failed use of this knowledge"""
        if entry_id not in self.entries:
            return
        
        entry = self.entries[entry_id]
        entry.failure_count += 1
        entry.updated_at = datetime.now()
        
        # Downgrade confidence if too many failures
        failure_rate = entry.failure_count / (entry.success_count + entry.failure_count)
        if failure_rate > 0.3 and entry.confidence in [ConfidenceLevel.PROVEN, ConfidenceLevel.RELIABLE]:
            entry.confidence = ConfidenceLevel.PROBABLE
        
        self.total_failure += 1
    
    def add_contributor(self, entry_id: str, genius_id: str, additional_notes: str = None):
        """Add a genius as contributor with additional knowledge"""
        if entry_id not in self.entries:
            return
        
        entry = self.entries[entry_id]
        
        if genius_id not in entry.contributors:
            entry.contributors.append(genius_id)
        
        if additional_notes:
            if entry.secret_notes:
                entry.secret_notes += f"\n[{genius_id}]: {additional_notes}"
            else:
                entry.secret_notes = f"[{genius_id}]: {additional_notes}"
        
        entry.updated_at = datetime.now()
        entry.version += 1
    
    def supersede(self, old_entry_id: str, new_entry_id: str):
        """Mark old knowledge as superseded by new knowledge"""
        if old_entry_id in self.entries and new_entry_id in self.entries:
            self.entries[old_entry_id].superseded_by = new_entry_id
            self.entries[new_entry_id].supersedes = old_entry_id
    
    # ═══════════════════════════════════════════════════════════════
    # AUTO-ORGANIZATION
    # ═══════════════════════════════════════════════════════════════
    
    def _auto_link_related(self, new_entry: VaultEntry):
        """Automatically find and link related entries"""
        related = []
        
        for entry in self.entries.values():
            if entry.id == new_entry.id:
                continue
            
            # Same categories
            common_cats = set(entry.categories) & set(new_entry.categories)
            if len(common_cats) >= 2:
                related.append(entry.id)
                continue
            
            # Same tags
            common_tags = set(entry.tags) & set(new_entry.tags)
            if len(common_tags) >= 3:
                related.append(entry.id)
                continue
            
            # Same device
            common_devices = set(entry.affected_devices) & set(new_entry.affected_devices)
            if common_devices:
                related.append(entry.id)
        
        new_entry.related_entries = related[:10]  # Max 10 related
    
    def organize_by_pattern(self) -> Dict[str, List[str]]:
        """Auto-organize entries by detected patterns"""
        patterns = {}
        
        for entry in self.entries.values():
            # Group by primary category + first tag
            if entry.categories and entry.tags:
                key = f"{entry.categories[0]}:{entry.tags[0]}"
                if key not in patterns:
                    patterns[key] = []
                patterns[key].append(entry.id)
        
        return patterns
    
    # ═══════════════════════════════════════════════════════════════
    # STATISTICS
    # ═══════════════════════════════════════════════════════════════
    
    def get_stats(self) -> Dict:
        """Get vault statistics"""
        return {
            "total_entries": len(self.entries),
            "total_fixes": sum(1 for e in self.entries.values() if e.knowledge_type == KnowledgeType.FIX),
            "total_patterns": sum(1 for e in self.entries.values() if e.knowledge_type == KnowledgeType.PATTERN),
            "total_secrets": sum(1 for e in self.entries.values() if e.knowledge_type == KnowledgeType.SECRET),
            "total_success": self.total_success,
            "total_failure": self.total_failure,
            "success_rate": self.total_success / (self.total_success + self.total_failure) if (self.total_success + self.total_failure) > 0 else 0,
            "categories_count": len(self.index_by_category),
            "tags_count": len(self.index_by_tag),
            "devices_indexed": len(self.index_by_device),
            "os_indexed": len(self.index_by_os),
            "geniuses_contributing": len(self.index_by_genius),
            "proven_knowledge": sum(1 for e in self.entries.values() if e.confidence == ConfidenceLevel.PROVEN),
            "last_sync": self.last_sync.isoformat()
        }
    
    def get_genius_contributions(self, genius_id: str) -> Dict:
        """Get contribution stats for a genius"""
        entries = self.index_by_genius.get(genius_id, [])
        
        return {
            "genius_id": genius_id,
            "total_contributions": len(entries),
            "entries": [self.entries[id].to_dict() for id in entries if id in self.entries]
        }


# ═══════════════════════════════════════════════════════════════════════════════
# SINGLETON INSTANCE
# ═══════════════════════════════════════════════════════════════════════════════

vault = NoizyVault()


# ═══════════════════════════════════════════════════════════════════════════════
# QUICK FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

def add_fix(title, description, solution, genius_id, categories, tags, **kwargs):
    """Quick add fix"""
    return vault.add_fix(title, description, solution, genius_id, categories, tags, **kwargs)

def add_secret(title, description, magic, genius_id, categories, tags):
    """Quick add secret"""
    return vault.add_secret(title, description, magic, genius_id, categories, tags)

def search(query, **kwargs):
    """Quick search"""
    return vault.search(query, **kwargs)

def record_success(entry_id, genius_id):
    """Quick record success"""
    return vault.record_success(entry_id, genius_id)

def record_failure(entry_id, genius_id, notes=None):
    """Quick record failure"""
    return vault.record_failure(entry_id, genius_id, notes)

def stats():
    """Quick stats"""
    return vault.get_stats()

