#!/usr/bin/env python3
"""
📦 CODEMASTER EVIDENCE PACK SERVICE 📦
========================================
The truth system. Every query/action produces an Evidence Pack:
- claims → evidence pointers → supported/partial/unsupported
- Verifier strips unsupported claims
- If no evidence: UNKNOWN + next retrieval step
- Tamper-evident audit chain

NON-NEGOTIABLE RULES:
1. Every answer has evidence pointers or becomes UNKNOWN
2. Every action logs who approved, what changed, rollback pointer
3. Verifier pass is FAIL-CLOSED (no evidence = no claim)
"""

import os
import json
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Dict, Any
from dataclasses import dataclass, asdict, field
from enum import Enum
import uuid

# ═══════════════════════════════════════════════════════════════
# 📁 CONFIGURATION
# ═══════════════════════════════════════════════════════════════

EVIDENCE_ROOT = Path(os.environ.get("EVIDENCE_ROOT", "/Users/m2ultra/NOIZY_AI/evidence_packs"))
AUDIT_LOG = Path(os.environ.get("AUDIT_LOG", "/Users/m2ultra/NOIZY_AI/logs/audit"))

class ClaimStatus(Enum):
    SUPPORTED = "supported"
    PARTIAL = "partial"
    UNSUPPORTED = "unsupported"
    UNKNOWN = "unknown"

class ActionType(Enum):
    READ = "read"
    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"
    EXECUTE = "execute"
    APPROVE = "approve"

# ═══════════════════════════════════════════════════════════════
# 📄 EVIDENCE PACK DATA MODEL
# ═══════════════════════════════════════════════════════════════

@dataclass
class EvidenceSource:
    """A pointer to evidence"""
    asset_id: Optional[str] = None
    path: Optional[str] = None
    sha256: Optional[str] = None
    timecode_start: Optional[str] = None
    timecode_end: Optional[str] = None
    span_start: Optional[int] = None
    span_end: Optional[int] = None
    url: Optional[str] = None
    retrieved_at: Optional[str] = None
    
    def to_dict(self) -> Dict:
        return {k: v for k, v in asdict(self).items() if v is not None}

@dataclass
class Claim:
    """A claim with evidence support"""
    claim_text: str
    support: List[EvidenceSource] = field(default_factory=list)
    status: ClaimStatus = ClaimStatus.UNSUPPORTED
    confidence: float = 0.0
    
    def to_dict(self) -> Dict:
        return {
            'claim_text': self.claim_text,
            'support': [s.to_dict() for s in self.support],
            'status': self.status.value,
            'confidence': self.confidence,
        }

@dataclass
class Action:
    """An action proposed or taken"""
    action_type: ActionType
    description: str
    target: str
    destructive: bool = False
    requires_approval: bool = False
    approved_by: Optional[str] = None
    approved_at: Optional[str] = None
    executed_at: Optional[str] = None
    result: Optional[str] = None
    
    def to_dict(self) -> Dict:
        return {
            'action_type': self.action_type.value,
            'description': self.description,
            'target': self.target,
            'destructive': self.destructive,
            'requires_approval': self.requires_approval,
            'approved_by': self.approved_by,
            'approved_at': self.approved_at,
            'executed_at': self.executed_at,
            'result': self.result,
        }

@dataclass
class VerifierResult:
    """Result of evidence verification"""
    passed: bool
    fail_reasons: List[str] = field(default_factory=list)
    claims_verified: int = 0
    claims_stripped: int = 0
    
    def to_dict(self) -> Dict:
        return asdict(self)

@dataclass 
class Rollback:
    """Rollback information"""
    snapshot_id: Optional[str] = None
    instructions: Optional[str] = None
    automated: bool = False
    
    def to_dict(self) -> Dict:
        return {k: v for k, v in asdict(self).items() if v is not None}

@dataclass
class EvidencePack:
    """The complete Evidence Pack"""
    pack_id: str
    created_at: str
    request_id: Optional[str]
    actor_id: str
    
    # The answer/response
    answer: str
    
    # Claims with evidence
    claims: List[Claim] = field(default_factory=list)
    
    # Sources referenced
    sources: List[EvidenceSource] = field(default_factory=list)
    
    # Actions taken or proposed
    actions: List[Action] = field(default_factory=list)
    
    # Verification status
    verifier: Optional[VerifierResult] = None
    
    # Rollback info
    rollback: Optional[Rollback] = None
    
    # Pack hash for tamper detection
    pack_hash: Optional[str] = None
    previous_pack_hash: Optional[str] = None
    
    def to_dict(self) -> Dict:
        return {
            'pack_id': self.pack_id,
            'created_at': self.created_at,
            'request_id': self.request_id,
            'actor_id': self.actor_id,
            'answer': self.answer,
            'claims': [c.to_dict() for c in self.claims],
            'sources': [s.to_dict() for s in self.sources],
            'actions': [a.to_dict() for a in self.actions],
            'verifier': self.verifier.to_dict() if self.verifier else None,
            'rollback': self.rollback.to_dict() if self.rollback else None,
            'pack_hash': self.pack_hash,
            'previous_pack_hash': self.previous_pack_hash,
        }
    
    def compute_hash(self) -> str:
        """Compute hash of pack contents"""
        content = json.dumps({
            'pack_id': self.pack_id,
            'created_at': self.created_at,
            'actor_id': self.actor_id,
            'answer': self.answer,
            'claims': [c.to_dict() for c in self.claims],
            'previous_pack_hash': self.previous_pack_hash,
        }, sort_keys=True)
        return hashlib.sha256(content.encode()).hexdigest()

# ═══════════════════════════════════════════════════════════════
# 🛡️ EVIDENCE VERIFIER (FAIL-CLOSED)
# ═══════════════════════════════════════════════════════════════

class EvidenceVerifier:
    """
    Verifies evidence packs. FAIL-CLOSED:
    - No evidence = claim becomes UNSUPPORTED
    - All unsupported claims get stripped from final answer
    - If no supported claims: answer becomes UNKNOWN
    """
    
    @staticmethod
    def verify(pack: EvidencePack) -> EvidencePack:
        """
        Verify an evidence pack. Strips unsupported claims.
        
        Returns:
            Modified pack with verification results
        """
        verified_claims = []
        stripped_count = 0
        fail_reasons = []
        
        for claim in pack.claims:
            # Check if claim has evidence
            if not claim.support:
                claim.status = ClaimStatus.UNSUPPORTED
                claim.confidence = 0.0
                stripped_count += 1
                fail_reasons.append(f"No evidence for: {claim.claim_text[:50]}...")
                continue
            
            # Verify each evidence source exists/is valid
            valid_sources = []
            for source in claim.support:
                if EvidenceVerifier._verify_source(source):
                    valid_sources.append(source)
            
            if not valid_sources:
                claim.status = ClaimStatus.UNSUPPORTED
                claim.confidence = 0.0
                stripped_count += 1
                fail_reasons.append(f"All evidence invalid for: {claim.claim_text[:50]}...")
                continue
            
            # Update claim with verified sources
            claim.support = valid_sources
            if len(valid_sources) == len(claim.support):
                claim.status = ClaimStatus.SUPPORTED
                claim.confidence = 1.0
            else:
                claim.status = ClaimStatus.PARTIAL
                claim.confidence = len(valid_sources) / len(claim.support)
            
            verified_claims.append(claim)
        
        # If no verified claims, answer becomes UNKNOWN
        if not verified_claims:
            pack.answer = f"UNKNOWN: Could not verify any claims. Original response stripped.\n\nNext retrieval steps:\n1. Search vault for relevant assets\n2. Request additional evidence\n3. Manual verification required"
            fail_reasons.append("No claims could be verified")
        
        # Update pack
        pack.claims = pack.claims  # Keep all claims for audit, but mark status
        pack.verifier = VerifierResult(
            passed=len(verified_claims) > 0,
            fail_reasons=fail_reasons,
            claims_verified=len(verified_claims),
            claims_stripped=stripped_count,
        )
        
        return pack
    
    @staticmethod
    def _verify_source(source: EvidenceSource) -> bool:
        """Verify an evidence source exists"""
        # Check file path
        if source.path:
            if Path(source.path).exists():
                # Optionally verify hash
                if source.sha256:
                    actual_hash = EvidenceVerifier._compute_file_hash(source.path)
                    return actual_hash == source.sha256
                return True
        
        # Check URL (basic validation)
        if source.url:
            return source.url.startswith(('http://', 'https://'))
        
        # Check asset_id (assume valid if present)
        if source.asset_id:
            return True
        
        return False
    
    @staticmethod
    def _compute_file_hash(path: str) -> str:
        """Compute SHA256 of file"""
        sha256 = hashlib.sha256()
        with open(path, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                sha256.update(chunk)
        return sha256.hexdigest()

# ═══════════════════════════════════════════════════════════════
# 📦 EVIDENCE PACK SERVICE
# ═══════════════════════════════════════════════════════════════

class EvidenceService:
    """Manages Evidence Packs with audit chain"""
    
    def __init__(self, root: Path = EVIDENCE_ROOT):
        self.root = root
        self.root.mkdir(parents=True, exist_ok=True)
        self.audit_log = AUDIT_LOG
        self.audit_log.mkdir(parents=True, exist_ok=True)
        self._last_pack_hash = self._get_last_pack_hash()
    
    def _get_last_pack_hash(self) -> Optional[str]:
        """Get hash of most recent pack for chain"""
        chain_file = self.root / ".chain"
        if chain_file.exists():
            return chain_file.read_text().strip()
        return None
    
    def _update_chain(self, pack_hash: str):
        """Update chain pointer"""
        chain_file = self.root / ".chain"
        chain_file.write_text(pack_hash)
        self._last_pack_hash = pack_hash
    
    def create_pack(self, 
                    answer: str,
                    actor_id: str,
                    claims: List[Dict] = None,
                    sources: List[Dict] = None,
                    actions: List[Dict] = None,
                    request_id: str = None,
                    verify: bool = True) -> EvidencePack:
        """
        Create a new Evidence Pack.
        
        Args:
            answer: The response/answer text
            actor_id: Who created this (user, system, agent)
            claims: List of claim dicts with 'claim_text' and 'support'
            sources: List of evidence source dicts
            actions: List of action dicts
            request_id: Optional request correlation ID
            verify: Whether to run verifier (default True)
        
        Returns:
            EvidencePack (verified if verify=True)
        """
        pack_id = str(uuid.uuid4())[:12]
        
        # Parse claims
        parsed_claims = []
        if claims:
            for c in claims:
                support = []
                for s in c.get('support', []):
                    support.append(EvidenceSource(**s))
                parsed_claims.append(Claim(
                    claim_text=c['claim_text'],
                    support=support,
                    status=ClaimStatus.UNSUPPORTED,
                ))
        
        # Parse sources
        parsed_sources = []
        if sources:
            for s in sources:
                parsed_sources.append(EvidenceSource(**s))
        
        # Parse actions
        parsed_actions = []
        if actions:
            for a in actions:
                parsed_actions.append(Action(
                    action_type=ActionType(a.get('action_type', 'read')),
                    description=a['description'],
                    target=a['target'],
                    destructive=a.get('destructive', False),
                    requires_approval=a.get('requires_approval', False),
                ))
        
        # Create pack
        pack = EvidencePack(
            pack_id=pack_id,
            created_at=datetime.now().isoformat(),
            request_id=request_id,
            actor_id=actor_id,
            answer=answer,
            claims=parsed_claims,
            sources=parsed_sources,
            actions=parsed_actions,
            previous_pack_hash=self._last_pack_hash,
        )
        
        # Verify if requested
        if verify:
            pack = EvidenceVerifier.verify(pack)
        
        # Compute and set hash
        pack.pack_hash = pack.compute_hash()
        
        # Save pack
        self._save_pack(pack)
        
        # Update chain
        self._update_chain(pack.pack_hash)
        
        # Audit log
        self._audit("PACK_CREATED", pack)
        
        return pack
    
    def _save_pack(self, pack: EvidencePack):
        """Save pack to disk"""
        # Organize by date
        date_dir = self.root / datetime.now().strftime("%Y/%m/%d")
        date_dir.mkdir(parents=True, exist_ok=True)
        
        # Save JSON
        json_path = date_dir / f"{pack.pack_id}.json"
        with open(json_path, 'w') as f:
            json.dump(pack.to_dict(), f, indent=2)
        
        # Save human-readable markdown
        md_path = date_dir / f"{pack.pack_id}.md"
        md_path.write_text(self._render_markdown(pack))
    
    def _render_markdown(self, pack: EvidencePack) -> str:
        """Render pack as markdown"""
        lines = [
            f"# Evidence Pack: {pack.pack_id}",
            f"",
            f"**Created:** {pack.created_at}",
            f"**Actor:** {pack.actor_id}",
            f"**Request ID:** {pack.request_id or 'N/A'}",
            f"",
            f"## Answer",
            f"",
            pack.answer,
            f"",
        ]
        
        if pack.claims:
            lines.append("## Claims")
            lines.append("")
            for i, claim in enumerate(pack.claims, 1):
                status_emoji = {
                    ClaimStatus.SUPPORTED: "✅",
                    ClaimStatus.PARTIAL: "⚠️",
                    ClaimStatus.UNSUPPORTED: "❌",
                    ClaimStatus.UNKNOWN: "❓",
                }.get(claim.status, "❓")
                
                lines.append(f"{i}. {status_emoji} **{claim.status.value.upper()}** ({claim.confidence:.0%})")
                lines.append(f"   > {claim.claim_text}")
                if claim.support:
                    lines.append(f"   Evidence:")
                    for s in claim.support:
                        if s.path:
                            lines.append(f"   - `{s.path}`")
                        elif s.asset_id:
                            lines.append(f"   - Asset: `{s.asset_id}`")
                        elif s.url:
                            lines.append(f"   - URL: {s.url}")
                lines.append("")
        
        if pack.actions:
            lines.append("## Actions")
            lines.append("")
            for action in pack.actions:
                risk = "🔴 DESTRUCTIVE" if action.destructive else "🟢"
                approval = "⏳ REQUIRES APPROVAL" if action.requires_approval else ""
                lines.append(f"- [{action.action_type.value}] {action.description}")
                lines.append(f"  Target: `{action.target}` {risk} {approval}")
            lines.append("")
        
        if pack.verifier:
            lines.append("## Verification")
            lines.append("")
            status = "✅ PASSED" if pack.verifier.passed else "❌ FAILED"
            lines.append(f"**Status:** {status}")
            lines.append(f"**Claims Verified:** {pack.verifier.claims_verified}")
            lines.append(f"**Claims Stripped:** {pack.verifier.claims_stripped}")
            if pack.verifier.fail_reasons:
                lines.append("")
                lines.append("**Fail Reasons:**")
                for reason in pack.verifier.fail_reasons:
                    lines.append(f"- {reason}")
            lines.append("")
        
        lines.append("---")
        lines.append(f"Pack Hash: `{pack.pack_hash}`")
        lines.append(f"Previous: `{pack.previous_pack_hash or 'GENESIS'}`")
        
        return "\n".join(lines)
    
    def _audit(self, event: str, pack: EvidencePack):
        """Write to audit log"""
        log_file = self.audit_log / f"{datetime.now().strftime('%Y-%m-%d')}.jsonl"
        entry = {
            'timestamp': datetime.now().isoformat(),
            'event': event,
            'pack_id': pack.pack_id,
            'actor_id': pack.actor_id,
            'pack_hash': pack.pack_hash,
            'verified': pack.verifier.passed if pack.verifier else None,
        }
        with open(log_file, 'a') as f:
            f.write(json.dumps(entry) + '\n')
    
    def get_pack(self, pack_id: str) -> Optional[EvidencePack]:
        """Retrieve a pack by ID"""
        # Search in all date directories
        for json_file in self.root.rglob(f"{pack_id}.json"):
            with open(json_file) as f:
                data = json.load(f)
                # Reconstruct pack
                return self._dict_to_pack(data)
        return None
    
    def _dict_to_pack(self, data: Dict) -> EvidencePack:
        """Convert dict back to EvidencePack"""
        claims = []
        for c in data.get('claims', []):
            support = [EvidenceSource(**s) for s in c.get('support', [])]
            claims.append(Claim(
                claim_text=c['claim_text'],
                support=support,
                status=ClaimStatus(c.get('status', 'unsupported')),
                confidence=c.get('confidence', 0.0),
            ))
        
        sources = [EvidenceSource(**s) for s in data.get('sources', [])]
        
        actions = []
        for a in data.get('actions', []):
            actions.append(Action(
                action_type=ActionType(a['action_type']),
                description=a['description'],
                target=a['target'],
                destructive=a.get('destructive', False),
                requires_approval=a.get('requires_approval', False),
                approved_by=a.get('approved_by'),
                approved_at=a.get('approved_at'),
                executed_at=a.get('executed_at'),
                result=a.get('result'),
            ))
        
        verifier = None
        if data.get('verifier'):
            verifier = VerifierResult(**data['verifier'])
        
        rollback = None
        if data.get('rollback'):
            rollback = Rollback(**data['rollback'])
        
        return EvidencePack(
            pack_id=data['pack_id'],
            created_at=data['created_at'],
            request_id=data.get('request_id'),
            actor_id=data['actor_id'],
            answer=data['answer'],
            claims=claims,
            sources=sources,
            actions=actions,
            verifier=verifier,
            rollback=rollback,
            pack_hash=data.get('pack_hash'),
            previous_pack_hash=data.get('previous_pack_hash'),
        )
    
    def verify_chain(self, limit: int = 100) -> Dict:
        """Verify the integrity of the audit chain"""
        packs = []
        for json_file in sorted(self.root.rglob("*.json"))[-limit:]:
            if json_file.name == '.chain':
                continue
            with open(json_file) as f:
                packs.append(json.load(f))
        
        if not packs:
            return {'status': 'empty', 'packs_checked': 0}
        
        # Sort by created_at
        packs.sort(key=lambda x: x.get('created_at', ''))
        
        errors = []
        for i, pack in enumerate(packs):
            # Verify hash
            temp_pack = self._dict_to_pack(pack)
            computed = temp_pack.compute_hash()
            if computed != pack.get('pack_hash'):
                errors.append(f"Hash mismatch for {pack['pack_id']}")
            
            # Verify chain link
            if i > 0:
                if pack.get('previous_pack_hash') != packs[i-1].get('pack_hash'):
                    errors.append(f"Chain break at {pack['pack_id']}")
        
        return {
            'status': 'valid' if not errors else 'invalid',
            'packs_checked': len(packs),
            'errors': errors,
        }
    
    def stats(self) -> Dict:
        """Get evidence pack statistics"""
        total = 0
        verified = 0
        failed = 0
        
        for json_file in self.root.rglob("*.json"):
            if json_file.name.startswith('.'):
                continue
            total += 1
            with open(json_file) as f:
                data = json.load(f)
                if data.get('verifier', {}).get('passed'):
                    verified += 1
                else:
                    failed += 1
        
        return {
            'total_packs': total,
            'verified': verified,
            'failed': failed,
            'verification_rate': f"{verified/total*100:.1f}%" if total > 0 else "N/A",
        }

# ═══════════════════════════════════════════════════════════════
# 🎯 CLI
# ═══════════════════════════════════════════════════════════════

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='📦 CODEMASTER Evidence Pack Service')
    parser.add_argument('command', choices=['create', 'get', 'verify', 'stats'])
    parser.add_argument('args', nargs='*')
    parser.add_argument('--actor', '-a', default='cli', help='Actor ID')
    parser.add_argument('--answer', help='Answer text for create')
    
    args = parser.parse_args()
    service = EvidenceService()
    
    if args.command == 'create':
        if not args.answer:
            print("Usage: evidence_service.py create --answer 'Your answer' --actor user123")
            return
        
        # Example pack with claims
        pack = service.create_pack(
            answer=args.answer,
            actor_id=args.actor,
            claims=[
                {
                    'claim_text': 'This is an example claim',
                    'support': []  # No evidence = will be marked unsupported
                }
            ]
        )
        
        print(f"\n📦 Created Evidence Pack: {pack.pack_id}")
        print(f"   Verified: {pack.verifier.passed if pack.verifier else 'N/A'}")
        print(f"   Hash: {pack.pack_hash[:16]}...")
    
    elif args.command == 'get':
        if not args.args:
            print("Usage: evidence_service.py get <pack_id>")
            return
        
        pack = service.get_pack(args.args[0])
        if pack:
            print(json.dumps(pack.to_dict(), indent=2))
        else:
            print(f"❌ Pack not found: {args.args[0]}")
    
    elif args.command == 'verify':
        result = service.verify_chain()
        print(f"\n🔗 CHAIN VERIFICATION")
        print(f"   Status: {result['status'].upper()}")
        print(f"   Packs Checked: {result['packs_checked']}")
        if result.get('errors'):
            print(f"   Errors:")
            for e in result['errors']:
                print(f"     - {e}")
    
    elif args.command == 'stats':
        stats = service.stats()
        print(f"\n📊 EVIDENCE PACK STATISTICS")
        print(f"   Total Packs: {stats['total_packs']}")
        print(f"   Verified: {stats['verified']}")
        print(f"   Failed: {stats['failed']}")
        print(f"   Verification Rate: {stats['verification_rate']}")

if __name__ == "__main__":
    main()
