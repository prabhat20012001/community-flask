from flask import Blueprint

# ----------- Instiantiate Blueprint ----------- #
chat = Blueprint('chat', __name__, template_folder='templates')

from .routes import *