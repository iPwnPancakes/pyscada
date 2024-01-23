import json
import os

from paho.mqtt.client import MQTTMessage
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from flask_app.lib.mqtt.Router import Router
from flask_app.models.Device import Device
from flask_app.models.ModbusConfig import ModbusConfig
from flask_app.models.Tag import Tag


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
        if isinstance(tag.device_tag_config, ModbusConfig):
            register = str(tag.device_tag_config.register)
            if register in data:
                tag.value_int = data[register]

    session.commit()
    session.close()


engine = create_engine(os.environ['SQLALCHEMY_DATABASE_URI'])
Session = sessionmaker(bind=engine)
session = Session()

routes = Router()

devices = session.query(Device).all()
for device in devices:
    routes.register(f'device/{device.id}', parse_device_message)
session.close()
