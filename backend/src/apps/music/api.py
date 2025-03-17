from flask import request, jsonify, send_file
from ..music import music_bp
from src.apps.music.music_app import MusicApp
import src.apps.settings.services as settings_service
import src.apps.music.services as music_service
import random
from io import BytesIO

@music_bp.route('/settings', methods=['POST'])
def save_spotify_settings():
    data = request.json
    client_id = data.get('CLIENT_ID')
    client_secret = data.get('CLIENT_SECRET')
    music_app = MusicApp(settings_service.get_settings())
    settings = music_app.save_spotify_settings(client_id, client_secret)
    return jsonify(settings)

@music_bp.route('/currently-playing/image', methods=['GET'])
def get_currently_playing_image():
    music_app = MusicApp(settings_service.get_settings())
    image = music_app.get_image()
    img_io = BytesIO()
    image.save(img_io, 'JPEG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

@music_bp.route('/currently-playing', methods=['GET'])
def get_currently_playing():
    music_app = MusicApp(settings_service.get_settings())
    current_track = music_app.get_currently_playing_track()
    return jsonify(current_track)

@music_bp.route('/spotify/callback', methods=['GET'])
# used to get the access token and refresh token
def spotify_call_back():
    code = request.args.get('code')
    client_id = settings_service.get_settings().get('SPOTIFY').get('CLIENT_ID')
    client_secret = settings_service.get_settings().get('SPOTIFY').get('CLIENT_SECRET')
    tokens = music_service.generate_tokens(client_id=client_id, client_secret=client_secret, code=code)

    return jsonify(tokens)

