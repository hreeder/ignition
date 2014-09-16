import os

from flask import Flask
from flask.ext.assets import Bundle, Environment
from flask.ext.login import LoginManager

app = Flask(__name__)

# Load the app config
app.config.from_object("config.Config")

assets = Environment(app)

login = LoginManager()
login.init_app(app)

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
        'bootswatch/sandstone/bootstrap.css',
        'css/ignition.css',
        output='css_all.css'
    )
)

from manager.views import core
