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
    mileage = Column(Float, nullable=False)

    status_id = Column(Integer, ForeignKey("status.id"))
    brand_id = Column(Integer, ForeignKey("brands.id"))
    color_id = Column(Integer, ForeignKey("colors.id"))
    fuel_type_id = Column(Integer, ForeignKey("fuel_types.id"))

    status = relationship("Status", back_populates="vehicles")
    brand = relationship("Brand", back_populates="vehicles")
    color = relationship("Color", back_populates="vehicles")
    fuel_type = relationship("FuelType", back_populates="vehicles")

    def to_dict(self):
        return {
            "id": self.id,
            "model": self.model,
            "year": self.year,
            "price": self.price,
            "motor": self.motor,
            "number_of_doors": self.number_of_doors,
            "mileage": self.mileage,
            "brand_id": self.brand_id,
            "brand": self.brand.name,
            "color_id": self.color_id,
            "color": self.color.name,
            "fuel_type_id": self.fuel_type_id,
            "fuel_type": self.fuel_type.name,
            "status_id": self.status_id,
            "status": self.status.name,
        }
