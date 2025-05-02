from app.connectors.database.postgresql import engine
from app.utils.postgresql import ALL_POSTGRESQL_MODELS

for model in ALL_POSTGRESQL_MODELS:
    print(f"Dropping table for model: {model.__name__}")
    model.__table__.drop(engine)
