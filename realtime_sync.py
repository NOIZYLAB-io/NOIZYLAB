"""
═══════════════════════════════════════════════════════════════════════════════
                      NOIZYVAULT REALTIME SYNC ENGINE
═══════════════════════════════════════════════════════════════════════════════

ALL 25 GENIUSES CONSTANTLY SHARE AND ORGANIZE DATA IN REALTIME.

When one Genius learns something, ALL Geniuses know it instantly.
The vault grows with every repair.
Nothing is lost. Everything is shared.
"""

from typing import Dict, List, Callable, Any
from dataclasses import dataclass
from datetime import datetime
import asyncio
import json
from enum import Enum

from .vault_core import vault, VaultEntry, KnowledgeType


class SyncEventType(Enum):
    """Types of sync events"""
    NEW_ENTRY = "new_entry"
    ENTRY_UPDATED = "entry_updated"
    SUCCESS_RECORDED = "success_recorded"
    FAILURE_RECORDED = "failure_recorded"
    PATTERN_DETECTED = "pattern_detected"
    SECRET_ADDED = "secret_added"
    GENIUS_INSIGHT = "genius_insight"
    CROSS_REFERENCE = "cross_reference"


@dataclass
class SyncEvent:
    """A realtime sync event"""
    event_type: SyncEventType
    entry_id: str
    genius_id: str
    data: Dict
    timestamp: datetime
    
    def to_dict(self) -> Dict:
        return {
            "event_type": self.event_type.value,
            "entry_id": self.entry_id,
            "genius_id": self.genius_id,
            "data": self.data,
            "timestamp": self.timestamp.isoformat()
        }


class RealtimeSyncEngine:
    """
    The engine that keeps all 25 Geniuses in perfect sync.
    
    When GENIUS_APPLE fixes a Mac issue, GENIUS_STORAGE immediately knows
    if there's a storage component. GENIUS_DATA knows if backup is relevant.
    
    This is the nervous system of the NoizyVault.
    """
    
    def __init__(self):
        self.subscribers: Dict[str, List[Callable]] = {}  # genius_id -> callbacks
        self.event_queue: List[SyncEvent] = []
        self.event_history: List[SyncEvent] = []
        self.is_running = False
        
        # Cross-reference rules
        self.cross_ref_rules: List[Dict] = []
        self._init_cross_ref_rules()
    
    def _init_cross_ref_rules(self):
        """Initialize automatic cross-reference rules"""
        self.cross_ref_rules = [
            {
                "if_category": "storage",
                "notify": ["GENIUS_DATA", "GENIUS_STORAGE"],
                "reason": "Storage issues may need data recovery awareness"
            },
            {
                "if_category": "network",
                "notify": ["GENIUS_NETWORK", "GENIUS_WIRELESS", "GENIUS_SECURITY"],
                "reason": "Network issues span multiple domains"
            },
            {
                "if_category": "security",
                "notify": ["GENIUS_SECURITY", "GENIUS_DATA", "GENIUS_NETWORK"],
                "reason": "Security issues require multi-domain awareness"
            },
            {
                "if_category": "boot",
                "notify": ["GENIUS_APPLE", "GENIUS_WINDOWS", "GENIUS_LINUX", "GENIUS_STORAGE"],
                "reason": "Boot issues can be OS or storage related"
            },
            {
                "if_tag": "slow",
                "notify": ["GENIUS_STORAGE", "GENIUS_MEMORY", "GENIUS_CPU"],
                "reason": "Performance issues need hardware analysis"
            },
            {
                "if_tag": "crash",
                "notify": ["GENIUS_SOFTWARE", "GENIUS_MEMORY", "GENIUS_GPU"],
                "reason": "Crashes can be software or hardware"
            },
            {
                "if_tag": "data_loss",
                "notify": ["GENIUS_DATA", "GENIUS_STORAGE", "GENIUS_SECURITY"],
                "reason": "Data loss is critical - all hands"
            }
        ]
    
    # ═══════════════════════════════════════════════════════════════
    # SUBSCRIPTION
    # ═══════════════════════════════════════════════════════════════
    
    def subscribe(self, genius_id: str, callback: Callable[[SyncEvent], None]):
        """Subscribe a genius to receive sync events"""
        if genius_id not in self.subscribers:
            self.subscribers[genius_id] = []
        self.subscribers[genius_id].append(callback)
    
    def unsubscribe(self, genius_id: str, callback: Callable = None):
        """Unsubscribe a genius"""
        if genius_id in self.subscribers:
            if callback:
                self.subscribers[genius_id].remove(callback)
            else:
                del self.subscribers[genius_id]
    
    # ═══════════════════════════════════════════════════════════════
    # EVENT BROADCASTING
    # ═══════════════════════════════════════════════════════════════
    
    def broadcast(self, event: SyncEvent):
        """Broadcast event to all subscribed geniuses"""
        self.event_queue.append(event)
        self.event_history.append(event)
        
        # Trim history to last 1000 events
        if len(self.event_history) > 1000:
            self.event_history = self.event_history[-1000:]
        
        # Notify all subscribers
        for genius_id, callbacks in self.subscribers.items():
            for callback in callbacks:
                try:
                    callback(event)
                except Exception as e:
                    print(f"[SYNC] Error notifying {genius_id}: {e}")
        
        # Auto cross-reference
        self._auto_cross_reference(event)
    
    def _auto_cross_reference(self, event: SyncEvent):
        """Automatically cross-reference based on rules"""
        if event.event_type != SyncEventType.NEW_ENTRY:
            return
        
        entry = vault.entries.get(event.entry_id)
        if not entry:
            return
        
        notified = set()
        
        for rule in self.cross_ref_rules:
            should_notify = False
            
            if "if_category" in rule and rule["if_category"] in entry.categories:
                should_notify = True
            if "if_tag" in rule and rule["if_tag"] in entry.tags:
                should_notify = True
            
            if should_notify:
                for genius_id in rule["notify"]:
                    if genius_id not in notified and genius_id != event.genius_id:
                        notified.add(genius_id)
                        
                        # Create cross-reference event
                        xref_event = SyncEvent(
                            event_type=SyncEventType.CROSS_REFERENCE,
                            entry_id=event.entry_id,
                            genius_id=genius_id,
                            data={
                                "original_genius": event.genius_id,
                                "reason": rule["reason"],
                                "entry_title": entry.title
                            },
                            timestamp=datetime.now()
                        )
                        
                        # Notify specific genius
                        if genius_id in self.subscribers:
                            for callback in self.subscribers[genius_id]:
                                try:
                                    callback(xref_event)
                                except:
                                    pass
    
    # ═══════════════════════════════════════════════════════════════
    # EVENT CREATION HELPERS
    # ═══════════════════════════════════════════════════════════════
    
    def emit_new_entry(self, entry: VaultEntry, genius_id: str):
        """Emit event for new vault entry"""
        event = SyncEvent(
            event_type=SyncEventType.NEW_ENTRY,
            entry_id=entry.id,
            genius_id=genius_id,
            data={
                "title": entry.title,
                "type": entry.knowledge_type.value,
                "categories": entry.categories,
                "tags": entry.tags
            },
            timestamp=datetime.now()
        )
        self.broadcast(event)
    
    def emit_success(self, entry_id: str, genius_id: str):
        """Emit event for successful knowledge use"""
        entry = vault.entries.get(entry_id)
        event = SyncEvent(
            event_type=SyncEventType.SUCCESS_RECORDED,
            entry_id=entry_id,
            genius_id=genius_id,
            data={
                "title": entry.title if entry else "Unknown",
                "new_success_count": entry.success_count if entry else 0,
                "reliability": entry.calculate_reliability_score() if entry else 0
            },
            timestamp=datetime.now()
        )
        self.broadcast(event)
    
    def emit_failure(self, entry_id: str, genius_id: str, notes: str = None):
        """Emit event for failed knowledge use"""
        entry = vault.entries.get(entry_id)
        event = SyncEvent(
            event_type=SyncEventType.FAILURE_RECORDED,
            entry_id=entry_id,
            genius_id=genius_id,
            data={
                "title": entry.title if entry else "Unknown",
                "notes": notes,
                "new_failure_count": entry.failure_count if entry else 0
            },
            timestamp=datetime.now()
        )
        self.broadcast(event)
    
    def emit_pattern_detected(self, pattern_description: str, genius_id: str, related_entries: List[str]):
        """Emit event for detected pattern"""
        event = SyncEvent(
            event_type=SyncEventType.PATTERN_DETECTED,
            entry_id="",
            genius_id=genius_id,
            data={
                "pattern": pattern_description,
                "related_entries": related_entries,
                "occurrence_count": len(related_entries)
            },
            timestamp=datetime.now()
        )
        self.broadcast(event)
    
    def emit_insight(self, insight: str, genius_id: str, related_entry: str = None):
        """Emit a genius insight"""
        event = SyncEvent(
            event_type=SyncEventType.GENIUS_INSIGHT,
            entry_id=related_entry or "",
            genius_id=genius_id,
            data={
                "insight": insight
            },
            timestamp=datetime.now()
        )
        self.broadcast(event)
    
    # ═══════════════════════════════════════════════════════════════
    # PATTERN DETECTION
    # ═══════════════════════════════════════════════════════════════
    
    def detect_patterns(self) -> List[Dict]:
        """Analyze vault for emerging patterns"""
        patterns = []
        
        # Group recent entries by category
        recent = [e for e in vault.entries.values() 
                  if (datetime.now() - e.created_at).days < 7]
        
        category_counts = {}
        for entry in recent:
            for cat in entry.categories:
                if cat not in category_counts:
                    category_counts[cat] = []
                category_counts[cat].append(entry.id)
        
        # Detect spikes
        for cat, entries in category_counts.items():
            if len(entries) >= 5:
                patterns.append({
                    "type": "category_spike",
                    "category": cat,
                    "count": len(entries),
                    "entries": entries,
                    "message": f"Spike in {cat} issues: {len(entries)} in last 7 days"
                })
        
        # Group by tag combinations
        tag_combos = {}
        for entry in recent:
            if len(entry.tags) >= 2:
                combo = tuple(sorted(entry.tags[:3]))
                if combo not in tag_combos:
                    tag_combos[combo] = []
                tag_combos[combo].append(entry.id)
        
        for combo, entries in tag_combos.items():
            if len(entries) >= 3:
                patterns.append({
                    "type": "tag_pattern",
                    "tags": list(combo),
                    "count": len(entries),
                    "entries": entries,
                    "message": f"Pattern: {' + '.join(combo)} appearing together"
                })
        
        return patterns
    
    # ═══════════════════════════════════════════════════════════════
    # STATISTICS
    # ═══════════════════════════════════════════════════════════════
    
    def get_sync_stats(self) -> Dict:
        """Get sync engine statistics"""
        return {
            "subscribed_geniuses": len(self.subscribers),
            "events_in_queue": len(self.event_queue),
            "events_in_history": len(self.event_history),
            "cross_ref_rules": len(self.cross_ref_rules),
            "is_running": self.is_running,
            "recent_events": [e.to_dict() for e in self.event_history[-10:]]
        }


# ═══════════════════════════════════════════════════════════════════════════════
# SINGLETON INSTANCE
# ═══════════════════════════════════════════════════════════════════════════════

sync_engine = RealtimeSyncEngine()


# ═══════════════════════════════════════════════════════════════════════════════
# QUICK FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

def subscribe(genius_id: str, callback: Callable):
    """Quick subscribe"""
    return sync_engine.subscribe(genius_id, callback)

def emit_new(entry: VaultEntry, genius_id: str):
    """Quick emit new entry"""
    return sync_engine.emit_new_entry(entry, genius_id)

def emit_success(entry_id: str, genius_id: str):
    """Quick emit success"""
    return sync_engine.emit_success(entry_id, genius_id)

def emit_failure(entry_id: str, genius_id: str, notes: str = None):
    """Quick emit failure"""
    return sync_engine.emit_failure(entry_id, genius_id, notes)

def detect_patterns():
    """Quick pattern detection"""
    return sync_engine.detect_patterns()

def stats():
    """Quick stats"""
    return sync_engine.get_sync_stats()

