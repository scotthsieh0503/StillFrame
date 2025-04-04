from .display import Display
import logging
import threading
import time
from ..apps.image.image_app import ImageApp
from ..apps.music.music_app import MusicApp
from ..apps.settings import services as setting_service

logger = logging.getLogger(__name__)

class DisplayController:
    def __init__(self, env=None):
        self.env = env
        self.setting_service = setting_service
        self.thread = None
        self.is_running = False
        self.current_settings = self.setting_service.get_settings()
        self.display = Display(self.current_settings['DISPLAY'])
        self.update_interval = self.current_settings['UPDATE_INTERVAL']
        self.current_mode = None
        self.current_app = None
        self.current_image = None

        self.poll_interval = 10

    def start(self):
        self.update()
        if not self.thread or not self.thread.is_alive():
            self.is_running = True
            self.thread = threading.Thread(target=self.run, daemon=True)
            self.thread.start()

    def update(self):
        if self.env == 'production':
            self.update_settings()
            self.update_current_app()
            image = self.current_app.get_image()
            if image and image != self.current_image:
                self.current_image = image
                self.display.show_image(image)
        
    def run(self):
        counter = 0
        while self.is_running:
            try:
                counter += self.poll_interval
                settings = self.setting_service.get_settings()
                settings_changed = self.__setting_changed(self.current_settings, settings)
                if (counter >= self.update_interval or settings_changed):
                    self.update()
                    counter = 0
            except Exception as e:
                logger.error(str(e))

            time.sleep(self.poll_interval)
    
    def update_current_app(self):
        app_mode = self.setting_service.get_setting('MODE')
        if(app_mode != self.current_mode):
            self.current_mode = app_mode
            self.current_app = self.__get_app_map().get(app_mode)
        return self.current_app
    
    def update_settings(self):
        self.current_settings = self.setting_service.get_settings()
        self.display.update_settings(self.setting_service.get_setting('DISPLAY'))
        self.update_interval = self.setting_service.get_setting('UPDATE_INTERVAL')

    
    def __get_app_map(self):
        app_map = {
            'photo': ImageApp(self.setting_service.get_settings()),
            'art': ImageApp(self.setting_service.get_settings()),
            'music': MusicApp(self.setting_service.get_settings())
        }
        return app_map


    def __setting_changed(self, current_settings, last_settings):
        for key in current_settings:
            if current_settings[key] != last_settings[key]:
                return True
        return False
        

    