import json
import os

SETTINGS_FILE = '/data/settings.json'

def get_settings():
    setting_file = SETTINGS_FILE
    if not os.path.exists(setting_file):
        setting_file = 'default_settings.json'
    with open(setting_file, 'r') as file:
        return json.load(file)

def update_settings(settings):
    os.makedirs(os.path.dirname(SETTINGS_FILE), exist_ok=True)
    with open(SETTINGS_FILE, 'w') as file:
        json.dump(settings, file, indent=4)
    return get_settings()

def get_setting(key):
    settings = get_settings()
    return settings.get(key)

def update_setting(key, value):
    settings = get_settings()
    settings[key] = value
    update_settings(settings)
    return get_settings()
