from flask import request, jsonify
from . import photo_bp
from .services import save_photo

@photo_bp.route('/upload', methods=['POST'])
def upload_photo():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    file_path = save_photo(file)  # Calls service function
    return jsonify({'message': 'Photo uploaded'}), 201