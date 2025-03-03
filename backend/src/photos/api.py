from flask import request, jsonify, send_file
from . import photo_bp
import src.photos.services as photo_services


@photo_bp.route('/upload', methods=['POST'])
def upload_photo():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    file_path = photo_services.save_photo(file)  # Calls service function
    base_url = request.host_url
    return jsonify({'message': 'success', 'result': base_url + 'api/photo/' + file.filename })
   

@photo_bp.route('/', methods=['GET'])
def list_photos():
    list = photo_services.get_photos()
    base_url = request.host_url
    list = [base_url + 'api/photo/' + photo for photo in list]
    return jsonify({'message': 'success', 'result': list })

@photo_bp.route('/<photo_name>', methods=['GET'])
def get_photo(photo_name):
    photo_path = photo_services.get_photo(photo_name)
    if not photo_path:
        return jsonify({'error': 'Photo not found'}), 404

    return send_file(photo_path, mimetype='image/jpeg')

@photo_bp.route('/<photo_name>', methods=['DELETE'])
def delete_photo(photo_name):
    photo_services.delete_photo(photo_name)
    return jsonify({'message': 'Photo deleted'}), 200
