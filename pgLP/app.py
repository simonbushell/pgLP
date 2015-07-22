import os

from flask import Flask

from settings import ProdConfig
from extensions import db, debug_toolbar
from pgLP import public


def create_app(config_object=ProdConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    return app

def register_extensions(app):
    db.init_app(app)
    debug_toolbar.init_app(app)
    return None

def register_blueprints(app):
    app.register_blueprint(public.views.blueprint)
    return None