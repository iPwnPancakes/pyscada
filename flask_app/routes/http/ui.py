from flask import Blueprint, render_template

routes = Blueprint('ui_routes', __name__)


@routes.route('/')
def hello_world():
    return render_template('index.jinja2', test='asdf')
