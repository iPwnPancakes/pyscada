import os
from datetime import datetime

from requests import post
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from flask_app.lib.modbus.ReadDriver import read_modbus
from flask_app.models.ModbusConfig import ModbusConfig
from flask_app.models.MqttConfig import MqttConfig  # noqa
from flask_app.models.Tag import Tag
from timer_process.utils.Job import Job


class PollTagModbusValues(Job):
    def __init__(self, schedule: str):
        super().__init__(schedule=schedule)

    def run(self):
        engine = create_engine(os.environ['SQLALCHEMY_DATABASE_URI'])
        Session = sessionmaker(bind=engine)
        session = Session()

        tags = session.query(Tag).all()
        for tag in tags:
            modbus_config = tag.get_config(ModbusConfig)
            if modbus_config:
                try:
                    value = read_modbus(tag.device, modbus_config)
                    print(f'Read Tag: \"{tag.name}\" Value: {value}')

                    self.send_value_to_api(tag, value)
                except Exception as e:
                    print(f'Error reading tag: \"{tag.name}\"')
                    print(e)

        self.last_run = datetime.now()

    def send_value_to_api(self, tag: Tag, value: int) -> None:
        post(f'{os.environ["SCADA_API_URL"]}/tags/{tag.id}/value', json={'value': value})
