#Extensions initialised in the app factory

from flask_debugtoolbar import DebugToolbarExtension
debug_toolbar = DebugToolbarExtension()

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
