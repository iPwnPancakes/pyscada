from flask import Blueprint, request, jsonify, current_app

from flask_app.lib.modbus.ReadDriver import Read
from flask_app.models.Device import Device
from flask_app.models.Tag import Tag

routes = Blueprint('modbus_routes', __name__)


@routes.route('/modbus/read', methods=['GET'])
def read_modbus():
    db = current_app.db

    device_id = request.args.get('device_id')
    tag_id = request.args.get('tag_id')

    device = db.session.query(Device).filter(Device.id == device_id).first()
    tag = db.session.query(Tag).filter(Tag.device_id == device_id, Tag.id == tag_id).first()

    Read().read(device, tag)

    return jsonify("Success")
