from flask import Blueprint, request, jsonify, current_app

from flask_app.models.Device import Device

routes = Blueprint('device_routes', __name__)


@routes.route('/devices', methods=['GET'])
def all_devices():
    db = current_app.db
    devices = db.session.query(Device).all()
    return jsonify([device.to_dict() for device in devices])


@routes.route('/devices', methods=['POST'])
def make_tag():
    db = current_app.db

    name = request.form.get('name')

    device = Device(name=name)

    db.session.add(device)
    db.session.commit()

    return jsonify("Success")


@routes.route('/device/<id>', methods=['DELETE'])
def delete_tag(id):
    db = current_app.db
    device = db.session.query(Device).filter(Device.id == id).first()

    db.session.delete(device)
    db.session.commit()

    return jsonify("Success")
