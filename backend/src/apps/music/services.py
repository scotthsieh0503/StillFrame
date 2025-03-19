from flask import request, jsonify
import os
import requests
import base64
import src.apps.settings.services as settings_service
from PIL import Image

IMAGE_DIR = "image/"

def get_currently_playing_track():
    url = "https://api.spotify.com/v1/me/player/currently-playing"
    current_track = make_request(url)
    return current_track

def get_image():
    tmp_file_name = "album_art.png"
    display_setting = settings_service.get_setting('DISPLAY')
    if display_setting['ORIENTATION'] == 'landscape':
        width, height = 1920, 1080
    else:
        width, height = 1080, 1920
    if os.getenv('FLASK_ENV') == 'production':
        os.system(f'chromium --headless --disable-gpu --no-sandbox --disable-logging --screenshot={tmp_file_name} --virtual-time-budget=5000 --window-size={width},{height} http://localhost:3000/music/currentTrack')
    else:
        os.system(f'chromium --headless --disable-gpu --no-sandbox --disable-logging --screenshot={tmp_file_name} --virtual-time-budget=5000 --window-size={width},{height} http://localhost:3303/music/currentTrack')

    image = Image.open(tmp_file_name)
    return image







def save_spotify_settings(client_id, client_secret):
    settings = settings_service.get_settings()
    settings['SPOTIFY'] = {
        'CLIENT_ID': client_id,
        'CLIENT_SECRET': client_secret,
    }
    settings_service.update_settings(settings)
    return settings


def make_request(url, method='GET', data=None):
    settings = settings_service.get_settings()
    access_token = settings['SPOTIFY'].get('ACCESS_TOKEN')
    
    if not access_token:
        access_token = refresh_access_token()
    
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    
    if method == 'GET':
        response = requests.get(url, headers=headers)
    elif method == 'POST':
        response = requests.post(url, headers=headers, data=data)
    else:
        raise ValueError("Unsupported HTTP method")
    
    if response.status_code == 401:  # Unauthorized
        access_token = refresh_access_token()
        headers['Authorization'] = f'Bearer {access_token}'
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, headers=headers, data=data)
    
    return response.json()

def refresh_access_token():
    settings = settings_service.get_settings()
    refresh_token = settings['SPOTIFY'].get('REFRESH_TOKEN')
    if not refresh_token:
        raise ValueError("Refresh token is missing")
    
    client_id = settings['SPOTIFY']['CLIENT_ID']
    client_secret = settings['SPOTIFY']['CLIENT_SECRET']
    
    url = "https://accounts.spotify.com/api/token"
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token
    }
    headers = {
        'Authorization': 'Basic ' + base64.b64encode(f"{client_id}:{client_secret}".encode()).decode(),
    }
    response = requests.post(url, data=data, headers=headers)
    if response.status_code != 200:
        raise ValueError(response.text)
    
    access_token = response.json()['access_token']
    settings['SPOTIFY']['ACCESS_TOKEN'] = access_token
    settings_service.update_settings(settings)
    
    return access_token