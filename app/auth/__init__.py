from flask import Blueprint

# ----------- Instiantiate Blueprint ----------- #
auth = Blueprint('auth', __name__, template_folder='templates')

from .routes import *