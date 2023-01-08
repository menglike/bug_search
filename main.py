from flask import Flask

app = Flask(__name__)

app.debug = True

from view import path

app.register_blueprint(path)

app.jinja_env.auto_reload = True

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.run("127.0.0.1", 7777)
