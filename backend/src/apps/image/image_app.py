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
        self.images = None

    def get_image(self):
        if not self.images:
            self.images = image_services.get_images(self.mode)

        random_photo = random.choice(self.image_history)
        self.images.remove(random_photo)
        image_path = image_services.get_image(self.mode, random_photo)
        return Image.open(image_path)
