import os

from flask import Flask
from flask.ext.assets import Bundle, Environment
from flask.ext.bcrypt import Bcrypt
from flask.ext.login import LoginManager, current_user
from flask.ext.migrate import Migrate
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Load the app config
app.config.from_object("config.Config")

assets = Environment(app)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
migrate = Migrate(app, db)

# Load Blueprints
from manager.core import core
from manager.dns import dns

app.register_blueprint(core)
app.register_blueprint(dns, url_prefix="/dns")

# Configure flask-login
login_manager.login_view = "core.login"

# Asset Management
assets.load_path = [
    os.path.join(os.path.dirname(__file__), 'static'),
    os.path.join(os.path.dirname(__file__), 'static', 'bower_components')
]

assets.register(
    'js_all',
    Bundle(
        'jquery/dist/jquery.min.js',
        'bootstrap/dist/js/bootstrap.min.js',
        output='js_all.js'
    )
)

assets.register(
    'css_all',
    Bundle(
        'bootstrap/dist/css/bootstrap.css',
        output='css_all.css'
    )
)
