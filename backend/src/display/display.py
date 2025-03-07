from inky.inky_ac073tc1a import Inky
# from inky.auto import auto -- my screen is not detectign properly
from PIL import Image, ImageDraw, ImageFont


class Display:
    def __init__(self):
        self.display = Inky()
        self.display.set_border(self.display.BLACK)

    def show_image(self, image):
        if not image:
            image = Image.new("P", (self.display.width, self.display.height))
            fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
            draw = ImageDraw.Draw(image)
            draw.text((10, 10), "Hello =)", font=fnt ,fill=(255, 255, 255, 255))
    
        image = self.crop_image(image, self.display.width, self.display.height)
        self.display.set_image(image)
        self.display.show()

    def crop_image(self, image, width, height):
        if not image:
            raise ValueError("Image is required")
        

        image_aspect_ratio = image.width / image.height
        display_aspect_ratio = self.display.width / self.display.height

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
        image_resized = image_cropped.resize((self.display.width, self.display.height), Image.LANCZOS)
        return image_resized 