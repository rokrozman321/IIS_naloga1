# from flask import Flask

# app1 = Flask(__name__)

# from serve import app

from flask import Flask

from .routes import main

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    return app