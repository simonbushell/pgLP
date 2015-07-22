import os

from flask import Flask

from settings import ProdConfig
from extensions import db, debug_toolbar


def create_app(config_object=ProdConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app

def register_extensions(app):
    db.init_app(app)
    debug_toolbar.init_app(app)
    return None
