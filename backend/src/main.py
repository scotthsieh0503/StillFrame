import os

from flask import Flask, jsonify
from flask_cors import CORS
from .apps.image import image_bp
from .apps.settings import settings_bp
from .display.display_controller import DisplayController
from .apps.settings import services as settings_service

# create and configure the app
def create_app(test_config=None):
    settings = settings_service.get_settings()
    app = Flask(__name__, instance_relative_config=True)

    # Enable CORS
    CORS(app)

    # Determine the configuration to use
    env = os.getenv('FLASK_ENV', 'production')

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
    app.register_blueprint(settings_bp, url_prefix='/api/setting')

    #setting up the display
    if env == 'production':
        controller = DisplayController(env=env, settings=settings_service)
        controller.start()

    return app