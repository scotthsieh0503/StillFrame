from flask import request, jsonify
import requests
import base64
import src.apps.settings.services as settings_service
from PIL import Image


def generate_tokens(client_id, client_secret, code):
    url = "https://accounts.spotify.com/api/token"
    data = {
        'grant_type': 'authorization_code', 
        'code': code, 
        'redirect_uri': 'http://localhost:5000/api/music/spotify/callback'
    }
    headers = {
        'Authorization': 'Basic ' + base64.b64encode(f"{client_id}:{client_secret}".encode()).decode(),
    }
    response = requests.post(url, data=data, headers=headers)
    if response.status_code != 200:
        raise ValueError(response.text)
    
    settings = settings_service.get_settings()
    settings['SPOTIFY']['ACCESS_TOKEN'] = response.json()['access_token']
    settings['SPOTIFY']['REFRESH_TOKEN'] = response.json()['refresh_token']
    settings_service.update_settings(settings)
    
    return {'access_token': response.json()['access_token'], 'refresh_token': response.json()['refresh_token']}
1
def get_currently_playing_track(access_token):
    if not access_token:
        raise ValueError("Access token is required")
    
    url = "https://api.spotify.com/v1/me/player/currently-playing"
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise ValueError(response.text, access_token)
    return response.json()

def get_currently_playing_image(access_token):
    current_track = get_currently_playing_track(access_token)
    image_url = current_track.get('item').get('album').get('images')[0].get('url')
    image = Image.open(requests.get(image_url, stream=True).raw)

def save_spotify_settings(client_id, client_secret):
    settings = settings_service.get_settings()
    settings['SPOTIFY'] = {
        'CLIENT_ID': client_id,
        'CLIENT_SECRET': client_secret,
    }
    settings_service.update_settings(settings)
    return settings