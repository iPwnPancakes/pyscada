from sqlalchemy import Column, String, Integer, Float, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)

    value_int = Column(Integer, nullable=True)
    value_float = Column(Float, nullable=True)
    value_string = Column(String, nullable=True)
    value_bool = Column(Boolean, nullable=True)

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'value_int': self.value_int,
            'value_float': self.value_float,
            'value_string': self.value_string,
            'value_bool': self.value_bool
        }
