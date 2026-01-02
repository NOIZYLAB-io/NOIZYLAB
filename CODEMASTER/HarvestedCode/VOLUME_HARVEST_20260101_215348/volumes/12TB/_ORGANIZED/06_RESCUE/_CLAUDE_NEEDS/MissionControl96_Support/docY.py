import os
import shutil
import yaml

def load_rules(rules_path):
    with open(rules_path, 'r') as f:
        return yaml.safe_load(f)

class PerfectionistCleaner:
    def __init__(self, rules_path):
        self.rules = load_rules(rules_path)

    def clean_folder(self, folder_path):
        removed = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                ext = os.path.splitext(file)[1]
                if ext in self.rules['cleaning']['remove_extensions']:
                    full_path = os.path.join(root, file)
                    os.remove(full_path)
                    removed.append(full_path)
        return removed

    def validate_structure(self, folder_path):
        required = self.rules.get('required_structure', [])
        missing = []
        for rel_path in required:
            abs_path = os.path.join(folder_path, rel_path)
            if not os.path.exists(abs_path):
                missing.append(rel_path)
        return missing

    def get_file_count_and_size(self, path):
        total_files = 0
        total_size = 0
        for root, dirs, files in os.walk(path):
            for file in files:
                total_files += 1
                total_size += os.path.getsize(os.path.join(root, file))
        return total_files, total_size
