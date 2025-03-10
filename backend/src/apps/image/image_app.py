import os
from PIL import Image
from src.apps.base_app import BaseApp
import random
import src.apps.image.services as image_services

class ImageApp(BaseApp):
    def __init__(self, settings):
        super().__init__(settings)
        self.settings = settings
        self.mode = self.settings.get('MODE', 'photo')

    def get_image(self):
        images = image_services.get_images(self.mode)
        if not images:
            return None
        
        random_photo = random.choice(images)
        image_path = image_services.get_image(self.mode, random_photo)
        
        # get a second image and merge them when the orientation is not the same
        image = Image.open(image_path)
        return image
        