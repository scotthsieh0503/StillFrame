from flask import Blueprint

settings_bp = Blueprint('settings', __name__)

from . import api  # Import the routes