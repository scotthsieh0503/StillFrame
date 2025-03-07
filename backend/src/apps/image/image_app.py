import os
from PIL import Image
from src.apps.base_app import BaseApp
import random
import src.apps.image.services as image_services

PHOTO_DIR = "image/"

class ImageApp(BaseApp):
    def __init__(self, settings):
        super().__init__(settings)

    def get_image(self):
        images = image_services.get_images('photo')
        if not images:
            return None
        
        random_photo = random.choice('photo')
        image_path = image_services.get_image('photo', random_photo)
        return Image.open(image_path)