import os
from flask import current_app

PHOTO_DIR = "photos/"

def save_photo(file):
    if not allowed_file(file.filename):
        raise ValueError("File type not allowed")
    
    upload_path = get_photo_path()
    
    if not os.path.exists(upload_path):
        os.makedirs(upload_path)
    
    file_path = os.path.join(upload_path, file.filename)
    return file.save(file_path)

def get_photo(photo_name):
    upload_path = get_photo_path()
    photo_path = os.path.join(upload_path, photo_name)
    if not os.path.exists(photo_path):
        return None
    
    return photo_path

def get_photos():
    upload_path = get_photo_path()
    if not os.path.exists(upload_path):
        return []
    
    return os.listdir(upload_path)

def delete_photo(photo_name):
    photo_path = get_photo(photo_name)
    if not photo_path:
        return False
    
    os.remove(photo_path)
    return True

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_photo_path():
    """Get the absolute path of the photo directory."""
    data_dir = current_app.config.get('DATA_DIR')
    return os.path.abspath(os.path.join(data_dir, PHOTO_DIR))