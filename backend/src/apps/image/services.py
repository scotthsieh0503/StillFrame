import os

IMAGE_DIR = "image/"

def save_image(folder_name, file):
    if not allowed_file(file.filename):
        raise ValueError("File type not allowed")
    
    upload_path = get_image_path(folder_name)
    
    if not os.path.exists(upload_path):
        os.makedirs(upload_path)
    
    file_path = os.path.join(upload_path, file.filename)
    return file.save(file_path)

def get_image(folder_name, image_name):
    upload_path = get_image_path(folder_name)
    image_path = os.path.join(upload_path, image_name)
    if not os.path.exists(image_path):
        return None
    
    return image_path

def get_images(folder_name):
    upload_path = get_image_path(folder_name)
    if not os.path.exists(upload_path):
        return []
    
    return [f for f in os.listdir(upload_path) if allowed_file(f)]

def delete_image(folder_name, image_name):
    image_path = get_image(folder_name, image_name)
    if not image_path:
        return False
    
    os.remove(image_path)
    return True

def get_image_path(folder_name):
    """Get the absolute path of the image directory."""
    data_dir = 'data'
    return os.path.abspath(os.path.join(data_dir, IMAGE_DIR, folder_name))

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS