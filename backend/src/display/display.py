from inky import InkInky_Impressions_7 as Inky
# from inky.auto import auto 

class Display:
    def __init__(self):
        self.display = Inky()
        self.display.set_border(self.display.BLACK)

        self.display_width = self.display.width
        self.display_height = self.display.height

    def send_image(self, image):
        if not image:
            raise ValueError("Image is required")
        

        image = self.crop_image(image, self.display_width, self.display_height)
        self.display.set_image(image)
        self.display.show()

    def crop_image(self, image, width, height):
        if not image:
            raise ValueError("Image is required")
        

        image_aspect_ratio = image.width / image.height
        display_aspect_ratio = self.display_width / self.display_height

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

        image = image.crop((left, top, right, bottom))
        return image