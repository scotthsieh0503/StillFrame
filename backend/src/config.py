import os 
import json

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
settings_file = os.path.join(BASE_DIR, 'settings.json')
with open(settings_file) as f:
    settings = json.load(f)  # 👈 Load JSON as a dictionary

class Config:
    """Base configuration."""
    DATA_DIR = settings.get('DATA_DIR', {})