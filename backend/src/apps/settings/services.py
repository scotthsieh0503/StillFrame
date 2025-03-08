import json
import os

SETTINGS_FILE = 'settings.json'

def get_settings():
    setting_file = get_setting_file_path()
    if not os.path.exists(setting_file):
        setting_file = 'default_settings.json'
    with open(setting_file, 'r') as file:
        return json.load(file)

def update_settings(settings):
    setting_file = get_setting_file_path()
    os.makedirs(os.path.dirname(setting_file), exist_ok=True)
    with open(setting_file, 'w') as file:
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

def get_setting_file_path():
    """Get the absolute path of the image directory."""
    data_dir = 'data'
    setting_file_path = os.path.abspath(os.path.join(data_dir, SETTINGS_FILE))
    return setting_file_path
