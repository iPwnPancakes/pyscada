from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_app.models.Tag import Tag

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.jinja2', test='asdf')

@app.route('/test')
def test():
    db = SQLAlchemy(model_class=Tag)
    return db.session.query(Tag).all()
