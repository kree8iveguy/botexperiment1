import yaml
from dotenv import load_dotenv
import os

load_dotenv()

def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
