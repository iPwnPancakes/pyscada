import os
from datetime import datetime

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
                    tag.value_int = value
                    session.commit()
                    print(f'Read Tag: \"{tag.name}\" Value: {value}')
                except Exception as e:
                    print(f'Error reading tag: \"{tag.name}\"')
                    print(e)

        self.last_run = datetime.now()
        print('ran')
