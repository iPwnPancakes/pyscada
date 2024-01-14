from sqlalchemy import Column, BIGINT, INTEGER

from flask_app.models import DeviceTagConfig


class ModbusConfig(DeviceTagConfig):
    __tablename__ = 'modbus_config'

    id = Column(BIGINT, primary_key=True)
    slave_id = Column(INTEGER, nullable=False)
    address = Column(INTEGER, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 1
    }
