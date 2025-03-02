import os

UPLOAD_FOLDER = "uploads/"

def save_photo(file):
    """Save uploaded photo to disk."""
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    return True