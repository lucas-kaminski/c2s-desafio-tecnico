from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.connectors.database.postgresql import Base


class Brand(Base):
    __tablename__ = "brands"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    vehicles = relationship("Vehicle", back_populates="brand")
