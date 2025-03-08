import json
import os

SETTINGS_FILE = '/data/settings.json'

def get_settings():
    if not os.path.exists(SETTINGS_FILE):
        return {}
    with open(SETTINGS_FILE, 'r') as file:
        return json.load(file)

def update_settings(settings):
    with open(SETTINGS_FILE, 'w') as file:
        json.dump(settings, file, indent=4)

