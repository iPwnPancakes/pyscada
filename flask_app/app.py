import os

from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from flask_app.models.Tag import Tag

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']

db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return render_template('index.jinja2', test='asdf')


@app.route('/tags', methods=['GET'])
def all_tags():
    tags = db.session.query(Tag).all()

    return jsonify([tag.to_dict() for tag in tags])


@app.route('/tags', methods=['POST'])
def make_tag():
    tag = Tag(name=request.form['name'])

    db.session.add(tag)
    db.session.commit()

    return jsonify("Success")


@app.route('/tags/<id>', methods=['DELETE'])
def delete_tag(id):
    tag = db.session.query(Tag).filter(Tag.id == id).first()

    db.session.delete(tag)
    db.session.commit()

    return jsonify("Success")
