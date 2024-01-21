from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from flask_app.models.Base import Base


class NetworkConfiguration(Base):
    __tablename__ = 'device_network_configurations'

    id: Mapped[int] = mapped_column(primary_key=True)
    device_id: Mapped[int] = mapped_column(ForeignKey('devices.id'))
    ip_address: Mapped[str] = mapped_column()
    port: Mapped[int] = mapped_column()

    device: Mapped["Device"] = relationship(back_populates="network_config")

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'device_id': self.device_id,
            'ip_address': self.ip_address,
            'port': self.port
        }
