import yaml
from pathlib import Path

def load_config(path="config.yaml"):
    with open(Path(path), "r") as f:
        return yaml.safe_load(f)

CONFIG = load_config()
