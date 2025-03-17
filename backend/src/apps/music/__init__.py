from flask import Blueprint

music_bp = Blueprint('music', __name__)

from . import api  # Import the routes