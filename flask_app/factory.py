import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from flask_app.models.Base import Base
from flask_app.routes.http.device import routes as device_routes
from flask_app.routes.http.modbus import routes as modbus_routes
from flask_app.routes.http.tag import routes as tag_routes
from flask_app.routes.http.ui import routes as ui_routes


def create_flask_app() -> Flask:
    app = Flask(__name__)
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']

    with app.app_context():
        db = SQLAlchemy(model_class=Base)
        db.init_app(app)
        app.db = db

    app.register_blueprint(ui_routes)
    app.register_blueprint(tag_routes)
    app.register_blueprint(device_routes)
    app.register_blueprint(modbus_routes)

    return app
