import json
import logging
import random

from app.connectors.external.brasilapi import BrasilAPI
from app.controllers.brands import select_all_brands
from app.models.brand import Brand
from app.models.color import Color
from app.models.fuel_type import FuelType
from app.models.status import Status
from app.models.vehicle import Vehicle
from app.utils.postgresql import get_session, save_to_database

logger = logging.getLogger(__name__)

db_session = next(get_session())

brasil_api = BrasilAPI()

years = list(range(2000, 2024))
price = list(range(10000, 200000, 1000))
motor = ["1.0", "1.4", "1.6", "2.0", "2.4", "3.0"]
number_of_doors = [2, 3, 4, 5]
mileage = list(range(0, 200000, 1000))

colors = []
with open("scripts/json/colors.json", "r", encoding="utf-8") as file:
    colors = json.load(file)
    for color in colors:
        color_instance = Color()
        color_instance.id = color["id"]
        color_instance.name = color["nome"]
        try:
            save_to_database(db_session, color_instance)
        except Exception as e:
            logger.error(f"Error saving color {color_instance.name}: {e}")

fuel_types = []
with open("scripts/json/fuel_types.json", "r", encoding="utf-8") as file:
    fuel_types = json.load(file)
    for fuel_type in fuel_types:
        fuel_type_instance = FuelType()
        fuel_type_instance.id = fuel_type["id"]
        fuel_type_instance.name = fuel_type["nome"]
        try:
            save_to_database(db_session, fuel_type_instance)
        except Exception as e:
            logger.error(f"Error saving fuel type {fuel_type_instance.name}: {e}")


statuses = []
with open("scripts/json/status.json", "r", encoding="utf-8") as file:
    statuses = json.load(file)
    for status in statuses:
        status_instance = Status()
        status_instance.id = status["id"]
        status_instance.name = status["nome"]
        try:
            save_to_database(db_session, status_instance)
        except Exception as e:
            logger.error(f"Error saving status {status_instance.name}: {e}")

all_brands = brasil_api.get_all_car_brands()
for brand in all_brands:
    brand_instance = Brand()
    brand_instance.id = brand["valor"]
    brand_instance.name = brand["nome"]
    try:
        save_to_database(db_session, brand_instance)
    except Exception as e:
        logger.error(f"Error saving brand {brand_instance.name}: {e}")

all_brands_in_db = select_all_brands(db_session)

logger.info(f"Total of brands inserted on database: {len(all_brands_in_db)}")

max_brands_must_be_inserted = input(
    "Enter the maximum number of brands to be inserted (0 for all): "
)
try:
    max_brands_must_be_inserted = int(max_brands_must_be_inserted)
except Exception:
    print("Invalid input. Using default value of 0 (all brands).")
    max_brands_must_be_inserted = 0

if max_brands_must_be_inserted > 0:
    all_brands_in_db = all_brands_in_db[:max_brands_must_be_inserted]

max_cars_per_brand: int = input(
    "Enter the maximum number of cars per brand (0 for all): "
)
try:
    max_cars_per_brand = int(max_cars_per_brand)
except Exception:
    print("Invalid input. Using default value of 0 (all cars).")
    max_cars_per_brand = 0


for brand in all_brands_in_db:
    all_cars_of_brand = brasil_api.get_all_cars_by_brand(brand.id)

    if max_cars_per_brand > 0:
        all_cars_of_brand = all_cars_of_brand[:max_cars_per_brand]

    for car in all_cars_of_brand:
        car_instance = Vehicle()

        car_instance.brand_id = brand.id

        car_instance.color_id = random.choice(colors)["id"]

        car_instance.fuel_type_id = random.choice(fuel_types)["id"]

        car_instance.model = car["modelo"]

        car_instance.year = random.choice(years)
        car_instance.price = random.choice(price)
        car_instance.motor = random.choice(motor)
        car_instance.number_of_doors = random.choice(number_of_doors)
        car_instance.mileage = random.choice(mileage)
        car_instance.status_id = random.choice(statuses)["id"]

        try:
            save_to_database(db_session, car_instance)
        except Exception as e:
            print(f"Error saving car {car_instance.model}: {e}")

    all_cars_of_brand_in_db = (
        db_session.query(Vehicle).filter_by(brand_id=brand.id).all()
    )
    logger.info(
        f"Total of cars inserted on database for brand {brand.name}: {len(all_cars_of_brand_in_db)}"
    )
