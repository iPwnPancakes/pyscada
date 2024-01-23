from typing import Optional, List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from flask_app.models.Base import Base
from flask_app.models.DeviceTagConfig import DeviceTagConfig


class Tag(Base):
    __tablename__ = 'tags'

    id: Mapped[int] = mapped_column(primary_key=True)
    device_id: Mapped[int] = mapped_column(ForeignKey('devices.id'))

    name: Mapped[str] = mapped_column()
    value_int: Mapped[Optional[int]] = mapped_column()
    value_float: Mapped[Optional[float]] = mapped_column()
    value_string: Mapped[Optional[str]] = mapped_column()
    value_bool: Mapped[Optional[bool]] = mapped_column()

    device: Mapped["Device"] = relationship(back_populates="tags")
    device_configs: Mapped[List[DeviceTagConfig]] = relationship(back_populates="tag")

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'device_id': self.device_id,
            'value_int': self.value_int,
            'value_float': self.value_float,
            'value_string': self.value_string,
            'value_bool': self.value_bool
        }
