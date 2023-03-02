from flask import Flask

from .routes import main

from .app import run_app

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    return app