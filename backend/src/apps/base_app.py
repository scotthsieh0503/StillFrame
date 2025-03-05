
import os


class BaseApp:
    def __init__(self, settings):
        self.settings = settings

    def get_image(self):
        raise NotImplementedError("get_images is a required function")

    def get_settings(self):
        return self.settings
