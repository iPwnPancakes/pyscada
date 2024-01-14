from flask import Blueprint, request, jsonify, current_app

from flask_app.models.Tag import Tag

routes = Blueprint('tag_routes', __name__)


@routes.route('/tags', methods=['GET'])
def all_tags():
    db = current_app.db
    tags = db.session.query(Tag).all()
    return jsonify([tag.to_dict() for tag in tags])


@routes.route('/tags', methods=['POST'])
def make_tag():
    db = current_app.db
    tag = Tag(name=request.form.get('name'))

    db.session.add(tag)
    db.session.commit()

    return jsonify("Success")


@routes.route('/tags/<id>', methods=['DELETE'])
def delete_tag(id):
    db = current_app.db
    tag = db.session.query(Tag).filter(Tag.id == id).first()

    db.session.delete(tag)
    db.session.commit()

    return jsonify("Success")
