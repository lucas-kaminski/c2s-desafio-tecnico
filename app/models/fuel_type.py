from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.connectors.database.postgresql import Base


class FuelType(Base):
    __tablename__ = "fuel_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    vehicles = relationship("Vehicle", back_populates="fuel_type")
