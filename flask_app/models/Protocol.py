from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship, Mapped

from flask_app.models.Base import Base


class Protocol(Base):
    __tablename__ = 'protocol'

    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String)
    description: Mapped[str] = Column(String)

    tag_configs: Mapped["DeviceTagConfig"] = relationship(back_populates="protocol")

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }
