from flask import Flask
from config import Config

app = Flask(__name__)

app.debug = True

from view import path

app.register_blueprint(path)

app.jinja_env.auto_reload = True

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.run("0.0.0.0", Config.port)
