import os
import shutil

# Official and custom BFD folder whitelist
WHITELIST = [
    'RP_Custom',
    'BFD 1',
    'BFD 1 - CVT',
    'BFD 2',
    'BFD 3',
    'BFD Deluxe',
    'BFD Eco',
    'BFD JNF',
    'BFD Jazz And Funk',
    'BFD Jazz Maple',
    'BFD Jazz Maple - Bonus Cymbals',
    'BFD Jazz Maple - Bonus Snare',
    'BFD Jazz Noir',
    'BFD London Sessions',
    'BFD London Sessions - Eco Version',
    'BFD Marching Drums',
    'BFD Metronomes',
    'BFD Orchestral',
    'BFD Percussion',
    'BFD Rock Tambourine',
    'BFD Virtually Erskine',
    'BFD XFL',
    'BFDLACTool',
    'BFD_UnInstallers',
    'DCAMFreeComp',
    # Add more official FXpansion names as needed
]

BFD_PATH = "/Volumes/4TB Big Fish/BFD"

# List all top-level folders in BFD
folders = [name for name in os.listdir(BFD_PATH) if os.path.isdir(os.path.join(BFD_PATH, name))]

# Find folders not in whitelist
not_in_whitelist = [f for f in folders if f not in WHITELIST]

if not_in_whitelist:
    print("Folders NOT in whitelist:")
    for f in not_in_whitelist:
        print(f"  {f}")
    # Optionally, you can rename or move them here
    # for f in not_in_whitelist:
    #     new_name = input(f"Enter correct name for '{f}' (or leave blank to skip): ")
    #     if new_name and new_name in WHITELIST:
    #         src = os.path.join(BFD_PATH, f)
    #         dst = os.path.join(BFD_PATH, new_name)
    #         shutil.move(src, dst)
    #         print(f"Renamed '{f}' to '{new_name}'")
else:
    print("All folders match the whitelist!")
