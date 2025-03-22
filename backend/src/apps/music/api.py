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

@music_bp.route('/currently-playing', methods=['GET'])
def get_currently_playing():
    music_app = MusicApp(settings_service.get_settings())
    current_track = music_app.get_currently_playing_track()
    return jsonify(current_track)

@music_bp.route('/currently-playing/image', methods=['GET'])
def get_currently_playing_image():

    image = music_service.get_image()
    image_data = BytesIO()
    image.save(image_data, format='PNG')
    image_data.seek(0)

    if not image_data:
        return jsonify({"error": "Image not found"}), 404

    return send_file(image_data, mimetype='image/png')

@music_bp.route('/currently-playing/image/PIL', methods=['GET'])
def get_currently_playing_image_pil():

    music_app = MusicApp(settings_service.get_settings())
    image = music_app.get_image()
    image_data = BytesIO()
    image.save(image_data, format='JPEG')
    image_data.seek(0)

    return send_file(image_data, mimetype='image/JPEG')
