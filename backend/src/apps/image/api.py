from flask import request, jsonify, send_file
from ..image import image_bp
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageOps
import io
import src.apps.image.services as image_service


@image_bp.route('/<folder_name>/upload', methods=['POST'])
def upload_image(folder_name):
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    file_path = image_service.save_image(folder_name, file)  # Pass folder_name
    base_url = request.host_url
    return jsonify({'message': 'success', 'result': base_url + 'api/image/' + folder_name + '/' + file.filename })
   

@image_bp.route('/<folder_name>', methods=['GET'])
def list_images(folder_name):
    list = image_service.get_images(folder_name)  # Pass folder_name
    base_url = request.host_url
    list = [base_url + 'api/image/' + folder_name + '/' + image for image in list]
    return jsonify({'message': 'success', 'result': list })

@image_bp.route('/<folder_name>/<image_name>', methods=['GET'])
def get_image(folder_name, image_name):
    image_path = image_service.get_image(folder_name, image_name)  # Pass folder_name
    if not image_path:
        return jsonify({'error': 'image not found'}), 404

    return send_file(image_path, mimetype='image/jpeg')

@image_bp.route('/<folder_name>/<image_name>', methods=['DELETE'])
def delete_image(folder_name, image_name):
    image_service.delete_image(folder_name, image_name)  # Pass folder_name
    return jsonify({'message': 'image deleted'}), 200

@image_bp.route('/<folder_name>/<image_name>/show', methods=['GET'])
def get_rotation_image(folder_name, image_name):
    image_path = image_service.get_image(folder_name, image_name)  # Pass folder_name
    if not image_path:
        return jsonify({'error': 'image not found'}), 404

    img = Image.open(image_path)
    img = img.rotate(270, expand=True)

    img_io = io.BytesIO()
    img.save(img_io, 'JPEG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')