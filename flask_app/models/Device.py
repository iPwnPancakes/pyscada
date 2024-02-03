from typing import List

from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from flask_app.models.Base import Base
from flask_app.models.DeviceTagConfig import DeviceTagConfig
from flask_app.models.NetworkConfiguration import NetworkConfiguration
from flask_app.models.Tag import Tag


class Device(Base):
    __tablename__ = 'devices'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String)

    tags: Mapped[List[Tag]] = relationship(back_populates="device")
    configs: Mapped[List[DeviceTagConfig]] = relationship(back_populates="device")
    network_config: Mapped[NetworkConfiguration] = relationship(back_populates="device")

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name
        }

    def to_complete_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'tags': [tag.to_complete_dict() for tag in self.tags],
            'configs': [config.to_dict() for config in self.configs],
            'network_config': self.network_config.to_dict() if self.network_config else None
        }
