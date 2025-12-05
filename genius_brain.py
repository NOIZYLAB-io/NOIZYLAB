"""
═══════════════════════════════════════════════════════════════════════════════
THE NOIZYGENIUS COLLECTIVE BRAIN
═══════════════════════════════════════════════════════════════════════════════

The unified intelligence of all 25 NoizyGeniuses working together.
COMPLETE OMNISCIENT KNOWLEDGE of every repair since the beginning of time.

THIS IS THE KEY TO ROB'S SUCCESS.
"""

from .genius_registry import (
    GENIUSES, 
    get_genius, 
    find_genius_for_issue, 
    get_genius_team_for_complex_issue
)

class GeniusBrain:
    """
    The collective intelligence of all 25 NoizyGeniuses.
    Routes problems to the right genius(es) and synthesizes solutions.
    """
    
    def __init__(self):
        self.geniuses = GENIUSES
        self.active_genius = None
        self.genius_team = []
        self.session_context = {}
        self.repair_history = []
    
    def analyze_issue(self, issue_description):
        """
        Analyze an issue and determine which genius(es) should handle it.
        Returns analysis with recommended geniuses and initial diagnosis.
        """
        # Find matching geniuses
        matches = find_genius_for_issue(issue_description)
        
        if not matches:
            # Default to software genius for unknown issues
            matches = [("GENIUS_SOFTWARE", self.geniuses["GENIUS_SOFTWARE"], 1)]
        
        # Set primary genius
        primary = matches[0]
        self.active_genius = primary[1]
        
        # Set team for complex issues
        if len(matches) > 1:
            self.genius_team = [m[1] for m in matches[:3]]
        else:
            self.genius_team = [primary[1]]
        
        return {
            "primary_genius": {
                "id": primary[0],
                "name": primary[1]["name"],
                "symbol": primary[1]["symbol"],
                "domain": primary[1]["domain"],
                "confidence": min(primary[2] / 10, 1.0)
            },
            "supporting_geniuses": [
                {
                    "id": m[0],
                    "name": m[1]["name"],
                    "symbol": m[1]["symbol"],
                    "relevance": min(m[2] / 10, 1.0)
                }
                for m in matches[1:4]
            ],
            "initial_diagnosis": self._generate_initial_diagnosis(issue_description, primary[1]),
            "recommended_questions": self._generate_diagnostic_questions(issue_description, primary[1])
        }
    
    def _generate_initial_diagnosis(self, issue, genius):
        """Generate initial diagnosis based on issue and genius expertise"""
        # Check against repair specialties
        issue_lower = issue.lower()
        possible_causes = []
        
        for specialty in genius["repair_specialties"]:
            specialty_lower = specialty.lower()
            # Simple keyword matching for now
            if any(word in issue_lower for word in specialty_lower.split()):
                possible_causes.append(specialty)
        
        if not possible_causes:
            possible_causes = genius["repair_specialties"][:3]
        
        return {
            "genius_handling": genius["name"],
            "domain": genius["domain"],
            "possible_causes": possible_causes[:5],
            "expertise_applied": [e for e in genius["expertise"][:5]]
        }
    
    def _generate_diagnostic_questions(self, issue, genius):
        """Generate smart diagnostic questions"""
        questions = []
        issue_lower = issue.lower()
        
        # Universal questions
        questions.append("When did this issue first start?")
        questions.append("Did anything change recently (updates, new software, hardware)?")
        
        # Domain-specific questions
        if "APPLE" in genius["id"]:
            questions.append("What macOS/iOS version are you running?")
            questions.append("Is this a Mac with Apple Silicon or Intel?")
        
        elif "WINDOWS" in genius["id"]:
            questions.append("What version of Windows are you running?")
            questions.append("Have you seen any error codes or blue screens?")
        
        elif "NETWORK" in genius["id"] or "wifi" in issue_lower:
            questions.append("Are other devices on the network working?")
            questions.append("What's your internet speed when you run a speed test?")
        
        elif "slow" in issue_lower:
            questions.append("Is it slow all the time or just sometimes?")
            questions.append("How much free storage space do you have?")
        
        elif "crash" in issue_lower or "freeze" in issue_lower:
            questions.append("Does it happen with specific apps or randomly?")
            questions.append("How long can you use it before it crashes?")
        
        elif "battery" in issue_lower:
            questions.append("How old is the device?")
            questions.append("What's the battery health percentage?")
        
        elif "screen" in issue_lower or "display" in issue_lower:
            questions.append("Is it a physical crack or a display issue?")
            questions.append("Does it happen all the time or intermittently?")
        
        return questions[:5]
    
    def get_repair_steps(self, issue_description, diagnosis=None):
        """
        Generate step-by-step repair instructions.
        Uses collective genius knowledge.
        """
        if not diagnosis:
            diagnosis = self.analyze_issue(issue_description)
        
        genius = self.active_genius
        steps = []
        
        # Always start with data protection
        steps.append({
            "step": 1,
            "action": "Backup Check",
            "description": "Verify client has recent backup before proceeding",
            "critical": True
        })
        
        # Diagnostic steps
        steps.append({
            "step": 2,
            "action": "Initial Diagnosis",
            "description": f"Run {genius['domain']} diagnostic procedures",
            "tools": genius.get("tools", [])
        })
        
        # Domain-specific repair steps
        step_num = 3
        for specialty in diagnosis["initial_diagnosis"]["possible_causes"][:3]:
            steps.append({
                "step": step_num,
                "action": f"Check: {specialty}",
                "description": f"Investigate {specialty} as potential cause",
                "genius": genius["name"]
            })
            step_num += 1
        
        # Resolution step
        steps.append({
            "step": step_num,
            "action": "Apply Fix",
            "description": "Implement solution based on diagnosis",
            "verify": True
        })
        
        # Verification step
        steps.append({
            "step": step_num + 1,
            "action": "Verify Resolution",
            "description": "Confirm issue is resolved, test thoroughly",
            "critical": True
        })
        
        # Prevention step
        steps.append({
            "step": step_num + 2,
            "action": "Prevention",
            "description": "Recommend steps to prevent recurrence",
            "upsell_opportunity": True
        })
        
        return {
            "issue": issue_description,
            "genius_team": [g["name"] for g in self.genius_team],
            "steps": steps,
            "estimated_time": self._estimate_repair_time(diagnosis),
            "difficulty": self._assess_difficulty(diagnosis)
        }
    
    def _estimate_repair_time(self, diagnosis):
        """Estimate repair time based on issue complexity"""
        # Simple heuristic for now
        cause_count = len(diagnosis["initial_diagnosis"]["possible_causes"])
        base_time = 30  # minutes
        return base_time + (cause_count * 15)
    
    def _assess_difficulty(self, diagnosis):
        """Assess repair difficulty"""
        genius = self.active_genius
        if "Master" in genius["name"]:
            # Check if issue matches core expertise
            if len(diagnosis["initial_diagnosis"]["possible_causes"]) <= 2:
                return "straightforward"
            elif len(diagnosis["initial_diagnosis"]["possible_causes"]) <= 4:
                return "moderate"
        return "complex"
    
    def consult_genius(self, genius_id, question):
        """
        Consult a specific genius with a question.
        Returns expert response based on genius knowledge.
        """
        genius = get_genius(genius_id)
        if not genius:
            return {"error": f"Genius {genius_id} not found"}
        
        return {
            "genius": genius["name"],
            "symbol": genius["symbol"],
            "domain": genius["domain"],
            "expertise_areas": genius["expertise"],
            "repair_capabilities": genius["repair_specialties"],
            "response": f"{genius['name']} is ready to help with {genius['domain']} issues."
        }
    
    def get_collective_status(self):
        """Get status of the collective genius brain"""
        return {
            "total_geniuses": len(self.geniuses),
            "active_genius": self.active_genius["name"] if self.active_genius else None,
            "team_size": len(self.genius_team),
            "domains_covered": list(set(g["domain"] for g in self.geniuses.values())),
            "ready": True,
            "motto": "EVERY REPAIR. EVERY OS. EVERY DEVICE. SINCE THE BEGINNING OF TIME."
        }


# Singleton instance
genius_brain = GeniusBrain()


def analyze(issue):
    """Quick analyze function"""
    return genius_brain.analyze_issue(issue)


def get_repair_plan(issue):
    """Quick repair plan function"""
    return genius_brain.get_repair_steps(issue)


def consult(genius_id, question):
    """Quick consult function"""
    return genius_brain.consult_genius(genius_id, question)

