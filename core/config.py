import json
import os

def load_config(config_file: str = 'config.json') -> Dict[str, str]:
    with open(config_file, 'r') as f:
        return json.load(f)

def save_config(config: Dict[str, str], config_file: str = 'config.json'):
    with open(config_file, 'w') as f:
        json.dump(config, f, indent=4)

# Example usage:
# config = load_config()
# print(config)
