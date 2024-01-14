from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class DeviceTagConfig(Base):
    __tablename__ = 'device_tag_config'

    id = Column(Integer, primary_key=True)
    device_id = Column(Integer, nullable=False)
    tag_id = Column(Integer, nullable=False)
    protocol_id = Column(Integer, nullable=False)  # Polymorphic association
    protocol_config_id = Column(Integer, nullable=False)  # Polymorphic association

    # Relationships
    device = relationship("Device", back_populates="device_tag_config")
    tag = relationship("Tag", back_populates="device_tag_config")
    protocol = relationship("Protocol", back_populates="device_tag_config")

    __mapper_args__ = {
        'polymorphic_on': protocol_id
    }
