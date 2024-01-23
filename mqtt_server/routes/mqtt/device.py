import json
import os

from paho.mqtt.client import MQTTMessage
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from mqtt_server.lib.mqtt.Router import Router
from flask_app.models.Device import Device
from flask_app.models.MqttConfig import MqttConfig
from flask_app.models.Tag import Tag
from flask_app.models.ModbusConfig import ModbusConfig
from flask_app.lib.modbus.Write import write_modbus
from flask_app.models.DeviceTagConfig import DeviceTagConfig


def parse_device_message(message: MQTTMessage):
    try:
        data = json.loads(message.payload)
    except json.JSONDecodeError:
        print(f'Received invalid JSON from topic {message.topic}')
        return

    engine = create_engine(os.environ['SQLALCHEMY_DATABASE_URI'])
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get ID from topic
    topic_parts = message.topic.split('/')
    device_id = topic_parts[1]

    # Get device from database
    tags = session.query(Tag).filter(Tag.device_id == device_id).all()
    for tag in tags:
        modbus_config: ModbusConfig|None = get_config(tag, ModbusConfig)
        mqtt_config: MqttConfig|None = get_config(tag, MqttConfig)

        if modbus_config is not None and mqtt_config is not None:
            register = mqtt_config.address
            if register in data:
                write_modbus(tag.device, modbus_config, data[register])

    session.commit()
    session.close()


def get_config(tag: Tag, config: type[DeviceTagConfig]) -> DeviceTagConfig | None:
    for tag_config in tag.device_configs:
        if isinstance(tag_config, config):
            return tag_config


engine = create_engine(os.environ['SQLALCHEMY_DATABASE_URI'])
Session = sessionmaker(bind=engine)
session = Session()

routes = Router()

devices = session.query(Device).all()
for device in devices:
    routes.register(f'device/{device.id}', parse_device_message)
session.close()
