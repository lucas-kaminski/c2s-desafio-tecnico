from app.connectors.database.postgresql import SessionLocal

from app.models.vehicle import Vehicle
from app.models.brand import Brand
from app.models.color import Color
from app.models.fuel_type import FuelType

ALL_POSTGRESQL_MODELS = [Vehicle, Brand, Color, FuelType]


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def save_to_database(session, instance):
    try:
        session.add(instance)
        session.commit()
        session.refresh(instance)
        return instance
    except Exception as e:
        session.rollback()
        raise e
