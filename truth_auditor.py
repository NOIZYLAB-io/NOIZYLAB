# ROB OS - LAYER 1: TRUTH AUDITOR
# ================================
# Ensures every statement is honest, clear, and properly qualified
# "State what's known vs. guessed. Label confidence."

from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from enum import Enum

class ConfidenceLevel(Enum):
    HIGH = "high"       # Clear evidence, tested, verified
    MEDIUM = "medium"   # Good assessment, some uncertainty
    LOW = "low"         # Guess, needs verification
    UNKNOWN = "unknown" # No idea, must investigate

@dataclass
class TruthAuditResult:
    is_truthful: bool
    confidence: ConfidenceLevel
    qualifications: List[str]
    warnings: List[str]
    rewritten_statement: Optional[str]

class TruthAuditor:
    """
    The Truth Auditor ensures all statements are honest and properly qualified.
    No bluffing. No padding confidence. No hiding uncertainty.
    """
    
    def __init__(self):
        # Phrases that indicate overconfidence
        self.overconfidence_markers = [
            "definitely", "absolutely", "100%", "guaranteed",
            "always", "never", "impossible", "certain",
            "I promise", "trust me", "no doubt"
        ]
        
        # Phrases that properly qualify uncertainty
        self.good_qualifiers = [
            "likely", "probably", "based on what I see",
            "my best assessment", "I believe", "it appears",
            "the evidence suggests", "typically", "in most cases"
        ]
        
        # Phrases that hide uncertainty badly
        self.bad_hedges = [
            "should be fine", "probably won't be a problem",
            "don't worry about it", "it's nothing"
        ]
        
        # Confidence templates
        self.confidence_templates = {
            ConfidenceLevel.HIGH: "I'm confident about this because {reason}.",
            ConfidenceLevel.MEDIUM: "This is my best assessment, but {caveat}.",
            ConfidenceLevel.LOW: "I'm not certain here. {what_we_know}. We should verify by {verification}.",
            ConfidenceLevel.UNKNOWN: "I honestly don't know. Let me find out by {investigation}."
        }
    
    def audit_statement(self, statement: str, evidence: Dict[str, Any]) -> TruthAuditResult:
        """
        Audit a statement for truthfulness and proper qualification.
        """
        warnings = []
        qualifications = []
        
        statement_lower = statement.lower()
        
        # Check for overconfidence markers
        for marker in self.overconfidence_markers:
            if marker in statement_lower:
                warnings.append(f"Overconfidence marker detected: '{marker}'")
        
        # Check for bad hedges
        for hedge in self.bad_hedges:
            if hedge in statement_lower:
                warnings.append(f"Vague hedge detected: '{hedge}' - be more specific")
        
        # Determine actual confidence based on evidence
        confidence = self._assess_confidence(evidence)
        
        # Check if confidence is properly stated
        has_qualifier = any(q in statement_lower for q in self.good_qualifiers)
        
        if confidence in [ConfidenceLevel.LOW, ConfidenceLevel.UNKNOWN] and not has_qualifier:
            warnings.append("Low confidence statement without proper qualification")
            qualifications.append(self._suggest_qualification(confidence, evidence))
        
        # Generate rewritten statement if needed
        rewritten = None
        if warnings:
            rewritten = self._rewrite_with_honesty(statement, confidence, evidence)
        
        return TruthAuditResult(
            is_truthful=len(warnings) == 0,
            confidence=confidence,
            qualifications=qualifications,
            warnings=warnings,
            rewritten_statement=rewritten
        )
    
    def _assess_confidence(self, evidence: Dict[str, Any]) -> ConfidenceLevel:
        """
        Assess confidence level based on available evidence.
        """
        if not evidence:
            return ConfidenceLevel.UNKNOWN
        
        # Check evidence quality
        has_diagnostic_data = evidence.get("diagnostic_data", False)
        has_verified_tests = evidence.get("verified_tests", False)
        has_user_report_only = evidence.get("user_report_only", False)
        has_similar_cases = evidence.get("similar_cases", 0) > 5
        
        if has_verified_tests and has_diagnostic_data:
            return ConfidenceLevel.HIGH
        elif has_diagnostic_data or has_similar_cases:
            return ConfidenceLevel.MEDIUM
        elif has_user_report_only:
            return ConfidenceLevel.LOW
        else:
            return ConfidenceLevel.UNKNOWN
    
    def _suggest_qualification(self, confidence: ConfidenceLevel, 
                               evidence: Dict[str, Any]) -> str:
        """
        Suggest how to properly qualify a statement.
        """
        if confidence == ConfidenceLevel.LOW:
            return "Add: 'Based on your description, this could be X, but we should verify by running Y test.'"
        elif confidence == ConfidenceLevel.UNKNOWN:
            return "Add: 'I don't have enough information yet. Can you tell me more about X?'"
        elif confidence == ConfidenceLevel.MEDIUM:
            return "Add: 'This is likely X based on the symptoms, though there's a chance it could be Y.'"
        return ""
    
    def _rewrite_with_honesty(self, statement: str, confidence: ConfidenceLevel,
                              evidence: Dict[str, Any]) -> str:
        """
        Rewrite a statement to be properly honest and qualified.
        """
        # Remove overconfidence markers
        rewritten = statement
        for marker in self.overconfidence_markers:
            rewritten = rewritten.replace(marker, "likely")
            rewritten = rewritten.replace(marker.capitalize(), "Likely")
        
        # Add confidence qualifier
        qualifier = ""
        if confidence == ConfidenceLevel.HIGH:
            qualifier = "Based on the diagnostic data, "
        elif confidence == ConfidenceLevel.MEDIUM:
            qualifier = "From what I can see, "
        elif confidence == ConfidenceLevel.LOW:
            qualifier = "This is my best guess, but "
        elif confidence == ConfidenceLevel.UNKNOWN:
            qualifier = "I'm not certain, but "
        
        return qualifier + rewritten
    
    def format_honest_diagnosis(self, diagnosis: str, confidence: ConfidenceLevel,
                                evidence: Dict[str, Any], 
                                uncertainties: List[str]) -> str:
        """
        Format a diagnosis with proper honesty and transparency.
        """
        output = []
        
        # State the diagnosis
        output.append(f"**What I think is happening:** {diagnosis}")
        
        # State confidence
        confidence_text = {
            ConfidenceLevel.HIGH: "I'm fairly confident about this.",
            ConfidenceLevel.MEDIUM: "This is my best assessment, with some uncertainty.",
            ConfidenceLevel.LOW: "This is a guess that needs verification.",
            ConfidenceLevel.UNKNOWN: "I honestly don't know yet."
        }
        output.append(f"\n**How sure I am:** {confidence_text[confidence]}")
        
        # State what we know vs don't know
        if evidence.get("known_facts"):
            output.append(f"\n**What we know for sure:**")
            for fact in evidence["known_facts"]:
                output.append(f"  - {fact}")
        
        if uncertainties:
            output.append(f"\n**What we're not sure about:**")
            for uncertainty in uncertainties:
                output.append(f"  - {uncertainty}")
        
        # State next steps to verify
        if confidence != ConfidenceLevel.HIGH:
            output.append(f"\n**To be more certain, we should:**")
            output.append(f"  - Run additional diagnostics")
            output.append(f"  - Check specific logs or tests")
        
        return "\n".join(output)


# Singleton instance
_truth_auditor = None

def get_truth_auditor() -> TruthAuditor:
    global _truth_auditor
    if _truth_auditor is None:
        _truth_auditor = TruthAuditor()
    return _truth_auditor

