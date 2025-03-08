import json
import os

SETTINGS_FILE = 'settings.json'

def get_settings():
    if not os.path.exists(SETTINGS_FILE):
        SETTINGS_FILE = 'default_settings.json'
    with open(SETTINGS_FILE, 'r') as file:
        return json.load(file)

def update_settings(settings):
    with open(SETTINGS_FILE, 'w') as file:
        json.dump(settings, file, indent=4)
    return get_settings

def get_setting(key):
    settings = get_settings()
    return settings.get(key)

def update_setting(key, value):
    settings = get_settings()
    settings[key] = value
    update_settings(settings)
    return get_setting(key)
