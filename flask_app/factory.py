import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_app.lib.mqtt.Client import Client
from flask_app.models.Base import Base
from flask_app.routes.http.device import routes as device_routes
from flask_app.routes.http.modbus import routes as modbus_routes
from flask_app.routes.http.tag import routes as tag_routes
from flask_app.routes.http.ui import routes as ui_routes
from flask_app.routes.mqtt.device import routes as mqtt_device_routes


def create_mqtt_app() -> Client:
    mqtt_client = Client(
        host=os.environ['MQTT_HOST'],
        port=int(os.environ['MQTT_PORT']),
    )

    mqtt_client.register_routes(mqtt_device_routes)

    return mqtt_client


def create_flask_app() -> Flask:
    app = Flask(__name__)
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
