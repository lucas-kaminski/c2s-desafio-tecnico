import logging

from app.connectors.database.postgresql import Base, engine
from app.utils.postgresql import ALL_POSTGRESQL_MODELS

logger = logging.getLogger(__name__)

for model in ALL_POSTGRESQL_MODELS:
    logger.info(f"Creating table for model: {model.__name__}")

Base.metadata.create_all(bind=engine)

logger.info("All tables created successfully.")
