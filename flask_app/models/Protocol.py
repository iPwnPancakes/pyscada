from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Protocol(Base):
    __tablename__ = 'protocol'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }
