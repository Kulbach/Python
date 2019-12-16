from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_marshmallow import Marshmallow
from config import app_config

db = SQLAlchemy()
ma = Marshmallow()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    db.init_app(app)
    ma.init_app(app)
    app.config.from_object(app_config[os.getenv('FLASK_ENV')])

    #with app.app_context():
        #db.create_all()

    return app