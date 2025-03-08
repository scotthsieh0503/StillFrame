from flask import request, jsonify, send_file
from ..settings import settings_bp
import src.apps.image.services as image_service
import src.apps.settings.services as settings_service  # Import settings service

@settings_bp.route('/display', methods=['GET'])
def get_display_settings():
    settings = settings_service.get_display_settings()  # Get display settings
    return jsonify({'message': 'success', 'result': settings})

@settings_bp.route('/display', methods=['PUT', 'POST'])
def update_display_settings():
    settings = request.json
    settings_service.update_display_settings(settings)  # Update display settings
    return jsonify({'message': 'settings updated'}), 200
