from .display import Display
import logging
import threading
import time
from ..apps.image.image_app import ImageApp
from ..apps.settings import services as setting_service

logger = logging.getLogger(__name__)

class DisplayController:
    def __init__(self, env=None):
        self.env = env
        self.setting_service = setting_service
        self.thread = None
        self.is_running = False
        self.display = Display(self.setting_service.get_setting('DISPLAY'))
        self.update_interval = self.setting_service.get_setting('UPDATE_INTERVAL')
        self.poll_interval = 10
        self.current_app = self.refresh_current_app()


    def start(self):
        self.update()
        if not self.thread or not self.thread.is_alive():
            self.is_running = True
            self.thread = threading.Thread(target=self.run, daemon=True)
            self.thread.start()

    def update(self):
        if self.env == 'production':
            self.refresh_current_app()
            image = self.current_app.get_image()
            if image:
                self.display.show_image(image)
        
    def run(self):
        counter = 0
        while self.is_running:
            try:
                counter += self.poll_interval
                if counter >= self.update_interval:
                    self.update()
                    counter = 0
            except Exception as e:
                logger.error(str(e))
            time.sleep(self.poll_interval)


    def __get_app_map(self):
        app_map = {
            'photo': ImageApp(),
            'art': ImageApp(),
            'music': ImageApp()
        }
        return app_map
    
    def refresh_current_app(self):
        current_app_setting = self.setting_service.get_setting('MODE')
        app_map = self.__get_app_map()
        return app_map.get(current_app_setting, ImageApp())

    