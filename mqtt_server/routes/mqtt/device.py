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

    print(f'Received data from topic {message.topic}: {data}')

    engine = create_engine(os.environ['SQLALCHEMY_DATABASE_URI'])
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get ID from topic
    topic_parts = message.topic.split('/')
    device_id = topic_parts[1]

    # Get device from database
    tags = session.query(Tag).filter(Tag.device_id == device_id).all()
    for tag in tags:
        modbus_config: ModbusConfig|None = tag.get_config(ModbusConfig)
        mqtt_config: MqttConfig|None = tag.get_config(MqttConfig)

        if modbus_config and mqtt_config:
            mqtt_address = mqtt_config.address
            if mqtt_address in data:
                print(f'Writing value: {data[mqtt_address]} to register: {modbus_config.register}')
                write_modbus(tag.device, modbus_config, data[mqtt_address])

    session.commit()
    session.close()


engine = create_engine(os.environ['SQLALCHEMY_DATABASE_URI'])
Session = sessionmaker(bind=engine)
session = Session()

routes = Router()

devices = session.query(Device).all()
for device in devices:
    routes.register(f'device/{device.id}', parse_device_message)
    print(f'Registered device {device.id} to topic device/{device.id}')
session.close()
