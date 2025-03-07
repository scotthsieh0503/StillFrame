from .display import Display
import logging
import threading
import time
from ..apps.image.image_app import ImageApp

logger = logging.getLogger(__name__)

class DisplayController:
    def __init__(self, settings=None):
        self.thread = None
        self.is_running = False
        self.display = Display()
        self.update_interval = 60
        self.app = ImageApp(settings)

    def start(self):
        logger.info("starting")
        self.update()
        if not self.thread or not self.thread.is_alive():
            self.is_running = True
            self.thread = threading.Thread(target=self.run, daemon=True)
            self.thread.start()
            
    def update(self):
        logger.info("update image")
        image = self.app.get_image()
        self.display.show_image(image)
        
    def run(self):
        while self.is_running:
            try:
             self.update()
             time.sleep(self.update_interval)
            except Exception as e:
                logger.error(str(e))
                if self.thread:
                    self.is_running = False
                    self.thread.join()
            

