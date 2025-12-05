import os
from spellchecker import SpellChecker

# Path to the BFD directory on the attached drive
BFD_PATH = "/Volumes/4TB Big Fish/BFD"

# Initialize spell checker
spell = SpellChecker()

# Collect all folder names in BFD (top-level and one level deep)
folder_names = set()
for root, dirs, files in os.walk(BFD_PATH):
    for d in dirs:
        folder_names.add(d)
    # Only check top two levels for now
    break

# Check spelling for each folder name
misspelled = {}
for name in folder_names:
    # Ignore names that are all uppercase or numbers (likely acronyms or versions)
    if name.isupper() or name.isdigit():
        continue
    # Split on spaces and check each word
    words = name.replace('-', ' ').replace('_', ' ').split()
    for word in words:
        if word.lower() not in spell:
            correction = spell.correction(word)
            if correction and correction != word:
                misspelled[name] = correction

# Print report
if misspelled:
    print("Possible misspellings in BFD folders:")
    for wrong, right in misspelled.items():
        print(f"  {wrong}  ->  {right}")
else:
    print("No obvious misspellings found in BFD folders.")
