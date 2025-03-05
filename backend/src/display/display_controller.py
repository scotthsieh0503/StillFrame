from .display import Display
import threading
import time

class DisplayController:
    def __init__(self, display:Display, app):
        self.thread = None
        self.is_running = False
        self.display = display
        self.update_interval = 60
        self.app = app

    def start(self):
        if not self.thread or not self.thread.is_alive():
            self.thread = threading.Thread(target=self.run, daemon=True)
            self.thread.start()
            self.thread_is_running = True


    def update(self):
        image = self.app.get_image()
        self.display.show_image(image)

    def run(self):
        while self.is_running:
            try:
             self.update()
             time.sleep(self.update_interval)
            except Exception as e:
                if self.thread:
                    self.is_running = False
                    self.thread.join()
            

