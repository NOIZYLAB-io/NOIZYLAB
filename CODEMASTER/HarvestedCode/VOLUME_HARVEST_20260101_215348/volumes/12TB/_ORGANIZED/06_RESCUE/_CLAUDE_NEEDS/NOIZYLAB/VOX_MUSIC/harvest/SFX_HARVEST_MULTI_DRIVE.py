#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎬 MULTI-DRIVE SFX HARVEST - GORUNFREE! 🎬                        ║
║                                                                           ║
║  Harvest ALL SFX from Multiple Drives: 12TB + 4TBSG                     ║
║  BITW 1000X Quality Standards                                            ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import sys
from pathlib import Path

# Import the SFX harvest system
sys.path.append(str(Path(__file__).parent))
from SFX_HARVEST_SYSTEM import SFXHarvestSystem


class MultiDriveSFXHarvest(SFXHarvestSystem):
    """Extended SFX harvester for multiple drives."""

    def __init__(self):
        super().__init__()

        # Multiple source volumes
        self.source_volumes = [
            Path("/Volumes/12TB 1"),
            Path("/Volumes/4TBSG")
        ]

        print(f"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎬 MULTI-DRIVE SFX HARVEST INITIALIZED 🎬                         ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

Target Drives:
""")

        for vol in self.source_volumes:
            if vol.exists():
                import subprocess
                result = subprocess.run(['df', '-h', str(vol)], capture_output=True, text=True)
                lines = result.stdout.strip().split('\n')
                if len(lines) > 1:
                    print(f"   ✅ {vol.name}: {lines[1].split()[2]} used")
            else:
                print(f"   ⚠️  {vol.name}: Not found")

        print()

    def find_all_sfx(self) -> list:
        """Find SFX from all volumes."""
        all_sfx = []

        for volume in self.source_volumes:
            if not volume.exists():
                print(f"\n⚠️  Skipping {volume.name} - not mounted")
                continue

            print(f"\n{'='*75}")
            print(f"🔍 SCANNING: {volume.name}")
            print(f"{'='*75}\n")

            # Temporarily set source volume
            self.source_volume = volume

            # Find SFX on this volume
            volume_sfx = super().find_all_sfx()
            all_sfx.extend(volume_sfx)

            print(f"\n✅ Found {len(volume_sfx):,} SFX files on {volume.name}")

        print(f"\n{'='*75}")
        print(f"✅ TOTAL SFX ACROSS ALL DRIVES: {len(all_sfx):,}")
        print(f"{'='*75}\n")

        return all_sfx


def main():
    """Execute multi-drive SFX harvest."""

    print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎬 MULTI-DRIVE SFX HARVEST - EXECUTE! 🎬                          ║
║                                                                           ║
║  Scanning: 12TB + 4TBSG                                                  ║
║  GORUNFREE! BITW 1000X!                                                  ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
    """)

    system = MultiDriveSFXHarvest()
    system.execute_harvest()

    return 0


if __name__ == "__main__":
    sys.exit(main())
