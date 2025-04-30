from app.connectors.database.postgresql import Base, engine
from app.utils.postgresql import ALL_POSTGRESQL_MODELS


for model in ALL_POSTGRESQL_MODELS:
    print(f"Creating table for model: {model.__name__}")

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")
