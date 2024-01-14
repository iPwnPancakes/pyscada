from typing import List

from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from flask_app.models.Base import Base


class Device(Base):
    __tablename__ = 'devices'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)

    tags: Mapped[List["Tag"]] = relationship("Tag", back_populates="device")

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name
        }
