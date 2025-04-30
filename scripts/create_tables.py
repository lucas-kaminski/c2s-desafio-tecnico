from app.connectors.database.postgresql import Base, engine
from app.models.brand import Brand
from app.models.color import Color
from app.models.fuel_type import FuelType
from app.models.vehicle import Vehicle

ALL_MODELS = [Brand, Color, FuelType, Vehicle]


for model in ALL_MODELS:
    print(f"Creating table for model: {model.__name__}")

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")
