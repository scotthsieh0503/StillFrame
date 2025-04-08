from flask import request, jsonify
import os
from io import BytesIO
import requests
import base64
import src.apps.settings.services as settings_service
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from playwright.sync_api import Page, sync_playwright
IMAGE_DIR = "image/"

def get_currently_playing_track():
    url = "https://api.spotify.com/v1/me/player/currently-playing"
    response = make_request(url)
    current_track = {}
    try:
        current_track['name'] = response['item']['name']
        current_track['artist'] = ", ".join(artist['name'] for artist in response['item']['artists'])
        current_track['image'] = response['item']['album']['images'][0]['url']
    except Exception as e:
        raise e

    return current_track

# This generate images using a headless browser with html and css but it is not working on rasperry pi due to memory issue
def get_image():
    tmp_file_name = "album_art.png"
    display_setting = settings_service.get_setting('DISPLAY')
    if display_setting['ORIENTATION'] == 'landscape':
        width, height = 800, 480
    else:
        width, height = 480, 800

    url = "http://localhost:3000/music/currentTrack" if os.getenv('FLASK_ENV') == 'production' else "http://frontend:3000/music/currentTrack"

    with sync_playwright() as playwright:
       # browser = playwright.firefox.launch(headless=True, args=['--no-sandbox', '--disable-dev-shm-usage', '--disable-gpu', '--no-remote', '--safe-mode'])
        browser = playwright.chromium.launch(
            headless=True,
            args=[
            "--disable-gpu",
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--disable-software-rasterizer",
            "--single-process",
            "--disable-background-networking",
            "--disable-extensions",
            "--disable-sync",
            ]
        )
        page = browser.new_page()
        page.set_viewport_size({"width": width, "height": height})
        page.goto(url, timeout=120000)  # Set timeout to 2 minutes (120000 ms)
        page.wait_for_timeout(2000)
        page.screenshot(path=tmp_file_name)
        browser.close()

    image = Image.open(tmp_file_name)
    return image

# generate image using PILLOW byt drawing the image
def generate_image():
    tmp_file_name = "album_art.png"
    display_setting = settings_service.get_setting('DISPLAY')
    music_setting = settings_service.get_setting('SPOTIFY')
    album_art_size = (240, 240)
    orientation = display_setting['ORIENTATION']
    opacity = round(float(music_setting.get('OPACITY', 0.6)) * 255)  # 255 is 100% opacity
    blur = int(music_setting.get('BLUR', 10))

    mode = music_setting.get('MODE', 'default')

    try:
        current_track = get_currently_playing_track()
        response = requests.get(current_track['image'])
        album_art = Image.open(BytesIO(response.content))
        background_color = (255, 255, 255)
    except Exception as e:
        current_track = {
            'name': 'No song playing',
            'artist': '',
        }
        background_color = (255, 255, 255)
        album_art = Image.open('src/apps/music/assets/spotify.png')

    # Set height and width based on display setting
    if orientation == 'portrait':
        width, height = 480, 800
        album_art_position = (120, 80)
        song_name_position = (album_art_position[0], album_art_position[1] + album_art_size[1] + height/4 )
        artist_name_position = (song_name_position[0], song_name_position[1] + 45)
        text_length = 20
    else:  
        width, height = 800, 480
        album_art_position = (80, 120)
        song_name_position = ((album_art_position[0] + album_art_size[0]) + 20, (album_art_position[1] + album_art_size[1])/2 )
        artist_name_position = (song_name_position[0], song_name_position[1] + 45)
        text_length = 28

    if mode == 'fullscreen':
        song_name_font_size = 30
        artist_font_size = 30
        song_name_position = (10, (height - 60))
        artist_name_position_x = max(width / 2, width - artist_font_size * len(current_track['artist']) * 0.6 - 10)  # Adjusting for font size to pixel ratio
        artist_name_position = (artist_name_position_x, (height - 60))
    elif mode == 'default':
        song_name_font_size = 30
        artist_font_size = 20


    # truncate song name and artist name if they are too long
    if len(current_track['name']) > text_length:
        current_track['name'] = current_track['name'][:text_length] + "..."
    if len(current_track['artist']) > text_length:
        current_track['artist'] = current_track['artist'][:text_length] + "..."
    
    # Create a new image with white background
    new_img = Image.new('RGB', (width, height), background_color)

    # Create a blurred background using the album art
    blurred_background = album_art.resize((800, 800))
    blurred_background = blurred_background.filter(ImageFilter.GaussianBlur(blur))
    alpha = Image.new('L', blurred_background.size, opacity)  # 153 is 60% opacity
    blurred_background.putalpha(alpha)
    
    new_img.paste(blurred_background, (0, 0), blurred_background)

    # Scale album art to fit within the new image
    album_art.thumbnail(album_art_size)

    # album art position
    if mode == 'default':
        new_img.paste(album_art, album_art_position)
    if mode == 'fullscreen':
        overlay = Image.new('RGBA', (width, 60), (255, 255, 255, 75))
        new_img.paste(overlay, (0, height - 60), overlay)
  

    
    # Add text to the image
    draw = ImageDraw.Draw(new_img)


    
    song_name = f"{current_track['name']}"
    song_name_font = ImageFont.truetype("NotoSansCJK-Regular.ttc", song_name_font_size)  
    artist = f"{current_track['artist']}"
    artist_font = ImageFont.truetype("NotoSansCJK-Regular.ttc", artist_font_size)  
    draw.text(song_name_position, song_name, fill=(0, 0, 0), font=song_name_font)
    draw.text(artist_name_position, artist, fill=(0, 0, 0), font=artist_font)

    # Save the image
    new_img.save(tmp_file_name)

    return new_img

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