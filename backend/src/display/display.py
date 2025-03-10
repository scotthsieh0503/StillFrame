from inky.inky_ac073tc1a import Inky
# from inky.auto import auto -- my screen is not detectign properly
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageOps


class Display:
    def __init__(self, settings):
        self.display = Inky()
        self.settings = settings
        self.orientation = self.settings['ORIENTATION']
        self.saturation = self.settings['SATURATION']
        self.contrast = self.settings['CONTRAST']
        self.display.set_border(self.display.BLACK)

    def show_image(self, image):
        if not image:
            raise ValueError("Image is required")
        
        image = self.rotate_image(image)
        image = self.crop_image(image, self.display.width, self.display.height)
        image = self.adjust_image(image)
        self.display.set_image(image, saturation=self.saturation)
        self.display.show()

    def crop_image(self, image, width, height):
        if not image:
            raise ValueError("Image is required")
                
        image_aspect_ratio = image.width / image.height
        display_aspect_ratio = width / height

        if image_aspect_ratio > display_aspect_ratio:
            new_width = int(image.height * display_aspect_ratio)
            new_height = image.height
        else:
            new_width = image.width
            new_height = int(image.width / display_aspect_ratio)

        left = (image.width - new_width) / 2
        top = (image.height - new_height) / 2
        right = (image.width + new_width) / 2
        bottom = (image.height + new_height) / 2
        
        image_cropped = image.crop((left, top, right, bottom))
        image_resized = image_cropped.resize((width, height), Image.LANCZOS)
        return image_resized 
    
    def adjust_image(self, image):
        # Adjust the image based on the settings
        if not image:
            raise ValueError("Image is required")
        
        color_enhancer = ImageEnhance.Color(image)
        image = color_enhancer.enhance(self.saturation)
        contrast_enhancer = ImageEnhance.Contrast(image)
        image = contrast_enhancer.enhance(self.contrast)
        return image
    
    def update_settings(self, settings):
        self.settings = settings
        self.orientation = self.settings['ORIENTATION']
        self.saturation = self.settings['SATURATION']
        self.contrast = self.settings['CONTRAST']