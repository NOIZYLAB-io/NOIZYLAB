#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🚀 AUTOMATED 12TB VOICE HARVESTER 🚀                              ║
║                                                                           ║
║  GORUNFREE! BITW 1000X!                                                  ║
║  Harvest ALL quality voices from 12TB drive                              ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import sys
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent / "src"))

from voice_harvester import VoiceHarvester


def main():
    """Harvest voices from 12TB drive."""

    print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🚀 12TB VOICE HARVEST - INITIATED! 🚀                             ║
║                                                                           ║
║  GORUNFREE! Finding ALL quality voices...                                ║
║  BITW 1000X Standards Applied                                            ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
    """)

    # Initialize harvester
    harvester = VoiceHarvester()

    # Target directory
    target_volume = Path("/Volumes/12TB 1")

    if not target_volume.exists():
        print(f"❌ Volume not found: {target_volume}")
        print("\nAvailable volumes:")
        volumes_dir = Path("/Volumes")
        if volumes_dir.exists():
            for vol in volumes_dir.iterdir():
                if vol.is_dir():
                    print(f"   • {vol.name}")
        return 1

    print(f"✅ Found target volume: {target_volume}")
    print(f"📊 Starting comprehensive voice harvest...\n")

    # Start harvesting
    harvester.harvest_directory(target_volume, recursive=True)

    # Generate report
    print("\n" + "=" * 75)
    print("GENERATING FINAL REPORT...")
    print("=" * 75)

    report = harvester.generate_harvest_report()
    print(report)

    # Save report to file
    report_file = harvester.harvest_dir / "HARVEST_REPORT.txt"
    with open(report_file, 'w') as f:
        f.write(report)

    print(f"\n📄 Report saved to: {report_file}")

    print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        ✅ HARVEST COMPLETE! ✅                                           ║
║                                                                           ║
║  All voices cataloged and organized!                                     ║
║  Ready for FISHY STORYS & MUSI integration!                              ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
    """)

    return 0


if __name__ == "__main__":
    sys.exit(main())
