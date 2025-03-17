import os
from PIL import Image
from src.apps.base_app import BaseApp
import src.apps.music.services as music_service

class MusicApp(BaseApp):
    def __init__(self, settings):
        super().__init__(settings)
        self.settings = settings
        self.image = None # List of all images in the folder
        self.current_track = None # Current track being played
        self.access_token = self.get_access_token()

    def get_image(self):
        if not self.image:
            image = self.get_currently_playing_image()
            self.image = image
        return self.image
    
    def save_spotify_settings(self, client_id, client_secret):
        return music_service.save_spotify_settings(client_id, client_secret)
    
    def get_access_token(self):
        spotify_settings = self.settings.get('SPOTIFY')
        if not spotify_settings:
           raise ValueError('Spotify settings not found please se it up again in the frontend')
        self.settings.get('SPOTIFY').get('ACCESS_TOKEN')
        return self.settings.get('SPOTIFY').get('ACCESS_TOKEN')
    
    def get_currently_playing_image(self):
        image = music_service.get_currently_playing_image(self.access_token)
        return image
    
    def get_currently_playing_track(self):
        current_track = self.current_track
        try:
            current_track = music_service.get_currently_playing_track(self.access_token)
        except Exception as e:
            if 'token expired' in str(e).lower():
               # self.access_token = self.authenticate()
                current_track = music_service.get_currently_playing_track(self.access_token)
            else:
                raise e
            
        self.current_track = current_track
        return current_track
            
        