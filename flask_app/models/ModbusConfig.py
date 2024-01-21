from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from flask_app.models.DeviceTagConfig import DeviceTagConfig


class ModbusConfig(DeviceTagConfig):
    __tablename__ = 'modbus_config'

    id: Mapped[int] = mapped_column(ForeignKey('device_tag_config.id'), primary_key=True)
    slave_id: Mapped[int]
    register: Mapped[int]

    __mapper_args__ = {
        'polymorphic_identity': 1
    }

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'slave_id': self.slave_id,
            'register': self.register
        }
