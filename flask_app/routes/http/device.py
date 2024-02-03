from flask import Blueprint, request, jsonify, current_app
from flask_cors import cross_origin

from flask_app.models.Device import Device
from flask_app.models.ModbusConfig import ModbusConfig
from flask_app.models.MqttConfig import MqttConfig
from flask_app.models.NetworkConfiguration import NetworkConfiguration
from flask_app.models.Tag import Tag

routes = Blueprint('device_routes', __name__)


@routes.route('/devices/<id>', methods=['GET'])
@cross_origin()
def get_complete_device_info(id):
    db = current_app.db
    device = db.session.query(Device).filter(Device.id == id).first()
    return jsonify(device.to_complete_dict())


@routes.route('/devices', methods=['GET'])
@cross_origin()
def all_devices():
    db = current_app.db
    devices = db.session.query(Device).all()
    return jsonify([device.to_dict() for device in devices])


@routes.route('/devices', methods=['POST'])
@cross_origin()
def make_device():
    db = current_app.db

    name = request.json.get('name')

    device = Device(name=name)

    db.session.add(device)
    db.session.commit()

    return jsonify("Success")


@routes.route('/devices/<id>', methods=['DELETE'])
def delete_device(id):
    db = current_app.db
    device = db.session.query(Device).filter(Device.id == id).first()

    db.session.delete(device)
    db.session.commit()

    return jsonify("Success")


@routes.route('/devices/<device_id>/tags', methods=['GET'])
def get_device_tags(device_id):
    db = current_app.db
    device = db.session.query(Device).filter(Device.id == device_id).first()

    return jsonify([tag.to_dict() for tag in device.tags])


@routes.route('/devices/<device_id>/tags/<tag_id>', methods=['GET'])
def get_device_tag(device_id, tag_id):
    db = current_app.db
    tag = db.session.query(Tag).filter(Tag.device_id == device_id, Tag.id == tag_id).first()

    return jsonify(tag.to_dict())


@routes.route('/devices/<device_id>/tags', methods=['POST'])
def add_tag_to_device(device_id):
    db = current_app.db

    device = db.session.query(Device).filter(Device.id == device_id).first()

    tag = Tag(name=request.form.get('name'), device_id=device_id)

    db.session.add(tag)
    device.tags.append(tag)
    db.session.commit()

    return jsonify("Success")


@routes.route('/devices/<device_id>/tags/<tag_id>/config', methods=['GET'])
def get_tag_device_config(device_id, tag_id):
    db = current_app.db

    tag = db.session.query(Tag).filter(Tag.device_id == device_id, Tag.id == tag_id).first()

    return jsonify([config.to_dict() for config in tag.device_configs])


@routes.route('/devices/<device_id>/tags/<tag_id>/config', methods=['POST'])
def create_tag_device_config(device_id, tag_id):
    db = current_app.db

    config = None

    if int(request.form.get('protocol_id')) == 1:
        config = ModbusConfig(
            device_id=device_id,
            tag_id=tag_id,
            protocol_id=request.form.get('protocol_id'),
            slave_id=request.form.get('slave_id'),
            register=request.form.get('address'),
        )
    elif int(request.form.get('protocol_id')) == 2:
        config = MqttConfig(
            device_id=device_id,
            tag_id=tag_id,
            protocol_id=request.form.get('protocol_id'),
            address=request.form.get('address'),
        )

    db.session.add(config)
    db.session.commit()

    return jsonify(config.to_dict())


@routes.route('/devices/<device_id>/network', methods=['GET'])
def get_device_network_config(device_id):
    db = current_app.db

    networkConfig = db.session.query(NetworkConfiguration).filter(NetworkConfiguration.device_id == device_id).first()

    return jsonify(networkConfig.to_dict())


@routes.route('/devices/<device_id>/network', methods=['POST'])
def create_device_network_config(device_id):
    db = current_app.db

    networkConfig = NetworkConfiguration(
        device_id=device_id,
        ip_address=request.form.get('ip_address'),
        port=request.form.get('port')
    )

    db.session.add(networkConfig)
    db.session.commit()

    return jsonify(networkConfig.to_dict())
