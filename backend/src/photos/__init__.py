from flask import Blueprint

photo_bp = Blueprint('photo', __name__)

from . import api  # Import the routes