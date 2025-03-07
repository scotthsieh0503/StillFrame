import os

from flask import Flask, jsonify
from flask_cors import CORS
from .apps.image import image_bp
from .config import Config
from .display.display import Display
from .display.display_controller import DisplayController
from .apps.image.image_app import ImageApp


 # create and configure the app
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    # Enable CORS
    CORS(app)

    # load the instance config, if it exists, when not testing
    app.config.from_object(Config)
    app.logger

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def home():
        return jsonify({"message": "Hello from StillFrame!"})

    # Import the blueprint and register it
    app.register_blueprint(image_bp, url_prefix='/api/image')

    #init photo app
    photo_app = ImageApp(app.config)
    #setting up the display
    display = Display()
    controller = DisplayController(display, photo_app)
    controller.start()

    return app