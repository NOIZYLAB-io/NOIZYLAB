#!/usr/bin/env python3
"""
NOIZYGENIE Terminal Output with Palatino 14 Aesthetic
Consistent styling for all terminal readouts
"""

import os
from datetime import datetime

class PalatinoTerminal:
    """Terminal output styled to match Palatino 14 aesthetic"""
    
    def __init__(self):
        self.width = 70  # Consistent width for elegant presentation
        
    def header(self, text):
        """Print main header in Palatino style"""
        print("🎹 " + text.upper())
        print("=" * self.width)
        
    def subheader(self, text):
        """Print subheader"""
        print(f"\n📚 {text}")
        print("-" * (len(text) + 4))
        
    def info(self, label, value):
        """Print info line with consistent formatting"""
        print(f"   📊 {label}: {value}")
        
    def success(self, text):
        """Print success message"""
        print(f"✅ {text}")
        
    def warning(self, text):
        """Print warning message"""
        print(f"⚠️  {text}")
        
    def error(self, text):
        """Print error message"""
        print(f"❌ {text}")
        
    def complete(self, text):
        """Print completion message"""
        print(f"🎉 {text}")
        
    def library_status(self, name, status, instruments, samples):
        """Print library status in elegant format"""
        status_icons = {
            "COMPLETE": "✅",
            "PARTIAL": "⚠️",
            "FRAGMENT": "❌",
            "UNKNOWN": "❓"
        }
        
        icon = status_icons.get(status, "•")
        ratio = f"{samples/instruments:.1f}" if instruments > 0 else "N/A"
        
        print(f"   {icon} {name:<30} {status:<10} {instruments:>4} inst, {samples:>4} samples (ratio: {ratio})")
        
    def section_break(self):
        """Print elegant section break"""
        print("\n" + "·" * self.width + "\n")
        
    def timestamp(self):
        """Print timestamp in Palatino style"""
        print(f"\n📅 Generated: {datetime.now().strftime('%A, %B %d, %Y at %I:%M %p')}")

# Example usage
def demo_palatino_terminal():
    """Demonstrate Palatino terminal styling"""
    pt = PalatinoTerminal()
    
    pt.header("NOIZYGENIE Arsenal Status")
    pt.info("Total Libraries", "1,257")
    pt.info("Total Files", "25,480")
    
    pt.subheader("Library Status Breakdown")
    pt.library_status("Cellos", "COMPLETE", 113, 100)
    pt.library_status("Violas", "COMPLETE", 127, 100)
    pt.library_status("Basses", "PARTIAL", 103, 62)
    pt.library_status("Presets", "FRAGMENT", 470, 0)
    
    pt.section_break()
    pt.success("Scan completed successfully")
    pt.timestamp()

if __name__ == "__main__":
    demo_palatino_terminal()