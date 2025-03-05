import os
from PIL import Image
from src.apps.base_app import BaseApp
import random
import src.apps.photos.services as photo_services

PHOTO_DIR = "photos/"

class PhotoApp(BaseApp):
    def __init__(self, settings):
        super().__init__(settings)

    def get_image(self):
        photos = photo_services.get_photos()
        if not photos:
            return None
        
        random_photo = random.choice(photos)
        image_path = photo_services.get_photo(random_photo)
        return Image.open(image_path)