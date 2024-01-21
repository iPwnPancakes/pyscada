from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from flask_app.models.Base import Base
from flask_app.models.Protocol import Protocol


class DeviceTagConfig(Base):
    __tablename__ = 'device_tag_config'

    id: Mapped[int] = mapped_column(primary_key=True)
    device_id: Mapped[int] = mapped_column(ForeignKey('devices.id'), nullable=False)
    tag_id: Mapped[int] = mapped_column(ForeignKey('tags.id'), nullable=False)
    protocol_id: Mapped[int] = mapped_column(ForeignKey('protocol.id'), nullable=False)  # Polymorphic association
    protocol_config_id: Mapped[int] = mapped_column(Integer, nullable=False)  # Polymorphic association

    # Relationships
    device: Mapped["Device"] = relationship(back_populates="configs")
    tag: Mapped["Tag"] = relationship(back_populates="device_tag_config")
    protocol: Mapped[Protocol] = relationship(back_populates="device_tag_configs")

    __mapper_args__ = {
        "polymorphic_identity": "device_tag_config",
        'polymorphic_on': 'protocol_id'
    }

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'device_id': self.device_id,
            'tag_id': self.tag_id,
            'protocol_id': self.protocol_id,
            'protocol_config_id': self.protocol_config_id
        }
