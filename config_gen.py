import yaml
from pathlib import Path

def load_config(config_path="./config_base.yaml"):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    
    # Expand the path
    config['path'] = Path(config['path']).expanduser()
    
    return config


