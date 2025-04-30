from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship


from app.connectors.database.postgresql import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    motor = Column(String, nullable=False)
    number_of_doors = Column(Integer, nullable=False)

    brand_id = Column(Integer, ForeignKey("brands.id"))
    color_id = Column(Integer, ForeignKey("colors.id"))
    fuel_type_id = Column(Integer, ForeignKey("fuel_types.id"))

    brand = relationship("Brand", back_populates="vehicles")
    color = relationship("Color", back_populates="vehicles")
    fuel_type = relationship("FuelType", back_populates="vehicles")
