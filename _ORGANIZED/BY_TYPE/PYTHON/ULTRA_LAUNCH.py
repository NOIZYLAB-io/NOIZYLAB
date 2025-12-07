#!/usr/bin/env python3
#!/usr/bin/env python3
"""
ULTRA HOT ROD LAUNCHER - M2 ULTRA MAC STUDIO
192GB RAM - MAXIMUM POWER
"""
import os
import sys
from pathlib import Path

# Maximum performance settings
os.environ['PYTHONOPTIMIZE'] = '2'
os.environ['PYTHONUNBUFFERED'] = '1'
os.environ['OMP_NUM_THREADS'] = '24'  # All CPU cores
os.environ['MKL_NUM_THREADS'] = '24'
os.environ['NUMEXPR_NUM_THREADS'] = '24'
os.environ['OPENBLAS_NUM_THREADS'] = '24'

# Memory settings
os.environ['PYTHONHASHSEED'] = '0'

sys.path.insert(0, str(Path(__file__).parent))

if __name__ == "__main__":
    try:
        from ULTIMATE_1000X_SYSTEM import Ultimate1000XSystem
        system = Ultimate1000XSystem()
        system.main_menu()
    except Exception as e:
        print(f"Error: {e}")