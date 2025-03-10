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
        
        image = Image.open(image_path)
        if self.settings['display']['orientation'] == 'landscape' and image.height > image.width:
            image = self.getLandScapeImage()
          #  image = self.mergeImages(image, image2, 'landscape')
        elif self.settings['display']['orientation'] == 'portrait' and image.width > image.height:
            image = self.getPortraitImage()
         #   image = self.mergeImages(image, image2, 'portrait')
        return image
        
    def getLandScapeImage(self):
        image = self.get_image()
        while image.height > image.width:
            image = self.get_image()
        return image

    def getPortraitImage(self):
        image = self.get_image()
        while image.width > image.height:
            image = self.get_image()
        return image  
    
    def mergeImages(self, image1, image2, orientation):
        if orientation == 'portrait':
            total_height = image1.height + image2.height
            max_width = max(image1.width, image2.width)
            merged_image = Image.new('RGB', (max_width, total_height))
            merged_image.paste(image1, (0, 0))
            merged_image.paste(image2, (0, image1.height))
        elif orientation == 'landscape':
            total_width = image1.width + image2.width
            max_height = max(image1.height, image2.height)
            merged_image = Image.new('RGB', (total_width, max_height))
            merged_image.paste(image1, (0, 0))
            merged_image.paste(image2, (image1.width, 0))
        else:
            merged_image = image1
        return merged_image
        
    def __get_mode_from_settings(self):
        mode = self.settings.get('MODE', 'photo')
        return mode