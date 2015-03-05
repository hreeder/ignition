from flask import Blueprint

dns = Blueprint('dns', __name__, template_folder='templates')

from manager.dns import views
