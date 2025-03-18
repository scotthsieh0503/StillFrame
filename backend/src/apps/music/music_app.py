import os
from PIL import Image
from src.apps.base_app import BaseApp
import src.apps.music.services as music_service

class MusicApp(BaseApp):
    def __init__(self, settings):
        super().__init__(settings)
        self.settings = settings
        self.image = None # List of all images in the folder
        self.current_track = {} # Current track being played

    def get_image(self):
        if not self.image:
            image = self.get_currently_playing_image()
            self.image = image
        return self.image
    
    def get_currently_playing_track(self):
        current_track = self.current_track or {}
        try:
            result = music_service.get_currently_playing_track()
            print(result)
            current_track['name'] = result['item']['name']
            current_track['artist'] = result['item']['artists'][0]['name']
            current_track['image'] = result['item']['album']['images'][0]['url']
        except Exception as e:
            raise e
            
        self.current_track = current_track
        return current_track
            
        