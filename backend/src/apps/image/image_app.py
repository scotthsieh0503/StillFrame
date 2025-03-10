import os
from PIL import Image
from src.apps.base_app import BaseApp
import random
import src.apps.image.services as image_services

class ImageApp(BaseApp):
    def __init__(self, settings):
        super().__init__(settings)
        self.settings = settings
        self.mode = self.__get_mode_from_settings()

    def get_image(self):
        images = image_services.get_images(self.mode)
        if not images:
            return None
        
        random_photo = random.choice(images)
        image_path = image_services.get_image(self.mode, random_photo)
        return Image.open(image_path)
    
    def __get_mode_from_settings(self):
        mode = self.settings.get('MODE', 'photo')
        return mode
    
    def get_combined_portrait_image(self):
        images = image_services.get_images(self.mode)
        if not images:
            return None
        
        portrait_images = [img for img in images if self.__is_portrait(img)]
        if len(portrait_images) < 2:
            return None
        
        first_image_path = image_services.get_image(self.mode, random.choice(portrait_images))
        second_image_path = image_services.get_image(self.mode, random.choice(portrait_images))
        
        first_image = Image.open(first_image_path)
        second_image = Image.open(second_image_path)
        
        combined_image = self.__combine_images(first_image, second_image)
        return combined_image

    def __is_portrait(self, image_name):
        image_path = image_services.get_image(self.mode, image_name)
        with Image.open(image_path) as img:
            width, height = img.size
            return height > width

    def __combine_images(self, img1, img2):
        total_width = img1.width + img2.width
        max_height = max(img1.height, img2.height)
        
        combined_image = Image.new('RGB', (total_width, max_height))
        combined_image.paste(img1, (0, 0))
        combined_image.paste(img2, (img1.width, 0))
        
        return combined_image