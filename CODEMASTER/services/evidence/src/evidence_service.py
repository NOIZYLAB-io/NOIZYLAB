#!/usr/bin/env python3
"""
📦 EVIDENCE SERVICE - The Truth System
=======================================
Every query/action produces an Evidence Pack:
- claims → evidence pointers → supported/partial/unsupported
- Verifier strips unsupported claims
- If no evidence: outputs UNKNOWN + Next retrieval step

NON-NEGOTIABLE: No claim without evidence. Period.
"""

import os
import json
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any, List
from dataclasses import dataclass, asdict, field
from enum import Enum
import uuid

# ═══════════════════════════════════════════════════════════════
# 🔧 CONFIGURATION
# ═══════════════════════════════════════════════════════════════

EVIDENCE_ROOT = Path(os.environ.get("EVIDENCE_ROOT", "/Users/m2ultra/NOIZYLAB/GABRIEL/NOIZY_AI/evidence_packs"))

# ═══════════════════════════════════════════════════════════════
# 📦 DATA MODELS
# ═══════════════════════════════════════════════════════════════

class SupportLevel(str, Enum):
    """How well a claim is supported by evidence"""
    SUPPORTED = "supported"          # Full evidence backing
    PARTIAL = "partial"              # Some evidence, gaps exist
    UNSUPPORTED = "unsupported"      # No evidence found
    UNKNOWN = "unknown"              # Cannot determine
    CONTRADICTED = "contradicted"    # Evidence contradicts claim

@dataclass
class EvidencePointer:
    """Points to source evidence"""
    id: str
    source_type: str          # file, api, database, observation
    source_path: str          # Path or identifier to source
    excerpt: str              # Relevant excerpt
    timestamp: str            # When evidence was captured
    hash: str                 # Hash of source at capture time
    confidence: float         # 0.0-1.0 confidence in source
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Claim:
    """A single claim that needs evidence"""
    id: str
    statement: str            # The claim being made
    category: str             # Type of claim
    evidence: List[EvidencePointer] = field(default_factory=list)
    support_level: SupportLevel = SupportLevel.UNKNOWN
    reasoning: str = ""       # Why this support level
    next_steps: List[str] = field(default_factory=list)  # If unsupported

@dataclass 
class EvidencePack:
    """Complete evidence package for a query/action"""
    id: str
    created_at: str
    query: str                         # Original query/action
    context: Dict[str, Any]            # Context of the query
    claims: List[Claim]                # All claims made
    summary: str                       # Human-readable summary
    overall_support: SupportLevel      # Overall pack support level
    verified: bool                     # Has passed verification
    verifier_notes: List[str]          # Notes from verification
    hash: str                          # Hash of entire pack
    metadata: Dict[str, Any] = field(default_factory=dict)

# ═══════════════════════════════════════════════════════════════
# 📦 EVIDENCE PACK GENERATOR
# ═══════════════════════════════════════════════════════════════

class EvidencePackGenerator:
    """Generate evidence packs for queries and actions"""
    
    def __init__(self):
        EVIDENCE_ROOT.mkdir(parents=True, exist_ok=True)
    
    def create_pack(self, query: str, context: Dict[str, Any] = None) -> EvidencePack:
        """Create a new evidence pack"""
        pack_id = f"ep_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}_{uuid.uuid4().hex[:8]}"
        
        return EvidencePack(
            id=pack_id,
            created_at=datetime.utcnow().isoformat(),
            query=query,
            context=context or {},
            claims=[],
            summary="",
            overall_support=SupportLevel.UNKNOWN,
            verified=False,
            verifier_notes=[],
            hash="",
            metadata={}
        )
    
    def add_claim(self, pack: EvidencePack, statement: str, 
                  category: str = "general") -> Claim:
        """Add a claim to the pack"""
        claim = Claim(
            id=f"claim_{len(pack.claims)+1}",
            statement=statement,
            category=category,
            evidence=[],
            support_level=SupportLevel.UNKNOWN
        )
        pack.claims.append(claim)
        return claim
    
    def add_evidence(self, claim: Claim, source_type: str, source_path: str,
                     excerpt: str, confidence: float = 1.0, 
                     metadata: Dict[str, Any] = None) -> EvidencePointer:
        """Add evidence to a claim"""
        evidence = EvidencePointer(
            id=f"ev_{len(claim.evidence)+1}",
            source_type=source_type,
            source_path=source_path,
            excerpt=excerpt[:2000],  # Limit excerpt size
            timestamp=datetime.utcnow().isoformat(),
            hash=hashlib.sha256(excerpt.encode()).hexdigest()[:16],
            confidence=min(1.0, max(0.0, confidence)),
            metadata=metadata or {}
        )
        claim.evidence.append(evidence)
        return evidence
    
    def evaluate_claim(self, claim: Claim) -> SupportLevel:
        """Evaluate support level for a claim"""
        if not claim.evidence:
            claim.support_level = SupportLevel.UNSUPPORTED
            claim.reasoning = "No evidence provided"
            claim.next_steps = ["Search vault for relevant sources", 
                               "Query external APIs",
                               "Mark as UNKNOWN if unverifiable"]
            return claim.support_level
        
        # Calculate average confidence
        avg_confidence = sum(e.confidence for e in claim.evidence) / len(claim.evidence)
        
        if avg_confidence >= 0.8 and len(claim.evidence) >= 1:
            claim.support_level = SupportLevel.SUPPORTED
            claim.reasoning = f"Backed by {len(claim.evidence)} evidence(s) with avg confidence {avg_confidence:.2f}"
        elif avg_confidence >= 0.5:
            claim.support_level = SupportLevel.PARTIAL
            claim.reasoning = f"Partially backed ({avg_confidence:.2f} confidence). Needs more evidence."
            claim.next_steps = ["Find additional corroborating sources"]
        else:
            claim.support_level = SupportLevel.UNSUPPORTED
            claim.reasoning = f"Low confidence evidence ({avg_confidence:.2f})"
            claim.next_steps = ["Verify source reliability", "Find better sources"]
        
        return claim.support_level
    
    def finalize(self, pack: EvidencePack) -> EvidencePack:
        """Finalize the evidence pack"""
        # Evaluate all claims
        support_levels = []
        for claim in pack.claims:
            self.evaluate_claim(claim)
            support_levels.append(claim.support_level)
        
        # Determine overall support
        if not support_levels:
            pack.overall_support = SupportLevel.UNKNOWN
        elif all(s == SupportLevel.SUPPORTED for s in support_levels):
            pack.overall_support = SupportLevel.SUPPORTED
        elif SupportLevel.CONTRADICTED in support_levels:
            pack.overall_support = SupportLevel.CONTRADICTED
        elif SupportLevel.UNSUPPORTED in support_levels:
            pack.overall_support = SupportLevel.PARTIAL
        else:
            pack.overall_support = SupportLevel.PARTIAL
        
        # Generate summary
        supported = sum(1 for s in support_levels if s == SupportLevel.SUPPORTED)
        total = len(support_levels)
        pack.summary = f"{supported}/{total} claims fully supported. Overall: {pack.overall_support.value}"
        
        # Compute pack hash
        pack_content = json.dumps(asdict(pack), sort_keys=True, default=str)
        pack.hash = hashlib.sha256(pack_content.encode()).hexdigest()
        
        return pack
    
    def save(self, pack: EvidencePack) -> Path:
        """Save evidence pack to disk"""
        date_path = datetime.utcnow().strftime("%Y/%m/%d")
        save_dir = EVIDENCE_ROOT / date_path
        save_dir.mkdir(parents=True, exist_ok=True)
        
        pack_path = save_dir / f"{pack.id}.json"
        with open(pack_path, 'w') as f:
            json.dump(asdict(pack), f, indent=2, default=str)
        
        return pack_path

# ═══════════════════════════════════════════════════════════════
# ✅ EVIDENCE VERIFIER (FAIL-CLOSED)
# ═══════════════════════════════════════════════════════════════

class EvidenceVerifier:
    """
    Verify evidence packs - FAIL-CLOSED
    
    Rules:
    1. Strip ALL unsupported claims
    2. If no evidence: output UNKNOWN + retrieval steps
    3. Never pass unverified claims through
    """
    
    def verify(self, pack: EvidencePack) -> EvidencePack:
        """
        Verify evidence pack - strips unsupported claims.
        
        Returns a verified copy with only supported claims.
        """
        pack.verifier_notes = []
        verified_claims = []
        stripped_claims = []
        
        for claim in pack.claims:
            # Re-evaluate each claim
            if claim.support_level == SupportLevel.SUPPORTED:
                # Verify evidence is real
                valid_evidence = self._verify_evidence(claim.evidence)
                if valid_evidence:
                    verified_claims.append(claim)
                    pack.verifier_notes.append(f"✅ PASS: {claim.statement[:50]}...")
                else:
                    stripped_claims.append(claim)
                    pack.verifier_notes.append(f"❌ STRIP (invalid evidence): {claim.statement[:50]}...")
            
            elif claim.support_level == SupportLevel.PARTIAL:
                # Include with warning
                claim.statement = f"[PARTIAL] {claim.statement}"
                verified_claims.append(claim)
                pack.verifier_notes.append(f"⚠️ PARTIAL: {claim.statement[:50]}...")
            
            else:
                # Strip unsupported/unknown claims
                stripped_claims.append(claim)
                pack.verifier_notes.append(f"❌ STRIP ({claim.support_level.value}): {claim.statement[:50]}...")
        
        # Update pack
        pack.claims = verified_claims
        pack.verified = True
        
        # If nothing survives verification
        if not verified_claims:
            pack.overall_support = SupportLevel.UNKNOWN
            pack.summary = "UNKNOWN - No claims could be verified. Next steps required."
            pack.verifier_notes.append("⚠️ FAIL-CLOSED: All claims stripped. Output is UNKNOWN.")
            
            # Add retrieval steps
            unknown_claim = Claim(
                id="unknown_result",
                statement="Unable to provide verified answer",
                category="system",
                support_level=SupportLevel.UNKNOWN,
                reasoning="All original claims failed verification",
                next_steps=[
                    "Search vault with expanded query",
                    "Query external knowledge sources",
                    "Request human input for clarification",
                    "Mark as 'cannot determine' if exhausted"
                ]
            )
            pack.claims = [unknown_claim]
        else:
            # Recalculate overall support
            supports = [c.support_level for c in verified_claims]
            if all(s == SupportLevel.SUPPORTED for s in supports):
                pack.overall_support = SupportLevel.SUPPORTED
            else:
                pack.overall_support = SupportLevel.PARTIAL
        
        # Add verification metadata
        pack.metadata["verified_at"] = datetime.utcnow().isoformat()
        pack.metadata["claims_passed"] = len(verified_claims)
        pack.metadata["claims_stripped"] = len(stripped_claims)
        
        # Recompute hash
        pack_content = json.dumps(asdict(pack), sort_keys=True, default=str)
        pack.hash = hashlib.sha256(pack_content.encode()).hexdigest()
        
        return pack
    
    def _verify_evidence(self, evidence: List[EvidencePointer]) -> bool:
        """Verify evidence pointers are valid"""
        if not evidence:
            return False
        
        for e in evidence:
            # Check source exists (for files)
            if e.source_type == "file":
                if not Path(e.source_path).exists():
                    return False
            
            # Check confidence threshold
            if e.confidence < 0.3:
                return False
        
        return True

# ═══════════════════════════════════════════════════════════════
# 🎯 CONVENIENCE FUNCTIONS
# ═══════════════════════════════════════════════════════════════

def create_evidence_pack(query: str, claims_with_evidence: List[Dict]) -> EvidencePack:
    """
    Convenience function to create a complete evidence pack.
    
    Args:
        query: The original query
        claims_with_evidence: List of dicts with 'statement', 'evidence' (list of dicts)
    
    Returns:
        Verified EvidencePack
    """
    generator = EvidencePackGenerator()
    verifier = EvidenceVerifier()
    
    pack = generator.create_pack(query)
    
    for claim_data in claims_with_evidence:
        claim = generator.add_claim(pack, claim_data['statement'], 
                                   claim_data.get('category', 'general'))
        
        for ev in claim_data.get('evidence', []):
            generator.add_evidence(
                claim,
                source_type=ev.get('source_type', 'observation'),
                source_path=ev.get('source_path', 'unknown'),
                excerpt=ev.get('excerpt', ''),
                confidence=ev.get('confidence', 0.5)
            )
    
    pack = generator.finalize(pack)
    pack = verifier.verify(pack)
    
    generator.save(pack)
    
    return pack

# ═══════════════════════════════════════════════════════════════
# 🚀 CLI
# ═══════════════════════════════════════════════════════════════

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="📦 EVIDENCE SERVICE")
    parser.add_argument("command", choices=["create", "verify", "list", "demo"])
    parser.add_argument("args", nargs="*")
    
    args = parser.parse_args()
    
    if args.command == "demo":
        print("🔬 Running Evidence Pack Demo...\n")
        
        # Create a demo pack
        pack = create_evidence_pack(
            query="What is the status of the MC96 network?",
            claims_with_evidence=[
                {
                    "statement": "MC96 has 12 active ports",
                    "category": "network",
                    "evidence": [
                        {
                            "source_type": "api",
                            "source_path": "/api/mc96/status",
                            "excerpt": "{'active_ports': 12, 'timestamp': '2025-12-29T14:00:00'}",
                            "confidence": 0.95
                        }
                    ]
                },
                {
                    "statement": "Network latency is under 5ms",
                    "category": "network",
                    "evidence": [
                        {
                            "source_type": "observation",
                            "source_path": "ping_test",
                            "excerpt": "avg latency: 3.2ms",
                            "confidence": 0.9
                        }
                    ]
                },
                {
                    "statement": "All firewalls are properly configured",
                    "category": "security",
                    "evidence": []  # No evidence - will be stripped
                }
            ]
        )
        
        print(f"📦 Evidence Pack: {pack.id}")
        print(f"   Query: {pack.query}")
        print(f"   Overall Support: {pack.overall_support.value}")
        print(f"   Verified: {pack.verified}")
        print(f"\n📋 Claims:")
        for claim in pack.claims:
            print(f"   [{claim.support_level.value}] {claim.statement}")
            if claim.next_steps:
                print(f"      Next steps: {claim.next_steps}")
        print(f"\n📝 Verifier Notes:")
        for note in pack.verifier_notes:
            print(f"   {note}")
    
    elif args.command == "list":
        print(f"📦 Evidence Packs in {EVIDENCE_ROOT}:")
        for pack_file in EVIDENCE_ROOT.rglob("*.json"):
            print(f"   {pack_file.relative_to(EVIDENCE_ROOT)}")

if __name__ == "__main__":
    main()
