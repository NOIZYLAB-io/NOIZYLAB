"""
═══════════════════════════════════════════════════════════════════════════════
                            TECH PASSPORT
═══════════════════════════════════════════════════════════════════════════════

Every big repair or change results in a clean, beautiful summary.

Easy for them to show a physical repair shop:
"We already ran all this; don't waste my money on step one."

Emotionally, it reframes the story:
"This wasn't chaos; this was a planned rescue."
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class HealthGrade(Enum):
    """Health grade for passport"""
    A_PLUS = "A+"    # 95-100
    A = "A"          # 90-94
    B_PLUS = "B+"    # 85-89
    B = "B"          # 80-84
    C_PLUS = "C+"    # 75-79
    C = "C"          # 70-74
    D = "D"          # 60-69
    F = "F"          # Below 60


@dataclass
class PassportEntry:
    """A single entry in the tech passport"""
    date: datetime
    title: str
    what_was_wrong: str
    what_we_did: str
    result: str
    genius_involved: str
    time_spent: str
    recommendations: List[str]
    red_flags: List[str]


@dataclass
class TechPassport:
    """
    The complete Tech Passport for a device.
    
    A beautiful, printable summary of everything about this device.
    """
    
    # Device info
    device_name: str
    device_type: str
    make: str
    model: str
    year: int
    serial: Optional[str]
    
    # Health
    current_health_score: int
    health_grade: HealthGrade
    last_checkup: datetime
    
    # History
    entries: List[PassportEntry]
    total_sessions: int
    total_repairs: int
    
    # Current status
    current_issues: List[str]
    recommendations: List[str]
    red_flags_to_watch: List[str]
    
    # NOIZYLAB relationship
    member_since: datetime
    membership_tier: str
    
    def get_health_grade(self, score: int) -> HealthGrade:
        """Convert score to grade"""
        if score >= 95: return HealthGrade.A_PLUS
        if score >= 90: return HealthGrade.A
        if score >= 85: return HealthGrade.B_PLUS
        if score >= 80: return HealthGrade.B
        if score >= 75: return HealthGrade.C_PLUS
        if score >= 70: return HealthGrade.C
        if score >= 60: return HealthGrade.D
        return HealthGrade.F
    
    def generate_summary(self) -> str:
        """Generate a text summary of the passport"""
        
        summary = f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                           NOIZYLAB TECH PASSPORT                             ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  DEVICE: {self.device_name:<60} ║
║  {self.make} {self.model} ({self.year})                                      
║  Serial: {self.serial or 'Not recorded':<52} ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  HEALTH STATUS                                                               ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  Current Health Score: {self.current_health_score}/100                       
║  Grade: {self.health_grade.value}                                            
║  Last Checkup: {self.last_checkup.strftime('%B %d, %Y')}                     
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  SERVICE HISTORY                                                             ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  Total Sessions: {self.total_sessions}                                       
║  Total Repairs: {self.total_repairs}                                         
║  Member Since: {self.member_since.strftime('%B %Y')}                         
║  Membership: {self.membership_tier}                                          
║                                                                              ║
"""
        
        # Add recent entries
        if self.entries:
            summary += "╠══════════════════════════════════════════════════════════════════════════════╣\n"
            summary += "║  RECENT SERVICE RECORDS                                                      ║\n"
            summary += "╠══════════════════════════════════════════════════════════════════════════════╣\n"
            
            for entry in self.entries[-5:]:  # Last 5 entries
                summary += f"""║                                                                              ║
║  📅 {entry.date.strftime('%Y-%m-%d')} - {entry.title:<50} ║
║  Problem: {entry.what_was_wrong[:60]:<60} ║
║  Action: {entry.what_we_did[:60]:<60} ║
║  Result: {entry.result:<60} ║
"""
        
        # Add recommendations
        if self.recommendations:
            summary += "╠══════════════════════════════════════════════════════════════════════════════╣\n"
            summary += "║  RECOMMENDATIONS                                                             ║\n"
            summary += "╠══════════════════════════════════════════════════════════════════════════════╣\n"
            for rec in self.recommendations:
                summary += f"║  • {rec:<70} ║\n"
        
        # Add red flags
        if self.red_flags_to_watch:
            summary += "╠══════════════════════════════════════════════════════════════════════════════╣\n"
            summary += "║  ⚠️  RED FLAGS TO WATCH                                                      ║\n"
            summary += "╠══════════════════════════════════════════════════════════════════════════════╣\n"
            for flag in self.red_flags_to_watch:
                summary += f"║  • {flag:<70} ║\n"
        
        summary += """╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  Generated by NOIZYLAB • Your Lifetime Tech Guardian                        ║
║  www.noizylab.ca                                                             ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
        
        return summary
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON/PDF generation"""
        return {
            "device": {
                "name": self.device_name,
                "type": self.device_type,
                "make": self.make,
                "model": self.model,
                "year": self.year,
                "serial": self.serial
            },
            "health": {
                "score": self.current_health_score,
                "grade": self.health_grade.value,
                "last_checkup": self.last_checkup.isoformat()
            },
            "history": {
                "total_sessions": self.total_sessions,
                "total_repairs": self.total_repairs,
                "entries": [
                    {
                        "date": e.date.isoformat(),
                        "title": e.title,
                        "problem": e.what_was_wrong,
                        "action": e.what_we_did,
                        "result": e.result,
                        "genius": e.genius_involved,
                        "time": e.time_spent
                    }
                    for e in self.entries
                ]
            },
            "status": {
                "current_issues": self.current_issues,
                "recommendations": self.recommendations,
                "red_flags": self.red_flags_to_watch
            },
            "membership": {
                "since": self.member_since.isoformat(),
                "tier": self.membership_tier
            },
            "generated": datetime.now().isoformat(),
            "generated_by": "NOIZYLAB"
        }
    
    def generate_for_repair_shop(self) -> str:
        """Generate a version optimized for showing to repair shops"""
        
        return f"""
NOIZYLAB DIAGNOSTIC SUMMARY
Device: {self.make} {self.model} ({self.year})
Serial: {self.serial or 'N/A'}
Health Score: {self.current_health_score}/100

ALREADY COMPLETED:
{chr(10).join(f'✓ {e.what_we_did}' for e in self.entries[-5:])}

CURRENT ISSUES:
{chr(10).join(f'• {issue}' for issue in self.current_issues) or 'None identified'}

RED FLAGS:
{chr(10).join(f'⚠ {flag}' for flag in self.red_flags_to_watch) or 'None'}

NOTES FOR TECHNICIAN:
{chr(10).join(f'• {rec}' for rec in self.recommendations) or 'Standard service'}

This device has been diagnosed by NOIZYLAB.
Please do not repeat diagnostic steps already completed.
Contact: help@noizylab.ca
        """.strip()


class PassportGenerator:
    """Generates Tech Passports"""
    
    def create_passport(
        self,
        device_name: str,
        device_type: str,
        make: str,
        model: str,
        year: int,
        serial: str = None,
        health_score: int = 75,
        entries: List[PassportEntry] = None,
        membership_tier: str = "Starter"
    ) -> TechPassport:
        """Create a new Tech Passport"""
        
        passport = TechPassport(
            device_name=device_name,
            device_type=device_type,
            make=make,
            model=model,
            year=year,
            serial=serial,
            current_health_score=health_score,
            health_grade=HealthGrade.B,  # Will be recalculated
            last_checkup=datetime.now(),
            entries=entries or [],
            total_sessions=len(entries) if entries else 1,
            total_repairs=sum(1 for e in (entries or []) if "repair" in e.title.lower()),
            current_issues=[],
            recommendations=[],
            red_flags_to_watch=[],
            member_since=datetime.now(),
            membership_tier=membership_tier
        )
        
        # Calculate grade
        passport.health_grade = passport.get_health_grade(health_score)
        
        return passport
    
    def add_entry(
        self,
        passport: TechPassport,
        title: str,
        problem: str,
        action: str,
        result: str,
        genius: str,
        time_spent: str,
        recommendations: List[str] = None,
        red_flags: List[str] = None
    ) -> PassportEntry:
        """Add an entry to a passport"""
        
        entry = PassportEntry(
            date=datetime.now(),
            title=title,
            what_was_wrong=problem,
            what_we_did=action,
            result=result,
            genius_involved=genius,
            time_spent=time_spent,
            recommendations=recommendations or [],
            red_flags=red_flags or []
        )
        
        passport.entries.append(entry)
        passport.total_sessions += 1
        passport.last_checkup = datetime.now()
        
        # Update recommendations and red flags
        if recommendations:
            passport.recommendations.extend(recommendations)
        if red_flags:
            passport.red_flags_to_watch.extend(red_flags)
        
        return entry


# Singleton
passport_gen = PassportGenerator()

