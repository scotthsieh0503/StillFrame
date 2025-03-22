import os
from src.apps.base_app import BaseApp
import src.apps.music.services as music_service

class MusicApp(BaseApp):
    def __init__(self, settings):
        super().__init__(settings)
        self.settings = settings
        self.image = None # List of all images in the folder
        self.current_track = {} # Current track being played

    def get_image(self):
        self.image = music_service.generate_image()
        return self.image
    
    def get_currently_playing_track(self):
        self.current_track = music_service.get_currently_playing_track()
        return self.current_track
            
        