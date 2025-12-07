import os
import json
from pathlib import Path

VENDORS = [
    {
        "name": "Native Instruments",
        "account_email": "rp@fishmusicinc.com",
        "platforms": ["Kontakt", "Komplete", "NKS"],
        "products": [
            {
                "title": "Komplete 14 Ultimate",
                "library_paths": [
                    "/Users/Shared/Native Instruments",
                    "/Libraries/Kontakt/Komplete"
                ]
            },
            {
                "title": "Kontakt 7",
                "library_paths": [
                    "/Users/Shared/Native Instruments/Kontakt"
                ]
            }
        ]
    },
    {
        "name": "iZotope",
        "account_email": "rp@fishmusicinc.com",
        "platforms": ["Ozone", "RX", "Neutron", "Nectar"],
        "products": [
            {
                "title": "Ozone",
                "library_paths": [
                    "/Library/Application Support/iZotope/Ozone"
                ]
            },
            {
                "title": "RX",
                "library_paths": [
                    "/Library/Application Support/iZotope/RX"
                ]
            },
            {
                "title": "Neutron",
                "library_paths": [
                    "/Library/Application Support/iZotope/Neutron"
                ]
            },
            {
                "title": "Nectar",
                "library_paths": [
                    "/Library/Application Support/iZotope/Nectar"
                ]
            }
        ]
    }
]

def scan_vendor_libraries(vendors):
    index = []
    for vendor in vendors:
        v_entry = {
            "name": vendor["name"],
            "account_email": vendor["account_email"],
            "platforms": vendor["platforms"],
            "products": []
        }
        for product in vendor["products"]:
            p_entry = {
                "title": product["title"],
                "found_libraries": []
            }
            for lib_path in product["library_paths"]:
                p = Path(lib_path).expanduser()
                if p.exists():
                    # List subfolders/files as libraries
                    libs = [str(x) for x in p.glob("*") if x.is_dir() or x.is_file()]
                    p_entry["found_libraries"].extend(libs)
            v_entry["products"].append(p_entry)
        index.append(v_entry)
    return index

def main():
    index = scan_vendor_libraries(VENDORS)
    print(json.dumps(index, indent=2))

if __name__ == "__main__":
    main()