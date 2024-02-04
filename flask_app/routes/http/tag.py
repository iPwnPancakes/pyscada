from flask import Blueprint, request, jsonify, current_app
from flask_cors import cross_origin

from flask_app.models.Tag import Tag
from flask_app.models.DeviceTagConfig import DeviceTagConfig

routes = Blueprint('tag_routes', __name__)


@routes.route('/tags', methods=['GET'])
def all_tags():
    db = current_app.db
    tags = db.session.query(Tag).all()
    return jsonify([tag.to_dict() for tag in tags])


@routes.route('/tags', methods=['POST'])
def make_tag():
    db = current_app.db

    name = request.form.get('name')
    device_id = request.form.get('device_id')

    tag = Tag(name=name, device_id=device_id)

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

@routes.route('/configs/<config_id>', methods=['GET'])
@cross_origin()
def get_tag_config(config_id):
    db = current_app.db
    config: DeviceTagConfig = db.session.query(DeviceTagConfig).filter(DeviceTagConfig.id == config_id).first()

    if config is None:
        return jsonify("Config not found"), 404

    return jsonify(config.to_dict())
