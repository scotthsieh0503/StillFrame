from flask import request, jsonify, send_file
from ..settings import settings_bp
import src.apps.image.services as image_service
import src.apps.settings.services as settings_service  # Import settings service

@settings_bp.route('/', methods=['GET'])
def get_settings():
    settings = settings_service.get_settings()
    return jsonify({'message': 'success', 'result': settings})

@settings_bp.route('/', methods=['POST', 'PUT', 'PATCH'])
def update_settings():
    settings = request.json
    settings_service.update_settings(settings)
    return jsonify({'message': 'success', 'result': settings})

@settings_bp.route('/<key>', methods=['GET'])
def get_setting(key):
    setting = settings_service.get_setting(key)
    return jsonify({'message': 'success', 'result': setting})

@settings_bp.route('/<key>', methods=['POST', 'PUT', 'PATCH'])
def update_setting(key):
    value = request.json
    setting = settings_service.update_setting(key, value)
    return jsonify({'message': 'success', 'result': setting})