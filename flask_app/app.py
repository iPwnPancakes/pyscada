import os

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from flask_app.models.Base import Base
from flask_app.routes.http.device import routes as device_routes
from flask_app.routes.http.modbus import routes as modbus_routes
from flask_app.routes.http.tag import routes as tag_routes

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']

with app.app_context():
    db = SQLAlchemy(model_class=Base)
    db.init_app(app)
    app.db = db

app.register_blueprint(tag_routes)
app.register_blueprint(device_routes)
app.register_blueprint(modbus_routes)


@app.route('/')
def hello_world():
    return render_template('index.jinja2', test='asdf')
