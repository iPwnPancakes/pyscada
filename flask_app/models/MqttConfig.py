from sqlalchemy.orm import Mapped, mapped_column

from flask_app.models.DeviceTagConfig import DeviceTagConfig


class MqttConfig(DeviceTagConfig):
    __tablename__ = 'mqtt_configs'

    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str]

    __mapper_args__ = {
        'polymorphic_identity': 2
    }

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'address': self.address
        }
